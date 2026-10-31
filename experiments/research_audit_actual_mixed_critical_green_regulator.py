"""Unpublished exact ACTUAL mixed-color critical Green word certificate.

Generates every head and color from the literal universal crossing, without
reading any private/formal result. The imported helper supplies only rational
Gauss maps, factor arithmetic and the proved formal-domain classification.
"""
import argparse
from collections import Counter
from functools import lru_cache
import json
from pathlib import Path
import sympy as s
import research_audit_critical_signed_green_word_regulator as a
b,t,v=a.b,a.t,a.v;I=s.I;x,c=a.x,a.c;sn,kk=a.sn,a.kk;clean=a.clean


def negative(left,right):
    k,e,f=left;l,g,h=right
    d=clean(1-(k/l)*g*f)
    output=[(clean(l*d),clean(k*g),clean(f+h/k-f/(l*l*d))),
            (clean(k/d),clean(l*e+g-k*k*g/d),clean(f/l))]
    # This final crossing has two MAIN colors -1.
    symbols=[(1,clean(-1/k)),(1,d),(1,clean(-l)),
             (-1,clean(-d/k)),(-1,clean(-d*l))]
    return output,symbols


@lru_cache(None)
def factors(poly):
    return s.factor_list(poly,b,t,v,extension=I)


