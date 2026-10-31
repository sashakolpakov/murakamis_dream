import argparse
import json
from collections import defaultdict, Counter
from pathlib import Path
import mpmath as mp

parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,default=Path(__file__).with_name('actual_fejer_forest_transfer_results.json'))
args=parser.parse_args()
mp.mp.dps=90
tol=mp.mpf('1e-65')
counts=Counter();err=mp.mpf(0)

def add(dst,src,scalar=1,shift=(0,0,0,0)):
    for e,v in src.items():dst[tuple(a+b for a,b in zip(e,shift))]+=scalar*v

def mul(a,b):
    out=defaultdict(mp.mpf)
    for e,v in a.items():
        for f,w in b.items():out[tuple(x+y for x,y in zip(e,f))]+=v*w
    return out

def polys(M,A,s):
    out=[{(0,0,0,0):mp.mpf(1)}]
    for j in range(1,M+1):
        p=defaultdict(mp.mpf)
        p[0,j,0,0]=mp.fprod(A[:j])
        add(p,out[j-1],s[j]**2,(1,0,0,0))
        add(p,out[j-1],s[j]**2,(0,0,0,1))
        if j>=2:add(p,out[j-2],s[j]*s[j-1]*A[j-1],(1,0,0,1))
        out.append(dict(p))
    return out

def dominated(left,right,label):
    for e in set(left)|set(right):
        l,r=left.get(e,0),right.get(e,0)
        assert l<=r+tol*max(1,abs(l),abs(r)),(label,e,l,r)
        counts[label]+=1

def value(poly,weights):
    return mp.fsum(v*mp.fprod(w**a for w,a in zip(weights,e)) for e,v in poly.items())

for N in range(4,31,2):
    m=N//2;M=m-1;theta=mp.pi/N
    cs=[2*mp.cos((2*j+1)*theta) for j in range(m)]
    A=[2+c for c in cs];delta=A[-1];s=[2*mp.sin(j*theta) for j in range(m)]
    As=[c-cs[-1] for c in cs]
    R=polys(M,A,s);Rs=polys(M,As,s)
    CN=4*(4-delta)/(delta*N*N)
    front=mp.fprod(As[:M])
    for lhs,rhs in [(front,N/mp.sqrt(delta*(4-delta))),
                    (mp.fsum(1/a for a in A),mp.mpf(N*N)/8),
                    (mp.sqrt(CN)*N/(4*front),(4-delta)/(2*N))]:
        err=max(err,abs(lhs-rhs)/max(1,abs(rhs)))
        counts['normalization_identities']+=1
    for j in range(M):
        shifted=defaultdict(mp.mpf);add(shifted,R[j],A[j],(0,1,0,0))
        dominated(shifted,R[j+1],'path_injection_coefficients')
    dominated(R[-1],{e:mp.sqrt(CN)*v for e,v in Rs[-1].items()},'paired_root_comparisons')
    Dc={(e[0],0,e[1],e[3]):v for e,v in Rs[-1].items()}
    Hbar={e:8*v/N for e,v in mul(Rs[-1],Dc).items()}
    H=defaultdict(mp.mpf);add(H,Hbar,shift=(1,0,0,0));add(H,Hbar,shift=(0,0,0,1))
    left=defaultdict(mp.mpf)
    transfer=defaultdict(mp.mpf)
    for j in range(m):
        add(left,R[j],2*mp.fprod(A[j+1:]),(0,0,m+M-j,0))
        add(transfer,Hbar,(4-delta)/(2*N)*delta/A[j],(0,-(M-j),M-j+1,0))
    dominated(left,transfer,'full_laurent_transfer_coefficients')
    for weights in [(1,1,1,1),(2,3,1,5),(1,7,mp.mpf('0.1'),2)]:
        x,b,c,y=map(mp.mpf,weights)
        actual=value(left,(x,b,c,y))/value(H,(x,b,c,y))
        bound=N*mp.sin(theta)**2/4*c/(x+y)
        assert actual<=bound+tol
        counts['downhill_radius_checks']+=1
    counts['levels']+=1
assert err<tol
out={'status':'PASS','precision':mp.mp.dps,'counts':dict(counts),'maximum_normalization_error':str(err),
 'scope':'Literal level-N half-block recurrence, exact path-injection and Laurent coefficient bounds; no universal forest capacity comparison.'}
args.output.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
