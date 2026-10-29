#!/usr/bin/env python3
"""Exact sign, norm, and peripheral-germ checks for the Ward edge.

The general cyclic determinant proof is in the note. These diagnostics
verify its signs, Frobenius product, and the unmodified peripheral ratio.
"""

import json
from pathlib import Path

import sympy as s


M, t, lam, z = s.symbols('M t lam z')


def finite_factorial_ward(n):
    multiplier=2
    while not s.isprime(2*n*multiplier+1):
        multiplier+=1
    prime=int(2*n*multiplier+1)
    generator=int(s.primitive_root(prime))
    q=pow(generator,(prime-1)//(2*n),prime)
    root=q*q%prime
    def multiply(a,b):
        return [[sum(a[i][k]*b[k][j] for k in range(n))%prime
                 for j in range(n)] for i in range(n)]
    identity=[[int(i==j) for j in range(n)] for i in range(n)]
    records=[]
    for m in (1,generator):
        epsilon=[(m*pow(root,-a-1,prime)-pow(m,-1,prime))%prime
                 for a in range(n)]
        kappa=(m-pow(m,-1,prime))%prime
        kappan=(pow(m,n,prime)-pow(m,-n,prime))%prime
        if m!=1:
            assert kappan!=0
        matrix=[[0 for _ in range(n)] for _ in range(n)]
        for a in range(n-1):matrix[a][a+1]=epsilon[a]
        matrix[n-1][0]=epsilon[n-1]
        assert epsilon[n-1]==kappa
        coefficient=1
        power=[row[:] for row in identity]
        gauge=[[0 for _ in range(n)] for _ in range(n)]
        for j in range(n):
            if j:
                coefficient=-2*coefficient*pow((1-pow(root,j,prime))%prime,-1,prime)%prime
                power=multiply(power,matrix)
            for a in range(n):
                for b in range(n):gauge[a][b]=(gauge[a][b]+coefficient*power[a][b])%prime
        xvalue=-m*pow(q,-1,prime)%prime
        kvals=[xvalue*pow(root,-a,prime)%prime for a in range(n)]
        conjugate=[[kvals[a]*gauge[a][b]*pow(kvals[b],-1,prime)%prime
                    for b in range(n)] for a in range(n)]
        unit=[[ (identity[a][b]+2*matrix[a][b])%prime for b in range(n)]
              for a in range(n)]
        rhs=multiply(unit,gauge)
        defect=-kappan*pow(2,n,prime)*pow(n,-1,prime)%prime
        for a in range(n):
            for b in range(n):
                assert (conjugate[a][b]-rhs[a][b])%prime==defect*int(a==b)%prime
        if m==1:
            assert defect==0
            assert s.det(s.Matrix(gauge))%prime==1
        records.append({'level':n,'complete_fiber':m==1,
                        'literal_affine_factorial_matrix_equation':True})
    return records


def main():
    records=[]
    for n in range(2,11):
        edges=s.symbols(f'a0:{n}')
        matrix=s.zeros(n)
        for a in range(n-1):
            matrix[a,a+1]=edges[a]
        matrix[n-1,0]=edges[n-1]
        product=s.prod(edges)
        assert s.expand(matrix.charpoly(lam).as_expr()-lam**n+product)==0
        assert s.expand((s.eye(n)+t*matrix).det()-(1-(-t)**n*product))==0
        # The resultant independently computes the product over all
        # primitive-orbit eigenvalues Q^(-a-1), including the last edge.
        norm=s.resultant(z**n-1,M*z-M**(-1),z)
        kappa=M-M**(-1)
        kappan=M**n-M**(-n)
        assert s.cancel(norm-(-1)**(n+1)*kappan)==0
        adapter=M**(1-n)*sum(M**(2*j) for j in range(n))
        assert s.cancel(adapter-kappan/kappa)==0
        assert s.limit(adapter,M,1)==n
        assert s.limit(kappan/kappa,M,1)==n
        assert s.limit(s.diff(kappan,M),M,1)==2*n
        assert s.cancel(1-(-t)**n*norm-(1+kappan*t**n))==0
        records.append({'level':n,'cycle_characteristic_sign':True,
                        'all_orbit_edge_norm':True,'determinant_character':True,
                        'complete_adapter':n,'peripheral_germ_retained':True})
    factorial=[case for n in range(2,11) for case in finite_factorial_ward(n)]
    output=Path(__file__).with_name('cyclic_ward_norm_adapter_results.json')
    output.write_text(json.dumps({'exact_levels':records,
                                 'literal_factorial_ward_cases':factorial,
                                 'scope':'Norm-character and source-edge identities; '
                                         'no bulk group comparison or volume theorem.'},indent=2)+'\n')
    print(json.dumps({'exact_levels':len(records),
                      'literal_factorial_ward_cases':len(factorial),
                      'output':str(output)},indent=2))


if __name__=='__main__':
    main()
