#!/usr/bin/env python3
"""Independent positive-frequency replay of the original power-four index currents.

No author implementation is imported. Every encoded binary tree is checked
for exact rectangle coverage before the alternative phase/gradient bounds.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import argparse,json,time
from flint import arb,acb,ctx

ROOT=Path(__file__).resolve().parents[1]
I=acb(0,1)
A,B,HMIN,HMAX=Q(1,5),Q(21,50),Q(-11,200),Q(3,200)

def ar(x):
    return arb(x.numerator)/x.denominator if isinstance(x,Q) else arb(x)
def iv(a,b):return ar(a).union(ar(b))
def au(x):return max(abs(x.lower()),abs(x.upper()))
def digest(path):return sha256(path.read_bytes()).hexdigest()
def verified_record(rel,script):
    p=ROOT/rel;d=json.loads(p.read_text());assert d['status']=='passed',rel
    assert d['script_sha256']==digest(ROOT/script),script
    for dep,h in d['dependencies_sha256'].items():assert digest(ROOT/dep)==h,dep
    return d

def j(z):
    """Sine primitive continued from (0,1), using positive frequencies."""
    p=arb.pi()
    return -I*p*(z*z-z)/2+I*(2*p*I*z).exp().polylog(2)/(2*p)-I*p/12

def primitive(z,K):
    return ((K*(-2*arb.pi()*I*z).exp()).polylog(2)-K.polylog(2))/(2*arb.pi()*I)
def phase(s,t,K):
    return j(s+t)-j(s)-j(t)-I*arb.pi()*s*t+(s+t)*K.log()-primitive(s,K)-primitive(t,K)
def gradient(s,t,K):
    p=arb.pi();base=(2*(p*(s+t)).sin()).log()+K.log()
    return (base-(2*(p*s).sin()).log()-I*p*t-(1-K*(-2*p*I*s).exp()).log(),
            base-(2*(p*t).sin()).log()-I*p*s-(1-K*(-2*p*I*t).exp()).log())
def side(k,u):
    if k in (0,1):return acb(ar(A if k==0 else B),ar(HMIN)+ar(HMAX-HMIN)*u),I*ar(HMAX-HMIN)
    return acb(ar(A)+ar(B-A)*u,ar(HMIN if k==2 else HMAX)),acb(ar(B-A))

def tree_boxes(paths):
    assert len(paths)==len(set(paths)) and paths
    def visit(words,box):
        if '' in words:
            assert len(words)==1,'A leaf is also an ancestor'
            yield box;return
        heads={w[0] for w in words};assert all(c in '0123' for c in heads)
        axes={int(c)//2 for c in heads};assert len(axes)==1,'Inconsistent split axes'
        axis=next(iter(axes));assert heads=={str(2*axis),str(2*axis+1)},'Missing child'
        a,b=box[axis];m=(a+b)/2
        for bit,ends in ((0,(a,m)),(1,(m,b))):
            head=str(2*axis+bit);child=list(box);child[axis]=ends
            yield from visit([w[1:] for w in words if w[0]==head],tuple(child))
    yield from visit(paths,((Q(0),Q(1)),(Q(0),Q(1))))

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision',type=int,default=320)
    ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-power-four-index-contours-replay.json')
    args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic()
    record_path='repro/results/research-power-four-index-contours.json'
    rec=verified_record(record_path,'experiments/certify_power_four_index_contours.py')
    original_artifact_sha256=digest(ROOT/record_path)
    ref=verified_record('repro/results/research-three-four-source-interface.json','experiments/check_three_four_source_interface.py')
    real=verified_record('repro/results/research-power-four-real-complement.json','experiments/check_power_four_real_complement.py')
    for key in ('reference','real_complement_input'):
        assert rec[key]['sha256']==digest(ROOT/rec[key]['record'])
    assert rec['index_rectangle']=={'real':[str(A),str(B)],'imaginary':[str(HMIN),str(HMAX)]}
    assert rec['vertical_product_gap']=='1/200' and rec['horizontal_product_excess']=='1/25'
    cr,ci=map(Q,ref['root_certificate']['center']);radius=ar(Q(ref['root_certificate']['complex_disk_radius']))
    a=acb(ar(cr)+arb(0,radius),ar(ci)+arb(0,radius))
    b=a*a*(2*a-1)**2/(2*(a-1));k=a*a*b/(a*a+b)
    # Algebraic exp(2 pi i asin sqrt k), rather than the author's inverse sine.
    K=1-2*k+2*I*k.sqrt()*(1-k).sqrt();p=arb.pi()
    x=K.log()/(2*p*I);Z=2*K/(1-K);z=Z.log()/(2*p*I)
    fc=phase(z,z,K).real;scalars={}
    def pos(name,value):assert value>0,(name,str(value));scalars[name]=str(value)
    pos('K argument lower',K.arg()-p/5);pos('K argument upper',2*p/5-K.arg())
    pos('denominator radius',ar(Q(7,10))-abs(K)*(2*p*ar(HMAX)).exp())
    pos('critical real lower',z.real-ar(A));pos('critical real upper',ar(B)-z.real)
    pos('critical lower height',z.imag-ar(HMIN));pos('critical upper height',ar(HMAX)-z.imag)
    gs,gt=gradient(z,z,K)
    pos('actual logarithmic lift s',p-abs(gs.imag));pos('actual logarithmic lift t',p-abs(gt.imag))
    assert gs.contains(0) and gt.contains(0),'Calibrated gradients do not contain zero'
    pos('original action',(phase(z,z,K)-2*p*I*x).real-ar(Q(4281,5000)))
    pos('sine lower',(2*p/5).sin()-ar(Q(19,20)))
    pos('hyperbolic numerator',ar(Q(9,25))-(11*p/100).sinh())
    pos('small cot upper',ar(Q(7,5))-1/(p/5).tan())
    pos('small cot lower',(2*p/5).sin()/((11*p/100).cosh()+(2*p/5).cos())-ar(Q(2,3)))
    pos('global cot lower',(21*p/25).sin()/((11*p/100).cosh()-(21*p/25).cos())-ar(Q(6,25)))
    gamma,zeta=ar(Q(36,95)),ar(Q(252,475));delta=(1-zeta*zeta)/(ar(Q(14,5))*(1+gamma*gamma))
    pos('positive C Hessian',p*delta-ar(Q(1,4)));pos('negative C Hessian',6*p/25-ar(Q(1,4)))
    pos('alias reserve',2*p*ar(HMAX)-ar(Q(1,25))-ar(Q(1,20)))
    seen=set();original=accepted=visited=0;minmargin=None
    for domain in rec['domains']:
        sk,tk=domain['s_side'],domain['t_side'];key=(sk,tk)
        assert key in {(j,k)for j in range(4)for k in range(4)} and key not in seen;seen.add(key)
        threshold=ar(Q(1,200) if min(sk,tk)<2 else Q(-1,25))
        for box in tree_boxes(domain['leaves']):
            original+=1;todo=[box]
            while todo:
                current=todo.pop();visited+=1
                values=[iv(a,b)for a,b in current];centers=[ar((a+b)/2)for a,b in current];radii=[ar((b-a)/2)for a,b in current]
                s,ds=side(sk,values[0]);t,dt=side(tk,values[1]);sm,_=side(sk,centers[0]);tm,_=side(tk,centers[1])
                fs,ft=gradient(s,t,K);costs=[radii[0]*au((fs*ds).real),radii[1]*au((ft*dt).real)]
                margin=fc-phase(sm,tm,K).real-sum(costs)-threshold
                if margin>0:
                    accepted+=1
                    if minmargin is None or margin.lower()<minmargin:minmargin=margin.lower()
                    continue
                axis=max(range(2),key=lambda j:float(costs[j].upper()))
                a0,b0=current[axis];assert b0-a0>Q(1,2**28),(key,current,'unproved')
                mid=(a0+b0)/2
                for ends in ((a0,mid),(mid,b0)):
                    child=list(current);child[axis]=ends;todo.append(tuple(child))
                assert visited<100000,'Replay budget exhausted without certificate'
        print('completed',key,'accepted',accepted,flush=True)
    assert len(seen)==16==rec['domain_count'] and original==rec['leaf_count']
    # Recheck provenance at the end: concurrent edits cannot produce a stale pass.
    verified_record(record_path,'experiments/certify_power_four_index_contours.py')
    assert digest(ROOT/record_path)==original_artifact_sha256,'Author artifact changed during replay'
    result={'status':'passed','precision_bits':args.precision,'domain_count':len(seen),
            'original_leaf_count':original,'replayed_leaf_count':accepted,'visited':visited,
            'strict_scalar_comparisons':len(scalars),'scalar_margins':scalars,
            'smallest_leaf_margin':str(minmargin),'exact_binary_cover':True,
            'critical_action':str((phase(z,z,K)-2*p*I*x).real),
            'phase':'Positive-frequency sine primitive with direct sine-log gradients; algebraic wire exponential. No author imports.',
            'elapsed_seconds':time.monotonic()-start,'script_sha256':digest(Path(__file__)),
            'artifact_sha256':digest(ROOT/record_path),'author_script_sha256':rec['script_sha256'],
            'dependencies_sha256':{key:digest(ROOT/key)for key in rec['dependencies_sha256']},
            'reference_artifacts_sha256':{rec[key]['record']:digest(ROOT/rec[key]['record'])for key in ('reference','real_complement_input')},
            'replay_command':f'python3 experiments/replay_power_four_index_contours.py --precision {args.precision} --output {args.output}'}
    args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k]for k in ('status','domain_count','original_leaf_count','replayed_leaf_count','strict_scalar_comparisons','elapsed_seconds')}))
if __name__=='__main__':main()
