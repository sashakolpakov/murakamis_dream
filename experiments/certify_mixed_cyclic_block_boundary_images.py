#!/usr/bin/env python3
"""Sharper block images by the distinguished-boundary maximum principle.

Global root holomorphy is supplied first by the completed four-real-dimensional
localization certificate. This two-angle cover is used only for subsequent
harmonic/maximum-modulus image bounds; it does not establish root existence.
"""
import argparse,ast,hashlib,importlib.util,json,time
from pathlib import Path
from fractions import Fraction as Q
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'experiments/certify_mixed_cyclic_block_localization.py'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=192);ap.add_argument('--input-radii',nargs=2,default=['9/100','8/125']);ap.add_argument('--output-radii',nargs=2,default=['83/1000','3/50']);ap.add_argument('--height-bounds',nargs=4,default=['-13/200','17/250','-51/500','-1/1000']);ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-cyclic-block-boundary-images.json');args=ap.parse_args()
 record=ROOT/'repro/results/research-mixed-cyclic-block-localization.json';data=json.loads(record.read_text());assert data['status']=='passed'and data['script_sha256']==sha(SOURCE)
 replay=ROOT/'repro/results/research-mixed-cyclic-block-localization-replay.json';rd=json.loads(replay.read_text());assert rd['status']=='passed'and rd['input_sha256']==sha(record)
 assert rd['proof_sha256']==sha(ROOT/'notes/research_mixed_cyclic_critical_localization.md')
 spec=importlib.util.spec_from_file_location('frozen_localization',SOURCE);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);ctx.prec=args.precision;m.PI=arb.pi();ar=m.ar
 rin=list(map(Q,args.input_radii));rout=list(map(Q,args.output_radii));h=list(map(Q,args.height_bounds));assert all(0<rin[i]<=m.rs[i]for i in (0,1));assert all(rout[i]<rin[i]for i in(0,1))
 tree=ast.parse(SOURCE.read_text());fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name=='certify')
 class Capture(ast.NodeTransformer):
  def visit_Return(self,n):
   if isinstance(n.value,ast.Constant)and n.value.value is True:return ast.copy_location(ast.Return(ast.Call(ast.Name('locals',ast.Load()),[],[])),n)
   return n
 fn=Capture().visit(fn);ast.fix_missing_locations(fn);ns=dict(m.__dict__)
 def arcs(lo,hi,ta,tb):
  return [acb(ar(m.cs[t][0]),ar(m.cs[t][1]))+ar(rin[t])*(2*m.PI*m.I*ar(lo[k]).union(ar(hi[k]))).exp()for k,t in[(0,ta),(2,tb)]]
 ns['pars']=arcs;exec(compile(ast.Module(body=[fn],type_ignores=[]),str(SOURCE)+'[boundary witness]','exec'),ns);cert=ns['certify']
 summaries=[];cases=[];start=time.time()
 for eps in(0,1):
  for ta,tb in[(0,0),(0,1),(1,1)]:
   stack=[('',[Q(0),Q(1),Q(0),Q(1)])];accepted=[];vis=0;maxdepth=0;worst_h=None;worst_rad=None
   while stack:
    adr,box=stack.pop();vis+=1;maxdepth=max(maxdepth,len(adr));assert len(adr)<=28,(eps,ta,tb,adr,box)
    al,ah,bl,bh=box;w=cert((al,Q(0),bl,Q(0)),(ah,Q(0),bh,Q(0)),eps,ta,tb)
    ok=False
    if w:
     ctr=acb(ar(m.cs[eps][0]),ar(m.cs[eps][1]));rr=[abs(w['zz'][i]+w['dz'][i]-ctr)+ar(w['rad'][i])for i in(0,1)]
     im=[(w['zz'][i]+w['dz'][i]).imag+arb(0,ar(w['rad'][i]))for i in(0,1)]
     ok=all(v<ar(rout[eps])for v in rr)and all(v>ar(h[2*eps])and v<ar(h[2*eps+1])for v in im)
    if ok:
     accepted.append(adr)
     up=max(v.upper()for v in rr);worst_rad=up if worst_rad is None else max(worst_rad,up)
     continue
    k=len(adr)%2;j=2*k;mid=(box[j]+box[j+1])/2
    for bit in(0,1):
     child=box.copy();child[j+1-bit]=mid;stack.append((adr+str(bit),child))
   assert sum((Q(1,2**len(a))for a in accepted),Q(0))==1
   summary={'types':[eps,ta,tb],'accepted':len(accepted),'visited':vis,'max_depth':maxdepth,'radius_upper':str(worst_rad)};summaries.append(summary);cases.append({'types':[eps,ta,tb],'addresses':accepted});print(json.dumps(summary),flush=True)
 out={'status':'passed','precision':args.precision,'input_radii':list(map(str,rin)),'output_radii':list(map(str,rout)),'height_bounds':list(map(str,h)),'summaries':summaries,'cases':cases,'elapsed_seconds':time.time()-start,'source_sha256':sha(SOURCE),'localization_record_sha256':sha(record),'localization_replay_sha256':sha(replay),'script_sha256':sha(__file__),'proof_sha256':sha(ROOT/'notes/research_mixed_cyclic_critical_height_bounds.md'),'scope':'Distinguished-boundary output estimates only, using already-established full-bidisk root holomorphy. Smaller input disks require a prior critical inclusion before iteration.'}
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n');print('PASS',sum(s['accepted']for s in summaries),'two-angle cells',flush=True)
if __name__=='__main__':main()
