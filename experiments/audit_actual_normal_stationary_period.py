#!/usr/bin/env python3
"""Actual crossing transport and transverse geometric stationary data.

The principal symbol is checked against all exact local shifts. Global
Hessians are made from the actual balanced coefficient action, while
their null vectors are differentiated from independent representation
matrices. No finite-period or volume-conjecture selection is asserted.
"""

from itertools import combinations,product
import json
from pathlib import Path

import numpy as np
import sympy as sp
from sympy.polys.domains import QQ

from audit_cyclic_steinberg_lattice import determinant,rank
from audit_kashaev_ado_pointing import WORDS
from audit_regular_holonomy_braiding import mm


def symbolic_principal_transport():
    A,B,C,M,h=sp.symbols('A B C M h',nonzero=True)
    Q=sp.exp(h);x=-M*sp.exp(-h/2);Y=M*M
    records=[]
    for sign in (1,-1):
        if sign>0:
            shapes=[B,C,Y/A,B*C,Y*C/A]
            vectors=[(0,1,0,0),(0,0,1,0),(-1,0,0,2),(0,1,1,0),(-1,0,1,2)]
            G=sp.Matrix([[0,1,1,-1],[1,0,-1,-1],[1,-1,-1,-1],[-1,-1,-1,0]])
            amplitude=A*B*(1-B*C)*(1-Y/A)/((1-B)*(1-C)*(1-Y*C/A))
            ratios=[B*C/x*(1-Y/(Q*A))/(1-Y*C/(Q*A)),
                    A/(C*x)*(1-Q*B*C)/(1-Q*B),
                    -A/(Q*B*C*x)*(1-Q*B*C)*(1-Y*C/A)/(1-Q*C)]
        else:
            shapes=[A,C,Y/B,A*C,Y*C/B]
            vectors=[(1,0,0,0),(0,0,1,0),(0,-1,0,2),(1,0,1,0),(0,-1,1,2)]
            G=sp.Matrix([[0,-1,0,1],[-1,0,0,1],[0,0,0,-1],[1,1,-1,0]])
            amplitude=C/(A*B)*(1-A*C)*(1-Y/B)/((1-A)*(1-C)*(1-Y*C/B))
            ratios=[x/B*(1-Q*A*C)/(1-Q*A),
                    x/A*(1-Y/(Q*B))/(1-Y*C/(Q*B)),
                    1/x*(1-Q*A*C)*(1-Y*C/B)/(1-Q*C)]
        H=G.copy()
        for z,v,e in zip(shapes,vectors,(1,1,1,-1,-1)):
            v=sp.Matrix(v);H+=e*z/(1-z)*v*v.T
        for i,(ratio,var) in enumerate(zip(ratios,(A,B,C))):
            sub=sp.cancel(sp.diff(ratio,h).subs(h,0)/ratio.subs(h,0))
            want=sp.cancel(H[i,i]/2+var*sp.diff(amplitude,var)/(2*amplitude))
            assert sp.cancel(sub-want)==0
        # The M->exp(h/2)M ratio has no h-dependent correction.
        assert sp.cancel(H[3,3]/8+M*sp.diff(amplitude,M)/(4*amplitude))==0
        records.append({'crossing_sign':sign,'principal_amplitude_squared':str(sp.factor(amplitude)),
                        'all_three_internal_first_transport_identities_exact':True,
                        'actual_meridian_half_step_transport_exact':True})
    return records


def jet_field(p):
    class J:
        __slots__=('v','d')
        def __init__(self,v,d=(0,0,0)):
            self.v=int(v)%p;self.d=tuple(int(a)%p for a in d)
        def coerce(self,z):return z if isinstance(z,J) else J(z)
        def __add__(self,z):
            z=self.coerce(z);return J(self.v+z.v,[a+b for a,b in zip(self.d,z.d)])
        __radd__=__add__
        def __neg__(self):return J(-self.v,[-a for a in self.d])
        def __sub__(self,z):return self+-self.coerce(z)
        def __rsub__(self,z):return self.coerce(z)+-self
        def __mul__(self,z):
            z=self.coerce(z);return J(self.v*z.v,[a*z.v+b*self.v for a,b in zip(self.d,z.d)])
        __rmul__=__mul__
        def __pow__(self,n):
            if n==0:return J(1)
            if n<0 and not self.v:raise ZeroDivisionError('outside the regular jet chart')
            power=pow(self.v,n,p)
            return J(power,[n*pow(self.v,n-1,p)*a for a in self.d])
        def __truediv__(self,z):return self*self.coerce(z)**-1
        def __rtruediv__(self,z):return self.coerce(z)*self**-1
        def __eq__(self,z):
            z=self.coerce(z);return self.v==z.v and self.d==z.d
    return J


