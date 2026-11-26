#!/usr/bin/env python3
"""Supporting planes for the prepared source on a wider real output interval.

This script records only the explicitly enumerated original currents.
Critical-height translation is a separate required scope until supplied
by the real-output critical-branch certificate.
"""
from fractions import Fraction as Q
from pathlib import Path
from itertools import product
from hashlib import sha256
import argparse,json,time
import numpy as np
from scipy.optimize import minimize
from scipy.special import spence
from flint import arb,acb,ctx
from certify_three_prepared_central_currents import function,numeric,BASE

ROOT=Path(__file__).resolve().parents[1];I=acb(0,1)
B=[(Q(7,50),Q(1,5)),(Q(0),Q(9,5)),(Q(1,4),Q(9,20)),
   (Q(1,4),Q(9,20)),(Q(11,75),Q(14,75))]

def r(v):
    if isinstance(v,arb):return v
    v=Q(v);return arb(v.numerator)/v.denominator

def height(which):
    return r('.10135867').union(r('.10135871')) if which==0 else arb(2).log()/(2*arb.pi())

def envelope(point,which,xi=None,eta=None):
    s,t=map(r,point);p=arb.pi();rad=(-2*p*height(which)).exp()
    J=-(2*p*I*(s+t)).exp().polylog(2).imag/(2*p)
    ell=lambda z,R:-(R*(p*I*z).exp()).polylog(2).imag/p
    if xi is None:
        den=ell(s,rad)
        g0=(2*rad*(p*(s+t)).sin()).log()-abs(1-rad*(p*I*s).exp()).log()
    else:
        X=rad*(2*p*I*r(xi)).exp();U=(-2*p*I*s).exp()
        den=((X*U).polylog(2)-X.polylog(2)).imag/(2*p)
        g0=(2*rad*(p*(s+t)).sin()).log()-abs(1-X*U).log()
    if eta is None:
        den1=ell(t,arb(1)/2)
        g1=(p*(s+t)).sin().log()-abs(1-(p*I*t).exp()/2).log()
    else:
        Y=(2*p*I*r(eta)).exp()/2;V=(-2*p*I*t).exp()
        den1=((Y*V).polylog(2)-Y.polylog(2)).imag/(2*p)
        g1=(p*(s+t)).sin().log()-abs(1-Y*V).log()
    val=-(rad/2).log()/2+J+s*rad.log()-t*arb(2).log()-den-den1
    return val,[g0,g1]

def envelope_numeric(point,which,xi=None,eta=None):
    s,t=point;p=np.pi;h=.10135869 if which==0 else np.log(2)/(2*p);rad=np.exp(-2*p*h)
    li=lambda z:spence(1-z)
    J=-li(np.exp(2j*p*(s+t))).imag/(2*p)
    ell=lambda z,R:-li(R*np.exp(1j*p*z)).imag/p
    if xi is None:den=ell(s,rad)
    else:
        X=rad*np.exp(2j*p*float(xi))
        den=(li(X*np.exp(-2j*p*s))-li(X)).imag/(2*p)
    if eta is None:den1=ell(t,.5)
    else:
        Y=.5*np.exp(2j*p*float(eta))
        den1=(li(Y*np.exp(-2j*p*t))-li(Y)).imag/(2*p)
    return -.5*np.log(rad/2)+J+s*np.log(rad)+t*np.log(.5)-den-den1

def domains():
    for axis,end,hs,ht in product((2,3),(0,1),(-Q(1,125),Q(1,125)),(-Q(17,1000),Q(3,250))):
        h=BASE[:];h[2]=hs;h[3]=ht;b=B[:];b[axis]=(b[axis][end],)*2
        yield ('index_side',axis,end,str(hs),str(ht)),b,h+[Q(0)],Q(19107,10000)
    for hs,ht in product((-Q(1,125),Q(1,125)),(-Q(17,1000),Q(3,250))):
        h=BASE[:];h[2]=hs;h[3]=ht
        yield ('alias',str(hs),str(ht)),B,h+[Q(0)],Q(39,20)
    for axis,end in product(range(4),(0,1)):
        b=B[:];b[axis]=(b[axis][end],)*2
        yield ('initial_face',axis,end),b,BASE+[Q(0)],Q(19107,10000)

