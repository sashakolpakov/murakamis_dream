#!/usr/bin/env python3
"""Extract correlated root images from the completed universal cover.

No adaptive cover is rerun. The frozen author self-map test is re-evaluated
on each stored accepted address, and its successful affine witness is
returned by a transparent AST instrumentation of that test. Nothing in
the frozen source or author/replay records is modified.
"""
import argparse,ast,gzip,hashlib,importlib.util,json,math,time
from pathlib import Path
from fractions import Fraction as Q
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'experiments/certify_mixed_cyclic_block_localization.py'
RECORD=ROOT/'repro/results/research-mixed-cyclic-block-localization.json'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def decode(address):
 lo=[Q(-1)]*4;hi=[Q(1)]*4
 for j,v in enumerate(address):
  k=j%4;m=(lo[k]+hi[k])/2
  if v=='0':hi[k]=m
  else:lo[k]=m
 return tuple(lo),tuple(hi)
def exact_complex(z):return [str(z.real),str(z.imag)]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=192);ap.add_argument('--own',type=int,choices=[0,1]);ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-cyclic-block-images.json.gz');ap.add_argument('--responses',action='store_true');args=ap.parse_args()
 d=json.loads(RECORD.read_text());assert d['status']=='passed' and d['script_sha256']==sha(SOURCE)
 for p,h in d['dependencies'].items():assert sha(ROOT/p)==h
 assert sha(ROOT/'notes/research_mixed_cyclic_critical_localization.md')==d['proof_sha256']
 spec=importlib.util.spec_from_file_location('frozen_localization_author',SOURCE);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);ctx.prec=args.precision;mod.PI=arb.pi()
 # Replace only successful return True in certify by return of its local witness.
 tree=ast.parse(SOURCE.read_text());fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name=='certify')
 class Capture(ast.NodeTransformer):
  def visit_Return(self,node):
   if isinstance(node.value,ast.Constant)and node.value.value is True:
    return ast.copy_location(ast.Return(ast.Call(ast.Name('locals',ast.Load()),[],[])),node)
   return node
 fn=Capture().visit(fn);ast.fix_missing_locations(fn);ns=dict(mod.__dict__);exec(compile(ast.Module(body=[fn],type_ignores=[]),str(SOURCE)+'[witness capture]','exec'),ns);certify=ns['certify']
 # PI is a shared exact interval constant at the selected precision.
 ns['PI']=arb.pi();ar=mod.ar
 scale=10**12
 def lower(x):
  n=math.floor(float(x.lower())*scale)
  while ar(Q(n,scale))>x.lower():n-=1
  return Q(n,scale)
 def upper(x):
  n=math.ceil(float(x.upper())*scale)
  while ar(Q(n,scale))<x.upper():n+=1
  return Q(n,scale)
 def hull(z):return [lower(z.real),upper(z.real),lower(z.imag),upper(z.imag)]
 allout=[];summaries=[];start=time.time()
 for case in d['cases']:
  eps,ta,tb=case['types']
  if args.own is not None and eps!=args.own:continue
  extrema=None;response=arb(0);worst_im=None;worst_lo=None;rows=[];t0=time.time()
  for num,address in enumerate(case['accepted']):
   lo,hi=decode(address);w=certify(lo,hi,eps,ta,tb);assert w,(case['types'],address)
   zbox=[w['zz'][i]+w['dz'][i]+acb(arb(0,ar(w['rad'][i])),arb(0,ar(w['rad'][i])))for i in range(2)]
   hh=[hull(z)for z in zbox]
   if extrema is None:extrema=[h[:]for h in hh]
   else:
    for i in range(2):
     for j in (0,2):extrema[i][j]=min(extrema[i][j],hh[i][j])
     for j in (1,3):extrema[i][j]=max(extrema[i][j],hh[i][j])
   high=max(h[3]for h in hh);low=min(h[2]for h in hh)
   if worst_im is None or high>worst_im[0]:worst_im=(high,address)
   if worst_lo is None or low<worst_lo[0]:worst_lo=(low,address)
   if args.responses:
    ee=[[abs(v).upper()for v in row]for row in w['ee']]
    delta=(1-ee[0][0])*(1-ee[1][1])-ee[0][1]*ee[1][0]
    assert delta>0,(case['types'],address,'absolute inverse determinant')
    inv=[[ (1-ee[1][1])/delta,ee[0][1]/delta],[ee[1][0]/delta,(1-ee[0][0])/delta]]
    e=[abs(2*mod.PI*mod.I/(1-(-2*mod.PI*mod.I*(zbox[i]+w['pp'][i])).exp()))for i in range(2)]
    ye=[sum((abs(w['yy'][i][j])*e[j]for j in range(2)),arb(0))for i in range(2)]
    bound=max(sum((inv[i][j]*ye[j]for j in range(2)),arb(0)).upper()for i in range(2))
    response=max(response,bound)
   # Decimal proposals are exact rationals in the original interval test.
   zz=[[str(v.real),str(v.imag)]for v in w['z']]
   DD=[[[str(v.real),str(v.imag)]for v in row]for row in w['D']]
   radii=[str(r)for r in w['rad']]
   rows.append([address,zz,DD,radii])
  summary={'types':case['types'],'cells':len(rows),'output_hulls':[[str(v)for v in h]for h in extrema], 'maximum_output_imaginary':[str(worst_im[0]),worst_im[1]],'minimum_output_imaginary':[str(worst_lo[0]),worst_lo[1]],'elapsed_seconds':time.time()-t0}
  if args.responses:summary['implicit_response_infinity_norm_upper']=str(response)
  summaries.append(summary);allout.append({'types':case['types'],'rows':rows});print(json.dumps(summary),flush=True)
 out={'status':'passed','precision':args.precision,'schema':'correlated-block-images-v1','columns':['address','center_complex_pairs','linear_complex_pairs','remainder_radii'],'interpretation':'z(p)=center+linear*(p-exact_parameter_midpoint)+w, |w_i|<=remainder_radii[i]. Inputs and midpoint decode from the frozen typed-disk address.','summary':summaries,'cases':allout,'elapsed_seconds':time.time()-start,'author_record_sha256':sha(RECORD),'source_sha256':sha(SOURCE),'script_sha256':sha(__file__),'proof_sha256':sha(ROOT/'notes/research_mixed_cyclic_critical_localization.md')}
 args.output.parent.mkdir(parents=True,exist_ok=True)
 if args.output.suffix=='.gz':
  with gzip.open(args.output,'wt')as f:json.dump(out,f,separators=(',',':'));f.write('\n')
 else:args.output.write_text(json.dumps(out,separators=(',',':'))+'\n')
 print('PASS extraction',sum(s['cells']for s in summaries),'cells',flush=True)
if __name__=='__main__':main()