def matmul(a,b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) for i in range(2) for j in range(2))


def inverse(a):
    d=a[0]*a[3]-a[1]*a[2]
    return tuple(v/d for v in (a[3],-a[1],-a[2],a[0]))


def crossing(z,w,sign):
    k,e,f=z;l,g,h=w
    if sign>0:
        d=1-e*h
        return [(l*d,(d*g+e*(d*l-1/l))/k,k*h/d),
                (k/d,e/(l*d),l*(d*f+h*(d/k-k)))]
    c=1-k*g*f/l
    return [(l*c,k*g,f+h/k-f/(l*l*c)),
            (k/c,l*e+g-k*k*g/c,f/l)]


def closure_embedding(strands,word):
    full=strands+len(word);positions=sp.eye(full)[:strands,:]
    maps=[]
    for t,(j,sign) in enumerate(word):
        a,b,c=positions[j,:],positions[j+1,:],sp.eye(full)[strands+t,:]
        maps.append(sp.Matrix.vstack(a,b,c))
        positions[j,:],positions[j+1,:]=b+sign*c,a-sign*c
    closure=positions-sp.eye(full)[:strands,:]
    unknown=closure[1:,1:strands]
    assert abs(unknown.det())==1
    embedding=sp.zeros(full,len(word)+1)
    embedding[0,0]=1
    for t in range(len(word)):embedding[strands+t,t+1]=1
    rest=closure[1:,:]*embedding
    embedding[1:strands,:]=-unknown.inv()*rest
    assert not any(closure*embedding)
    assert all(v.q==1 for v in embedding)
    return [np.array(m*embedding,dtype=np.int64) for m in maps]


def framed_figure_states(p,riley,frame):
    J=jet_field(p)
    M=J(1,(0,0,1));r=J(frame[0],(1,0,0));s=J(frame[1],(0,1,0))
    t=J(riley)  # Its first log-M derivative is zero at M=1.
    A=(M,J(1),J(0),1/M);B=(M,J(0),t,1/M)
    C=matmul(matmul(matmul(matmul(inverse(A),B),A),inverse(B)),A)
    w1=1/M-M
    F=(r,1-r,s,w1-s)
    holonomies=[tuple(-v for v in matmul(matmul(inverse(F),mu),F)) for mu in (A,B,C)]
    previous=(J(1),J(0),J(0),J(1));states=[]
    for H in holonomies:
        G=matmul(matmul(previous,H),inverse(previous));k,e=G[0],G[1];f=G[2]/k
        states.append((k,e,f));previous=matmul((J(1),J(0),-k*f,k),previous)
    return J,M,states


def local_hessian(A,B,C,M,sign,J):
    if sign>0:
        G=[[0,1,1,-1],[1,0,-1,-1],[1,-1,-1,-1],[-1,-1,-1,0]]
        shapes=[B,C,M*M/A,B*C,M*M*C/A]
        vectors=[(0,1,0,0),(0,0,1,0),(-1,0,0,2),(0,1,1,0),(-1,0,1,2)]
        amp=A*B*(1-B*C)*(1-M*M/A)/((1-B)*(1-C)*(1-M*M*C/A))
    else:
        G=[[0,-1,0,1],[-1,0,0,1],[0,0,0,-1],[1,1,-1,0]]
        shapes=[A,C,M*M/B,A*C,M*M*C/B]
        vectors=[(1,0,0,0),(0,0,1,0),(0,-1,0,2),(1,0,1,0),(0,-1,1,2)]
        amp=C/(A*B)*(1-A*C)*(1-M*M/B)/((1-A)*(1-C)*(1-M*M*C/B))
    if any(z.v in (0,1) for z in shapes):raise ZeroDivisionError('degenerate shape')
    H=[[J(G[i][j]) for j in range(4)] for i in range(4)]
    for z,v,e in zip(shapes,vectors,(1,1,1,-1,-1)):
        for i in range(4):
            for j in range(4):H[i][j]+=e*z/(1-z)*v[i]*v[j]
    return H,amp


