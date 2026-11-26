#!/usr/bin/env python3
"""Saved-configuration attenuation-vertex diagnostics; no optimization or cover."""
import argparse,hashlib,json,time
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from phase_helpers import Candidate,g,THETA

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
INPUTS={
 'witnesses':ROOT/'repro/diagnostics/2026-11-05-seam-actual-plane/seam-actual-plane-common-a3-diagnostic.json',
 'repairs':ROOT/'repro/diagnostics/2026-11-05-seam-exact-halo-repairs/seam-exact-halo-repairs-diagnostic.json',
 'grid_repairs':ROOT/'repro/diagnostics/2026-11-05-seam-exact-halo-repairs/seam-exact-halo-repairs-grid-diagnostic.json',
 'profiles':ROOT/'repro/results/research-mixed-height-resolved-seam-sources.json',
}
RHO=.001

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def evaluator(cc,witness,selection2,inner_halos,profiles):
 xm2,xm1,xp1,xp2,_=witness['variables_xm2_xm1_xp1_xp2_lambda']
 sm2,sl,sr=witness['selection_xm2_xm1_xp1'];xm3,xp3=inner_halos
 bL=.12 if sl else .22;bR=.12 if sr else .22;p0=cc.r(0).real
 cut=lambda x,b:float(np.clip((x-.1)/(b-.1),0,1))
 mleft=min(cut(xm2,bL),cut(xm1,bL));mright=min(cut(xp1,bR),cut(xp2,bR))
 outstate=[xm2,xm1,p0];instate=[p0,xp1,xp2]
 E=float(cc.E3(0,outstate,(sm2,sl,0))[0]);A=float(cc.V(2,instate,(0,sr,selection2))[0])
 psi=float(cc.om(-2,xm2,sm2)+cc.om(-1,xm1,sl)+cc.om(0,p0,0))
 occupation=THETA*.5*float(cc.om(-1,xm1,sl)+cc.om(1,xp1,sr))
 closure=-E-A-(1-THETA)*psi-occupation
 nu=-float(g(RHO).real);Delta=RHO*np.log(2)+nu
 collar=2*Delta+cc.t(0)*nu
 def profile(name,h):
  knots=profiles[name];xs=np.array([float(F(z['height'])) for z in knots]);ys=np.array([float(F(z['upper'])) for z in knots])
  assert np.all(h>=xs[0]-1e-14) and np.all(h<=xs[-1]+1e-14)
  return np.interp(h,xs,ys)
 def evaluate(lambdas):
  lam=np.asarray(lambdas,dtype=float).reshape(-1);assert np.all((lam>=0)&(lam<=1))
  n=len(lam);col=lambda x:np.full(n,x)
  xiL=.1+(bL-.1)*lam;xiR=.1+(bR-.1)*lam
  exphys=np.column_stack((col(xm3),col(xm2),col(xm1),xiL));exbase=exphys.copy();exbase[:,3]=p0
  enphys=np.column_stack((xiR,col(xp1),col(xp2),col(xp3)));enbase=enphys.copy();enbase[:,0]=p0
  de=cc.w(-1,exphys,(0,sm2,sl,0),True)[0]-cc.w(-1,exbase,(0,sm2,sl,0),True)[0]
  di=cc.w(2,enphys,(0,sr,selection2,0),True)[0]-cc.w(2,enbase,(0,sr,selection2,0),True)[0]
  zl=cc.target(-1,col(xm2),col(xm1),xiL,sl)
  zr=cc.target(1,xiR,col(xp1),col(xp2),sr)
  source=profile(f'A{cc.t(0)}{cc.t(-1)}',zl.imag)+profile(f'B{cc.t(1)}',zr.imag)
  xseam=RHO*(1-lam)
  fl,gl=cc.base[0];fr,gr=cc.base[1%cc.m]
  # Both original complex tangent planes, including the numerical middle
  # residual. At the exact reference that middle coefficient is zero.
  plane=(fl+gl[0]*(zl-cc.r(-1))+gl[1]*(xseam-cc.r(0))
         +fr+gr[0]*(xseam-cc.r(0))+gr[1]*(zr-cc.r(1))).real
  total=closure+de+di+source+collar-plane
  assert np.isfinite(total).all()
  return [dict(lambda_value=float(v),value=float(t),Delta_exit=float(a),Delta_entry=float(b),source=float(s),collar=collar,actual_pair_plane=float(p),physical_neighbor_heights=[float(hl),float(hr)],base_closure=-E-A,Psi_out=psi,outgoing_occupation_debit=(1-THETA)*psi,endpoint_occupation_debit=occupation,exit_E3=E,entry_A3=A)
          for v,t,a,b,s,p,hl,hr in zip(lam,total,de,di,source,plane,zl.imag,zr.imag)]
 return evaluate,mleft,mright

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--output',type=Path,default=HERE/'results.json')
 args=ap.parse_args();assert not args.output.exists(),'refuse overwrite; choose a distinct --output'
 started=time.time();hashes={str(p.relative_to(ROOT)):sha(p) for p in INPUTS.values()}
 code_hashes={p.name:sha(p) for p in (Path(__file__),HERE/'phase_helpers.py')}
 data={k:json.loads(p.read_text()) for k,p in INPUTS.items()}
 assert data['profiles']['status']=='passed' and data['profiles']['extracted_zero_slope_knots']==19
 refs={tuple(r['word']):np.array([complex(*z) for z in r['reference']]) for r in data['witnesses']['references']}
 candidates={word:Candidate(word,r) for word,r in refs.items()}
 residuals={','.join(map(str,w)):c.reference_residual() for w,c in candidates.items()}
 assert max(residuals.values())<1e-9
 prior_grid={(c['original_case'],c['selection_xp2']):c for c in data['grid_repairs']['cases']}
 cases=[];prior_errors=[];convexity=[];endpoint_count=interior_count=0
 for saved in data['repairs']['cases']:
  idx=saved['original_case'];sel2=saved['selection_xp2'];w=data['witnesses']['cases'][idx];cc=candidates[tuple(w['word'])]
  assert w['word']==saved['word'] and w['selection_xm2_xm1_xp1']==saved['selection_xm2_xm1_xp1']
  modes=[('reference',saved['inner_halos_xm3_xp3'],saved['value'])]
  grid=prior_grid[idx,sel2]
  if grid['maximizing_sampled_halos']!=modes[0][1]:modes.append(('saved_grid_maximizer',grid['maximizing_sampled_halos'],grid['value']))
  for mode,halos,prior in modes:
   fn,ml,mr=evaluator(cc,w,sel2,halos,data['profiles']['profiles'])
   old=fn([w['variables_xm2_xm1_xp1_xp2_lambda'][-1]])[0]
   err=abs(old['value']-prior);prior_errors.append(err);assert err<1e-10,(idx,sel2,mode,err)
   vertices=sorted(set([0.,1.,ml,mr]));endpoint_rows=fn(vertices);endpoint_count+=len(vertices)
   probes=[]
   for lo,hi in zip(vertices,vertices[1:]):
    for fraction in (.25,.5,.75):probes.append((lo+(hi-lo)*fraction,lo,hi,fraction))
   interior_rows=fn([p[0] for p in probes]);interior_count+=len(probes)
   bylambda={r['lambda_value']:r['value'] for r in endpoint_rows}
   for p,r in zip(probes,interior_rows):
    _,lo,hi,f=p;chord=(1-f)*bylambda[lo]+f*bylambda[hi]
    r['chord_upper']=chord;r['observed_chord_excess']=r['value']-chord
    convexity.append(r['observed_chord_excess'])
   cases.append(dict(original_case=idx,word=w['word'],selection_xm2_xm1_xp1=w['selection_xm2_xm1_xp1'],selection_xp2=sel2,physical_A_reals=w['variables_xm2_xm1_xp1_xp2_lambda'][:4],inner_halo_mode=mode,inner_halos_xm3_xp3=halos,m_left=ml,m_right=mr,candidate_vertices=vertices,endpoint_values=endpoint_rows,interior_values=interior_rows,worst_endpoint=max(endpoint_rows,key=lambda r:r['value']),prior_value_error=err))
 worst=max(cases,key=lambda r:r['worst_endpoint']['value'])
 assert all(sha(ROOT/p)==h for p,h in hashes.items())
 assert all(sha(HERE/p)==h for p,h in code_hashes.items())
 result=dict(scope='Floating attenuation-candidate evaluation at saved physical A-coordinate/selection/reference configurations only. Exact original-w repair differences, full source height profiles, actual pair tangent planes and occupation retained. No new optimization, root proposal, interval cover, universal sign or whole-period conclusion. Independent end corrections represent runs of length at least3; the joint length2 correction and singleton case are excluded.',theta=THETA,collar_width=RHO,input_sha256=hashes,local_code_sha256=code_hashes,reference_gradient_residuals=residuals,saved_witness_count=29,selection_configurations=49,fixed_inner_halo_configurations=len(cases),endpoint_evaluations=endpoint_count,interior_evaluations=interior_count,cases=cases,worst_endpoint_configuration=worst,positive_endpoint_values=sum(r['value']>0 for c in cases for r in c['endpoint_values']),largest_observed_interior_chord_excess=max(convexity),interior_check_tolerance=1e-10,interior_checks_pass=max(convexity)<1e-10,maximum_prior_value_error=max(prior_errors),optimization_jobs=0,new_interval_cells=0,elapsed_seconds=time.time()-started)
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(dict(configurations=len(cases),endpoint_evaluations=endpoint_count,interior_evaluations=interior_count,worst=worst,largest_chord_excess=max(convexity),elapsed_seconds=result['elapsed_seconds']),indent=2))
if __name__=='__main__':main()
