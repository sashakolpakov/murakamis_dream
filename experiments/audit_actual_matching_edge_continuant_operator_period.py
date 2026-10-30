#!/usr/bin/env python3
"""Original generic Green kernels, contour residues, normals and bandwidth."""
import json
import math
from pathlib import Path

from audit_actual_q_hahn_physical_generic_jet_bound import Jet, matrix
from audit_high_color_first_normal_r_degree import root_field


def padd(a,b):
    out=[Jet(0) for _ in range(max(len(a),len(b)))]
    for i,x in enumerate(a):out[i]+=x
    for i,x in enumerate(b):out[i]+=x
    return out


def pscale(a,c):return [x*c for x in a]


def pmul(a,b):
    out=[Jet(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def peval(a,z):
    value=Jet(0)
    for x in reversed(a):value=value*z+x
    return value


def remainder(a,monic):
    out=[Jet(x) for x in a]
    while len(out)>=len(monic):
        factor=out[-1];offset=len(out)-len(monic)
        for k,c in enumerate(monic):out[offset+k]-=factor*c
        assert out[-1]==0;out.pop()
    return out+[Jet(0)]*(len(monic)-1-len(out))


def ident(n):return [[Jet(int(i==j)) for j in range(n)] for i in range(n)]
def zero(n):return [[Jet(0) for _ in range(n)] for _ in range(n)]
def madd(A,B):return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]
def mscale(A,c):return [[v*c for v in row] for row in A]
def mm(A,B):return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Jet(0)) for j in range(len(B[0]))] for i in range(len(A))]


def root_mm(A,B,p):return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%p for j in range(len(B[0]))] for i in range(len(A))]
def root_add(A,B,p):return [[(a+b)%p for a,b in zip(x,y)] for x,y in zip(A,B)]


def divide_root_linear(coeff,x,p):
    out=[0]*(len(coeff)-1);carry=coeff[-1];out[-1]=carry
    for k in range(len(coeff)-2,0,-1):carry=(coeff[k]+x*carry)%p;out[k-1]=carry
    assert (coeff[0]+x*carry)%p==0
    return out


def ev(coeff,x,p):return sum(c*pow(x,k,p) for k,c in enumerate(coeff))%p
def dev(coeff,x,p):return sum(k*c*pow(x,k-1,p) for k,c in enumerate(coeff) if k)%p


