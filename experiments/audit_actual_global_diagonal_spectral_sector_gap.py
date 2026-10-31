"""Actual path diagonal coefficients and original sewn-sector endpoint/IBP checks.

This supplements, but does not numerically prove, the uniform entropy gap.
"""
import argparse,json,sys
from collections import Counter,defaultdict
from pathlib import Path
from types import SimpleNamespace
import sympy as sp
import mpmath as mp
sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_actual_gaussian_resolvent_numerator_and_cap import finite_H,paths
from audit_actual_original_marked_face_coefficient import morse_faces

ap=argparse.ArgumentParser()
ap.add_argument('--output',type=Path,default=Path(__file__).with_name('actual_global_diagonal_spectral_sector_gap_results.json'))
args=ap.parse_args();counts=Counter();mp.mp.dps=65
errors=defaultdict(mp.mpf)

def check(label,a,b,tol=mp.mpf('1e-45')):
    err=abs(a-b)/max(1,abs(a),abs(b));errors[label]=max(errors[label],err)
    counts[label]+=1
    assert err<tol,(label,err,a,b)

# Compare the diagonal of the full ORIGINAL unused-row path polynomial with
# independent scalar synthetic division of the Chebyshev polynomial.
z=sp.Symbol('z')
for N in range(3,14):
    mult=20
    while not sp.isprime(2*N*mult+1):mult+=1
    prime=2*N*mult+1;q=pow(int(sp.primitive_root(prime)),mult,prime)
    loc=SimpleNamespace(N=N,p=prime,q=q,Q=q*q%prime)
    nodes=[(q*pow(loc.Q,j,prime)+pow(q,-1,prime)*pow(loc.Q,-j,prime))%prime for j in range(N)]
    chi=[int(c)%prime for c in sp.Poly(2*sp.chebyshevt(N,z/2)+2,z).all_coeffs()]
    quotients=[]
    for node in nodes:
        qq=[chi[0]]
        for coefficient in chi[1:-1]:qq.append((coefficient+node*qq[-1])%prime)
        assert (chi[-1]+node*qq[-1])%prime==0
        quotients.append(qq)
    for sigma in sorted(set([0,2,prime-2,5,11]+nodes)):
        H=finite_H(loc,sigma)
        for j,qq in enumerate(quotients):
            val=0
            for coefficient in qq:val=(val*sigma+coefficient)%prime
            assert H.get((0,j,N-1-j,0),0)==val
            counts['original_zero_step_vs_divided_chebyshev']+=1
            if sigma in nodes:counts['removable_node_values']+=1
        # Disjoint DIAG + strict CROSS removes the odd central path once.
        m=N//2;upper=m-(N%2==0)
        diag={e:v for e,v in H.items() if e[0]+e[3]==0}
        cross={e:v for e,v in H.items() if e[1]<=upper and e[2]<=upper and e[0]+e[3]>0}
        assert not diag.keys()&cross.keys()
        counts['disjoint_parity_sectors']+=1

