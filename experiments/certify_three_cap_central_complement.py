#!/usr/bin/env python3
"""Outward actual cap currents and real retained-index complement.

The central stationary integral is not estimated here. Every domain below
is an original angular remainder, or an absolute real summand outside the
central index square. Exact binary covers are saved only on full success.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import argparse,json,time
from flint import arb,acb,ctx
from certify_three_cap_wire_complement import jreal as original_jreal
from certify_three_vertex_directed_packet import phase
ROOT=Path(__file__).resolve().parents[1]
I=acb(0,1)
def jreal(z):
    z=acb(z);radius=abs(z).upper()
    if z.real.contains(0)and z.imag.contains(0)and radius<arb(1)/20:
        if radius==0:return arb(0)
        bound=radius*(-(2*arb.pi()*radius).log()+arb.pi()+1+arb(1)/199)
        return arb(0,bound.upper())
    return original_jreal(z)
def bupper(x,t):
    return -jreal(arb(1)/2-x+t/(2*arb.pi()))-jreal(arb(1)/2-x-t/(2*arb.pi()))-2*jreal(x)
def psi(t):return -4*jreal(arb(1)/4+t/(4*arb.pi()))-4*jreal(arb(1)/4-t/(4*arb.pi()))
def rat(q):return arb(q.numerator)/q.denominator if isinstance(q,Q)else arb(q)
def interval(a,b):return rat(a).union(rat(b))
def upperabs(v):return max(abs(v.lower()),abs(v.upper()))
def constants():
    pi=arb.pi();yh=arb(2).log()/(2*pi)
    hc=arb('.10135867').union(arb('.10135871'))
    ht=arb('.97895508').union(arb('.97895512'))
    return pi,yh,hc,ht
def domains():
    yield ('capcentral',),2
    for k in range(6):yield ('capcontour',k),2
    yield ('captail',),1;yield ('capradical',),1
    for swap in range(2):
        for r in range(3):yield ('index',swap,r),3
def cap_value(key,p):
    pi,yh,hc,ht=constants();x=acb(arb(7)/50+arb(3)/50*p[0],hc);T=arb(41)/20
    if key[0]=='captail':return bupper(x,acb(T))+psi(acb(T))
    if key[0]=='capradical':return bupper(x,acb(0))
    if key[0]=='capcentral':t=acb(arb(9)/5*p[1],-ht)
    elif key[1]<2:t=acb(-T+T*p[1]if key[1]==0 else arb(9)/5+(T-arb(9)/5)*p[1],-ht)
    else:
        L=2*pi*hc;h=L*p[1]if key[1]%2==0 else L+(ht-L)*p[1]
        t=acb(T if key[1]<4 else -T,-h)
    return bupper(x,t)+psi(t)+3*t.real*(-t.imag)/(2*pi)+t.imag
def index_data(key,p):
    pi,yh,hc,_=constants();x=acb(arb(7)/50+arb(3)/50*p[0],hc);y=acb(arb(1)/6,yh)
    X=(2*pi*I*x).exp();Y=(2*pi*I*y).exp()
    if key[2]==0:lo,hi,tl=arb(0),arb(1)/50,arb(1)/50
    elif key[2]==1:lo,hi,tl=arb(1)/50,arb(1)/4,arb(0)
    else:lo=hi=arb(9)/20;tl=arb(0)
    ds=hi-lo;s=lo+ds*p[1];t=tl+(arb(99)/100-s-tl)*p[2]
    if key[1]:s,t=t,s
    return x,y,X,Y,s,t,ds,tl
def index_value(key,p):
    x,y,X,Y,s,t,_,_=index_data(key,p)
    return (phase(s,t,X,Y)-arb.pi()*I*(x+y)).real
def evaluate(key,box):
    p=[interval(a,b)for a,b in box];c=[rat((a+b)/2)for a,b in box];r=[rat((b-a)/2)for a,b in box]
    if key[0].startswith('cap'):
        direct=cap_value(key,p);costs=None
        threshold=arb(253)/200 if key[0]=='capcentral'else(arb(2)/3 if key[0]=='capradical'else arb(63)/50)
        if key[0]=='capcentral'or(key[0]=='capcontour'and key[1]<2):
            pi,yh,hc,ht=constants();x=acb(arb(7)/50+arb(3)/50*p[0],hc)
            if key[0]=='capcentral':ta=arb(0);ts=arb(9)/5
            elif key[1]==0:ta=-arb(41)/20;ts=arb(41)/20
            else:ta=arb(9)/5;ts=arb(41)/20-ta
            t=acb(ta+ts*p[1],-ht)
            cp=(pi*x+t/2).cos();cm=(pi*x-t/2).cos();sn=(pi*x).sin()
            bx=cp.log()+cm.log()-2*sn.log()
            bt=(cp.log()-cm.log())/(2*pi)-((t/2).tan()+1/(t/2).cos()).log()/pi+3*I*t/(2*pi)-I
            grads=[arb(3)/50*bx.real,ts*bt.real]
            costs=[r[j]*upperabs(grads[j])for j in range(2)]
            mv=cap_value(key,c)+sum(costs)
            if mv.upper()<direct.upper():direct=mv
        return direct<threshold,costs,direct
    direct=index_value(key,p);x,y,X,Y,s,t,ds,tl=index_data(key,p);pi=arb.pi()
    U=(-2*pi*I*s).exp();V=(-2*pi*I*t).exp()
    fs=(X.log()+(1-U*V).log()-(1-X*U).log()).real
    ft=(Y.log()+(1-U*V).log()-(1-Y*V).log()).real
    gx=((1-X*U).log()-(1-X).log()).real*arb(3)/50
    if key[1]:fs,ft=ft,fs;s,t=t,s
    grads=[gx,ds*(fs-p[2]*ft),(arb(99)/100-s-tl)*ft]
    costs=[r[j]*upperabs(grads[j])for j in range(3)]
    mv=index_value(key,c)+sum(costs)
    if mv.upper()<direct.upper():direct=mv
    return direct<arb(16)/25,costs,direct
def scalar_checks():
    pi,yh,hc,ht=constants();rr=arb(27)/50
    checks={
      'wire radius below 27/50':(-2*pi*hc).exp()<rr,
      'all wire coordinates in central chamber':hc>arb(9)/100 and hc<arb(3)/25,
      'trace height in joint chamber':ht>arb(97)/100 and ht<1,
      'small negative log radius':rr.log()<-arb(3)/5,
      'dilog majorant':rr+rr**2/4+rr**3/(9*(1-rr))<arb(2)/3,
      'top logarithm':arb(25).log()<arb(10)/3,
      'cardinal prefactor':pi*(hc+yh)<arb(7)/10,
      'top real-index rate':-arb(3)/5*arb(99)/100+arb(4)/9+arb(13)/300+arb(7)/10<arb(16)/25,
      'high index central derivative':2*rr<(1+rr*rr).sqrt(),
      'high index endpoint derivative':rr*pi/4<1-rr,
      'high index rotation lower':Q(9,20)-Q(1,5)==Q(1,4),
      'high index rotation upper':arb(7)/8-arb(7)/50<arb(3)/4,
      'real index complement action gap':arb(19113)/10000-arb(253)/200-arb(16)/25>arb(1)/200,
      'angular complement action gap':arb(19113)/10000-arb(63)/50-arb(3237)/5000>arb(3)/1000,
    }
    assert all(checks.values()),checks
    return list(checks)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=160)
    ap.add_argument('--output',default='repro/results/research-three-cap-central-complement.json')
    args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic();checks=scalar_checks();saved=[];visits=0
    for key,dim in domains():
        todo=[('',tuple((Q(0),Q(1))for _ in range(dim)))];leaves=[]
        while todo:
            path,box=todo.pop();visits+=1
            try:passed,costs,v=evaluate(key,box)
            except (ValueError,ZeroDivisionError):passed,costs,v=False,None,None
            if passed:leaves.append(path);continue
            if costs is not None and all(z.is_finite()for z in costs):axis=max(range(dim),key=lambda k:float(costs[k]))
            else:
                weights=[.06,.5,.8]if dim==3 else[.06,2]
                if key[0]=='index'and key[2]==2:weights[1]=0
                axis=max(range(dim),key=lambda k:float(box[k][1]-box[k][0])*weights[k])
            a,b=box[axis];assert b-a>Q(1,2**25),('unproved',key,box,v);mid=(a+b)/2
            for side,ends in enumerate(((a,mid),(mid,b))):
                child=list(box);child[axis]=ends;todo.append((path+str(2*axis+side),tuple(child)))
            assert visits<600000,'Coverage unfinished; no certificate saved.'
        saved.append({'domain':list(key),'dimension':dim,'leaves':leaves});print(key,len(leaves),visits,flush=True)
    deps=['experiments/certify_three_cap_wire_complement.py','experiments/certify_three_vertex_directed_packet.py',
          'notes/research_three_cap_first_attachment.md','notes/research_three_vertex_joint_concavity.md',
          'notes/research_three_cap_wire_complement.md','notes/research_three_vertex_global_wire_bound.md',
          'notes/research_three_cap_central_source.md',
          'notes/research_three_chain_fourier_corner_transfer.md',
          'notes/research_three_attachment_index_currents.md']
    result={'status':'passed','precision_bits':args.precision,'domain_count':len(saved),'domains':saved,
            'leaf_count':sum(len(d['leaves'])for d in saved),'visited':visits,'scalar_checks':checks,
            'elapsed_seconds':time.monotonic()-start,'scope':'Actual central cap angular currents and retained real-index complement; no index-contour sides or aliases.',
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest()for p in deps}}
    path=ROOT/args.output;path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k]for k in ('status','domain_count','leaf_count','visited','elapsed_seconds')}))
if __name__=='__main__':main()
