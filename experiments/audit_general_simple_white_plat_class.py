#!/usr/bin/env python3
"""Check the literal simple-white plat family and knot parity at widths 2--30."""
from pathlib import Path
import sys,json,argparse
from collections import Counter
sys.path.insert(0,str(Path(__file__).resolve().parent))
from audit_actual_original_marked_face_coefficient import morse_faces
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path,default=Path(__file__).with_name('general_simple_white_plat_class_results.json'))
args=parser.parse_args()
records=[]
for k in range(2,31):
 O=list(range(1,2*k-2,2));E=list(range(0,2*k-1,2));w=O+E+O if k>=3 else [1,0,1]
 data=morse_faces(k,w);tris=[t for x,b,c,y in data['circles'] for t in ((x,b,y),(x,y,c))]
 assert all(len(set(t))==3 for t in tris)
 edge=Counter(tuple(sorted((t[i],t[(i+1)%3]))) for t in tris for i in range(3))
 assert set(edge.values())=={2}
 assert len({tuple(sorted(t)) for t in tris})==len(tris)
 assert data['faces']-len(edge)+len(tris)==2
 if k>=3:
  # The audit compiler orders its final faces exactly as these named gaps.
  u=0;a=list(range(1,k+1));e=[u]+list(range(k+1,2*k))+[u];b=list(range(2*k,3*k))
  expected=[(a[j-1],u,e[j],a[j]) for j in range(1,k)]
  expected += [(e[j],a[j],b[j],e[j+1]) for j in range(k)]
  expected += [(b[j-1],e[j],u,b[j]) for j in range(1,k)]
  assert data['circles']==expected
 perm=list(range(2*k))
 for slot in O:perm[slot],perm[slot+1]=perm[slot+1],perm[slot]
 parent=list(range(2*k))
 def root(v):
  while parent[v]!=v:v=parent[v]
  return v
 def join(a,b):parent[root(a)]=root(b)
 for j in range(k):join(2*j,2*j+1);join(perm[2*j],perm[2*j+1])
 assert len({root(j) for j in range(2*k)})==1
 records.append(dict(k=k,ports=len(w),white_vertices=data['faces'],white_edges=len(edge),triangles=len(tris),main_components=1))
out=dict(status='PASS',scope='Literal source gap incidences, simplicity, sphere counts and knot parity for the explicit family; general k proof and RA geometry are analytic.',widths=records)
args.output.write_text(json.dumps(out,indent=2)+'\n')
print('PASS',len(records),'widths; last',records[-1])
