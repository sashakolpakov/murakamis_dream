#!/usr/bin/env python3
"""Original odd V/V' source and positive comparison, not an asymptotic proof."""
import argparse,collections,json,math,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import mpmath as mp
import numpy as np
import sympy as sp
from audit_actual_small_circle_polynomial_face_insertion import Local,casimir
from audit_actual_gaussian_resolvent_numerator_and_cap import paths
from audit_actual_original_marked_face_coefficient import morse_faces,substitute,mul,local_polynomials
from audit_general_odd_endpoint_matching_network import apply_pair


def field_kernels(loc):
    N,p,q,Q=loc.N,loc.p,loc.q,loc.Q;m=N//2
    a=[(2+q*pow(Q,j,p)+pow(q,-1,p)*pow(Q,-j,p))%p for j in range(N)]
    b=[(2-pow(Q,j,p)-pow(Q,-j,p))%p for j in range(N)]
    e=[(q+pow(q,-1,p)-q*pow(Q,-j,p)-pow(q,-1,p)*Q**j)%p for j in range(N)]
    out=[collections.defaultdict(int) for _ in range(3)]
    for j in range(N):
        for i,edges,vis in paths(N,j):
            w=1;o=t=0
            for v,step in edges:
                w=w*(b[v] if step==1 else e[v])%p;o+=step==1;t+=step==2
            unused=[v for v in range(N) if v not in vis]
            f0=math.prod(a[v] for v in unused)%p
            f1=sum(math.prod(a[v] for v in unused if v!=r) for r in unused)%p
            factors=(f0,f1,(f0+pow(N*N,-1,p)*f1)%p)
            for k in range(o+1):
                n=(k+t,i,N-1-j,o-k+t);ww=w*math.comb(o,k)%p
                for H,f in zip(out,factors):H[n]=(H[n]+ww*f)%p
    return [{n:v for n,v in H.items() if v} for H in out]


def original_ops(loc):
    z=sp.symbols('z');N,p=loc.N,loc.p;O=casimir(loc)
    chi=sp.Poly(2*sp.chebyshevt(N,z/2)+2,z)
    powers=[np.eye(N*N,dtype=np.int64)]
    for _ in range(N-1):powers.append(powers[-1]@O%p)
    out=[]
    for derivative in (False,True):
        coeff=[0]*N
        for (degree,),c in chi.terms():
            for k in range(degree):
                exponent=degree-1-k
                value=exponent*pow(-2,exponent-1,p) if derivative and exponent else (0 if derivative else pow(-2,exponent,p))
                coeff[k]=(coeff[k]+int(c)*value)%p
        op=np.zeros_like(O)
        for c,A in zip(coeff,powers):op=(op+c*A)%p
        out.append(op)
    # Q is the u derivative, hence MINUS the sigma derivative.
    P0=out[0];Q=-out[1]%p;F=(P0+pow(N*N,-1,p)*Q)%p
    return P0,Q,F


