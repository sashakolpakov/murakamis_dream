#!/usr/bin/env python3
"""Original cap currents at the initial height of the direct three-chain contour.

The nine domains cover the original cap pieces. Additional scalar checks
verify the analytic global real-index complement and assembly margins.
The central-current certificate is checked as an explicit dependency.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import argparse,json,time
from flint import arb,acb,ctx
from certify_three_cap_wire_complement import jreal as original_jreal
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
    hc=yh
    ht=arb(24961509)/25000000
    return pi,yh,hc,ht
def domains():
    yield ('capcentral',),2
    for k in range(6):yield ('capcontour',k),2
    yield ('captail',),1;yield ('capradical',),1
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
def evaluate(key,box):
    p=[interval(a,b)for a,b in box];c=[rat((a+b)/2)for a,b in box];r=[rat((b-a)/2)for a,b in box]
    if key[0].startswith('cap'):
        direct=cap_value(key,p);costs=None
        threshold=arb(1267)/1000 if key[0]=='capcentral'else(arb(2)/3 if key[0]=='capradical'else arb(63)/50)
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
def scalar_checks():
    pi,yh,hc,ht=constants();cc=arb(161533)/500000;checks=[]
    def pos(name,value):
        assert value>0,(name,value)
        checks.append({'name':name,'positive_margin':str(value)})
    pos('initial wire above .09',yh-arb(9)/100)
    pos('initial wire below .12',arb(3)/25-yh)
    pos('initial angular height above .97',ht-arb(97)/100)
    pos('initial angular height below 1',1-ht)
    pos('angular-cut color real part below 2',2+2*(arb(41)/20).cos()*ht.cosh())
    pos('small-zero primitive estimate',arb(1)/200-((pi/20).sinh()/(pi/20)-1))
    # Global real-index envelope at both radii1/2. These are analytic
    # three-case premises, not sampled maximization.
    eps=arb(1)/40
    pos('small-sum first endpoint below .623',arb(623)/1000-arb(2).log()-eps*((2*pi*eps).log()-1))
    pos('small-sum second endpoint below .623',arb(623)/1000-arb(2).log()+arb(8)/75)
    pos('increasing smaller index for sum in[1/3,1/2]',(pi/3).sin()**2-(arb(5)/4-(pi/4).cos()))
    dd=pi*(arb(9)*pi/20).sin()/(arb(5)/2-2*(arb(9)*pi/20).cos())
    pos('index curvature greater than7/5',dd-arb(7)/5)
    pos('index curvature decreasing on[1/4,9/20]',arb(4)/5-(pi/4).cos())
    pos('real-index complement below .6413',arb(6413)/10000-2*cc+arb(7)/1440)
    pos('small-sum bound below .6413',arb(6413)/10000-arb(623)/1000)
    M=arb(63519)/20000
    pos('one exterior source loss above1/4000',M-arb(158)/125-arb(38233)/20000-arb(1)/4000)
    pos('double exterior loss above1/1000',M-2*arb(158)/125-2*cc-arb(1)/1000)
    pos('Fourier corner in one exterior below action',M-arb(158)/125-arb(343)/200)
    pos('real-index complement loss above3/5000',M-2*arb(1267)/1000-arb(6413)/10000-arb(3)/5000)
    pos('one angular remainder loss above1/1000',M-arb(63)/50-arb(957)/500-arb(1)/1000)
    pos('two angular remainders loss above1/200',M-2*arb(63)/50-2*cc-arb(1)/200)
    pos('index side loss above1/200',M-arb(317)/100-arb(1)/200)
    pos('index alias below3.12',arb(78)/25-arb(1591)/500+pi/50)
    pos('initial Stokes face loss above1/1000',M-arb(1587)/500-arb(1)/1000)
    pos('ordinary-boundary corner below3',3-5*cc-arb(550)/471-arb(27)/200)
    return checks
def central_provenance():
    base='research-three-chain-three-central-currents'
    author_path=ROOT/f'repro/results/{base}.json'
    replay_path=ROOT/f'repro/results/{base}-replay.json'
    author=json.loads(author_path.read_text()); replay=json.loads(replay_path.read_text())
    assert author['status']==replay['status']=='passed'
    assert author['support_plane_count']==replay['support_plane_count']==28
    assert replay['exact_domain_cover'] is True
    assert replay['artifact_sha256']==sha256(author_path.read_bytes()).hexdigest()
    for record,script in ((author,'check_three_chain_three_central_currents.py'),
                          (replay,'replay_three_chain_three_central_currents.py')):
        assert record['script_sha256']==sha256((ROOT/'experiments'/script).read_bytes()).hexdigest()
        for path,digest in record['dependencies_sha256'].items():
            assert sha256((ROOT/path).read_bytes()).hexdigest()==digest,path
    return [str(author_path.relative_to(ROOT)),str(replay_path.relative_to(ROOT))]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=160)
    ap.add_argument('--output',default='repro/results/research-three-chain-three-complements.json')
    args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic();checks=scalar_checks();provenance=central_provenance();saved=[];visits=0
    for key,dim in domains():
        todo=[('',tuple((Q(0),Q(1))for _ in range(dim)))];leaves=[]
        while todo:
            path,box=todo.pop();visits+=1
            try:passed,costs,v=evaluate(key,box)
            except (ValueError,ZeroDivisionError):passed,costs,v=False,None,None
            if passed:leaves.append(path);continue
            if costs is not None and all(z.is_finite()for z in costs):axis=max(range(dim),key=lambda k:float(costs[k]))
            else:
                weights=[.06,2]
                axis=max(range(dim),key=lambda k:float(box[k][1]-box[k][0])*weights[k])
            a,b=box[axis];assert b-a>Q(1,2**25),('unproved',key,box,v);mid=(a+b)/2
            for side,ends in enumerate(((a,mid),(mid,b))):
                child=list(box);child[axis]=ends;todo.append((path+str(2*axis+side),tuple(child)))
            assert visits<600000,'Coverage unfinished; no certificate saved.'
        saved.append({'domain':list(key),'dimension':dim,'leaves':leaves});print(key,len(leaves),visits,flush=True)
    deps=['experiments/certify_three_cap_wire_complement.py',
          'notes/research_three_cap_wire_complement.md',
          'notes/research_three_vertex_global_wire_bound.md',
          'notes/research_three_vertex_joint_concavity.md',
          'notes/research_three_prepared_cap_period_bound.md',
          'notes/research_three_chain_three_closure.md',
          'notes/research_three_chain_fourier_corner_transfer.md',
          'notes/research_three_chain_three_central_currents.md',
          'notes/research_three_chain_outside_boundary_decay.md',
          'notes/research_free_boundary_half_charge_observation.md',
          'notes/research_pair_free_boundary_kernel.md']+provenance
    result={'status':'passed','precision_bits':args.precision,'domain_count':len(saved),'domains':saved,
            'leaf_count':sum(len(d['leaves'])for d in saved),'visited':visits,'scalar_checks':checks,
            'checked_central_provenance_records':len(provenance),
            'elapsed_seconds':time.monotonic()-start,'scope':'Original cap at wire height log(2)/(2pi), angular depth24961509/25000000; complete real-index complement scalar premises and direct three-chain budgets. Central joint currents have a separate certificate.',
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest()for p in deps}}
    path=ROOT/args.output;path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k]for k in ('status','domain_count','leaf_count','visited','elapsed_seconds')}))
if __name__=='__main__':main()
