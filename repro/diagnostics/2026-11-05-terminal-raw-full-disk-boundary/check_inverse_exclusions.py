#!/usr/bin/env python3
"""Necessary inverse-map exclusions on exactly the 22 old failed cells."""
from fractions import Fraction as F
import hashlib,json
from pathlib import Path
import sys
from flint import acb,acb_mat,arb,ctx

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
sys.path.insert(0,str(ROOT/'experiments'))
import certify_mixed_open_word_critical_localization as base
ar,cp=base.ar,base.cp
FAILED=[1369,1381,1384,1429,1435,1438,1450,1451,1454,1670,1685,
        1688,1689,1701,1707,1710,1711,1724,1846,1849,1853,1866]

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def all_responses(z,a,eps,w):
    """Original implicit response, with a whole-box Neumann tail."""
    pi,ii=arb.pi(),acb(0,1)
    Y=acb_mat([[cp(v)for v in row]for row in w['inverse']])
    E=base.ident(3)-Y*base.jacobian(z,a,eps)
    rho=max(sum((abs(E[i,j])for j in range(3)),arb(0)).upper()for i in range(3))
    assert 0<=rho<1
    forcing=acb_mat([[0],[pi*(pi*(z[1]+a)).cot()+ii*pi],[0]])
    term=-(Y*forcing);result=acb_mat(term)
    norm=max(abs(term[j,0]).upper()for j in range(3))
    for _ in range(4):term=E*term;result+=term
    tail=norm*rho**5/(1-rho)
    return [result[j,0]+acb(arb(0,tail.upper()),arb(0,tail.upper()))for j in range(3)]

def attached_response(z,a,eps,w):return all_responses(z,a,eps,w)[1]

def inverse(a,b,d,bp=None):
    pi,ii=arb.pi(),acb(0,1)
    V=(-2*pi*ii*a).exp();B=(-2*pi*ii*b).exp()
    D=1-V*B
    assert abs(D)>0
    N=B*(1-V)**d;U=(1-N/D)/V
    if bp is None:return U
    Vp=-2*pi*ii*V;Bp=-2*pi*ii*bp*B
    Np=Bp*(1-V)**d-d*B*(1-V)**(d-1)*Vp
    Dp=-Vp*B-V*Bp
    Up=-(Np/D-N*Dp/D**2)/V-U*Vp/V
    return U,Up

