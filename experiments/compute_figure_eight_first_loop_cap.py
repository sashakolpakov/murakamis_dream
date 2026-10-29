#!/usr/bin/env python3
"""Actual transverse Wick1 in physical external coordinates (a0,a2).

The rational framing residue is on the candidate eta_geo incidence
boundary, independently of the actual band-Fourier eta_F cap. Its
calculation does not provide that source pushforward or an all-order finite-cap
comparison. All flow derivatives precede evaluation at s=1.
"""

import argparse
import json
import time
from itertools import product
from pathlib import Path

import sympy as sp
from sympy.polys.domains import GF, QQ

from audit_actual_normal_stationary_period import matmul, inverse, crossing, closure_embedding
from audit_kashaev_ado_pointing import WORDS


class QuadraticFractionField:
    """Q(r)[t]/(t^2-t+1), with fast rational ground gcds."""
    def __init__(self,r):
        self.base=QQ.frac_field(r)
        self.domain=QQ.algebraic_field(sp.sqrt(-3))
        self.target=self.domain.frac_field(r)
        self.t_symbol=(1-sp.sqrt(-3))/2
        field=self
        class Element:
            __slots__=('a','b')
            def __init__(self,a=0,b=0):
                if isinstance(a,Element):self.a,self.b=a.a,a.b;return
                self.a,self.b=field.base.convert(a),field.base.convert(b)
            def __add__(self,x):
                x=Element(x);return Element(self.a+x.a,self.b+x.b)
            __radd__=__add__
            def __neg__(self):return Element(-self.a,-self.b)
            def __sub__(self,x):return self+-Element(x)
            def __rsub__(self,x):return Element(x)+-self
            def __mul__(self,x):
                x=Element(x)
                return Element(self.a*x.a-self.b*x.b,self.a*x.b+self.b*x.a+self.b*x.b)
            __rmul__=__mul__
            def inv(self):
                norm=self.a*self.a+self.a*self.b+self.b*self.b
                return Element((self.a+self.b)/norm,-self.b/norm)
            def __truediv__(self,x):return self*Element(x).inv()
            def __rtruediv__(self,x):return Element(x)*self.inv()
            def __pow__(self,n):
                if n<0:return self.inv()**(-n)
                value=Element(1);base=self
                while n:
                    if n%2:value=value*base
                    base=base*base;n//=2
                return value
            def __bool__(self):return bool(self.a) or bool(self.b)
            def diff(self,_):return Element(self.a.diff(field.base.gens[0]),self.b.diff(field.base.gens[0]))
        self.Element=Element;self.one=Element(1);self.zero=Element(0)
        self.gens=(Element(self.base.gens[0]),)
    def convert(self,value,*_):return self.Element(value)
    def to_sympy(self,value):
        value=self.Element(value)
        return self.base.to_sympy(value.a)+self.base.to_sympy(value.b)*self.t_symbol


def dot(v, w, zero):
    return sum((a*b for a, b in zip(v, w)), zero)


def inverse3(H, one, zero):
    a,b,c=H[0];d,e,f=H[1];g,h,i=H[2]
    determinant=a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
    assert determinant
    return [[(e*i-f*h)/determinant,(c*h-b*i)/determinant,(b*f-c*e)/determinant],
            [(f*g-d*i)/determinant,(a*i-c*g)/determinant,(c*d-a*f)/determinant],
            [(d*h-e*g)/determinant,(b*g-a*h)/determinant,(a*e-b*d)/determinant]],determinant


