#!/usr/bin/env python3
"""Outward directed Schur cones for an isolated unselected left transition.

Only rational saved witnesses and interval original-log Newton tests enter
acceptance. This certificate is a phase comparison, not a new finite packet.
"""
import argparse, hashlib, importlib.util, itertools, json, math, time
from fractions import Fraction as F
from pathlib import Path
import sympy as sy
from flint import acb, arb, ctx
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_isolated_transition_phase.md'
HELPER=ROOT/'experiments/certify_mixed_real_small_support.py'
HELPER_SHA=hashlib.sha256(HELPER.read_bytes()).hexdigest()
sp=importlib.util.spec_from_file_location('transition_phase_arithmetic',HELPER)
core=importlib.util.module_from_spec(sp);sp.loader.exec_module(core)
assert HELPER_SHA==hashlib.sha256(HELPER.read_bytes()).hexdigest()
REF={0:[F('-.03'),F('.02')],1:[F('-.057'),F('-.02')]}
RMIN={0:F('.30'),1:F('.27')}
POLY={0:[(F('.10'),F(0)),(F('.22'),F('-.03')),(F('.39'),F('-.03')),(F('.39'),F('.02')),(F('.22'),F('.02'))],
      1:[(F('.10'),F(0)),(F('.22'),F('-.057')),(F('.33'),F('-.057')),(F('.33'),F('-.02'))]}
PLAT={0:[(F('.22'),F('-.03')),(F('.45'),F('-.03')),(F('.45'),F('.02')),(F('.22'),F('.02'))],
      1:[(F('.22'),F('-.057')),(F('.45'),F('-.057')),(F('.45'),F(0)),(F('.22'),F(0))]}
DEPS=['experiments/certify_mixed_real_small_support.py',
'notes/research_mixed_closed_cotangent_roots.md','experiments/check_mixed_closed_cotangent_roots.py','repro/results/research-mixed-closed-cotangent-roots.json',
'notes/research_mixed_oriented_height_reset.md','experiments/certify_mixed_oriented_height_reset.py','repro/results/research-mixed-oriented-height-reset.json']
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def clip(poly,cut,lower):
 out=[]
 for a,b in zip(poly,poly[1:]+poly[:1]):
  ia=(a[0]>=cut)if lower else(a[0]<=cut);ib=(b[0]>=cut)if lower else(b[0]<=cut)
  if ia:out.append(a)
  if ia!=ib:
   t=(cut-a[0])/(b[0]-a[0]);out.append((cut,a[1]+t*(b[1]-a[1])))
 ret=[]
 for z in out:
  if not ret or z!=ret[-1]:ret.append(z)
 if len(ret)>1 and ret[0]==ret[-1]:ret.pop()
 return ret

def specs():
 out=[]
 for eta,eps,side in itertools.product((0,1),repeat=3):
  low=(eta,eps)[side];poly=POLY[low]
  cuts=[F('.10'),F('.27')]+[F('.27')+F(j,200)for j in range(1,13)] if(eta,eps,side)==(1,1,1) else [poly[0][0],max(v[0]for v in poly)]
  for j,(lo,hi)in enumerate(zip(cuts,cuts[1:])):
   pp=clip(clip(poly,lo,True),hi,False);L=1/(max(RMIN[low],lo)-F('.1'))
   for fa,fb in itertools.product(range(len(pp)),range(4)):
    out.append((eta,eps,side,j,fa,fb,pp,L))
 return out

def edge(poly,j,lo,hi):
 a,b=poly[j],poly[(j+1)%len(poly)];t=core.ar(lo).union(core.ar(hi))
 return acb(core.ar(a[0]),core.ar(a[1]))+acb(core.ar(b[0]-a[0]),core.ar(b[1]-a[1]))*t

ar=core.ar; proposal=core.proposal; second=core.second; equation=core.equation; gpp=core.gpp; point_root=core.point_root

