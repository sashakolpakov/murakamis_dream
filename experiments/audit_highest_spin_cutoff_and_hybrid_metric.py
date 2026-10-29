"""PBW pole cutoff, coherent highest-spin clocks and actual hybrid source.

Proofs use full functions and named source rows. These checks do not
replace the original coherent row by the interval average.
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def generators(N):
    e, f = sp.zeros(N+1), sp.zeros(N+1)
    h = sp.diag(*[N-2*r for r in range(N+1)])
    for r in range(1,N+1):
        e[r-1,r] = N-r+1
        f[r,r-1] = r
    return e,f,h


def comm(a,b):
    return a*b-b*a


def symbol_numerator(matrix,N,u,t):
    return sp.expand(sum(sp.binomial(N,i)*matrix[i,j]*u**i*t**j
                         for i in range(N+1) for j in range(N+1)
                         if matrix[i,j]))


def cutoff_case(N):
    u,t = sp.symbols('u t')
    e,f,h = generators(N)
    max_degree = min(3,N-1)
    powers={}
    for name,g in [('e',e),('f',f),('h',h)]:
        powers[name]=[sp.eye(N+1)]
        for _ in range(max_degree):
            powers[name].append(powers[name][-1]*g)
    count=0
    for a in range(max_degree+1):
        for b in range(max_degree+1-a):
            for c in range(max_degree+1-a-b):
                degree=a+b+c
                C=powers['e'][a]*powers['h'][b]*powers['f'][c]
                P=symbol_numerator(C,N,u,t)
                factor=sp.Poly((1+u*t)**(N-degree),u,t)
                _,remainder=sp.div(sp.Poly(P,u,t),factor)
                assert remainder.is_zero,(N,a,b,c,'pole order')
                ob=sp.expand(sum((-1)**j*sp.binomial(N,i)*C[i,j]*u**(N+i-j)
                                 for i in range(N+1) for j in range(N+1)))
                assert ob==0,(N,a,b,c,'elevation complement')
                count+=1
    return {'N':N,'max_PBW_degree':max_degree,
            'full_symbol_divisibility_checks':count}


def source_clock_case(N):
    u,z,Q = sp.symbols('u z Q')
    weights=[sp.binomial(N,r) for r in range(N+1)]
    gram=sp.diag(*weights)
    e,f,h=generators(N)
    B=sp.diag(*[(-1)**r*weights[r] for r in range(N+1)])
    casimir=comm(e,comm(f,B))+comm(f,comm(e,B))+comm(h,comm(h,B))/2
    assert casimir==2*N*(N+1)*B
    norm2=sum(w*w for w in weights)
    assert norm2==sp.binomial(2*N,N)
    clock_pair=sum((-1)**r*weights[r]*z**r for r in range(N+1))
    assert sp.expand(clock_pair-(1-z)**N)==0
    assert norm2*(2*N+1)>=4**N

    # G is an actual weighted permutation; the hybrid weight depends
    # only on R. Fourier/N is checked in the exact cyclotomic ring.
    dimension=N*(N+1)
    hybrid=sp.MutableSparseMatrix(dimension,dimension,
        {(R*N+S,R*N+S):weights[R] for R in range(N+1) for S in range(N)})
    G=sp.MutableSparseMatrix(dimension,dimension,
        {(R*N+(S+R)%N,R*N+S):1 for R in range(N+1) for S in range(N)})
    assert G.T*hybrid*G==hybrid
    old_psi=sp.MutableSparseMatrix(dimension,1,{(R*N,0):1 for R in range(N+1)})
    old_row=sp.MutableSparseMatrix(1,dimension,
        {(0,R*N):weights[R]/2**N for R in range(N+1)})
    coupled_psi=G*old_psi
    coupled_row=old_row*G.T
    assert hybrid*coupled_psi/2**N==coupled_row.T
    for R in range(N+1):
        for S in range(N):
            expected=int(S==R%N)
            assert coupled_psi[R*N+S]==expected
            assert coupled_row[R*N+S]==weights[R]*expected/2**N
    phi=sp.cyclotomic_poly(N,Q)
    for S in range(N):
        for T in range(N):
            character_sum=sum(Q**((k*(T-S))%N) for k in range(N))
            expected=N if S==T else 0
            assert sp.rem(character_sum-expected,phi,Q)==0

    psi_norm2=sum(weights)
    dual_norm2=sum(w*w/w for w in weights)/4**N
    assert psi_norm2==2**N and dual_norm2==sp.Rational(1,2**N)
    assert psi_norm2*dual_norm2==1

    # Build the original coupled e_D blocks independently and compare
    # their full matrix-valued obstruction with its factorization.
    ob=sp.zeros(N)
    for i in range(N+1):
        for j in range(N+1):
            ob[i%N,j%N]+=(-1)**j*weights[i]*weights[j]*u**(N+i-j)/2**N
    a=sp.zeros(N,1)
    b=sp.zeros(N,1)
    for i in range(N+1):
        a[i%N]+=weights[i]*u**i
        b[i%N]+=(-1)**i*weights[i]*u**(-i)
    expected=u**N*a*b.T/2**N
    assert all(sp.expand(x)==0 for x in ob-expected)
    E00=sp.zeros(N)
    E00[0,0]=1
    assert ob.applyfunc(lambda x:sp.expand(x).coeff(u,2*N))==E00/2**N
    assert ob.applyfunc(lambda x:sp.expand(x).coeff(u,0))==(-1)**N*E00/2**N

    # The actual selected and uniform rows differ on the closed wall.
    W=sp.zeros(N+1)
    W[N,0]=1
    selected=sp.Rational(1,2**N)
    uniform=sp.Rational(1,N+1)
    assert e*W!=W*e
    assert f*W==W*f
    assert sp.Rational(uniform,selected)==sp.Rational(2**N,N+1)
    interval=sp.integrate(((1-u)/2)**N,(u,-1,1))/2
    assert interval==uniform
    uniform_norm2=2**N*sum(1/w for w in weights)/(N+1)**2
    assert uniform_norm2>=sp.Rational(2**(N+1),(N+1)**2)
    return {'N':N,'hybrid_selected_coupon_norm':1,
            'whole_clock_and_Casimir_normalization':True,
            'coupled_source_obstruction_exact':True,
            'selected_wall':str(selected),'uniform_wall':str(uniform),
            'source_ratio_retained':str(uniform/selected)}


def main():
    cutoff=[cutoff_case(N) for N in range(2,10)]
    source=[source_clock_case(N) for N in range(2,10)]
    result={'status':'pass','PBW_cutoff':cutoff,'clock_metric_and_source':source,
            'scope':'Raw PBW interaction cutoff and actual root source/clock norms; no replacement of the selected source or global period bound.'}
    destination=Path(__file__).with_name('highest_spin_cutoff_and_hybrid_metric_results.json')
    destination.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','levels':len(cutoff),
                      'PBW_matrices':sum(c['full_symbol_divisibility_checks'] for c in cutoff),
                      'results':str(destination)},indent=2))


if __name__=='__main__':
    main()
