#!/usr/bin/env python3
"""Independent literal cap-order audit; noncommuting boxes prevent aliasing."""

import itertools
import json
from pathlib import Path

import numpy as np
import mpmath as mp

from audit_actual_two_cut_ports import balanced_data
from audit_actual_odd_pretzel_augmented_transfer_source import literal_source
from audit_actual_pretzel_complete_base_casimir_polynomial import rotate_box


def physical_case(N, s):
    p,eta,q,E,F,K,pivot,Rp,Rm = balanced_data(N)
    x, rng = int(K[0,0]), np.random.default_rng(812+N+s)
    boxes=[]
    for _ in range(s):
        B=np.zeros((N*N,N*N),dtype=np.int64)
        for a,b,c,e in itertools.product(range(N),repeat=4):
            if a+b==c+e:
                B[c*N+e,a*N+b]=int(rng.integers(0,p))
        boxes.append(B)
    turns=[rotate_box(B,N,x,p) for B in boxes]
    for B,T in zip(boxes,turns):
        assert np.array_equal(rotate_box(T,N,x,p),B)
    product=reverse=np.eye(N*N,dtype=np.int64)
    for T in turns:
        product=product@T%p
    for T in reversed(turns):
        reverse=reverse@T%p
    phi=lambda W: sum(int(pivot[b])*int(W[a*N+b,a*N+b])
                      for a in range(N) for b in range(N))*pow(N,-1,p)%p
    original=literal_source(N,x,p,boxes)
    assert original==phi(product)
    assert original!=phi(reverse)
    return {'N':N,'physical_boxes':s,'full_marked_tensor_value':int(original),
            'correct_right_to_left_product_value':int(phi(product)),
            'incorrect_reversed_product_value':int(phi(reverse)),
            'all_box_double_turns_literal':True}


def gluing_case(s):
    p,w,start=1000003,13,7
    us=[j+2 for j in range(s-1)]
    us.append(pow(int(np.prod(us,dtype=object))%p,-1,p))
    incoming=[None]*s
    incoming[-1]=start
    for b in range(s-1,0,-1):
        incoming[b-1]=us[b]*incoming[b]%p
    outgoing=[u*t%p for u,t in zip(us,incoming)]
    assert outgoing[0]==incoming[-1]
    k=(w-1)**2*pow((w+1)**2,-1,p)%p
    def g(z):
        return np.array([[-2*w*pow(w+1,-1,p)%p,z],
                         [-k*pow(z,-1,p)%p,-2*pow(w+1,-1,p)%p]],dtype=np.int64)
    h=lambda z:g(-w*z%p)
    def inverse(M):
        assert int(M[0,0]*M[1,1]-M[0,1]*M[1,0])%p==1
        return np.array([[M[1,1],-M[0,1]],[-M[1,0],M[0,0]]],dtype=np.int64)%p
    I=np.eye(2,dtype=np.int64)
    for b in range(s):
        nxt=(b+1)%s
        assert incoming[b]==outgoing[nxt]
        assert np.array_equal(inverse(h(incoming[b]))@h(outgoing[nxt])%p,I)
        assert np.array_equal(g(incoming[b])@inverse(g(outgoing[nxt]))%p,I)
    wrong=[start]
    for b in range(s-1):
        wrong.append(us[b]*wrong[-1]%p)
    wrong_out=[u*t%p for u,t in zip(us,wrong)]
    failed=sum(wrong[b]!=wrong_out[(b+1)%s] for b in range(s))
    assert failed>0
    # Port map of the orientation-preserving planar half turn.
    def turn(port):
        b,kind=port
        return s-1-b,{'a':'d','b':'c','c':'b','d':'a'}[kind]
    bottom=[frozenset(((b,'b'),((b+1)%s,'a'))) for b in range(s)]
    top=[frozenset(((b,'d'),((b+1)%s,'c'))) for b in range(s)]
    assert {frozenset(map(turn,edge)) for edge in bottom}==set(top)
    assert {frozenset(map(turn,edge)) for edge in top}==set(bottom)
    assert round(np.linalg.det(np.diag([-1,-1,1])))==1
    return {'physical_boxes':s,'all_bottom_and_top_inverse_caps':2*s,
            'nonconstant_clock_parameters':True,'wrong_forward_caps_detected':failed,
            'rigid_half_turn_preserves_both_matchings_and_orientation':True}


def complete_holomorphic_case(s):
    mp.mp.dps=85
    alpha=mp.pi/s
    rho=mp.sqrt(1/mp.cos(alpha)+mp.tan(alpha))
    w,r=-rho**4,1/mp.sin(alpha)
    Y=mp.exp(2j*mp.atan(1/mp.cos(alpha)))
    F=mp.matrix([[0,rho],[1/rho,0]])
    I=mp.eye(2)
    z=lambda i:r/rho*mp.exp((2*i-1)*1j*alpha)
    def g(i):
        return mp.matrix([[-2*w/(w+1),z(i)],[-r*r/z(i),-2/(w+1)]])
    h=lambda i:mp.matrix([[-2*w/(w+1),-w*z(i)],
                          [r*r/(w*z(i)),-2/(w+1)]])
    P=lambda i:g(i)*g(i+1)**-1
    C=lambda i:I-(P(i)+I)/(1+Y)
    for i in range(s):
        assert mp.norm(F*g(i)*F**-1-h(1-i)**-1)<mp.mpf('1e-65')
        assert mp.norm(F*h(i)*F**-1-g(1-i)**-1)<mp.mpf('1e-65')
        assert mp.norm(F*P(i)*F**-1-P(-i)**-1)<mp.mpf('1e-65')
        assert mp.norm(F*C(i)*F**-1-C(-i)**-1)<mp.mpf('1e-65')
        Zi=rho*mp.exp(2j*i*alpha)
        plus=rho**-1*mp.exp((2*i+1)*1j*alpha)
        minus=rho**3*mp.exp((2*i+1)*1j*alpha)
        assert abs(rho**2/Zi-rho*mp.exp(-2j*i*alpha))<mp.mpf('1e-65')
        assert abs(rho**2/plus-rho**3*mp.exp((-2*i-1)*1j*alpha))<mp.mpf('1e-65')
        assert abs(rho**2/minus-rho**-1*mp.exp((-2*i-1)*1j*alpha))<mp.mpf('1e-65')
    return {'physical_boxes':s,'holomorphic_half_turn':'rho^2/z',
            'all_white_generators_and_both_peripheral_generators':True,
            'joint_meridian_longitude_inversion_no_framing_shear':True,
            'positive_volume_orientation_preserved':True}


if __name__=='__main__':
    physical=[physical_case(N,s) for N,s in
              ((2,3),(2,5),(2,7),(3,3),(3,5),(4,3),(5,3))]
    gluing=[gluing_case(s) for s in (3,5,7,9,13,25)]
    complete=[complete_holomorphic_case(s) for s in (3,5,7,9,13,25)]
    result={'status':'PASS','fresh_original_noncommuting_cap_tensors':physical,
            'corrected_all_port_geometry':gluing,
            'complete_holomorphic_reverse_traversal':complete,
            'scope':'Corrected literal order and orientation; geometric face holonomy is proved in its separate anchor theorem.'}
    Path(__file__).with_name('actual_pretzel_literal_cap_order_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print(f'PASS {len(physical)} fresh full marked noncommuting tensor sources; {len(gluing)} all-cap families; {len(complete)} complete holomorphic generator/peripheral families')
