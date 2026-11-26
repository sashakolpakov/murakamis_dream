#!/usr/bin/env python3
"""Exact rational Bernstein bounds for isolated seams at all nonlow angles.

The phase lower bounds are inherited from the original-log scalar certificate.
This checker evaluates no new critical root or dilogarithm. All subsequent
coefficients and Bernstein comparisons use exact rational arithmetic.
"""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from math import comb
from pathlib import Path

from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_general_angle_seam_replacement.md'
BREAKS = tuple(map(F, ('1/10', '3/25', '11/50', '9/20', '1/2')))
PI_UPPER = F(355, 113)
LOSS = F(3, 1000)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def add(*polys):
    return tuple(sum((p[k] if k < len(p) else F(0)) for p in polys)
                 for k in range(max(map(len, polys))))


def scale(p, s):
    return tuple(s*v for v in p)


def multiply(p, q):
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i+j] += x*y
    return tuple(r)


def bernstein(p, a, b):
    """Degree-three Bernstein coefficients on [a,b], exactly."""
    assert len(p) <= 4
    power = [sum(p[k]*comb(k,j)*a**(k-j)*(b-a)**j
                 for k in range(j,len(p))) for j in range(4)]
    return tuple(sum(power[k]*F(comb(j,k),comb(3,k))
                     for k in range(j+1)) for j in range(4))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input', type=Path)
    ap.add_argument('--output', type=Path, default=ROOT /
                    'repro/results/research-mixed-general-angle-seam-replacement.json')
    args = ap.parse_args()
    ctx.prec = 400
    proof_hash, script_hash = sha(PROOF), sha(__file__)
    deps, records, primary = {}, {}, {}

    def bind(path, expected=None):
        if path not in deps:
            deps[path] = sha(ROOT/path)
        if expected is not None:
            assert deps[path] == expected, path
        return deps[path]

    def inherit(path):
        if path in records:
            return records[path]
        bind(path)
        record = json.loads((ROOT/path).read_text())
        records[path] = record
        nested = {}
        for field in ('dependencies', 'dependencies_sha256'):
            for key, value in record.get(field, {}).items():
                assert key not in nested or nested[key] == value
                nested[key] = value
                bind(key, value)
        for key in nested:
            if key.startswith('repro/results/') and key.endswith('.json'):
                inherit(key)
        return record

    def load(stem):
        path = 'repro/results/research-' + stem.replace('_','-') + '.json'
        record = inherit(path)
        assert record['status'] == 'passed'
        assert record['proof_sha256'] == bind('notes/research_'+stem+'.md')
        assert record['script_sha256'] == bind('experiments/check_'+stem+'.py')
        primary[path] = record
        return record

    real = load('mixed_low_endpoint_connector_lower')
    profiles = load('mixed_height_resolved_seam_sources')['profiles']
    acute = load('mixed_acute_gradient_height_transfer')
    vertices = load('mixed_seam_attenuation_vertices')
    deep = load('mixed_deep_low_half_region')
    assert real['scalar_comparisons'] == 64
    assert arb(PI_UPPER.numerator)/PI_UPPER.denominator > arb.pi()
    assert F(3,1000)-F(1,1000) == F(1,500)

    def ar(r):
        return arb(r.numerator)/r.denominator

    # Use rational floors of certified lower margins, checking each floor
    # against the full outward enclosure rather than its printed midpoint.
    floors = {}
    for row in real['comparisons']:
        ball = arb(row['margin_lower'])
        guess = F(str(float(ball.mid())))
        lower = F((guess*10**8).__floor__()-1,10**8)
        while not ar(lower) < ball:
            lower -= F(1,10**8)
        key = (tuple(row['types']), F(row['middle_real']),
               F(row['left_real']), F(row['right_real']))
        assert key not in floors
        floors[key] = lower
    expected = {(types,t,a,c) for types in itertools.product((0,1),repeat=3)
                for t in map(F,real['middle_real_intervals'][str(types[1])])
                for a,c in itertools.product((F(1,10),F(1,2)),repeat=2)}
    assert set(floors) == expected

    def profile_lines(name, selection):
        points = [(F(row['height']),F(row['upper'])) for row in profiles[name]]
        if name in ('A01','A11','B1'):
            points = [(x,y) for x,y in points if (x >= 0 if selection else x <= 0)]
        lines = []
        for (x,y),(z,w) in zip(points,points[1:]):
            slope = (w-y)/(z-x)
            lines.append((slope,y-slope*x))
        assert all(v[0] >= u[0] for u,v in zip(lines,lines[1:]))
        for x,y in points:
            assert max(m*x+b for m,b in lines) == y
        zero = next(y for x,y in points if x == 0)
        return lines, zero

    polynomial_cache = {}

    def side_polynomials(kind, selection, name, left, piece):
        key = kind,selection,name,left,piece
        if key in polynomial_cache:
            return polynomial_cache[key]
        lo,hi = BREAKS[piece:piece+2]
        cutoff_end = F(3,25) if selection else F(11,50)
        cut = ((F(1),) if lo >= cutoff_end else
               (-F(1,10)/(cutoff_end-F(1,10)),1/(cutoff_end-F(1,10))))
        assert lo >= cutoff_end or hi <= cutoff_end
        taper = (F(1),) if hi <= F(9,20) else (F(100),F(-400),F(400))
        factor = multiply(cut,taper)
        assert len(factor) <= 3
        coefficients = ((F(7,500),) if selection else
                        (F(-57,1000),) if kind else (F(-3,100),F(1,50)))
        common = scale((F(selection)-F(kind,4),F(kind,2)), PI_UPPER)
        lines,zero = profile_lines(name,selection)
        options = [(F(0),)]
        for coefficient in coefficients:
            h = scale(factor,coefficient)
            for physical_same in (False,True):
                cost = multiply(common,scale(h,1 if physical_same else 2))
                extra = ((1 if coefficient>0 else 0) if left else
                         (-1 if coefficient<0 else 0))
                if not physical_same:
                    extra += ((-1 if coefficient<0 else 0) if left else
                              (1 if coefficient>0 else 0))
                cost = add(cost,scale(h,PI_UPPER*extra/2))
                if physical_same:
                    options.extend(add(cost,scale(h,m),(b-zero,)) for m,b in lines)
                else:
                    options.append(cost)
        assert all(len(p) <= 4 for p in options)
        polynomial_cache[key] = options
        return options

    def interpolate(types,t,a,c):
        wa,wc=(a-F(1,10))/F(2,5),(c-F(1,10))/F(2,5)
        return sum(floors[types,t,x,y]*u*v for x,u in ((F(1,10),1-wa),(F(1,2),wa))
                   for y,v in ((F(1,10),1-wc),(F(1,2),wc)))

    def bounds(case, piece, address):
        alpha,beta,gamma,sl,sr,t = case
        i,j=piece
        a0,a1=BREAKS[i:i+2];c0,c1=BREAKS[j:j+2]
        for digit in address:
            assert digit in '0123'
            am,cm=(a0+a1)/2,(c0+c1)/2
            if int(digit)//2: a0=am
            else: a1=am
            if int(digit)%2: c0=cm
            else: c1=cm
        left = side_polynomials(alpha,sl,f'A{beta}{alpha}',True,i)
        right = side_polynomials(gamma,sr,f'B{gamma}',False,j)
        lc = list(zip(*(bernstein(p,a0,a1) for p in left)))
        rc = list(zip(*(bernstein(p,c0,c1) for p in right)))
        middle = PI_UPPER*(F(57,1000)*(1-t) if beta else F(3,200))
        upper = max(max(lc[k])+max(rc[l])+middle-
                    interpolate((alpha,beta,gamma),t,a0+(a1-a0)*F(k,3),
                                c0+(c1-c0)*F(l,3))
                    for k,l in itertools.product(range(4),repeat=2))
        return upper

    cases = [(a,b,c,sl,sr,t) for a,b,c in itertools.product((0,1),repeat=3)
             for sl,sr in itertools.product(range(a+1),range(c+1))
             for t in map(F,real['middle_real_intervals'][str(b)])]
    assert len(cases) == 36
    input_bytes = args.input.read_bytes() if args.input else None
    input_hash = hashlib.sha256(input_bytes).hexdigest() if input_bytes is not None else None
    old = json.loads(input_bytes) if input_bytes is not None else None
    if old:
        assert old['status'] == 'passed'
        assert old['proof_sha256'] == proof_hash and old['script_sha256'] == script_hash
        assert old['dependencies_sha256'] == deps
        assert len(old['domains']) == 36*16
    domains=[];accepted=0;maxdepth=0;largest=None

    def complete(addresses, prefix=''):
        if prefix in addresses:
            assert not any(a != prefix and a.startswith(prefix) for a in addresses)
            return
        assert any(a.startswith(prefix) for a in addresses),prefix
        for d in '0123': complete(addresses,prefix+d)

    for caseid,case in enumerate(cases):
        for i,j in itertools.product(range(4),repeat=2):
            position=caseid*16+i*4+j
            if old:
                saved=old['domains'][position]
                assert saved['case'] == [str(v) for v in case]
                assert saved['pieces'] == [i,j]
                addresses=[cell['address'] for cell in saved['cells']]
                assert len(addresses)==len(set(addresses))
                complete(set(addresses))
                stack=list(reversed(addresses))
            else: stack=['']
            cells=[]
            while stack:
                address=stack.pop()
                upper=bounds(case,(i,j),address)
                if upper <= -LOSS:
                    cells.append({'address':address,'upper':str(upper)})
                    accepted+=1;maxdepth=max(maxdepth,len(address))
                    largest=upper if largest is None else max(largest,upper)
                else:
                    assert not old,(case,(i,j),address,upper)
                    assert len(address)<12,(case,(i,j),address,upper)
                    stack.extend(address+d for d in '3210')
            complete({cell['address'] for cell in cells})
            domains.append({'case':[str(v) for v in case], 'pieces':[i,j], 'cells':cells})
    assert all(sha(ROOT/path)==digest for path,digest in deps.items())
    assert sha(PROOF)==proof_hash and sha(__file__)==script_hash
    result=dict(status='passed',arithmetic='exact rational Bernstein coefficients',
                typed_selection_cases=len(cases),initial_rectangles=len(domains),
                accepted_cells=accepted,maximum_depth=maxdepth,
                uniform_comparison_loss=str(LOSS),largest_bernstein_upper=str(largest),
                finite_region_loss='1/500',pi_upper=str(PI_UPPER),
                primary_records=len(primary),current_bindings=len(deps),domains=domains,
                phase_parameter_cover_cells=0,new_critical_roots=0,
                proof_sha256=proof_hash,script_sha256=script_hash,dependencies_sha256=deps,
                scope='Original independent seams with every adjacent nonseam real coordinate in [.1,.5]. Arbitrary permitted heights, selections and inner nonseam variables. No adjacent-seam or whole-period theorem.')
    if args.input:
        assert sha(args.input) == input_hash
        result['input_sha256'] = input_hash
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',len(cases),'cases;',accepted,'rational cells; worst',float(largest),flush=True)


if __name__ == '__main__':
    main()
