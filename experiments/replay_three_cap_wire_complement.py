#!/usr/bin/env python3
"""Independent reflection-based replay of the actual cap exterior certificate."""
from fractions import Fraction as R
from pathlib import Path
from hashlib import sha256
import argparse,json,time
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1]
i=acb(0,1)
def rat(q):return arb(q.numerator)/q.denominator if isinstance(q,R)else arb(q)
def interval(a,b):return rat(a).union(rat(b))
def positive_primitive(a,b):
 z=acb(a,b);p=arb.pi()
 return (-i*p*(z*z-z)/2+i*(2*p*i*z).exp().polylog(2)/(2*p)-i*p/12).real
def jr(z):
 z=acb(z);a=z.real;b=abs(z.imag)
 if a.contains(0) and b.contains(0) and abs(acb(a,b))<arb(1)/20:return arb(0,arb(3)/10)
 if a>=0:return positive_primitive(a,b)
 if a<=0:return -positive_primitive(-a,b)-arb.pi()*b
 # Split an interval crossing the real-coordinate wall exactly at zero.
 pos=positive_primitive(arb(0).union(a.upper()),b)
 neg=-positive_primitive(arb(0).union(-a.lower()),b)-arb.pi()*b
 return pos.union(neg)
def bphase(x,t):return -jr(arb(1)/2-x+t/(2*arb.pi()))-jr(arb(1)/2-x-t/(2*arb.pi()))-2*jr(x)
def edge(t):return -4*jr(arb(1)/4+t/(4*arb.pi()))-4*jr(arb(1)/4-t/(4*arb.pi()))
REGIONS=[(R(-1,8),R(0)),(R(0),R(7,50)),(R(1,5),R(1,2)),(R(1,2),R(7,8))]
def value(key,box):
 p=[interval(a,b)for a,b in box];lo,hi=REGIONS[key[1]]
 pi=arb.pi();L=arb(2).log();Y=L/(2*pi);T=arb(41)/20;H=arb(99)/100
 x=acb(rat(lo)+rat(hi-lo)*p[0],Y)
 if key[0]=='tail':return bphase(x,acb(T))+edge(acb(T))
 typ=key[2]
 if typ<2:t=acb(-T+T*p[1]if typ==0 else T*p[1],-H)
 else:
  h=L*p[1]if typ%2==0 else L+(H-L)*p[1]
  t=acb(T if typ<4 else -T,-h)
 return bphase(x,t)+edge(t)+3*t.real*(-t.imag)/(2*pi)+t.imag
def partition(paths,dimension):
    """Verify exact multiplicity-one cover, including all shared faces."""
    trie={}
    for path in paths:
        node=trie
        for char in path:
            assert '#' not in node,'Leaf contains another leaf'
            k=int(char);assert 0<=k<2*dimension
            node=node.setdefault(k,{})
        assert not node,'Duplicate leaf or leaf contains previous subtree'
        node['#']=True
    def walk(node,box):
        if '#'in node:
            assert list(node)==['#'];yield box;return
        codes=sorted(node)
        assert len(codes)==2 and codes[0]%2==0 and codes[1]==codes[0]+1,'Incomplete rectangle partition'
        axis=codes[0]//2;lo,hi=box[axis];mid=(lo+hi)/2
        for code,ends in zip(codes,((lo,mid),(mid,hi))):
            child=list(box);child[axis]=ends
            yield from walk(node[code],tuple(child))
    yield from walk(trie,tuple((R(0),R(1))for _ in range(dimension)))


def main():
 ap=argparse.ArgumentParser();ap.add_argument('artifact',nargs='?',default='repro/results/research-three-cap-wire-complement.json');ap.add_argument('--precision',type=int,default=192);ap.add_argument('--output',default='repro/results/research-three-cap-wire-complement-replay.json')
 args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic();path=ROOT/args.artifact;data=json.loads(path.read_text());assert data['status']=='passed'
 expected={('contour',r,k):2 for r in range(4)for k in range(6)};expected.update({('tail',r):1 for r in (1,2)})
 seen=set();original=refined=visits=0
 for dom in data['domains']:
  key=tuple(dom['domain']);assert key in expected and key not in seen;seen.add(key);assert dom['dimension']==expected[key]
  for original_box in partition(dom['leaves'],dom['dimension']):
   original+=1;todo=[original_box]
   while todo:
    box=todo.pop();visits+=1;v=value(key,box)
    if v<arb(253)/200:refined+=1;continue
    axis=max(range(len(box)),key=lambda k:box[k][1]-box[k][0]);a,b=box[axis];assert b-a>R(1,2**27),(key,box,v)
    mid=(a+b)/2
    for left,right in ((a,mid),(mid,b)):
     child=list(box);child[axis]=(left,right);todo.append(tuple(child))
    assert visits<500000,'Replay unfinished'
 assert seen==set(expected)and original==data['leaf_count']
 p=arb.pi();L=arb(2).log();Y=L/(2*p);T=arb(41)/20;r=arb(1)/20;z=p*r
 comparisons=[arb(1)/200-(z.sinh()/z-1),arb(3)/10-r*(-(2*p*r).log()+p+1+arb(1)/199),(-arb(1)).exp()-2*p*r,arb(24)/25-arb(1)/2-arb(1)/8-T/(2*p),arb(3)/2+2*T.cos()*(arb(99)/100).cosh(),arb(23)/20-edge(acb(T))-p*Y,arb(2)/3-bphase(acb(arb(1)/4,Y),acb(0)),arb(2)/3-p*Y,arb(161533)/500000-2*jr(acb(arb(5)/6)),arb(19113)/10000-(2*arb(161533)/500000+arb(253)/200)-arb(1)/10000]
 assert all(q>0 for q in comparisons)
 for f,h in data['dependencies_sha256'].items():assert sha256((ROOT/f).read_bytes()).hexdigest()==h,f
 assert sha256((ROOT/'experiments/certify_three_cap_wire_complement.py').read_bytes()).hexdigest()==data['script_sha256']
 result={'status':'passed','precision_bits':args.precision,'domain_count':len(seen),'original_leaf_count':original,'replayed_leaf_count':refined,'interval_visits':visits,'exact_binary_cover':True,'scalar_checks':len(comparisons),'primitive':'Independent reflection of negative real part to the ordinary positive strip','elapsed_seconds':time.monotonic()-start,'artifact_sha256':sha256(path.read_bytes()).hexdigest(),'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
 (ROOT/args.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
