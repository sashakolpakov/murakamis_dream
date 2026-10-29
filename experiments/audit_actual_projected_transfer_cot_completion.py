#!/usr/bin/env python3
"""Original finite output Fourier projection at colliding transfer poles.

No new basis is used. The sinc vector is the literal unit-circle Fourier
projection onto the original orthonormal head basis. Proof is in the note;
small offsets supplement its exact pole-order and residue calculation.
"""
import itertools,json
from pathlib import Path
import numpy as np
import mpmath as mp
from audit_exact_factorial_interpolation import factorial


class Projected:
    def __init__(self,N):
        self.N=N;self.d=N-1;self.q=mp.exp(mp.pi*1j/N);self.Q=self.q**2;self.x=-1/self.q
        self.kappa=mp.exp(mp.pi*1j*(N-1)**2/(2*N))
        self.F=[mp.mpc(1)];self.qfac=[mp.mpc(1)];self.rho=self.q-1/self.q
        for j in range(1,N):
            self.F.append(self.F[-1]*(1-self.Q**j))
            self.qfac.append(self.qfac[-1]*(self.q**j-self.q**(-j))/self.rho)
        self.flip=np.zeros((N*N,N*N),complex)
        for a,b in itertools.product(range(N),repeat=2):self.flip[b*N+a,a*N+b]=1

    def vector(self,nu):
        numerator=mp.expm1(2j*mp.pi*nu)
        return np.array([complex(numerator/(2j*mp.pi*(nu-j)))
                         if abs(nu-j)>mp.mpf('1e-70') else 1.
                         for j in range(self.N)],complex)

    def matrix(self,z):
        N,Q,x=self.N,self.Q,self.x
        # Exact integer shift eliminates all but ONE Barnes factorial.
        fm=factorial(N,-z);plus=[mp.mpc(1)];minus=[mp.mpc(1)]
        for j in range(1,N):
            plus.append(plus[-1]*(1-mp.exp(2j*mp.pi*(z+j)/N)))
            minus.append(minus[-1]*(1-mp.exp(2j*mp.pi*(j-z)/N)))
        va=[self.vector(a-z) for a in range(N)]
        vb=[self.vector(b+z) for b in range(N)]
        R=np.zeros((N*N,N*N),complex)
        for a,b in itertools.product(range(N),repeat=2):
            phase=mp.exp((-a-b+z)*mp.log(x)+2j*mp.pi*b*(a-z)/N)
            r=self.kappa*phase*plus[b]*self.F[a]/(self.F[b]*fm*minus[a])
            R[:,a*N+b]=complex(r)*np.kron(vb[b],va[a])
        return R

    def original(self,sign=1):
        N,d,q,Q,x=self.N,self.d,self.q,self.Q,self.x
        R=np.zeros((N*N,N*N),complex)
        def e(a):
            return ((q**a-q**(-a))/self.rho
                    *(x*q**(1-a)-x**(-1)*q**(a-1))/self.rho)
        for a,b in itertools.product(range(N),repeat=2):
            maximum=min(a,d-b) if sign>0 else min(b,d-a)
            for k in range(maximum+1):
                ec=mp.fprod(e((a if sign>0 else b)-j) for j in range(k))
                universal=self.rho**k/self.qfac[k]
                if sign>0:
                    universal*=q**(k*(k-1)/2);u,v=b+k,a-k
                    cartan=x**(-a-b)*Q**((a-k)*(b+k))
                else:
                    universal*=(-1)**k*q**(-k*(k-1)/2);u,v=b-k,a+k
                    cartan=x**(a+b)*Q**(-a*b)
                value=self.kappa**sign*universal*ec*cartan*self.F[u]*self.F[v]/(self.F[a]*self.F[b])
                R[u*N+v,a*N+b]=complex(value)
        return R


