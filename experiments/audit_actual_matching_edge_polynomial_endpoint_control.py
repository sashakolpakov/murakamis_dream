#!/usr/bin/env python3
"""Original polynomial endpoint convolution and genuine generic control.

The uniform neighborhood/jet bounds are proved in the note. Exact
generic/root germs and positive endpoint/disk diagnostics audit them.
"""
import json
import math
from pathlib import Path
import mpmath as mp
from audit_actual_q_hahn_physical_generic_jet_bound import Jet
from audit_high_color_first_normal_r_degree import root_field


def original(d,a,q,z):
    delta=q-q**-1
    qint=lambda n:(q**n-q**(-n))/delta
    term=value=q**0
    for k in range(a):
        lam=q**(2*k+1)+q**(-2*k-1)
        term=-term*qint(a-k)*qint(a+k+1)*(z-lam)/(qint(k+1)**2*qint(d-k)*qint(d+k+2)*delta**2)
        value+=term
    return value


def transformed(d,a,q,Z):
    Q=q*q;pref=q**0
    for r in range(a):
        pref*=((1-q**-1*Z**-1*Q**(-d+r))*(1-q**-1*Z*Q**(-d-a+r))
               /((1-Q**(-d+r))*(1-Q**(-d-a-1+r))))
    term=value=q**0
    for k in range(a):
        term*=((1-Q**(k-a))**2*(1-q*Z*Q**k)**2*Q
              /((1-Q**(k+1))**2*(1-q*Z*Q**(d+1-a+k))*(1-q*Z*Q**(-d-a-1+k))))
        value+=term
    return pref*value


def exact():
    generic=germs=0
    Jet.p=1000003;Jet.order=1
    for q0 in [2,3,5]:
        for Z0 in [7,11]:
            q=Jet(q0);Z=Jet(Z0)
            for d in range(1,16):
                for a in range(d//2+1):
                    assert original(d,a,q,Z+Z**-1)==transformed(d,a,q,Z)
                    generic+=1
    for N in range(3,17):
        p,eta=root_field(N);root=eta*eta%p
        Jet.p=p;Jet.order=4
        for slope in [0,1,7]:
            q=Jet([root*pow(slope,k,p)*pow(math.factorial(k),-1,p)%p for k in range(4)])
            Z=Jet([1,1,0,0])
            for a in range((N-1)//2+1):
                assert original(N-1,a,q,Z+Z**-1)==transformed(N-1,a,q,Z)
                germs+=1
    return dict(exact_generic_Sears_values=generic,exact_joint_root_four_jets=germs)


def positive_and_matrices():
    mp.mp.dps=100;endpoints=matrices=0;rows=[]
    for N in range(3,82):
        th=mp.pi/N;q=mp.exp(1j*th);bs=[mp.mpf(1)]
        for a in range(1,(N-1)//2+1):bs.append(bs[-1]*mp.sin((a-mp.mpf('.5'))*th)/mp.sin(a*th))
        for a in range((N-1)//2+1):
            pos=sum(bs[k]**2*bs[a-k]**2 for k in range(a+1))
            literal=original(N-1,a,q,mp.mpf(2))
            assert abs(literal-pos)<mp.mpf('1e-60')
            assert pos>=mp.mpf(1)/(4*a+1)-mp.mpf('1e-90') and pos<=1+mp.mpf('1e-90')
            endpoints+=1
        if N not in [4,5,8,9,16,17,32,33]:continue
        a=(N-1)//2
        D=mp.matrix(a);Di=mp.matrix(a)
        for n in range(a):
            D[n,n]=1/(mp.cos(n*th)*mp.cos((n+1)*th))
            if n:
                v=mp.sin(n*th)/(mp.cos(n*th)*mp.sqrt(mp.sin((2*n-1)*th)*mp.sin((2*n+1)*th)))
                D[n,n-1]=D[n-1,n]=v
        for k in range(1,a+1):
            for l in range(1,a+1):
                Di[k-1,l-1]=(-1)**(k+l)*mp.sqrt(mp.sin((2*k-1)*th)*mp.sin((2*l-1)*th))*sum(mp.cot(m*th) for m in range(max(k,l),a+1))
        assert mp.norm(D*Di-mp.eye(a))<mp.mpf('1e-85')
        trace=sum(Di[n,n] for n in range(a))
        expected=mp.sin(a*th)*mp.sin((a+1)*th)/(2*mp.sin(th)**2)
        assert abs(trace-expected)<mp.mpf('1e-85')
        H=mp.diag([mp.sin((n+mp.mpf('.5'))*th) for n in range(a)])
        shift=2*H*D*H+2*mp.sin(th/2)**2*D
        gap=min(mp.eigsy(shift,eigvals_only=True))
        bound=4*mp.sin(th/2)**2*mp.sin(th)**2
        assert gap>=bound*(1-mp.mpf('1e-80'))
        rows.append(dict(N=N,a=a,min_root_gap=str(gap),proved_lower_bound=str(bound)))
        matrices+=1
    return dict(precision_digits=100,positive_original_endpoint_values=endpoints,
                exact_inverse_trace_and_gap_matrices=matrices,gap_rows=rows)


def disks():
    mp.mp.dps=100;count=0;worst=mp.mpf(0)
    for N in [8,9,16,17,32,33,64,65,129]:
        q=mp.exp(mp.pi*1j/N);d=N-1
        for a in sorted(set([1,d//4,d//2])):
            p2=transformed(d,a,q,mp.mpf(1))
            for phase in [1,-1,1j,-1j]:
                eps=mp.mpf('.02')*phase/N**3
                z=2+mp.mpf('.02')*phase/N**4
                Z=(z+mp.sqrt(z*z-4))/2
                actual=transformed(d,a,q*mp.exp(eps),Z)
                err=abs(actual/p2-1)
                assert err<mp.mpf('.5')
                worst=max(worst,err);count+=1
    return dict(actual_generic_joint_disk_samples=count,max_relative_change=str(worst))


def main():
    result=dict(status='PASS',exact=exact(),endpoint=positive_and_matrices(),joint_disk=disks(),
                scope='Actual polynomial positive endpoint, quantitative root separation, generic joint Sears identity and endpoint disks. No contour deformation, operator dominance or whole-source asymptotic.')
    Path(__file__).with_name('actual_matching_edge_polynomial_endpoint_control_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({**result,'endpoint':{k:v for k,v in result['endpoint'].items() if k!='gap_rows'}},indent=2))

if __name__=='__main__':main()