def root_box(a, b, a0, b0, eps, witness=None):
    center = proposal(a0, b0, eps) if witness is None else witness["center"]
    if center is None:
        return None
    z0 = acb(ar(center[0]), ar(center[1]))
    H0 = second(z0, a0, b0, eps)
    Y = 1/H0
    E = [gpp(z0+a0)+2*pi*ii, gpp(z0+b0)]
    dp = [a-a0, b-b0]
    if witness is None:
        dd = [[str(float((-Y*e).real.mid())), str(float((-Y*e).imag.mid()))] for e in E]
    else:
        dd = witness["derivatives"]
    deriv = [acb(ar(v[0]), ar(v[1])) for v in dd]
    dz = sum((deriv[j]*dp[j] for j in (0, 1)), acb(0))
    lin = equation(z0, a0, b0, eps)+sum(((H0*deriv[j]+E[j])*dp[j] for j in (0, 1)), acb(0))

    def rem(base, delta):
        w = base+acb(arb(0, abs(delta.real).upper()), arb(0, abs(delta.imag).upper()))
        if not 0 < w.real < 1:
            return arb.pos_inf()
        return pi*pi*abs(1/(pi*w).sin()**2)*abs(delta)**2/2

    err = abs(Y)*(abs(lin)+rem(z0+a0, dz+dp[0])+rem(z0+b0, dz+dp[1])+(2+eps)*rem(z0, dz))
    if not err.is_finite():
        return None
    radius = F(witness["radius"]) if witness is not None else F(max(1, math.ceil(float(err.upper())*1.5*2**42)), 2**42)
    if radius > F(1, 20):
        return None
    delta = dz+acb(arb(0, ar(radius)), arb(0, ar(radius)))
    z = z0+delta
    S=(pi*z).cot()
    if not (0 < z.real < ar(F(1,2)) and S.real > 0 and abs(S.imag) < 1):
        return None
    if not all(0 < w.real < 1 for w in (z, z+a, z+b)):
        return None

    def dc(base, move):
        return -pi*(pi*move).sin()/((pi*base).sin()*(pi*(base+move)).sin())

    defect = 1-Y*H0-Y*(dc(z0+a0, delta+dp[0])+dc(z0+b0, delta+dp[1])-(2+eps)*dc(z0, delta))
    if not err+abs(defect)*ar(radius) < ar(radius):
        return None
    pr = point_root(a0, b0, eps, center)
    if pr is None:
        return None
    return z, pr[0], {"center": center, "derivatives": dd, "radius": str(radius)}


def test(spec,address,witness=None):
 eta,eps,side,j,fa,fb,poly,L=spec;lo,hi,ul,uh=core.box(address)
 zlo=edge(poly,fa,lo,hi);zhi=edge(PLAT[(eta,eps)[1-side]],fb,ul,uh)
 c0=edge(poly,fa,(lo+hi)/2,(lo+hi)/2);c1=edge(PLAT[(eta,eps)[1-side]],fb,(ul+uh)/2,(ul+uh)/2)
 a,b=(zlo,zhi)if side==0 else(zhi,zlo);a0,b0=(c0,c1)if side==0 else(c1,c0)
 packet=root_box(a,b,a0,b0,eps,witness)
 if packet is None:return None
 s,_,wit=packet;sa=gpp(s+a)+2*pi*ii;sb=gpp(s+b);ss=second(s,a,b,eps)
 H=[[gpp(s+a)-(1+ar(F(eta,2)))*gpp(a)-sa*sa/ss,-sa*sb/ss],[-sa*sb/ss,gpp(s+b)-(1+ar(F(eps,2)))*gpp(b)-sb*sb/ss]]
 oth=1-side;A=-H[oth][oth].real
 if not A>0:return None
 charge=F(11)if side==0 else F(151,10)
 dirs=[(F(0),F(0))]+[(L*x,L*y)for x,y in itertools.product(REF[eta],REF[eps])]
 margins=[]
 for alpha,beta in dirs:
  w=[ii*ar(alpha),ii*ar(beta)];w[side]+=1
  value=sum((w[k]*H[k][l]*w[l]for k,l in itertools.product((0,1),repeat=2)),acb(0)).real
  lin=sum((H[oth][k]*w[k]for k in(0,1)),acb(0)).real
  excess=-value-lin**2/A-ar(charge)*ar((beta if side==0 else alpha)**2)
  if not excess>ar('1/8'):return None
  margins.append(excess.lower())
 return wit,min(margins)

def check_record(path,proof,script):
 r=json.loads(path.read_text());assert r['status']=='passed';assert r['proof_sha256']==sha(proof)and r['script_sha256']==sha(script)
 for key in('dependencies','dependencies_sha256'):
  for p,h in r.get(key,{}).items():assert sha(ROOT/p)==h,p

