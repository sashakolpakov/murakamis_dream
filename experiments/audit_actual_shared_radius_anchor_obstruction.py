"""Verify a rational anchored-capacity obstruction on an actual marked source."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,argparse,math
from flint import arb,ctx
sys.path.insert(0,str(Path(__file__).resolve().parent))
from audit_actual_original_marked_face_coefficient import morse_faces

def verify(data,M=8192):
 from collections import Counter
 ctx.prec=192
 ports=data['ports'];zero=set(data['protected']);ordinary=data['ordinary'];anchor=data['anchor'];mixed=set(data['spectator_mixed_ports'])
 chart=morse_faces(data['k'],data['word'],data['mark']);assert chart['circles']==[tuple(p) for p in ports] and (0,chart['v'])==tuple(data['protected'])
 tt=[t for x,b,c,y in ports for t in [(x,b,y),(x,c,y)]]
 assert all(len(set(t))==3 for t in tt)
 edges=Counter(tuple(sorted((t[i],t[(i+1)%3]))) for t in tt for i in range(3));assert len(set(tuple(sorted(t)) for t in tt))==2*len(ports) and set(edges.values())=={2}
 assert len(edges)==3*len(ports) and chart['faces']==len(ports)+2
 assert sorted(ordinary)==[f for f in range(chart['faces']) if f not in zero]
 main={tuple(sorted(v)) for x,b,c,y in ports for v in [(x,b),(b,y),(x,c),(c,y)]}
 assert tuple(sorted(zero)) in main
 assert [(r['port'],r['side']) for r in data['triangles']]==[(e,s) for e in range(len(ports)) if e!=anchor for s in [0,1]]
 assert all(len(r['faces'])==len(r['variables']) for r in data['triangles'])
 vals=[F(v['n'],v['d']) for v in data['variables']];ix={tuple(v['name']):i for i,v in enumerate(data['variables'])};assert len(ix)==len(vals) and min(vals)>=0
 mass={e:(vals[ix[('mass',e)]] if e in mixed else F(1)) for e in range(len(ports)) if e!=anchor}
 loads={f:F(0) for f in ordinary}
 assert sorted(i for r in data['triangles'] for i in r['variables'])==sorted(i for i,v in enumerate(data['variables']) if v['name'][0]=='corner')
 for row in data['triangles']:
  e=row['port'];assert F(0)<mass[e]<=1
  assert sum((vals[i] for i in row['variables']),F(0))==mass[e]/2
  assert tuple(row['faces'])==tuple(f for f in (ports[e][0],ports[e][1+row['side']],ports[e][3]) if f not in zero)
  for f,i in zip(row['faces'],row['variables']):assert tuple(data['variables'][i]['name'])==('corner',e,row['side'],f);loads[f]+=vals[i]
 for e in mixed:loads[ports[e][1]]+=1-mass[e]
 x,b,c,y=ports[anchor];assert x in zero and c in zero
 beta=vals[ix[('anchor_y',anchor,y)]];assert 0<=beta<=F(1,2);loads[b]+=1-beta;loads[y]+=beta
 assert all(v==1 for v in loads.values())
 def ab(f):return arb(f.numerator)/f.denominator
 def lob(a):
  total=arb(0)
  for n in range(1,M+1): total+=(2*n*a).sin()/(2*n*n)
  return total+arb(0,arb(1)/(2*M))
 cache={}
 def fentropy(a):
  if a in (F(0),F(1,2)):return arb(0)
  if a not in cache:cache[a]=(lob(arb.pi()*ab(a))+lob(arb.pi()*ab(F(1,2)-a)))/arb.pi()
  return cache[a]
 primal=arb(0)
 for row in data['triangles']:
  lam=mass[row['port']];primal+=ab(lam)*sum((fentropy(vals[i]/lam) for i in row['variables']),arb(0))
 L={f:arb(0) for f in zero};L.update({int(f):ab(F(*v)) for f,v in data['complete_upper_radii'].items()});assert all(L[f]>0 for f in ordinary)
 qcache={}
 def Q(tri):
  key=tuple(tri)
  if key in qcache:return qcache[key]
  w=[L[f] for f in tri];positive=[v for v in w if not v.is_zero()]
  if len(positive)==1:out=positive[0].log()/2
  else:
   discr=(w[0]*w[1]+w[1]*w[2]+w[2]*w[0]).sqrt();out=arb(0)
   for wj in positive:
    a=(wj/discr).atan();out+=(lob(a)+lob(arb.pi()/2-a))/arb.pi()+a/arb.pi()*wj.log()
  qcache[key]=out;return out
 upper=sum((Q(t) for t in tt),arb(0))-sum((L[f].log() for f in ordinary),arb(0))
 gap=primal-upper
 assert gap>arb('0.025'),gap
 def interval(v):return {'lower':str(v.lower()),'upper':str(v.upper())}
 return {'status':'PASS','scope':'Exact feasible fractional primal for the anchored H-spectator envelope only; not a fixed LEFT/CROSS/RIGHT sector counterexample. The complete volume is bounded above by a rational shared-radius triangle potential; no numerical packing solve is used as proof.','counts':{'ports':len(ports),'triangles':len(tt),'edges':len(edges),'exact_primal_variables':len(vals),'exact_face_targets':len(loads),'mixed_spectator_ports':len(mixed)},'primal_entropy':interval(primal),'complete_capacity_upper':interval(upper),'strict_excess':interval(gap),'uniform_certified_excess':'0.025','fourier_terms':M,'precision_bits':ctx.prec}

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--certificate',type=Path,default=Path(__file__).with_name('actual_shared_radius_anchor_obstruction_certificate.json'))
 parser.add_argument('--output',type=Path,default=Path(__file__).with_name('audit_actual_shared_radius_anchor_obstruction_results.json'))
 args=parser.parse_args()
 result=verify(json.loads(args.certificate.read_text()))
 args.output.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k!='branch_intervals'},indent=2))
if __name__=='__main__':main()
