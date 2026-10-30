#!/usr/bin/env python3
"""Exact complete disk-trace and endpoint-coordinate checks.

These are character identities, not a quantum concentration or
noncancellation proof for general augmented plats.
"""
import json
from pathlib import Path
import sympy as s


def main():
    a,b,c,d,t,u,ell,V=s.symbols('a b c d t u ell V', nonzero=True)
    P=s.Matrix([[a,b],[c,d]])
    C=s.Matrix([[1,1],[0,1]])
    comm=P*C-C*P
    assert comm==s.Matrix([[-c,a-d],[0,c]])
    restricted=P.subs({c:0,d:a})
    assert restricted.det()==a*a
    A=-s.Matrix([[1,t],[0,1]])
    B=-s.Matrix([[1,0],[u,1]])
    disk=B*A
    assert s.expand(s.trace(disk))==2+t*u
    assert s.trace(disk.subs(u,-4/t))==-2
    assert s.simplify((disk.subs(u,-4/t)+s.eye(2))**2)==s.zeros(2)
    # Hurwitz transport preserves the original ordered product exactly.
    Anew=A.inv()*B*A
    Bnew=A
    assert s.simplify(Bnew*Anew-disk)==s.zeros(2)
    trace=-(ell+1/ell)
    assert s.factor(trace+2)==-(ell-1)**2/ell
    assert s.diff(trace,ell).subs(ell,1)==0
    assert s.diff(trace,ell,2).subs(ell,1)==-2
    assert s.series(-2*s.cosh(V/2)+2,V,0,6)==-V**2/4-V**4/192+s.Order(V**6)
    theta_symbol=s.symbols('theta',real=True)
    assert s.trigsimp(2-2*s.cos(theta_symbol)-4*s.sin(theta_symbol/2)**2)==0
    rows=[]
    for N in range(2,19):
        j=(N-1)//2
        delta=N-1-2*j
        assert delta==(1 if N%2==0 else 0)
        theta=s.pi*delta/N
        node=2*s.cos((2*j+1)*s.pi/N)
        assert s.trigsimp(node+2*s.cos(theta))==0
        rows.append({'N':N,'last_folded_j':j,'delta':delta,
                     'sector':'simple' if N%2 else 'paired first normal'})
    result={'status':'PASS','parabolic_centralizer':'c=0,d=a,a^2=1',
            'noncommuting_common_trace_parabolics':'Tr(BA)=2+tu=-2',
            'trace_ramification':'c+2=-(ell-1)^2/ell',
            'root_endpoints':rows,
            'scope':'Exact geometric character and source-coordinate identities. No general quantum endpoint dominance, mixed-color packet, or volume equality is proved.'}
    Path(__file__).with_name('actual_augmented_plat_geometric_channel_endpoint_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS parabolic trace, exact Hurwitz product, square-root trace ramification and 17 parity endpoint checks')


if __name__=='__main__':
    main()
