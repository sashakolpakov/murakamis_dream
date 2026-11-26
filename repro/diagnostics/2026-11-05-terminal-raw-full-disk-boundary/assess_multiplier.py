#!/usr/bin/env python3
"""Bounded multiplier assessment on the 165 existing 3/3 circle cells."""
from fractions import Fraction as F
import hashlib,json,time
from pathlib import Path
import sys
from flint import acb,acb_mat,arb,ctx

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
import diagnose as diag
import check_inverse_exclusions as inv
base,raw,core,end=diag.base,diag.raw,diag.core,diag.end
ar,cp=diag.ar,diag.cp
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

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

def main():
    ctx.prec=256
    pi,ii=arb.pi(),acb(0,1)
    diag.PI,diag.II=pi,ii
    raw.PI,raw.II,raw.HALF=pi,ii,acb(ar('1/2'))
    core.PI,core.II,core.HALF=pi,ii,raw.HALF
    end.PI,end.II=pi,ii
    uh=acb(ar('1/4'),arb(3).log()/(4*pi))
    diag.HHALF=(end.J(raw.HALF)+end.phase(raw.HALF,uh)).real
    diag.B2=-4*end.J(acb(ar('1/4'))).real
    deps={}
    def bind(p,h=None):
        hh=sha(ROOT/p)
        if h is not None:assert hh==h,p
        assert p not in deps or deps[p]==hh
        deps[p]=hh
    old=json.loads((HERE/'result.json').read_text())
    bind(str((HERE/'result.json').relative_to(ROOT)))
    for p,h in old['dependencies_sha256'].items():bind(p,h)
    bind(str((HERE/'diagnose.py').relative_to(ROOT)),old['script_sha256'])
    bind(str((HERE/'check_inverse_exclusions.py').relative_to(ROOT)))
    bind('notes/research_mixed_cyclic_critical_height_bounds.md')
    roots=json.loads((ROOT/'repro/results/research-mixed-open-word-critical-localization.json').read_text())
    domain=roots['domains'][0]
    assert(domain['epsilon'],domain['neighbor_epsilon'])==(0,0)
    stack=[([(F(-1),F(1)),(F(-1),F(1))],0)]
    rows=[];lower=0.;upper=float('inf');bad=[];start=time.monotonic()
    trials=[F(1,1000),F(1,500),F(1,300),F(1,200),F(1,100),F(1,50)]
    trial_minima={str(lam):None for lam in trials}
    trial_failures={str(lam):[]for lam in trials}
    for ni,node in enumerate(domain['tree']):
        assert time.monotonic()-start<120
        box,depth=stack.pop()
        if node[0]=='S':
            assert node[1]==depth%2
            left,right=base.split(box,node[1]);stack.extend([(left,depth+1),(right,depth+1)])
            continue
        if node[0]=='X':assert base.excluded(box);continue
        assert node[0]=='L'
        if not diag.meets(box,0):continue
        result,lows=diag.test(box,0,0,node[1])
        a=base.parameter(box,0);a0=base.parameter([((lo+hi)/2,)*2 for lo,hi in box],0)
        radii=[ar(base.DISKS[0][2]*(hi-lo)/2)for lo,hi in box]
        w=node[1];rr=ar(w['radius'])
        z=[cp(v)+acb(arb(0,rr),arb(0,rr))for v in w['centers']]
        pr=ar('1/10000000000');b0=cp(w['centers'][1])+acb(arb(0,pr),arb(0,pr))
        zp=[cp(c)+acb(arb(0,pr),arb(0,pr))for c in w['centers']]
        # Tighten only enclosures on the same saved cell using the already
        # validated implicit branch. No root proposal or subdivision occurs.
        for _ in range(3):
            responses=inv.all_responses(z,a,0,w)
            transported=[q+d*(a-a0)for q,d in zip(zp,responses)]
            z=[acb(q.real.intersection(t.real),q.imag.intersection(t.imag))for q,t in zip(z,transported)]
        bp=inv.attached_response(z,a,0,w)
        first=inv.all_responses(z,a,0,w)
        second=second_response(z,a,w,first)
        direct,Up=inv.inverse(a,z[1],2,bp);U0=inv.inverse(a0,b0,2)
        mean=U0+Up*(a-a0)
        U=acb(direct.real.intersection(mean.real),direct.imag.intersection(mean.imag))
        phi_upper=abs(U).upper().log()+ar('.13')*pi
        phi_method='modulus'
        if abs(U)>0:
            derivative=Up/U
            alternative=abs(U0).log()+ar('.13')*pi+abs(derivative.real)*radii[0]+abs(derivative.imag)*radii[1]
            if alternative.upper()<phi_upper.upper():phi_upper=alternative;phi_method='log_mean_value'
        # A^-1 has no denominator zero on this analytic endpoint graph.
        V=(-2*pi*ii*a).exp();Ai=U+(1-U)**2/(1-U*V)
        phi2_upper=abs(Ai).upper().log()+ar('.146')*pi if Ai.is_finite() else arb.pos_inf()
        g=min(v.lower()for v in lows)
        pp=float(phi_upper.upper());gg=float(g)
        if pp>0:upper=min(upper,gg/pp)
        elif pp<0:lower=max(lower,gg/pp)
        elif gg<=0:bad.append(ni)
        corrected={}
        v,vm,_=raw.raw_row(a,a0,0)
        ep,tp,up=[cp(c)+acb(arb(0,pr),arb(0,pr))for c in w['centers']]
        P0=core.action(a0,ep,tp,up,0).real
        values=[P0-diag.HHALF-raw.row(vm,a0,0),
                P0-diag.HHALF+2*pi*a0.imag,
                P0-diag.HHALF-diag.B2/2,
                P0-diag.HHALF-diag.B2/2+pi*a0.imag]
        Pprime=core.gp(z[1]+a)+2*pi*ii*z[1]-core.gp(a)
        derivatives=[core.gp(z[1]+a)+2*pi*ii*z[1]-core.gp(a+v)-2*pi*ii*v,
                     Pprime-2*pi*ii,Pprime,Pprime-pi*ii]
        midpoint_first=inv.all_responses(zp,a0,0,w)
        _,U0p=inv.inverse(a0,b0,2,midpoint_first[1])
        Pprime0=core.gp(tp+a0)+2*pi*ii*tp-core.gp(a0)
        derivatives0=[core.gp(tp+a0)+2*pi*ii*tp-core.gp(a0+vm)-2*pi*ii*vm,
                      Pprime0-2*pi*ii,Pprime0,Pprime0-pi*ii]
        gpp=lambda q:pi*(pi*q).cot()-pi*ii
        Psecond=gpp(a+z[1])*(1+first[1])+2*pi*ii*first[1]-gpp(a)
        Qaa=gpp(a+v)-gpp(a)
        Qav=gpp(a+v)+2*pi*ii
        Tv=(pi*(pi*(a+v)).cot()-pi*(pi*v).tan()-2*pi*(pi*v).cot()).real
        assert Tv< -2*pi
        common=Psecond-Qaa
        raw_hessian=[common.real+Qav.real**2/Tv,
                     -common.imag-Qav.real*Qav.imag/Tv,
                     -common.real+Qav.imag**2/Tv]
        other_hessian=[Psecond.real,-Psecond.imag,-Psecond.real]
        _,_,Upp=inverse_jet(a,z[1],first[1],second[1])
        log_second=Upp/U-(Up/U)**2 if abs(U)>0 else None
        for lam in trials:
            chosen=[]
            for j in range(4):
                baseline=lows[j]-ar(lam)*phi_upper
                if abs(U)>0:
                    dp=derivatives[j]-ar(lam)*Up/U
                    mid=acb(dp.real.mid(),dp.imag.mid())
                    error=dp-mid
                    bound=values[j]-ar(lam)*(abs(U0).log()+ar('.13')*pi)
                    bound+=circle_linear_lower(mid,box,a0)
                    bound-=abs(error.real)*radii[0]+abs(error.imag)*radii[1]
                    baseline=max(baseline.lower(),bound.lower())
                    # Second-order bound with the exact midpoint gradient.
                    dp0=derivatives0[j]-ar(lam)*U0p/U0
                    dp0mid=acb(dp0.real.mid(),dp0.imag.mid());dp0err=dp0-dp0mid
                    hess=raw_hessian if j==0 else other_hessian
                    log_hess=[log_second.real,-log_second.imag,-log_second.real]
                    hj=[x-ar(lam)*y for x,y in zip(hess,log_hess)]
                    remainder=(abs(hj[0])*radii[0]**2+2*abs(hj[1])*radii[0]*radii[1]+abs(hj[2])*radii[1]**2)/2
                    b2=values[j]-ar(lam)*(abs(U0).log()+ar('.13')*pi)
                    b2+=circle_linear_lower(dp0mid,box,a0)
                    b2-=abs(dp0err.real)*radii[0]+abs(dp0err.imag)*radii[1]+remainder
                    baseline=max(baseline.lower(),b2.lower())
                chosen.append(baseline.lower())
            low=min(chosen);key=str(lam)
            if trial_minima[key]is None or low<trial_minima[key]:trial_minima[key]=low
            if not low>0:trial_failures[key].append(ni)
            corrected[key]=[str(q)for q in chosen]
        row=dict(node=ni,box=[[str(x)for x in side]for side in box],
                 gap_lowers=[str(v.lower())for v in lows],
                 phi_upper=str(phi_upper.upper()),phi_method=phi_method,
                 phi2_upper=str(phi2_upper.upper()),U=str(U),U_prime=str(Up),
                 phi_midpoint=str(abs(U0).log()+ar('.13')*pi),corrected_lower_bounds=corrected)
        rows.append(row)
    assert not stack and len(rows)==165
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    out=dict(status='bounded_multiplier_assessment',scope='Necessary multiplier feasibility using whole old cells; no sign theorem or new roots/subdivisions. Floating lambda interval is a proposal only.',
             precision_bits=ctx.prec,old_cells=165,rows=rows,
             scalar_multiplier_proposal_interval=[lower,upper],zero_slope_failures=bad,
             rational_multiplier_tests={k:dict(minimum=str(trial_minima[k]),failed_nodes=trial_failures[k])for k in trial_minima},
             new_endpoint_roots=0,new_parameter_subdivisions=0,elapsed_seconds=time.monotonic()-start,
             dependencies_sha256=deps,script_sha256=sha(__file__))
    (HERE/'multiplier-assessment.json').write_text(json.dumps(out,indent=2)+'\n')
    print('165 cells; scalar multiplier proposal',lower,upper,'seconds',out['elapsed_seconds'])
    print('combined gradient/circle trials',out['rational_multiplier_tests'])
    for r in rows:
        if r['node']in inv.FAILED:
            print(r['node'],'gap',r['gap_lowers'][0],'phi upper',r['phi_upper'],'phi mid',r['phi_midpoint'])

if __name__=='__main__':main()
