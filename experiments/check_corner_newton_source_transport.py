#!/usr/bin/env python3
"""Check the original two-vertex tensor transport and crossing normalization.

These finite checks use the original crossing and Newton multiplication
matrices. Transpose is the bilinear transpose, never the Hermitian adjoint.
"""
import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp
from check_twist_period_insertion import original_matrices, encode


def basis_matrices(N):
    D=N-1
    z=mp.matrix(N)
    for j in range(N):
        z[j,j]=2*mp.cos((2*j+1)*mp.pi/N)
        if j<D:z[j+1,j]=-4*mp.sin((j+1)*mp.pi/N)**2
    I=mp.eye(N)
    out=[I]
    for j in range(D):
        out.append((2*mp.cos((2*j+1)*mp.pi/N)*I-z)*out[-1]
                   /(4*mp.sin((j+1)*mp.pi/N)**2))
    return out


def factorials(N):
    S=[mp.mpf(1)]
    for k in range(1,N):S.append(S[-1]*2*mp.sin(mp.pi*k/N))
    return S


def direct_crossing_entry(N,sign,k,r,S):
    q=mp.exp(1j*mp.pi/N)
    kappa=q**(mp.mpf((N-1)**2)/2)
    return kappa**sign*(-1)**k*q**(sign*k*(r+1))*S[k]/(S[r]*S[k-r])


def J(x):
    # Real regular-strip logarithmic sine integral.
    return -mp.im(mp.polylog(2,mp.exp(2j*mp.pi*x)))/(2*mp.pi)


def phase(sign,x,y):
    return J(x)-J(y)-J(x-y)+sign*1j*mp.pi*(mp.mpf('0.5')+x+x*y)


def amplitude(sign,x,y):
    return -mp.exp(sign*1j*mp.pi*x)*mp.sqrt(
        2*mp.sin(mp.pi*x)/(2*mp.sin(mp.pi*y)*2*mp.sin(mp.pi*(x-y))))


def evaluation_defect(N,M,power,c):
    """Polynomial divided differences; no inverse at a spectral root."""
    D=N-1
    Z=mp.matrix(N)
    for k in range(N):
        Z[k,k]=2*mp.cos((2*k+1)*mp.pi/N)
        if k<D:Z[k+1,k]=-4*mp.sin((k+1)*mp.pi/N)**2
    L=Z.T
    I=mp.eye(N)
    endpoint=mp.matrix(N,1)
    endpoint[D]=1
    values=[mp.mpf(1)]
    derivatives=[mp.mpf(0)]
    divided=[mp.matrix(N,1)]
    divided_derivatives=[mp.matrix(N,1)]
    for k in range(D):
        node=2*mp.cos((2*k+1)*mp.pi/N)
        scale=4*mp.sin((k+1)*mp.pi/N)**2
        divided.append(((node*I-L)*divided[-1]-values[-1]*endpoint)/scale)
        divided_derivatives.append(
            ((node*I-L)*divided_derivatives[-1]-derivatives[-1]*endpoint)/scale)
        derivatives.append(((node-c)*derivatives[-1]-values[-1])/scale)
        values.append((node-c)*values[-1]/scale)
    Mn=M**power
    alpha=[Mn[k,0] for k in range(N)]
    r=mp.fsum(a*v for a,v in zip(alpha,values))
    rp=mp.fsum(a*v for a,v in zip(alpha,derivatives))
    d=mp.matrix(N,1)
    dp=mp.matrix(N,1)
    for a,v,vp in zip(alpha,divided,divided_derivatives):
        d+=a*v
        dp+=a*vp
    v=mp.matrix(values)
    vp=mp.matrix(derivatives)
    P=2*mp.chebyt(N,c/2)+2
    Pp=N*mp.chebyu(N-1,c/2)
    eta=(-1)**D
    lhs=Mn.T*v
    rhs=r*v-eta*P*d/N**2
    lhs_derivative=Mn.T*vp
    rhs_derivative=rp*v+r*vp-eta*(Pp*d+P*dp)/N**2
    return (mp.norm(lhs-rhs)/max(1,mp.norm(lhs),mp.norm(rhs)),
            mp.norm(lhs_derivative-rhs_derivative)/
            max(1,mp.norm(lhs_derivative),mp.norm(rhs_derivative)))