def main():
    ctx.prec=320
    pi,ii=arb.pi(),acb(0,1)
    deps={}
    def bind(p,h=None):
        hh=sha(ROOT/p)
        if h is not None:assert hh==h,p
        assert p not in deps or deps[p]==hh
        deps[p]=hh
    ap='repro/results/research-mixed-open-word-critical-localization.json'
    rp='repro/results/research-mixed-open-word-critical-localization-replay.json'
    bind(ap);bind(rp)
    old=json.loads((ROOT/ap).read_text());replay=json.loads((ROOT/rp).read_text())
    assert old['status']==replay['status']=='passed'
    assert old['domains']==replay['domains']and replay['input_sha256']==deps[ap]
    for record in(old,replay):
        bind('notes/research_mixed_open_word_critical_localization.md',record['proof_sha256'])
        bind('experiments/certify_mixed_open_word_critical_localization.py',record['script_sha256'])
        for p,h in record['dependencies_sha256'].items():bind(p,h)
    for p in ['notes/research_mixed_open_local_factor_coverage.md',
              'notes/research_mixed_open_word_endpoint_rectangles.md',
              'repro/results/research-mixed-open-local-factor-coverage.json',
              'repro/results/research-mixed-open-word-endpoint-rectangles.json']:
        bind(p)
    for p in ['notes/research_mixed_cyclic_critical_height_bounds.md',
              'repro/results/research-mixed-cyclic-block-boundary-images.json',
              'repro/results/research-mixed-cyclic-block-boundary-images-replay.json']:
        bind(p)
    domain=old['domains'][0]
    assert(domain['epsilon'],domain['neighbor_epsilon'])==(0,0)
    stack=[([(F(-1),F(1)),(F(-1),F(1))],0)];rows=[]
    centers=[acb(ar('.35'),ar('-.01')),acb(ar('.30'),ar('-.052'))]
    radii=[ar('.083'),ar('.060')]
    for ni,node in enumerate(domain['tree']):
        assert stack
        box,depth=stack.pop()
        if node[0]=='S':
            assert node[1]==depth%2
            left,right=base.split(box,node[1]);stack.extend([(left,depth+1),(right,depth+1)])
            continue
        if node[0]=='X':
            assert base.excluded(box);continue
        assert node[0]=='L'
        if ni not in FAILED:continue
        a=base.parameter(box,0);w=node[1]
        assert base.test(w,a,0)is not None
        rad=ar(w['radius'])
        b=cp(w['centers'][1])+acb(arb(0,rad),arb(0,rad))
        b=acb(b.real.intersection(ar('.278').union(ar('.391'))),
              b.imag.intersection(ar('-.072').union(ar('.021'))))
        z=[cp(c)+acb(arb(0,rad),arb(0,rad))for c in w['centers']]
        a0=base.parameter([((lo+hi)/2,)*2 for lo,hi in box],0)
        point=dict(w,radius='1/10000000000')
        assert base.test(point,a0,0)is not None
        pr=ar(point['radius']);b0=cp(w['centers'][1])+acb(arb(0,pr),arb(0,pr))
        bp=attached_response(z,a,0,w)
        directU,Up=inverse(a,b,2,bp)
        U0=inverse(a0,b0,2)
        Umean=U0+Up*(a-a0)
        U=acb(directU.real.intersection(Umean.real),directU.imag.intersection(Umean.imag))
        V=(-2*pi*ii*a).exp()
        reasons=[]
        if abs(U)<(-ar('.24')*pi).exp()or abs(U)>(ar('.24')*pi).exp():
            reasons.append('outside_Q_height')
        if abs(U)<(-ar('.186')*pi).exp()or abs(U)>(ar('.146')*pi).exp():
            reasons.append('outside_type3_height')
        if abs(U)<(-ar('.13')*pi).exp()or abs(U)>(ar('.136')*pi).exp():
            reasons.append('outside_ordinary_type3_height')
        # Every type-three smaller-disk leg has Re s>.267>.25, hence Re U<0.
        if U.real>0:reasons.append('outside_type3_real_sector')
        s=None
        if U.imag<0:
            s=-U.log()/(2*pi*ii)
            if abs(s-centers[0])>radii[0]:reasons.append('outside_type3_disk')
        denominator=(1-U)**2+U*(1-U*V)
        c=None;A=None
        if abs(denominator)>0:
            A=(1-U*V)/denominator
            if A.imag>0:reasons.append('preceding_wrong_sector')
            if A.imag<0:
                c=-A.log()/(2*pi*ii)
                if all(abs(c-center)>r for center,r in zip(centers,radii)):
                    reasons.append('preceding_outside_both_disks')
        m2=(a.real<ar('.278')or a.real>ar('.391')or
            a.imag<ar('-.072')or a.imag>ar('.021'))
        row=dict(node=ni,parameter_box=[[str(v)for v in side]for side in box],
                 external=str(a),endpoint_attached=str(b),U=str(U),
                 direct_U=str(directU),U_derivative=str(Up),attached_derivative=str(bp),
                 U_modulus=str(abs(U)),s=str(s)if s is not None else None,
                 preceding=str(c)if c is not None else None,
                 m_ge_3_exclusion_reasons=reasons,m2_excluded=bool(m2),
                 excluded_all_lengths=bool(reasons)and bool(m2))
        rows.append(row)
        print(ni,'exclude m>=3',reasons,'m2',bool(m2),flush=True)
    assert not stack and [v['node']for v in rows]==FAILED
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    output=dict(status='necessary_constraint_cell_test',precision_bits=ctx.prec,
        scope='Exactly 22 original whole cells; necessary inverse constraints only, no sufficiency, no statement that excluding bad outer circle cells repairs the entire interior domain.',
        rows=rows,surviving_nodes=[v['node']for v in rows if not v['excluded_all_lengths']],
        dependencies_sha256=deps,script_sha256=sha(__file__),
        new_endpoint_roots=0,new_parameter_subdivisions=0)
    (HERE/'inverse-exclusions.json').write_text(json.dumps(output,indent=2)+'\n')
    print('surviving',output['surviving_nodes'])

if __name__=='__main__':main()

