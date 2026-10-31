#!/usr/bin/env python3
"""Literal L1 source, explicit labeled packing, and fixed-radius test.

The negative examples concern only the fixed OLD-radii sufficient test.
They do not compute or disprove the fully optimized smoothed capacity.
"""
import argparse
from collections import defaultdict
import json
from pathlib import Path

import mpmath as mp
import networkx as nx
import numpy as np
import sympy as sp

from audit_actual_original_marked_face_coefficient import (
    add, local_polynomials, morse_faces, mul, substitute,
)
from audit_actual_nc_morse_graph_first_normal_source_reduction import Local
from original_source_tensor import apply_pair


def original_source_checks():
    rows=[]
    for N in (3,4):
      for k,boxes in ((2,[1,0,2,1]),(2,[1,0,2,1,0,2,1])):
        loc=Local(N);p=loc.p;d=N-1;M=d//2;old=morse_faces(k,boxes)
        imag=pow(loc.eta,N,p)
        S=[pow(imag,j,p)*pow(loc.q,-j*(j+1)//2,p)*loc.fac[j]%p for j in range(N)]
        beta=[S[2*a]*pow(S[a]**2,-1,p)%p for a in range(M+1)]
        polys={a:local_polynomials(loc,a) for a in range(M+1)}
        for deletion,(x,b,c,y) in enumerate(old['circles']):
            if b==c or b in(0,old['v']) or c in(0,old['v']):continue
            shorter=boxes[:deletion]+boxes[deletion+1:]
            if 1 not in shorter:continue
            new=morse_faces(k,shorter,old['marked'])
            variables=[f for f in range(new['faces']) if f not in(0,new['v'])]
            signs=[(-1,0,1)[j%3] for j in range(len(boxes))];signs[deletion]=0
            state=np.array([1],dtype=np.int64);mark=np.array([1],dtype=np.int64)
            marker=np.array([[pow(loc.x,j,p)*pow(N*N,-1,p)%p for j in range(N)] for i in range(N)],dtype=np.int64)
            for j in range(k):
                state=np.kron(state,loc.cup[0].reshape(-1))%p
                mark=np.kron(mark,(marker if j==old['marked'] else loc.cap[0]).reshape(-1))%p
            state=state.reshape((N,)*(2*k));product={(0,)*len(variables):1};r=0
            for j,(slot,eps) in enumerate(zip(boxes,signs)):
                if j==deletion:
                    state=apply_pair(np.eye(N*N,dtype=np.int64),state,slot,N,p)
                    continue
                coupon=np.zeros((N*N,N*N),dtype=np.int64);polynomial={}
                x,b,c,y=new['circles'][r];r+=1
                for a in range(M+1):
                    unit=pow(loc.omega[a],eps,p)
                    coupon=(coupon+loc.h0[a]*unit%p*(loc.W[a][0]@loc.pi[a][0]%p))%p
                    D,P=polys[a];local={(0,)*len(variables):1}
                    for poly,ids in [(D,(x,b,y)),(D,(x,c,y)),(P,(x,y))]:
                        local=mul(local,substitute(poly,ids,variables,p),p,d)
                    ka=1 if 2*a==d else 2
                    polynomial=add(polynomial,local,p,ka*beta[a]**2*unit%p)
                state=apply_pair(coupon,state,slot,N,p)
                product=mul(product,polynomial,p,d)
            actual=int(mark@state.reshape(-1)%p)
            expected=pow(N,len(shorter),p)*product.get((d,)*len(variables),0)%p
            assert actual==expected
            rows.append({'N':N,'original_boxes':len(boxes),'deleted_slot_index':deletion,
                         'literal_L1_source':actual,'shorter_coefficient_source':expected,'field':p})
    assert rows
    return {'literal_marked_L1_sources':len(rows),'cases':rows,
            'scope':'Whole original source with exactly one untwisted identity port; every retained half-twist phase, cup, mark and shorter N-power measure remains.'}


def family(n):
    tri=[(p,j,(j+1)%4) for p in(4,5) for j in range(4)]
    circles={0:(mp.mpc(0,'.5'),mp.mpf('.5')),1:(mp.mpc(0,'1.5'),mp.mpf('.5')),
             4:(mp.mpc(-mp.sqrt(2),1),mp.mpf(1)),5:(mp.mpc(mp.sqrt(2),1),mp.mpf(1))}
    matching={(0,1),(1,2),(3,4),(3,5)};prev=5
    for j in range(1,n+1):
        B=4*j*j+4*mp.sqrt(2)*j+1;new=5+j
        circles[new]=(mp.mpc((2*j+mp.sqrt(2))/B,1),1/B)
        tri.remove(next(t for t in tri if set(t)=={0,1,prev}))
        tri.extend([(0,1,new),(1,prev,new),(prev,0,new)])
        matching.add(tuple(sorted((prev,new))));prev=new
    edges=defaultdict(list)
    for i,t in enumerate(tri):
        for j in range(3):edges[tuple(sorted((t[j],t[(j+1)%3])))].append(i)
    return tri,circles,matching,edges


def boundary_point(edge,circles):
    f,g=edge
    if edge==(2,3):return None
    if f in(2,3) or g in(2,3):
        line=f if f in(2,3) else g;circle=g if f in(2,3) else f
        z,r=circles[circle];return mp.mpc(mp.re(z),2 if line==2 else 0)
    z,r=circles[f];w,s=circles[g]
    assert abs(abs(z-w)-r-s)<mp.mpf('1e-65')
    return (s*z+r*w)/(r+s)


def point_row(z):
    return [mp.mpf(1),mp.mpf(0),mp.mpf(0),mp.mpf(0)] if z is None else [abs(z)**2,2*mp.re(z),2*mp.im(z),mp.mpf(1)]


def dot(a,b):return mp.fsum(x*y for x,y in zip(a,b))
def lorentz(a,b):return (a[0]*b[3]+a[3]*b[0])/2-a[1]*b[1]-a[2]*b[2]
def normalize(a):return [v/mp.sqrt(-lorentz(a,a)) for v in a]


def geometric_certificate():
    nvar=sp.symbols('n',integer=True,positive=True)
    B=lambda n:4*n*n+4*sp.sqrt(2)*n+1
    x=lambda n:(2*n+sp.sqrt(2))/B(n)
    assert sp.simplify(x(nvar)**2-1/B(nvar)**2-1/B(nvar))==0
    assert sp.simplify(x(nvar-1)-x(nvar)-1/B(nvar-1)-1/B(nvar))==0
    counts=dict(symbolic_tangencies=2,matching_covers=0,three_connected_graphs=0,
                connected_literal_smoothings=0,white_support_values=0,shaded_support_values=0,
                original_right_angle_checks=0)
    worst=mp.mpf(0);min_slack=mp.inf
    for n in range(9):
        tri,circles,matching,edges=family(n)
        assert all(len(t)==2 for t in edges.values())
        graph=nx.Graph();graph.add_nodes_from(range(len(tri)));graph.add_edges_from(edges.values())
        assert nx.node_connectivity(graph)==3;counts['three_connected_graphs']+=1
        incident=defaultdict(int)
        for e in matching:
            for v in edges[e]:incident[v]+=1
        assert set(incident)==set(graph) and set(incident.values())=={1}
        assert (2,3) not in matching;counts['matching_covers']+=1
        removed=edges[(0,1)];remain=graph.copy();remain.remove_nodes_from(removed)
        assert nx.is_connected(remain);counts['connected_literal_smoothings']+=1
        points={e:point_row(boundary_point(e,circles)) for e in edges}
        white={2:[0,0,-1,4],3:[0,0,1,0]}
        for f,(z,r) in circles.items():white[f]=[1,-mp.re(z),-mp.im(z),abs(z)**2-r*r]
        white={f:normalize(v) for f,v in white.items()}
        for f,H in white.items():
            for edge,v in points.items():
                val=dot(H,v);counts['white_support_values']+=1
                if f in edge:worst=max(worst,abs(val));assert abs(val)<mp.mpf('1e-60')
                else:assert val>mp.mpf('1e-60');min_slack=min(min_slack,val)
        for t in tri:
            te=[tuple(sorted((t[j],t[(j+1)%3]))) for j in range(3)]
            rows=[points[e] for e in te]
            H=[(-1)**j*mp.det(mp.matrix([[row[k] for k in range(4) if k!=j] for row in rows])) for j in range(4)]
            H=normalize(H)
            test=next(v for e,v in points.items() if e not in te)
            if dot(H,test)<0:H=[-v for v in H]
            for e,v in points.items():
                val=dot(H,v);counts['shaded_support_values']+=1
                if e in te:worst=max(worst,abs(val));assert abs(val)<mp.mpf('1e-60')
                else:assert val>mp.mpf('1e-60');min_slack=min(min_slack,val)
            for f in t:
                error=abs(lorentz(H,white[f]));worst=max(worst,error)
                assert error<mp.mpf('1e-60');counts['original_right_angle_checks']+=1
    counts.update(maximum_incidence_orthogonality_error=str(worst),minimum_strict_support_slack=str(min_slack))
    return counts


def angles(L):
    delta=mp.sqrt(L[0]*L[1]+L[1]*L[2]+L[2]*L[0])
    return [2*mp.atan2(l,delta) for l in L]


def F(*L):
    L=list(map(mp.mpf,L));th=angles(L)
    lob=lambda t:mp.im(mp.polylog(2,mp.exp(2j*t)))/2
    entropy=2*mp.fsum(lob(t/2)+lob((mp.pi-t)/2) for t in th)
    return (mp.fsum(t*mp.log(l) for t,l in zip(th,L) if l)+entropy)/(2*mp.pi)


def capacity_profiles():
    rows=[];K=F(2,1,2)+2*F(2,1,0)-mp.mpf('1.5')*mp.log(2)
    for n in (1,2,3,5,10,30,100):
        B=4*n*n+4*mp.sqrt(2)*n+1;prev=4*(n-1)**2+4*mp.sqrt(2)*(n-1)+1
        C=F(2,B,2)+2*F(2,prev,B)+F(2,1,2)+2*F(2,1,0)-mp.log(B)
        derivative=lambda s:mp.mpf('.5')-(angles([2,prev,mp.exp(s)])[2]+angles([2,mp.exp(s),0])[1])/mp.pi
        lo=mp.mpf(-10);hi=mp.mpf(10)
        assert derivative(lo)>0 and derivative(hi)<0
        for _ in range(260):
            mid=(lo+hi)/2
            if derivative(mid)>0:lo=mid
            else:hi=mid
        s=(lo+hi)/2;z=mp.exp(s)
        gap=C-2*F(2,prev,z)-2*F(2,z,0)+s/2
        assert abs(derivative(s))<mp.mpf('1e-65')
        assert (gap>0)==(n<=3)
        rows.append({'insertions':n,'new_curvature':str(B),'optimal_merged_radius':str(z),
                     'best_fixed_old_radius_gap':str(gap),
                     'gap_plus_log_n_minus_limit':str(gap+mp.log(n)-K)})
    # A concrete positive test remains positive after BOTH marked faces
    # are made fixed positive variables, with their targets still zero.
    n=1;tri,circles,matching,edges=family(n);L={f:1/r for f,(z,r) in circles.items()};L[2]=L[3]=0
    old=mp.fsum(F(*(L[f] for f in t)) for t in tri)-mp.fsum(mp.log(v) for v in L.values() if v)
    z=mp.mpf(rows[0]['optimal_merged_radius']);L[4]=L[6]=z
    remain=[t for t in tri if not(0 in t and 1 in t)]
    free=set(L)-{2,3,4}
    atzero=mp.fsum(F(*(L[f] for f in t)) for t in remain)-mp.fsum(mp.log(L[f]) for f in free)
    assert abs(old-atzero-mp.mpf(rows[0]['best_fixed_old_radius_gap']))<mp.mpf('1e-60')
    L[2]=L[3]=mp.mpf('1e-8')
    regular=mp.fsum(F(*(L[f] for f in t)) for t in remain)-mp.fsum(mp.log(L[f]) for f in free)
    assert regular<old-(old-atzero)/2
    return {'exact_radical_family_profiles':len(rows),'limit_constant':str(K),'profiles':rows,
            'fixed_positive_marked_radius_checks':1,'regularized_gap':str(old-regular),
            'scope':'Analytic proof supplies the all-n obstruction; finite optimal gaps diagnose its normalization. Full smoothed capacities are not computed.'}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='experiments/actual_smoothing_fixed_radius_gap_results.json');args=ap.parse_args()
    mp.mp.dps=80
    data={'status':'PASS','precision_digits':80,'source':original_source_checks(),
          'certificate':geometric_certificate(),'capacity':capacity_profiles(),
          'scope':'Actual L1 marked source and finite measures; labeled positive circle/ideal-plane certificates and perfect matchings; fixed-old-radius sufficient gaps and their explicit counterfamily. No universal smoothing gap, L_h charged-alias estimate, or filled-source claim.'}
    Path(args.output).write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))


if __name__=='__main__':main()
