#!/usr/bin/env python3
"""Exact original local Newton kernels and a certified polynomial-capacity obstruction.

The family is a certified matched graph, not a claimed flat-plat source
fixture. Coefficient limits are analytic proofs; finite profiles diagnose them.
"""
import argparse
import itertools
import json
from collections import defaultdict
from pathlib import Path
import mpmath as mp
import networkx as nx
import numpy as np
import sympy as sp
from audit_actual_small_circle_polynomial_face_insertion import Local, casimir, physical_colors
from audit_actual_smoothing_fixed_radius_gap import boundary_point, point_row, dot, lorentz, normalize, angles
from audit_actual_complete_circle_positive_face_polynomial import determinant_coefficients

def symbolic():
    q,K,R,I,J=sp.symbols('q K R I J',nonzero=True)
    s=lambda z:(z-z**-1)/sp.I
    lhs=s(K/R)*s(q*R/I)*s(q*R/J)
    lhs+=s(q*K)*(s(I)*s(q*R/J)+s(J)*s(q*R/I))
    lhs+=s(q*q*K*R)*s(I)*s(J)
    rhs=s(K*I*J/R)*s(q*R)**2
    assert sp.cancel(lhs-rhs)==0
    assert sp.cancel(s(K*q*q*R)*s(q*K)-s(K)*s(q**3*K*R)-s(q)*s(q*q*R))==0
    return 2