def main():
 global pi,ii
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--precision',type=int,default=256);ap.add_argument('--input',type=Path);ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-isolated-transition-phase.json');ap.add_argument('--max-visits',type=int,default=1000000);args=ap.parse_args();assert args.precision>=160
 ctx.prec=args.precision;pi,ii=arb.pi(),acb(0,1);core.pi,core.ii=pi,ii
 deps={p:sha(ROOT/p)for p in DEPS};ph,sh=sha(PROOF),sha(__file__)
 assert deps['experiments/certify_mixed_real_small_support.py']==HELPER_SHA
 for stem,prefix in [('mixed_closed_cotangent_roots','check'),('mixed_oriented_height_reset','certify')]:
  check_record(ROOT/f'repro/results/research-{stem.replace("_","-")}.json',ROOT/f'notes/research_{stem}.md',ROOT/f'experiments/{prefix}_{stem}.py')
 # The polygon lies in the original open cotangent cone. Its height is
 # bounded by .057*rho; the quadratic comparison is exact on the left.
 left_factor=F(121,120)
 x,t,r,u,A,b,c=sy.symbols('x t r u A b c',real=True)
 assert sy.expand(sy.Rational(125,6)*x*x-sy.Rational(25,3)*(x-sy.Rational(1,10))-sy.Rational(125,6)*(x-sy.Rational(1,5))**2)==0
 assert sy.expand((sy.Rational(22,100)-t)*(r-sy.Rational(1,10))-sy.Rational(12,100)*(r-t)-(t-sy.Rational(1,10))*(sy.Rational(22,100)-r))==0
 assert sy.expand(-A*u*u+2*b*u+c-(-A*(u-b/A)**2+c+b*b/A))==0
 cotbound=ar(left_factor)*(2*pi*ar('.057')).sinh()/(2*(pi*ar('.22')).sin()**2)
 assert cotbound<ar('1/2')
 domains=specs();saved=None;ih=None
 if args.input:
  ih=sha(args.input);saved=json.loads(args.input.read_text());assert saved['status']=='passed'and saved['proof_sha256']==ph and saved['script_sha256']==sh
  assert saved['dependencies_sha256']==deps
  assert len(saved['cases'])==len(domains)
 start=time.time();rows=[];vis=0;refinements=0;minimum=None
 for number,spec in enumerate(domains):
  case=list(spec[:6]);leaves=[]
  if saved:
   row=saved['cases'][number];assert row['case']==case
   assert row['polygon']==[[str(x),str(y)]for x,y in spec[6]]and row['slope_bound']==str(spec[7])
   todo=[(v['address'],v['witness'])for v in row['leaves']]
  else:todo=[('',None)]
  while todo:
   ad,wit=todo.pop();vis+=1;assert vis<=args.max_visits,(number,ad)
   value=test(spec,ad,wit)
   if value is None:
    assert not saved,('saved witness failed',case,ad)
    assert len(ad)<30,('cell depth',case,ad)
    todo.extend([(ad+'0',None),(ad+'1',None)]);refinements+=1;continue
   wit,m=value;minimum=m if minimum is None else min(minimum,m)
   leaves.append({'address':ad,'witness':wit})
  codes=sorted(v['address']for v in leaves);assert len(codes)==len(set(codes))and all(not b.startswith(a)for a,b in zip(codes,codes[1:]));assert sum((F(1,2**len(a))for a in codes),F(0))==1
  rows.append({'case':case,'polygon':[[str(x),str(y)]for x,y in spec[6]],'slope_bound':str(spec[7]),'leaves':leaves})
  print('progress',number+1,len(domains),case,len(leaves),vis,'minimum',minimum,flush=True)
 assert ph==sha(PROOF)and sh==sha(__file__)and deps=={p:sha(ROOT/p)for p in DEPS}
 if args.input:assert ih==sha(args.input)
 out=dict(status='passed',exact_identities=3,precision_bits=args.precision,domains=len(domains),cells=sum(len(r['leaves'])for r in rows),visits=vis,refinements=refinements,minimum_directed_schur=str(minimum),cotangent_imaginary_upper_bound=str(cotbound.upper()),cases=rows,proof_sha256=ph,script_sha256=sh,dependencies_sha256=deps,elapsed_seconds=time.time()-start,scope='Isolated unselected transition phase plus oriented neighboring reset debit. No new finite-source bound, extra suppression factors, selections or arbitrary transition clusters.')
 if args.input:out.update(input_path=str(args.input),input_sha256=ih)
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n');print('PASS',out['domains'],out['cells'],vis,flush=True)
if __name__=='__main__':main()
