#!/usr/bin/env python3
"""Literal Q1 cabling, flow polynomial and original fixed-normal graph sources.

All finite checks are exact in prime fields. The all-graph proof is the
signed ribbon-state expansion and elementary deletion/contraction argument
in the note; no polynomial fit or vanishing-order extrapolation is used.
"""
import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_trivalent_complete_circle_vertex_kernel import (
    axis_apply, contract, matching, noncrossing,
    theta_graph, ordered_cube_graph,
)
from audit_actual_trivalent_full_cd_normalization_and_magnetic_growth import (
    ordinary, canonical_three_j,
)
from audit_actual_nc_morse_graph_first_normal_source_reduction import (
    Local, contract_jet, graph_case, module_jet, ordered_dipole_graph,
)


def incidence(graph):
    ports, black, _ = graph
    edges = {}
    for v, es in ports.items():
        for e in es:
            edges.setdefault(e, []).append(v)
    assert sorted(edges) == list(range(len(edges)))
    assert all(len(vs) == 2 and ((vs[0] in black) != (vs[1] in black))
               for vs in edges.values())
    return [tuple(edges[e]) for e in range(len(edges))]


def components(vertices, edges):
    parent = {v: v for v in vertices}
    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v
    for a, b in edges:
        a, b = find(a), find(b)
        parent[a] = b
    return len({find(v) for v in vertices})


def flow_coefficients(graph):
    vertices = list(graph[0])
    edges = incidence(graph)
    out = [0]*(len(edges)-len(vertices)+2)
    for mask in range(1 << len(edges)):
        active = [edge for e, edge in enumerate(edges) if mask >> e & 1]
        exponent = len(active)-len(vertices)+components(vertices, active)
        out[exponent] += (-1)**(len(edges)-len(active))
    return out