def complex_gradient(point,heights):
    p=arb.pi();x,tau,s,t=[acb(r(point[j]),r(heights[j]))for j in range(4)]
    y=acb(r(point[4]),arb(2).log()/(2*p))
    X=(2*p*I*x).exp();Y=(2*p*I*y).exp();U=(-2*p*I*s).exp();V=(-2*p*I*t).exp()
    cp=(p*x+tau/2).cos().log();cm=(p*x-tau/2).cos().log()
    bx=cp+cm-2*(p*x).sin().log()
    bt=(cp-cm)/(2*p)-((tau/2).tan()+1/(tau/2).cos()).log()/p+3*I*tau/(2*p)-I
    px=2*p*I*s+(1-X*U).log()-(1-X).log()-p*I
    py=2*p*I*t+(1-Y*V).log()-(1-Y).log()-p*I
    fs=X.log()+(1-U*V).log()-(1-X*U).log()
    ft=Y.log()+(1-U*V).log()-(1-Y*V).log()
    return [bx+px,bt,fs,ft,py]

def height_plane_value(point,heights):
    mid=[z.mid()for z in heights]
    value,_=function(point,mid+[Q(0)])
    g=complex_gradient(point,heights)
    value+=sum(abs(gj.imag).upper()*abs(hj-mj).upper()for gj,hj,mj in zip(g,heights,mid))
    return value,[z.real for z in g]