def original_newton():
    counts=dict(original_newton_monomial_paths=0,high_total_paths=0,
                preserved_N_blocks=0,actual_low_color_matrix_entries=0,
                actual_complete_matrix_entries=0,
                numerator_zero_coefficients=0,positive_coefficients=0)
    for N in range(3,10):
        loc=Local(N);p,q,Q,d=loc.p,loc.q,loc.Q,loc.d
        ii=pow(loc.eta,N,p)
        sn=lambda k:ii*(pow(q,-k,p)-pow(q,k,p))%p
        S=[1]
        for k in range(1,N):S.append(S[-1]*sn(k)%p)
        def choose(n,r):
            if n<r:return 0
            out=1
            for k in range(1,r+1):out=out*sn(n-r+k)*pow(sn(k),-1,p)%p
            return out
        O=casimir(loc);ident=np.eye(N*N,dtype=np.int64)
        Bs=[ident]
        for r in range(d):
            cr=(pow(q,2*r+1,p)+pow(q,-2*r-1,p))%p
            Bs.append((cr*ident-O)@Bs[-1]%p*pow(sn(r+1)**2,-1,p)%p)
        for m in range(N):
            for r in range(N):
                for a in range(r+1):
                    for b in range(r+1):
                        if a+b>m:continue
                        v=choose(m,r)*choose(m+r-a-b,r)*choose(r,a)*choose(r,b)%p
                        if r>m or m+r-a-b>=N:
                            assert v==0;counts['numerator_zero_coefficients']+=1
                        else:
                            assert v!=0;counts['positive_coefficients']+=1
        for u,v in [(0,0),(0,d),(d,0),(d,d),(d//2,d//2),(d,d//2)]:
            xx=-q*pow(Q,u,p)%p; yy=-pow(q,-1,p)*pow(Q,-v,p)%p
            for m in list(range(N))+[N,N+1,2*N+1]:
                mm=m%N
                for r in range(N):
                    predicted=0
                    for a in range(r+1):
                        for b in range(r+1):
                            if a+b>mm:continue
                            co=choose(mm,r)*choose(mm+r-a-b,r)*choose(r,a)*choose(r,b)%p
                            predicted+=co*pow(xx,a,p)*pow(yy,b,p)
                    actual=0
                    for z in range(max(0,u+v-d),min(d,u+v)+1):
                        step=z-u
                        actual+=int(Bs[r][z*N+u+v-z,u*N+v])*pow(q,d*step,p)*pow(Q,-step*m,p)
                    assert actual%p==predicted%p,(N,u,v,m,r,actual%p,predicted%p)
                    counts['original_newton_monomial_paths']+=1
                    counts['high_total_paths']+=u+v>d
                    counts['preserved_N_blocks']+=m>=N
        colors=physical_colors(loc)
        for h in range(1,N//2+1):
            test=np.zeros_like(O)
            for r in range(h):
                br=S[r]**2*S[h+r]*pow(S[2*r+1]*S[h-r-1],-1,p)%p
                test=(test+pow(-1,h-1+r)*br*Bs[r])%p
            assert np.array_equal(test,colors[h])
            counts['actual_low_color_matrix_entries']+=N**4
        test=np.zeros_like(O)
        for v in range((d//2)+1):
            co=N*N*S[2*v]*pow(S[v]**4,-1,p)%p
            test=(test+co*Bs[d-v])%p
        assert np.array_equal(test,colors[N]);counts['actual_complete_matrix_entries']+=N**4
    return counts


def family(n):
    triangles=[(p,j,(j+1)%4) for p in (4,5) for j in range(4)]
    circles={0:(mp.mpc(0,'.5'),mp.mpf('.5')),1:(mp.mpc(0,'1.5'),mp.mpf('.5')),
             4:(mp.mpc(-mp.sqrt(2),1),mp.mpf(1)),5:(mp.mpc(mp.sqrt(2),1),mp.mpf(1))}
    matching={(0,1),(1,2),(3,4),(3,5)}
    last=[]
    for side,old in ((-1,4),(1,5)):
        prev=old
        for j in range(1,n+1):
            B=4*j*j+4*mp.sqrt(2)*j+1;new=max(circles)+1
            circles[new]=(mp.mpc(side*(2*j+mp.sqrt(2))/B,1),1/B)
            triangles.remove(next(t for t in triangles if set(t)=={0,1,prev}))
            triangles.extend([(0,1,new),(1,prev,new),(prev,0,new)])
            matching.add(tuple(sorted((prev,new))));prev=new
        last.append(prev)
    edges=defaultdict(list)
    for i,t in enumerate(triangles):
        for j in range(3):edges[tuple(sorted((t[j],t[(j+1)%3])))].append(i)
    return triangles,circles,matching,edges,last


def graph_and_rounding():
    counts=dict(certified_matched_graphs=0,matching_vertices=0,white_supports=0,
                shaded_supports=0,right_angles=0,shared_face_equations=0,
                integral_flow_roundings=0,integer_rows=0,integer_fixed_columns=0,
                kernel_strict_domains=0)
    worst=mp.mpf(0)
    for n in (1,2,3,5):
        tri,circles,matching,edges,last=family(n)
        graph=nx.Graph();graph.add_nodes_from(range(len(tri)));graph.add_edges_from(edges.values())
        assert nx.node_connectivity(graph)==3
        assert all(len(ts)==2 for ts in edges.values())
        incidences=defaultdict(int)
        for e in matching:
            for v in edges[e]:incidences[v]+=1
        assert set(incidences)==set(graph) and set(incidences.values())=={1}
        counts['matching_vertices']+=len(incidences)
        assert (2,3) not in matching
        removed=set(edges[(0,1)]);remaining=graph.copy();remaining.remove_nodes_from(removed)
        assert nx.is_connected(remaining);counts['certified_matched_graphs']+=1
        points={e:point_row(boundary_point(e,circles)) for e in edges}
        white={2:[0,0,-1,4],3:[0,0,1,0]}
        white.update({f:[1,-mp.re(z),-mp.im(z),abs(z)**2-r*r] for f,(z,r) in circles.items()})
        white={f:normalize(v) for f,v in white.items()}
        for f,H in white.items():
            for edge,v in points.items():
                value=dot(H,v);counts['white_supports']+=1
                if f in edge:assert abs(value)<mp.mpf('1e-60');worst=max(worst,abs(value))
                else:assert value>mp.mpf('1e-60')
        for t in tri:
            te=[tuple(sorted((t[j],t[(j+1)%3]))) for j in range(3)]
            rows=[points[e] for e in te]
            H=[(-1)**j*mp.det(mp.matrix([[row[k] for k in range(4) if k!=j] for row in rows])) for j in range(4)]
            H=normalize(H)
            if dot(H,next(v for e,v in points.items() if e not in te))<0:H=[-v for v in H]
            for e,v in points.items():
                val=dot(H,v);counts['shaded_supports']+=1
                if e in te:assert abs(val)<mp.mpf('1e-60')
                else:assert val>mp.mpf('1e-60')
            for f in t:assert abs(lorentz(H,white[f]))<mp.mpf('1e-60');counts['right_angles']+=1
        curv={f:1/r for f,(_,r) in circles.items()}|{2:mp.mpf(0),3:mp.mpf(0)}
        corner={k:[z/(2*mp.pi) for z in angles([curv[f] for f in t])] for k,t in enumerate(tri)}
        totals=defaultdict(lambda:mp.mpf(0))
        for k,t in enumerate(tri):
            for f,a in zip(t,corner[k]):totals[f]+=a
        for f in curv:
            assert abs(totals[f]-(0 if f in (2,3) else 1))<mp.mpf('1e-65')
            counts['shared_face_equations']+=1
        b,c=last;aa=2/mp.pi*mp.atan(1/mp.sqrt(curv[b]+1))
        remcols=defaultdict(lambda:mp.mpf(0))
        for k,t in enumerate(tri):
            if k in removed:continue
            for f,a in zip(t,corner[k]):remcols[f]+=a
        for f,expected in ((0,1-aa),(1,1-aa),(b,mp.mpf('.5')+aa),(c,mp.mpf('.5')+aa)):
            assert abs(remcols[f]-expected)<mp.mpf('1e-65');counts['shared_face_equations']+=1
        if n<3:continue
        for N in (257,513,1025):
            d=N-1;M=d//2;exception={0,1,b,c};network=nx.DiGraph();floors={};raw={}
            rows=[k for k in range(len(tri)) if k not in removed]
            for k in rows:
                for j,f in enumerate(tri[k]):
                    v=d*corner[k][j];raw[k,f]=v
                    floors[k,f]=int(mp.floor(v+mp.mpf('1e-65')))
            demands={}
            for k in rows:demands['t',k]=-(M-sum(floors[k,f] for f in tri[k]))
            for f in curv:
                demands['f',f]=0 if f in exception else (0 if f in(2,3) else d)-sum(v for (k,ff),v in floors.items() if ff==f)
            demands['sink',0]=-sum(demands.values())
            for node,dem in demands.items():network.add_node(node,demand=dem)
            for (k,f),v in raw.items():
                hi=int(mp.ceil(v-mp.mpf('1e-65')))
                network.add_edge(('t',k),('f',f),capacity=max(0,hi-floors[k,f]),weight=0)
            for f in exception:network.add_edge(('f',f),('sink',0),capacity=10*len(tri),weight=0)
            _,flows=nx.network_simplex(network)
            rounded={(k,f):v+flows['t',k]['f',f] for (k,f),v in floors.items()}
            for k in rows:assert sum(rounded[k,f] for f in tri[k])==M;counts['integer_rows']+=1
            cols={f:sum(v for (k,ff),v in rounded.items() if ff==f) for f in curv}
            for f in curv:
                if f not in exception:assert cols[f]==(0 if f in(2,3) else d);counts['integer_fixed_columns']+=1
            assert all(abs(rounded[key]-raw[key])<=1+mp.mpf('1e-60') for key in raw)
            m=cols[c];i=d-cols[0];j=d-cols[1];r=N//4
            assert cols[b]+m-i-j==d
            assert 0<i<r<m<N and 0<j<r and i+j<m and m+r-i-j<N,(n,N,m,i,j,r)
            counts['kernel_strict_domains']+=1;counts['integral_flow_roundings']+=1
    return counts|{'maximum_support_incidence_error':str(worst)}


def profiles():
    lob=lambda x:mp.im(mp.polylog(2,mp.exp(2j*x)))/2
    J=lambda x:-lob(mp.pi*x)/mp.pi
    V=lambda th:2*sum(lob(mp.pi*t/2)+lob(mp.pi*(1-t)/2) for t in th)
    rows=[]
    for n in (1,2,3,5,10,30,100):
        B=4*n*n+4*mp.sqrt(2)*n+1;a=2/mp.pi*mp.atan(1/mp.sqrt(B+1));mu=mp.mpf('.5')+a;r=mp.mpf('.25')
        K=J(mu)+J(mu+r-2*a)-J(mu-r)-J(mu-2*a)-2*J(a)-2*J(r-a)
        E=K-V((a,1-2*a,a))/mp.pi
        if n>=3:assert E>0
        rows.append(dict(depth=n,corner_fraction=str(a),entropy_excess=str(E)))
    coefficient_rows=[]
    for N in (17,33,65):
        M=(N-1)//2;dc=determinant_coefficients(N,M)
        for fractions in ((mp.mpf('.25'),mp.mpf('.5')),(mp.mpf('.1'),mp.mpf('.2')),(mp.mpf(0),mp.mpf('.4')),
                          (mp.mpf(1),mp.mpf(0)),(mp.mpf(0),mp.mpf(1)),(mp.mpf(0),mp.mpf(0))):
            i=int(mp.floor(M*fractions[0]));j=int(mp.floor(M*fractions[1]));k=M-i-j
            val=dc[i,j,k];assert val>0
            theta=(mp.mpf(i)/M,mp.mpf(j)/M,mp.mpf(k)/M)
            rate=V(theta)/(2*mp.pi)
            err=(mp.log(val)-N*rate)/mp.log(N)
            assert abs(err)<10
            coefficient_rows.append(dict(N=N,exponents=[i,j,k],logN_scaled_rate_error=str(err)))
    return dict(entropy_profiles_diagnostic=rows,analytic_limit=str(2*mp.catalan/mp.pi),
                literal_triangle_coefficients=len(coefficient_rows),coefficient_profiles_diagnostic=coefficient_rows)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='experiments/actual_positive_newton_capacity_obstruction_results.json')
    args=ap.parse_args();mp.mp.dps=80
    data=dict(status='PASS',precision_digits=80,symbolic=symbolic(),original_local=original_newton(),
              certified_graph=graph_and_rounding(),profiles=profiles(),
              scope='Original local Casimir/Newton identities and certified matched-graph positive-polynomial obstruction. No flat-plat adapter for the insertion family is claimed; whole original-source obstruction is conditional on it. Limiting rates follow from the written proofs, not these diagnostics.')
    Path(args.output).write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))


if __name__=='__main__':main()
