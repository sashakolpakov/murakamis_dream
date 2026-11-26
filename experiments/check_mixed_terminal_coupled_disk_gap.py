#!/usr/bin/env python3
"""A single fixed coupling multiplier on165 old terminal3/3 circle cells.

No endpoint root proposal or parameter subdivision is performed. Saved mode
reuses all scalar row brackets and rechecks exact original tree coverage.
"""
import argparse
from fractions import Fraction as F
import hashlib,json,time
from pathlib import Path
from flint import acb,acb_mat,arb,ctx
import check_mixed_terminal_raw_half_gap as raw
core,base,end=raw.core,raw.base,raw.end
ar,cp=raw.ar,raw.cp
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_terminal_coupled_disk_gap.md'
MULTIPLIER=F(1,200)
FLOOR=F(1,4000)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def meets(box):
    r=F(83,90)
    minimum=sum(min(lo*lo,hi*hi)if lo*hi>0 else F(0)for lo,hi in box)
    maximum=sum(max(lo*lo,hi*hi)for lo,hi in box)
    return minimum<=r*r<=maximum

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

def solve_response(z,a,w,forcing):
    Y=acb_mat([[cp(v)for v in row]for row in w['inverse']])
    E=base.ident(3)-Y*base.jacobian(z,a,0)
    rho=max(sum((abs(E[i,j])for j in range(3)),arb(0)).upper()for i in range(3))
    assert 0<=rho<1
    term=-(Y*acb_mat([[q]for q in forcing]));result=acb_mat(term)
    norm=max(abs(term[j,0]).upper()for j in range(3))
    for _ in range(4):term=E*term;result+=term
    tail=norm*rho**5/(1-rho)
    return [result[j,0]+acb(arb(0,tail.upper()),arb(0,tail.upper()))for j in range(3)]

def second_response(z,a,w,first):
    pi=arb.pi();e,t,u=z;ep,tp,up=first
    j2=lambda v:-pi*pi/(pi*v).sin()**2
    forcing=[-j2(e-u)*(ep-up)**2+j2(e+t)*(ep+tp)**2,
             j2(e+t)*(ep+tp)**2+j2(t+a)*(tp+1)**2-2*j2(t)*tp**2,
             -2*pi*pi*up**2/(pi*u).cos()**2+j2(e-u)*(ep-up)**2-3*j2(u)*up**2]
    return solve_response(z,a,w,forcing)

def jet_add(a,b):return tuple(x+y for x,y in zip(a,b))

def jet_neg(a):return tuple(-x for x in a)

def jet_mul(a,b):return(a[0]*b[0],a[1]*b[0]+a[0]*b[1],a[2]*b[0]+2*a[1]*b[1]+a[0]*b[2])

def jet_inv(a):return(1/a[0],-a[1]/a[0]**2,2*a[1]**2/a[0]**3-a[2]/a[0]**2)

def inverse_jet(a,b,bp,bpp):
    k=-2*arb.pi()*acb(0,1);V=(k*a).exp();B=(k*b).exp()
    Vj=(V,k*V,k*k*V);Bj=(B,k*bp*B,(k*bpp+k*k*bp*bp)*B)
    one=(acb(1),acb(0),acb(0))
    omv=jet_add(one,jet_neg(Vj));den=jet_add(one,jet_neg(jet_mul(Vj,Bj)))
    numerator=jet_mul(Bj,jet_mul(omv,omv))
    return jet_mul(jet_add(one,jet_neg(jet_mul(numerator,jet_inv(den)))),jet_inv(Vj))