def all_input_cancellations():
    rows=[];eps=mp.mpf('1e-12')
    for N in range(2,9):
        A=Projected(N);worst=0.;classes=[0,0,0]
        upper_worst=0.;upper_classes=[0,0,0]
        new_residues=np.zeros((N*N,N*N),complex)
        for s in range(1,min(3,N-1)+1):
            left=A.matrix(-s-eps);right=A.matrix(-s+eps)
            # Complete cot density; all original physical columns retained.
            dl=complex(mp.pi*mp.cot(mp.pi*(-s-eps)))*left
            dr=complex(mp.pi*mp.cot(mp.pi*(-s+eps)))*right
            for a,b in itertools.product(range(N),repeat=2):
                i=a*N+b;I=int(b<s)+int(a+s>=N);classes[I]+=1
                error=np.linalg.norm(dl[:,i]-dr[:,i])/max(1.,np.linalg.norm(dl[:,i]),np.linalg.norm(dr[:,i]))
                worst=max(worst,error)
                assert error<1e-6,(N,s,a,b,error)
            # Each projected column has a zero, including the scalar poles.
            assert np.linalg.norm(left)<1e-6*max(1.,np.linalg.norm(dl))
            assert np.linalg.norm(right)<1e-6*max(1.,np.linalg.norm(dr))
            new_residues+=(left+right)/2
        for k in range(N,N+min(3,N-2)+1):
            left=A.matrix(k-eps);right=A.matrix(k+eps);half=A.matrix(k+eps/2)
            for a,b in itertools.product(range(N),repeat=2):
                col=a*N+b;extra=int(b+k>=2*N)+int(k-a>=N+1)
                upper_classes[extra]+=1;order=3+extra
                e=float(eps)
                cl=left[:,col]/(-e)**order;cr=right[:,col]/e**order
                ch=half[:,col]/(e/2)**order
                error=max(np.linalg.norm(cl-cr),np.linalg.norm(ch-cr))/max(1.,np.linalg.norm(cl),np.linalg.norm(cr),np.linalg.norm(ch))
                upper_worst=max(upper_worst,error)
                assert error<1e-6,(N,k,a,b,order,error)
                ratio=np.linalg.norm(right[:,col])/np.linalg.norm(half[:,col])
                assert abs(ratio/2**order-1)<1e-6,(N,k,a,b,order,ratio)
            # The complete cot density has zero order at least two here.
            dl=complex(mp.pi*mp.cot(mp.pi*(k-eps)))*left
            dr=complex(mp.pi*mp.cot(mp.pi*(k+eps)))*right
            assert max(np.linalg.norm(dl),np.linalg.norm(dr))<1e-12
            new_residues+=(left+right)/2
        # Expanded cot integral equals its old positive integer residues:
        # all newly enclosed negative residues have just been canceled.
        residue_sum=np.zeros((N*N,N*N),complex)
        for k in range(N):residue_sum+=(A.matrix(k-eps)+A.matrix(k+eps))/2
        original=A.original(1)
        rel=np.linalg.norm(residue_sum-original)/max(1.,np.linalg.norm(original))
        assert rel<1e-7,(N,rel)
        expanded=residue_sum+new_residues
        expanded_rel=np.linalg.norm(expanded-original)/max(1.,np.linalg.norm(original))
        assert expanded_rel<1e-7,(N,expanded_rel)
        negative=A.original(-1)
        mirrored=A.flip@original.conj()@A.flip
        assert np.linalg.norm(negative-mirrored)/max(1.,np.linalg.norm(negative))<1e-12
        neg_residues=A.flip@residue_sum.conj()@A.flip
        assert np.linalg.norm(neg_residues-negative)/max(1.,np.linalg.norm(negative))<1e-7
        neg_expanded=A.flip@expanded.conj()@A.flip
        assert np.linalg.norm(neg_expanded-negative)/max(1.,np.linalg.norm(negative))<1e-7
        rows.append({'N':N,'all_original_input_columns_checked':N*N,
                     'negative_collision_columns_by_number_invalid_outputs':classes,
                     'upper_columns_by_extra_scalar_zero_order':upper_classes,
                     'max_relative_canceled_density_jump':worst,
                     'max_relative_upper_zero_order_test':upper_worst,
                     'expanded_cot_residue_sum_vs_literal_original_R_relative_error':rel,
                     'both_collars_expanded_residue_sum_vs_literal_original_R_relative_error':expanded_rel,
                     'both_original_signs_and_complete_scalar_convention_retained':True})
    return rows


def upper_fractional_bases():
    rows=[]
    for N in range(2,9):
        A=Projected(N);h=2j*mp.pi/N;worst=mp.mpf(0);checks=0
        for w in (mp.mpc('.5','.3'),mp.mpc('.17','.7'),mp.mpc('.83','-.6')):
            # Direct Barnes evaluations audit the N-shift independently
            # of the finite-product implementation of the matrix columns.
            shift=factorial(N,w+N)/(factorial(N,w)*(1-mp.exp(2j*mp.pi*w)))
            assert abs(shift-1)<mp.mpf('1e-60')
            z=N-1+w
            fz=factorial(N,z);fmz=factorial(N,-z)
            fwm=factorial(N,w-1);f1mw=factorial(N,1-w)
            lhs_num=[fz];lhs_den=[fmz];rhs_num=[fwm];rhs_den=[f1mw]
            for j in range(1,N):
                lhs_num.append(lhs_num[-1]*(1-mp.exp(h*(z+j))))
                lhs_den.append(lhs_den[-1]*(1-mp.exp(h*(-z+j))))
                rhs_num.append(rhs_num[-1]*(1-mp.exp(h*(w-1+j))))
                rhs_den.append(rhs_den[-1]*(1-mp.exp(h*(1-w+j))))
            norm=1-mp.exp(-2j*mp.pi*w)
            for a,b in itertools.product(range(N),repeat=2):
                lhs=lhs_num[b]*A.F[a]/(fz*A.F[b]*lhs_den[a])
                rhs=rhs_num[b]/A.F[b]*A.F[a]/rhs_den[a]*norm/fwm
                error=abs(lhs/rhs-1);worst=max(worst,error)
                assert error<mp.mpf('1e-60'),(N,a,b,w,error)
                checks+=1
        rows.append({'N':N,'all_input_fractional_upper_formula_checks':checks,
                     'max_relative_error':float(worst),'central_N_shift_factor_retained':True})
    return rows


def projection_norms():
    rows=[]
    for N in (3,5,8,13,21):
        A=Projected(N)
        for nu in (mp.mpc('-.7','.5'),mp.mpc(N+mp.mpf('.2'),'-.8'),mp.mpc('.37','.23')):
            norm=np.linalg.norm(A.vector(nu));bound=float(mp.exp(2*mp.pi*abs(mp.im(nu))))
            assert norm<=bound*(1+1e-12)
        rows.append({'N':N,'literal_orthogonal_Fourier_projection_norm_verified':True})
    return rows


def main():
    mp.mp.dps=85
    data={'status':'PASS','all_input_source_pole_cancellations':all_input_cancellations(),
          'upper_fractional_bases_and_exact_N_shift':upper_fractional_bases(),
          'bounded_physical_projection':projection_norms(),
          'scope':'Actual finite physical output projection and BOTH normal collars. No sharp bulk-exterior bound, dropped sinc terms, or global stationary-support claim.'}
    Path(__file__).with_name('actual_projected_transfer_cot_completion_results.json').write_text(json.dumps(data,indent=2)+'\n')
    print('PASS all physical inputs N2..8: both cot collars, upper N-shift, original signed R residue sums, and bounded Fourier projection')


if __name__=='__main__':main()
