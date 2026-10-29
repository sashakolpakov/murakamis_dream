#!/usr/bin/env python3
"""Root-normal kernel/cokernel maps with gauge and actual factorial source.

Exact finite-field rational-function identities test the characteristic-zero
proof, including a Jordan block where the symbol is zero. No regulator
identification or knot volume theorem is inferred.
"""

import json
from pathlib import Path

import sympy as s


Q,Y=s.symbols('Q Y')


def field(N):
    k=(10000+N-1)//N
    while not s.isprime(N*k+1):k+=1
    p=int(N*k+1);g=int(s.primitive_root(p))
    return p,pow(g,(p-1)//N,p)


def modpoly(f,p):
    polynomial=s.Poly(s.expand(f),Y)
    return sum(int(c.p)%p*pow(int(c.q),-1,p)%p*Y**m[0]
               for m,c in polynomial.terms())


def modmat(A,p):return A.applyfunc(lambda f:modpoly(f,p))
def D(A):return A.applyfunc(lambda f:Y*s.diff(f,Y))


def assert_zero(f,p):
    numerator=s.together(f).as_numer_denom()[0]
    assert modpoly(numerator,p)==0


def jets(B,N,z,p):
    B0=modmat(B.subs(Q,z),p)
    B1=modmat(B.diff(Q).subs(Q,z)*z,p)
    H0=s.eye(B.rows);H1=s.zeros(B.rows)
    for j in range(N):
        scale=pow(z,j,p)
        F0=modmat(B0.subs(Y,scale*Y),p)
        F1=modmat((B1+j*D(B0)).subs(Y,scale*Y),p)
        H1=modmat(H1*F0+H0*F1,p)
        H0=modmat(H0*F0,p)
    return B0,H0,H1


def normal_maps_and_gauges():
    records=[]
    for N in range(2,8):
        p,z=field(N);epsilon=Q/s.Integer(z)-1
        G0=s.Matrix([[1,0],[Y,1]])
        E12=s.Matrix([[0,1],[0,0]])
        G=G0*(s.eye(2)+epsilon*Y*Y*E12)
        inverse=(s.eye(2)-epsilon*Y*Y*E12)*G0.inv()
        G1=modmat(z*G.diff(Q).subs(Q,z),p)
        for jordan in (False,True):
            if jordan:
                B=s.Matrix([[1,1],[epsilon*N,1]])
                project=lambda v:v[1]
            else:
                B=s.diag(1+epsilon*N*Y**N,2)
                project=lambda v:v[0]
            B0,H0,H1=jets(B,N,z,p)
            L0=modmat(H0-s.eye(2),p)
            Bg=(inverse*B*G.subs(Y,Q*Y)).applyfunc(s.expand)
            _,Hg0,Hg1=jets(Bg,N,z,p)
            assert modmat(G0*Hg0-H0*G0,p)==s.zeros(2)
            Lg0=modmat(Hg0-s.eye(2),p)
            residual=modmat(G0*Hg1-H1*G0-N*H0*D(G0)-L0*G1+G1*Lg0,p)
            assert residual==s.zeros(2)
            v=s.Matrix([Y+Y*Y,0])
            L1=lambda w:modmat(H1*w+N*H0*D(w),p)
            # Reduce the scalar polynomial after modular normalization.
            value=modpoly(project(L1(v))*pow(N*N,-1,p),p)
            expected=(Y+Y*Y) if jordan else (Y+2*Y*Y)/s.Integer(N)+Y**N*(Y+Y*Y)
            assert_zero(value-expected,p)
            symbol=project(v)
            assert (symbol==0) == jordan
            shifted=modmat(B0*v.subs(Y,z*Y),p)
            equiv=project(L1(shifted)-B0*L1(v).subs(Y,z*Y))
            assert_zero(equiv,p)
            # The normal co-source includes both its first coefficient
            # and the first coefficient of the section.
            v0=s.Matrix([1+Y,0]);v1=s.Matrix([Y*Y,Y+1])
            ell0=s.Matrix([[1,Y]]);ell1=s.Matrix([[Y*Y,1]])
            w0=G0.inv()*v0
            w1=G0.inv()*v1-G0.inv()*G1*G0.inv()*v0
            old=(ell0*v1+ell1*v0)[0]
            new=(ell0*G0*w1+(ell1*G0+ell0*G1)*w0)[0]
            assert_zero(old-new,p)
            records.append({'level':N,'jordan':jordan,
                            'kernel_cokernel_symbol_invertible':not jordan,
                            'normal_operator_and_cyclic_equivariance_exact':True,
                            'quantum_and_meridian_dependent_gauge_exact':True,
                            'normal_cosource_exact':True})
    return records


def factorial_source():
    records=[]
    for N in range(2,9):
        p,z=field(N)
        G=s.prod(1-Q**j*Y for j in range(N))
        F=modpoly(G.subs(Q,z),p)
        assert F==modpoly(1-Y**N,p)
        defect=s.expand(G.subs(Y,Q*Y)-G)
        h1=modpoly(z*s.diff(defect,Q).subs(Q,z),p)
        expected=-N*Y*(1-Y**N)/(1-Y)
        assert_zero(h1-expected,p)
        source=sum(expected.subs(Y,pow(z,j,p)*Y) for j in range(N))
        assert_zero(source+N*N*Y**N,p)
        assert_zero(Y*s.diff(F,Y)/N-source/(N*N),p)
        records.append({'level':N,'root_factorial_section':'1-U',
                        'normalized_actual_normal_source':'-U',
                        'central_derivative_and_cyclic_source_exact':True,
                        'root_horizontal_section_is_not_normal_horizontal':True})
    return records


def main():
    result={'normal_maps_and_gauges':normal_maps_and_gauges(),
            'finite_factorial_actual_source':factorial_source(),
            'scope':'First quantum-normal pointed module; no geometric regulator identification or volume theorem.'}
    path=Path(__file__).with_name('first_quantum_normal_connection_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'kernel_cokernel_gauge_cases':len(result['normal_maps_and_gauges']),
                      'actual_finite_factorial_source_cases':len(result['finite_factorial_actual_source']),
                      'output':str(path)},indent=2))


if __name__=='__main__':main()
