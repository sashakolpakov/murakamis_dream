#!/usr/bin/env python3
"""Independent original-phase replay of the wider real-output currents."""
from fractions import Fraction as Q
from pathlib import Path
from itertools import product
from hashlib import sha256
import argparse,json,time
from flint import arb,acb,ctx
from replay_three_prepared_central_currents import value_gradient

ROOT=Path(__file__).resolve().parents[1];I=acb(0,1)
B=[(Q(7,50),Q(1,5)),(Q(0),Q(9,5)),(Q(1,4),Q(9,20)),
   (Q(1,4),Q(9,20)),(Q(11,75),Q(14,75))]
H=list(map(Q,['.10135869','-.97895510','.00300831','-.00629803']))

def r(x):
    x=Q(x);return arb(x.numerator)/x.denominator

def envelope(point,which,xi=None,eta=None):
    p=arb.pi();s,t=map(r,point)
    h=r('.10135867').union(r('.10135871'))if which==0 else arb(2).log()/(2*p)
    R=(-2*p*h).exp();T=arb(1)/2
    J=(-2*p*I*(s+t)).exp().polylog(2).imag/(2*p)
    def denominator(z,rad,phase):
        if phase is None:
            term=(rad*(-p*I*z).exp()).polylog(2).imag/p
            grad=abs(1-rad*(-p*I*z).exp()).log()
        else:
            Z=rad*(-2*p*I*r(phase)).exp();U=(2*p*I*z).exp()
            term=-((Z*U).polylog(2)-Z.polylog(2)).imag/(2*p)
            grad=abs(1-Z*U).log()
        return term,grad
    dx,gx=denominator(s,R,xi);dy,gy=denominator(t,T,eta)
    value=-(R*T).log()/2+J+s*R.log()+t*T.log()-dx-dy
    common=(2*(p*(s+t)).sin()).log()
    return value,[common+R.log()-gx,common+T.log()-gy]

def real_critical():
    path=ROOT/'repro/results/research-three-prepared-cap-real-critical.json'
    data=json.loads(path.read_text());assert data['status']=='passed'
    cover=sorted((Q(c['output_interval'][0]),Q(c['output_interval'][1]))for c in data['cells'])
    assert len(cover)==data['cell_count']and cover[0][0]==-Q(1,50)and cover[-1][1]==Q(1,50)
    assert all(a<b for a,b in cover)and all(a[1]==b[0]for a,b in zip(cover,cover[1:]))
    for cell in data['cells']:
        z=[acb(arb(a),arb(b))for a,b in cell['coordinate_parts']]
        x,tau,s,t=z
        assert x.real>r(Q(7,50))and x.real<r(Q(1,5))
        assert x.imag>r(Q(9,100))and x.imag<r(Q(3,25))
        assert tau.real>0 and tau.real<r(Q(31,20))
        assert tau.imag>-1 and tau.imag<-r(Q(97,100))
        assert all(w.real>r(Q(1,4))and w.real<r(Q(9,20))and abs(w.imag)<r(Q(3,100))for w in(s,t))
    return data

def gradient_complex(point,heights):
    p=arb.pi();x,tau,s,t=[acb(r(point[j]),heights[j])for j in range(4)]
    y=acb(r(point[4]),arb(2).log()/(2*p))
    X=(2*p*I*x).exp();Y=(2*p*I*y).exp();U=(-2*p*I*s).exp();V=(-2*p*I*t).exp()
    lplus=(p*x+tau/2).cos().log();lminus=(p*x-tau/2).cos().log()
    gx=lplus+lminus-2*(p*x).sin().log()+2*p*I*s+(1-X*U).log()-(1-X).log()-p*I
    gtau=(lplus-lminus)/(2*p)-(tau/2).tan().asinh()/p+3*I*tau/(2*p)-I
    gs=X.log()+(1-U*V).log()-(1-X*U).log()
    gt=Y.log()+(1-U*V).log()-(1-Y*V).log()
    gy=2*p*I*t+(1-Y*V).log()-(1-Y).log()-p*I
    return [gx,gtau,gs,gt,gy]

def height_value_gradient(point,heights):
    # The frozen independent primitive expects exact rational heights.
    # Choose an interior dyadic midpoint and retain its exact rounding
    # error in the full height difference, independently at replay precision.
    mids=[]
    for h in heights:
        a,b=h.mid().fmpq().p,h.mid().fmpq().q
        mids.append(Q(int(a),int(b)))
    value,_=value_gradient(point,mids+[Q(0)])
    g=gradient_complex(point,heights)
    value+=sum(abs(gj.imag).upper()*abs(h-r(m)).upper()for gj,h,m in zip(g,heights,mids))
    return value,[z.real for z in g]

