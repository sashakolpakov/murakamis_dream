#!/usr/bin/env python3
"""Independent replay of the real-input / union-output finite-source cover.

No author module is imported.  The action uses the negative-frequency
dilogarithm primitive, independently of the author's J-based expression.
Every stored partition is checked as a complete binary rectangle tree.
"""
from fractions import Fraction as R
from pathlib import Path
from hashlib import sha256
from itertools import product
import argparse
import json
import time
from flint import arb, acb, ctx

ROOT=Path(__file__).resolve().parents[1]
ii=acb(0,1)


def real(x):
    return arb(x.numerator)/x.denominator if isinstance(x,R) else arb(x)


def enclosure(a,b):
    return real(a).union(real(b))


HEIGHTS={
 'disk':((-26,6,-6,23),(-20,6,-6,19),(-15,6,-6,15),(-10,6,-8,12),
         (-6,10,-12,8),(-6,15,-15,6),(-6,20,-19,6),(-6,24,-23,6)),
 'real':((-29,6,-6,25),(-23,6,-6,21),(-18,6,-7,18),(-13,8,-11,14),
         (-8,13,-14,10),(-6,18,-18,7),(-6,23,-22,6),(-6,27,-25,6))}


def center():return acb(arb(1)/6,arb(2).log()/(2*arb.pi()))


def parameters(family,j,a,b):
    x=center()+(j-4+a)/200
    if family=='real':return x,center()+9*(2*b-1)/1000,acb(arb(1)/200),acb(arb(9)/500)
    yy=(2*arb.pi()*ii*b).exp()/200
    return x,center()+yy,acb(arb(1)/200),2*arb.pi()*ii*yy


def point(x,y):
    X=(2*arb.pi()*ii*x).exp();Y=(2*arb.pi()*ii*y).exp()
    a=1/X-1;b=1/Y-1;delta=1-2*a-2*b+(a-b)**2
    assert delta.imag>0
    d=delta.sqrt();u=(1+a-b-d)/2;v=(1-a+b-d)/2
    assert max(u.real.upper(),u.imag.upper(),v.real.upper(),v.imag.upper())<0
    return X,Y,u,v,ii*u.log()/(2*arb.pi()),ii*v.log()/(2*arb.pi())


def action(s,t,X,Y):
    E=lambda z:(-2*arb.pi()*ii*z).exp()
    # Integral from zero of log(1-exp(-2*pi*i*z)), with the original lift.
    d=(E(s+t).polylog(2)-arb.pi()**2/6
       -(X*E(s)).polylog(2)+X.polylog(2)
       -(Y*E(t)).polylog(2)+Y.polylog(2))
    return d/(2*arb.pi()*ii)+s*X.log()+t*Y.log()


def sides(family,patch,coordinate,f,z):
    lo,hi=HEIGHTS[family][patch][2*coordinate:2*coordinate+2]
    if f<2:return acb(arb(23)/100 if f==0 else arb(9)/20,(lo+(hi-lo)*z)/1000),ii*(hi-lo)/1000
    return acb(arb(23)/100+11*z/50,arb(lo if f==2 else hi)/1000),acb(arb(11)/50)


def boundabs(z):
    return max(abs(z.lower()),abs(z.upper()))