def circle_linear_lower(gradient,box,a0):
    """Minimum of a real linear form on the old box/circle intersection.

    Keep every possibly admitted side intersection and stationary point.
    Including an uncertain candidate only weakens the lower bound.
    """
    rho=ar(F(83,90));c=acb(ar('.35'),ar('-.01'));scale=ar('.09')
    candidates=[]
    def meets(x,j):
        return not (x<ar(box[j][0])or x>ar(box[j][1]))
    for axis in(0,1):
        for side in box[axis]:
            q=ar(side);remaining=rho*rho-q*q
            if remaining<0:continue
            assert remaining>=0
            v=remaining.sqrt()
            for sign in(-1,1):
                v1=sign*v
                if meets(v1,1-axis):
                    x,y=(q,v1)if axis==0 else(v1,q)
                    candidates.append(c+scale*acb(x,y))
    if abs(gradient)>0:
        critical=-rho*gradient.conjugate()/abs(gradient)
        if meets(critical.real,0)and meets(critical.imag,1):
            candidates.append(c+scale*critical)
    assert candidates
    return min((gradient*(p-a0)).real.lower()for p in candidates)

def test(box,w,row_witness=None):
    pi,ii=arb.pi(),acb(0,1)
    a=base.parameter(box,0)
    a0=base.parameter([((lo+hi)/2,)*2 for lo,hi in box],0)
    assert base.test(w,a,0)is not None
    point=dict(w,radius='1/10000000000')
    assert base.test(point,a0,0)is not None
    radius=ar(w['radius']);pr=ar(point['radius'])
    z=[cp(v)+acb(arb(0,radius),arb(0,radius))for v in w['centers']]
    zp=[cp(v)+acb(arb(0,pr),arb(0,pr))for v in w['centers']]
    ep,tp,up=zp
    radii=[ar(base.DISKS[0][2]*(hi-lo)/2)for lo,hi in box]
    # These are inclusions for the same original branch over the same cell.
    for _ in range(3):
        responses=all_responses(z,a,0,w)
        transported=[q+d*(a-a0)for q,d in zip(zp,responses)]
        z=[acb(q.real.intersection(t.real),q.imag.intersection(t.imag))for q,t in zip(z,transported)]
    first=all_responses(z,a,0,w)
    second=second_response(z,a,w,first)
    direct,Up=inverse(a,z[1],2,first[1]);U0=inverse(a0,tp,2)
    mean=U0+Up*(a-a0)
    U=acb(direct.real.intersection(mean.real),direct.imag.intersection(mean.imag))
    assert U.is_finite()and U0.is_finite()
    phi_upper=abs(U).upper().log()+ar('.13')*pi
    if abs(U)>0:
        dp=Up/U
        alternative=abs(U0).log()+ar('.13')*pi+abs(dp.real)*radii[0]+abs(dp.imag)*radii[1]
        phi_upper=min(phi_upper.upper(),alternative.upper())
    v,vm,rw=raw.raw_row(a,a0,0,row_witness)
    P0=core.action(a0,ep,tp,up,0).real
    values=[P0-HHALF-raw.row(vm,a0,0),P0-HHALF+2*pi*a0.imag,
            P0-HHALF-B2/2,P0-HHALF-B2/2+pi*a0.imag]
    Pprime=core.gp(z[1]+a)+2*pi*ii*z[1]-core.gp(a)
    gradients=[core.gp(z[1]+a)+2*pi*ii*z[1]-core.gp(a+v)-2*pi*ii*v,
               Pprime-2*pi*ii,Pprime,Pprime-pi*ii]
    midpoint_first=all_responses(zp,a0,0,w)
    _,U0p=inverse(a0,tp,2,midpoint_first[1])
    Pprime0=core.gp(tp+a0)+2*pi*ii*tp-core.gp(a0)
    gradients0=[core.gp(tp+a0)+2*pi*ii*tp-core.gp(a0+vm)-2*pi*ii*vm,
                Pprime0-2*pi*ii,Pprime0,Pprime0-pi*ii]
    gpp=lambda q:pi*(pi*q).cot()-pi*ii
    Psecond=gpp(a+z[1])*(1+first[1])+2*pi*ii*first[1]-gpp(a)
    Qaa=gpp(a+v)-gpp(a);Qav=gpp(a+v)+2*pi*ii
    Tv=(pi*(pi*(a+v)).cot()-pi*(pi*v).tan()-2*pi*(pi*v).cot()).real
    assert Tv< -2*pi
    common=Psecond-Qaa
    raw_hessian=[common.real+Qav.real**2/Tv,
                 -common.imag-Qav.real*Qav.imag/Tv,
                 -common.real+Qav.imag**2/Tv]
    other_hessian=[Psecond.real,-Psecond.imag,-Psecond.real]
    _,_,Upp=inverse_jet(a,z[1],first[1],second[1])
    nonzero=bool(abs(U)>0)
    log_second=Upp/U-(Up/U)**2 if nonzero else None
    lam=ar(MULTIPLIER);lowers=[]
    for j in range(4):
        # All three methods are lower bounds for exactly the same branch.
        g=values[j]-abs(gradients[j].real)*radii[0]-abs(gradients[j].imag)*radii[1]
        best=(g-lam*phi_upper).lower()
        if nonzero:
            value0=values[j]-lam*(abs(U0).log()+ar('.13')*pi)
            dp=gradients[j]-lam*Up/U
            mid=acb(dp.real.mid(),dp.imag.mid());error=dp-mid
            bound=value0+circle_linear_lower(mid,box,a0)
            bound-=abs(error.real)*radii[0]+abs(error.imag)*radii[1]
            best=max(best,bound.lower())
            dp0=gradients0[j]-lam*U0p/U0
            dp0mid=acb(dp0.real.mid(),dp0.imag.mid());dp0err=dp0-dp0mid
            hess=raw_hessian if j==0 else other_hessian
            log_hess=[log_second.real,-log_second.imag,-log_second.real]
            hj=[x-lam*y for x,y in zip(hess,log_hess)]
            assert all(x.is_finite()for x in hj)
            remainder=(abs(hj[0])*radii[0]**2+2*abs(hj[1])*radii[0]*radii[1]+abs(hj[2])*radii[1]**2)/2
            bound=value0+circle_linear_lower(dp0mid,box,a0)
            bound-=abs(dp0err.real)*radii[0]+abs(dp0err.imag)*radii[1]+remainder
            best=max(best,bound.lower())
        assert best>ar(FLOOR),('coupled boundary gap',box,j,best)
        lowers.append(best)
    return dict(row_bracket=rw,branch_lower_bounds=[str(q)for q in lowers],
                U_nonzero_on_cell=nonzero),min(lowers)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision',type=int,default=256)
    parser.add_argument('--input',type=Path)
    parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-terminal-coupled-disk-gap.json')
    args=parser.parse_args();assert args.precision>=192;ctx.prec=args.precision
    global HHALF,B2
    pi,ii=arb.pi(),acb(0,1)
    raw.PI,raw.II,raw.HALF=pi,ii,acb(ar('1/2'))
    core.PI,core.II,core.HALF=pi,ii,raw.HALF
    end.PI,end.II=pi,ii
    uh=acb(ar('1/4'),arb(3).log()/(4*pi))
    HHALF=(end.J(raw.HALF)+end.phase(raw.HALF,uh)).real
    B2=-4*end.J(acb(ar('1/4'))).real
    ph,sh=sha(PROOF),sha(__file__);ih=sha(args.input)if args.input else None
    saved=json.loads(args.input.read_text())if args.input else None
    deps={};primary={}
    def bind(p,h=None):
        hh=sha(ROOT/p)
        if h is not None:assert hh==h,p
        assert p not in deps or deps[p]==hh
        deps[p]=hh;return hh
    def read(p):
        primary[p]=bind(p);r=json.loads((ROOT/p).read_text());assert r['status']=='passed'
        for key in('dependencies_sha256','dependencies'):
            for pp,hh in r.get(key,{}).items():bind(pp,hh)
        return r
    for stem,proof,script in[
        ('terminal-raw-half-gap','research_mixed_terminal_raw_half_gap.md','check_mixed_terminal_raw_half_gap.py'),
        ('terminal-inverse-constraint','research_mixed_terminal_inverse_constraint.md','check_mixed_terminal_inverse_constraint.py')]:
        p='repro/results/research-mixed-'+stem+'.json'
        r='repro/results/research-mixed-'+stem+'-replay.json'
        author,replay=read(p),read(r)
        assert replay['input_sha256']==deps[p]
        for rec in(author,replay):
            bind('notes/'+proof,rec['proof_sha256']);bind('experiments/'+script,rec['script_sha256'])
    ap='repro/results/research-mixed-open-word-critical-localization.json'
    rp='repro/results/research-mixed-open-word-critical-localization-replay.json'
    roots,replay=read(ap),read(rp)
    assert replay['input_sha256']==deps[ap]and roots['domains']==replay['domains']
    for rec in(roots,replay):
        bind('notes/research_mixed_open_word_critical_localization.md',rec['proof_sha256'])
        bind('experiments/certify_mixed_open_word_critical_localization.py',rec['script_sha256'])
    for p in ['notes/research_terminal_coupling_barriers.md',
              'notes/research_mixed_terminal_half_row_envelope.md',
              'notes/research_mixed_endpoint_polynomial_collar.md']:
        bind(p)
    for p in ['repro/results/research-mixed-cyclic-block-boundary-images.json',
              'repro/results/research-mixed-cyclic-block-boundary-images-replay.json']:
        bind(p);record=json.loads((ROOT/p).read_text())
        assert record['status']=='passed'and record['height_bounds']==['-13/200','17/250','-51/500','-1/1000']
        bind('notes/research_mixed_cyclic_critical_height_bounds.md',record['proof_sha256'])
    if saved:
        assert saved['status']=='passed'and saved['proof_sha256']==ph and saved['script_sha256']==sh
        assert saved['dependencies_sha256']==deps
        assert saved['multiplier']==str(MULTIPLIER)and saved['floor']==str(FLOOR)
        old={w['node']:w for w in saved['witnesses']}
        assert len(old)==165
    domain=roots['domains'][0]
    assert(domain['epsilon'],domain['neighbor_epsilon'])==(0,0)
    stack=[([(F(-1),F(1)),(F(-1),F(1))],0)]
    rows=[];nodes=leaves=exclusions=0;minimum=None;start=time.monotonic()
    for ni,node in enumerate(domain['tree']):
        assert time.monotonic()-start<120 and stack
        box,depth=stack.pop();nodes+=1
        if node[0]=='S':
            assert node[1]==depth%2
            left,right=base.split(box,node[1]);stack.extend([(left,depth+1),(right,depth+1)])
            continue
        if node[0]=='X':
            assert base.excluded(box)and not meets(box);exclusions+=1;continue
        assert node[0]=='L';leaves+=1
        if not meets(box):continue
        witness=old[ni]['row_bracket']if saved else None
        result,low=test(box,node[1],witness)
        row=dict(node=ni,box=[[str(q)for q in side]for side in box],**result)
        if saved:assert row['box']==old[ni]['box']and row['row_bracket']==old[ni]['row_bracket']
        rows.append(row)
        if minimum is None or low<minimum:minimum=low
    assert not stack and(nodes,leaves,exclusions,len(rows))==(3439,1645,75,165)
    if saved:assert [r['node']for r in rows]==[r['node']for r in saved['witnesses']]
    out=dict(status='passed',precision_bits=ctx.prec,original_domain=0,epsilon=0,neighbor_epsilon=0,
        original_nodes=nodes,original_leaves=leaves,original_exclusions=exclusions,
        circle_cells=len(rows),raw_majorant_branches=4,multiplier=str(MULTIPLIER),floor=str(FLOOR),
        minimum_lower_bound=str(minimum),witnesses=rows,new_endpoint_roots=0,new_parameter_subdivisions=0,
        scope='Single coupled3/3 terminal family: circle multiplier, actual critical-input gap for m>=3 and its small ambient continuation. No whole open-source or arbitrary integration-target claim.',
        primary_records_sha256=primary,dependencies_sha256=deps,proof_sha256=ph,script_sha256=sh,
        elapsed_seconds=time.monotonic()-start)
    if ih:out['input_sha256']=ih
    assert sha(PROOF)==ph and sha(__file__)==sh
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    if ih:assert sha(args.input)==ih
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print('PASS165 cells/660 branches, minimum',minimum,'bindings',len(deps))

if __name__=='__main__':main()
