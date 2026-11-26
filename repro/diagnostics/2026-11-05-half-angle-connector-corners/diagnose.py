#!/usr/bin/env python3
"""Bounded corner diagnostic only; no boundary cover or universal sign."""
import hashlib,importlib.util,itertools,json,time
from fractions import Fraction as F
from pathlib import Path
from flint import arb,acb
ROOT=Path('/Users/sasha/volume-conjecture')
HP=ROOT/'experiments/certify_mixed_hybrid_zero_pair_support.py'
spec=importlib.util.spec_from_file_location('frozen_zero_pair',HP)
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
h.configure(192);p=h.p;ar=h.ar
bound_paths=[HP,ROOT/'experiments/certify_mixed_paired_right_transition_support.py',ROOT/'experiments/certify_mixed_cyclic_window_heights.py',ROOT/'experiments/certify_mixed_real_small_support.py',ROOT/'repro/results/research-mixed-half-angle-seam-source.json']
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
hashes={str(f):sha(f) for f in bound_paths}
half=json.loads(bound_paths[-1].read_text())
c=[arb(half['scalar_values'][f'constant_type{e}'])for e in (0,1)]
rho=ar('1/1000');nu=-p.core.g(acb(rho)).real
delta=rho*arb(2).log()+nu
rows=[];start=time.monotonic();minimum=None
for word in itertools.product((0,1),repeat=5):
 for ta,tb in itertools.product((0,1),repeat=2):
  for fa,va,fb,vb in itertools.product((0,2),(0,1),(0,2),(0,1)):
   p.faces[:]=[fa,fb];bnd=list(map(F,[va,va,vb,vb]))
   w=p.cert(word,ta,tb,bnd,-F(3,25))
   assert w,(word,ta,tb,fa,va,fb,vb,'point root')
   z=[w['boxes'][i]for i in(3,5,7)]
   rf=p.pair(z,word,w['boxes'][4],w['boxes'][6])
   plane=(rf[0]+rf[1][0]*(acb(ar('.5'))-z[0])+rf[1][2]*(acb(ar('.5'))-z[2])).real
   real_cost=ar('5.5')*(ar('.5')-z[0].real)**2+ar('7.55')*(ar('.5')-z[2].real)**2
   collar=2*delta+word[2]*nu
   D=plane-c[word[2]]-c[word[3]]-collar-real_cost
   row=dict(word=word,external_types=[ta,tb],faces=[fa,fb],parameters=[va,vb],external_points=list(map(str,w['p0'])),reference_legs=list(map(str,z)),plane=str(plane),rotated_cost=str(real_cost),collar=str(collar),reserve=str(D),common_collar_reserve=str(plane-c[word[2]]-c[word[3]]-ar('1/50')-real_cost))
   rows.append(row)
   score=float(D.lower())
   if minimum is None or score<minimum[0]:minimum=(score,row)
 assert time.monotonic()-start<180
 print('word',''.join(map(str,word)),len(rows),'minimum',minimum[0],'elapsed',time.monotonic()-start,flush=True)
assert len(rows)==2048 and all(sha(f)==hashes[str(f)]for f in bound_paths)
out=dict(status='bounded-corner-diagnostic-complete',precision_bits=192,points=len(rows),minimum=minimum[1],rows=rows,dependencies_sha256=hashes,elapsed_seconds=time.monotonic()-start,scope='Only 16 exact external rectangle corner pairs for each of 32 windows and 4 external type pairs. Point root/phase enclosures are outward; no full boundary/domain coverage or universal reserve theorem.')
path=Path('/tmp/uniform-half-angle-connector-corners.json');path.write_text(json.dumps(out,indent=2)+'\n')
print('DONE',len(rows),minimum[0],json.dumps(minimum[1]),flush=True)
