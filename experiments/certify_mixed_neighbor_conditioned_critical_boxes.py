#!/usr/bin/env python3
"""Three-vertex geometric images; no right-transition source conclusion."""
from pathlib import Path
from fractions import Fraction as F
import argparse,ast,hashlib,importlib.util,itertools,json,time
from flint import arb,acb,ctx

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_neighbor_conditioned_critical_boxes.md'
SRC=ROOT/'experiments/certify_mixed_cyclic_window_heights.py'
RECTS=[['3/10','39/100','-3/100','1/50'],
       ['27/100','33/100','-57/1000','-1/50']]
# Bounds in order: Re(t_1), Im(t_1), Im(t_0), all in thousandths.
LIMITS={
 '000':[[322,349],[-10,10],[-17,10]],
 '001':[[358,379],[-17,-2],[-19,7]],
 '010':[[271,292],[-49,-30],[-25,1]],
 '011':[[302,318],[-57,-43],[-25,1]],
 '100':[[311,334],[-17,2],[-51,-31]],
 '101':[[346,363],[-25,-11],[-53,-34]],
 '110':[[268,288],[-54,-36],[-61,-42]],
 '111':[[299,313],[-62,-49],[-61,-42]],
}

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def decode(address):
 box=[F(0),F(1),F(0),F(1)]
 for j,c in enumerate(address):
  assert c in '01';k=2*(j%2);mid=(box[k]+box[k+1])/2
  box[k+1-int(c)]=mid
 return box

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--precision',type=int,default=256)
 ap.add_argument('--word')
 ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-neighbor-conditioned-critical-boxes.json')
 args=ap.parse_args();assert args.precision>=160;ctx.prec=args.precision
 deps=['experiments/certify_mixed_cyclic_window_heights.py',
       'notes/research_mixed_cyclic_critical_localization.md',
       'notes/research_mixed_cyclic_critical_height_bounds.md',
       'notes/research_mixed_type_three_window_strip.md',
       'notes/research_mixed_type_four_height_refinement.md']
 inherited=[
  ('cyclic-block-localization','certify_mixed_cyclic_block_localization.py','research_mixed_cyclic_critical_localization.md'),
  ('cyclic-window-heights','certify_mixed_cyclic_window_heights.py','research_mixed_cyclic_critical_height_bounds.md'),
  ('type-three-window-strip','certify_mixed_type_three_window_strip.py','research_mixed_type_three_window_strip.md'),
  ('type-four-height-refinement','certify_mixed_type_four_height_refinement.py','research_mixed_type_four_height_refinement.md')]
 for name,script,proof in inherited:
  record='repro/results/research-mixed-'+name+'.json'
  for p in(record,'experiments/'+script,'notes/'+proof):
   if p not in deps:deps.append(p)
  r=json.loads((ROOT/record).read_text())
  assert r['status']=='passed'
  assert r['script_sha256']==sha(ROOT/'experiments'/script)
  assert r['proof_sha256']==sha(ROOT/'notes'/proof)
  for key in('dependencies','dependencies_sha256'):
   for p,h in r.get(key,{}).items():assert sha(ROOT/p)==h,(record,p)
 hashes={p:sha(ROOT/p)for p in deps};ph,sh=sha(PROOF),sha(__file__)
 spec=importlib.util.spec_from_file_location('unchanged_window_primitive',SRC)
 m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);m.PI=arb.pi();ar=m.ar
 faces=[0,0]
 def params(box,ta,tb):
  ans=[]
  for k,ty in enumerate((ta,tb)):
   xl,xh,yl,yh=map(F,RECTS[ty]);v=ar(box[2*k]).union(ar(box[2*k+1]));face=faces[k]
   ans.append(acb(ar(xl)+ar(xh-xl)*v,ar(yl if face==0 else yh))if face in(0,2)
              else acb(ar(xh if face==1 else xl),ar(yl)+ar(yh-yl)*v))
  return ans
 fn=next(x for x in ast.parse(SRC.read_text()).body if isinstance(x,ast.FunctionDef)and x.name=='certify')
 class Capture(ast.NodeTransformer):
  def visit_Return(self,node):
   if isinstance(node.value,ast.List):
    return ast.copy_location(ast.Return(ast.Call(ast.Name('locals',ast.Load()),[],[])),node)
   return node
 fn=Capture().visit(fn);ast.fix_missing_locations(fn);ns=dict(m.__dict__);ns['params']=params
 exec(compile(ast.Module(body=[fn],type_ignores=[]),str(SRC)+'[three-window image]','exec'),ns)
 certify=ns['certify'];rows=[];start=time.time();visits=0
 words=[args.word]if args.word else list(LIMITS)
 for wordstr in words:
  assert wordstr in LIMITS;word=tuple(map(int,wordstr))
  limits=[[F(v,1000)for v in pair]for pair in LIMITS[wordstr]]
  for ta,tb,fa,fb in itertools.product(range(2),range(2),range(4),range(4)):
   faces[:]=[fa,fb];stack=[''];leaves=[];hulls=None
   while stack:
    address=stack.pop();visits+=1;assert len(address)<=28,(wordstr,ta,tb,fa,fb,address)
    try:w=certify(word,ta,tb,decode(address),-F(3,25))
    except(ValueError,ZeroDivisionError,OverflowError):w=False
    ok=False
    if w:
     vals=[w['boxes'][3].real,w['boxes'][3].imag,w['boxes'][1].imag]
     ok=all(v>ar(lo)and v<ar(hi)for v,(lo,hi)in zip(vals,limits))
    if ok:
     leaves.append(address)
     hulls=vals if hulls is None else [x.union(y)for x,y in zip(hulls,vals)]
    else:stack.extend([address+'1',address+'0'])
   codes=sorted(leaves);assert len(codes)==len(set(codes))
   assert all(not b.startswith(a)for a,b in zip(codes,codes[1:]))
   assert sum((F(1,2**len(a))for a in codes),F(0))==1
   row=dict(word=wordstr,external_types=[ta,tb],faces=[fa,fb],addresses=codes,
            accepted=len(codes),coordinate_hulls=[str(x)for x in hulls]);rows.append(row)
   print('progress',len(rows),wordstr,ta,tb,fa,fb,len(codes),visits,time.time()-start,flush=True)
   Path(str(args.output)+'.partial').write_text(json.dumps(dict(status='running',cases=rows),separators=(',',':'))+'\n')
 assert len(rows)==64*len(words)
 assert len({(r['word'],*r['external_types'],*r['faces'])for r in rows})==len(rows)
 assert hashes=={p:sha(ROOT/p)for p in deps}and ph==sha(PROOF)and sh==sha(__file__)
 out=dict(status='partial-word-passed'if args.word else'passed',precision_bits=args.precision,
          boundary_products=len(rows),accepted_cells=sum(r['accepted']for r in rows),visited_cells=visits,
          rectangles=RECTS,limits_in_thousandths=LIMITS,cases=rows,elapsed_seconds=time.time()-start,
          script_sha256=sh,proof_sha256=ph,dependencies=hashes,
          scope='Neighbor-conditioned geometric bounds from original three-vertex open windows. No paired source or whole-transition estimate.')
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n')
 Path(str(args.output)+'.partial').unlink(missing_ok=True)
 print('PASS',len(rows),out['accepted_cells'],visits,flush=True)

if __name__=='__main__':main()
