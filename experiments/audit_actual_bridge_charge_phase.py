#!/usr/bin/env python3
"""Exact signed bridge charges, full phase, and actual postbridge source selection."""
import itertools
import json
from fractions import Fraction
from pathlib import Path
import mpmath as mp
import sympy as sp
from flint import acb,arb,ctx

from audit_actual_hardy_cauchy_network import HardyNetwork
import audit_bridge_reduced_absolute_envelope as whole


def poch(Q,p,a,L):
    out=1
    for j in range(L):out=out*(1-a*pow(Q,j,p))%p
    return out


def qbinom(H,L,s):
    if not 0<=s<=L:return 0
    return H.fac[L]*pow(H.fac[s]*H.fac[L-s],-1,H.p)%H.p


def compositions(d,k):
    if k==1:
        yield(d,);return
    for j in range(d+1):
        for tail in compositions(d-j,k-1):yield(j,)+tail


def charged_value(H,signs,aa,zin,zout,ns):
    p,Q,q,x=H.p,H.Q,H.q,H.x;m=len(signs)
    bb=[Q*Q*x*pow(a,-1,p)%p for a in aa]
    z=[bb[0]*pow(zin,-1,p)%p]+[aa[j]*bb[j+1]*pow(Q,-1,p)%p for j in range(m-1)]+[aa[-1]*zout%p]
    t=[1];w=0
    for j,(sig,a) in enumerate(zip(signs,aa),1):
        w+=sig;t.append((-1)**j*pow(q,2+w,p)*pow(zin*a,-1,p)%p)
    answer=pow(H.kappa,sum(signs),p)
    for zr,tr,n in zip(z,t,ns):answer=answer*poch(Q,p,zr,n)*H.inv[n]*pow(tr,n,p)%p
    return answer,z,t


