"""Narrow original-block audit of whole-interval contour and paired currents.
No numerical large-N tail or shared mixed-source theorem is asserted.
"""
import argparse, json, sys
from pathlib import Path
import mpmath as mp
import sympy as sp
sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_actual_q_hahn_physical_generic_jet_bound import matrix


def run():
    mp.mp.dps=55
    z=sp.symbols('z')
    counts={'original_block_entries':0,'paired_endpoint_entries':0,'whole_contour_entries':0,'negative_charge_entries':0}
    error=mp.mpf(0)
    for N in (3,4):
        q=mp.exp(mp.pi*1j/N)
        t=N-1
        di,up,lo=matrix(N,q,t)
        J=mp.diag(di)
        for j in range(t): J[j,j+1]=up[j]; J[j+1,j]=lo[j]
        coeff=[int(sp.Poly(2*sp.chebyshevt(N,z/2)+2,z).nth(k)) for k in range(N+1)]
        powers=[mp.eye(t+1)]
        for j in range(1,N): powers.append(powers[-1]*J)
        mat_coeff=[mp.zeros(t+1) for j in range(N)]
        for degree in range(1,N+1):
            for j in range(degree): mat_coeff[degree-1-j] += coeff[degree]*powers[j]
        positions=[(0,0),(t,t),(0,min(2,t)),(t,0)]
        for n in (-3,3):
            ell=4; tau=mp.mpf('.09')
            for row,col in positions:
                def V(zz): return mp.polyval([M[row,col] for M in reversed(mat_coeff)],zz)
                def B(dd): return mp.sin(2*mp.pi*dd)*mp.exp(mp.pi*1j*n*N*dd*dd)*V(-2*mp.cos(2*mp.pi*dd))
                def integrand(dd,charge=ell): return B(dd)*mp.exp(2*mp.pi*1j*charge*N*dd)
                for v in (mp.mpf('0'),mp.mpf('.017'),tau):
                    actual=B(mp.mpf('.5')+1j*v)-B(-mp.mpf('.5')+1j*v)
                    expected=2j*mp.sinh(2*mp.pi*v)*mp.sinh(mp.pi*n*N*v)*mp.exp(mp.pi*1j*n*N*(mp.mpf('.25')-v*v))*V(2*mp.cosh(2*mp.pi*v))
                    err=abs(actual-expected)/max(1,abs(actual),abs(expected))
                    error=max(error,err);assert err<mp.mpf('1e-45')
                    counts['paired_endpoint_entries']+=1
                grid=[mp.mpf(j)/8 for j in range(-4,5)]
                bottom=mp.quad(integrand,grid)
                horizontal=mp.quad(lambda x:integrand(x+1j*tau),grid)
                vertical=2*(-1)**(N*ell)*mp.quad(lambda v:mp.exp(-2*mp.pi*ell*N*v)*mp.sinh(2*mp.pi*v)*mp.sinh(mp.pi*n*N*v)*mp.exp(mp.pi*1j*n*N*(mp.mpf('.25')-v*v))*V(2*mp.cosh(2*mp.pi*v)),[0,tau])
                err=abs(bottom-horizontal-vertical)/max(1,abs(bottom),abs(horizontal),abs(vertical))
                error=max(error,err);assert err<mp.mpf('1e-43'),(N,n,row,col,err)
                counts['whole_contour_entries']+=1
                neg=mp.quad(lambda x:integrand(x,-ell),grid)
                err=abs(bottom+neg)/max(1,abs(bottom),abs(neg));error=max(error,err)
                assert err<mp.mpf('1e-43')
                counts['negative_charge_entries']+=1
                counts['original_block_entries']+=1
    return {'status':'PASS','precision_digits':mp.mp.dps,'counts':counts,'maximum_relative_error':str(error),'scope':'Original physical-block polynomial numerator: exact paired endpoint expression, retained whole-contour side currents and charge-sign symmetry. No asymptotic, operator-norm rate, or mixed-source numerical claim.'}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=Path(__file__).with_name('actual_whole_domain_large_charge_tail_results.json'))
    args=ap.parse_args();result=run();args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