def geometric_hessian_case(p,riley,frame):
    J,M,states=framed_figure_states(p,riley,frame)
    initial=list(states);x=-M;word=WORDS[0];d=len(word)+1
    maps=closure_embedding(3,word)
    H=[[J(0) for _ in range(d+1)] for _ in range(d+1)]
    free=[x/states[0][0]];amplitude=J(1);longitude_inverse=J(1)
    for n,(j,sign) in enumerate(word):
        k,e,f=states[j];l,g,h=states[j+1]
        A,B=x/k,x/l
        C=1/(1-e*h) if sign>0 else 1-k*g*f/l
        free.append(C)
        local,amp=local_hessian(A,B,C,M,sign,J)
        amplitude*=amp
        tau=(B*C/x*(1-M*M/A)/(1-M*M*C/A) if sign>0
             else x/A*(1-M*M/B)/(1-M*M*C/B))
        longitude_inverse*=tau
        P=np.zeros((4,d+1),dtype=np.int64);P[:3,:d]=maps[n];P[3,-1]=1
        for a in range(d+1):
            for b in range(d+1):
                H[a][b]+=sum(int(P[i,a])*local[i][j]*int(P[j,b]) for i,j in product(range(4),repeat=2))
        states[j:j+2]=crossing(states[j],states[j+1],sign)
    assert states==initial
    writhe=sum(sign for _,sign in word)
    amplitude*=M**(2*(3-1-writhe))
    for state in initial[1:]:amplitude/=(x/state[0])**2
    assert amplitude.v
    tangents=np.array([[a*pow(z.v,-1,p)%p for a in z.d] for z in free],dtype=np.int64)
    H0=np.array([[z.v for z in row] for row in H],dtype=np.int64)
    normal=H0[:d,:d]
    assert rank(tangents[:,:2],p)==2
    assert rank(normal,p)==d-2
    assert not np.any(mm(p,normal,tangents[:,:2]))
    assert not np.any((mm(p,normal,tangents[:,2:3])[:,0]+H0[:d,d])%p)
    longitude=1/longitude_inverse
    cusp=longitude.d[2]*pow(longitude.v,-1,p)%p
    reduced_second=(int(H0[d,d])+int(mm(p,H0[d:d+1,:d],tangents[:,2:3])[0,0]))%p
    assert reduced_second==2*cusp%p
    pivots=next(pair for pair in combinations(range(d),2)
                if determinant(tangents[list(pair),:2],p))
    transverse=[j for j in range(d) if j not in pivots]
    Hn=normal[np.ix_(transverse,transverse)]
    det=determinant(Hn,p);assert det
    gauge=determinant(tangents[list(pivots),:2],p)
    omega_squared=pow(-1,d-2,p)*amplitude.v*gauge*gauge*pow(det,-1,p)%p
    return {'prime':p,'Riley_parameter':riley,'frame':list(frame),
            'independent_phase_variables':d,'Hessian_rank':d-2,'framing_kernel_dimension':2,
            'transverse_Hessian_determinant':det,'framing_slice_indices':list(pivots),
            'actual_squared_principal_amplitude':amplitude.v,
            'independent_representation_tangents_annihilated_by_Hessian':True,
            'meridian_tangent_and_longitude_second_derivative_exact':True,
            'cusp_derivative':cusp,'normal_two_form_coefficient_squared':omega_squared,
            'two_form_times_frame_s_squared':omega_squared*frame[1]**2%p,
            'two_form_times_frame_s_fourth':omega_squared*frame[1]**4%p}


