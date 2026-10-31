"""Original level-N recurrence checks for the protected-middle angular lemma."""
import argparse
from collections import Counter,defaultdict
import json
from pathlib import Path
import mpmath as mp
import sympy as sp

parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,default=Path(__file__).with_name('actual_cross_cofactor_protected_angular_gap_results.json'))
args=parser.parse_args()
mp.mp.dps=70
counts=Counter(); worst=mp.mpf(0)
tt,jj=sp.symbols('tt jj', real=True)
expr=8*sp.sin(jj*tt)*sp.sin((jj-1)*tt)+4*sp.cos((jj-sp.Rational(1,2))*tt)**2-1
assert sp.trigsimp(sp.expand_trig(expr-(4*sp.cos(tt)+1-2*sp.cos((2*jj-1)*tt))))==0
counts['exact_level_identity']+=1

def coefficients(N,n):
    old={(0,0):mp.mpf(1)};older={};theta=mp.pi/N
    for j in range(1,n+1):
        sj=2*mp.sin(j*theta);sm=2*mp.sin((j-1)*theta)
        aa=4*mp.cos((j-mp.mpf('.5'))*theta)**2
        out=defaultdict(mp.mpf)
        for (i,k),v in old.items():
            out[i+1,k]+=sj*sj*v;out[i,k]+=sj*sj*v
        for (i,k),v in older.items():
            out[i+1,k]+=sj*sm*aa*v;out[i+1,k+1]+=sj*sm*v
        older,old=old,dict(out)
    return old

for N in range(3,41):
    for n in sorted(set((max(0,N//2-2),N//2-1,N//2))):
        co=coefficients(N,n)
        for (i,k),value in co.items():
            bound=mp.binomial(n,k)*co[i,0]
            assert value<=bound*(1+mp.mpf('1e-60'))
            counts['original_coefficientwise_spectral_bounds']+=1

def recurrence(N,n,x,y,w):
    old=mp.mpf(1);older=mp.mpf(0);theta=mp.pi/N
    for j in range(1,n+1):
        sj=2*mp.sin(j*theta);sm=2*mp.sin((j-1)*theta)
        aa=4*mp.cos((j-mp.mpf('.5'))*theta)**2
        new=sj*sj*(x+y)*old+sj*sm*(aa+w)*x*y*older
        older,old=old,new
    return old

beta0=16*mp.sin(mp.pi/8)**4/(16*mp.sin(mp.pi/8)**4+5)
max_actual_gap_ratio=mp.mpf(0)
for N in (64,65,128,129,256,257):
    for x0,y0 in ((1,1),(2,5),(mp.mpf('.3'),4)):
        x0=mp.mpf(x0);y0=mp.mpf(y0);A=x0+y0;P=x0*y0
        for eps in (mp.pi/7,mp.pi/2,mp.pi):
            rr=mp.sqrt(max(mp.mpf(0),1-4*P/A**2*mp.sin(eps/2)**2))
            eta=(1-rr)*beta0
            for w in (mp.mpf(0),eta/16,mp.mpc(eta/32,eta/40)):
                for n in sorted(set((N//2-2,N//2-1,N//2))):
                    actual=abs(recurrence(N,n,x0*mp.exp(1j*eps),y0,w))
                    reference=recurrence(N,n,x0,y0,0)
                    allowed=mp.exp(-eta*N/32)*reference
                    assert actual<=allowed*(1+mp.mpf('1e-55'))
                    max_actual_gap_ratio=max(max_actual_gap_ratio,actual/allowed)
                    counts['actual_complex_angular_bounds']+=1
            # Check the entrywise block comparison separately on actual rows.
            v=mp.mpf(1)
            def transfer(j,r):
                sj=2*mp.sin(mp.pi*j/N);sm=2*mp.sin(mp.pi*(j-1)/N)
                aa=4*mp.cos(mp.pi*(j-mp.mpf('.5'))/N)**2
                return mp.matrix([[r*sj*sj*A,sj*sm*(aa+v)*P],[1,0]])
            for end in (int(mp.ceil(N/8))+2,int(mp.floor(3*N/8))):
                lhs=transfer(end,rr)*transfer(end-1,rr)*transfer(end-2,rr)
                rhs=(1-eta)*transfer(end,1)*transfer(end-1,1)*transfer(end-2,1)
                for a,b in zip(lhs,rhs):
                    assert a<=b*(1+mp.mpf('1e-60'))
                    counts['actual_three_step_entry_bounds']+=1

for N in (16,17,64,65):
    n=N//2
    for x,y in ((mp.mpc(2,1),0),(0,mp.mpc('.7','-.3'))):
        for w in (mp.mpc('.2','.1'),mp.mpf(-1)):
            direct=recurrence(N,n,x,y,w)
            expected=(x+y)**n*mp.fprod((2*mp.sin(mp.pi*j/N))**2 for j in range(1,n+1))
            err=abs(direct-expected)/max(1,abs(expected));worst=max(worst,err)
            assert err<mp.mpf('1e-60')
            counts['exact_monomer_specializations']+=1

out={'status':'PASS','precision':mp.mp.dps,'counts':dict(counts),
     'max_actual_to_angular_bound_ratio':str(max_actual_gap_ratio),
     'max_monomer_relative_error':str(worst),
     'scope':'Actual protected b=0 recurrence, coefficientwise spectral repair, bulk transfer entries and fixed-complex angular bound. No whole shared-face torus or filling-cycle assertion.'}
args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
