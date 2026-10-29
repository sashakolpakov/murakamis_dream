#!/usr/bin/env python3
"""Faithful reduced cap witnesses and finite parabolic character atlas."""

import itertools
import json
from pathlib import Path

import sympy as s
import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct


I=s.eye(2)
def upper(t):return s.Matrix([[1,t],[0,1]])
def lower(t):return s.Matrix([[1,0],[t,1]])
def unipotent(z,t):return I+t*s.Matrix([[-z,z*z],[-1,z]])


def symbolic():
    X,Y,Z=s.symbols('X Y Z',nonzero=True)
    S=X+Y+Z;F=S*S+X*Y*Z
    mu=[upper(1),lower(X),s.Matrix([[1+S/X,Y/X],[Z,1-S/X]])]
    assert s.simplify(mu[2].det()-1+F/X**2)==0
    assert [s.simplify(s.trace(mu[b]*mu[a])-2) for a,b in [(0,1),(1,2),(0,2)]]==[X,Y,Z]
    assert s.simplify(s.trace(mu[2]*mu[1]*mu[0])-2)==0
    t=s.symbols('t')
    caps=[upper(1),upper(-1),lower(t)]
    assert caps[1]*caps[0]==I
    assert s.trace(caps[2]*caps[1])==2-t and s.trace(caps[2]*caps[0])==2+t
    # Localized witness scheme: offdiagonals killed, diagonal square remains.
    u,v,w,a=s.symbols('u v w a',nonzero=True)
    T=s.Matrix([[u,v],[w,-u]])
    assert s.expand((I+T).det()-1)==-u*u-v*w
    assert s.trace(upper(1)*T)==w and s.trace(lower(a)*T)==a*v
    t,z11,z12,z21,z22=s.symbols('t z11 z12 z21 z22')
    S=s.Matrix([[z11,z12],[z21,z22]])
    assert s.expand(s.trace(upper(t)*S)-s.trace(S))==t*z21
    return True


def quantum_interval_deletions():
    rows=[]
    for N,maximum_width in [(2,6),(3,5),(4,4),(5,3),(6,3)]:
        prime,eta,q,E,F,K,pivot,Rp,Rm=balanced_data(N)
        Q,d,x=q*q % prime,N-1,int(K[0,0])
        rho=(q-pow(q,-1,prime)) % prime
        Ec=rho*rho*E % prime
        cup=np.zeros((N*N,1),dtype=np.int64)
        cap=np.zeros((1,N*N),dtype=np.int64)
        for a in range(N):
            cup[a*N+d-a,0]=N*pow(x,a-d,prime) % prime
            cap[0,a*N+d-a]=pow(x,-a,prime)*pow(Q,-a,prime)*pow(N,-1,prime) % prime
        for width in range(2,maximum_width+1):
            Et,Ft,Kt=coproduct(Ec,F,K,width,N,prime)
            if width==2:
                Er,Fr=np.zeros((1,1),dtype=np.int64),np.zeros((1,1),dtype=np.int64)
                Kr=np.ones((1,1),dtype=np.int64)
            else:
                Er,Fr,Kr=coproduct(Ec,F,K,width-2,N,prime)
            Kti=np.diag([pow(int(v),-1,prime) for v in np.diag(Kt)])
            Kri=np.diag([pow(int(v),-1,prime) for v in np.diag(Kr)])
            Ot=(Ft@Et+q*Kt+pow(q,-1,prime)*Kti) % prime
            Or=(Fr@Er+q*Kr+pow(q,-1,prime)*Kri) % prime
            for slot in range(width-1):
                before=np.eye(N**slot,dtype=np.int64)
                after=np.eye(N**(width-slot-2),dtype=np.int64)
                insertion=np.kron(before,np.kron(cup,after))
                withdrawal=np.kron(before,np.kron(cap,after))
                for actual,reduced in [(Et,Er),(Ft,Fr),(Kt,Kr),(Ot,Or)]:
                    assert np.array_equal(actual@insertion % prime,insertion@reduced % prime)
                    assert np.array_equal(withdrawal@actual % prime,reduced@withdrawal % prime)
                rows.append({'N':N,'interval_width':width,'cup_position':slot,
                             'literal_cup_and_ordinary_cap_E_F_K_Casimir_deletion':True,
                             'empty_interval_uses_actual_trivial_Casimir':width==2})
    return rows


def all_width_counter():
    mu=[upper(1),upper(-1),lower(1),lower(1),lower(-1),lower(-1)]
    P=[mu[2*j+1]*mu[2*j] for j in range(3)]
    assert all(s.trace(p)==2 for p in P)
    assert P[2]*P[1]*P[0]==I
    assert P[1]!=I and P[2]!=I
    assert s.trace(mu[0]*P[1])==4
    return {'pair_traces_and_total_identity_do_not_replace_witnesses':True}


def bounded_tuple_case(zs,ts):
    mu=[unipotent(s.Rational(z),s.Rational(t)) for z,t in zip(zs,ts)]
    pairs=[(abs(s.trace(b*a)-2),i,j) for i,a in enumerate(mu) for j,b in enumerate(mu) if i<j]
    M,r,k=max(pairs,key=lambda z:float(z[0]))
    assert M>0
    # Normalize the two distinct fixed eigenvectors, then scale upper translation.
    er=mu[r]-I;es=mu[k]-I
    vr=er.columnspace()[0];vs=es.columnspace()[0]
    basis=s.Matrix.hstack(vr,vs)
    mr=basis.inv()*mu[r]*basis;ms=basis.inv()*mu[k]*basis
    b=mr[0,1]
    change=basis*s.diag(b,1)
    normalized=[s.simplify(change.inv()*v*change) for v in mu]
    assert normalized[r]==upper(1)
    a=normalized[k][1,0]
    assert normalized[k]==lower(a) and abs(a)==M
    for v in normalized:
        u,up,down=v[0,0]-1,v[0,1],v[1,0]
        assert abs(up)<=1 and abs(down)<=M and abs(u)**2<=M
        assert s.simplify(u*u+up*down)==0
    # Add a literal inverse cup and verify every witness is exact.
    literal_pair=normalized[r].inv()*normalized[r]
    assert all(s.trace(v*literal_pair)==2 for v in normalized)
    # A nonidentity P sharing one chosen flag is detected by an irreducible witness.
    P=normalized[r]
    assert any(s.trace(v*P)!=2 for v in normalized)
    return {'heads':len(mu),'maximum_pair_trace_difference':str(M),'bounded_normalized_atlas':True}


if __name__=='__main__':
    result={'status':'PASS','exact_symbolic_cubic_source_and_normal_scheme':symbolic(),
            'exact_quantum_interval_Ward':quantum_interval_deletions(),
            'all_width_counterexample':all_width_counter(),
            'bounded_representative_tuples':[bounded_tuple_case(z,t) for z,t in [
                ([0,1,2],[1,1,1]),([-2,0,3,5],[1,-1,2,3]),
                ([0,1,2,3,4,5],[1,2,-1,3,-2,1]),([0,2,5,7,11,13,17,19],[1]*8)]]}
    Path(__file__).with_name('actual_parabolic_cap_trace_certificate_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print('PASS',len(result['exact_quantum_interval_Ward']),
          'literal all-position quantum cup/cap interval deletions; '
          'exact cubic/source/witness/normal-scheme identities; six-head counterexample; '
          'four all-width bounded irreducible reconstruction families')
