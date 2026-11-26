#!/usr/bin/env python3
"""Bounded floating grid of affine vertical-star lower bounds; no cover."""
import hashlib,importlib.util,itertools,json,time
from fractions import Fraction as F
from pathlib import Path
import numpy as np
ROOT=Path('/Users/sasha/volume-conjecture')
HELP=ROOT/'repro/diagnostics/2026-11-05-seam-attenuation-vertices/phase_helpers.py'
spec=importlib.util.spec_from_file_location('frozen_floating_phase',HELP)
q=importlib.util.module_from_spec(spec);spec.loader.exec_module(q)
REFS=ROOT/'repro/diagnostics/2026-11-05-seam-actual-plane/seam-actual-plane-common-a3-diagnostic.json'
PROFILES=ROOT/'repro/results/research-mixed-height-resolved-seam-sources.json'
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
bindings={str(f):sha(f)for f in (HELP,REFS,PROFILES)}
data=json.loads(REFS.read_text());profiles=json.loads(PROFILES.read_text())['profiles']
theta=.5;rho=.001;nu=-float(q.g(rho).real);delta=rho*np.log(2)+nu
cut=lambda x,b:np.clip((np.asarray(x)-.1)/(b-.1),0,1)
R=lambda x:np.where(np.asarray(x)<=.45,1,400*(.5-np.asarray(x))**2)

def source(name,h):
 knots=profiles[name];xs=[float(F(v['height']))for v in knots];ys=[float(F(v['upper']))for v in knots]
 assert np.all(h>=xs[0]-1e-12)and np.all(h<=xs[-1]+1e-12)
 return np.interp(h,xs,ys)

def rate(cc,j,a,b,sa,sb):
 val=q.phase(a,b,cc.t(j-1),cc.t(j))[0].real
 return val+.5*sa*np.maximum(q.g(a).real,-2*np.pi*np.asarray(a).imag)+.5*sb*np.maximum(q.g(b).real,-2*np.pi*np.asarray(b).imag)

def evaluate(cc,xL,xR,sig):
 sm2,sL,sR,sp2=sig;t=cc.r(0).real
 xm2,xp2=cc.r(-2).real,cc.r(2).real
 xm3,xp3=cc.r(-3).real,cc.r(3).real
 bL=.12 if sL else .22;bR=.12 if sR else .22
 mL=np.minimum(cut(xL,bL),cut(xm2,bL));mR=np.minimum(cut(xR,bR),cut(xp2,bR))
 xL,xR=np.tile(xL,4),np.tile(xR,4)
 lam=np.concatenate((np.zeros_like(mL),np.ones_like(mL),mL,mR))
 mL,mR=np.tile(mL,4),np.tile(mR,4)
 coefL=(.014 if sL else cc.r(-1).imag)*R(xL)
 coefR=(.014 if sR else cc.r(1).imag)*R(xR)
 hL,hR=coefL*np.minimum(mL,lam),coefR*np.minimum(mR,lam)
 hLs,hRs=coefL*mL,coefR*mR
 hs=cc.r(0).imag*np.minimum(cut(xL,.22),cut(xR,.22))
 left,gL=q.phase(xL,t,cc.t(-1),cc.t(0));right,gR=q.phase(t,xR,cc.t(0),cc.t(1))
 base=left.real+right.real
 linear=(gL[...,0].imag+np.pi*sL)*hLs+(gL[...,1].imag+gR[...,0].imag)*hs+(gR[...,1].imag+np.pi*sR)*hRs
 affine_lower=base-linear
 pair_exact=rate(cc,0,xL+1j*hLs,t+1j*hs,sL,0)+rate(cc,1,t+1j*hs,xR+1j*hRs,0,sR)
 zl,zr=xL+1j*hL,xR+1j*hR;zls,zrs=xL+1j*hLs,xR+1j*hRs
 zm2=cc.target(-2,xm3,xm2,xL,sm2);zp2=cc.target(2,xR,xp2,xp3,sp2)
 dl=rate(cc,-1,zm2,zl,sm2,sL)-rate(cc,-1,zm2,zls,sm2,sL)
 dr=rate(cc,2,zr,zp2,sR,sp2)-rate(cc,2,zrs,zp2,sR,sp2)
 U=source(f'A{cc.t(0)}{cc.t(-1)}',hL)+source(f'B{cc.t(1)}',hR)+2*delta+cc.t(0)*nu
 defect=U-affine_lower+dl+dr
 assert np.min(pair_exact-affine_lower)>-1e-10
 k=int(np.argmax(defect))
 return dict(value=float(defect[k]),pair_only_defect=float((U-affine_lower)[k]),exact_replacement_defect=float((U-pair_exact+dl+dr)[k]),affine_lower=float(affine_lower[k]),exact_repaired_pair=float(pair_exact[k]),affine_loss=float((pair_exact-affine_lower)[k]),source=float(U[k]),real_pair=float(base[k]),vertical_linear_term=float(linear[k]),AA_corrections=[float(dl[k]),float(dr[k])],targets=[float(xL[k]),float(xR[k])],attenuation=float(lam[k]),physical_heights=[float(hL[k]),float(hR[k])],repaired_heights=[float(hLs[k]),float(hs[k]),float(hRs[k])],selected=list(sig),grid_points=len(defect)),float(np.min(pair_exact-affine_lower))

grid=np.unique(np.concatenate((np.linspace(.1,.5,17),[.12,.22,.45])))
xL,xR=np.meshgrid(grid,grid,indexing='ij');xL=xL.ravel();xR=xR.ravel()
rows=[];start=time.monotonic();min_convex=1
for ref in data['references']:
 cc=q.Candidate(ref['word'],[complex(*z)for z in ref['reference']]);assert cc.reference_residual()<1e-9
 for sig in itertools.product(*[(0,1)if cc.t(j)else(0,)for j in(-2,-1,1,2)]):
  result,con=evaluate(cc,xL,xR,sig);min_convex=min(min_convex,con)
  rows.append(dict(word=ref['word'],reference=ref['reference'],**result))
 print('word',ref['word'],'cases',len(rows),'worst',max(v['value']for v in rows),'elapsed',time.monotonic()-start,flush=True)
assert all(sha(Path(f))==v for f,v in bindings.items())
out=dict(scope='Floating bounded grid only. Actual periodic references repeated along isolated seam windows; four independently selected local endpoints. Inner real coordinates and outer halos fixed at reference reals. Exterior corrections are exact complete coherent e differences, not tangent defects w. No interval cover, universal comparison, joint short-run correction or whole-region theorem.',formula='source_height_profiles+collar-[f_pair-Im(phi gradients)*h_repaired-pi*selected_neighbor_heights]+Delta_e_left+Delta_e_right',grid=grid.tolist(),cases=rows,worst=max(rows,key=lambda r:r['value']),minimum_observed_convexity_difference=min_convex,point_evaluations=sum(v['grid_points']for v in rows),dependencies_sha256=bindings,elapsed_seconds=time.monotonic()-start)
Path('/tmp/affine-seam-replacement-diagnostic.json').write_text(json.dumps(out,indent=2)+'\n')
print('DONE',json.dumps(out['worst']),flush=True)