def symbolic_framing_density(r_parameter=2, exact_field=None, holonomy_data=None):
    # A None parameter retains the entire two-variable framing torsor.
    # Fixed-r runs still keep both framing derivatives analytically.
    # Reconstruct the Gauss chart directly from constant group prefixes.
    ss,rr=sp.symbols('s r');base=QQ.algebraic_field(sp.sqrt(-3))
    field=exact_field if exact_field is not None else (base.frac_field(ss,rr) if r_parameter is None else base.frac_field(ss))
    s=field.gens[0];zero,one=field.zero,field.one
    r=field.gens[1] if r_parameter is None else field.convert(r_parameter)
    if holonomy_data is None:
        radical=field.convert(base.from_sympy(sp.sqrt(-3)),base);root=(one-radical)/2
        A=(one,one,zero,one);B=(one,zero,root,one)
        C=matmul(matmul(matmul(matmul(inverse(A),B),A),inverse(B)),A)
        mus=[A,B,C];word=WORDS[0]
    else:
        mus=list(holonomy_data['meridians']);word=holonomy_data['word']
    initial=list(mus);identity=(one,zero,zero,one)
    def gauss_roots(matrices):
        previous=(one,zero,zero);prefix=identity;states=[]
        for j,mu in enumerate(matrices):
            prefix=matmul(mu,prefix);a,b,c,d=prefix
            value=d+(a-d)*r+b*s+c*r*(one-r)/s
            dr=(a-d)+c*(one-2*r)/s;ds=b-c*r*(one-r)/(s*s)
            current=(((-1)**(j+1))*value,dr/value,ds/value)
            states.append((current[0]/previous[0],current[1]-previous[1],current[2]-previous[2]))
            previous=current
        return states
    states=gauss_roots(mus);old_states=list(states);maps=closure_embedding(len(mus),word);d=len(word)+1
    hessian=[[zero for _ in range(d)] for _ in range(d)]
    tangent=[[-states[0][1],-states[0][2]]];amp=one
    for n,(j,sign) in enumerate(word):
        a,b=-one/states[j][0],-one/states[j+1][0]
        left,right=mus[j:j+2]
        mus[j:j+2]=([matmul(matmul(inverse(left),right),left),left] if sign>0
                     else [right,matmul(matmul(right,left),inverse(right))])
        new=gauss_roots(mus)
        c=(new[j+1][0]/states[j][0] if sign>0 else states[j][0]/new[j+1][0])
        tangent.append([sign*(new[j+1][k]-states[j][k]) for k in (1,2)])
        if sign>0:
            constants=[[0,1,1],[1,0,-1],[1,-1,-1]]
            shapes=[b,c,one/a,b*c,c/a]
            vectors=[(0,1,0),(0,0,1),(-1,0,0),(0,1,1),(-1,0,1)]
            amp*=a*b*(one-b*c)*(one-one/a)/((one-b)*(one-c)*(one-c/a))
        else:
            constants=[[0,-1,0],[-1,0,0],[0,0,0]]
            shapes=[a,c,one/b,a*c,c/b]
            vectors=[(1,0,0),(0,0,1),(0,-1,0),(1,0,1),(0,-1,1)]
            amp*=c/(a*b)*(one-a*c)*(one-one/b)/((one-a)*(one-c)*(one-c/b))
        local=[[field.convert(constants[i][k]) for k in range(3)] for i in range(3)]
        for z,v,epsilon in zip(shapes,vectors,(1,1,1,-1,-1)):
            coefficient=epsilon*z/(one-z)
            for i,k in product(range(3),repeat=2):
                if v[i]*v[k]:local[i][k]+=coefficient*v[i]*v[k]
        P=maps[n]
        for a0,b0 in product(range(3),repeat=2):
            if not local[a0][b0]:continue
            for i in np.flatnonzero(P[a0]):
                for k in np.flatnonzero(P[b0]):
                    hessian[i][k]+=int(P[a0,i])*int(P[b0,k])*local[a0][b0]
        states=new
    # FracElement equality over an algebraic coefficient field can depend
    # on its constant denominator frame. Test the field differences.
    assert all(not(a-b) for left,right in zip(mus,initial) for a,b in zip(left,right))
    for state in old_states[1:]:amp/=(-one/state[0])**2
    assert all(not sum(hessian[i][k]*tangent[k][a] for k in range(d))
               for i in range(d) for a in range(2))
    cut=next(pair for pair in combinations(range(d),2) if
             tangent[pair[0]][0]*tangent[pair[1]][1]-tangent[pair[0]][1]*tangent[pair[1]][0])
    transverse=[j for j in range(d) if j not in cut];H=[[hessian[i][j] for j in transverse] for i in transverse]
    det=exact_field_determinant(H,one,zero)
    gauge=tangent[cut[0]][0]*tangent[cut[1]][1]-tangent[cut[0]][1]*tangent[cut[1]][0]
    density=(-one)**(d-2)*amp*gauge*gauge/det
    if holonomy_data is not None:
        expected=holonomy_data['expected_density']
        assert not density-expected
        return {'field':holonomy_data['field_label'],'phase_variables':d,
                'both_framing_tangents_annihilated_exactly':True,
                'squared_two_form_coefficient_on_full_torsor':str(sp.factor(field.to_sympy(expected))),
                'identity_checked_in_exact_function_field':True,'global_r_independence_proved':True,
                'fixed_normalizer_and_root_cut_cycle_not_evaluated':True}
    cusp=2-4*root
    expected=-cusp/(6*s*s*(s+one)**2)
    assert not density-expected
    return {'field':'Q(sqrt(-3))(s,r)' if r_parameter is None else 'Q(sqrt(-3))(s)','r_parameter':r_parameter,
            'both_framing_derivatives_retained_before_evaluation':True,
            'both_framing_tangents_annihilated_exactly':True,
            'framing_slice_indices':list(cut),
            'cusp_derivative':str(sp.simplify(field.to_sympy(cusp))),
            'squared_two_form_coefficient_at_fixed_r' if r_parameter is not None else 'squared_two_form_coefficient_on_full_torsor':str(sp.factor(sp.simplify(field.to_sympy(expected)))),
            'identity_checked_in_exact_function_field':True,
            'global_r_independence_proved':r_parameter is None,
            'fixed_normalizer_and_root_cut_cycle_not_evaluated':True}