def polymul(a,b):
    out=[mp.mpf(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def path_polynomials(N,kind):
    theta=mp.pi/N;nodes=[2*mp.cos((2*j+1)*theta) for j in range(N)]
    out={};m=N//2;upper=m-(N%2==0)
    for j in range(N):
        for i,edges,vis in paths(N,j):
            if kind=='diag' and edges:continue
            if kind=='cross' and (not edges or i>upper or N-1-j>upper):continue
            pol=[mp.mpf(1)]
            for row in range(N):
                if row not in vis:pol=polymul(pol,[-nodes[row],1])
            ones=sum(step==1 for row,step in edges);twos=len(edges)-ones
            weight=mp.mpf((-1)**len(edges))
            for row,step in edges:
                weight*=4*mp.sin(row*theta)**2 if step==1 else 4*mp.sin(row*theta)*mp.sin((row-1)*theta)
            for k in range(ones+1):
                ex=(twos+k,i,N-1-j,twos+ones-k)
                value=[v*weight*mp.binomial(ones,k) for v in pol]
                if ex not in out:out[ex]=[mp.mpf(0)]*N
                for l,v in enumerate(value):out[ex][l]+=v
    return out

def evaluate(p,sigma):return mp.polyval(list(reversed(p)),sigma)

def sewn_univariate(N,chart,diagport,variable):
    d=N-1;nf=chart['faces'];target=tuple(0 if f in (0,chart['v']) else d for f in range(nf))
    product={(0,)*nf:[mp.mpf(1)]}
    for port,ids in enumerate(chart['circles']):
        local=path_polynomials(N,'diag' if port==diagport else 'cross')
        sigma=-2*mp.cos(2*mp.pi*mp.mpf(port+1)/17)
        fac={}
        for e,pol in local.items():
            ex=[0]*nf
            for f,v in zip(ids,e):ex[f]+=v
            if any(v>t for v,t in zip(ex,target)):continue
            ex=tuple(ex); pp=pol if port==variable else [evaluate(pol,sigma)]
            if ex not in fac:fac[ex]=[mp.mpf(0)]*len(pp)
            for k,v in enumerate(pp):fac[ex][k]+=v
        new={}
        for a,pa in product.items():
            for b,pb in fac.items():
                ex=tuple(v+w for v,w in zip(a,b))
                if any(v>t for v,t in zip(ex,target)):continue
                pp=polymul(pa,pb)
                if ex not in new:new[ex]=[mp.mpf(0)]*len(pp)
                for k,v in enumerate(pp):new[ex][k]+=v
        product=new
    return product.get(target,[mp.mpf(0)]*N)

def Bjet(t,N,n,pol):
    a=2*mp.pi;sigma=-2*mp.cos(a*t)
    sj=[sigma,2*a*mp.sin(a*t),2*a*a*mp.cos(a*t),-2*a**3*mp.sin(a*t)]
    pp=[pol]
    for r in range(3):pp.append([(j+1)*v for j,v in enumerate(pp[-1][1:])])
    pv=[evaluate(v,sigma) if v else 0 for v in pp]
    S=[pv[0],pv[1]*sj[1],pv[2]*sj[1]**2+pv[1]*sj[2],
       pv[3]*sj[1]**3+3*pv[2]*sj[1]*sj[2]+pv[1]*sj[3]]
    sine=[mp.sin(a*t),a*mp.cos(a*t),-a*a*mp.sin(a*t),-a**3*mp.cos(a*t)]
    pre=[sum(mp.binomial(k,j)*sine[j]*S[k-j] for j in range(k+1)) for k in range(4)]
    vv=2j*mp.pi*N*n*t;dv=2j*mp.pi*N*n;gg=mp.exp(1j*mp.pi*N*n*t*t)
    gj=[gg,vv*gg,(vv*vv+dv)*gg,(vv**3+3*vv*dv)*gg]
    return [sum(mp.binomial(k,j)*pre[j]*gj[k-j] for j in range(k+1)) for k in range(4)]

nonzero=0
for N in (3,4,5):
    chart=morse_faces(2,[1,0,1],1)
    for diagonal in range(3):
        for variable in (diagonal,(diagonal+1)%3):
            pol=sewn_univariate(N,chart,diagonal,variable)
            counts['original_marked_sector_polynomials']+=1
            if max(map(abs,pol))<mp.mpf('1e-45'):continue
            nonzero+=1
            for n in (2,-3):
                lo=Bjet(-mp.mpf('.5'),N,n,pol);hi=Bjet(mp.mpf('.5'),N,n,pol)
                check('original_endpoint_zero',lo[0],0)
                check('original_endpoint_zero',hi[0],0)
                check('original_first_endpoint_match',lo[1],hi[1])
                for ell in (1,-2):
                    omega=2*mp.pi*N*ell
                    phase=lambda t:mp.exp(1j*omega*t)
                    mesh=[-mp.mpf('.5')+mp.mpf(k)/16 for k in range(17)]
                    original=mp.quad(lambda t:Bjet(t,N,n,pol)[0]*phase(t),mesh)
                    third=mp.quad(lambda t:Bjet(t,N,n,pol)[3]*phase(t),mesh)
                    boundary=hi[2]*phase(mp.mpf('.5'))-lo[2]*phase(-mp.mpf('.5'))
                    reconstructed=(boundary-third)/(1j*omega)**3
                    check('original_sector_three_IBP_identity',original,reconstructed)
                    counts['nonzero_second_endpoint_currents']+=abs(boundary)>mp.mpf('1e-40')
assert nonzero>0
out={'status':'PASS','precision':mp.mp.dps,'counts':dict(counts),
     'nonzero_sewn_sector_polynomials':nonzero,'maximum_relative_errors':{k:str(v) for k,v in errors.items()},
     'scope':'Actual unused-row zero-step coefficients at ordinary and removable spectral values, and actual marked flat-plat DIAG/CROSS sector endpoint/three-IBP identities. No finite numerical test substitutes for the compact entropy gap or infinite charge estimate.'}
args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
