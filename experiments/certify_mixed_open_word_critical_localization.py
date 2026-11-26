#!/usr/bin/env python3
"""Four original-log endpoint disk maps and the two one-vertex roots.

Saved mode checks the exact complete trees and supplied Newton witnesses,
without proposing roots. This proves critical geometry, not a source packet.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

from flint import acb, acb_mat, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/'notes/research_mixed_open_word_critical_localization.md'
DISKS = [(F(7,20),-F(1,100),F(9,100)),
         (F(3,10),-F(13,250),F(8,125))]

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def ar(x):
    x=F(x)
    return arb(x.numerator)/x.denominator

def cp(v):
    return acb(ar(v[0]),ar(v[1]))

def ident(n):
    return acb_mat([[int(i==j) for j in range(n)] for i in range(n)])

def jp(z):
    return (2*(arb.pi()*z).sin()).log()

def cot(z):
    return (arb.pi()*z).cot()

def equation(z,b,eps,one=False):
    pi,ii=arb.pi(),acb(0,1)
    if one:
        e,u=z;t=e
    else:
        e,t,u=z
    fe=-jp(e-u)+jp(e+t)-eps*jp(e)+ii*pi*(u-t+eps*(e-ar('1/2')))
    fu=2*(pi*u).cos().log()+(pi*(e-u)).sin().log()-3*(pi*u).sin().log()+ii*pi*e
    if one:
        return acb_mat([[fe],[fu]])
    ft=jp(e+t)+jp(t+b)-(2+eps)*jp(t)+ii*pi*(b-e+eps*(t-ar('1/2')))
    return acb_mat([[fe],[ft],[fu]])

def jacobian(z,b,eps,one=False):
    pi,ii=arb.pi(),acb(0,1)
    if one:
        e,u=z;t=e
    else:
        e,t,u=z
    a=pi*(2*(pi*u).tan()+3*cot(u))
    bb=pi*cot(e-u);c=pi*cot(e+t)
    ee=-bb+c-eps*pi*cot(e)+ii*pi*eps
    eu=bb+ii*pi
    if one:
        return acb_mat([[ee+c-ii*pi,eu],[eu,-a-bb]])
    tt=c+pi*cot(t+b)-(2+eps)*pi*cot(t)+ii*pi*eps
    return acb_mat([[ee,c-ii*pi,eu],[c-ii*pi,tt,0],[eu,0,-a-bb]])

def parameter(box,neighbor):
    cr,ci,r=DISKS[neighbor]
    return acb(ar(cr)+ar(r)*ar(box[0][0]).union(ar(box[0][1])),
               ar(ci)+ar(r)*ar(box[1][0]).union(ar(box[1][1])))

def excluded(box):
    return sum(min(abs(a),abs(b))**2 if a*b>0 else F(0) for a,b in box)>1

def propose(b,eps,one=False):
    import numpy as np
    from scipy.optimize import root
    def jp0(z):return np.log(2*np.sin(np.pi*z))
    def fun(v):
        n=len(v)//2;z=v[:n]+1j*v[n:]
        if one:e,u=z;t=e
        else:e,t,u=z
        fe=-jp0(e-u)+jp0(e+t)-eps*jp0(e)+1j*np.pi*(u-t+eps*(e-.5))
        fu=2*np.log(np.cos(np.pi*u))+np.log(np.sin(np.pi*(e-u)))-3*np.log(np.sin(np.pi*u))+1j*np.pi*e
        vals=[fe,fu] if one else [fe,jp0(e+t)+jp0(t+b)-(2+eps)*jp0(t)+1j*np.pi*(b-e+eps*(t-.5)),fu]
        vals=np.array(vals);return np.r_[vals.real,vals.imag]
    z=np.array([.40-.01j if not eps else .35-.045j,.23+.05j] if one else [.41+.01j if not eps else .35-.035j,complex(float(DISKS[eps][0]),float(DISKS[eps][1])),.23+.05j])
    result=root(fun,np.r_[z.real,z.imag],tol=1e-11)
    assert max(abs(fun(result.x)))<1e-8
    n=len(z);z=result.x[:n]+1j*result.x[n:]
    centers=[[format(v.real,'.17g'),format(v.imag,'.17g')] for v in z]
    zz=list(map(cp,centers));bp=acb(str(b.real),str(b.imag))
    inverse=jacobian(zz,bp,eps,one).inv()
    # Round-to-nearest doubles solely propose rational Y entries.
    Y=[[[format(float(inverse[i,j].real.mid()),'.17g'),format(float(inverse[i,j].imag.mid()),'.17g')] for j in range(n)] for i in range(n)]
    return {'centers':centers,'inverse':Y}

def test(w,b,eps,one=False):
    n=2 if one else 3
    assert len(w['centers'])==n and len(w['inverse'])==n
    assert all(len(v)==2 for v in w['centers'])
    assert all(len(row)==n for row in w['inverse'])
    assert all(len(v)==2 for row in w['inverse'] for v in row)
    z0=list(map(cp,w['centers']));Y=acb_mat([[cp(v) for v in row] for row in w['inverse']])
    radius=ar(w['radius'])
    assert radius>0
    z=[v+acb(arb(0,radius),arb(0,radius)) for v in z0]
    J=jacobian(z,b,eps,one)
    if any(not J[i,j].is_finite() for i in range(n) for j in range(n)):
        return None
    error=ident(n)-Y*J
    residual=Y*equation(z0,b,eps,one)
    if not all(abs(residual[i,0])+radius*sum(abs(error[i,j]) for j in range(n))<radius for i in range(n)):
        return None
    if not abs(Y.det())>0:return None
    if one:e,u=z;t=e
    else:e,t,u=z
    if not (ar('.33')<e.real<ar('.47') and ar('-.09')<e.imag<ar('.08')):return None
    if not (ar('.21')<u.real<ar('.25') and ar('.01')<u.imag<ar('.10')):return None
    if not one:
        cr,ci,r=DISKS[eps]
        # The unknown is in a complex disk, not its derivative square.
        tm=z0[1]
        if not abs(tm-acb(ar(cr),ar(ci)))+radius<ar(r):return None
        if not (ar('.23')<t.real<ar('.45') and ar('-.12')<t.imag<ar('.12')):return None
    if not all(0<v.real<1 for v in [e-u,e+t,e,t,u]):return None
    if not one and not 0<(t+b).real<1:return None
    if not 0<u.real<ar('1/2'):return None
    # Exact complete-end quadratic plus original residual <pi selects its
    # zero lift; scalar strict accretivity identifies it with this u.
    pi,ii=arb.pi(),acb(0,1)
    uc=((ii+(1-2*(2*pi*ii*e).exp()).sqrt())/2).atan()/pi
    if not (0<uc.real<ar('1/2') and 0<(e-uc).real<ar('1/2')):return None
    fuc=2*(pi*uc).cos().log()+(pi*(e-uc)).sin().log()-3*(pi*uc).sin().log()+ii*pi*e
    if not abs(fuc)<pi:return None
    return {name:[[str(v.real.lower()),str(v.real.upper())],[str(v.imag.lower()),str(v.imag.upper())]] for name,v in [('e',e),('u',u)]+([] if one else [('t',t)])}

def split(box,j):
    a,b=box[j];m=(a+b)/2
    left=list(box);right=list(box)
    left[j]=(a,m);right[j]=(m,b)
    return left,right

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision',type=int,default=256)
    ap.add_argument('--input',type=Path)
    ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-open-word-critical-localization.json')
    ap.add_argument('--max-visits',type=int,default=20000)
    ap.add_argument('--max-seconds',type=float,default=120)
    args=ap.parse_args();ctx.prec=args.precision
    ph,sh=sha(PROOF),sha(__file__);start=time.monotonic()
    old=None;input_hash=None
    if args.input:
        raw=args.input.read_bytes();input_hash=hashlib.sha256(raw).hexdigest();old=json.loads(raw)
        assert old['status']=='passed' and old['proof_sha256']==ph and old['script_sha256']==sh
    deps={}
    def bind(p,expected=None):
        digest=sha(ROOT/p)
        if expected is not None:assert digest==expected,p
        assert p not in deps or deps[p]==digest,p
        deps[p]=digest
        return digest
    for stem in ['mixed_complete_boundary_sum','complete_boundary_full_index_interval','mixed_first_cap_critical','mixed_cyclic_critical_localization','mixed_open_word_hessian']:
        bind('notes/research_'+stem+'.md')
    first_path='repro/results/research-mixed-first-cap-critical.json'
    first=json.loads((ROOT/first_path).read_text());bind(first_path)
    assert first['status']=='passed'
    bind('notes/research_mixed_first_cap_critical.md',first['proof_sha256'])
    bind('experiments/check_mixed_first_cap_critical.py',first['script_sha256'])
    hessian_path='repro/results/research-mixed-open-word-hessian.json'
    hessian=json.loads((ROOT/hessian_path).read_text());bind(hessian_path)
    assert hessian['status']=='passed'
    bind('notes/research_mixed_open_word_hessian.md',hessian['proof_sha256'])
    bind('experiments/check_mixed_open_word_hessian.py',hessian['script_sha256'])
    hessian_replay_path='repro/results/research-mixed-open-word-hessian-replay.json'
    hessian_replay=json.loads((ROOT/hessian_replay_path).read_text());bind(hessian_replay_path)
    assert hessian_replay['status']=='passed' and hessian_replay['input_sha256']==deps[hessian_path]
    assert hessian_replay['proof_sha256']==hessian['proof_sha256'] and hessian_replay['script_sha256']==hessian['script_sha256']
    author_path='repro/results/research-mixed-cyclic-block-localization.json'
    author=json.loads((ROOT/author_path).read_text());bind(author_path)
    assert author['status']=='passed'
    assert author['proof_sha256']==deps['notes/research_mixed_cyclic_critical_localization.md']
    bind('experiments/certify_mixed_cyclic_block_localization.py',author['script_sha256'])
    replay_path='repro/results/research-mixed-cyclic-block-localization-replay.json'
    replay=json.loads((ROOT/replay_path).read_text());bind(replay_path)
    assert replay['status']=='passed' and replay['input_sha256']==deps[author_path]
    assert replay['proof_sha256']==author['proof_sha256']
    bind('experiments/replay_mixed_cyclic_block_localization.py',replay['script_sha256'])
    for data in (author,replay,hessian,hessian_replay,first):
        for key in ('dependencies','dependencies_sha256'):
            for p,h in data.get(key,{}).items():bind(p,h)
    if old:assert old['dependencies_sha256']==deps
    specs=[(e,n) for e in range(2) for n in range(2)]
    if old:assert [(x['epsilon'],x['neighbor_epsilon']) for x in old['domains']]==specs
    domains=[];visits=leaves=omitted=0
    for index,(eps,neighbor) in enumerate(specs):
        todo=[([(F(-1),F(1)),(F(-1),F(1))],0)]
        tree=[];cursor=0;local_leaves=local_omitted=0
        while todo:
            box,depth=todo.pop();visits+=1
            assert visits<=args.max_visits,'visit budget exceeded'
            assert time.monotonic()-start<args.max_seconds,'time budget exceeded'
            if old:
                node=old['domains'][index]['tree'][cursor];cursor+=1
                if node[0]=='X':assert excluded(box);tree.append(node);local_omitted+=1;continue
                if node[0]=='S':
                    assert len(node)==2
                    j=node[1];assert j==depth%2
                    left,right=split(box,j);todo.extend([(left,depth+1),(right,depth+1)]);tree.append(node);continue
                assert node[0]=='L' and len(node)==2
                assert not excluded(box)
                bounds=test(node[1],parameter(box,neighbor),eps)
                assert bounds is not None,(eps,neighbor,cursor)
                tree.append(node);local_leaves+=1;continue
            if excluded(box):tree.append(['X']);local_omitted+=1;continue
            b=parameter(box,neighbor);bm=complex(float(b.real.mid()),float(b.imag.mid()))
            w=propose(bm,eps)
            accepted=None
            for radius in ['1/1000','1/500','1/250','1/125','1/80','1/50','1/32']:
                w['radius']=radius
                bounds=test(w,b,eps)
                if bounds is not None:accepted=dict(w);break
            if accepted is not None:tree.append(['L',accepted]);local_leaves+=1
            else:
                assert depth<20
                j=depth%2;left,right=split(box,j);todo.extend([(left,depth+1),(right,depth+1)]);tree.append(['S',j])
        if old:
            assert cursor==len(old['domains'][index]['tree'])
            assert local_leaves==old['domains'][index]['leaves']
            assert local_omitted==old['domains'][index]['excluded']
        leaves+=local_leaves;omitted+=local_omitted
        domains.append({'epsilon':eps,'neighbor_epsilon':neighbor,'leaves':local_leaves,'excluded':local_omitted,'tree':tree})
        print('PASS endpoint',eps,neighbor,local_leaves,local_omitted,flush=True)
    one=[]
    if old:assert [v['epsilon'] for v in old['one_vertex']]==[0,1]
    for eps in (0,1):
        if old:w=old['one_vertex'][eps]['witness']
        else:w=propose(0j,eps,True);w['radius']='1/10000000000'
        bounds=test(w,acb(0),eps,True)
        assert bounds is not None
        one.append({'epsilon':eps,'witness':w,'bounds':bounds})
    assert [v['leaves'] for v in domains]==[1645,1702,1002,909]
    assert (leaves,omitted,visits)==(5258,233,10978)
    if old:
        assert (old['domain_count'],old['one_vertex_count'],old['leaves'],old['excluded'],old['visits'])==(4,2,leaves,omitted,visits)
    assert sha(PROOF)==ph and sha(__file__)==sh
    for p,h in deps.items():assert sha(ROOT/p)==h,p
    if args.input:assert sha(args.input)==input_hash
    out={'status':'passed','precision_bits':args.precision,'scope':'Original zero-lift open critical geometry only; no full endpoint/source asymptotic.','domains':domains,'one_vertex':one,'domain_count':4,'one_vertex_count':2,'leaves':leaves,'excluded':omitted,'visits':visits,'proof_sha256':ph,'script_sha256':sh,'dependencies_sha256':deps}
    if input_hash:out['input_sha256']=input_hash
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n')
    print('PASS',len(domains),leaves,omitted,visits,'seconds',time.monotonic()-start,flush=True)

if __name__=='__main__':main()
