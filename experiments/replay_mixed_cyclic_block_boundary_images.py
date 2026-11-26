#!/usr/bin/env python3
"""Independent sine/cotangent replay of two-angle block image bounds."""
import argparse,ast,hashlib,importlib.util,json,time
from pathlib import Path
from fractions import Fraction as Q
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def box(adr):
 b=[Q(0),Q(1),Q(0),Q(1)]
 for i,bit in enumerate(adr):
  k=2*(i%2);mid=(b[k]+b[k+1])/2;b[k+1-int(bit)]=mid
 return b

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=256);ap.add_argument('--input',type=Path,default=ROOT/'repro/results/research-mixed-cyclic-block-boundary-images.json');ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-cyclic-block-boundary-images-replay.json');args=ap.parse_args()
 d=json.loads(args.input.read_text());assert d['status']=='passed'
 assert d['proof_sha256']==sha(ROOT/'notes/research_mixed_cyclic_critical_height_bounds.md')
 expected={(e,a,b) for e in (0,1) for a,b in ((0,0),(0,1),(1,1))}
 assert {tuple(c['types']) for c in d['cases']}==expected and len(d['cases'])==len(expected)
 author=ROOT/'experiments/certify_mixed_cyclic_block_boundary_images.py';assert d['script_sha256']==sha(author)
 original=ROOT/'repro/results/research-mixed-cyclic-block-localization.json';original_replay=ROOT/'repro/results/research-mixed-cyclic-block-localization-replay.json';assert d['localization_record_sha256']==sha(original)and d['localization_replay_sha256']==sha(original_replay)
 source=ROOT/'experiments/replay_mixed_cyclic_block_localization.py';spec=importlib.util.spec_from_file_location('independent_block_replay',source);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);ctx.prec=args.precision;m.PI=arb.pi();ar=m.ar;rin=list(map(Q,d['input_radii']));rout=list(map(Q,d['output_radii']));h=list(map(Q,d['height_bounds']))
 assert all(0<rin[k]<=m.RADII[k]for k in(0,1))
 tree=ast.parse(source.read_text());fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name=='verify_cell')
 class Capture(ast.NodeTransformer):
  def visit_Return(self,n):
   if isinstance(n.value,ast.Constant)and n.value.value is True:return ast.copy_location(ast.Return(ast.Call(ast.Name('locals',ast.Load()),[],[])),n)
   return n
 fn=Capture().visit(fn);ast.fix_missing_locations(fn);ns=dict(m.__dict__)
 def params(lo,hi,types):
  return [acb(ar(m.CENTERS[t][0]),ar(m.CENTERS[t][1]))+ar(rin[t])*(2*m.PI*m.I*ar(lo[2*i]).union(ar(hi[2*i]))).exp()for i,t in enumerate(types)]
 ns['params']=params;exec(compile(ast.Module(body=[fn],type_ignores=[]),str(source)+'[boundary replay]','exec'),ns);verify=ns['verify_cell']
 result=[];start=time.time()
 for c in d['cases']:
  e,a,b=c['types'];addresses=sorted(c['addresses']);assert len(set(addresses))==len(addresses)
  for x,y in zip(addresses,addresses[1:]):assert not y.startswith(x)
  assert sum((Q(1,2**len(x))for x in addresses),Q(0))==1
  count=split=0
  for address in addresses:
   work=[address]
   while work:
    adr=work.pop();al,ah,bl,bh=box(adr);w=verify((al,Q(0),bl,Q(0)),(ah,Q(0),bh,Q(0)),e,a,b);ok=False
    if w:
     ctr=acb(ar(m.CENTERS[e][0]),ar(m.CENTERS[e][1]));rad=[abs(w['zz'][i]+w['dz'][i]-ctr)+ar(w['rad'][i])for i in(0,1)]
     imag=[(w['zz'][i]+w['dz'][i]).imag+arb(0,ar(w['rad'][i]))for i in(0,1)]
     ok=all(v<ar(rout[e])for v in rad)and all(v>ar(h[2*e])and v<ar(h[2*e+1])for v in imag)
    if ok:count+=1;continue
    assert len(adr)<len(address)+12,(e,a,b,adr)
    work.extend([adr+'0',adr+'1']);split+=1
  row={'types':[e,a,b],'author_boxes':len(addresses),'replay_boxes':count,'refinements':split};result.append(row);print(json.dumps(row),flush=True)
 out={'status':'passed','precision':args.precision,'cases':result,'replay_boxes':sum(x['replay_boxes']for x in result),'refinements':sum(x['refinements']for x in result),'elapsed_seconds':time.time()-start,'input_sha256':sha(args.input),'script_sha256':sha(__file__),'proof_sha256':sha(ROOT/'notes/research_mixed_cyclic_critical_height_bounds.md'),'independent_localization_replay_script_sha256':sha(source),'input_radii':d['input_radii'],'output_radii':d['output_radii'],'height_bounds':d['height_bounds']}
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n');print('PASS boundary images',out['replay_boxes'],flush=True)
if __name__=='__main__':main()
