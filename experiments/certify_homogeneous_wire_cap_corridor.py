#!/usr/bin/env python3
"""Outward continuum certificate for a directed complete-cap wire corridor.

Numerical roots select rational circle centers only. Every accepted
parameter box has a uniform analytic Rouche certificate, a common
univalence rectangle, and strict scalar contour inequalities.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

import mpmath as mp
from flint import acb, arb, ctx


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=192)
    parser.add_argument("--max-boxes", type=int, default=16384)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    ctx.prec = args.precision
    mp.mp.dps = 50
    pi, ii = arb.pi(), acb(0, 1)
    y0 = arb(2).log()/(2*pi)
    initial = (Q(0), Q(13,1000), Q(-3,2000), Q(1,1000))
    global_t = acb(arb(619)/400 + arb(0, arb(11)/400),
                   -arb(197)/200 + arb(0, arb(3)/200))

    def rat(q):
        return arb(q.numerator)/q.denominator

    def interval(lo, hi):
        return rat((lo+hi)/2)+arb(0,rat((hi-lo)/2))

    def qwire(x):
        return 1/(pi*x).tan()

    def period(t,x):
        z=(t/2).tan(); sec=1/(t/2).cos(); q=qwire(x)
        return 3*t+2*ii*(z+sec).log()+ii*((q+z).log()-(q-z).log())-2*pi

    def first(t,x):
        z=(t/2).tan(); sec=1/(t/2).cos(); q=qwire(x)
        return 3+ii*(sec+((q/(q-z))*sec*sec)/(q+z))

    def second(t,x):
        z=(t/2).tan(); sec=1/(t/2).cos(); q=qwire(x)
        dz=(1+z*z)/2; ddz=z*(1+z*z)/2
        inv=1/(q-z)/(q+z)
        return 2*ii*(sec*z/4+q*(ddz*inv+2*z*dz*dz*inv*inv))

    def wire_derivative(t,x):
        z=(t/2).tan();q=qwire(x)
        return 2*pi*ii*z*(1+q*q)/(q-z)/(q+z)

    def J(z):
        z=acb(z)
        return -ii*pi*(z*z-z)/2+ii*(2*ii*pi*z).exp().polylog(2)/(2*pi)-ii*pi/12

    def b(x,t):
        return -J(arb(1)/2-x+t/(2*pi))-J(arb(1)/2-x-t/(2*pi))-2*J(x)

    def phase(x,t):
        return (b(x,t)-4*J(arb(1)/4+t/(4*pi))-4*J(arb(1)/4-t/(4*pi))
                +3*ii*t*t/(4*pi)-ii*t)

    def attempt(box):
        ul,uh,vl,vh=box
        U,V=interval(ul,uh),interval(vl,vh)
        x=acb(arb(1)/6+U,y0-arb(4)/5*U+V)
        uc,vc=(ul+uh)/2,(vl+vh)/2
        xm=mp.mpf(1)/6+mp.mpf(uc.numerator)/uc.denominator+1j*(mp.log(2)/(2*mp.pi)
             -mp.mpf(4)/5*mp.mpf(uc.numerator)/uc.denominator+mp.mpf(vc.numerator)/vc.denominator)
        qm=1/mp.tan(mp.pi*xm)
        def fm(t):
            z=mp.tan(t/2); sec=1/mp.cos(t/2)
            return 3*t+2j*mp.log(z+sec)+1j*(mp.log(qm+z)-mp.log(qm-z))-2*mp.pi
        root=mp.findroot(fm,1.55-.985j)
        cr=Q(int(mp.nint(root.real*10**12)),10**12)
        ci=Q(int(mp.nint(root.imag*10**12)),10**12)
        center=acb(rat(cr),rat(ci))
        xcenter=acb(arb(1)/6+rat(uc),y0-arb(4)/5*rat(uc)+rat(vc))
        radius_q=4*((uh-ul)+(vh-vl))+Q(1,10**8)
        radius=rat(radius_q)
        t=acb(center.real+arb(0,radius),center.imag+arb(0,radius))
        conditions={}

        def margin(name,value):
            if not value>0:
                raise ValueError(name)
            conditions[name]=str(value)

        # A uniform positive real derivative in one common convex t
        # rectangle identifies all local circles as the same branch.
        q=qwire(x); zg=(global_t/2).tan(); sg=1/(global_t/2).cos()
        margin('global log q+z',(q+zg).real)
        margin('global log q-z',(q-zg).real)
        margin('global log sec+z',(sg+zg).real)
        margin('common-rectangle univalence',first(global_t,x).real)
        margin('root circle real lower',t.real-arb(38)/25)
        margin('root circle real upper',arb(63)/40-t.real)
        margin('root circle height lower',-t.imag-arb(97)/100)
        margin('root circle height upper',1+t.imag)

        base=first(center,xcenter)
        half_u,half_v=rat((uh-ul)/2),rat((vh-vl)/2)
        parameter_radius=(half_u**2+(arb(4)/5*half_u+half_v)**2).sqrt()
        residual=abs(period(center,xcenter))+abs(wire_derivative(center,x))*parameter_radius
        error=(residual+abs(first(center,x)-base)*radius
               +abs(second(t,x))*radius**2/2)
        margin('uniform Rouche',abs(base)*radius-error)
        H=-t.imag
        margin('saddle below pi/2',pi/2-t.real)
        margin('saddle height dominates wire',H-2*pi*x.imag)
        margin('saddle height below 107/100',arb(107)/100-H)
        margin('saddle cosine modulus',1-abs((t/2).cos()))
        margin('saddle negative real Hessian',-(ii*first(t,x)/(2*pi)).real-arb(1)/4)

        T=pi-2*pi*x.real-arb(1)/50
        margin('cut above pi/2',T-pi/2)
        margin('cut below 2pi/3',2*pi/3-T)
        margin('spectral half-plane reserve',arb(7)/4+2*T.cos()*H.cosh())
        margin('angular alpha condition',1+T.cos()*H.cosh())
        margin('wire alpha condition',1-(2*pi*x.real).cos()*(2*pi*x.imag).cosh())
        # Avoid first-order loss from the root enclosure: F_t vanishes
        # at the root, and its integral from the rational center gives
        # this uniform second-order phase uncertainty.
        phase_error=(residual*radius/(2*pi)
                     +abs(first(t,x))*radius**2/(4*pi))
        M=phase(x,center).real-arb(0,phase_error)
        margin('radical gap above 1/2',M-b(x,acb(0)).real-arb(1)/2)
        margin('real endpoint gap above 1/1000',M-phase(x,acb(T)).real-arb(1)/1000)
        margin('bottom endpoint gap above 1/1000',M-phase(x,acb(T,-H)).real-arb(1)/1000)
        return {'parameter_box':[str(v) for v in box],
                'center':[str(cr),str(ci)],'radius':str(radius_q),
                'positive_margins':conditions}

    pending=[initial]; accepted=[]; visited=0; failures={}
    while pending:
        box=pending.pop(); visited+=1
        if visited>args.max_boxes:
            raise RuntimeError(f'bounded certificate budget exceeded: accepted={len(accepted)}, pending={len(pending)}, last_box={box}, failures={failures}')
        try:
            record=attempt(box)
        except (ValueError,ZeroDivisionError) as error:
            key=str(error);failures[key]=failures.get(key,0)+1
            ul,uh,vl,vh=box
            if uh-ul>=vh-vl:
                mid=(ul+uh)/2; pending.extend([(ul,mid,vl,vh),(mid,uh,vl,vh)])
            else:
                mid=(vl+vh)/2; pending.extend([(ul,uh,vl,mid),(ul,uh,mid,vh)])
        else:
            accepted.append(record)

    # Independent exact vertical sweep verifies multiplicity-one
    # coverage of the stored parameter rectangles (apart from faces).
    leaves=[tuple(Q(v) for v in r['parameter_box']) for r in accepted]
    cuts=sorted(set([initial[0],initial[1]]+[v for box in leaves for v in box[:2]]))
    for left,right in zip(cuts,cuts[1:]):
        mid=(left+right)/2
        intervals=sorted((vl,vh) for ul,uh,vl,vh in leaves if ul<mid<uh)
        endpoint=initial[2]
        for lo,hi in intervals:
            assert lo==endpoint and hi>lo
            endpoint=hi
        assert endpoint==initial[3]
    assert cuts[0]==initial[0] and cuts[-1]==initial[1]

    task_root=Path(__file__).resolve().parents[1]
    deps=[Path(__file__).resolve(),task_root/'notes/research_homogeneous_wire_complete_cap.md',
          task_root/'experiments/check_homogeneous_wire_complete_cap.py']
    result={'status':'passed','precision_bits':ctx.prec,'parameter_domain':[str(v) for v in initial],
            'wire_map':'x=1/6+u+i(log(2)/(2pi)-4u/5+v)',
            'cut':'T=pi-2pi Re(x)-1/50',
            'common_t_rectangle':'Re(t) in [38/25,63/40], -Im(t) in [97/100,1]',
            'accepted_count':len(accepted),'visited_count':visited,
            'exact_coverage':'multiplicity-one rational sweep passed',
            'scope':'Uniform analytic period zero and scalar hypotheses of the cap proof on a fixed directed parameter corridor; no composed-wire saddle or full open-chain contour claim.',
            'accepted':accepted,
            'sha256':{str(p.relative_to(task_root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in deps}}
    out=args.output or task_root/'repro/results/research-homogeneous-wire-cap-corridor.json'
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n')
    print(f'Passed {len(accepted)} boxes, {visited} visits, exact rational cover at {ctx.prec} bits.\n{out}')


if __name__=='__main__':main()
