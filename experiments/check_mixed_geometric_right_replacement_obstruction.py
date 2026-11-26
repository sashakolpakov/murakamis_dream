#!/usr/bin/env python3
"""Fixed original-root/raw-row obstruction; no search or parameter cover."""
import argparse,hashlib,importlib.util,json
from fractions import Fraction as F
from pathlib import Path
import sympy as sp
from flint import arb,acb,ctx

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_geometric_right_replacement_obstruction.md'
CORE=ROOT/'experiments/certify_mixed_real_small_support.py'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ar(x):
 x=F(x);return arb(x.numerator)/x.denominator

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--precision',type=int,default=256)
 ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-geometric-right-replacement-obstruction.json')
 args=ap.parse_args();assert args.precision>=160;ctx.prec=args.precision
 ph,sh=sha(PROOF),sha(__file__);deps={};records={}
 def bind(p,h=None):
  value=sha(ROOT/p);assert h is None or value==h,(p,h,value)
  if p in deps:assert deps[p]==value
  deps[p]=value;return value
 def inherited(stem,script,proof):
  rp='repro/results/'+stem+'.json';bind(rp);r=json.loads((ROOT/rp).read_text());assert r['status']=='passed'
  bind('experiments/'+script,r['script_sha256']);bind('notes/'+proof)
  if 'proof_sha256'in r:assert r['proof_sha256']==deps['notes/'+proof]
  for key in('dependencies','dependencies_sha256'):
   for p,h in r.get(key,{}).items():bind(p,h)
  records[stem]=r;return r
 src=inherited('research-three-four-source-interface','check_three_four_source_interface.py','research_three_four_source_interface.md')
 inherited('research-mixed-contracted-phase','check_mixed_contracted_phase.py','research_mixed_contracted_phase.md')
 inherited('research-mixed-cyclic-block-localization','certify_mixed_cyclic_block_localization.py','research_mixed_cyclic_critical_localization.md')
 inherited('research-mixed-closed-cotangent-roots','check_mixed_closed_cotangent_roots.py','research_mixed_closed_cotangent_roots.md')
 inherited('research-mixed-half-endpoint-conditional-packet','check_mixed_half_endpoint_conditional_packet.py','research_mixed_half_endpoint_conditional_packet.md')
 inherited('research-mixed-fourier-weight-continuation','check_mixed_fourier_weight_continuation.py','research_mixed_fourier_weight_continuation.md')
 inherited('research-mixed-split-cutoff-hybrid-contour','check_mixed_split_cutoff_hybrid_contour.py','research_mixed_split_cutoff_hybrid_contour.md')
 bind(str(CORE.relative_to(ROOT)))
 spec=importlib.util.spec_from_file_location('fixed_original_roots',CORE);core=importlib.util.module_from_spec(spec);spec.loader.exec_module(core)
 core.pi,core.ii=arb.pi(),acb(0,1);pi,ii=core.pi,core.ii
 checks=[];margins={}
 def exact(name,v):assert sp.cancel(v)==0,name;checks.append(name)
 def positive(name,v):assert v>0,(name,str(v));margins[name]=str(v.lower())
 a=sp.symbols('a');p=4*a**4-6*a**3+4*a**2-2*a+1;K=1/(1+2*a-4*a*a);U=1-2*a;V=(1-K)/(2*K)
 for name,z in [('three original exponential',(1-U*U)*(1-U*V)-V*(1-U)**2),('four original exponential',(1-V*V)*(1-U*V)-U*(1-V)**3)]:
  num=sp.fraction(sp.factor(z))[0];exact(name,sp.rem(num,p,a))
 cert=src['root_certificate'];cc=acb(ar(cert['center'][0]),ar(cert['center'][1]));rad=ar(cert['complex_disk_radius'])
 box=cc+acb(arb(0,rad),arb(0,rad));poly=lambda z:(((4*z-6)*z+4)*z-2)*z+1;dp=lambda z:((16*z-18)*z+8)*z-2
 Y=1/dp(cc);rho=abs(1-Y*dp(box));res=abs(Y*poly(cc))
 positive('quartic contraction',1-rho);positive('quartic strict disk selfmap',rad-res-rho*rad)
 kr=1/(1+2*box-4*box*box);uu=1-2*box;vv=(1-kr)/(2*kr)
 r3=-uu.log()/(2*pi*ii);r4=-vv.log()/(2*pi*ii)
 original=[]
 for label,z,other,e in [('three',r3,r4,0),('four',r4,r3,1)]:
  f=core.gp(2*z)+core.gp(z+other)-(2+e)*core.gp(z)+2*pi*ii*other
  assert f.contains(0),(label,str(f));positive(label+' zero logarithmic lift',pi-abs(f.imag))
  for name,margin in [('real lower',z.real-ar('1/4')),('real upper',ar('9/20')-z.real),('height chamber',ar('3/25')-abs(z.imag))]:positive(label+' '+name,margin)
  cot=(pi*z).cot();positive(label+' selected cotangent real',cot.real);positive(label+' selected cotangent imaginary',1-abs(cot.imag))
  for k,t in enumerate((z,2*z,z+other)):
   positive(label+f' strip{k} lower',t.real);positive(label+f' strip{k} upper',1-t.real)
  original.append(str(f))
 c=r3.real;positive('geometric center lower',c-ar('.3535'));positive('geometric center upper',ar('.3537')-c)
 targetpairs=[(acb(ar('1/10')),acb(c),1,0),(acb(c),acb(ar('1/2')),0,1)]
 roots=[];values=[]
 for j,(aa,bb,eta,e)in enumerate(targetpairs):
  root=core.point_root(aa,bb,e);assert root is not None,('original target root',j)
  ss,center=root;value,_,_=core.phase(ss,aa,bb,eta,e);values.append(value.real)
  roots.append(dict(center=center,radius='1e-12',root_box=str(ss),original_equation=str(core.equation(ss,aa,bb,e))))
  assert core.equation(ss,aa,bb,e).contains(0)
 J=lambda x:core.g(acb(ar(x))).real
 rawleft=J('19/50')+J('39/50')-ar('3/2')*J('1/10')-2*J('7/25')
 rawright=2*J('73/100')-3*J('23/100')
 positive('physical left factorial branch',-J('1/10'));assert J('1/2').contains(0)
 excess=rawleft+rawright-sum(values,arb(0));positive('raw envelope exceeds geometric replacement by3/50',excess-ar('3/50'))
 exact('left physical row at levels100k',100*sp.Rational(7,25)-28)
 exact('right physical row at levels100k',100*sp.Rational(23,100)-23)
 assert F(1,2)+F(7,25)<1 and F(1,2)+F(23,100)<1
 checks.append('both physical rows precede every cyclotomic zero')
 assert ph==sha(PROOF)and sh==sha(__file__);assert all(sha(ROOT/p)==h for p,h in deps.items())
 out=dict(status='passed',precision_bits=args.precision,exact_checks=len(checks),checks=checks,strict_comparisons=len(margins),margins=margins,
   quartic_center=cert['center'],quartic_radius=cert['complex_disk_radius'],reference=[str(r3),str(r4)],original_zero_lifts=original,
   target_roots=roots,raw_row_rates=[str(rawleft),str(rawright)],coherent_replacement_rates=list(map(str,values)),excess=str(excess),certified_excess='3/50',
   original_target_cycle=['1/2','1/2','1/2','1/10'],type_word=[3,4,3,4],replaced_coordinate=0,
   source_levels='N divisible by100; physical outer indicesN/10,N/2 and rows28N/100,23N/100 remain nonzero',
   proof_sha256=ph,script_sha256=sh,dependencies_sha256=deps,
   scope='Strict obstruction to the two-incident absolute-row-envelope comparison with geometric real-center replacement. No failure of the signed conditional sum, whole cyclic source, or volume theorem.')
 args.output.write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(checks),'exact;',len(margins),'outward; excess',str(excess),flush=True)
if __name__=='__main__':main()
