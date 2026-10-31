#!/usr/bin/env python3
"""Exact polynomial cross factorization against original unused-row paths.

Finite-field checks of the new cleared cofactors. No asymptotic claim.
The imported path expansion is separately checked against original physical
coproduct matrices in the public Gaussian-resolvent audit.
"""
import argparse, json, sys
from pathlib import Path
from types import SimpleNamespace
import sympy as sp
import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_actual_gaussian_resolvent_numerator_and_cap import finite_H, paths

ONE={(0,0,0,0):1}
X={(1,0,0,0):1}; Y={(0,0,0,1):1}
XY={(1,0,0,1):1}

def add(p, *polys):
    out={}
    for poly in polys:
        for e,v in poly.items():out[e]=(out.get(e,0)+v)%p
    return {e:v for e,v in out.items() if v}

def scale(poly,v,p):return {e:v*c%p for e,c in poly.items() if v*c%p}

def mul(f,g,p):
    out={}
    for a,v in f.items():
        for b,w in g.items():
            e=tuple(x+y for x,y in zip(a,b));out[e]=(out.get(e,0)+v*w)%p
    return {e:v for e,v in out.items() if v}

def loc(N):
    k=20
    while not sp.isprime(2*N*k+1):k+=1
    p=2*N*k+1; q=pow(int(sp.primitive_root(p)),k,p)
    return SimpleNamespace(N=N,p=p,q=q,Q=q*q%p)

def factorized(L,u):
    N,p,q,Q=L.N,L.p,L.q,L.Q;m=N//2
    a=[(2+q*pow(Q,j,p)+pow(q,-1,p)*pow(Q,-j,p))%p for j in range(N)]
    bs=[(2-pow(Q,j,p)-pow(Q,-j,p))%p for j in range(N)]
    es=[(q+pow(q,-1,p)-q*pow(Q,-j,p)-pow(q,-1,p)*pow(Q,j,p))%p for j in range(N)]
    A=add(p,X,Y)
    def R(face):
        seq=[];prefix=1
        for j in range(m+1):
            e=[0]*4;e[face]=j
            terms=[{tuple(e):prefix}]
            if j:terms.append(scale(mul(A,seq[-1],p),bs[j],p))
            if j>1:terms.append(scale(mul(XY,seq[-2],p),es[j]*(a[j-1]+u),p))
            seq.append(add(p,*terms));prefix=prefix*(a[j]+u)%p
        return seq
    rb,rc=R(1),R(2);db,dc=rb[m-1],rc[m-1]
    if N%2:
        return add(p,mul(rb[m],rc[m],p),scale(mul(XY,mul(db,dc,p),p),u*es[m+1],p))
    eb=scale(rb[m-2],a[m-1]+u,p) if m>1 else {}
    ec=scale(rc[m-2],a[m-1]+u,p) if m>1 else {}
    return add(p,scale(mul(A,mul(db,dc,p),p),bs[m],p),
               scale(mul(XY,add(p,mul(db,ec,p),mul(eb,dc,p)),p),es[m],p))

