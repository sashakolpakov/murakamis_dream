#!/usr/bin/env python3
"""Audit the actual source family used by the cotangent homology obstruction.

No replacement norm or root invariant. Markov traces use literal physical
R matrices and every new original pivot. High states use independently
evaluated universal R coefficients, not the asymptotic product formula.
"""
from pathlib import Path
import json
import mpmath as mp
import numpy as np
from audit_actual_projected_transfer_cot_completion import Projected


def actual_diagonal(n, a, b, sign):
    q=mp.exp(mp.j*mp.pi/n);Q=q*q;x=-1/q
    rho=q-1/q;kap=mp.exp(mp.j*mp.pi*(n-1)**2/(2*n))
    k=a-b if sign>0 else b-a
    assert 0<=k<n
    fac=mp.mpc(1)
    for j in range(1,k+1):fac*=(q**j-q**(-j))/rho
    source=a if sign>0 else b
    ec=mp.fprod(((q**(source-j)-q**(-source+j))/rho)**2 for j in range(k))
    if sign>0:
        return kap*rho**k/fac*q**(mp.mpf(k*(k-1))/2)*ec*x**(-a-b)*Q**((a-k)*(b+k))
    return (kap**(-1)*(-1)**k*rho**k/fac*q**(-mp.mpf(k*(k-1))/2)
            *ec*x**(a+b)*Q**(-a*b))


def original_markov_checks():
    rows=[]
    for n in range(2,8):
        p=Projected(n)
        x=complex(p.x);Q=complex(p.Q);kap=complex(p.kappa)
        theta=x**(1-n)
        g=[theta*Q**(-j) for j in range(n)]
        for sig in (1,-1):
            R=p.original(sig)
            cut=np.zeros((n,n),complex)
            for a in range(n):
                for c in range(n):
                    cut[c,a]=sum(g[b]*R[c*n+b,a*n+b] for b in range(n))
            mu=(kap*theta)**sig
            err=np.linalg.norm(cut-mu*np.eye(n))/max(1,np.linalg.norm(cut))
            assert err<1e-11,(n,sig,err)
            assert abs(abs(mu)-1)<1e-12
            rows.append({"N":n,"sign":sig,"all_cut_columns":n,
                         "original_pivotal_trace_relative_error":float(err),
                         "framing_markov_unit_modulus":abs(mu)})
    return rows


def diagonal_and_states():
    v8=4*mp.catalan
    rows=[]
    for n in (8,12,16,24,32,64,128):
        q=mp.exp(2*mp.j*mp.pi/n)
        fs=[mp.mpc(1)]
        for j in range(1,n):fs.append(fs[-1]*(1-q**j))
        a,b,k=3*n//4,n//4,n//2
        plus=actual_diagonal(n,a,b,1)
        minus=actual_diagonal(n,b,a,-1)
        magnitude=abs(fs[a]**2/(fs[k]*fs[b]**2))
        assert abs(abs(plus)/magnitude-1)<mp.mpf('1e-70')
        assert abs(minus/mp.conj(plus)-1)<mp.mpf('1e-70')
        reference=mp.exp(n*v8/(2*mp.pi))/mp.sqrt(2*n)
        ratio=magnitude/reference
        assert n*abs(ratio-1)<5,(n,ratio)
        # A literal stabilized figure-eight SOURCE STATE, with the old
        # crossing transfers zero. This construction works for any old word.
        for stabilizations in (1,2,3,4):
            oldword=[1,-2,1,-2];width=3
            initial=[a]*width+[b if j%2==0 else a for j in range(stabilizations)]
            heads=initial.copy();weight=mp.mpc(1)
            for letter in oldword:
                i=abs(letter)-1;aa,bb=heads[i:i+2]
                assert aa==bb
                sig=1 if letter>0 else -1
                weight*=actual_diagonal(n,aa,bb,sig)
                heads[i:i+2]=[bb,aa]
            for j in range(stabilizations):
                i=width-1+j;sig=1 if j%2==0 else -1
                aa,bb=heads[i:i+2]
                transfer=aa-bb if sig>0 else bb-aa
                assert transfer==k
                weight*=actual_diagonal(n,aa,bb,sig)
                heads[i:i+2]=[bb+sig*transfer,aa-sig*transfer]
            assert heads==initial
            x=-mp.exp(-mp.j*mp.pi/n);theta=x**(1-n)
            # Every old/new unmarked head retains its original pivot.
            pivot=mp.fprod(theta*q**(-value) for value in initial[1:])
            actual=weight*pivot/n # exactly ONE original averaged-cut factor.
            assert abs(abs(actual)/(magnitude**stabilizations/n)-1)<mp.mpf('1e-70')
        rows.append({"N":n,"positive_negative_universal_comparison":True,
                     "diagonal_asymptotic_ratio":float(ratio),
                     "single_state_rate":float(mp.log(magnitude)/n),
                     "stabilized_source_states_with_all_pivots":4})
    return rows


def main():
    mp.mp.dps=100
    result={"status":"PASS","original_markov_pivotal_cuts":original_markov_checks(),
            "actual_diagonal_and_stabilized_states":diagonal_and_states(),
            "scope":"Source-homology barrier for universal undecomposed contour transport; exact pruning and source-specific current recombination are not excluded."}
    target=Path(__file__).with_suffix('.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS:12 complete original signed Markov traces;14 independent universal diagonal coefficients;'
          '28 stabilized source states retaining every new pivot and the single average')
    print(target)


if __name__=='__main__':main()
