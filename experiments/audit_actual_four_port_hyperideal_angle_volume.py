#!/usr/bin/env python3
"""Own algebraic saddle/length identities and actual local angle geometry.

Six-variable polynomial certificates establish the stationary-discriminant
and edge-length algebra. Finite metric/action samples supplement the
Lorentz and first-variation proofs, not an imported 6j asymptotic theorem.
"""
import itertools
import json
from pathlib import Path

import mpmath as mp
import sympy as sp


FACES=((0,1,4),(2,3,4),(0,3,5),(1,2,5))
QUADS=((0,1,2,3),(0,2,4,5),(1,3,4,5))
ENDS=((0,2),(0,3),(1,3),(1,2),(0,1),(2,3))


def symbolic():
    a,b,c,d,e,f=sp.symbols('a b c d e f');u=(a,b,c,d,e,f)
    U=[a*b*e,c*d*e,a*d*f,b*c*f]
    V=[a*b*c*d,a*c*e*f,b*d*e*f]
    a2=sum(U)-1-sum(V)
    a1=sum(V[i]*V[j] for i in range(3) for j in range(i+1,3))+sum(V)-sum(U[i]*U[j] for i in range(4) for j in range(i+1,4))
    a0=sum(sp.prod(U[j] for j in range(4) if j!=i) for i in range(4))-sp.prod(V)-sum(V[i]*V[j] for i in range(3) for j in range(i+1,3))
    cos=lambda z:(z+1/z)/2
    ca,cb,cc,cd,ce,cf=map(cos,u)
    # Direct determinant of the four-face Gram, first as a polynomial
    # in six independent Gram entries, to avoid rational matrix inverses.
    x=sp.symbols('g0:6');xa,xb,xc,xd,xe,xf=x
    G=sp.Matrix([[1,xf,xc,xd],[xf,1,xb,xa],[xc,xb,1,xe],[xd,xa,xe,1]])
    det=G.det().subs(dict(zip(x,(ca,cb,cc,cd,ce,cf))))
    P=sp.prod(u)
    assert sp.Poly(sp.expand(a1*a1-4*a2*a0-16*P*P*det),*u).is_zero
    A=-a1-a2*(U[0]+U[2]);B=a2*U[0]*U[2]-a0
    C=-a1-a2*(V[0]+V[1]);D=a2*V[0]*V[1]-a0
    den=C*C*a0-C*D*a1+D*D*a2
    numsum=c*(2*A*C*a0-(A*D+B*C)*a1+2*B*D*a2)
    numprod=c*c*(A*A*a0-A*B*a1+B*B*a2)
    rnum=(a*e-b)*(a*b-e)*(a*f-d)*(a*d-f)
    rden=(b*e-a)*(a*b*e-1)*(d*f-a)*(a*d*f-1)
    cofactor=-cc*(1-ca*ca)+cf*cb+cd*ce-ca*(cf*ce+cd*cb)
    assert sp.Poly(sp.expand(numprod*rnum-den*rden),*u).is_zero
    target=sp.cancel(8*a*a*b*d*e*f*cofactor)
    assert sp.Poly(sp.expand(numsum*rnum-den*target),*u).is_zero
    # Exact three-face Gram sine product after all square roots cancel.
    c11=1-ca*ca-cb*cb-ce*ce+2*ca*cb*ce
    factor=(a*b*e-1)*(b*e-a)*(a*e-b)*(a*b-e)/(4*a*a*b*b*e*e)
    assert sp.cancel(c11-factor)==0
    return {'independent_edge_variables':6,'stationary_discriminant':True,
            'critical_edge_exponential_product':True,'critical_edge_exponential_sum':True,
            'three_face_Gram_sine_product':True}


def solve(colors):
    colors=list(map(mp.mpf,colors))
    F=[sum(colors[j] for j in row) for row in FACES]
    Q=[sum(colors[j] for j in row) for row in QUADS]
    lo,hi=max(F),min(Q)
    assert min(colors)>0 and max(colors)<mp.mpf('.5') and min(F)>1 and lo<hi
    grad=lambda z:mp.log(mp.sin(mp.pi*(z-1)))-mp.fsum(mp.log(mp.sin(mp.pi*(z-x))) for x in F)+mp.fsum(mp.log(mp.sin(mp.pi*(x-z))) for x in Q)
    # Uniqueness is proved in the note from the exact quadratic and
    # endpoint signs; this bracket then follows that selected root.
    for _ in range(270):
        mid=(lo+hi)/2
        if grad(mid)>0:lo=mid
        else:hi=mid
    z=(lo+hi)/2
    L=lambda t:-mp.im(mp.polylog(2,mp.exp(2j*mp.pi*t)))/(2*mp.pi)
    action=L(z-1)-sum(L(z-x) for x in F)-sum(L(x-z) for x in Q)
    action+=mp.fsum(mp.fsum(L(F[i]-2*colors[j]) for j in row)-L(F[i]-1) for i,row in enumerate(FACES))/2
    G=mp.eye(4)
    for k,ends in enumerate(ENDS):
        i,j=[t for t in range(4) if t not in ends]
        G[i,j]=G[j,i]=mp.cos(2*mp.pi*colors[k])
    inv=G**-1
    assert mp.det(G)<0 and all(inv[i,i]>0 for i in range(4))
    error=mp.mpf(0)
    for k,(v,w) in enumerate(ENDS):
        assert inv[v,w]<0
        length=mp.acosh(-inv[v,w]/mp.sqrt(inv[v,v]*inv[w,w]))
        derivative=mp.fsum(mp.log(mp.sin(mp.pi*(z-F[i]))) for i,row in enumerate(FACES) if k in row)
        derivative-=mp.fsum(mp.log(mp.sin(mp.pi*(Q[i]-z))) for i,row in enumerate(QUADS) if k in row)
        for i,row in enumerate(FACES):
            if k not in row:continue
            derivative+=mp.fsum((mp.mpf('-.5') if j==k else mp.mpf('.5'))*mp.log(mp.sin(mp.pi*(F[i]-2*colors[j]))) for j in row)
            derivative-=mp.log(mp.sin(mp.pi*(F[i]-1)))/2
        error=max(error,abs(derivative-length))
    assert error<mp.mpf('1e-65')
    return action,error,z


