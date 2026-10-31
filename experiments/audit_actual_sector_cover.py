"""Finite actual-sector cover: exact source/flow data plus certified shared radii."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import argparse,json,sys,math,itertools
from flint import arb,ctx
sys.path.insert(0,str(Path(__file__).resolve().parent))
from audit_actual_original_marked_face_coefficient import morse_faces
def pair(f):return [f.numerator,f.denominator]
def verify(d,M=2048):
 ctx.prec=192;ports=d['ports'];R=len(ports);zero=set(d['protected']);ordinary=d['ordinary'];B=d['bad_ports'];chart=morse_faces(d['k'],d['word'],d['mark'])
 assert chart['circles']==list(map(tuple,ports)) and (0,chart['v'])==tuple(d['protected']);assert ordinary==[f for f in range(chart['faces']) if f not in zero]
 tris=[t for x,b,c,y in ports for t in [(x,b,y),(x,c,y)]];assert all(len(set(t))==3 for t in tris) and len({tuple(sorted(t)) for t in tris})==2*R
 ed=Counter(tuple(sorted((t[j],t[(j+1)%3]))) for t in tris for j in range(3));assert len(ed)==3*R and set(ed.values())=={2}
 vals=[F(*v['value']) for v in d['complete_variables']];assert min(vals)>=0;assert {(r['port'],r['side']) for r in d['triangle_rows']}==set(itertools.product(range(R),range(2))) and len(d['triangle_rows'])==2*R
 assert all(len(r['variables'])==len(r['faces']) for r in d['triangle_rows'])
 assert sorted(i for r in d['triangle_rows'] for i in r['variables'])==list(range(len(vals)))
 loads={f:F(0) for f in ordinary}
 for r in d['triangle_rows']:
  e=r['port'];fs=[f for f in (ports[e][0],ports[e][1+r['side']],ports[e][3]) if f not in zero];assert fs==r['faces'];assert sum((vals[i] for i in r['variables']),F(0))==F(1,2)
  for f,i in zip(fs,r['variables']):assert d['complete_variables'][i]['name']==[e,r['side'],f];loads[f]+=vals[i]
 assert all(v==1 for v in loads.values())
 # Symbolic branch-cover verification:15 nonempty bad-R subsets, then every
 # possible one-sided anchor in the no-bad-R branch. No actual sector is lost.
 expected=[]
 for mask in itertools.product([False,True],repeat=len(B)):
  if any(mask):
   tags=['H']*R
   for e,on in zip(B,mask):tags[e]='R' if on else '!R'
   expected.append(tags)
 for e,(x,b,c,y) in enumerate(ports):
  for tag,f in [('L',c),('R',b)]:
   if f in zero or (e in B and tag=='R'):continue
   tags=['H']*R
   for j in B:tags[j]='!R'
   tags[e]=tag;expected.append(tags)
 assert [r['tags'] for r in d['branches']]==expected
 main_edges={tuple(sorted(edge)) for x,b,c,y in ports for edge in [(x,b),(b,y),(x,c),(c,y)]}
 assert tuple(sorted(zero)) in main_edges
 def ab(f):return arb(f.numerator)/f.denominator
 def lob(a):
  s=arb(0)
  for n in range(1,M+1):s+=(2*n*a).sin()/(2*n*n)
  return s+arb(0,arb(1)/(2*M))
 ec={}
 def ent(a):
  if a in (F(0),F(1,2)):return arb(0)
  if a not in ec:ec[a]=(lob(arb.pi()*ab(a))+lob(arb.pi()*ab(F(1,2)-a)))/arb.pi()
  return ec[a]
 lower=sum((ent(a) for a in vals),arb(0))
 def maxb(v):
  lo=max(a.lower() for a in v);hi=max(a.upper() for a in v);return (arb(lo)+arb(hi))/2+arb(0,(arb(hi)-arb(lo))/2)
 gaps=[];caps=[]
 for branch in d['branches']:
  L={f:arb(0) for f in zero};L.update({int(f):ab(F(*v)) for f,v in branch['radii'].items()});assert set(L)==set(range(R+2)) and all(L[f]>0 for f in ordinary)
  qc={}
  def Q(tri):
   key=tuple(sorted(tri))
   if key in qc:return qc[key]
   w=[L[f] for f in tri];pos=[v for v in w if not v.is_zero()]
   if len(pos)==1:a=pos[0].log()/2
   else:
    discr=(w[0]*w[1]+w[1]*w[2]+w[2]*w[0]).sqrt();a=arb(0)
    for v in pos:
     t=(v/discr).atan();a+=(lob(t)+lob(arb.pi()/2-t))/arb.pi()+t/arb.pi()*v.log()
   qc[key]=a;return a
  value=arb(0)
  for tag,(x,b,c,y) in zip(branch['tags'],ports):
   qb=Q((x,b,y));qcc=Q((x,c,y));X=qb+qcc
   if tag=='H':choices=[X]+[L[f].log() for f in (b,c) if f not in zero]
   elif tag=='!R':choices=[X]+([L[c].log()] if c not in zero else [])
   elif tag=='R':assert b not in zero;choices=[L[b].log(),qcc+L[b].log()/2]
   elif tag=='L':assert c not in zero;choices=[L[c].log(),qb+L[c].log()/2]
   else:raise AssertionError(tag)
   value+=maxb(choices)
  value-=sum((L[f].log() for f in ordinary),arb(0));gap=lower-value;assert gap>arb('.04'),gap;gaps.append(gap);caps.append(value)
 def it(v):return {'lower':str(v.lower()),'upper':str(v.upper())}
 return {'status':'PASS','scope':'Exact original source and complete rational feasible triangle flow provide a lower bound on Phi. Forty fixed rational shared-radius branches cover every non-CROSS actual path sector, using only RIGHT versus CROSS/LEFT grouping at four ports; all branch upper rates are strictly smaller. No optimizer is used by verification, and no universal fixed-sector capacity bound is inferred.','counts':{'original_ports':R,'original_triangles':2*R,'original_edges':len(ed),'exact_complete_flow_variables':len(vals),'exact_ordinary_targets':len(ordinary),'nonempty_bad_R_branches':15,'no_bad_R_anchors':len(expected)-15,'rational_shared_radius_branches':len(expected)},'complete_entropy_lower':it(lower),'largest_branch_upper':str(max(v.upper() for v in caps)),'smallest_certified_gap':str(min(v.lower() for v in gaps)),'uniform_certified_gap':'.04','precision_bits':ctx.prec,'fourier_terms':M,'branch_intervals':[{'index':i,'capacity':it(c),'gap':it(g)} for i,(c,g) in enumerate(zip(caps,gaps))]}
def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--certificate',type=Path,default=Path(__file__).with_name('actual_sector_cover_certificate.json'))
 parser.add_argument('--output',type=Path,default=Path(__file__).with_name('audit_actual_sector_cover_results.json'))
 args=parser.parse_args()
 result=verify(json.loads(args.certificate.read_text()))
 args.output.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k!='branch_intervals'},indent=2))
if __name__=='__main__':main()