def grid_checks(counts):
    for N in (3,5,7,9):
        loc=Local(N);p,q,Q,d=loc.p,loc.q,loc.Q,loc.d
        Hs=field_kernels(loc);ops=original_ops(loc)
        D,_=local_polynomials(loc,N//2)
        Dleft={(x,b,0,y):v for (x,b,y),v in D.items()}
        Dright={(x,0,c,y):v for (x,c,y),v in D.items()}
        Dpair={n:v*N*N%p for n,v in mul(Dleft,Dright,p).items()}
        assert Hs[0]==Dpair
        counts['literal_simple_fold_factorizations']+=1
        for H,op in zip(Hs,ops):
            for u in range(N):
                for v in range(N):
                    x=-q*pow(Q,u,p)%p;y=-pow(q,-1,p)*pow(Q,-v,p)%p
                    for r in range(N):
                        s=(u+v-r)%N;delta=r-u;c=pow(Q,-delta,p)
                        value=sum(co*pow(x,k,p)*pow(c,t,p)*pow(y,l,p) for (k,i,t,l),co in H.items())%p
                        pred=value*pow(N,-1,p)*pow(q,-d*delta,p)*pow(c,-d,p)%p
                        assert pred==int(op[r*N+s,u*N+v]),(N,u,v,r,s)
                        counts['original_value_derivative_grid_entries']+=1
                        counts['wrong_unwrapped_total_zeros']+=r+s!=u+v
    for N,k,word in ((3,2,[1,0,2,1]),(5,2,[1,0,2,1]),(3,3,[1,3,0,2,4,1,3])):
        loc=Local(N);p=loc.p;H=field_kernels(loc)[2];op=original_ops(loc)[2]
        for marked in (0,k-1):
            chart=morse_faces(k,word,marked);nf=chart['faces'];target=tuple(0 if f in(0,chart['v']) else N-1 for f in range(nf))
            product={(0,)*nf:1}
            for ids in chart['circles']:
                fac=substitute(H,ids,list(range(nf)),p)
                fac={n:v for n,v in fac.items() if all(n[j]<=target[j] for j in range(nf))}
                product=mul(product,fac,p,cap=N-1)
                product={n:v for n,v in product.items() if all(n[j]<=target[j] for j in range(nf))}
            predicted=product.get(target,0)
            state=np.array([1],dtype=np.int64);cap=np.array([1],dtype=np.int64)
            marker=np.array([[pow(loc.x,j,p)*pow(N*N,-1,p)%p for j in range(N)] for i in range(N)],dtype=np.int64)
            for j in range(k):
                state=np.kron(state,loc.cup[0].reshape(-1))%p
                cap=np.kron(cap,(marker if j==marked else loc.cap[0]).reshape(-1))%p
            state=state.reshape((N,)*(2*k))
            for slot in word:state=apply_pair(op,state,slot,N,p)
            assert int(cap@state.reshape(-1)%p)==predicted
            counts['whole_original_regularized_sources']+=1


def positive_checks(counts):
    maxerr=mp.mpf(0)
    for N in (3,5,7,9,11,13):
        m=N//2;th=mp.pi/N;s=[2*mp.sin(j*th) for j in range(N)]
        a=[4*mp.cos((j+mp.mpf('.5'))*th)**2 for j in range(N)];a[m]=mp.mpf(0)
        aa=a[:];aa[m]=mp.mpf(1)/(N*N)
        err=max(abs(mp.fprod(a[j] for j in range(N) if j!=m)-N*N),
                abs(mp.fsum(1/a[j] for j in range(N) if j!=m)-mp.mpf(N*N-1)/12))
        maxerr=max(maxerr,err);assert err<mp.mpf('1e-60');counts['odd_product_and_reciprocal_sum']+=2
        H0=collections.defaultdict(mp.mpf);HQ=collections.defaultdict(mp.mpf);HK=collections.defaultdict(mp.mpf)
        for j in range(N):
            for i,edges,vis in paths(N,j):
                w=mp.mpf(1);o=t=0
                for v,step in edges:w*=s[v]**2 if step==1 else s[v]*s[v-1];o+=step==1;t+=step==2
                unused=[r for r in range(N) if r not in vis]
                f0=mp.fprod(a[r] for r in unused)
                f1=mp.fsum(mp.fprod(a[v] for v in unused if v!=r) for r in unused)
                fk=1/mp.fprod(aa[v] for v in vis)
                for kk in range(o+1):
                    key=(kk+t,i,N-1-j,o-kk+t);ww=w*math.comb(o,kk)
                    H0[key]+=ww*f0;HQ[key]+=ww*f1;HK[key]+=ww*fk
                counts['positive_unused_row_derivative_paths']+=1
        assert len(HK)==math.comb(N+2,3)
        for n,v in HK.items():
            F=H0[n]+HQ[n]/(N*N)
            assert v<=F*(1+mp.mpf('1e-60'))
            assert F<=mp.mpf(13)/12*v*(1+mp.mpf('1e-60'))
            if n[1]<=m and n[2]<=m:
                assert H0[n]<=v*(1+mp.mpf('1e-60'))
                assert v<=(1+1/(2*N*N*s[m]*s[m+1]))*H0[n]*(1+mp.mpf('1e-60'))
                counts['central_cross_repair_coefficients']+=1
            counts['full_support_regularization_bounds']+=1
        for u in (mp.mpf(0),mp.mpf(1)/N**4,mp.mpf('.02')):
            C=mp.fprod(1+u/a[r] for r in range(N) if r!=m)
            tt=mp.acosh(1+u/2)
            expected=mp.mpf(1) if not u else (mp.sinh(N*tt/2)/(N*mp.sinh(tt/2)))**2
            err=abs(C-expected)/max(1,C);maxerr=max(maxerr,err)
            assert err<mp.mpf('1e-60') and C<=mp.exp((N-1)*tt)*(1+mp.mpf('1e-60'))
            H=collections.defaultdict(mp.mpf)
            for j in range(N):
                for i,edges,vis in paths(N,j):
                    w=mp.fprod(a[r]+u for r in range(N) if r not in vis);o=t=0
                    for v,step in edges:w*=s[v]**2 if step==1 else s[v]*s[v-1];o+=step==1;t+=step==2
                    for kk in range(o+1):H[(kk+t,i,N-1-j,o-kk+t)]+=w*math.comb(o,kk)
            for n,v in H.items():
                assert v<=C*max(1,N*N*u)*(H0[n]+HQ[n]/(N*N))*(1+mp.mpf('1e-60'))
                counts['spectral_radius_full_coefficient_bounds']+=1
    return maxerr


def run():
    mp.mp.dps=75;counts=collections.Counter();grid_checks(counts);err=positive_checks(counts)
    return dict(status='PASS',precision=mp.mp.dps,counts=dict(counts),maximum_relative_identity_error=str(err),
        scope='Exact odd original V and spectral derivative physical grids, actual marked regularized sources, full positive coefficient comparisons and spectral-radius majorants. Uniform entropy and geometric volume are proved analytically, not by finite diagnostics; no genuine-q normal or filling cycle tested.')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=Path(__file__).with_name('actual_fejer_odd_regularized_full_numerator_results.json'));args=ap.parse_args()
    result=run();args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
