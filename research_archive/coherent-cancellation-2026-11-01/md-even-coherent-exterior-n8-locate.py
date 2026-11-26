import importlib.util,random,json,time
from pathlib import Path
p='/private/tmp/md-even-coherent-exterior-n8.py';sp=importlib.util.spec_from_file_location('c',p);c=importlib.util.module_from_spec(sp);sp.loader.exec_module(c)
import numpy as np
rng=random.Random(20601)
base=[(0,1,2),(0,3,1),(1,3,2),(0,2,3)]
def flip(faces):
 edges,_=c.pairs(faces)
 es=list(edges);rng.shuffle(es)
 for edge in es:
  i,j=edges[edge];f,g=faces[i],faces[j]
  a,b,cc,d=c.quartet(f,g)
  if tuple(sorted((b,cc))) in edges:continue
  # (a,b,d),(a,d,cc) become (b,d,cc),(b,cc,a).
  out=[t for k,t in enumerate(faces) if k not in (i,j)]+[(b,d,cc),(b,cc,a)]
  c.sphere_link_check(out);return out
 return faces
records=[];tested=[]
for R in range(5,9):
 for sample in range(3):
  faces=base[:]
  while len(faces)<2*R:faces=c.stellar(faces,rng.randrange(len(faces)))
  for _ in range(6*R):faces=flip(faces)
  matches=c.sphere_link_check(faces);rng.shuffle(matches)
  for match in matches[:3]:
   qs=[c.quartet(faces[i],faces[j]) for i,j in match]
   for anchor in range(R):
    coeff=c.exterior(qs,anchor);defects=c.newton_defects(coeff)
    vals=np.array([c.numeric(v) for v in coeff]);nz=np.flatnonzero(vals)
    roots=np.roots(vals[nz[0]:nz[-1]+1][::-1]);nonreal=bool(max(abs(roots.imag),default=0)>1e-6)
    tested.append({'R':R,'sample':sample,'faces':faces,'matching':match,'quartets':qs,'anchor':anchor,'coefficients':coeff,'newton_defects':defects,'located_roots':[[float(z.real),float(z.imag)] for z in roots]})
    if defects or nonreal:
     record={'R':R,'sample':sample,'faces':faces,'matching':match,'quartets':qs,'anchor':anchor,'coefficients':coeff,'newton_defects':defects,'located_roots':[[float(z.real),float(z.imag)] for z in roots]}
     records.append(record);print('candidate',R,sample,anchor,'exact',bool(defects),flush=True)
     Path('/private/tmp/md-even-coherent-exterior-n8-candidates.json').write_text(json.dumps(records,indent=2)+'\n')
     if defects:raise SystemExit
  print('finished',R,sample,'candidates',len(records),flush=True)

Path('/private/tmp/md-even-coherent-exterior-n8-locating-results.json').write_text(json.dumps({'scope':'Completed bounded finite diagnostic only; no general stability or asymptotic implication','tested':tested,'candidates':records},indent=2)+'\n')