def hermite_certificate(field,total):
    r=field.gens[0];t=field.Element(0,1);zero=field.zero
    V=2+t-t*r*r;U=4-t-(t+1)*(r+r*r)
    J=U.diff(r)*V-U*V.diff(r)
    numerator=total*J**4
    def poly_coefficients(value):
        assert value.a.denom.degree()==0 and value.b.denom.degree()==0
        degree=max(value.a.numer.degree(),value.b.numer.degree())
        da=value.a.denom.get((0,),QQ.one);db=value.b.denom.get((0,),QQ.one)
        return [field.Element(value.a.numer.get((j,),QQ.zero)/da,
                              value.b.numer.get((j,),QQ.zero)/db) for j in range(degree+1)]
    aa=total.a.numer.div(total.a.denom)[0]
    bb=total.b.numer.div(total.b.denom)[0]
    polynomial=field.Element(field.base(aa),field.base(bb))
    pc=poly_coefficients(polynomial)
    integral=sum((pc[j]*r**(j+1)/(j+1) for j in range(len(pc))),zero)
    basis=[r/J**3,1/J**3,r/J**2,1/J**2,r/J,1/J]
    columns=[poly_coefficients(phi.diff(r)*J**4) for phi in basis]
    target=poly_coefficients((total-polynomial)*J**4)
    rows=max(len(target),*(len(c) for c in columns))
    work=[[columns[j][i] if i<len(columns[j]) else zero for j in range(6)]
          +[target[i] if i<len(target) else zero] for i in range(rows)]
    for j in range(6):
        pivot=next(i for i in range(j,rows) if work[i][j])
        work[j],work[pivot]=work[pivot],work[j]
        divisor=work[j][j]
        work[j]=[x/divisor for x in work[j]]
        for i in range(rows):
            if i==j or not work[i][j]:continue
            factor=work[i][j]
            work[i]=[a-factor*b for a,b in zip(work[i],work[j])]
    assert all(not x for row in work[6:] for x in row)
    coefficients=[work[j][-1] for j in range(6)]
    stated=[(34960*t-16932)/81,(7004*t-23476)/81,
            (5228*t+3356)/81,(8022*t-8974)/81,
            -(154*t+214)/27,-(55*t+697)/27]
    assert all(not(a-b) for a,b in zip(coefficients,stated))
    primitive=integral+sum((a*phi for a,phi in zip(coefficients,basis)),zero)
    assert not primitive.diff(r)-total
    def evaluate(value,point):
        def poly(P):return sum((field.convert(c)*point**power[0] for power,c in P.items()),zero)
        return poly(value.a.numer)/poly(value.a.denom)+t*poly(value.b.numer)/poly(value.b.denom)
    cap1,cap2=evaluate(primitive,field.convert(-2)),evaluate(primitive,1-t)
    classical_end=evaluate(primitive,field.convert(-1))
    capgap=cap2-cap1;classgap=classical_end-cap1
    assert not capgap-(889-125*t)/216
    assert not classgap-(1076-991*t)/432
    base_invariant=capgap/(3-t)-classgap
    assert not base_invariant-(295*t-138)/112
    poles=(2*t-1,-(1+4*t)/3)
    pole_records=[]
    for cp in poles:
        point=field.domain.from_sympy(field.to_sympy(cp))
        valuation,residue=valuation_residue(total,point,field)
        pole_records.append({'r':str(field.to_sympy(cp)),'valuation':valuation,
                             'residue':str(field.domain.to_sympy(residue))})
    assert all(x['valuation']==-4 and x['residue']=='0' for x in pole_records)
    return {'physical_projection_jacobian_numerator':str(field.to_sympy(J)),
            'prefix_principal_minor':str(field.to_sympy(V)),
            'numerator_after_multiplying_J_fourth_is_polynomial':True,
            'numerator_degree':len(poly_coefficients(numerator))-1,
            'finite_poles_exactly_projection_caustics':pole_records,
            'pole_order_at_r_infinity':2,
            'polynomial_part':str(field.to_sympy(polynomial)),
            'primitive_polynomial_part':str(field.to_sympy(integral)),
            'primitive_basis':['r/J^3','1/J^3','r/J^2','1/J^2','r/J','1/J'],
            'primitive_coefficients':[str(field.to_sympy(x)) for x in coefficients],
            'exact_derivative_certificate':True,
            'two_cap_primitive_gap_G_1_minus_t_minus_G_minus2':str(field.to_sympy(cap2-cap1)),
            'classical_centralizer_gap_G_minus1_minus_G_minus2':str(field.to_sympy(classical_end-cap1)),
            'base_only_unit_invariant_difference_of_average_gaps':str(field.to_sympy(base_invariant)),
            'base_only_constant_changes_both_gaps_by_interval_length':True}