def run(precision):
    mp.mp.dps=precision
    rows=[]
    for N in (3,4,5,8):
        M,_,_=original_matrices(N)
        E=basis_matrices(N)
        reversal=mp.matrix(N)
        for j in range(N):reversal[j,N-1-j]=1
        S=factorials(N)
        coefficient_error=mp.mpf(0)
        for sign in (-1,1):
            C=reversal*(M**sign)*reversal
            for r in range(N):
                for k in range(N):
                    exact=direct_crossing_entry(N,sign,k,r,S) if r<=k else 0
                    coefficient_error=max(coefficient_error,abs(C[r,k]-exact))
        if coefficient_error>mp.mpf('1e-40'):
            raise ArithmeticError('Signed original crossing entry failed')
        for m,n in ((0,0),(1,-1),(2,-3),(-2,2)):
            Cm=reversal*(M**m)*reversal
            Cn=reversal*(M**n)*reversal
            transpose_error=max(mp.norm(Cm-(M**m).T),mp.norm(Cn-(M**n).T))
            tensor_error=mp.mpf(0)
            # Each b,d block contains every coefficient on the other two legs.
            for b in range(N):
                for d in range(N):
                    direct=(reversal*M**m*E[b])*(reversal*M**n*E[d]).T
                    zero=(reversal*E[b])*(reversal*E[d]).T
                    transported=Cm*zero*Cn.T
                    error=mp.norm(direct-transported)/max(1,mp.norm(direct))
                    tensor_error=max(tensor_error,error)
            if max(transpose_error,tensor_error)>mp.mpf('1e-40'):
                raise ArithmeticError('Full four-leg tensor transport failed')
            rows.append({'N':N,'left_power':m,'right_power':n,
                         'unit_crossing_absolute_error':mp.nstr(coefficient_error,30),
                         'bilinear_transpose_error':mp.nstr(transpose_error,30),
                         'full_tensor_relative_error':mp.nstr(tensor_error,30)})
        print(f'Checked every four-leg tensor coefficient at N={N}.',flush=True)
    defects=[]
    for N in range(2,9):
        M,_,_=original_matrices(N)
        for power in (-3,0,1,2):
            for c in (mp.mpc('.37','.12'),mp.mpf(-2)):
                error,derivative_error=evaluation_defect(N,M,power,c)
                if max(error,derivative_error)>mp.mpf('1e-40'):
                    raise ArithmeticError('Arbitrary-power evaluation defect failed')
                defects.append({'N':N,'power':power,'boundary_value':encode(c),
                                'value_relative_error':mp.nstr(error,30),
                                'boundary_derivative_relative_error':mp.nstr(derivative_error,30)})
    print('Checked all 56 evaluation defects and their boundary derivatives.',flush=True)
    expansions=[]
    x=mp.mpf('0.5')
    y=mp.mpf('0.25')
    for N in (24,48,96):
        S=factorials(N)
        for sign in (-1,1):
            for delta in (0,-1):
                k=N//2+delta
                r=N//4
                Fx=mp.log(2*mp.sin(mp.pi*x))-mp.log(2*mp.sin(mp.pi*(x-y)))+sign*1j*mp.pi*(1+y)
                leading=N**mp.mpf('-0.5')*amplitude(sign,x,y)*mp.exp(N*phase(sign,x,y)+delta*Fx)
                exact=direct_crossing_entry(N,sign,k,r,S)
                expansions.append({'N':N,'sign':sign,'input_offset':delta,
                                   'finite_over_leading':encode(exact/leading)})
    return {'scope':'All-normal original-matrix tensor checks and finite asymptotic diagnostics; no general nonzero-power packet asserted.',
            'decimal_precision':precision,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'tensor_checks':rows,'evaluation_defect_checks':defects,
            'crossing_density_checks':expansions}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--precision',type=int,default=100)
    p.add_argument('--output',type=Path)
    a=p.parse_args()
    data=run(a.precision)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(json.dumps(data,indent=2)+'\n')
        print(f'Saved {a.output}.')
    else:print(json.dumps(data,indent=2))


if __name__=='__main__':main()