def check(domain,box):
    p=[enclosure(a,b)for a,b in box];c=[real((a+b)/2)for a,b in box]
    widths=[real((b-a)/2)for a,b in box]
    kind=domain[0]
    if kind=='geometry':
        X,Y,u,v,s,t=point(center()+(2*p[0]-1)/50,center()+9*(2*p[1]-1)/1000+ii*(2*p[2]-1)/200)
        assert all(z.real>arb(2)/25 and z.imag>arb(2)/25 and abs(z)<arb(27)/50 for z in (X,Y))
        assert all(z.real>arb(3)/10 and z.real<arb(2)/5 and abs(z.imag)<arb(1)/25 for z in (s,t))
        return
    family,patch=domain[1:3];x,y,dx,dy=parameters(family,patch,p[0],p[1])
    X,Y,u,v,sc,tc=point(x,y)
    xc,yc,_,_=parameters(family,patch,c[0],c[1]);Xc,Yc,_,_,sc0,tc0=point(xc,yc)
    if kind=='floor':
        for coordinate,z in enumerate((sc,tc)):
            lo,hi=HEIGHTS[family][patch][2*coordinate:2*coordinate+2]
            assert z.imag>arb(lo)/1000+arb(1)/100000 and z.imag<arb(hi)/1000-arb(1)/100000
        grad=[((2*arb.pi()*ii*sc+(1-X*u).log()-(1-X).log())*dx).real,
              ((2*arb.pi()*ii*tc+(1-Y*v).log()-(1-Y).log())*dy).real]
        lo=action(sc0,tc0,Xc,Yc).real-sum(w*boundabs(d)for w,d in zip(widths,grad))
        assert lo>-arb(1)/10,(domain,box,lo)
        return
    if kind=='exterior':
        intervals=[(R(0),R(1,40),R(1,40)),(R(1,40),R(23,100),R(0)),(R(9,20),R(9,20),R(0))]
        left,right,low=intervals[domain[3]];ds=real(right-left)
        s=real(left)+ds*p[2];t=real(low)+(arb(99)/100-s-real(low))*p[3]
        s0=real(left)+ds*c[2];t0=real(low)+(arb(99)/100-s0-real(low))*c[3]
        ds2,dt2=ds,-ds*p[3];ds3,dt3=0,arb(99)/100-s-real(low)
        if domain[4]:
            s,t,s0,t0=t,s,t0,s0
            ds2,dt2,ds3,dt3=dt2,ds2,dt3,ds3
        target=arb(1)/250
    else:
        j,k=domain[3:5];s,ds2=sides(family,patch,0,j,p[2]);t,dt3=sides(family,patch,1,k,p[3])
        s0,_=sides(family,patch,0,j,c[2]);t0,_=sides(family,patch,1,k,c[3]);dt2=ds3=0
        target=arb(1)/1000 if j<2 or k<2 else -arb(1)/50
    es=(-2*arb.pi()*ii*s).exp();et=(-2*arb.pi()*ii*t).exp()
    fs=X.log()+(1-es*et).log()-(1-X*es).log()
    ft=Y.log()+(1-es*et).log()-(1-Y*et).log()
    grad=[((2*arb.pi()*ii*(sc-s)+(1-X*u).log()-(1-X*es).log())*dx).real,
          ((2*arb.pi()*ii*(tc-t)+(1-Y*v).log()-(1-Y*et).log())*dy).real,
          (-fs*ds2-ft*dt2).real,(-fs*ds3-ft*dt3).real]
    lo=(action(sc0,tc0,Xc,Yc)-action(s0,t0,Xc,Yc)).real
    lo-=sum(w*boundabs(d)for w,d in zip(widths,grad))
    assert lo>target,(domain,box,lo,target)


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
    ap=argparse.ArgumentParser();ap.add_argument('artifact',nargs='?',default='repro/results/research-three-vertex-real-input-union.json')
    ap.add_argument('--precision',type=int,default=192)
    ap.add_argument('--output',default='repro/results/research-three-vertex-real-input-union-replay.json')
    args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic()
    source=ROOT/args.artifact;data=json.loads(source.read_text());assert data['status']=='passed'
    assert data['input_real_radius']=='1/50' and data['output_disk_radius']=='1/200' and data['output_real_radius']=='9/1000' and data['deleted_corner_fraction']=='1/40'
    assert data['index_heights_millesimal']=={k:[list(row)for row in v]for k,v in HEIGHTS.items()}
    expected={('geometry',):3}
    for family,patch in product(('disk','real'),range(8)):
        expected[('floor',family,patch)]=2
        for r,flip in product(range(3),range(2)):expected[('exterior',family,patch,r,flip)]=4
        for j,k in product(range(4),repeat=2):expected[('contour',family,patch,j,k)]=4
    seen=set();count=0
    for item in data['domains']:
        key=tuple(item['domain']);assert key in expected and key not in seen
        seen.add(key);assert item['dimension']==expected[key]
        for box in partition(item['leaves'],item['dimension']):check(key,box);count+=1
    assert seen==set(expected) and count==data['leaf_count']
    # Independent scalar enclosures used in the analytic top/high-index reductions.
    r=arb(27)/50;p=arb.pi()
    values=[r-arb(1)/2*(p/100).exp(),-arb(3)/5-r.log(),
            arb(2)/3-r-r*r/4-r**3/(9*(1-r)),arb(10)/3-arb(25).log(),
            -arb(1)/10+arb(3)/5*arb(99)/100-arb(4)/9-arb(13)/300-arb(1)/200,
            (1+r*r).sqrt()-2*r,1-r-2*r*11*p/100,
            -p/2-2*p*(arb(1)/6+arb(1)/50-arb(9)/20),
            2*p*(arb(1)/6-arb(1)/50-arb(89)/100)+3*p/2,
            2*p*arb(6)/1000-arb(1)/50-arb(1)/100,
            1-r*(2*p*arb(29)/1000).exp(),
            arb(3)/2-(arb(2).log()+68*p/1000).cosh(),
            p*(13*p/150).sin()/(arb(3)/2-(13*p/150).cos())-arb(3)/2,
            p*(91*p/150).sin()/(arb(3)/2-(91*p/150).cos())-arb(3)/2,
            arb(2)/5-p*(p/25).tan()]
    assert all(z>0 for z in values)
    for name,digest in data['dependencies_sha256'].items():assert sha256((ROOT/name).read_bytes()).hexdigest()==digest,name
    assert sha256((ROOT/'experiments/certify_three_vertex_real_input_union.py').read_bytes()).hexdigest()==data['script_sha256']
    result={'status':'passed','precision_bits':args.precision,'domain_count':len(seen),
            'leaf_count':count,'exact_partition_cover':True,'scalar_checks':len(values),
            'phase':'Independent negative-frequency dilogarithm primitive',
            'artifact_sha256':sha256(source.read_bytes()).hexdigest(),
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'elapsed_seconds':time.monotonic()-start}
    (ROOT/args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