def half_domain(atoms,eps):
    """The generated formal shapes have exactly one possible real divisor."""
    xx=s.Symbol('positive_x',real=True,positive=True);dd=1+v*v
    T2=xx*(b+1)+b+4*b*b*v*v/dd**2
    def monic(p,variables,extension=None):
        return s.Poly(p,*variables,extension=extension).monic().as_expr()
    exceptional=(xx+1)*dd**2-16*(xx if eps==1 else 1)*v*v
    exceptional=monic(exceptional,(b,xx,v))
    allowed={monic(p,(b,xx,v)) for p in
             [b,b+1,v,dd,xx,xx+1,(xx+1)*dd**2+4*b*v*v]}
    allowed.add(exceptional)
    seen=set();potential=set();counts=Counter()
    for _,z in atoms:
        for polynomial in s.fraction(s.cancel(z)):
            _,ff=factors(polynomial)
            for f,_ in ff:
                f=monic(f,(b,t,v),I);counts['factor_incidences']+=1
                if f in seen:continue
                seen.add(f);im=s.factor(s.im(f))
                if im!=0:
                    if im not in [1,-1]:
                        q=s.factor(im/(t*(b+1)*(v**4-1)))
                        assert q in [s.Rational(1,6),s.Rational(-1,6),
                                     s.Rational(1,2),s.Rational(-1,2),v*v/2,-v*v/2]
                    counts['nonzero_imaginary_certificates']+=1
                else:
                    g=clean(f.subs(t*t,T2))
                    assert t not in g.free_symbols
                    contains=False
                    for pp in s.fraction(g):
                        coefficient,gg=s.factor_list(pp,b,xx,v)
                        assert coefficient.is_Rational and coefficient!=0
                        for factor,_ in gg:
                            normalized=monic(factor,(b,xx,v))
                            assert normalized in allowed,(eps,factor)
                            contains=contains or normalized==exceptional
                    if contains:potential.add(f)
                    counts['real_factor_certificates']+=1
    assert len(potential)==1
    return dict(counts)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,default=Path(__file__).with_name(
        'research_actual_mixed_critical_green_regulator_results.json'))
    args=ap.parse_args();counts=Counter();records=[]
    pin=(t-I*b*kk)/(t+I*b*kk);pout=(t-I*c*kk)/(t+I*c*kk)
    G1,L1,h1=a.head(-x/b,-pin);G2,L2,h2=a.head(-b,1)
    P=(L1.inv()*G2*L1*G1).applyfunc(clean);sig=a.sigma
    assert clean(s.trace(P)-sig)==0
    L=(L2*L1).applyfunc(clean)
    nyb=(x-1)+b*(x+2*kk*kk-1)+2*I*kk*t
    nyc=(x-1)-c*(x+2*kk*kk-1)-2*I*kk*t
    nxb=x*(1-x)+b*(1+x*(2*kk*kk-1))+2*I*x*kk*t
    nxc=x*(1-x)-c*(1+x*(2*kk*kk-1))-2*I*x*kk*t
    gout=clean(nyb*(1-c)/(nyc*(1+b)))
    _,_,o1=a.head(x/c,-gout*pout);_,_,o2=a.head(c,gout)
    forces=[(b,clean(pin),1),(clean(c),clean(pout),-1),
            (clean(x),clean(nxb/nxc),-1)]
    for eps in [0,1,-1]:
        M=((2*P-sig*s.eye(2))/(4*sn*kk) if eps==0 else
           (((sig+1)*s.eye(2)-P)/(2*sn) if eps==1 else -(P+s.eye(2))/(2*sn)))
        M=M.applyfunc(clean)
        assert clean(s.det(M)-1)==0
        # Actual preferred longitude lambda=P; ell=-P is centered.
        word=(M*M*(P**eps)).applyfunc(clean)
        expected=-s.eye(2) if eps==0 else s.eye(2)
        assert word==expected
        counts['exact_preferred_word_identities']+=1
        for lift in [1,-1]:
            G3=(L*(lift*M)*L.inv()).applyfunc(clean)
            h3=tuple(clean(q) for q in [G3[0,0],G3[0,1],G3[1,0]/G3[0,0]])
            heads=[h1,h2,h3];crossing_data=[];formal=[]
            for pos in [1,0,0,1]:
                left,right=heads[pos:pos+2];K1,E1,F1=left;K2,E2,F2=right
                d=clean(1-E1*F2)
                crossing_data.append((pos,K1,K2,d))
                out,syms=a.crossing(left,right);heads[pos:pos+2]=out;formal+=syms
            final_symbols=[]
            if eps:
                out,final_symbols=(a.crossing if eps==1 else negative)(*heads[:2])
                heads[:2]=out;formal+=final_symbols
            for actual,expected_head in zip(heads,[o1,o2,h3]):
                for q,r in zip(actual,expected_head):
                    assert clean(q-r)==0
                    counts['exact_returned_head_coordinates']+=1
            if eps==0:
                domain={'factor_incidences':a.physical_domain_certificate(formal)}
            else:domain=half_domain(formal,eps)
            print('direct matrix/domain PASS',eps,lift,flush=True)
            for flag in [1,-1]:
                # Flag+1 is the selected P=J raw eigenline; flag-1 its reciprocal.
                chi0=-lift*I if eps==0 else lift*(eps*sn+I*kk)
                eig0=lift*I if eps==0 else -lift*I*(kk+I*eps*sn)
                chi=clean(chi0**flag);eig=clean(eig0**flag)
                assert clean(chi*eig-1)==0
                assert clean(chi*s.conjugate(chi)-1)==0
                assert clean(chi+1/chi-s.trace(lift*M))==0
                counts['exact_color_flag_unit_trace_identities']+=3
                colors=[s.Integer(-1),s.Integer(-1),chi];atoms=[];changed=[]
                for j,(pos,K1,K2,d) in enumerate(crossing_data):
                    ch1,ch2=colors[pos:pos+2]
                    # DERIVED DIRECTLY FROM THE LITERAL MIXED COEFFICIENT:
                    # A=ch1/K1, B=ch2/K2, C=1/d.
                    shapes=[ch2/K2,1/d,ch1*K1,ch2/(K2*d),ch1*K1/d]
                    for n,z in zip([1,1,1,-1,-1],shapes):atoms.append((n,clean(z)))
                    for j0,fac in enumerate([-ch2,1,-ch1,-ch2,-ch1]):
                        assert clean(atoms[5*j+j0][1]-fac*formal[5*j+j0][1])==0
                        if fac!=1:changed.append(5*j+j0)
                    colors[pos:pos+2]=[ch2,ch1]
                assert colors==[-1,-1,chi]
                assert changed==[0,3,5,8,12,14,17,19]
                atoms+=final_symbols
                size=a.differential_certificate(atoms,forces)
                counts['exact_actual_mixed_differential_tensors']+=1
                vals=[]
                for coefficient,z in atoms:
                    val=a.valuation_at_one(z)
                    # BEFORE cancelling the leading ratio, exclude a hidden 0/0
                    # at the chosen b=1,x=2 endpoint anchor.
                    for key in ["uncancelled_leading_numerator",
                                "uncancelled_leading_denominator"]:
                        endpoint_piece=s.sympify(val[key],locals={'b':b,'t':t})
                        endpoint_piece=clean(endpoint_piece.subs({b:1,t:s.sqrt(6)}))
                        assert endpoint_piece!=0 and endpoint_piece.is_finite
                        counts['uncancelled_anchor_nonzero_checks']+=1
                    if eps:
                        anchor=clean(s.sympify(val['leading'],locals={'b':b,'t':t}).subs({b:1,t:s.sqrt(6)}))
                        assert val['order']==0 and anchor.is_real and anchor.is_finite
                    val.update({'coefficient':coefficient,'shape':str(z)})
                    vals.append(val);counts['actual_mixed_endpoint_valuations']+=1
                records.append({'epsilon':eps,'central_lift':lift,'raw_P_eigenflag':flag,
                    'auxiliary_color':str(chi),'selected_raw_eigenvalue':str(eig),
                    'tensor_positions':size,'domain_certificate':domain,'actual_mixed_shapes':vals})
                print('ACTUAL mixed tensor/calibration PASS',eps,lift,flag,flush=True)
    result={'status':'PASS','counts':dict(counts),'records':records,
        'scope':'Actual mixed-source symbols generated from universal head inputs and tracked colors; both reciprocal auxiliary flags and central lifts, all retained half signs. Local critical Bloch identity only; no protected/global relative-chain or source-cycle claim.'}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','counts':dict(counts),'output':str(args.output)},indent=2))

if __name__=='__main__':main()
