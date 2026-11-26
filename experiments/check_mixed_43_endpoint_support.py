#!/usr/bin/env python3
"""Original (4,3) tapered-endpoint supporting-plane certificate.

Local source chords are used only on intersecting certified slope intervals.
Reference boundaries are covered exactly; all source and height boundaries remain.
"""
import argparse,hashlib,json,time
from fractions import Fraction as Q
from pathlib import Path
from flint import arb,acb,ctx
ctx.prec=160;pi=arb.pi();ii=acb(0,1)
ar=lambda v:arb(Q(v).numerator)/Q(v).denominator
rects=[['27/100','33/100','-57/1000','-1/50'],['3/10','39/100','-3/100','1/50']]
rows={}
def edge(k,f,lo,hi):
 xl,xh,yl,yh=map(Q,rects[k]);v=ar(lo).union(ar(hi))
 return acb(ar(xl)+(ar(xh)-ar(xl))*v,ar(yl if f==0 else yh))if f in[0,2]else acb(ar(xh if f==1 else xl),ar(yl)+(ar(yh)-ar(yl))*v)
def direction(k,f):
 xl,xh,yl,yh=map(Q,rects[k]);return acb(ar(xh-xl))if f in[0,2]else ii*ar(yh-yl)
def box(ad):
 b=[Q(0),Q(1),Q(0),Q(1)]
 for j,bit in enumerate(ad):
  k=2*(j%2);mid=(b[k]+b[k+1])/2;b[k+1-int(bit)]=mid
 return b
def root(a,b):
 A=(-2*pi*ii*a).exp();B=(-2*pi*ii*b).exp();D=((A-B)**2-4*A*(B-1)*(1-A)).sqrt()
 for sign in[-1,1]:
  U=(B-A+sign*D)/(2*A*(B-1));st=ii*U.log()/(2*pi)
  if st.real>ar('1/5')and st.real<ar('11/25')and abs(st.imag)<ar('3/20'):
   residual=gp(st+a)+gp(st+b)-2*gp(st)+2*pi*ii*a
   if abs(residual)<1:return st
 return None
def gp(z):return(1-(-2*pi*ii*z).exp()).log()
def gpp(z):
 U=(-2*pi*ii*z).exp();return 2*pi*ii*U/(1-U)
def g(z):return ((-2*pi*ii*z).exp().polylog(2)-pi*pi/6)/(2*pi*ii)
def phase(a,b,full=False):
 s=root(a,b)
 if s is None:return None
 da=gp(s+a)+2*pi*ii*s-ar('3/2')*gp(a);db=gp(s+b)-gp(b)
 if not full:return da
 f=g(s+a)+g(s+b)-2*g(s)+2*pi*ii*a*s-ar('3/2')*g(a)-g(b)
 sa=gpp(s+a)+2*pi*ii;sb=gpp(s+b);ss=gpp(s+a)+gpp(s+b)-2*gpp(s)
 aa=gpp(s+a)-ar('3/2')*gpp(a)-sa*sa/ss;ab=-sa*sb/ss;bb=gpp(s+b)-gpp(b)-sb*sb/ss
 return f,da,db,aa,ab,bb