def expected():
    for axis,end,hs,ht in product((2,3),(0,1),(-Q(1,125),Q(1,125)),(-Q(17,1000),Q(3,250))):
        h=H[:];h[2]=hs;h[3]=ht;b=B[:];b[axis]=(b[axis][end],)*2
        yield ('index_side',axis,end,str(hs),str(ht)),b,Q(19107,10000),('joint',h+[Q(0)])
    for hs,ht in product((-Q(1,125),Q(1,125)),(-Q(17,1000),Q(3,250))):
        h=H[:];h[2]=hs;h[3]=ht
        yield ('alias',str(hs),str(ht)),B,Q(39,20),('joint',h+[Q(0)])
    for axis,end in product(range(4),(0,1)):
        b=B[:];b[axis]=(b[axis][end],)*2
        yield ('initial_face',axis,end),b,Q(19107,10000),('joint',H+[Q(0)])
    for which,axis,end in product(range(2),range(2),range(2)):
        cut=Q(1,4)if end==0 else Q(9,20);b=[(Q(1,2)-cut,1-cut)]*2;b[axis]=(cut,cut)
        yield ('real_index_complement',which,axis,end),b,Q(16,25),('envelope',which,None,None)
    for which,xi in product(range(2),(Q(7,50),Q(1,5))):
        yield ('wire_join',which,str(xi)),[(Q(1,4),Q(9,20))]*2,Q(6459,10000),('envelope',which,xi,None)
    for cut in (Q(22,75),Q(28,75)):
        yield ('far_output_index',str(cut)),[(Q(1,2)-cut,1-cut),(cut,cut)],Q(6465,10000),('envelope',0,None,None)
    for eta in (Q(11,75),Q(14,75)):
        yield ('far_output_phase',str(eta)),[(Q(1,4),Q(9,20)),(Q(22,75),Q(28,75))],Q(6465,10000),('envelope',0,None,eta)
    critical=real_critical()
    for j,cell in enumerate(critical['cells']):
        a,b=map(Q,cell['output_interval']);heights=[arb(z[1])for z in cell['coordinate_parts']]
        for axis,end in product(range(4),(0,1)):
            box=B[:];box[4]=(Q(1,6)+a,Q(1,6)+b);box[axis]=(box[axis][end],)*2
            yield ('critical_face',j,axis,end),box,Q(19107,10000),('height',heights)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=192)
    ap.add_argument('--output',default='repro/results/research-three-prepared-real-output-currents-replay.json')
    args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic()
    path=ROOT/'repro/results/research-three-prepared-real-output-currents.json';data=json.loads(path.read_text())
    assert data['status']=='passed';wanted={key:(b,t,mode)for key,b,t,mode in expected()};seen=set()
    for item in data['domains']:
        key=tuple(item['domain']);assert key in wanted and key not in seen;seen.add(key)
        b,target,mode=wanted[key]
        assert [[Q(v)for v in row]for row in item['bounds']]==[list(z)for z in b]
        assert Q(item['threshold'])==target
        z=list(map(Q,item['support_point']));assert len(z)==len(b)and all(a<=v<=c for v,(a,c)in zip(z,b))
        if mode[0]=='joint':
            assert list(map(Q,item['heights']))==mode[1]
            value,g=value_gradient(z,mode[1])
        elif mode[0]=='height':
            assert len(item['height_enclosures'])==4
            assert all(arb(text).contains(h)for text,h in zip(item['height_enclosures'],mode[1]))
            value,g=height_value_gradient(z,mode[1])
        else:value,g=envelope(z,*mode[1:])
        upper=value+sum(max((gj*r(a-v)).upper(),(gj*r(c-v)).upper())for gj,v,(a,c)in zip(g,z,b))
        assert upper<r(target),(key,upper,target)
    assert seen==set(wanted)and len(seen)==44+8*data['critical_cell_count']
    checks=[r(Q(16,25)-Q(347,500)+Q(7,100)-Q(3,250)),
            r(Q(19107,10000)-Q(126465,100000)-Q(16,25)),
            r(Q(19107,10000)-Q(63,50)-Q(64699,100000)),
            r(Q(19107,10000)-Q(6319,5000)-Q(6459,10000)),
            r(Q(19107,10000)-Q(158,125)-2*Q(161533,500000)),
            r(Q(191116,100000)-Q(126465,100000)-Q(6465,10000)),
            r(Q(19107,10000)-Q(39,20))+2*arb.pi()/125]
    assert all(v>0 for v in checks)
    for f,h in data['dependencies_sha256'].items():assert sha256((ROOT/f).read_bytes()).hexdigest()==h,f
    assert sha256((ROOT/'experiments/certify_three_prepared_real_output_currents.py').read_bytes()).hexdigest()==data['script_sha256']
    result={'status':'passed','precision_bits':args.precision,'support_planes':len(seen),
            'exact_domain_list':True,'scalar_checks':len(checks),'elapsed_seconds':time.monotonic()-start,
            'scope':data['scope'],'artifact_sha256':sha256(path.read_bytes()).hexdigest(),
            'critical_cells_checked':data['critical_cell_count'],
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'independent_helper_sha256':sha256((ROOT/'experiments/replay_three_prepared_central_currents.py').read_bytes()).hexdigest(),
            'method':'Independent negative-frequency primitives and real logarithmic gradients; exact domain enumeration; no author imports or optimizer.'}
    (ROOT/args.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':main()
