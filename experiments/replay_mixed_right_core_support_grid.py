#!/usr/bin/env python3
"""Replay core tangent bounds in the original signed-height variables.

This does not import the author's source formulas or call an optimizer.
It checks the complete profile list, both Fourier branches, rational trial
points and all stored upper bounds. Geometric reference bounds are separate.
"""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/'notes/research_mixed_right_core_support.md'
AUTHOR = ROOT/'experiments/certify_mixed_right_core_support_grid.py'
SOURCE = ROOT/'repro/results/research-mixed-right-core-support-grid.json'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ar(value):
    value = F(value)
    return arb(value.numerator)/value.denominator


def taper(x, left, right):
    if x < left:
        return (x/left)**2
    if x > right:
        return ((F(1,2)-x)/(F(1,2)-right))**2
    return F(1)


def profile_key(p):
    return (p['e'], p['b'], p['c'], p['sig'],
            F(p['ylo']), F(p['yhi']), F(p['h']), p['name'])


def expected_profiles():
    expected = set()
    intervals = [(F(13,100), F(1,5)), (F(1,5), F(11,50)),
                 (F(11,50), F(1,4)), (F(1,4), F(2,5)), (F(2,5), F(1,2))]
    for e,b,c in ((0,0,0), (1,1,0), (0,0,1), (0,1,1), (1,0,1), (1,1,1)):
        if b == 0:
            for h in (F(-3,100), F(1,50)):
                expected.add((e,b,c,0,F(13,100),F(1,2),h,'all3'))
            continue
        for j,(lo,hi) in enumerate(intervals):
            points = {lo,hi} | {x for x in (F(11,50),F(1,4),F(2,5),F(9,20))
                                 if lo <= x <= hi}
            lower = min(taper(x,F(1,4),F(2,5)) for x in points)
            upper = max(taper(x,F(11,50),F(9,20)) for x in points)
            for selected, heights in (
                    (0, (-F(57,1000)*upper, -F(1,50)*lower)),
                    (1, (F(7,500)*lower, F(7,500)*upper))):
                for h in heights:
                    expected.add((e,b,c,selected,lo,hi,h,f'part{j}'))
        upper = taper(F(13,100), F(11,50), F(9,20))
        for selected, heights in ((0, (-F(57,1000)*upper,F(0))),
                                  (1, (F(0),F(7,500)*upper))):
            for h in heights:
                expected.add((e,b,c,selected,F(13,100),F(13,100),h,'small'))
    return expected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=320)
    parser.add_argument('--input', type=Path, default=SOURCE)
    parser.add_argument('--output', type=Path, default=ROOT/
                        'repro/results/research-mixed-right-core-support-grid-replay.json')
    args = parser.parse_args()
    assert args.precision >= 192
    ctx.prec = args.precision
    pi, ii = arb.pi(), acb(0,1)
    initial = {str(p.relative_to(ROOT)):sha(p) for p in (PROOF,AUTHOR)}
    input_hash, script_hash = sha(args.input), sha(__file__)
    data = json.loads(args.input.read_text())
    assert data['status'] == 'passed'
    assert data['proof_sha256'] == sha(PROOF)
    assert data['script_sha256'] == sha(AUTHOR)
    for name, digest in data['dependencies_sha256'].items():
        assert sha(ROOT/name) == digest, name
        initial[name] = digest
    profiles = data['profiles']
    assert len(profiles) == len({profile_key(p) for p in profiles}) == 75
    assert {profile_key(p) for p in profiles} == expected_profiles()

    def g(z):
        return (((-2*pi*ii*z).exp().polylog(2)-pi*pi/6)/(2*pi*ii)).real

    def gp(z):
        # Independent sine form, on the original strip 0<Re z<1.
        return ((2*(pi*z).sin()).log()+pi*ii*(acb(arb('0.5'))-z)).real

    def tangent(value, derivative, point, endpoints):
        return value + max((derivative*ar(x-point)).upper() for x in endpoints)

    supports = branches = endpoints = 0
    for p in profiles:
        e,b,c,selected,lo,hi,h,_ = profile_key(p)
        hp = max(h,F(0))
        assert len(p['grid']) == 10
        assert [F(v['k']) for v in p['grid']] == [F(-1,5)+F(j,20) for j in range(10)]
        for row in p['grid']:
            k, upper = F(row['k']), ar(row['upper'])
            assert {v['q'] for v in row['trials']} == {0,b}
            assert {v['q'] for v in row['endpoint_trials']} == {0,b}
            assert len(row['trials']) == len(row['endpoint_trials']) == len({0,b})
            for trial in row['trials']:
                q = trial['q']
                u,y = map(F,trial['point'])
                assert F(1,5) <= u < F(1,2) and lo <= y <= hi
                z, uz = acb(ar(y),ar(h)), acb(ar(y+u),ar(h))
                constant = pi*ar((b-q)*hp-b*selected*h)
                value = (g(acb(ar(F(1,2)+u))) + g(uz)
                         - (1+ar(F(q,2)))*g(z) - (2+e)*g(acb(ar(u)))
                         - 2*pi*ar(c*h*u) + constant-ar(k*y))
                du = ((2*(pi*ar(u)).cos()).log()+gp(uz)
                      -(2+e)*(2*(pi*ar(u)).sin()).log()-2*pi*ar(c*h))
                dy = gp(uz)-(1+ar(F(q,2)))*gp(z)-ar(k)
                bound = tangent(tangent(value,du,u,(F(1,5),F(1,2))),dy,y,(lo,hi))
                assert bound < upper, (profile_key(p),k,q,'core')
                branches += 1
            for trial in row['endpoint_trials']:
                q, y = trial['q'], F(trial['point'])
                assert lo <= y <= hi
                z = acb(ar(y),ar(h))
                value = (2*pi*ar(hp-c*h)-ar(F(q,2))*g(z)
                         +pi*ar((b-q)*hp-b*selected*h)-ar(k*y))
                dy = -ar(F(q,2))*gp(z)-ar(k)
                assert tangent(value,dy,y,(lo,hi)) < upper, (profile_key(p),k,q,'endpoint')
                endpoints += 1
            supports += 1
    assert supports == 750
    assert input_hash == sha(args.input) and script_hash == sha(__file__)
    assert all(sha(ROOT/p) == h for p,h in initial.items())
    result = {'status':'passed','precision_bits':args.precision,
              'source_profiles':75,'support_values':supports,
              'core_branch_bounds':branches,'endpoint_branch_bounds':endpoints,
              'input_sha256':input_hash,'script_sha256':script_hash,
              'proof_sha256':sha(PROOF),'dependencies':initial,
              'method':'Original signed-height dilogarithm and sine logarithmic derivative; independent profile enumeration and tangent bounds; no author import or optimization.',
              'scope':'All saved scalar source supports, including u=1. The reference-plane comparison requires its separate proof and certificate.'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('Replayed',supports,'support values,',branches,'core branches and',endpoints,'endpoint branches.')


if __name__ == '__main__':
    main()
