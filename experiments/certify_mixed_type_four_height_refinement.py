#!/usr/bin/env python3
"""Type-four image heights on the already established critical rectangles.

The completed global block theorem supplies the branch before any boundary
maximum principle is used. This new two-real-parameter cover changes none of
the original existence or window certificates.
"""
import argparse,ast,hashlib,importlib.util,json,time
from pathlib import Path
from fractions import Fraction as Q
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'experiments/certify_mixed_cyclic_block_localization.py'
PROOF=ROOT/'notes/research_mixed_type_four_height_refinement.md'
RECTS=[['3/10','39/100','-3/100','1/50'],
       ['27/100','33/100','-57/1000','-1/1000']]
RECORDS=[
 'repro/results/research-mixed-cyclic-block-localization.json',
 'repro/results/research-mixed-cyclic-block-localization-replay.json',
 'repro/results/research-mixed-cyclic-window-heights.json',
 'repro/results/research-mixed-cyclic-window-heights-replay.json',
 'repro/results/research-mixed-type-three-window-strip.json',
 'repro/results/research-mixed-type-three-window-strip-replay.json']
DEPS=[
 'notes/research_mixed_cyclic_critical_localization.md',
 'notes/research_mixed_cyclic_critical_height_bounds.md',
 'notes/research_mixed_type_three_window_strip.md',
 str(SOURCE.relative_to(ROOT)),
 'experiments/replay_mixed_cyclic_block_localization.py',
 'experiments/certify_mixed_cyclic_window_heights.py',
 'experiments/replay_mixed_cyclic_window_heights.py',
 'experiments/certify_mixed_type_three_window_strip.py',
 'experiments/replay_mixed_type_three_window_strip.py',*RECORDS]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def decode(address):
 box=[Q(0),Q(1),Q(0),Q(1)]
 for j,bit in enumerate(address):
  assert bit in '01';k=2*(j%2);mid=(box[k]+box[k+1])/2
  box[k+1-int(bit)]=mid
 return box

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--precision',type=int,default=192)
 ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-type-four-height-refinement.json')
 args=ap.parse_args()
 initial={p:sha(ROOT/p)for p in DEPS};proof_initial=sha(PROOF);script_initial=sha(__file__)
 for k,p in enumerate(RECORDS):
  data=json.loads((ROOT/p).read_text());assert data['status']=='passed',p
  stem=['mixed_cyclic_block_localization','mixed_cyclic_window_heights','mixed_type_three_window_strip'][k//2]
  script='experiments/'+('replay_'if k%2 else'certify_')+stem+'.py'
  proof=['notes/research_mixed_cyclic_critical_localization.md','notes/research_mixed_cyclic_critical_height_bounds.md','notes/research_mixed_type_three_window_strip.md'][k//2]
  assert data['script_sha256']==sha(ROOT/script),p
  assert data['proof_sha256']==sha(ROOT/proof),p
  if k%2:assert data['input_sha256']==sha(ROOT/RECORDS[k-1]),p
  for key in ['dependencies','dependencies_sha256']:
   for name,h in data.get(key,{}).items():assert sha(ROOT/name)==h,(p,name)
 ld=json.loads((ROOT/RECORDS[0]).read_text());lr=json.loads((ROOT/RECORDS[1]).read_text())
 assert ld['script_sha256']==sha(SOURCE)
 assert lr['input_sha256']==sha(ROOT/RECORDS[0])
 assert lr['proof_sha256']==sha(ROOT/'notes/research_mixed_cyclic_critical_localization.md')
 spec=importlib.util.spec_from_file_location('unchanged_block_author',SOURCE)
 m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 ctx.prec=args.precision;m.PI=arb.pi();ar=m.ar
 inclusion=[]
 for t,rr in enumerate(RECTS):
  xl,xh,yl,yh=map(Q,rr);cx,cy=m.cs[t]
  distance=max((x-cx)**2+(y-cy)**2 for x in (xl,xh)for y in(yl,yh))
  assert distance<m.rs[t]**2
  inclusion.append(str(m.rs[t]**2-distance))
 tree=ast.parse(SOURCE.read_text())
 fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name=='certify')
 class Capture(ast.NodeTransformer):
  def visit_Return(self,node):
   if isinstance(node.value,ast.Constant)and node.value.value is True:
    return ast.copy_location(ast.Return(ast.Call(ast.Name('locals',ast.Load()),[],[])),node)
   return node
 fn=Capture().visit(fn);ast.fix_missing_locations(fn)
 ns=dict(m.__dict__)
 def edge(t,face,lo,hi):
  xl,xh,yl,yh=map(Q,RECTS[t]);v=ar(lo).union(ar(hi))
  if face==0:return acb(ar(xl)+(ar(xh)-ar(xl))*v,ar(yl))
  if face==1:return acb(ar(xh),ar(yl)+(ar(yh)-ar(yl))*v)
  if face==2:return acb(ar(xl)+(ar(xh)-ar(xl))*v,ar(yh))
  if face==3:return acb(ar(xl),ar(yl)+(ar(yh)-ar(yl))*v)
  raise AssertionError(face)
 active_faces=[0,0]
 def pars(lo,hi,ta,tb):
  return [edge(t,active_faces[i],lo[2*i],hi[2*i])for i,t in enumerate((ta,tb))]
 ns['pars']=pars
 exec(compile(ast.Module(body=[fn],type_ignores=[]),str(SOURCE)+'[rectangle image]','exec'),ns)
 certify=ns['certify'];start=time.time();cases=[]
 for ta,tb in((0,0),(0,1),(1,1)):
  for fa in range(4):
   for fb in range(4):
    active_faces[:]=[fa,fb];stack=[''];accepted=[];visits=0;maximum=None
    while stack:
     address=stack.pop();visits+=1
     assert len(address)<=26,(ta,tb,fa,fb,address)
     al,ah,bl,bh=decode(address)
     try:w=certify((al,Q(0),bl,Q(0)),(ah,Q(0),bh,Q(0)),1,ta,tb)
     except (ValueError,ZeroDivisionError,OverflowError):w=False
     ok=False
     if w:
      heights=[(w['zz'][i]+w['dz'][i]).imag+arb(0,ar(w['rad'][i]))for i in(0,1)]
      ok=all(v<ar('-1/50')for v in heights)
     if ok:
      accepted.append(address);value=max(v.upper()for v in heights)
      maximum=value if maximum is None else max(maximum,value)
     else:stack.extend([address+'1',address+'0'])
    leaves=sorted(accepted)
    assert len(set(leaves))==len(leaves)
    assert all(not b.startswith(a)for a,b in zip(leaves,leaves[1:]))
    assert sum((Q(1,2**len(x))for x in leaves),Q(0))==1
    row={'types':[1,ta,tb],'faces':[fa,fb],'addresses':leaves,'accepted':len(leaves),
         'visited':visits,'maximum_imaginary_upper':str(maximum)}
    cases.append(row)
    print(json.dumps({k:v for k,v in row.items()if k!='addresses'}),flush=True)
 assert len(cases)==48
 assert initial=={p:sha(ROOT/p)for p in DEPS}
 assert proof_initial==sha(PROOF)and script_initial==sha(__file__)
 out={'status':'passed','precision_bits':args.precision,'rectangles':RECTS,'upper_height':'-1/50',
      'cases':cases,'case_count':48,'accepted_cells':sum(c['accepted']for c in cases),
      'visited_cells':sum(c['visited']for c in cases),'rectangle_disk_inclusion_margins':inclusion,
      'elapsed_seconds':time.time()-start,'dependencies':initial,
      'script_sha256':script_initial,'proof_sha256':proof_initial,
      'scope':'Both type-four block outputs on the full products of the established critical rectangles. Boundary harmonic principles use independently proved global holomorphy; every actual finite cyclic word is included.'}
 args.output.parent.mkdir(parents=True,exist_ok=True)
 args.output.write_text(json.dumps(out,indent=2)+'\n')
 print('PASS',out['case_count'],'boundary products,',out['accepted_cells'],'cells',flush=True)
if __name__=='__main__':main()
