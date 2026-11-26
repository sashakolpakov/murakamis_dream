#!/usr/bin/env python3
"""Outward bounds for the two original complete-cap wire joins.

Every accepted rectangle is stored as a rational binary partition.  This
uses the same original reflected trace contour as the exterior theorem,
but the wire height ranges from 1013/10000 to log(2)/(2*pi).
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import argparse,json,time
from flint import arb,acb,ctx
from certify_three_cap_wire_complement import bupper,psi,jreal

ROOT=Path(__file__).resolve().parents[1]
def rat(q):return arb(q.numerator)/q.denominator if isinstance(q,Q)else arb(q)
def interval(a,b):return rat(a).union(rat(b))
def domains():
    for side in range(2):
        for endpoint in range(2):yield ('central',side,endpoint),1
        for kind in range(6):yield ('contour',side,kind),2
        yield ('tail',side),1
        yield ('radical',side),1
def evaluate(key,box):
    p=[interval(a,b)for a,b in box]
    pi=arb.pi();Y0=arb(1013)/10000;Y1=arb(2).log()/(2*pi)
    Y=(Y0 if key[2]==0 else Y1)if key[0]=='central'else Y0+(Y1-Y0)*p[0]
    L=2*pi*Y;T=arb(41)/20;H=arb(99)/100
    x=acb(arb(7)/50 if key[1]==0 else arb(1)/5,Y)
    if key[0]=='central':
        t=acb(arb(9)/5*p[0],-H)
        return bupper(x,t)+psi(t)+3*t.real*H/(2*pi)-H
    if key[0]=='tail':return bupper(x,acb(T))+psi(acb(T))
    if key[0]=='radical':return bupper(x,acb(0))
    typ=key[2]
    if typ<2:t=acb(-T+T*p[1]if typ==0 else arb(9)/5+(T-arb(9)/5)*p[1],-H)
    else:
        h=L*p[1]if typ%2==0 else L+(H-L)*p[1]
        t=acb(T if typ<4 else -T,-h)
    return bupper(x,t)+psi(t)+3*t.real*(-t.imag)/(2*pi)+t.imag
def threshold(key):
    if key[0]=='radical':return arb(2)/3
    return arb(1261)/1000 if key[1]==0 else arb(6319)/5000
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=160)
    ap.add_argument('--output',default='repro/results/research-three-cap-wire-joins.json')
    args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic();saved=[];visits=0
    pi=arb.pi();Y1=arb(2).log()/(2*pi)
    scalars={
      'positive wire-height interval':Y1>arb(1013)/10000,
      'wire height change below ninety-one ten-thousandths':Y1-arb(1013)/10000<arb(91)/10000,
      'complete low-kernel half-plane':-2*(arb(41)/20).cos()*(arb(99)/100).cosh()<arb(3)/2,
      'right join strict action reserve':arb(19113)/10000-arb(6319)/5000-arb(3237)/5000>arb(1)/20000,
      'actual root height above join lower end':arb('0.101358689576302370861575311618')-arb('0.00000001')>arb(1013)/10000,
      'actual root height below homogeneous height':arb('0.101358689576302370861575311618')+arb('0.00000001')<Y1,
      'actual join height change below nine thousandths':Y1-arb('0.101358689576302370861575311618')+arb('0.00000001')<arb(9)/1000,
    }
    assert all(scalars.values()),scalars
    for key,dim in domains():
        todo=[('',tuple((Q(0),Q(1))for _ in range(dim)))];leaves=[]
        while todo:
            path,box=todo.pop();visits+=1;value=evaluate(key,box)
            if value<threshold(key):leaves.append(path);continue
            weights=[1.8]if key[0]=='central'else([.01]if dim==1 else[.01,2.05 if key[2]==0 else(.25 if key[2]==1 else .7)])
            axis=max(range(dim),key=lambda k:float(box[k][1]-box[k][0])*weights[k])
            a,b=box[axis];assert b-a>Q(1,2**25),('unproved',key,box,value)
            mid=(a+b)/2
            for side,ends in enumerate(((a,mid),(mid,b))):
                child=list(box);child[axis]=ends;todo.append((path+str(2*axis+side),tuple(child)))
            assert visits<400000,'Coverage unfinished; no certificate saved.'
        saved.append({'domain':list(key),'dimension':dim,'leaves':leaves})
        print(key,len(leaves),visits,flush=True)
    deps=['experiments/certify_three_cap_wire_complement.py',
          'notes/research_three_cap_wire_complement.md',
          'notes/research_three_vertex_joint_concavity.md',
          'notes/research_three_vertex_global_wire_bound.md',
          'notes/research_three_cap_first_attachment.md']
    result={'status':'passed','precision_bits':args.precision,'domains':saved,
            'domain_count':len(saved),'leaf_count':sum(len(d['leaves'])for d in saved),
            'visited':visits,'scalar_checks':list(scalars),'elapsed_seconds':time.monotonic()-start,
            'scope':'Original complete-cap bound on the vertical joins xi=7/50 and xi=1/5, 1013/10000<=Im x<=log(2)/(2*pi).',
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest()for p in deps}}
    path=ROOT/args.output;path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k]for k in ('status','domain_count','leaf_count','visited','elapsed_seconds')}))
if __name__=='__main__':main()
