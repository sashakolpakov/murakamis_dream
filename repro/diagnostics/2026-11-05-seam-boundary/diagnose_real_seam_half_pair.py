"""Original real seam/half-angle raw pair: bounded 1D profiles, not a certificate."""
from pathlib import Path
import importlib.util,json
import numpy as np
from scipy.optimize import minimize_scalar
s=importlib.util.spec_from_file_location('a3','/tmp/diagnose_a3_incoming_residuals.py');a3=importlib.util.module_from_spec(s);s.loader.exec_module(a3)
g=a3.g;J=lambda x:g(np.asarray(x,dtype=complex)).real
def profile(u,e):return J(np.asarray(u)+.5)-(1+e)*J(u)
def main():
 rows=[]
 for e in [0,1]:
  grid=np.linspace(0,1,10001);values=profile(grid,e);k=int(np.argmax(values))
  opt=minimize_scalar(lambda u:-float(profile(u,e)),bounds=(grid[max(0,k-2)],grid[min(len(grid)-1,k+2)]),method='bounded',options={'xatol':1e-14})
  algebraic=.25 if e==0 else np.arcsin(np.sqrt((np.sqrt(17)-1)/8))/np.pi
  rows.append(dict(epsilon=e,grid_size=len(grid),grid_maximum=float(values[k]),optimized_u=float(opt.x),optimized_value=float(-opt.fun),explicit_algebraic_u=float(algebraic),explicit_algebraic_value=float(profile(algebraic,e)),high_half_maximum=float(np.max(values[5000:])),reflection_grid_error=float(np.max(np.abs(values+values[::-1])))))
 ref,M,res=a3.reference((0,1));f10,gr10=a3.phase(ref[1],ref[0],1,0);f01,gr01=a3.phase(ref[0],ref[1],0,1)
 gamma=f10+gr10[0]*(.5-ref[1])+gr10[1]*(0-ref[0])+f01+gr01[0]*(0-ref[0])+gr01[1]*(.5-ref[1])
 total=sum(r['explicit_algebraic_value']for r in rows)
 common=json.load(open('/tmp/seam-common-incoming-diagnostic.json'))['cases'][0]
 difference=common['comparisons'][-1]['difference'];endpoint=common['endpoint_occupation_debit']
 rho=.001;Delta=rho*np.log(2)-float(J(rho))
 const_source=.447948+.515591
 universal_gap=.28+common['Q']
 comparisons=dict(universal_gap=dict(pair_gap=universal_gap,net_estimate=difference-endpoint-universal_gap,collar_already_included=True),actual_plane_constant_source=dict(source_ceiling=const_source,pair_gap=float(gamma.real)-const_source-2*Delta,net_estimate=const_source+2*Delta-float(gamma.real)+difference-endpoint,collar_cost=2*Delta),actual_plane_angular_source=dict(source_ceiling=total,pair_gap=float(gamma.real)-total-2*Delta,net_estimate=total+2*Delta-float(gamma.real)+difference-endpoint,collar_cost=2*Delta))
 out=dict(scope='Floating evaluation of exact original endpoint row formulas and a bounded1D maximization. The low-row critical locations also have the displayed exact algebraic descriptions; no outward numerical certificate is claimed. Any comparison involving A5 remains diagnostic because its incoming maxima were estimated.',type_star=[4,3,4],targets=[.5,0,.5],profiles=rows,raw_pair_rate=total,actual_reference=[[z.real,z.imag]for z in ref],critical_gradient_residual=res,geometric_pair_rate=M,actual_pair_plane_real=float(gamma.real),plane_minus_critical=float(gamma.real-M),raw_pair_gap=M-total,known_common_A5_difference_estimate=difference,endpoint_occupation_debit=endpoint,net_with_endpoint_raw_profile=total-M+difference-endpoint,collar_rho=rho,collar_rate_cost_2Delta=2*Delta,net_with_collar_rate=total+2*Delta-M+difference-endpoint,three_distinct_comparisons=comparisons,all_type_source_ceiling='A[beta,alpha]+B[gamma]+2*Delta_rho+beta*nu_rho; compare to ACTUAL Re(C+P_L*z_L+P_R*z_R). No second Q subtraction.',certified_constant_table=dict(A=[[.360050,.447948],[.485081,.551147]],B=[.347548,.515591]),
 finite_rows=['C0(-1,1)=sum_j (-1)^j p_j(-1)/P_j','C1(1,-1)=sum_j p_j(-1)/P_j^2'],parity='For evenN p_j(-1)=0 at j>=N/2; for oddN those high rows remain and have the retained full profile. Both profile maxima occur belowN/2. Fourier d_N(-1) has uniform upper rate0 for all levels; no root-grid equality is assumed at oddN.',selected_factors='All relevant selected monomials have modulus1 on these real arguments.')
 Path('/tmp/real-seam-half-pair-diagnostic.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':main()
