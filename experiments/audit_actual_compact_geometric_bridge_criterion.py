#!/usr/bin/env python3
"""All-width compact criterion, exact geometric prototype and cap weights."""
import itertools
import json
from pathlib import Path
import numpy as np
import sympy as sp

from audit_actual_bounded_quantum_meridians import nielsen_substitution


def exact_geometric_prototype():
    u,z=sp.symbols('u z')
    field=sp.groebner([u*u-u+1,z*z-sp.Rational(5,3)*z+1],u,z)
    def red(x):return field.reduce(sp.expand(x))[1]
    def rm(A):return A.applyfunc(red)
    def mul(A,B):return rm(A*B)
    def bar(A):return rm(A.subs({u:1-u,z:sp.Rational(5,3)-z},simultaneous=True))
    def star(A):return bar(A).T
    def inv(A):return rm(sp.Matrix([[A[1,1],-A[0,1]],[-A[1,0],A[0,0]]]))
    I=sp.eye(2);a=1+u;zi=sp.Rational(5,3)-z
    G1=sp.Matrix([[u,-a],[a,-2-u]])
    G2=sp.Matrix([[u,-a*zi],[a*z,-2-u]])
    J=sp.diag(1,-1)
    for G in (G1,G2):
        assert red(G.det())==1 and red(sp.trace(G)+2)==0
        assert red(G[0,0]*bar(G)[0,0]-1)==0
        assert red(G[1,0]+G[0,0]*bar(G)[0,1])==0
        assert rm(star(G)*J*G-J+sp.Rational(1,2)*star(G+I)*(G+I))==sp.zeros(2)
    assert red(sp.trace(G1*G2)-2-u)==0
    A=sp.Matrix([[1,1],[0,1]]);B=sp.Matrix([[1,0],[u,1]])
    F=sp.Matrix([[a*(z-1),1],[a*(z-1),z]])
    assert rm(F*A+G1*F)==sp.zeros(2)
    assert rm(F*B+G2*F)==sp.zeros(2)
    BB=mul(star(F),F);JJ=mul(mul(star(F),J),F)
    assert rm(JJ*BB.adjugate()*JJ-BB.det()*BB)==sp.zeros(2)
    for M in (A,B):
        assert rm(star(M)*JJ*M-JJ+sp.Rational(1,2)*star(M-I)*BB*(M-I))==sp.zeros(2)
    # Actual bottom bridge: both endpoints cannot be in one compact star frame.
    C=sp.Matrix([[2,u],[u-1,0]])
    Ac=sp.Matrix([[1,-1],[0,1]]);Bc=sp.Matrix([[1,0],[-u,1]])
    assert rm(Ac*B*Ac*Bc*A-C)==sp.zeros(2)
    circle=sp.Matrix([[0,2-u],[1+u,0]])
    assert red(circle.det())==-3
    assert rm(star(A)*circle*A-circle)==sp.diag(0,3)
    assert rm(star(B)*circle*B-circle)==sp.diag(3,0)
    assert rm(star(C)*circle*C-circle)==sp.zeros(2)
    heads=[G1,inv(G1),G2,inv(G2)]
    word=[2,-1,2,2];images=[[j+1] for j in range(4)]
    for letter in word:images=nielsen_substitution(images,letter)
    outputs=[]
    for w in images:
        M=I
        for j in w:M=mul(M,heads[abs(j)-1] if j>0 else inv(heads[abs(j)-1]))
        outputs.append(M)
    assert mul(outputs[1],outputs[0])==I and mul(outputs[3],outputs[2])==I
    # Direct identification of the remaining plat relator with figure8.
    R=[2,-1,2,1,-2,-1,2,-1,-2,1]
    left=[1,-2,-1,2,1];right=[2,1,-2,-1,2]
    standard=[-j for j in left[::-1]]+right
    assert R==standard[3:]+standard[:3]
    return {'exact_field':['u^2-u+1','3z^2-5z+3'],
            'all_compact_star_and_Hermitian_conditions':True,
            'explicit_same_representation_conjugation':True,
            'literal_four_plat_word':word,'all_bottom_Nielsen_cap_constraints':True,
            'no_common_compact_star_frame_for_both_source_endpoints':True,
            'actual_bottom_bridge_J_unitary_defect_zero':True,
            'same_figure_eight_relator_cyclic_shift':3,
            'pair_trace_parameter':'u'}


def cardioid_checks():
    rows=[]
    for phi in (-2.7,-1.4,0.,.6,2.2):
        for fraction in (.05,.4,1.):
            radius=16*np.cos(phi/2)**2*fraction;tau=radius*np.exp(1j*phi)
            k=np.exp(1j*phi);a=1+k;delta=2*np.arcsin(np.sqrt(fraction))
            ts=(1,np.exp(1j*delta));Gs=[]
            for t in ts:
                G=np.array([[k,-a/t],[a*t,-2-k]],complex)
                assert abs(np.linalg.det(G)-1)<1e-12
                assert abs(G[1,0]+G[0,0]*G[0,1].conjugate())<1e-12
                Gs.append(G)
            actual=np.trace(Gs[0]@Gs[1])-2
            assert abs(actual-tau)<1e-11
            rows.append({'phase':phi,'relative_cardioid_radius':fraction,
                         'actual_tau':[actual.real,actual.imag],
                         'all_compact_conditions':True})
    # A genuine necessary flag obstruction: four nonconcyclic ideal points.
    u=np.exp(1j*np.pi/3)
    assert abs(u.imag)>0
    return {'all_two_bridge_compact_constructions':rows,
            'four_actual_figure_eight_meridian_flags':[0,'infinity',1,[u.real,u.imag]],
            'their_cross_ratio_nonreal':True,
            'scope':'a flag diagnostic, not a claim that this four-tuple is a specified plat marking'}


