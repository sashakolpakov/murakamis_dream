#!/usr/bin/env python3
"""Same-sign type-four reset cone from complete original saved source witnesses."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,importlib.util,itertools,json,time
import sympy as sy
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_same_sign_height_reset.md'
HELPER=ROOT/'experiments/certify_mixed_oriented_height_reset.py'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
h0=sha(HELPER)
sp=importlib.util.spec_from_file_location('same_sign_reset_arithmetic',HELPER);old=importlib.util.module_from_spec(sp);sp.loader.exec_module(old)
assert h0==sha(HELPER)
core=old.core
DEPS=['notes/research_mixed_oriented_height_reset.md','experiments/certify_mixed_oriented_height_reset.py','repro/results/research-mixed-oriented-height-reset.json','notes/research_mixed_full_height_reset.md','experiments/certify_mixed_full_height_reset.py','repro/results/research-mixed-full-height-reset.json','experiments/certify_mixed_real_small_support.py']
def bindings(path,proof,script):
 r=json.loads(path.read_text());assert r['status']=='passed'and r['proof_sha256']==sha(proof)and r['script_sha256']==sha(script)
 for key in('dependencies','dependencies_sha256'):
  for p,h in r.get(key,{}).items():assert sha(ROOT/p)==h,p
 return r

def test(case,address,witness):
 eta,eps,fa,fb=case;assert eta==eps==1
 al,ah,bl,bh=core.box(address)
 a,b=old.old.edge(old.old.U[1],fa,al,ah),old.old.edge(old.old.U[1],fb,bl,bh)
 a0,b0=old.old.edge(old.old.U[1],fa,(al+ah)/2,(al+ah)/2),old.old.edge(old.old.U[1],fb,(bl+bh)/2,(bl+bh)/2)
 packet=core.root_box(a,b,a0,b0,1,witness)
 if packet is None:return None
 s,_,wit=packet;_,_,H=core.phase(s,a,b,1,1)
 A,C,D=-H[0][0].real,-H[0][1].real,-H[1][1].real;E,Ff,G=H[0][0].imag,H[0][1].imag,H[1][1].imag;det=A*D-C*C
 if not(A>0 and D>0 and det>0):return None
 k0=A+(D*E*E-2*C*E*Ff+A*Ff*Ff)/det
 k1=D+(D*Ff*Ff-2*C*Ff*G+A*G*G)/det
 cross=C+(D*E*Ff-C*(E*G+Ff*Ff)+A*Ff*G)/det
 if not(k0<11 and k1<core.ar(F(151,10))and cross<0):return None
 return wit,cross.upper()

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--precision',type=int,default=256);ap.add_argument('--input',type=Path);ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-same-sign-height-reset.json');args=ap.parse_args();assert args.precision>=160
 ctx.prec=args.precision;core.pi,core.ii=arb.pi(),acb(0,1)
 deps={p:sha(ROOT/p)for p in DEPS};ph,sh=sha(PROOF),sha(__file__);assert deps[DEPS[1]]==h0
 inherited=bindings(ROOT/DEPS[2],ROOT/DEPS[0],ROOT/DEPS[1]);bindings(ROOT/DEPS[5],ROOT/DEPS[3],ROOT/DEPS[4])
 aa,cc,dd,ee,ff,gg=sy.symbols('a c d e f g',real=True);Am=sy.Matrix([[aa,cc],[cc,dd]]);Bm=sy.Matrix([[ee,ff],[ff,gg]]);K=Am+Bm*Am.inv()*Bm
 assert sy.cancel(K[0,1]-(cc+(dd*ee*ff-cc*(ee*gg+ff*ff)+aa*ff*gg)/(aa*dd-cc*cc)))==0
 path=args.input or ROOT/DEPS[2];ih=sha(path);saved=json.loads(path.read_text())
 if args.input:
  assert saved['status']=='passed'and saved['proof_sha256']==ph and saved['script_sha256']==sh and saved['dependencies_sha256']==deps
 cases=[r for r in saved['cases']if r['case'][:2]==[1,1]]
 assert len(cases)==16 and {tuple(r['case'])for r in cases}==set(itertools.product((1,),(1,),range(4),range(4)))
 rows=[];vis=0;refined=0;maximum=None;start=time.time()
 for row in cases:
  pending=[(v['address'],v['witness'])for v in row['leaves']];accepted=[]
  while pending:
   address,witness=pending.pop();vis+=1;ret=test(row['case'],address,witness)
   if ret is None:
    assert not args.input,('saved failure',row['case'],address)
    assert len(address)<30,(row['case'],address)
    pending.extend([(address+'0',None),(address+'1',None)]);refined+=1;continue
   wit,upper=ret;maximum=upper if maximum is None else max(maximum,upper)
   accepted.append({'address':address,'witness':wit})
  codes=sorted(v['address']for v in accepted);assert len(codes)==len(set(codes))and all(not b.startswith(a)for a,b in zip(codes,codes[1:]));assert sum((F(1,2**len(a))for a in codes),F(0))==1
  rows.append({'case':row['case'],'leaves':accepted});print('progress',row['case'],len(accepted),vis,refined,'K01 upper',maximum,flush=True)
 assert ph==sha(PROOF)and sh==sha(__file__)and deps=={p:sha(ROOT/p)for p in DEPS}and ih==sha(path)
 out=dict(status='passed',precision_bits=args.precision,domains=16,cells=sum(len(r['leaves'])for r in rows),visits=vis,refinements=refined,exact_identities=1,maximum_boundary_cross_entry=str(maximum),cases=rows,proof_sha256=ph,script_sha256=sh,dependencies_sha256=deps,input_path=str(path),input_sha256=ih,elapsed_seconds=time.time()-start,scope='Same-sign two-height cone bound for original type-four/type-four phase and existing finite-block upper rates. No global diagonal matrix domination or right-region contribution theorem.')
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n');print('PASS',out['domains'],out['cells'],vis,refined,flush=True)
if __name__=='__main__':main()
