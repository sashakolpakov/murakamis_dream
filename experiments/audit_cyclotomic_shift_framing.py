#!/usr/bin/env python3
"""Exact crossing/pivot/twist phases for integral root weight shifts."""

import json
from pathlib import Path

import sympy as s


def field(N):
    k=(10000+4*N-1)//(4*N)
    while not s.isprime(4*N*k+1):k+=1
    p=int(4*N*k+1);g=int(s.primitive_root(p))
    omega=pow(g,(p-1)//(4*N),p);q=omega*omega%p
    assert pow(omega,2*N,p)==p-1 and pow(q,N,p)==p-1
    return p,omega,q


def main():
    crossings=0;framings=0;records=[]
    for N in range(2,9):
        p,omega,q=field(N)
        for m in range(0,2*N+2):
            for k in (-2,-1,1,2):
                h=k*N
                s0=pow(omega,h*h,p)*pow(-1,k*m,p)%p
                gh=pow(q,(1-N)*h,p)
                assert gh in (1,p-1)
                theta_ratio=pow(omega,(m+h)**2-m*m,p)*pow(q,(1-N)*h,p)%p
                assert theta_ratio==s0*gh%p
                for a in range(m+1):
                    for b in range(m+1):
                        for sign in (1,-1):
                            maximum=min(a,m-b) if sign>0 else min(b,m-a)
                            for u in range(min(maximum,N-1)+1):
                                if sign>0:
                                    c=b+u
                                    h1=m-2*(a-u);h2=m-2*(b+u)
                                    cartan=pow(omega,(h1+h)*(h2+h)-h1*h2,p)
                                else:
                                    c=b-u
                                    h1=m-2*a;h2=m-2*b
                                    cartan=pow(omega,-(h1+h)*(h2+h)+h1*h2,p)
                                got=cartan*pow(-1,k*u,p)%p
                                expected=pow(s0,sign,p)*pow(-1,k*(c-a),p)%p
                                assert got==expected
                                crossings+=1
                for strands in range(2,7):
                    for winding in range(-3,4):
                        writhe=strands-1+2*winding
                        total=pow(s0,writhe,p)*pow(gh,strands-1,p)*pow(theta_ratio,-writhe,p)%p
                        assert total==1
                        framings+=1
        records.append({'level':N,'full_Cartan_half_phase_retained':True,
                        'all_weight_shifts_and_framings_exact':True})
    result={'levels':records,'crossing_phase_checks':crossings,
            'zero_framing_cancellations':framings,
            'scope':'Uniform one-dimensional-shift phases; no volume theorem.'}
    path=Path(__file__).with_name('cyclotomic_shift_framing_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'crossing_phase_checks':crossings,
                      'zero_framing_cancellations':framings,
                      'output':str(path)},indent=2))


if __name__=='__main__':main()