def evaluate_poly(poly, point):
    return poly.evaluate(poly.ring.gens[0], point)


def valuation_residue(value, point, field):
    if isinstance(field,QuadraticFractionField):
        domain=field.domain
        def at(poly):
            result=domain.zero
            for (power,),coefficient in poly.terms():
                result+=domain.convert(coefficient,QQ)*point**power
            return result
        def rational_coefficients(frac):
            if not frac:return {}
            def taylor(poly):
                values=[];fac=1
                for j in range(poly.degree()+1):
                    if j:fac*=j
                    values.append(at(poly)/domain.convert(fac))
                    poly=poly.diff(poly.ring.gens[0])
                return values
            aa,bb=taylor(frac.numer),taylor(frac.denom)
            nv=next(j for j,x in enumerate(aa) if x)
            dv=next(j for j,x in enumerate(bb) if x)
            val=nv-dv
            if val>0:return {val:aa[nv]/bb[dv]}
            cc=[]
            for j in range(-val+1):
                av=aa[nv+j] if nv+j<len(aa) else domain.zero
                cc.append((av-sum(((bb[dv+k] if dv+k<len(bb) else domain.zero)*cc[j-k]
                                  for k in range(1,j+1)),domain.zero))/bb[dv])
            return {val+j:x for j,x in enumerate(cc)}
        aa,bb=rational_coefficients(value.a),rational_coefficients(value.b)
        t=domain.from_sympy(field.t_symbol)
        powers=set(aa)|set(bb)
        merged={j:aa.get(j,domain.zero)+t*bb.get(j,domain.zero) for j in powers}
        nonzero=[j for j,x in merged.items() if x]
        valuation=min(nonzero) if nonzero else None
        return valuation,merged.get(-1,domain.zero)
    if not value:
        return None, field.domain.zero
    var=value.numer.ring.gens[0]
    linear=var-point
    numerator,denominator=value.numer,value.denom
    nv=dv=0
    while not evaluate_poly(numerator,point):
        numerator,remainder=numerator.div(linear)
        assert not remainder
        nv+=1
    while not evaluate_poly(denominator,point):
        denominator,remainder=denominator.div(linear)
        assert not remainder
        dv+=1
    valuation=nv-dv
    if valuation>=0:
        return valuation,field.domain.zero
    order=-valuation-1
    def coefficients(poly):
        out=[];factorial=1
        for j in range(order+1):
            if j:
                factorial*=j
            out.append(evaluate_poly(poly,point)/field.domain.convert(factorial))
            poly=poly.diff(var)
        return out
    aa,bb=coefficients(numerator),coefficients(denominator)
    cc=[]
    for j in range(order+1):
        cc.append((aa[j]-sum((bb[k]*cc[j-k] for k in range(1,j+1)),field.domain.zero))/bb[0])
    return valuation,cc[-1]


def critical_data(field, t):
    r=field.gens[0];one,zero=field.one,field.zero
    s=one
    A=(one,one,zero,one);B=(one,zero,t,one)
    C=matmul(matmul(matmul(matmul(inverse(A),B),A),inverse(B)),A)
    F=(r,one-r,s,-s)
    mus=(A,B,C)
    previous=(one,zero,zero,one);states=[]
    for mu in mus:
        H=tuple(-x for x in matmul(matmul(inverse(F),mu),F))
        G=matmul(matmul(previous,H),inverse(previous));k,e=G[0],G[1];f=G[2]/k
        states.append((k,e,f))
        previous=matmul((one,zero,-k*f,k),previous)
    return states


