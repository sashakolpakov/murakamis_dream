#!/usr/bin/env python3
"""Physical THIRD five-point certificate, opposite root and original source.

The whole word is contracted before any source is evaluated.  No product
of auxiliary coordinate ports and no selected knot value defines a frame.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_shared_quantum_flags import head, shift, mm, mpow, euler, equal
from audit_actual_rogers_bridge_transport import crossing
from audit_actual_borel_regular_fusion import inv
from audit_figure_eight_whole_source import MixedEntries
from audit_finite_sum_annihilator import field


def symbolic_faces():
    X, Z, T = sp.symbols('X Z T')
    R = 1-(1-T)*X
    H = X+Z-X*Z
    Zp = 1-R*(1-Z)
    Xp = T*X/R
    C = Xp/H
    points = [sp.Matrix([1, 0]), sp.Matrix([1, 1-X]), sp.Matrix([0, 1]),
              sp.Matrix([1-Z, 1]), sp.Matrix([1, R])]
    # THIRD is (a,b,p,p1,sR).  This even permutation is (a,sR,b,p1,p).
    permutation = [0, 4, 1, 3, 2]
    points = [points[j] for j in permutation]
    def determinant(v, w):
        return sp.det(sp.Matrix.hstack(v, w))
    def cross_ratio(vs):
        a, b, c, d = vs
        return determinant(d,b)*determinant(c,a)/(determinant(d,a)*determinant(c,b))
    g = 1-C+C*Zp
    expected = [g, g/Zp, 1/Zp, (1-1/C)/Zp, 1-1/C]
    for j in range(5):
        actual = cross_ratio([v for k,v in enumerate(points) if k != j])
        assert sp.factor(actual-expected[j]) == 0
    assert sp.factor(H-(Xp+Zp-Xp*Zp)) == 0
    assert sp.factor(H-Zp/(1-C+C*Zp)) == 0
    y = -C*Zp/(1-C)
    assert sp.factor(y/(y-1)-Xp) == 0
    assert sp.factor(C*(1-Zp)/(C*(1-Zp)-1)-(1-H/Zp)) == 0
    return {'even_flag_permutation': permutation, 'all_five_literal_faces': True,
            'both_explicit_negative_quads': True}


def main():
    results = []
    for N in range(2, 11):
        p, generator, q = field(N)
        E = MixedEntries(N,p,q)
        Em = MixedEntries(N,p,pow(q,-1,p))
        Q, r, d = E.Q, Em.Q, N-1
        assert r == pow(Q,-1,p)
        xc = -pow(q,-1,p) % p
        lam, kn = pow(xc,-1,p), pow(xc,N,p)
        z, k, e, f = head(E,xc)
        eye = np.eye(N,dtype=np.int64)
        I = np.eye(N*N,dtype=np.int64)
        zero = np.zeros_like(I)
        Z, T = np.kron(z,eye), np.kron(eye,z)
        Ktot = np.kron(k,k)
        ftot = (np.kron(f,eye)+np.kron(inv(k,p),f)) % p
        D = np.diag([pow(xc,-a-b,p)*pow(Q,a*b,p) % p
                     for a in range(N) for b in range(N)]).astype(np.int64)
        Fm = np.diag([Em.F[(-j) % N] for j in range(N)])
        e1 = np.diag([0,1]+[0]*(N-2))
        flip = np.zeros_like(I)
        for a in range(N):
            for b in range(N): flip[b*N+a,a*N+b] = 1
        B = crossing(E,xc,xc,1)
        Bi = crossing(E,xc,xc,-1)
        equal(mm(B,Bi,p),I,p)
        cup, marker = np.zeros(N*N,dtype=np.int64), np.zeros(N*N,dtype=np.int64)
        for a in range(N):
            cup[a*N+d-a] = N*pow(xc,a-d,p) % p
            for b in range(N): marker[a*N+b] = pow(xc,b,p)*pow(N,-2,p) % p

        for mu in (1,generator,pow(generator,2,p)):
            S1 = np.kron(shift(N,mu),eye)
            S2 = np.kron(eye,shift(N,kn*mu % p))
            X = xc*mm(S2,inv(S1,p),p) % p
            aunit = mm(T,X,p)
            ae = Q*mm(aunit,inv(Z,p),p) % p
            nplus = mm(np.kron(e,eye),S2,p)
            nminus = -mm(Q*I-inv(Z,p),aunit,p) % p
            Pplus, M = euler(E,nplus), euler(E,nminus)
            Pplusi = inv(Pplus,p)
            A = mm(M,Pplus,p)
            Ai = inv(A,p)
            equal(mm(mm(flip,D,p),A,p),B,p)
            H = mm(mm(Pplusi,Z,p),Pplus,p)
            R = (I-mm(I-T,X,p)) % p
            Xp = mm(aunit,inv(R,p),p)
            Zp = mm(mm(Ai,Z,p),A,p)
            equal(Zp,I-mm(R,I-Z,p),p)
            C = mm(inv(H,p),Xp,p)
            equal(C,mm(mm(Ai,ae,p),A,p),p)
            equal(mm(C,Zp,p),Q*mm(Zp,C,p),p)
            equal(mpow(C,N,p),I,p)
            equal(mm(H,C,p),Xp,p)
            Narg = mm(C,I-Zp,p)
            equal(Narg,mm(mm(Pplusi,nminus,p),Pplus,p),p)
            equal(H,mm(Zp,inv(I-Narg,p),p),p)
            # The all-N proof uses these inverse actual shared-flag identities.
            equal(mm(mm(Bi,S1,p),B,p),xc*mm(S2,inv(H,p),p),p)
            equal(mm(mm(Bi,S2,p),B,p),pow(xc,-1,p)*mm(Ktot,S1-ftot,p),p)

            # The clock mark uses root r=Q^-1 and index j_new=-j (mod N).
            E_Q = mm(mm(Ai,np.kron(e1,eye),p),A,p)
            c3 = mm(C,I-E_Q,p)
            a3 = mm(c3,I-r*Zp,p)
            equal(mpow(c3,N,p),zero,p)
            equal(mm(c3,Zp,p),Q*mm(Zp,c3,p),p)
            equal(a3,mm(mm(inv(C,p),Narg,p),C,p),p)
            F3 = mm(mm(Ai,np.kron(Fm,eye),p),A,p)
            F3i = inv(F3,p)
            equal(mm(mm(F3,c3,p),F3i,p),a3,p)
            P3, B3 = euler(Em,c3), euler(Em,a3)
            P3i, B3i = inv(P3,p), inv(B3,p)
            H3 = mm(mm(P3i,Zp,p),P3,p)
            FH = mm(mm(P3i,F3,p),P3,p)
            FHi = inv(FH,p)
            y3 = -r*mm(c3,H3,p) % p
            Y = euler(Em,y3)
            equal(mm(FHi,P3i,p),mm(mm(P3i,FHi,p),Y,p),p)
            # Explicit inverse-word port, not just its unframed product.
            Yi = inv(Y,p)
            J3 = mm(mm(Yi,H3,p),Y,p)
            equal(mm(mm(P3,H3,p),P3i,p),Zp,p)
            equal(mm(mm(mm(mm(Yi,FH,p),c3,p),FHi,p),Y,p),a3,p)
            W3 = mm(P3,FH,p)
            W3i = inv(W3,p)
            def frame(value): return mm(mm(W3,value,p),W3i,p)
            Fhat, Phat, Yhat = frame(FHi), frame(P3i), frame(Y)
            equal(mm(mm(Fhat,frame(c3),p),inv(Fhat,p),p),c3,p)
            equal(frame(H3),Zp,p)
            equal(frame(c3),a3,p)
            equal(mm(mm(Phat,frame(H3),p),inv(Phat,p),p),J3,p)
            previous = mm(Phat,Fhat,p)
            equal(mm(mm(previous,frame(y3),p),inv(previous,p),p),y3,p)
            PN = euler(E,Narg)
            reflected = mm(mm(mm(inv(C,p),I-Narg,p),inv(PN,p),p),C,p)
            equal(B3,reflected,p)
            prefix = mm(mm(mm(D,Pplus,p),C,p),F3,p)
            suffix = mm(inv(C,p),I-Narg,p)
            equal(suffix,mm(mm(R,inv(aunit,p),p),Zp,p),p)
            left = mm(FHi,P3i,p)
            right = mm(mm(P3i,FHi,p),Y,p)
            actual = mm(D,A,p)
            for word in (left,right):
                physical = mm(mm(prefix,word,p),suffix,p)
                equal(physical,actual,p)
                equal(inv(mm(flip,physical,p),p),Bi,p)
                assert int(marker@flip@physical@cup) % p == 1
            for h in range(N):
                forbidden = np.zeros_like(I)
                for j in range(1,h+1):
                    ej = np.zeros_like(eye); ej[j,j]=1
                    forbidden = (forbidden+mm(mm(Ai,np.kron(ej,eye),p),A,p)) % p
                equal(mpow(c3,h,p),mm(mpow(C,h,p),I-forbidden,p),p)
            results.append({'N':N,'prime':p,'physical_wrap':mu,
                            'actual_inverse_flag_transport':True,'actual_third_pair':True,
                            'opposite_root_and_full_mark':True,'all_carry_powers':True,
                            'inverse_word_face_frame_checked':True,
                            'input_adapter_has_no_singular_inverse':True,
                            'whole_original_positive_and_negative_R':True,
                            'original_one_crossing_source':1})
    Path(__file__).with_name('audit_literal_third_full_phi_certificate_results.json').write_text(
        json.dumps({'symbolic_faces':symbolic_faces(),'cases':results,
                    'scope':'literal physical THIRD operator identity and original full source; '
                            'positive charged atlas/cycle transport not claimed'},indent=2)+'\n')
    print(f'PASS five literal third faces, {len(results)} actual inverse-flag pairs and '
          'opposite-root third words, all carry powers and full original +/- R source')


if __name__ == '__main__':
    main()
