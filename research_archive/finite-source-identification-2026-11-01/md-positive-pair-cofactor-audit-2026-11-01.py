#!/usr/bin/env python3
"""Finite diagnostics for a bounded written-proof audit; no asymptotic proof."""
import argparse
import ast
import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp


def formal_row_replacement():
    b = sp.Symbol('b')
    counts = 0
    for j in range(7):
        alpha = sp.symbols('a:'+str(j+1))
        p = sp.symbols('p:'+str(j+1))
        z = sp.symbols('z:'+str(j+1))
        mat = sp.diag(*alpha)
        for v in range(1,j+1):
            mat[v-1,v] = -p[v]
            if v >= 2:
                mat[v-2,v] = -z[v]
        for i in range(j+1):
            mat[j,i] = b**i
        values = [sp.Integer(1)]
        for v in range(1,j+1):
            values.append(b**v*sp.prod(alpha[:v])+p[v]*values[v-1]
                          +(z[v]*alpha[v-1]*values[v-2] if v >= 2 else 0))
        assert sp.expand(mat.det(method='domain-ge')-values[j]) == 0
        counts += 1
    return counts


def finite_determinants():
    cases = dict(ldl=0, determinant_newton=0, boundary_202=0,
                 nodal_cofactor=0, forced_factor=0, pair_trace=0)
    worst = mp.mpf(0)

    def equal(x,y):
        nonlocal worst
        err=abs(x-y)/max(1,abs(x),abs(y))
        worst=max(worst,err)
        assert err < mp.mpf('1e-60'), (x,y,err)

    for N in range(3,17):
        th=mp.pi/N; q=mp.exp(1j*th); Q=q*q
        S=[mp.mpf(1)]; F=[mp.mpc(1)]
        for r in range(1,N):
            S.append(S[-1]*2*mp.sin(r*th))
            F.append(F[-1]*(1-Q**r))
        for a in range((N-1)//2+1):
            beta=S[2*a]/S[a]**2
            hm=mp.matrix(a); hp=mp.matrix(a)
            for r in range(a):
                hm[r,r]=hp[r,r]=1/(mp.cos(r*th)*mp.cos((r+1)*th))
                if r:
                    bn=mp.sin(r*th)**2/(mp.cos(r*th)**2*mp.sin((2*r-1)*th)*mp.sin((2*r+1)*th))
                    hm[r-1,r]=mp.sqrt(bn)*(mp.sin(r*th)-1j*mp.cos(r*th))
                    hp[r-1,r]=mp.conj(hm[r-1,r])
                    hm[r,r-1]=mp.conj(hm[r-1,r]); hp[r,r-1]=mp.conj(hp[r-1,r])
            if a:
                piv=1/mp.cos(th)
                for r in range(1,a):
                    piv=hm[r,r]-abs(hm[r-1,r])**2/piv
                    equal(piv,mp.sin((r+1)*th)/(mp.cos((r+1)*th)*mp.sin((2*r+1)*th)))
                equal(mp.det(hm)/2**a,1/beta)
                assert piv > 0
            cases['ldl']+=1
            def detface(x,b,y):
                return mp.det(b*mp.eye(a)+x*hm/2+y*hp/2) if a else mp.mpf(1)
            for U,V in [(mp.mpc('.7','.2'),mp.mpc('1.3','-.1')),
                        (mp.mpc('-.9','.1'),mp.mpc('-.8','.2'))]:
                literal=mp.mpc(0)
                for k in range(a+1):
                    gb=F[a]/(F[k]*F[a-k])
                    literal += (gb**2*q**(k*(k-(N-1)))*V**k
                                *mp.fprod(U-Q**r for r in range(k))
                                *mp.fprod(V-Q**r for r in range(a-k)))
                matrix=mp.eye(a)-q*U*hm/2-q**-1*hp/(2*V)
                candidate=V**a*q**(a*a)*beta*(mp.det(matrix) if a else 1)
                equal(literal,candidate); cases['determinant_newton']+=1
            x=mp.mpf('1.2');y=mp.mpf('1.7');b=mp.mpf('.8')
            p202=mp.fsum((S[a]/(S[k]*S[a-k]))**2*x**(a-k)*y**k for k in range(a+1))/beta
            equal(detface(x,0,y),p202); cases['boundary_202']+=1
            u=-4*mp.cos((a+mp.mpf('.5'))*th)**2
            before=mp.mpf(0);now=mp.mpf(1);prefix=mp.mpf(1)
            for j in range(1,a+1):
                al=4*mp.cos((j-mp.mpf('.5'))*th)**2+u
                prefix*=al
                sj=2*mp.sin(j*th);sm=2*mp.sin((j-1)*th)
                before,now=now,b**j*prefix+sj**2*(x+y)*now+sj*sm*al*x*y*before
            equal(now,S[2*a]*detface(x,b,y));cases['nodal_cofactor']+=1
            s=N-1-2*a
            forced=mp.fprod(x-Q**r*y for r in range(a+1,N-a))
            equal(forced,mp.fsum(S[s]/(S[k]*S[s-k])*x**(s-k)*y**k for k in range(s+1)))
            cases['forced_factor']+=1
            if a:
                X=x*hm/2;Y=y*hp/2;M=b*mp.eye(a)+X+Y;Mi=M**-1
                A=Mi*X;B=Mi*Y;C=b*Mi
                angles=[mp.mpf('.17'),mp.mpf('-.32'),mp.mpf('.71')]
                Z=mp.exp(1j*angles[0])*C+mp.exp(1j*angles[1])*A+mp.exp(1j*angles[2])*B
                # Similar to M^{-1/2} M(theta) M^{-1/2}; use cyclic traces.
                # B*B in the correct metric is M^{-1} M(theta)^* M^{-1} M(theta).
                Mt=b*mp.exp(1j*angles[0])*mp.eye(a)+mp.exp(1j*angles[1])*X+mp.exp(1j*angles[2])*Y
                lhs=mp.trace(mp.eye(a)-Mi*Mt.H*Mi*Mt) if hasattr(mp,'trace') else sum((mp.eye(a)-Mi*Mt.H*Mi*Mt)[k,k] for k in range(a))
                mats=[C,A,B]
                rhs=mp.mpf(0)
                for i in range(3):
                    for j in range(i+1,3):
                        pair=sum((mats[i]*mats[j])[k,k] for k in range(a))
                        assert abs(mp.im(pair)) < mp.mpf('1e-60') and mp.re(pair)>0
                        rhs+=abs(mp.exp(1j*angles[i])-mp.exp(1j*angles[j]))**2*pair
                equal(lhs,rhs);cases['pair_trace']+=1
    return dict(counts=cases,maximum_relative_residual=str(worst))


def original_source_replay(repo):
    namespace={'mp':mp,'sp':sp}
    selected=[('audit_actual_q_hahn_negative_clock_boundary.py',{'literal_h','matrix'}),
              ('audit_actual_correlated_boundary_band_ratio.py',{'root_cup'}),
              ('audit_actual_complete_circle_positive_face_polynomial.py',{'source_checks'})]
    for name,names in selected:
        path=repo/'experiments'/name
        tree=ast.parse(path.read_text())
        nodes=[node for node in tree.body if isinstance(node,ast.FunctionDef) and node.name in names]
        assert {node.name for node in nodes} == names
        exec(compile(ast.Module(body=nodes,type_ignores=[]),str(path),'exec'),namespace)
    return namespace['source_checks']()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--repo',type=Path,default=Path('/private/tmp/murakamis_dream-publication'))
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();mp.mp.dps=80
    out=dict(formal_row_replacement_identities=formal_row_replacement(),
             independent_finite_diagnostics=finite_determinants(),
             original_literal_circle_replay=original_source_replay(args.repo),
             scope='Finite algebra diagnostics only. Uniform bounds are assessed in the written audit; no compiler, geometry, Hermite, or asymptotic theorem is established by these samples.')
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