def audit():
    counts=dict(original_characteristic_coefficients=0,green_matrix_three_jets=0,
                moving_resolvent_first_normals=0,contour_polynomial_entries=0,
                genuine_operator_jet_coefficients=0,exact_bandwidth_zeros=0,
                genuine_double_poles=0,fourth_order_pole_cancellations=0,
                third_order_pole_coefficients=0)
    Jet.order=3
    for N in range(3,9):
        p,eta=root_field(N);root=eta*eta%p;Jet.p=p;d=N-1
        q=Jet([root*pow(math.factorial(k),-1,p)%p for k in range(3)])
        delta=q-q**-1
        qi=[(q**r-q**(-r))/delta for r in range(2*N)]
        fac=[Jet(1)];omit=[Jet(1)]
        for r in range(1,2*N):
            fac.append(fac[-1]*qi[r]);omit.append(omit[-1] if r==N else omit[-1]*qi[r])
        polynomials=[];faces=[]
        for a in range(d//2+1):
            term=[Jet(1)];poly=[Jet(1)]
            for k in range(a):
                scalar=-qi[a-k]*qi[a+k+1]/(qi[k+1]**2*qi[d-k]*qi[d+k+2]*delta**2)
                lam=q**(2*k+1)+q**(-2*k-1)
                term=pscale(pmul(term,[-lam,Jet(1)]),scalar);poly=padd(poly,term)
            polynomials.append(poly)
            faces.append((-1)**a*fac[a]**2*fac[d-a]/omit[d+a+1])
        for t in range(N):
            diag,upper,lower=matrix(N,q,t);n=t+1
            J=zero(n)
            for r in range(n):
                J[r][r]=diag[r]
                if r<t:J[r][r+1]=upper[r];J[r+1][r]=lower[r]
            prefix=[[Jet(1)]]
            for r in range(n):
                value=pmul([-diag[r],Jet(1)],prefix[-1])
                if r:value=padd(value,pscale(prefix[-2],-upper[r-1]*lower[r-1]))
                prefix.append(value)
            suffix=[None]*(n+1);suffix[n]=[Jet(1)]
            for r in range(t,-1,-1):
                value=pmul([-diag[r],Jet(1)],suffix[r+1])
                if r<t:value=padd(value,pscale(suffix[r+2],-upper[r]*lower[r]))
                suffix[r]=value
            chi=prefix[-1];spectral=[Jet(1)];lams=[]
            for m in range(n):
                lam=q**(2*N-2*m-1)+q**(-2*N+2*m+1);lams.append(lam)
                spectral=pmul(spectral,[-lam,Jet(1)])
            assert chi==spectral==suffix[0]
            counts['original_characteristic_coefficients']+=len(chi)
            nums=[[None]*n for _ in range(n)]
            for u in range(n):
                for v in range(n):
                    lo,hi=min(u,v),max(u,v);prod=Jet(1)
                    entries=upper if u<=v else lower
                    for r in range(lo,hi):prod*=entries[r]
                    nums[u][v]=pscale(pmul(prefix[lo],suffix[hi+1]),prod)
            z=next(z for z in range(2,p) if all(z!=lam.c[0] for lam in lams))
            den=peval(chi,Jet(z));R=[[peval(nums[u][v],Jet(z))/den for v in range(n)] for u in range(n)]
            zminus=madd(mscale(ident(n),z),mscale(J,-1))
            assert mm(zminus,R)==ident(n)==mm(R,zminus)
            counts['green_matrix_three_jets']+=n*n
            R0=[[v.c[0] for v in row] for row in R];J1=[[v.c[1] for v in row] for row in J]
            first=root_mm(root_mm(R0,J1,p),R0,p)
            assert first==[[v.c[1] for v in row] for row in R]
            counts['moving_resolvent_first_normals']+=n*n
            for a,poly in enumerate(polynomials):
                direct=zero(n)
                for c in reversed(poly):direct=madd(mm(direct,J),mscale(ident(n),c))
                direct=mscale(direct,1/faces[a])
                for u in range(n):
                    for v in range(n):
                        # Residue at infinity of p(z)*Green(z): top remainder/monic chi.
                        res=remainder(pmul(poly,nums[u][v]),chi)[-1]/faces[a]
                        assert res==direct[u][v]
                        counts['contour_polynomial_entries']+=1
                        counts['genuine_operator_jet_coefficients']+=3
                        if abs(u-v)>a:
                            assert res==0;counts['exact_bandwidth_zeros']+=1
            chi0=[v.c[0] for v in chi]
            for j in range((N-1)//2+1):
                ell=d-j
                if not j<ell<=t:continue
                lam=lams[j].c[0];assert lam==lams[ell].c[0]
                h=divide_root_linear(divide_root_linear(chi0,lam,p),lam,p)
                hh=ev(h,lam,p);hp=dev(h,lam,p);assert hh
                M=[[0]*n for _ in range(n)];C=[[0]*n for _ in range(n)]
                for u in range(n):
                    for v in range(n):
                        nu=[x.c[0] for x in nums[u][v]]
                        val=ev(nu,lam,p);der=dev(nu,lam,p)
                        M[u][v]=val*pow(hh,-1,p)%p
                        C[u][v]=(der*pow(hh,-1,p)-val*hp*pow(hh,-2,p))%p
                zeros=[[0]*n for _ in range(n)]
                assert root_mm(M,M,p)==zeros and any(v for row in M for v in row)
                assert root_mm(C,C,p)==C and root_mm(C,M,p)==M==root_mm(M,C,p)
                assert root_mm(root_mm(M,J1,p),M,p)==zeros
                lhs=root_add(root_mm(root_mm(C,J1,p),M,p),root_mm(root_mm(M,J1,p),C,p),p)
                speed=(lams[j].c[1]+lams[ell].c[1])%p
                assert lhs==[[speed*v%p for v in row] for row in M]
                counts['genuine_double_poles']+=1
                counts['fourth_order_pole_cancellations']+=n*n
                counts['third_order_pole_coefficients']+=n*n
    return counts


def main():
    result=dict(status='PASS',exact=audit(),
                scope='Original generic continuant Green entries, contour polynomial residues, genuine q jets and paired pole cancellation. No contour deformation, geometric contribution or scalar-to-operator asymptotic.')
    Path(__file__).with_name('actual_matching_edge_continuant_operator_period_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