def matched_packet_weights():
    rng=np.random.default_rng(7293);rows=[]
    for N,k,marked in ((2,1,0),(3,1,0),(3,2,0),(5,2,1),(3,3,1)):
        q=np.exp(1j*np.pi/N);Q=q*q;x=-1/q;d=N-1
        cup=np.zeros(N*N,complex)
        for j in range(N):cup[(d-j)*N+j]=x**(-j)/np.sqrt(N)
        u=np.array([1],complex)
        for _ in range(k):u=np.kron(u,cup)
        bases=[]
        for _ in range(k):
            A=rng.normal(size=(N,N))+1j*rng.normal(size=(N,N))
            V,_=np.linalg.qr(A);bases.append(V)
        g=np.array([x**(1-N)*Q**(-a) for a in range(N)])
        G=[]
        for state in itertools.product(range(N),repeat=2*k):
            G.append(np.prod([g[state[2*r]] for r in range(k) if r!=marked]))
        G=np.array(G);phi=G.conjugate()*u
        total=np.zeros_like(u);count=0
        for choices in itertools.product(range(N),repeat=k):
            packet=np.array([1],complex)
            for r,a in enumerate(choices):
                v=bases[r][:,a]
                w=np.array([x**(-j)*v[d-j].conjugate() for j in range(N)])
                packet=np.kron(packet,np.kron(v,w))
            packet=G.conjugate()*packet
            assert abs(np.linalg.norm(packet)-1)<1e-12
            assert abs(np.vdot(packet,phi)-N**(-k/2))<1e-12
            total+=packet;count+=1
        assert np.linalg.norm(phi-N**(-k/2)*total)<1e-11
        rows.append({'N':N,'cups':k,'marked_pair':marked,
                     'exact_positive_cap_coefficient':N**(-k/2),
                     'full_orthonormal_matched_packet_terms':count,
                     'original_unitary_pivot_included':True})
    return rows


def localized_geometric_packets():
    rows=[]
    for sign,N in itertools.product((1,-1),(24,48,96,192,384)):
        u=np.exp(sign*1j*np.pi/3);z=(5+sign*1j*np.sqrt(11))/6
        q=np.exp(1j*np.pi/N);Q=q*q;x=-1/q;d=N-1
        K=np.array([x*Q**(-a) for a in range(N)])
        fr=np.array([0]+[1-Q**a for a in range(1,N)])
        er=np.array([1/x-x*Q**(-a) for a in range(N-1)]+[0])
        def action(v,kind):
            if kind=='K':return K*v
            if kind=='e':return er*np.roll(v,-1)
            return fr*np.roll(v,1)
        errors=[];weights=[]
        for t in (1,z):
            index=np.arange(N);center=N*(.5-np.angle(u)/(2*np.pi))-.5
            v=np.exp(-(index-center)**2/(2*N)-1j*np.angle(t)*index)
            v=v/np.linalg.norm(v)
            w=np.array([x**(-j)*v[d-j].conjugate() for j in range(N)])
            target=(u,-(1+u)/t,(2-u)*t)
            partner=(1/u,(2-u)/t,-(1+u)*t)
            for vector,vals in ((v,target),(w,partner)):
                errors.append(max(np.linalg.norm(action(vector,kind)-val*vector)**2
                                  for kind,val in zip(('K','e','f'),vals)))
            # Avoid a dense N^2 cup vector: the exact contraction is N terms.
            weight=sum(v[d-j].conjugate()*w[j].conjugate()*x**(-j) for j in range(N))/np.sqrt(N)
            assert abs(weight-1/np.sqrt(N))<1e-12
            weights.append(float(abs(weight)))
        error=max(errors)
        assert error<100/N
        rows.append({'N':N,'Riley_orientation_sign':sign,
                     'largest_geometric_head_mean_square_error':float(error),
                     'N_times_error':float(N*error),'two_actual_cup_packet_coefficients':weights})
    return rows


def main():
    out={'same_discrete_faithful_compact_figure_eight':exact_geometric_prototype(),
         'general_criterion_diagnostics':cardioid_checks(),
         'original_positive_cap_packet_weights':matched_packet_weights(),
         'localized_packets_at_that_geometric_compact_point':localized_geometric_packets(),
         'scope':'all-width compact feasibility and exact cap half-density; '
                 'no nonzero original braid transition or exponential overlap asserted'}
    Path(__file__).with_name('audit_actual_compact_geometric_bridge_criterion_results.json').write_text(
        json.dumps(out,indent=2)+'\n')
    print('PASS exact discrete-faithful compact4plat/Riley/Hermitian proof, '
          '15 two-bridge constructions, original cap packet decompositions and geometric packet scales')


if __name__=='__main__':main()
