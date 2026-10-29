#!/usr/bin/env python3
"""Principal geometric density versus the intrinsic holonomy torsion.

The evaluator accepts any braid and regular fixed representation.
Figure-eight and 5_2 are prototype tests for a uniform determinant lemma.
No selected global quantum-period volume theorem is asserted.
"""

from itertools import combinations
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_cut_density import fixed_point_complex_case
from audit_actual_normal_stationary_period import (
    closure_embedding, crossing, inverse, jet_field, local_hessian, matmul)
from audit_cyclic_steinberg_lattice import determinant,rank


WORDS = {'4_1':[(0,1),(1,-1),(0,1),(1,-1)],
         '5_2':[(0,1),(0,1),(0,1),(1,1),(0,-1),(1,1)]}


def parabolic_meridians(p,t,knot):
    mm=lambda a,b:a@b%p
    def mi(a):
        assert (a[0,0]*a[1,1]-a[0,1]*a[1,0])%p==1
        return np.array([[a[1,1],-a[0,1]],[-a[1,0],a[0,0]]],dtype=np.int64)%p
    A=np.array([[1,1],[0,1]],dtype=np.int64)
    B=np.array([[1,0],[t,1]],dtype=np.int64)
    if knot=='4_1':
        C=mm(mm(mm(mm(mi(A),B),A),mi(B)),A)
    else:
        D=mm(mm(mi(A),B),A)
        E=mm(mm(mi(D),A),D)
        C=mm(mm(E,A),mi(E))
    return [A,B,C]


def normal_density(p,raw_meridians,word,frame):
    J=jet_field(p);M=J(1);x=-M
    r,s=J(frame[0],(1,0,0)),J(frame[1],(0,1,0))
    F=(r,1-r,s,-s)
    holonomies=[]
    for raw in raw_meridians:
        matrix=tuple(J(int(v)) for v in raw.flat)
        holonomies.append(tuple(-v for v in matmul(matmul(inverse(F),matrix),F)))
    previous=(J(1),J(0),J(0),J(1));states=[]
    for H in holonomies:
        G=matmul(matmul(previous,H),inverse(previous))
        k,e,f=G[0],G[1],G[2]/G[0]
        states.append((k,e,f))
        previous=matmul((J(1),J(0),-k*f,k),previous)
    initial=list(states);b=len(states);d=len(word)+1
    maps=closure_embedding(b,word)
    H=np.zeros((d,d),dtype=np.int64)
    free=[x/states[0][0]];amplitude=1
    for n,(j,sign) in enumerate(word):
        k,e,f=states[j];l,g,h=states[j+1]
        A,B=x/k,x/l
        C=1/(1-e*h) if sign>0 else 1-k*g*f/l
        free.append(C)
        local,amp=local_hessian(A,B,C,M,sign,J)
        matrix=np.array([[local[i][j].v for j in range(3)] for i in range(3)],dtype=np.int64)
        P=maps[n]
        H=(H+P.T@matrix@P)%p
        amplitude=amplitude*amp.v%p
        states[j:j+2]=crossing(states[j],states[j+1],sign)
    assert states==initial
    for state in initial[1:]:
        amplitude=amplitude*pow((x/state[0]).v,-2,p)%p
    tangent=np.array([[value.d[j]*pow(value.v,-1,p)%p for j in range(2)] for value in free],dtype=np.int64)
    assert rank(tangent,p)==2 and rank(H,p)==d-2
    assert not np.any(H@tangent%p)
    chi=next(pair for pair in combinations(range(d),2) if determinant(tangent[list(pair),:],p))
    transverse=[i for i in range(d) if i not in chi]
    hn=determinant(H[np.ix_(transverse,transverse)],p)
    assert hn
    gauge=determinant(tangent[list(chi),:],p)
    omega=pow(-1,d-2,p)*amplitude*gauge*gauge*pow(hn,-1,p)%p
    return {'phase_variables':d,'normal_Hessian_rank':d-2,
            'raw_framing_two_form_squared':int(omega),
            'parity_normalized_framing_two_form_squared':int(pow(-1,b-1,p)*omega%p)}


def inspect_case(p,t,knot,frame):
    raw=parabolic_meridians(p,t,knot);word=WORDS[knot]
    normal=normal_density(p,raw,word,frame)
    torsion=fixed_point_complex_case(p,t,frame,base_meridians=raw,braid_word=word)['torsion']
    s=frame[1]
    ratio=normal['parity_normalized_framing_two_form_squared']*s*s*(1+s)**2*pow(torsion,-1,p)%p
    assert ratio == -pow(2,-1,p)%p
    return {'knot':knot,'prime':p,'trace_parameter':t,'frame':list(frame),
            'intrinsic_holonomy_torsion':torsion,'density_to_torsion_and_cut_form_ratio':int(ratio),**normal}


if __name__=='__main__':
    from functools import reduce
    t=sp.symbols('t');symbolic=[]
    for knot in ('4_1','5_2'):
        A=sp.Matrix([[1,1],[0,1]]);B=sp.Matrix([[1,0],[t,1]])
        if knot=='4_1':C=A.inv()*B*A*B.inv()*A
        else:
            D=A.inv()*B*A;E=D.inv()*A*D;C=E*A*E.inv()
        initial=[A,B,C];moved=list(initial)
        for j,sign in WORDS[knot]:
            a,b=moved[j:j+2]
            moved[j:j+2]=[a.inv()*b*a,a] if sign>0 else [b,b*a*b.inv()]
        polys=[sp.expand(x-y) for a,b in zip(moved,initial) for x,y in zip(a,b) if sp.expand(x-y)!=0]
        common=sp.Poly(reduce(sp.gcd,polys),t).monic().as_expr()
        expected=t*t-t+1 if knot=='4_1' else t**3+t*t+2*t+1
        assert common==expected
        symbolic.append({'knot':knot,'exact_nonabelian_fixed_point_polynomial':str(common)})
    records=[]
    for knot,p in (('4_1',97),('5_2',101)):
        roots=[t for t in range(p) if ((t*t-t+1) if knot=='4_1' else (t**3+t*t+2*t+1))%p==0]
        for t in roots:
            for frame in ((2,3),(3,2),(4,5),(5,3),(2,7),(7,2)):
                try:
                    record=inspect_case(p,t,knot,frame)
                except ZeroDivisionError:
                    continue
                records.append(record)
    path=Path(__file__).with_name('geometric_a_density_results.json')
    path.write_text(json.dumps({'scope':'Prototype checks accompanying the separate characteristic-zero proof; no general identity or volume theorem asserted.',
                               'exact_symbolic_holonomy':symbolic,'records':records},indent=2)+'\n')
    print(json.dumps({'results':str(path),'symbolic_fixed_point_polynomials':len(symbolic),
                      'finite_field_diagnostic_cases':len(records),'common_ratio':'-1/2'},indent=2),flush=True)