def certify_plane(key,box,target,evaluate,propose,center):
    center=list(center)
    for j,(a,b)in enumerate(box):center[j]=min(b,max(a,center[j]))
    free=[j for j,(a,b)in enumerate(box)if a!=b]
    def extend(z):
        pt=list(map(float,center))
        for j,v in zip(free,z):pt[j]=v
        return pt
    sol=minimize(lambda z:-propose(extend(z)),[float(center[j])for j in free],
                 method='Nelder-Mead',bounds=[tuple(map(float,box[j]))for j in free],
                 options={'maxiter':6000,'xatol':1e-12,'fatol':1e-13})
    point=center[:]
    for j,v in zip(free,sol.x):point[j]=min(box[j][1],max(box[j][0],Q(str(float(v)))))
    value,g=evaluate(point)
    upper=value+sum(max((gj*r(a-z)).upper(),(gj*r(b-z)).upper())for gj,(a,b),z in zip(g,box,point))
    assert upper<r(target),(key,upper,point,g)
    return {'domain':list(key),'bounds':[[str(a),str(b)]for a,b in box],
            'support_point':list(map(str,point)),'threshold':str(target),
            'support_upper':str(upper)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=160)
    ap.add_argument('--output',default='repro/results/research-three-prepared-real-output-currents.json')
    args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic();saved=[]
    for key,box,h,target in domains():
        item=certify_plane(key,box,target,lambda z:function(z,h),lambda z:numeric(z,h),
                           list(map(Q,['.1773','1.534','.351','.325']))+[Q(1,6)])
        item['heights']=list(map(str,h));saved.append(item)
    for which,axis,end in product(range(2),range(2),range(2)):
        cut=Q(1,4)if end==0 else Q(9,20);box=[(Q(1,2)-cut,1-cut)]*2;box[axis]=(cut,cut)
        item=certify_plane(('real_index_complement',which,axis,end),box,Q(16,25),
                           lambda z:envelope(z,which),lambda z:envelope_numeric(z,which),[Q('.35'),Q('.34')])
        saved.append(item)
    for which,xi in product(range(2),(Q(7,50),Q(1,5))):
        item=certify_plane(('wire_join',which,str(xi)),[(Q(1,4),Q(9,20))]*2,Q(6459,10000),
                           lambda z:envelope(z,which,xi),lambda z:envelope_numeric(z,which,xi),[Q('.35'),Q('.33')])
        saved.append(item)
    for cut in (Q(22,75),Q(28,75)):
        box=[(Q(1,2)-cut,1-cut),(cut,cut)]
        item=certify_plane(('far_output_index',str(cut)),box,Q(6465,10000),
                           lambda z:envelope(z,0),lambda z:envelope_numeric(z,0),[Q('.35'),cut])
        saved.append(item)
    for eta in (Q(11,75),Q(14,75)):
        box=[(Q(1,4),Q(9,20)),(Q(22,75),Q(28,75))]
        item=certify_plane(('far_output_phase',str(eta)),box,Q(6465,10000),
                           lambda z:envelope(z,0,eta=eta),lambda z:envelope_numeric(z,0,eta=eta),[Q('.35'),Q('.33')])
        saved.append(item)
    critical_path=ROOT/'repro/results/research-three-prepared-cap-real-critical.json'
    critical=json.loads(critical_path.read_text());assert critical['status']=='passed'
    intervals=sorted((Q(cell['output_interval'][0]),Q(cell['output_interval'][1]))for cell in critical['cells'])
    assert len(intervals)==critical['cell_count']and intervals[0][0]==-Q(1,50)and intervals[-1][1]==Q(1,50)
    assert all(a<b for a,b in intervals)and all(a[1]==b[0]for a,b in zip(intervals,intervals[1:]))
    for j,cell in enumerate(critical['cells']):
        heights=[arb(parts[1])for parts in cell['coordinate_parts']]
        coordinates=[arb(parts[0])for parts in cell['coordinate_parts']]
        center=[Q(str(float(z.mid())))for z in coordinates]
        a,b=map(Q,cell['output_interval']);center.append(Q(1,6)+(a+b)/2)
        for axis,end in product(range(4),(0,1)):
            box=B[:];box[4]=(Q(1,6)+a,Q(1,6)+b);box[axis]=(box[axis][end],)*2
            item=certify_plane(('critical_face',j,axis,end),box,Q(19107,10000),
                               lambda z:height_plane_value(z,heights),
                               lambda z:numeric(z,[float(h.mid())for h in heights]+[Q(0)]),center)
            item['height_enclosures']=[str(h)for h in heights];saved.append(item)
        if j%50==0:print('critical cells',j+1,'/',len(critical['cells']),flush=True)
    checks={'low_sum_envelope':Q(347,500)-Q(7,100)+Q(3,250)<Q(16,25),
            'real_index_product':Q(126465,100000)+Q(16,25)<Q(19107,10000),
            'angular_remainder_product':Q(63,50)+Q(64699,100000)<Q(19107,10000),
            'wire_join_product':Q(6319,5000)+Q(6459,10000)<Q(19107,10000),
            'exterior_product':Q(158,125)+2*Q(161533,500000)<Q(19107,10000),
            'far_output_product':Q(126465,100000)+Q(6465,10000)<Q(191116,100000),
            'alias_penalty':r(Q(39,20))-2*arb.pi()/125<r(Q(19107,10000))}
    assert all(checks.values()),checks
    deps=['experiments/certify_three_prepared_central_currents.py',
          'notes/research_three_vertex_joint_concavity.md',
          'notes/research_three_vertex_global_wire_bound.md',
          'notes/research_three_prepared_cap_period_bound.md',
          'notes/research_three_prepared_cap_quantified_source.md',
          'notes/research_three_prepared_cap_real_extension.md',
          'repro/results/research-three-prepared-cap-real-critical.json']
    result={'status':'passed','precision_bits':args.precision,'domain_count':len(saved),'domains':saved,
            'scalar_checks':list(checks),'elapsed_seconds':time.monotonic()-start,
            'scope':'All initial and actual critical-height boundary currents, real-index and wire-join complements on real output±.02, with a far-output bound; no source asymptotic inferred without the written Stokes proof.',
            'critical_cell_count':len(critical['cells']),'exact_critical_interval_cover':True,
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest()for p in deps}}
    (ROOT/args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k]for k in ('status','domain_count','elapsed_seconds')}))

if __name__=='__main__':main()