def polynomial_product(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def evaluate(a, x):
    return sum(c*x**k for k, c in enumerate(a))


def derivative(a, x):
    return sum(k*c*x**(k-1) for k, c in enumerate(a) if k)


def cable(q, p):
    qi = pow(q, -1, p)
    d0 = (q+qi) % p
    cup = np.array([[0, 1], [-qi % p, 0]], dtype=np.int64)
    cap = np.array([[0, -q % p], [1, 0]], dtype=np.int64)
    delta = -d0 % p
    e = np.outer(cup.reshape(-1), cap.reshape(-1)) % p
    Pi = (np.eye(4, dtype=np.int64)-e*pow(delta, -1, p)) % p
    i = np.array([[1,0,0], [0,qi,0], [0,1,0], [0,0,qi]], dtype=np.int64)
    pi = np.array([[1,0,0,0], [0,pow(d0,-1,p),q*pow(d0,-1,p)%p,0],
                   [0,0,0,q]], dtype=np.int64)
    assert np.array_equal(pi@i % p, np.eye(3, dtype=np.int64))
    assert np.array_equal(i@pi % p, Pi)
    E,F,K=(A[0] for A in module_jet(1,q,p))
    EQ,FQ,KQ=ordinary(1,q,p)
    Ki=np.diag([pow(int(z),-1,p) for z in np.diag(K)])
    physical=(np.kron(E,K)+np.kron(np.eye(2,dtype=np.int64),E),
              np.kron(F,np.eye(2,dtype=np.int64))+np.kron(Ki,F),
              np.kron(K,K))
    for A,B in zip(physical,(EQ,FQ,KQ)):
        assert np.array_equal(A@i%p,i@B%p)
        assert np.array_equal(pi@A%p,B@pi%p)
    Q = q*q % p
    pQ = np.array([[0,0,1], [0,-pow(1+Q,-1,p)%p,0],
                   [pow(q,-2,p),0,0]], dtype=np.int64)
    cQ = np.zeros_like(pQ)
    for a in range(3):
        cQ[2-a,a] = pow(int(pQ[a,2-a]),-1,p)
    P = np.eye(4,dtype=np.int64).reshape(2,2,2,2).transpose(1,0,2,3).reshape(4,4)
    dual_i = pQ.T@i.T % p@np.kron(cap.T,cap.T) % p@P % p
    assert np.array_equal(dual_i,qi*pi % p)
    theta = canonical_three_j((1,1,1), [ordinary(1,q,p)]*3, q, p)
    dual = theta.copy()
    for axis in range(3):
        dual = axis_apply(cQ,dual,axis,p)
    dual = dual.transpose(2,1,0)
    J = np.zeros((4,4,4),dtype=np.int64)
    ell = J.copy()
    for a,b,c in itertools.product(range(2),repeat=3):
        ids=(2*a+b,2*(1-b)+c,2*(1-c)+1-a)
        J[ids]=int(cup[a,1-a])*int(cup[b,1-b])*int(cup[c,1-c])%p
        ell[ids]=int(cap[a,1-a])*int(cap[b,1-b])*int(cap[c,1-c])%p
    black,white=J,ell
    for axis in range(3):
        black=axis_apply(pi,black,axis,p)
        white=axis_apply(i.T,white,axis,p)
    u=-pow(q,-2,p)*pow(d0,-1,p)%p
    assert np.array_equal(black,u*theta%p)
    assert np.array_equal(white,pow(q,-3,p)*u*dual%p)
    return cup,cap,Pi,theta,dual,d0


def primitive_cable_graph(graph, cup, cap, Pi, p):
    ports,black,_=graph
    E=len(incidence(graph))
    B=[ports[v] for v in ports if v in black]
    W=[ports[v] for v in ports if v not in black]
    assert noncrossing(B) and noncrossing(W)
    tensors=[]
    for e in range(E):
        tensors.append((Pi.reshape((2,)*4),(2*e,2*e+1,2*E+2*e,2*E+2*e+1)))
    tensors.extend((cup,(2*E+a,2*E+b)) for a,b in matching(B))
    tensors.extend((cap,(a,b)) for a,b in matching(W))
    return contract(tensors,p)


def spin_graph(graph, theta, dual, p):
    ports,black,_=graph
    return contract([(theta if v in black else dual,es) for v,es in ports.items()],p)


def insert_cube(graph, vertex):
    ports,black,marked=graph
    interval=ports[vertex]
    assert vertex in black and tuple(range(interval[0],interval[0]+3))==interval
    start=interval[0]
    template=ordered_cube_graph()
    glued=(0,10,11)
    def old_edge(e):
        if e<start:return e
        if e>start+2:return e+9
        return start+glued[e-start]
    out={v:tuple(old_edge(e) for e in es) for v,es in ports.items() if v!=vertex}
    new_black=set(black)-{vertex}
    offset=max(ports)+1
    for v,es in template[0].items():
        if v==4:continue
        out[offset+v]=tuple(start+e for e in es)
        if v in template[1]:new_black.add(offset+v)
    result=(out,new_black,marked)
    assert noncrossing([out[v] for v in out if v in new_black])
    assert noncrossing([out[v] for v in out if v not in new_black])
    matching([out[v] for v in out if v in new_black])
    matching([out[v] for v in out if v not in new_black])
    return result,(offset,offset+3)


def three_edge_connected(graph):
    vertices=list(graph[0]);edges=incidence(graph)
    for r in (0,1,2):
        for deleted in itertools.combinations(range(len(edges)),r):
            if components(vertices,[e for i,e in enumerate(edges) if i not in deleted])!=1:
                return False
    return True


if __name__=='__main__':
    base_graphs=[('theta',theta_graph()),('dipole',ordered_dipole_graph()),('cube',ordered_cube_graph())]
    polys={name:flow_coefficients(graph) for name,graph in base_graphs}
    assert polys['theta']==[2,-3,1]
    assert polys['dipole']==[-4,8,-5,1]
    H=[-32,29,-9,1]
    assert polys['cube']==polynomial_product(polys['theta'],H)
    rows=[]
    for q in (2,5,11):
        p=1009
        cup,cap,Pi,theta,dual,d0=cable(q,p)
        for name,graph in base_graphs:
            b=len(graph[1]);D=d0*d0%p;F=evaluate(polys[name],D)%p
            actual_spin=spin_graph(graph,theta,dual,p)
            assert actual_spin==pow(-pow(q,7,p)*d0,b,p)*F%p
            actual_cable=primitive_cable_graph(graph,cup,cap,Pi,p)
            assert actual_cable==pow(-d0,-b,p)*F%p
            assert actual_spin==pow(pow(q,7,p)*d0*d0,b,p)*actual_cable%p
            rows.append({'generic_parameter':q,'prime':p,'graph':name,
                         'all_input_cabling_and_literal_Morse_flow_identity':True})
    family=[]
    graph=theta_graph();queue=[0];Pflow=polys['theta']
    for k in range(6):
        if k:
            vertex=queue.pop(0)
            graph,children=insert_cube(graph,vertex)
            queue.extend(children)
            Pflow=polynomial_product(Pflow,H)
        assert three_edge_connected(graph)
        assert derivative(Pflow,1)==(-1)**(k+1)*11**k
        assert derivative(Pflow,2)==(-2)**k
        for q in (2,11):
            p=1009
            cup,cap,Pi,theta,dual,d0=cable(q,p)
            actual=spin_graph(graph,theta,dual,p)
            assert actual==pow(-pow(q,7,p)*d0,len(graph[1]),p)*evaluate(Pflow,d0*d0%p)%p
        family.append({'cube_insertions':k,'black_vertices':len(graph[1]),
                       'physical_heads':2*len(incidence(graph)),
                       'literal_NC_Morse_sewing_and_three_edge_connectivity':True,
                       'dual_beta':11**k,'flow_first_derivative_at_2':(-2)**k})
    roots=[]
    for N in (3,4):
        local=Local(N);graph=theta_graph();queue=[0];Pflow=polys['theta']
        for k in range(5):
            if k:
                graph,children=insert_cube(graph,queue.pop(0));queue.extend(children)
                Pflow=polynomial_product(Pflow,H)
            b=len(graph[1]);E=len(incidence(graph));p=local.p;q=local.q
            row=graph_case(local,f'cube_insertion_tree_k{k}',graph,(1,)*E,(0,)*E)
            if N==3:
                expected=pow(108,b,p)*11**k%p
            else:
                expected=pow(2,12*b+k,p)*pow(q+pow(q,-1,p),-1,p)%p
            assert row['original_marked_scalar']==expected
            d0=(q+pow(q,-1,p))%p;D=d0*d0%p
            Dprime=2*d0*(q-pow(q,-1,p))%p
            Xi=row['ordinary_spin_root_and_first_normal']
            assert Xi[0]==0 and Xi[1]==pow(-pow(q,7,p)*d0,b,p)*derivative(Pflow,D)*Dprime%p
            roots.append(row)
        # Exact two-edge-neck order is TWO at N4, despite connectivity.
        if N==4:
            graph=ordered_dipole_graph();E=len(incidence(graph))
            row=graph_case(local,'dipole_order_two',graph,(1,)*E,(0,)*E)
            assert row['original_marked_scalar']==0
            assert evaluate(polys['dipole'],2)==derivative(polys['dipole'],2)==0
            assert sum(k*(k-1)*c*2**(k-2) for k,c in enumerate(polys['dipole']) if k>=2)!=0
            roots.append(row)
    out={'status':'PASS','literal_generic_cabling_and_graph_state_expansions':rows,
         'arbitrarily_branching_NC_cube_insertions':family,
         'original_fixed_level_marked_source_and_normal_orders':roots,
         'scope':'Exact generic Q1 graph polynomial and fixed N3/N4 source-order model. No all-N surviving-label asymptotic, arbitrary-label simple-zero claim, or geometric volume theorem.'}
    Path(__file__).with_name('actual_nc_spin_one_flow_order_certificate_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS 9 generic literal Morse/cabling graphs; 6 branching NC/three-edge-connected insertions; 11 original N3/N4 first-normal sources')
