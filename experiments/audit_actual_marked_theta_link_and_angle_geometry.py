#!/usr/bin/env python3
"""Actual theta/pretzel source, literal faces and an exact linear angle slice.

Combinatorial and finite-field checks supplement the written cut proof.
The geometry is the existing directly constructed ideal antiprism geometry.
"""
import itertools
import json
from fractions import Fraction
from pathlib import Path

import numpy as np

from audit_actual_augmented_pretzel_geometric_volume import UF, gluing_case
from audit_actual_trivalent_complete_circle_vertex_kernel import data, sources, axis_apply, matrix_power


def four_oct_angles():
    Z = [('z',k) for k in range(3)]
    U = [('u',k) for k in range(3)]
    faces = {'Z':Z, 'U':U}
    for k in range(3):
        faces[f'Q{k}'] = [Z[k],U[k],Z[(k+1)%3]]
        faces[f'T{k}'] = [Z[k],U[(k-1)%3],U[k]]
    edges = set()
    for cycle in faces.values():
        edges.update(tuple(sorted((a,b))) for a,b in zip(cycle,cycle[1:]+cycle[:1]))
    assert len(edges)==12
    cells = list(itertools.product(range(2),repeat=2))
    classes = UF([(cell,edge) for cell in cells for edge in edges])
    vertices = UF([(cell,v) for cell in cells for v in Z+U])
    for p,s in cells:
        for face,cycle in faces.items():
            target = (p,s^1) if face=='Z' or face.startswith('T') else (p^1,s)
            for v in cycle:vertices.union(((p,s),v),(target,v))
            for a,b in zip(cycle,cycle[1:]+cycle[:1]):
                edge = tuple(sorted((a,b)))
                classes.union(((p,s),edge),(target,edge))
    assert len(classes.groups())==12 and all(len(g)==4 for g in classes.groups())
    assert len(vertices.groups())==6
    assert all({cell for cell,_ in g}==set(cells) for g in classes.groups())
    axis0,axis1 = Z[0],U[1]
    equator = [Z[1],Z[2],U[2],U[0]]
    # Coefficients represent angle/pi in (constant,x0,x1,x2,x3).
    zero = lambda:[Fraction(0)]*5
    add = lambda a,b:[x+y for x,y in zip(a,b)]
    alpha = lambda k:[Fraction(0)]+[Fraction(i==k) for i in range(4)]
    beta = lambda k:[Fraction(1,2)]+[Fraction(-int(i==k)) for i in range(4)]
    right = [Fraction(1,2)]+[Fraction(0)]*4
    boundary = {}
    multiplicities = [0]*4
    for cell in cells:
        p,s = cell
        angles = {edge:zero() for edge in edges}
        internal = zero()
        for i in range(4):
            k = (i+2*p+s)%4
            multiplicities[k] += 1
            vi,vj = equator[i],equator[(i+1)%4]
            internal = add(internal,right)
            for edge,value in ((tuple(sorted((vi,vj))),right),
                               (tuple(sorted((axis0,vi))),alpha(k)),
                               (tuple(sorted((axis1,vj))),alpha(k)),
                               (tuple(sorted((axis0,vj))),beta(k)),
                               (tuple(sorted((axis1,vi))),beta(k))):
                angles[edge] = add(angles[edge],value)
            assert add(add(right,alpha(k)),beta(k))==[1,0,0,0,0]
        assert internal==[2,0,0,0,0]
        for edge,value in angles.items():boundary[(cell,edge)] = value
    for group in classes.groups():
        value = zero()
        for occurrence in group:value = add(value,boundary[occurrence])
        assert value==[2,0,0,0,0]
    assert multiplicities==[4]*4
    return {'ideal_octahedra':4,'positive_ideal_tetrahedra':16,
            'boundary_edge_cycles':12,'internal_axis_edges':4,'cusps':6,
            'exact_affine_angle_equations_for_entire_open_four_cube':True,
            'each_source_right_tetrahedron_angle_occurs':multiplicities}


def original_source(N):
    p,q,x,R,Ri,L,*_ = data(N)
    d = N-1
    source,ell,mark = sources(N,x,p)
    rows = []
    for exponents in ((0,0,0),(1,-2,3),(5,7,9)):
        boxes = [matrix_power(R,e,Ri,p)@L % p for e in exponents]
        value = source.copy()
        for axis,box in enumerate(boxes):value = axis_apply(box,value,axis,p)
        actual = int(np.sum(mark*value) % p)
        assert int(np.sum(ell*value) % p)==0
        transfer = 0
        for h in range(-d,d+1):
            ids = list(range(max(0,h),min(d,d+h)+1))
            Ms = []
            for B in boxes:
                Ms.append(np.array([[pow(x,-2*a+h,p)*int(B[(a-h)*N+d-ap+h,a*N+d-ap]) % p
                                     for ap in ids] for a in ids],dtype=np.int64))
            diagonal = np.diag([pow(x,2*a,p) for a in ids])
            transfer += int(np.trace(diagonal@Ms[0] % p@Ms[1] % p@Ms[2] % p))
        transfer = transfer*pow(x,2*d,p)*pow(N,-1,p) % p
        assert actual==transfer
        geometry = gluing_case(3,tuple(e%2 for e in exponents))
        rows.append({'signed_original_exponents':list(exponents),'raw_marked_scalar':actual,
                     'exact_s3_pretzel_transfer_identity':True,
                     'literal_components':geometry['circle_cusps']+geometry['main_cusps']})
    return {'N':N,'actual_original_sources':rows}


if __name__=='__main__':
    out = {'status':'PASS','source_angle_slice':four_oct_angles(),
           'all_eight_literal_half_twist_choices':[gluing_case(3,h) for h in itertools.product((0,1),repeat=3)],
           'original_source_and_transfer':[original_source(N) for N in range(2,8)],
           'scope':'Actual three-belt theta source and its four-octahedron complement; positive angle slice for the untwisted sixteen-tetrahedron triangulation only. No arbitrary-graph source factorization.'}
    Path(__file__).with_name('actual_marked_theta_link_and_angle_geometry_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS exact 16-tetrahedron angle slice,8 literal half-twist geometries,18 original signed marked sources')
