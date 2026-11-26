#!/usr/bin/env python3
"""Bounded grid after analytic height-triangle relaxation; not a certificate."""
import hashlib,importlib.util,itertools,json,time
from fractions import Fraction as F
from pathlib import Path
import numpy as np
ROOT=Path('/Users/sasha/volume-conjecture')
HELP=ROOT/'repro/diagnostics/2026-11-05-seam-attenuation-vertices/phase_helpers.py'
spec=importlib.util.spec_from_file_location('real_star_phase',HELP)
q=importlib.util.module_from_spec(spec);spec.loader.exec_module(q)
PP=ROOT/'repro/results/research-mixed-height-resolved-seam-sources.json'
profiles=json.loads(PP.read_text())['profiles'];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
bindings={str(p):sha(p)for p in(HELP,PP)}
rho=.001;nu=-float(q.g(rho).real);delta=rho*np.log(2)+nu
cut=lambda x,b:np.clip((np.asarray(x)-.1)/(b-.1),0,1)
R=lambda x:np.where(np.asarray(x)<=.45,1,400*(.5-np.asarray(x))**2)

def profile(name,h):
 knots=profiles[name];xs=[float(F(v['height']))for v in knots];ys=[float(F(v['upper']))for v in knots]
 assert np.all(h>=xs[0]-1e-12)and np.all(h<=xs[-1]+1e-12)
 return np.interp(h,xs,ys)

def side(x,grad,typ,sigma,name,orientation):
 # The type-four unselected endpoint interval is enlarged to[-.057,0].
 cs=[.014]if sigma else([-.057,0]if typ else[-.03,.02])
 values=[];metadata=[]
 for c in cs:
  H=c*R(x)*cut(x,.12 if sigma else .22)
  for k,(hp,hr)in enumerate(((np.zeros_like(H),np.zeros_like(H)),(np.zeros_like(H),H),(H,H))):
   dh=hr-hp;theta=np.pi*(.5-x)
   if orientation=='left':
    upper=np.pi*sigma-typ*theta/2;lower=np.pi*(sigma-.5)-typ*theta/2
   else:
    upper=np.pi*(sigma+.5)-typ*theta/2;lower=np.pi*sigma-typ*theta/2
   correction=upper*np.maximum(dh,0)+lower*np.minimum(dh,0)
   value=profile(name,hp)+(grad+np.pi*sigma)*hr+correction
   values.append(value);metadata.append((c,k,hp,hr,correction))
 matrix=np.stack(values);indices=matrix.argmax(axis=0);best=matrix.max(axis=0)
 return best,indices,metadata

angles=np.unique(np.concatenate((np.linspace(.1,.5,17),[.12,.22,.45])))
left,right=np.meshgrid(angles,angles,indexing='ij');left=left.ravel();right=right.ravel()
rows=[];start=time.monotonic()
for alpha,beta,gamma in itertools.product((0,1),repeat=3):
 tlo,thi=(.27,.33)if beta else(.30,.39)
 for sl,sr in itertools.product((0,1)if alpha else(0,),(0,1)if gamma else(0,)):
  bestcase=None
  for t in np.linspace(tlo,thi,9):
   fl,gl=q.phase(left,t,alpha,beta);fr,gr=q.phase(t,right,beta,gamma)
   lval,li,lmeta=side(left,gl[:,0].imag,alpha,sl,f'A{beta}{alpha}','left')
   rval,ri,rmeta=side(right,gr[:,1].imag,gamma,sr,f'B{gamma}','right')
   fraction=np.minimum(cut(left,.22),cut(right,.22))
   middle_grad=gl[:,1].imag+gr[:,0].imag
   c0s=[-.057,-.02]if beta else[-.03,.02]
   mid=np.stack([middle_grad*c*fraction for c in c0s]);mi=mid.argmax(axis=0)
   defect=lval+rval+mid.max(axis=0)+2*delta+beta*nu-fl.real-fr.real
   k=int(defect.argmax());lm=lmeta[int(li[k])];rm=rmeta[int(ri[k])]
   result=dict(value=float(defect[k]),types=[alpha,beta,gamma],selections=[sl,sr],reals=[float(left[k]),float(t),float(right[k])],source_names=[f'A{beta}{alpha}',f'B{gamma}'],endpoint_reference_heights=[lm[0],rm[0]],middle_reference_height=c0s[int(mi[k])],triangle_vertices=[lm[1],rm[1]],physical_heights=[float(lm[2][k]),float(rm[2][k])],repaired_heights=[float(lm[3][k]),float(c0s[int(mi[k])]*fraction[k]),float(rm[3][k])],AA_acute_envelopes=[float(lm[4][k]),float(rm[4][k])],real_pair=float(fl[k].real+fr[k].real),middle_cost=float(mid[:,k].max()),side_costs=[float(lval[k]),float(rval[k])])
   if bestcase is None or result['value']>bestcase['value']:bestcase=result
  rows.append(bestcase)
 print('types',alpha,beta,gamma,'cases',len(rows),'max',max(v['value']for v in rows),flush=True)
assert all(sha(Path(p))==v for p,v in bindings.items())
out=dict(scope='Floating grid only in three real variables after a conditional analytic acute-gradient envelope and exact convex height-triangle relaxation. The proposed uniform acute gradient lemma is not established by this diagnostic. Independent full typed reference-height intervals replace actual correlations; all inner reals, halos and common attenuation are enlarged by triangle vertices. No multivariate cover, uniform sign, whole finite-source or short-run assembly theorem.',angles=angles.tolist(),middle_samples_per_type=9,real_grid_points=18*9*len(left),cases=rows,worst=max(rows,key=lambda r:r['value']),dependencies_sha256=bindings,elapsed_seconds=time.monotonic()-start)
Path('/tmp/acute-affine-seam-triangle-diagnostic.json').write_text(json.dumps(out,indent=2)+'\n')
print('DONE',json.dumps(out['worst']), 'elapsed',out['elapsed_seconds'],flush=True)
