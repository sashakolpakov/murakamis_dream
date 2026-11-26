#!/usr/bin/env python3
"""Exact acute-gradient eliminations and affine height-transfer identities.

No numerical root or source cell is evaluated. Strict signs, logarithm
calibration, continuation and convexity are the accompanying written proof.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_acute_gradient_height_transfer.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT /
                        'repro/results/research-mixed-acute-gradient-height-transfer.json')
    args = parser.parse_args()
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

    for stem in ('mixed_closed_cotangent_roots', 'mixed_seam_attenuation_vertices'):
        rp = f'repro/results/research-{stem.replace("_", "-")}.json'
        record = inherit(rp)
        assert record['status'] == 'passed', rp
        assert record['proof_sha256'] == bind(f'notes/research_{stem}.md')
        assert record['script_sha256'] == bind(f'experiments/check_{stem}.py')
        primary[rp] = record
    assert primary['repro/results/research-mixed-closed-cotangent-roots.json']['exact_identity_count'] == 13
    attenuation = primary['repro/results/research-mixed-seam-attenuation-vertices.json']
    assert attenuation['status'] == 'passed'

    identities = []

    def zero(name, expression):
        assert sp.cancel(sp.expand(expression)) == 0, name
        identities.append(name)

    u, v, p, q, x, t, alpha, beta = sp.symbols(
        'u v p q x t alpha beta', real=True)
    I = sp.I
    S = u + I*v
    F0 = lambda P, Q: sp.expand(S*S + (P+Q)*S - 1 + I*(Q-P))
    F1 = lambda P, Q: sp.expand((S+I)*(S+P)*(S+Q)-2*I*(P-I)*(Q+I))
    A, B, U = (p-I)/(p+I), (q-I)/(q+I), (S-I)/(S+I)
    zero('original left gradient exponential', (1-A*U)/((1-A)*U)-(S+p)/(S-I))
    zero('original right gradient exponential', (1-B*U)/(1-B)-(S+q)/(S+I))
    Na, Nb = u*u+u*p+v*v-v, u*u+u*q+v*v+v
    zero('left ratio real numerator', sp.re((S+p)*sp.conjugate(S-I))-Na)
    zero('right ratio real numerator', sp.re((S+q)*sp.conjugate(S+I))-Nb)
    zero('left ratio positive imaginary numerator', sp.im((S+p)*sp.conjugate(S-I))-(u+p*(1-v)))
    zero('right ratio negative imaginary numerator', sp.im((S+q)*sp.conjugate(S+I))+u+q*(1+v))

    real_f0 = F0(p, q)
    G0 = sp.groebner([sp.re(real_f0), sp.im(real_f0)], p, q, u, v)
    real_a = (1+v)*u*u+v*v*(v+3)+1-v
    real_b = (1-v)*u*u+v*v*(3-v)+1+v
    zero('quadratic acute left identity modulo original equations', G0.reduce(sp.expand(2*Na-real_a))[1])
    zero('quadratic acute right identity modulo original equations', G0.reduce(sp.expand(2*Nb-real_b))[1])
    complex_f0 = F0(p, q+I*beta)
    G0c = sp.groebner([sp.re(complex_f0), sp.im(complex_f0)], p, q, u, v, beta)
    ca = (1+v+beta)*u*u+v**3+(3+beta)*v*v+(2*beta-1)*v+1+beta
    zero('quadratic one-real endpoint identity', G0c.reduce(sp.expand(2*Na-ca))[1])
    zero('quadratic coefficient increases with neighbor imaginary cotangent', sp.diff(ca,beta)-(u*u+(v+1)**2))
    zero('quadratic worst-neighbor positive decomposition', ca.subs(beta,-sp.Rational(1,2))-
         ((sp.Rational(1,2)+v)*u*u+v**3+sp.Rational(5,2)*(v-sp.Rational(2,5))**2+sp.Rational(1,10)))
    P, Q = p+I*alpha, q+I*beta
    zero('quadratic conjugate-swap symmetry',
         sp.expand(sp.conjugate(S)**2+(sp.conjugate(Q)+sp.conjugate(P))*sp.conjugate(S)-1+
                   I*(sp.conjugate(P)-sp.conjugate(Q))-sp.conjugate(F0(P,Q))))

    Pa = (x*x*(v**3+6*v*v+4+beta*(v+2)**2)
          +2*x*(v**5+2*v**4+v**3+6*v*v-4*v+2+beta*(v**4+7*v*v-2*v+2))
          +v*v*(1-v)**4*(v+2+beta))
    Pb = (x*x*(t**3-6*t*t+4*t+4-alpha*(t-2)**2)
          +2*x*(t**5-4*t**4+t**3+4*t*t-2*t+2+alpha*(-t**4+2*t**3+t*t-2*t-2))
          +t*t*(1-t)**2*(1+t)*(t*t-t+2-alpha*(t+1)))

    def resultant_left(neighbor):
        f = F1(p, neighbor)
        real = sp.cancel(u*sp.re(f).subs(p,(v-v*v-u*u)/u))
        imag = sp.cancel(u*sp.im(f).subs(p,(v-v*v-u*u)/u))
        assert sp.denom(real) == 1 and sp.denom(imag) == 1
        return sp.resultant(real, imag, q)

    def resultant_right(neighbor):
        f = F1(neighbor, q)
        real = sp.cancel(u*sp.re(f).subs(q,(-v-v*v-u*u)/u))
        imag = sp.cancel(u*sp.im(f).subs(q,(-v-v*v-u*u)/u))
        assert sp.denom(real) == 1 and sp.denom(imag) == 1
        return sp.resultant(real, imag, p)

    zero('real-neighbor cubic left resultant', resultant_left(q)-Pa.subs({beta:0,x:u*u}))
    zero('real-neighbor cubic right resultant', resultant_right(p)+Pb.subs({alpha:0,x:u*u,t:-v}))
    zero('complex-neighbor cubic left resultant', resultant_left(q+I*beta)-Pa.subs(x,u*u))
    zero('complex-neighbor cubic right resultant', resultant_right(p+I*alpha)+Pb.subs({x:u*u,t:-v}))
    zero('real left resultant middle coefficient decomposition', 3*v*v-2*v+1-
         (3*(v-sp.Rational(1,3))**2+sp.Rational(2,3)))
    zero('real right resultant leading coefficient decomposition', t**3-6*t*t+4*t+4-
         (4*(1-t*t)+2*t*(2-t)+t**3))
    zero('real right resultant middle coefficient decomposition', t**5-4*t**4+t**3+4*t*t-2*t+2-
         (t**5+t**3+4*t*t*(1-t*t)+2*(1-t)))
    zero('real right resultant constant bracket decomposition', t*t-t+2-
         ((t-sp.Rational(1,2))**2+sp.Rational(7,4)))
    zero('complex left monotone middle slope decomposition', v**4+7*v*v-2*v+2-
         (v**4+7*(v-sp.Rational(1,7))**2+sp.Rational(13,7)))
    Pa_min = sp.Poly(Pa.subs(beta,-sp.Rational(1,2)), x)
    zero('complex left worst leading coefficient positive decomposition', Pa_min.coeff_monomial(x*x)-
         (v**3+sp.Rational(11,2)*(v-sp.Rational(2,11))**2+sp.Rational(20,11)))
    zero('complex left worst middle coefficient positive decomposition', Pa_min.coeff_monomial(x)-
         (2*v**5+3*v**4+2*v**3+5*(v-sp.Rational(3,5))**2+sp.Rational(1,5)))
    zero('complex left worst constant coefficient', Pa_min.coeff_monomial(1)-v*v*(1-v)**4*(v+sp.Rational(3,2)))
    zero('complex right monotone middle slope decomposition', -t**4+2*t**3+t*t-2*t-2-
         (-(t*t-1)**2+2*t*(t*t-1)-t*t-1))
    Pb_min = sp.Poly(Pb.subs(alpha,sp.Rational(1,2)), x)
    zero('complex right worst leading coefficient positive decomposition', Pb_min.coeff_monomial(x*x)-
         (t**3+6*t*(1-t)+2-t*t/2))
    bernstein = [sp.Rational(k) for k in ('2','4/5','1/2','3/2','12/5','2')]
    assert all(c>0 for c in bernstein)
    zero('complex right worst middle positive Bernstein expansion', Pb_min.coeff_monomial(x)-
         sum(c*sp.binomial(5,j)*t**j*(1-t)**(5-j) for j,c in enumerate(bernstein)))
    zero('complex right worst constant positive decomposition', Pb_min.coeff_monomial(1)-
         t*t*(1-t)**2*(1+t)*((t-sp.Rational(3,4))**2+sp.Rational(15,16)))

    base = F1(0,0)
    zero('cubic analytic base real equation', sp.re(base)-u*(u*u-3*v*v-2*v))
    zero('cubic analytic base imaginary equation after real elimination',
         sp.im(base).subs(u*u,3*v*v+2*v)-2*(4*v**3+4*v*v+v-1))
    zero('cubic analytic base left positive numerator', Na.subs(p,0).subs(u*u,3*v*v+2*v)-(4*v*v+v))
    zero('cubic analytic base right positive numerator', Nb.subs(q,0).subs(u*u,3*v*v+2*v)-(4*v*v+3*v))
    assert sp.Rational(4,3)-sp.Rational(5,3)<0

    h,k,ga,gb,sa,sb,aa,bb,ta,tb,eta,eps = sp.symbols(
        'h k ga gb sa sb aa bb ta tb eta eps', real=True)
    zero('left vertical derivative with selected frequency', sp.re(I*(ga+I*gb+I*sp.pi*sa))+gb+sp.pi*sa)
    zero('affine acute-gradient substitution',
         -(ta-eta*aa/2+sp.pi*sa)*h-(tb-eps*bb/2+sp.pi*sb)*k-
         (-ta*h-tb*k+eta*aa*h/2+eps*bb*k/2-sp.pi*sa*h-sp.pi*sb*k))
    H00,H01,H11,J00,J01,J11 = sp.symbols('H00 H01 H11 J00 J01 J11',real=True)
    H=sp.Matrix([[H00+I*J00,H01+I*J01],[H01+I*J01,H11+I*J11]])
    vec=sp.Matrix([h,k])
    zero('height Hessian equals negative real holomorphic Hessian',
         sp.re(((I*vec).T*H*(I*vec))[0])+((vec.T*sp.re(H)*vec)[0]))
    # Exact branch bookkeeping: a selected own-real frequency branch is
    # available, and remaining allocated own-factorial coefficients are >=0.
    branches=[]
    for et,ep in itertools.product((0,1),repeat=2):
        for sig_a,sig_b in itertools.product(range(et+1),range(ep+1)):
            for f_a,f_b in itertools.product(sorted({0,sig_a}),sorted({0,sig_b})):
                assert et-f_a>=0 and ep-f_b>=0
                branches.append([et,ep,sig_a,sig_b,f_a,f_b])
    assert len(branches)==16
    # The positive-part losses are pointwise in the sign of each height.
    r,Habs = sp.symbols('r Habs',nonnegative=True)
    for sign in (-1,1):
        hval=sign*Habs
        left_loss=sp.pi/2*(Habs if sign>0 else 0)
        right_loss=sp.pi/2*(Habs if sign<0 else 0)
        left_res=sp.expand(-sp.pi*r*hval/2+left_loss)
        right_res=sp.expand(sp.pi*r*hval/2+right_loss)
        assert left_res.subs(r,0)>=0 and left_res.subs(r,1)>=0
        assert right_res.subs(r,0)>=0 and right_res.subs(r,1)>=0

    assert proof_hash==sha(PROOF) and script_hash==sha(__file__)
    assert all(sha(ROOT/path)==digest for path,digest in dependencies.items())
    result=dict(
        status='passed', arithmetic='exact symbolic rational identities and positive decompositions',
        exact_identity_count=len(identities), exact_identities=identities,
        cubic_resultants=4, positive_bernstein_coefficients=list(map(str,bernstein)),
        selected_branches=branches, selected_branch_count=len(branches),
        primary_records=len(primary), current_bindings=len(dependencies),
        numerical_roots_evaluated=0, source_cells_recomputed=0,
        proof_sha256=proof_hash, script_sha256=script_hash,
        dependencies_sha256=dependencies,
        scope='Acute original gradients when the differentiated endpoint is real, including a complex neighbor in the closed cotangent chamber; exact affine and one-sided vertical lower bounds for the selected coherent rate on the typed polygons. No finite-kernel lower bound, new source coverage or seam-sign assertion.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',len(identities),'exact identities;',len(branches),'selected branches;',
          len(primary),'primary records;',len(dependencies),'current bindings',flush=True)


if __name__=='__main__':
    main()