def test(ad,fa,fb):
 al,ah,bl,bh=box(ad);a=edge(0,fa,al,ah);b=edge(1,fb,bl,bh);a0=edge(0,fa,(al+ah)/2,(al+ah)/2);b0=edge(1,fb,(bl+bh)/2,(bl+bh)/2)
 vals=phase(a,b,True);mid=phase(a0,b0,True)
 if vals is None or mid is None:return False
 f,da,db,aa,ab,bb=vals;f0,da0,db0,*_=mid;k=da.real
 if not(k>ar('-2/5')and k<ar('3/10')):return False
 ra=ar((ah-al)/2);rb=ar((bh-bl)/2);va=direction(0,fa);vb=direction(1,fb)
 worst=None
 for h,rr in rows.items():
  for e in[0,1]:
   C0=f0-a0*da0+(e-b0)*db0+ii*ar(h)*da0
   for r1,r2 in zip(rr,rr[1:]):
    kl=Q(r1['kappa']);kh=Q(r2['kappa'])
    if k<ar(kl)or k>ar(kh):continue
    slope=(Q(r2['upper'])-Q(r1['upper']))/(kh-kl);intercept=Q(r1['upper'])-slope*kl
    d1=(ar(slope)+a-ii*ar(h))*aa-(e-b)*ab
    d2=(ar(slope)+a-ii*ar(h))*ab-(e-b)*bb
    upper=(ar(slope)*da0+ar(intercept)-C0).real+abs((d1*va).real)*ra+abs((d2*vb).real)*rb
    if not upper<ar('-1/1000'):return False
    worst=upper.upper()if worst is None else max(worst,upper.upper())
 # Vertical seam source bound -2pi h is exact for h<0.
 for h in[Q(-57,1000),Q(0)]:
  for x in[0,1]:
   for e in[0,1]:
    C0=f0-a0*da0+(e-b0)*db0+ii*ar(h)*da0
    d1=(a-x-ii*ar(h))*aa-(e-b)*ab
    d2=(a-x-ii*ar(h))*ab-(e-b)*bb
    upper=(-2*pi*ar(h)-x*da0-C0).real+abs((d1*va).real)*ra+abs((d2*vb).real)*rb
    if not upper<ar('-1/1000'):return False
    worst=upper.upper()if worst is None else max(worst,upper.upper())
 # Raw selected positive seam source has rate less than1/20 on [0,.014].
 for h in[Q(0),Q(7,500)]:
  for x in[0,1]:
   for e in[0,1]:
    C0=f0-a0*da0+(e-b0)*db0+ii*ar(h)*da0
    d1=(a-x-ii*ar(h))*aa-(e-b)*ab
    d2=(a-x-ii*ar(h))*ab-(e-b)*bb
    upper=(ar('1/20')-x*da0-C0).real+abs((d1*va).real)*ra+abs((d2*vb).real)*rb
    if not upper<ar('-1/1000'):return False
    worst=upper.upper()if worst is None else max(worst,upper.upper())
 assert worst is not None
 return worst

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_43_endpoint_support.md'
INPUT=ROOT/'repro/results/research-mixed-endpoint-support-grid.json'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 global rows,pi
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--precision',type=int,default=192)
 ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-43-endpoint-support.json')
 args=ap.parse_args();ctx.prec=args.precision;pi=arb.pi()
 assert 1-(-7*pi/250).exp()<ar('1/10')
 source_bytes=INPUT.read_bytes();data=json.loads(source_bytes)
 assert data['status']=='passed'and data['source_grid_count']==60
 assert data['script_sha256']==sha(ROOT/'experiments/check_mixed_endpoint_support_grid.py')
 assert data['proof_sha256']==sha(ROOT/'notes/research_mixed_endpoint_support_grid.md')
 deps=dict(data['dependencies'])
 deps['experiments/check_mixed_endpoint_support_grid.py']=data['script_sha256']
 deps['notes/research_mixed_endpoint_support_grid.md']=data['proof_sha256']
 for f,h in deps.items():assert sha(ROOT/f)==h
 initial=dict(deps);ph=sha(PROOF);sh=sha(__file__)
 rows={h:sorted([r for r in data['source_grid']if Q(r['height'])==h],key=lambda r:Q(r['kappa']))for h in[Q(-57,1000),Q(-1,50),Q(0),Q(7,500)]}
 for h,rr in rows.items():
  assert len(rr)==15
  assert [Q(r['kappa'])for r in rr]==[Q(-2,5)+Q(j,20)for j in range(15)]
 out=[];start=time.time()
 for fa in range(4):
  for fb in range(4):
   stack=[''];yes=[];vis=0;maximum=None
   while stack:
    ad=stack.pop();vis+=1;assert len(ad)<30,(fa,fb,ad)
    try:v=test(ad,fa,fb)
    except(ValueError,ZeroDivisionError):v=False
    if v is not False:
     yes.append(ad);maximum=v if maximum is None else max(maximum,v)
    else:stack.extend([ad+'1',ad+'0'])
   yes.sort();assert len(yes)==len(set(yes))
   assert all(not b.startswith(a)for a,b in zip(yes,yes[1:]))
   assert sum((Q(1,2**len(x))for x in yes),Q(0))==1
   row={'faces':[fa,fb],'addresses':yes,'accepted':len(yes),'visited':vis,'maximum_defect_upper':str(maximum)}
   out.append(row);print(fa,fb,len(yes),vis,str(maximum),flush=True)
 assert len(out)==16
 assert INPUT.read_bytes()==source_bytes and initial=={f:sha(ROOT/f)for f in initial}
 assert ph==sha(PROOF)and sh==sha(__file__)
 result={'status':'passed','precision_bits':args.precision,'cases':out,'case_count':16,
         'accepted_cells':sum(r['accepted']for r in out),'gap':'1/1000','raw_positive_seam_rate':'1/20',
         'reference_rectangles':rects,'unselected_target_heights':['-57/1000','0'],
         'selected_target_heights':['0','7/500'],
         'source_input_sha256':hashlib.sha256(source_bytes).hexdigest(),
         'script_sha256':sh,'proof_sha256':ph,'dependencies':initial,
         'elapsed_seconds':time.time()-start,
         'scope':'Actual (4,3) right endpoint, both geometric representatives0/1, all target angles and full unselected/selected target height intervals; original row source and true Fourier weights. No other exterior family or full mixed-word source claim.'}
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
 print('PASS16 boundary products',result['accepted_cells'],'cells',flush=True)
if __name__=='__main__':main()
