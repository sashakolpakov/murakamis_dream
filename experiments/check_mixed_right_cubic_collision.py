#!/usr/bin/env python3
"""Fixed exact cubic collision/lift identities and outward root disks.

No root proposal, parameter search, source-cell cover, or finite-source
asymptotic is performed. Analytic continuation is proved in the note.
"""
import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_right_cubic_collision.md'
ARCHIVE = 'repro/diagnostics/2026-11-05-right-cubic-collision/'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=320)
    parser.add_argument('--output', type=Path, default=ROOT /
                        'repro/results/research-mixed-right-cubic-collision.json')
    args = parser.parse_args()
    assert args.precision >= 128
    ctx.prec = args.precision
    proof_hash, script_hash = sha(PROOF), sha(__file__)
    dependencies, visited, primary = {}, set(), {}

    def bind(path, expected=None):
        digest = sha(ROOT / path)
        if path in dependencies:
            assert dependencies[path] == digest, path
        dependencies[path] = digest
        if expected is not None:
            assert digest == expected, path
        return digest

    def inherit(path):
        data = (ROOT / path).read_bytes()
        bind(path, hashlib.sha256(data).hexdigest())
        record = json.loads(data)
        if path in visited:
            return record
        visited.add(path)
        bindings = {}
        for field in ('dependencies', 'dependencies_sha256'):
            for name, digest in record.get(field, {}).items():
                if name in bindings:
                    assert bindings[name] == digest, (path, name)
                bindings[name] = digest
                bind(name, digest)
        for name in bindings:
            if name.startswith('repro/results/') and name.endswith('.json'):
                inherit(name)
        return record

    for stem, count in (('mixed_closed_cotangent_roots', 13),
                        ('mixed_all_real_conditional_packet', 15),
                        ('lower_half_factorial_continuation', 15)):
        rp = f'repro/results/research-{stem.replace("_", "-")}.json'
        record = inherit(rp)
        assert record['status'] == 'passed', rp
        assert record['exact_identity_count'] == count, rp
        assert record['proof_sha256'] == bind(f'notes/research_{stem}.md')
        assert record['script_sha256'] == bind(f'experiments/check_{stem}.py')
        primary[rp] = record
    witness_path = ARCHIVE + 'fixed_witnesses.json'
    bind(witness_path)
    bind(ARCHIVE + 'README.md')
    witness = json.loads((ROOT / witness_path).read_bytes())

    identities, comparisons = [], []

    def zero(name, expression):
        assert sp.cancel(sp.expand(expression)) == 0, name
        identities.append(name)

    def check(name, statement):
        assert statement, name
        comparisons.append(name)

    def ar(x):
        x = sp.Rational(x)
        return arb(int(x.p))/int(x.q)

    p, q, z, v = sp.symbols('p q z v', real=True)
    f = sp.expand((z+sp.I)*(z+p)*(z+q)-2*sp.I*(p-sp.I)*(q+sp.I))
    ca, cb, cc = p+q+sp.I, p*q+sp.I*(p+q), 2*(p-q)-sp.I*(p*q+2)
    zero('original cubic coefficients', f-(z**3+ca*z*z+cb*z+cc))
    zero('local exponentiated gradient',
         (z+sp.I)*(z+p)*(z+q)/(2*sp.I*(p-sp.I)*(q+sp.I))-1
         -f/(2*sp.I*(p-sp.I)*(q+sp.I)))
    disc = sp.expand(sp.discriminant(f, z))
    dr, di = sp.re(disc), sp.im(disc)
    W = (81*p**16+34412*p**14+4632744*p**12+276067068*p**10
         +7895210226*p**8+107074960628*p**6+551742302000*p**4
         +65754674660*p**2-389141071067)
    A = (24*p**12+11849*p**10+1152259*p**8+36800794*p**6
         +392808686*p**4+110330813*p**2-252846825)
    B = (-1271*p**11-125181*p**9-2725502*p**7-5163890*p**5
         +125665653*p**3+134257263*p)
    zero('real discriminant elimination', sp.resultant(dr, di, q)+256*(p*p+1)**5*W)
    zero('nonzero linear subresultant', sp.subresultants(dr, di, q)[-2]-16*(p*p+1)**3*(A*q+B))
    for name, part in (('real', dr), ('imaginary', di)):
        zero(name+' discriminant vanishes modulo W',
             sp.rem(sp.together(part.subs(q, -B/A)).as_numer_denom()[0], W, p))
    lo, hi = map(sp.Rational, witness['p_isolation'])
    check('positive isolating endpoints', 0 < lo < hi)
    check('lower W sign', W.subs(p, lo) < 0)
    check('upper W sign', W.subs(p, hi) > 0)
    check('strictly positive derivative coefficients', all(c > 0 for _, c in sp.Poly(sp.diff(W, p), p).terms()))
    pp = ar((lo+hi)/2)+arb(0, ar((hi-lo)/2))

    def ev(poly):
        out = arb(0)
        for coefficient in sp.Poly(poly, p).all_coeffs():
            out = out*pp+ar(coefficient)
        return out

    av = ev(A)
    check('linear subresultant coefficient nonzero', not av.contains(0))
    qq = -ev(B)/av
    caa, cbb, ccc = acb(pp+qq, 1), acb(pp*qq, pp+qq), acb(2*(pp-qq), -pp*qq-2)
    check('nontriple collision', not (caa*caa-3*cbb).contains(0))
    sd = (9*ccc-caa*cbb)/(2*(caa*caa-3*cbb))
    third = -caa-2*sd
    for name, value, lower, upper in (
            ('collision q', qq, '-3.534031', '-3.534030'),
            ('double root real', sd.real, '2.199221', '2.199223'),
            ('double root imaginary', sd.imag, '-.219473', '-.219470'),
            ('third root real', third.real, '-1.720563', '-1.720560'),
            ('third root imaginary', third.imag, '-.561059', '-.561055')):
        check(name+' enclosure', value > arb(lower) and value < arb(upper))
    c, d, e = sp.symbols('c d e')
    K = c*c-3*d
    rr = (9*e-c*d)/(2*K)
    D = c*c*d*d-4*d**3-4*c**3*e-27*e*e+18*c*d*e
    zero('double-root derivative identity', 3*rr*rr+2*c*rr+d+9*D/(4*K*K))
    zero('double-root value identity', rr**3+c*rr*rr+d*rr+e+(2*c**3-9*c*d+27*e)*D/(8*K**3))
    axis = sp.expand(f.subs(z, sp.I*v))
    zero('imaginary-axis real equation', sp.re(axis)-(p*(2-v*v-v)-q*(2+v*v+v)))
    zero('imaginary-axis imaginary equation', sp.im(axis)-((v-1)*p*q-v*v*(v+1)-2))
    zero('positive axis denominator', 2+v*v+v-((v+sp.Rational(1,2))**2+sp.Rational(7,4)))
    check('axis q-zero endpoint signs', sp.im(axis).subs({q:0, v:1}) == -4 and sp.im(axis).subs({q:0, v:-2}) == 2)

    t, u = sp.symbols('t u', real=True)
    base = 2*t**3+2*t*t+t-2
    zero('original selected baseline', f.subs({p:1, q:0, z:(1+sp.I)*t})-(-1+sp.I)*base)
    check('baseline interval', base.subs(t, sp.Rational(3,5)) < 0 < base.subs(t, sp.Rational(7,10)))
    check('baseline monotone positive axis', all(c > 0 for _, c in sp.Poly(sp.diff(base,t),t).terms()))
    check('p-one line has no discriminant zeros', W.subs(p,1) > 0)
    cross = sp.expand(f.subs({p:1, z:u}))
    zero('positive-real root elimination', sp.re(cross)-u*sp.im(cross)-2*(u*(q+1)+1-q))
    zero('unique real crossing equation', sp.im(cross).subs(q,(u+1)/(1-u))-(u*u-3))
    check('u-one excluded', (sp.re(cross)-u*sp.im(cross)).subs(u,1) == 4)
    zero('exact lift-point cubic root', f.subs({p:1,q:-2-sp.sqrt(3),z:sp.sqrt(3)}))
    zero('exact right outer cotangent', sp.cot(11*sp.pi/12)+2+sp.sqrt(3))
    zero('exact left outer cotangent', sp.cot(sp.pi/4)-1)
    zero('exact inner cotangent', sp.cot(sp.pi/6)-sp.sqrt(3))
    zero('lower derivative real part', 4*sp.sin(5*sp.pi/12)*sp.sin(sp.pi/12)-1)
    zero('lower derivative imaginary part', sp.Rational(1,12)+sp.Rational(5,12)-3*sp.Rational(1,3)+sp.Rational(1,2))
    zero('marked upper derivative shift', sp.diff(-2*sp.pi*sp.I*z,z)+2*sp.pi*sp.I)
    zero('shifted upper alias is stationary', -2*sp.pi*sp.I+sp.diff(2*sp.pi*sp.I*z,z))
    n = sp.symbols('n', integer=True, positive=True)
    zero('physical factorial multiplier vanishes', 1-sp.exp(-2*sp.pi*sp.I*(12*n)*sp.Rational(1,12)))
    check('physical proposed index exceeds support', 2*n > n-1)
    zero('support first zero', (12*n)-(11*n)-n)

    assert witness['endpoint'] == {'p':'1','q':'-4'}
    aa, bb, cc4 = acb(-3,1), acb(-4,-3), acb(10,2)
    disks = []
    rad = ar(witness['root_disk_radius'])
    assert len(witness['root_disk_centers']) == 3 and rad > 0
    for j, (xr, xi) in enumerate(witness['root_disk_centers']):
        zz = acb(ar(xr), ar(xi))
        val, der = zz**3+aa*zz**2+bb*zz+cc4, 3*zz**2+2*aa*zz+bb
        margin = rad*abs(der)-abs(val)-rad**2*abs(3*zz+aa)-rad**3
        check(f'fixed root disk {j} Rouche inequality', margin > 0)
        check(f'fixed root disk {j} below real axis', zz.imag+rad < 0)
        disks.append(dict(center=[xr,xi],radius=witness['root_disk_radius'],rouche_margin=str(margin)))
    for j in range(3):
        for k in range(j):
            zj, zk = [acb(*[ar(c) for c in disks[i]['center']]) for i in (j,k)]
            check(f'root disks {k},{j} disjoint', abs(zj-zk) > 2*rad)

    assert proof_hash == sha(PROOF) and script_hash == sha(__file__)
    assert all(sha(ROOT/path) == digest for path,digest in dependencies.items())
    out = dict(status='passed',precision_bits=args.precision,
        exact_identity_count=len(identities),exact_identities=identities,
        comparison_count=len(comparisons),comparisons=comparisons,
        collision_polynomial=str(W),linear_subresultant_A=str(A),linear_subresultant_B=str(B),
        p_isolation=list(map(str,(lo,hi))),p=str(pp),q=str(qq),
        double_root=str(sd),third_root=str(third),
        a=str((arb.pi()/2-acb(pp).atan().real)/arb.pi()),
        b=str((arb.pi()/2-acb(qq).atan().real)/arb.pi()),
        lift_point=dict(a='1/4',b='11/12',s='1/6',cotangent_q='-2-sqrt(3)',
                        lower_log_lift='0',marked_upper_log_lift='-2*pi*i'),
        endpoint_rouche_disks=disks,primary_records=len(primary),current_bindings=len(dependencies),
        root_proposals=0,parameter_searches=0,source_cells_recomputed=0,
        proof_sha256=proof_hash,script_sha256=script_hash,dependencies_sha256=dependencies,
        scope='A collision of the algebraic continuation attached to the original half-endpoint root, and a separate exact marked-phase lift change. No finite-source dominance, finite-sum cancellation, or volume-asymptotic counterexample.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print('PASS',len(identities),'exact identities;',len(comparisons),'comparisons;',
          len(primary),'primary records;',len(dependencies),'current bindings',flush=True)


if __name__ == '__main__':
    main()