def geometry_profiles():
    with mp.workdps(90):
        cases=[['.4']*6,['.36','.38','.43','.4','.42','.39'],
            ['.1','.48','.15','.48','.48','.48'],
            ['.48','.49','.4','.45','.43','.46']]
        # Actual half-step colors, including interior chambers close
        # to face saturation and strongly unequal edge labels.
        for N in (16,17,32,33):
            m=(N-1)//2
            for labels in [(m-1,)*6,(m-2,m-1,m-1,m-2,m-1,m-1)]:
                colors=[(mp.mpf(j)+mp.mpf('.5'))/N for j in labels]
                if min(sum(colors[k] for k in face) for face in FACES)>1:
                    cases.append(colors)
        rows=[]
        for colors in cases:
            action,error,z=solve(colors)
            rows.append({'colors':list(map(str,colors)),'selected_stationary_Z':mp.nstr(z,30),
                'max_all_six_edge_length_error':mp.nstr(error,10),'pi_action':mp.nstr(mp.pi*action,40)})
        # Independent regular geometric integration of the directly
        # derived Schlaefli length, not numerical differentiation of Psi.
        v3=3*mp.im(mp.polylog(2,mp.exp(2j*mp.pi/3)))/2
        regular=[]
        for x in (mp.mpf('0.35'),mp.mpf('0.4'),mp.mpf('0.47')):
            action,_,_=solve([x]*6);alpha=mp.pi*(1-2*x)
            length=lambda t:mp.acosh(mp.cos(t)/(2*mp.cos(t)-1))
            # quad never uses the singular endpoint itself.
            volume=v3+3*mp.quad(length,[alpha,(alpha+mp.pi/3)/2,mp.pi/3])
            assert abs(volume-mp.pi*action)<mp.mpf('1e-75')
            regular.append({'equal_color':str(x),'independent_regular_volume':mp.nstr(mp.re(volume),40)})
        return rows,regular


def physical_halfsteps():
    rows=[]
    for N in range(3,11):
        M=(N-1)//2;count=0;zeroedges=0
        for js in itertools.product(range(M+1),repeat=6):
            sums=[sum(js[j] for j in face) for face in FACES]
            if min(sums)<N-1:continue
            quads=[sum(js[j] for j in quad) for quad in QUADS]
            lower,upper=max(sums),min(quads)
            assert lower<=upper and upper-lower+1<=N
            # Use numerator units 1/(4N): the geometric interval
            # endpoints are 4lower+6,4upper+8; grid endpoints are
            # 4lower+7,4upper+7, giving exact quarter-step insets.
            assert (4*lower+7)-(4*lower+6)==1
            assert (4*upper+8)-(4*upper+7)==1
            for z in range(lower,upper+1):
                assert 0<=z-(N-1)<N
                assert 0<4*(z-(N-1))+3<4*N
                assert all(0<=z-s<N and 0<4*(z-s)+1<4*N for s in sums)
                assert all(0<=s-z<N and 0<4*(s-z)+1<4*N for s in quads)
            assert all(0<=N-2*j-1<N for j in js)
            # pi minus vertex-angle sum is exactly
            # (pi/N)(2*faceSum-2N+3)>=pi/N.
            assert min(2*s-2*N+3 for s in sums)>=1
            count+=1;zeroedges+=sum(2*j+1==N for j in js)
        rows.append({'N':N,'all_supported_folded_six_tuples':count,'retained_zero_angle_edges':zeroedges,
            'exact_quarter_step_endpoint_insets':True,'all_shifted_action_arguments_physical':True,
            'positive_true_term_count_le_N':True})
    return rows


if __name__=='__main__':
    algebra=symbolic()
    profiles,regular=geometry_profiles()
    shifted=physical_halfsteps()
    out={'status':'PASS','universal_rational_certificates':algebra,
        'local_geometry_profiles':profiles,'independent_regular_volume_integrals':regular,
        'exact_source_halfstep_ranges':shifted,
        'scope':'Face-normalized positive factorial action and local hyperideal geometry. No actual arbitrary recoupling-energy normalization, partner-normal pruning or global knot-volume theorem is inferred.'}
    Path(__file__).with_name('actual_four_port_hyperideal_angle_volume_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS4 universal six-variable certificates;all-six length/Gram profiles;3 direct regular volume integrals;8 exact physical angle-range levels')
