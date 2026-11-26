#!/usr/bin/env python3
"""Outward compact certificate for the real-input / union-output retained packet.

No sampled inequality is accepted.  Each leaf is a rational binary rectangle;
its full interval, or a first-derivative mean-value enclosure, is checked.
The paths in the result preserve the complete partition for independent replay.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from itertools import product
import argparse
import json
import time
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]
CUT, A, B = Q(1,40), Q(23,100), Q(9,20)
REGIONS = [(Q(0), CUT, CUT), (CUT, A, Q(0)), (B, B, Q(0))]
# Exact millesimal index heights; columns are s_low,s_high,t_low,t_high.
PATCHES = {
 'disk': [(-26,6,-6,23),(-20,6,-6,19),(-15,6,-6,15),(-10,6,-8,12),
          (-6,10,-12,8),(-6,15,-15,6),(-6,20,-19,6),(-6,24,-23,6)],
 'real': [(-29,6,-6,25),(-23,6,-6,21),(-18,6,-7,18),(-13,8,-11,14),
          (-8,13,-14,10),(-6,18,-18,7),(-6,23,-22,6),(-6,27,-25,6)]}
I = acb(0, 1)


def ball(x):
    return arb(x.numerator) / x.denominator if isinstance(x, Q) else arb(x)


def interval(a, b):
    return ball(a).union(ball(b))


def base():
    return acb(arb(1)/6, arb(2).log()/(2*arb.pi()))


def wires(family, patch, a, b):
    x = base()+ball(Q(patch-4,200))+a/200
    if family == 'disk':
        displacement = (2*arb.pi()*I*b).exp()/200
        return x, base()+displacement, acb(arb(1)/200), 2*arb.pi()*I*displacement
    return x, base()+arb(9)/500*(b-arb(1)/2), acb(arb(1)/200), acb(arb(9)/500)


def geometry_wires(a,b,c):
    return base()+arb(1)/25*(a-arb(1)/2), base()+arb(9)/500*(b-arb(1)/2)+I/100*(c-arb(1)/2)


def critical(x, y):
    pi = arb.pi()
    X, Y = (2 * pi * I * x).exp(), (2 * pi * I * y).exp()
    a, b = 1 / X - 1, 1 / Y - 1
    delta = 1 - 2 * (a + b) + (a - b)**2
    assert delta.imag > 0
    root = delta.sqrt()
    u, v = (1 + a - b - root) / 2, (1 - a + b - root) / 2
    assert u.real < 0 and u.imag < 0 and v.real < 0 and v.imag < 0
    return X, Y, u, v, I * u.log() / (2 * pi), I * v.log() / (2 * pi)


def primitive(z):
    z, pi = acb(z), arb.pi()
    return -I * pi * (z*z-z) / 2 + I * (2*pi*I*z).exp().polylog(2)/(2*pi) - I*pi/12


def phase(s, t, X, Y):
    pi = arb.pi()
    def integral(z, w):
        return ((w * (-2*pi*I*z).exp()).polylog(2)-w.polylog(2))/(2*pi*I)
    return (primitive(s+t)+I*pi*((s+t)-(s+t)**2)/2+s*X.log()+t*Y.log()
            - integral(s, X)-integral(t, Y))


def derivatives(s, t, X, Y):
    u, v = (-2*arb.pi()*I*s).exp(), (-2*arb.pi()*I*t).exp()
    return (X.log()+(1-u*v).log()-(1-X*u).log(),
            Y.log()+(1-u*v).log()-(1-Y*v).log(), u, v)


def index_side(family, patch, coordinate, face, z):
    lo,hi = [arb(k)/1000 for k in PATCHES[family][patch][2*coordinate:2*coordinate+2]]
    if face < 2:
        return acb(ball(A if face == 0 else B),lo+(hi-lo)*z), I*(hi-lo)
    return acb(ball(A)+ball(B-A)*z,lo if face==2 else hi), acb(ball(B-A))


def domains():
    yield ('geometry',),3
    for family, patch in product(('disk','real'),range(8)):
        yield ('floor',family,patch),2
        for r,flip in product(range(3),range(2)):
            yield ('exterior',family,patch,r,flip),4
        for j,k in product(range(4),repeat=2):
            yield ('contour',family,patch,j,k),4


def abs_upper(x):
    return max(abs(x.lower()), abs(x.upper()))


def evaluate(domain, box):
    p = [interval(a, b) for a, b in box]
    c = [ball((a+b)/2) for a, b in box]
    radii = [ball((b-a)/2) for a, b in box]
    if domain[0] == 'geometry':
        X,Y,u,v,s,t=critical(*geometry_wires(*p))
        margins=[X.real-arb(2)/25,X.imag-arb(2)/25,Y.real-arb(2)/25,Y.imag-arb(2)/25,
                 arb(27)/50-abs(X),arb(27)/50-abs(Y)]
        for z in (s,t):
            margins += [z.real-arb(3)/10,arb(2)/5-z.real,arb(1)/25-abs(z.imag)]
        return all(z>0 for z in margins),None,min(z.lower() for z in margins)
    _,family,patch,*extra=domain
    x,y,dx,dy=wires(family,patch,p[0],p[1])
    X,Y,u,v,sc,tc=critical(x,y)
    if domain[0] == 'floor':
        margins=[]
        for coordinate,z in enumerate((sc,tc)):
            lo,hi=[arb(k)/1000 for k in PATCHES[family][patch][2*coordinate:2*coordinate+2]]
            margins.extend([z.imag-lo-arb(1)/100000,hi-z.imag-arb(1)/100000])
        if not all(z>0 for z in margins):return False,None,None
        grads=[(2*arb.pi()*I*sc+(1-X*u).log()-(1-X).log())*dx,
               (2*arb.pi()*I*tc+(1-Y*v).log()-(1-Y).log())*dy]
        xc,yc,_,_=wires(family,patch,c[0],c[1])
        Xc,Yc,_,_,ss,tt=critical(xc,yc)
        value=phase(ss,tt,Xc,Yc).real
        costs=[radii[k]*abs_upper(grads[k].real) for k in range(2)]
        lower=value-sum(costs)
        return lower>-arb(1)/10,costs,lower
    if domain[0] == 'exterior':
        sl, sr, tl = REGIONS[extra[0]]
        ds = ball(sr-sl)
        s = ball(sl)+ds*p[2]; t = ball(tl)+(arb(99)/100-s-ball(tl))*p[3]
        ds2, dt2, ds3, dt3 = ds, -ds*p[3], 0, arb(99)/100-s-ball(tl)
        ss = ball(sl)+ds*c[2]; tt = ball(tl)+(arb(99)/100-ss-ball(tl))*c[3]
        if extra[1]:
            s,t,ss,tt = t,s,tt,ss
            ds2,dt2,ds3,dt3 = dt2,ds2,dt3,ds3
        fs, ft, us, vt = derivatives(s,t,X,Y)
        last = [(-fs*ds2-ft*dt2).real, (-fs*ds3-ft*dt3).real]
        threshold = ball(Q(1,250))
    else:
        j, k = extra
        s, ds = index_side(family,patch,0,j,p[2]); t, dt = index_side(family,patch,1,k,p[3])
        fs, ft, us, vt = derivatives(s,t,X,Y)
        last = [(-fs*ds).real, (-ft*dt).real]
        ss, _ = index_side(family,patch,0,j,c[2]); tt, _ = index_side(family,patch,1,k,c[3])
        threshold = ball(Q(1,1000) if min(j,k)<2 else Q(-1,50))
    gx = (2*arb.pi()*I*(sc-s)+(1-X*u).log()-(1-X*us).log())*dx
    gy = (2*arb.pi()*I*(tc-t)+(1-Y*v).log()-(1-Y*vt).log())*dy
    grads = [gx.real,gy.real]+last
    xc,yc,_,_=wires(family,patch,c[0],c[1])
    Xc,Yc,_,_,scc,tcc=critical(xc,yc)
    value = (phase(scc,tcc,Xc,Yc)-phase(ss,tt,Xc,Yc)).real
    costs = [radii[k]*abs_upper(grads[k]) for k in range(4)]
    lower = value-sum(costs)
    return lower>threshold, costs, lower


def scalar_checks():
    r,pi=arb(27)/50,arb.pi()
    comparisons={
      'wire_radius':arb(1)/2*(pi/100).exp()<r,
      'log_radius':r.log()<-arb(3)/5,
      'dilog_majorant':r+r*r/4+r**3/(9*(1-r))<arb(2)/3,
      'top_log':arb(25).log()<arb(10)/3,
      'top_gap':-arb(1)/10-(-arb(3)/5*arb(99)/100+arb(4)/9+arb(13)/300)>arb(1)/200,
      'high_index_first':2*r<(1+r*r).sqrt(),
      'high_index_last':2*r*arb(11)*pi/100<1-r,
      'high_index_rotation':2*pi*(arb(1)/6+arb(1)/50-arb(9)/20)<-pi/2,
      'high_index_rotation_other':2*pi*(arb(1)/6-arb(1)/50-arb(89)/100)>-3*pi/2,
      'alias_margin':2*pi*arb(6)/1000-arb(1)/50>arb(1)/100,
      'interpolant_denominator':r*(2*pi*arb(29)/1000).exp()<1,
      'height_cosh':(arb(2).log()+arb(68)*pi/1000).cosh()<arb(3)/2,
      'index_hessian_lower':pi*(arb(13)*pi/150).sin()/(arb(3)/2-(arb(13)*pi/150).cos())>arb(3)/2,
      'index_hessian_upper':pi*(arb(91)*pi/150).sin()/(arb(3)/2-(arb(91)*pi/150).cos())>arb(3)/2,
      'negative_common_hessian':pi*(pi/25).tan()<arb(2)/5,
    }
    assert all(comparisons.values()),comparisons
    assert all(lo<=-6 and hi>=6 for rows in PATCHES.values() for p in rows for lo,hi in (p[:2],p[2:]))
    return list(comparisons)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--precision',type=int,default=160)
    parser.add_argument('--output',default='repro/results/research-three-vertex-real-input-union.json')
    args=parser.parse_args();ctx.prec=args.precision
    scalars=scalar_checks();start=time.monotonic();results=[];visited=0
    for domain, dim in domains():
        stack=[('',tuple((Q(0),Q(1)) for _ in range(dim)))];leaves=[]
        while stack:
            path,box=stack.pop();visited+=1
            try: passed,costs,_=evaluate(domain,box)
            except (AssertionError,ValueError,ZeroDivisionError): passed,costs=False,None
            if passed: leaves.append(path);continue
            if costs is not None and all(c.is_finite() for c in costs):
                axis=max(range(dim),key=lambda k:float(costs[k].upper()))
            else:
                weights=([.04,.018,.01] if domain[0]=='geometry' else [.02,.04,.5,.8])
                if domain[0]=='exterior' and domain[3]==2:weights[2]=0
                axis=max(range(dim),key=lambda k:float(box[k][1]-box[k][0])*weights[k])
            lo,hi=box[axis]
            assert hi-lo>Q(1,2**24), ('unproved',domain,box)
            mid=(lo+hi)/2
            for side,(a,b) in enumerate(((lo,mid),(mid,hi))):
                child=list(box);child[axis]=(a,b)
                stack.append((path+str(2*axis+side),tuple(child)))
            assert visited<1000000,'Coverage unfinished; no certificate saved.'
        results.append({'domain':list(domain),'dimension':dim,'leaves':leaves})
        if len(results)%16==0: print('domains',len(results),'leaves',sum(len(d['leaves'])for d in results),flush=True)
    paths=['notes/research_three_vertex_real_input_union.md',
           'notes/research_three_vertex_input_rectangle.md',
           'notes/research_three_vertex_joint_concavity.md',
           'notes/research_three_vertex_central_index_chart.md',
           'notes/research_traced_three_vertex_endpoint.md',
           'notes/research_root_pochhammer_interpolation.md',
           'notes/exact_factorial_interpolation_and_complex_contours.md']
    result={'status':'passed','precision_bits':args.precision,
            'input_real_radius':'1/50','output_disk_radius':'1/200','output_real_radius':'9/1000',
            'deleted_corner_fraction':str(CUT),'index_heights_millesimal':PATCHES,'domains':results,
            'domain_count':len(results),'leaf_count':sum(len(d['leaves'])for d in results),
            'visited':visited,'scalar_checks':scalars,'elapsed_seconds':time.monotonic()-start,
            'scope':'Original retained L40 vertex, real input radius1/50, output true disk radius1/200 union real interval radius9/1000 about x_h. Separate fixed contours on eight input patches; no source-class induction asserted.',
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest()for p in paths if (ROOT/p).exists()}}
    output=ROOT/args.output;output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k]for k in ('status','domain_count','leaf_count','visited','elapsed_seconds')}))
    print(output)


if __name__=='__main__':main()
