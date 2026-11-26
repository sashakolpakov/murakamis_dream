#!/usr/bin/env python3
"""Oriented full-real-readjustment reset bounds on the original source domain."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,importlib.util,itertools,json,time
import sympy as sy
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_oriented_height_reset.md'
HELPER=ROOT/'experiments/certify_mixed_full_height_reset.py'
sp=importlib.util.spec_from_file_location('oriented_reset_arithmetic',HELPER);old=importlib.util.module_from_spec(sp);sp.loader.exec_module(old)
core=old.core
DEPS=['notes/research_mixed_full_height_reset.md','experiments/certify_mixed_full_height_reset.py','repro/results/research-mixed-full-height-reset.json','experiments/certify_mixed_real_small_support.py','notes/research_mixed_unselected_right_taper_products.md','experiments/certify_mixed_right_square_conditional_packets.py','repro/results/research-mixed-right-square-conditional-packets.json','notes/research_mixed_fourier_weight_continuation.md']
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def check_record(r):
 assert r['status']=='passed'
 for key in('dependencies','dependencies_sha256'):
  for p,h in r.get(key,{}).items():assert sha(ROOT/p)==h,p

def test(case,address,witness=None):
 eta,eps,fa,fb=case;al,ah,bl,bh=core.box(address)
 a,b=old.edge(old.U[eta],fa,al,ah),old.edge(old.U[eps],fb,bl,bh)
 a0,b0=old.edge(old.U[eta],fa,(al+ah)/2,(al+ah)/2),old.edge(old.U[eps],fb,(bl+bh)/2,(bl+bh)/2)
 packet=core.root_box(a,b,a0,b0,eps,witness)
 if packet is None:return None
 s,_,wit=packet;_,_,h=core.phase(s,a,b,eta,eps)
 A,C,D=-h[0][0].real,-h[0][1].real,-h[1][1].real;E,Ff,G=h[0][0].imag,h[0][1].imag,h[1][1].imag;det=A*D-C*C
 if not(A>0 and D>0 and det>0):return None
 k0=A+(D*E*E-2*C*E*Ff+A*Ff*Ff)/det
 k1=D+(D*Ff*Ff-2*C*Ff*G+A*G*G)/det
 if not(k0<11 and k1<core.ar(F(151,10))):return None
 return wit,k0.upper(),k1.upper()

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--precision',type=int,default=256);ap.add_argument('--input',type=Path);ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-oriented-height-reset.json');args=ap.parse_args();assert args.precision>=160
 ctx.prec=args.precision;core.pi,core.ii=arb.pi(),acb(0,1)
 hashes={p:sha(ROOT/p)for p in DEPS};ph,sh=sha(PROOF),sha(__file__)
 inherited=json.loads((ROOT/DEPS[2]).read_text());check_record(inherited);assert inherited['proof_sha256']==hashes[DEPS[0]]and inherited['script_sha256']==hashes[DEPS[1]]
 source=json.loads((ROOT/DEPS[6]).read_text());check_record(source);assert source['script_sha256']==hashes[DEPS[5]]
 assert source.get('proof_sha256',source.get('dependencies_sha256',{}).get(DEPS[4]))==hashes[DEPS[4]]
 path=args.input or ROOT/DEPS[2];ih=sha(path);saved=json.loads(path.read_text());check_record(saved)
 if args.input:assert saved['proof_sha256']==ph and saved['script_sha256']==sh
 aa,cc,dd,ee,ff,gg=sy.symbols('aa cc dd ee ff gg');Am=sy.Matrix([[aa,cc],[cc,dd]]);Bm=sy.Matrix([[ee,ff],[ff,gg]]);K=Am+Bm*Am.inv()*Bm
 assert sy.cancel(K[0,0]-(aa+(dd*ee**2-2*cc*ee*ff+aa*ff**2)/(aa*dd-cc**2)))==0
 assert sy.cancel(K[1,1]-(dd+(dd*ff**2-2*cc*ff*gg+aa*gg**2)/(aa*dd-cc**2)))==0
 start=time.time();rows=[];vis=0;refinements=0;maxima=[arb(0),arb(0)]
 for case0 in saved['cases']:
  case=case0['case'];pending=[(r['address'],r['witness'])for r in case0['leaves']];leaves=[]
  while pending:
   address,witness=pending.pop();vis+=1;r=test(case,address,witness)
   if r is None:
    assert len(address)<28,(case,address)
    pending.extend([(address+'0',None),(address+'1',None)]);refinements+=1;continue
   wit,k0,k1=r;maxima=[max(maxima[0],k0),max(maxima[1],k1)];leaves.append(dict(address=address,witness=wit))
  codes=sorted(x['address']for x in leaves);assert len(codes)==len(set(codes))and all(not b.startswith(a)for a,b in zip(codes,codes[1:]));assert sum((F(1,2**len(a))for a in codes),F(0))==1
  rows.append(dict(case=case,leaves=leaves));print('progress',case,len(leaves),vis,refinements,flush=True)
 expected=set(itertools.product((0,1),(0,1),range(4),range(4)));assert len(rows)==64 and {tuple(r['case'])for r in rows}==expected
 assert hashes=={p:sha(ROOT/p)for p in DEPS}and ph==sha(PROOF)and sh==sha(__file__)and ih==sha(path)
 result=dict(status='passed',precision_bits=args.precision,domains=64,cells=sum(len(r['leaves'])for r in rows),visits=vis,refinements=refinements,diagonal_upper_bounds=['11','151/10'],maximum_outward_diagonals=list(map(str,maxima)),integrated_one_height_costs=['11/2','151/20'],exact_identities=2,cases=rows,input_path=str(path),input_sha256=ih,proof_sha256=ph,script_sha256=sh,dependencies=hashes,elapsed_seconds=time.time()-start,scope='One reset height with arbitrary real readjustment of both coordinates on the original U3/U4 source products. No correlated right-star gap or all-cycle theorem.')
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n');print('PASS',result['cells'],vis,refinements,time.time()-start,flush=True)
if __name__=='__main__':main()