def charged_checks():
    rows=[]
    for N in range(2,11):
        H=HardyNetwork(N,1);p,Q,q,x,d=H.p,H.Q,H.q,H.x,N-1
        count=0
        for m in (1,2,4):
            aa=[j+2 for j in range(m)];bb=[Q*Q*x*pow(a,-1,p)%p for a in aa]
            hs=sorted(((N+3*j+m)%N for j in range(m)),reverse=True)
            ns=[d-hs[0]]+[a-b for a,b in zip(hs,hs[1:])]+[hs[-1]]
            for signs in itertools.product((1,-1),repeat=m):
                original=pow(N,m-1,p)*pow(7,-hs[0],p)%p
                original=original*poch(Q,p,bb[0]*pow(7,-1,p)%p,d-hs[0])%p
                original=original*poch(Q,p,aa[-1]*11%p,hs[-1])%p
                for j,(hh,sig,a) in enumerate(zip(hs,signs,aa)):
                    u=(pow(Q,-hh,p)*pow(x*a,-1,p) if sig>0 else Q*x*pow(a,-1,p))%p
                    c=(pow(H.kappa,sig,p)*pow(N,-1,p)*(-1)**hh
                       *pow(Q,sig*hh*(hh+1)//2,p)*pow(u,hh,p))%p
                    assert c==pow(H.kappa,sig,p)*pow(N,-1,p)*pow(a,-hh,p)*pow(q,-hh*hh+(1+sig)*hh,p)%p
                    original=original*c%p
                    if j<m-1:
                        sn=hs[j+1];dn=hh-sn
                        original=original*pow(-a,sn,p)*pow(Q,sn*(sn-1)//2,p)%p
                        original=original*qbinom(H,hh,sn)*poch(Q,p,a*bb[j+1]*pow(Q,-1,p)%p,dn)%p
                transformed,z,t=charged_value(H,signs,aa,7,11,ns)
                assert original==transformed,(N,m,signs)
                for j,sig in enumerate(signs):assert z[j]*t[j]%p==pow(Q,(1-sig)//2,p)*t[j+1]%p
                assert z[-1]*t[-1]%p==(-1)**m*pow(q,2+sum(signs),p)*11*pow(7,-1,p)%p
                count+=1
        rows.append({'N':N,'all_signed_fully_normalized_charged_bridges':count,
                     'all_quadratic_interior_clock_phases_cancel_exactly':True})
    return rows


def independent_height_sum():
    rows=[]
    for N in range(2,9):
        H=HardyNetwork(N,1);p,Q,q,d=H.p,H.Q,H.q,N-1
        count=0
        for m in (1,2,3):
            aa=[j+2 for j in range(m)]
            for signs in itertools.product((1,-1),repeat=m):
                left=0;ts=None
                for ns in compositions(d,m+1):
                    value,z,ts=charged_value(H,signs,aa,7,11,ns);left=(left+value)%p
                end=(-1)**m*pow(q,2+sum(signs),p)*11*pow(7,-1,p)%p
                coeff=[poch(Q,p,end,n)*H.inv[n]%p for n in range(N)]
                for j,sig in enumerate(signs,1):
                    if sig>0:continue
                    coeff=[sum(coeff[k]*pow(ts[j],n-k,p) for k in range(n+1))%p for n in range(N)]
                right=pow(H.kappa,sum(signs),p)*coeff[d]%p
                assert left==right,(N,m,signs)
                count+=1
        rows.append({'N':N,'conditional_independent_height_generating_identities':count,
                     'no_global_spectator_independence_assumed':True})
    return rows


def seam_checks():
    rows=[]
    for N in range(2,13):
        H=HardyNetwork(N,1);p,Q,d=H.p,H.Q,N-1
        def poly(a,L):
            f=[1]
            for j in range(L):
                g=[0]*(len(f)+1)
                for k,v in enumerate(f):g[k]=(g[k]+v)%p;g[k+1]=(g[k+1]-a*pow(Q,j,p)*v)%p
                f=g
            return f
        count=0
        for r,h in itertools.product(range(N),repeat=2):
            a=3;b=Q*pow(a,-1,p)%p
            A=poly(a,d-r);B=poly(b,d-h)
            actual=sum(A[i]*B[j] for i in range(len(A)) for j in range(len(B)) if r-h+i-j==0)%p
            expected=(-1)**(d-r)*pow(a,h-r,p)*pow(Q,(d-r)*(d-r-1)//2-h*(d-h),p)*qbinom(H,r,d-h)%p
            assert actual==expected
            assert bool(actual)==(r+h>=d)
            count+=1
        rows.append({'N':N,'actual_complementary_charge_CT_cases':count,
                     'support_exactly_r_plus_H_ge_d':True})
    return rows


def phase_polynomial():
    X={v:sp.Symbol('x'+str(v),real=True) for v in whole.LABELS}
    base={X[v]:sp.Rational(n,20) for v,n in whole.LABELS.items()};base[X[6]]=sp.Rational(89,100)
    Y={v:X[v]+sp.Rational(whole.PHASES[v].numerator,whole.PHASES[v].denominator) for v in X}
    data=[]
    for r in whole.RECORDS:
        vi=r['in'][1-r['over_in']];vo=r['out'][1-r['over_out']]
        raw=r['sign']*(X[vi]-X[vo]);hh=raw-sp.floor(raw.subs(base))
        ar=-hh-sp.Rational(1,2)-Y[vo] if r['sign']>0 else sp.Rational(1,2)-Y[vo]
        ar=ar-sp.floor(ar.subs(base));data.append((hh,ar))
    def chi(z):
        value=z.subs(base);assert not value.is_integer
        f=z-sp.floor(value);return (f*f-f)/2
    theta=0
    for path in whole.PATHS:
        hs=[data[j][0] for j in path];aa=[data[j][1] for j in path]
        first,last=whole.RECORDS[path[0]],whole.RECORDS[path[-1]]
        yi=Y[first['in'][first['over_in']]];yo=Y[last['out'][last['over_out']]]
        tt=[1-hs[0]]+[a-b for a,b in zip(hs,hs[1:])]+[hs[-1]]
        al=[sp.Rational(1,2)-aa[0]-yi]+[sp.Rational(1,2)+a-b for a,b in zip(aa,aa[1:])]+[aa[-1]+yo]
        tau=[0]+[sp.Rational(j,2)-yi-aa[j-1] for j in range(1,len(path)+1)]
        theta+=sum(chi(a+t)-chi(a)-chi(t)+2*t*u for a,t,u in zip(al,tt,tau))
    derivative=sp.factor(sp.diff(theta,X[5]))
    assert sp.expand(derivative-(X[3]-2*X[6]+X[7]+1))==0
    assert derivative.subs(base)==sp.Rational(21,50)
    return {'entire_actual_reduced_phase_derivative_over_pi':str(derivative),
            'exact_interior_source_value':'21/50','nontrivial_bridge_already_eliminated':[2,3]}


def whole_source_checks():
    rows=[]
    for N in (100,200,400):
        W=whole.full_reduced_weight(N,{6:89*N//100},precision=100)
        Wnext=whole.full_reduced_weight(N,{6:89*N//100,5:N//10+1},precision=100)
        phase=mp.arg(Wnext/W);target=21*mp.pi/50
        assert N*abs(phase-target)<5
        rows.append({'N':N,'full_original_caps_pivots_and_reduced_weight':True,
                     'actual_neighbor_phase':float(phase),'limiting_phase_21pi_over50':float(target),
                     'N_times_phase_error':float(N*abs(phase-target))})
    N=100;mp.mp.dps=140;q=mp.exp(mp.pi*1j/N);Q=q*q;x=-1/q
    roots=[mp.exp(mp.log(mp.mpc((-1)**i*c))/N) for i,c in enumerate((2,3,4))]
    variable_roots=dict(enumerate(roots))
    for rec in whole.RECORDS:
        pos,sig=rec['position'],rec['sign'];factor=x if sig>0 else 1/x
        outs=[factor*roots[pos+1],factor*roots[pos]]
        variable_roots.update(dict(zip(rec['out'],outs)));roots[pos:pos+2]=outs
    labs={v:n*N//20 for v,n in whole.LABELS.items()};labs[6]=89
    vals={v:rr*Q**labs[v] for v,rr in variable_roots.items() if v in labs}
    r=(labs[3]-labs[6])%N;H=(labs[6]-labs[7])%N
    assert (r,H)==(1,59)
    a=Q**(r+1)/vals[3];b=vals[6]/x;assert abs(a*b-Q)<mp.mpf('1e-120')
    def pc(arg,L):return mp.fprod(1-arg*Q**j for j in range(L))
    def g(z):return z**(r-H)*pc(a*z,N-1-r)*pc(b/z,N-1-H)
    ref=whole.full_reduced_weight(N,{6:89},precision=140)
    refg=g(vals[5])
    for label in (0,17,59,99):
        actual=whole.full_reduced_weight(N,{6:89,5:label},precision=140)/ref
        predicted=g(variable_roots[5]*Q**label)/refg
        assert abs(actual/predicted-1)<mp.mpf('1e-105')
    fiber=sum(g(variable_roots[5]*Q**j)/refg for j in range(N))
    assert abs(fiber)<mp.mpf('1e-100')
    return rows,{'N':N,'actual_whole_source_fiber_agrees_with_typed_seam':True,
                 'normalized_entire_wire_sum_abs':float(abs(fiber)),
                 'r':r,'H':H,'exact_sum_zero_by_spectral_support':True}


def main():
    source,fiber=whole_source_checks()
    result={'fully_normalized_charge_identities':charged_checks(),
            'optional_independent_height_sum':independent_height_sum(),
            'actual_second_stage_charge_projector':seam_checks(),
            'whole_reduced_phase_polynomial':phase_polynomial(),
            'whole_original_source_neighbor_phases':source,'whole_original_zero_fiber':fiber,
            'scope':'full marked bridge complex phase; one actual additional source selection; '
                    'no blanket positivity or global volume theorem'}
    Path(__file__).with_name('audit_actual_bridge_charge_phase_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS nine full signed charged bridges, seven conditional height sums, eleven exact seam tables, '
          'whole original5_2 phase polynomial/three scales/exact zero sourcefiber')


if __name__=='__main__':main()