def compute(field,t,label,save_expression=False):
    start=time.monotonic();one,zero=field.one,field.zero
    r=field.gens[0]
    states=critical_data(field,t);initial=list(states)
    # k2=a2-a0+k3. Remaining variables are (k1,k3,k4).
    transverse=sp.Matrix([[0,0,0],[1,0,0],[0,1,0],[0,1,0],[0,0,1]])
    maps=[sp.Matrix(P)*transverse for P in closure_embedding(3,WORDS[0])]
    # Initial closed a1=a0-k1+k2-k4, a2=a0+k2-k3.
    initial_closed=[sp.Matrix([[1,-1,1,0,-1]])*transverse,
                    sp.Matrix([[1,0,1,-1,0]])*transverse]
    H=[[zero for _ in range(3)] for _ in range(3)]
    gradient=[-sum((field.convert(int(row[i])) for row in initial_closed),zero) for i in range(3)]
    loghessian=[[zero for _ in range(3)] for _ in range(3)]
    atoms=[];variable_a1=zero
    epsilon=(1,1,1,-1,-1)
    alpha=(-one/2,-one/2,one/2,one/2,-one/2)
    for n,(slot,sign) in enumerate(WORDS[0]):
        k,e,f=states[slot];l,g,h=states[slot+1]
        A,B=-one/k,-one/l
        C=one/(one-e*h) if sign>0 else one-k*g*f/l
        if sign>0:
            shapes=(B,C,one/A,B*C,C/A)
            vectors=((0,1,0),(0,0,1),(-1,0,0),(0,1,1),(-1,0,1))
            quadratic=sp.Matrix([[0,1,1],[1,0,-1],[1,-1,-1]])
            monomial=sp.Matrix([[sp.Rational(1,2),sp.Rational(1,2),0]])
        else:
            shapes=(A,C,one/B,A*C,C/B)
            vectors=((1,0,0),(0,0,1),(0,-1,0),(1,0,1),(0,-1,1))
            quadratic=sp.Matrix([[0,-1,0],[-1,0,0],[0,0,0]])
            monomial=sp.Matrix([[-sp.Rational(1,2),-sp.Rational(1,2),sp.Rational(1,2)]])
        P=maps[n]
        q=P.T*quadratic*P
        mg=monomial*P
        for i,j in product(range(3),repeat=2):H[i][j]+=field.convert(int(q[i,j]))
        for i in range(3):gradient[i]+=field.convert(int(mg[i].p))/int(mg[i].q)
        for z,v,eps,al in zip(shapes,vectors,epsilon,alpha):
            vv=tuple(int(x) for x in sp.Matrix([v])*P)
            f0=z/(one-z);h0=z/(one-z)**2;q0=z*(one+z)/(one-z)**3
            variable_a1+=eps*f0/12
            for i in range(3):
                gradient[i]-=al*f0*vv[i]
                for j in range(3):
                    H[i][j]+=eps*f0*vv[i]*vv[j]
                    loghessian[i][j]-=al*h0*vv[i]*vv[j]
            atoms.append((vv,eps*h0,eps*q0))
        states[slot:slot+2]=crossing(states[slot],states[slot+1],sign)
    assert all(not(a-b) for X,Y in zip(states,initial) for a,b in zip(X,Y))
    G,determinant=inverse3(H,one,zero)
    print(label,'built exact critical Hessian',round(time.monotonic()-start,3),flush=True)
    mv=lambda v:[sum((G[i][j]*v[j] for j in range(3)),zero) for i in range(3)]
    Ggradient=mv(gradient)
    phase3={};phase4={}
    for v,b,c in atoms:
        if not any(v):continue
        if next(x for x in v if x)<0:
            v=tuple(-x for x in v);b=-b
        phase3[v]=phase3.get(v,zero)+b
        phase4[v]=phase4.get(v,zero)+c
    vectors=list(phase3)
    metric={v:mv(v) for v in vectors}
    norms={v:dot(v,metric[v],zero) for v in vectors}
    contributions={}
    contributions['variable_compact_factor']=variable_a1
    contributions['amplitude_second']=-sum((G[i][j]*loghessian[i][j] for i,j in product(range(3),repeat=2)),zero)/2-dot(gradient,Ggradient,zero)/2
    contributions['amplitude_cubic']=sum((phase3[v]*norms[v]*dot(v,Ggradient,zero) for v in vectors),zero)/2
    contributions['phase_quartic']=sum((phase4[v]*norms[v]**2 for v in vectors),zero)/8
    contributions['cubic_cross']= -sum((phase3[v]*phase3[w]*dot(v,metric[w],zero)**3 for v in vectors for w in vectors),zero)/12
    tadpole=[sum((phase3[v]*norms[v]*v[i] for v in vectors),zero) for i in range(3)]
    contributions['cubic_internal']=-dot(tadpole,mv(tadpole),zero)/8
    print(label,'contracted Wick tensors',round(time.monotonic()-start,3),flush=True)
    total=sum(contributions.values(),zero)
    point=field.domain.convert(-2)
    records={}
    for name,value in contributions.items():
        val,res=valuation_residue(value,point,field)
        records[name]={'valuation_at_r_minus2':val,'residue':str(field.domain.to_sympy(res))}
    valuation,residue=valuation_residue(total,point,field)
    other_point=field.domain.one-field.domain.from_sympy(field.to_sympy(t))
    other_valuation,other_residue=valuation_residue(total,other_point,field)
    result={'field':label,'external_actual_positions':['a0','a2'],
            'transverse_actual_flows':['k1','k3','k4'],'exact_relation':'k2=a2-a0+k3',
            's_specialized_after_all_flow_derivatives':1,'boundary_r':-2,
            'phase_convention':'exp(S/H), covariance=-H*(S_perp_second)^-1',
            'base_only_line_retained_separately':True,'number_local_atoms':len(atoms),
            'number_cubic_vector_classes':len(vectors),'pieces':records,
            'total_valuation':valuation,'total_residue':str(field.domain.to_sympy(residue)),
            'other_k_equals1_sheet_r':str(field.domain.to_sympy(other_point)),
            'other_sheet_valuation':other_valuation,'other_sheet_residue':str(field.domain.to_sympy(other_residue)),
            'correction_constant_in_r':not total.diff(r),
            'Omega_times_z1_ds_residue':str(field.domain.to_sympy(-residue/2)),
            'elapsed_seconds':round(time.monotonic()-start,3),
            'scope':'Actual transverse formal first-loop framing residue on the candidate eta_geo incidence boundary; no pushforward of the independent actual eta_F cap or global source claim.'}
    if save_expression:
        result['relative_one_loop_rational_function']=str(field.to_sympy(total))
        if isinstance(field,QuadraticFractionField):
            result['relative_one_loop_quadratic_pair']={'a':str(field.base.to_sympy(total.a)),
                                                        'b':str(field.base.to_sympy(total.b)),
                                                        't':'(1-sqrt(-3))/2, t^2-t+1=0'}
            result['hermite_primitive_certificate']=hermite_certificate(field,total)
    return result


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--exact',action='store_true');parser.add_argument('--fast-exact',action='store_true');args=parser.parse_args()
    r=sp.symbols('r')
    if args.fast_exact:
        field=QuadraticFractionField(r);t=field.Element(0,1)
        result=compute(field,t,'Q(r)[t]/(t^2-t+1)',save_expression=True)
        name='figure_eight_first_loop_cap_exact_results.json'
    elif args.exact:
        base=QQ.algebraic_field(sp.sqrt(-3));field=base.frac_field(r)
        t=(field.one-field.convert(base.from_sympy(sp.sqrt(-3)),base))/2
        result=compute(field,t,'Q(sqrt(-3))(r)',save_expression=True)
        name='figure_eight_first_loop_cap_exact_results.json'
    else:
        p=97;roots=[x for x in range(p) if (x*x-x+1)%p==0]
        field=GF(p).frac_field(r)
        result=[compute(field,field.convert(t),f'F_{p}(r), Riley={t}',save_expression=True) for t in roots]
        name='figure_eight_first_loop_cap_modular_results.json'
    target=Path(__file__).with_name(name);target.write_text(json.dumps(result,indent=2)+'\n')
    if isinstance(result,dict):
        summary={'result':str(target),'field':result['field'],
                 'marked_cap_residue':result['total_residue'],
                 'other_cap_residue':result['other_sheet_residue'],
                 'correction_constant_in_r':result['correction_constant_in_r'],
                 'exact_rational_primitive':result.get('hermite_primitive_certificate',{}).get('exact_derivative_certificate',False)}
    else:
        summary={'result':str(target),'modular_places':len(result),
                 'cap_residues':[x['total_residue'] for x in result]}
    print(json.dumps(summary,indent=2),flush=True)


if __name__=='__main__':main()