def exact_field_determinant(matrix,one,zero):
    work=[list(row) for row in matrix];n=len(work);value=one
    for j in range(n):
        pivot=next((k for k in range(j,n) if work[k][j]),None)
        if pivot is None:return zero
        if pivot!=j:
            work[pivot],work[j]=work[j],work[pivot];value=-value
        diagonal=work[j][j];value*=diagonal
        for k in range(j+1,n):
            if not work[k][j]:continue
            ratio=work[k][j]/diagonal
            for l in range(j+1,n):work[k][l]-=ratio*work[j][l]
            work[k][j]=zero
    return value


def main():
    records=[]
    candidates=[(a,b) for a,b in ((2,3),(3,2),(4,5),(5,3),(2,7),(7,2),(3,5),(6,7),(8,3),(9,4))]
    for p in (97,193,601):
        roots=[u for u in range(p) if (u*u-u+1)%p==0]
        assert len(roots)==2
        for riley in roots:
            accepted=[]
            for frame in candidates:
                try:record=geometric_hessian_case(p,riley,frame)
                except ZeroDivisionError:continue
                accepted.append(record)
                if len(accepted)==4:break
            assert len(accepted)==4
            records.extend(accepted)
    result={'scope':'Actual local first transport and normal stationary diagnostics; no finite-period selection or volume theorem.',
            'local_exact_transport':symbolic_principal_transport(),'geometric_normal_data':records,
            'symbolic_framing_density':symbolic_framing_density()}
    path=Path(__file__).with_name('actual_normal_stationary_period_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    groups=[]
    for p in (97,193,601):
        for root in sorted({r['Riley_parameter'] for r in records if r['prime']==p}):
            group=[r for r in records if r['prime']==p and r['Riley_parameter']==root]
            groups.append({'prime':p,'Riley_parameter':root,
                's_squared_values':[r['two_form_times_frame_s_squared'] for r in group],
                's_fourth_values':[r['two_form_times_frame_s_fourth'] for r in group]})
    print(json.dumps({'result':str(path),'normal_cases':len(records),'framing_density_diagnostics':groups}),flush=True)


if __name__=='__main__':main()