def run():
    counts={'levels':0,'spectral_values':0,'cross_coefficients':0,'central_zero_values':0,
            'all_support_degrees':0,'complete_node_full_cross_identities':0,
            'full_real_spectral_countercoefficient_identities':0}
    for N in range(3,13):
        L=loc(N);p=L.p;m=N//2
        amid=(2+L.q*pow(L.Q,m-1,p)+pow(L.q,-1,p)*pow(L.Q,1-m,p))%p
        values=list(dict.fromkeys(list(range(N))+[(-amid)%p]))
        for u in values:
            direct=scale(finite_H(L,(-2-u)%p),(-1)**(N-1),p)
            cross={e:v for e,v in direct.items() if e[1]<=m-(N%2==0) and e[2]<=m-(N%2==0)}
            fact=factorized(L,u)
            assert cross==fact,(N,u,next((e for e in cross.keys()|fact.keys() if cross.get(e)!=fact.get(e)),None))
            for e in fact:
                assert sum(e)==N-1
                counts['all_support_degrees']+=1
            counts['cross_coefficients']+=len(cross)
            counts['spectral_values']+=1
            counts['central_zero_values']+=u==(-amid)%p
        for channel in range((N-1)//2+1):
            node=(L.q*pow(L.Q,channel,p)+pow(L.q,-1,p)*pow(L.Q,-channel,p))%p
            u=(-2-node)%p
            direct=scale(finite_H(L,node),(-1)**(N-1),p)
            assert direct==factorized(L,u),(N,channel)
            counts['complete_node_full_cross_identities']+=1
        if N%4==0:
            j=N//4-1;e=(j,0,N-1-j,0)
            endpoint=scale(finite_H(L,-2%p),(-1)**(N-1),p)[e]
            opposite=scale(finite_H(L,2),(-1)**(N-1),p)[e]
            pred=1
            for r in range(N//4,N//2):
                ar=(2+L.q*pow(L.Q,r,p)+pow(L.q,-1,p)*pow(L.Q,-r,p))%p
                pred=pred*(ar-4)*pow(ar,-1,p)%p
            pred=pred*(-1)**(N//2)%p
            assert opposite==endpoint*pred%p
            counts['full_real_spectral_countercoefficient_identities']+=1
        counts['levels']+=1
    mp.mp.dps=70
    eta=mp.mpf(1)/8
    C=max(1/(4*mp.sin(mp.pi*eta/2)**2),
          1/(4*mp.cos(mp.pi*eta)*mp.cos(2*mp.pi*eta)))
    counts['localized_derivative_coefficient_bounds']=0
    counts['localized_repair_paths']=0
    for N in range(8,16):
        th=mp.pi/N
        a=[4*mp.cos((j+mp.mpf('.5'))*th)**2 for j in range(N)]
        if N%2:a[N//2]=mp.mpf(0)
        s=[2*mp.sin(j*th) for j in range(N)]
        coeff={}
        for j in range(int(mp.ceil(N*(mp.mpf('.5')+eta))),N):
            for i,edges,vis in paths(N,j):
                if i>N*(mp.mpf('.5')-eta):continue
                weights=[mp.mpf(1)]
                for r in range(N):
                    if r in vis:continue
                    nxt=[mp.mpf(0)]*(len(weights)+1)
                    for k,v in enumerate(weights):nxt[k]+=a[r]*v;nxt[k+1]+=v
                    weights=nxt
                ones=sum(step==1 for r,step in edges);twos=len(edges)-ones
                stepweight=mp.fprod(s[r]**2 if step==1 else s[r]*s[r-1] for r,step in edges)
                for xx in range(ones+1):
                    e=(twos+xx,i,N-1-j,twos+ones-xx)
                    for k,v in enumerate(weights):
                        coeff[(e,k)]=coeff.get((e,k),0)+v*stepweight*mp.binomial(ones,xx)
                counts['localized_repair_paths']+=1
        for (e,k),v in coeff.items():
            if not v:continue
            base=coeff.get((e,0),0)
            assert base>0,(N,e,k)
            assert v<=mp.binomial(N,k)*C**k*base*(1+mp.mpf('1e-60')),(N,e,k)
            counts['localized_derivative_coefficient_bounds']+=1
    counts['nodal_cofactor_coefficient_bounds']=0
    for N in range(3,19):
        J=(N-1)//2;th=mp.pi/N
        aa=[4*mp.cos((j+mp.mpf('.5'))*th)**2 for j in range(J+1)]
        if N%2:aa[J]=mp.mpf(0)
        ss=[2*mp.sin(j*th) for j in range(J+1)]
        def rr(u):
            seq=[];pref=mp.mpf(1)
            for j in range(J+1):
                out={(0,j,0):pref}
                if j:
                    for (xx,bb,yy),v in seq[-1].items():
                        for e in [(xx+1,bb,yy),(xx,bb,yy+1)]:out[e]=out.get(e,0)+ss[j]**2*v
                if j>1:
                    for (xx,bb,yy),v in seq[-2].items():
                        e=(xx+1,bb,yy+1)
                        out[e]=out.get(e,0)+ss[j]*ss[j-1]*(aa[j-1]+u)*v
                seq.append(out);pref*=aa[j]+u
            return seq
        base=rr(0)
        for node in aa:
            values=rr(-node)
            for j,pol in enumerate(values):
                for e,v in pol.items():
                    b0=base[j][e];tol=mp.mpf('1e-55')*max(1,b0)
                    assert v>=-tol and v<=b0+tol,(N,j,node,e,v,b0)
                    counts['nodal_cofactor_coefficient_bounds']+=1
    return {'status':'PASS','counts':counts,'repair_precision':mp.mp.dps,
            'scope':'Exact cleared cross polynomial versus original full-numerator unused-row paths at both parities; original-path coefficient checks of the central-strip repair bound and all-node lower-cofactor positivity. No fixed-complex relative packet or cycle estimate.'}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',default=str(Path(__file__).with_name('actual_cross_cofactor_factorization_results.json')));args=ap.parse_args()
    result=run();Path(args.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
