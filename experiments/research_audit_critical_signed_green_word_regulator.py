"""QUARANTINED SOURCE LABEL: formal complete-color shapes on a mixed Gauss word.

The matrix word is universal, but auxiliary color is not -1. This verifier
does NOT identify the actual mixed-source Bloch symbol or regulator.

This verifier keeps Gaussian rational units, including their log norms.
It has no numerical optimizer or floating-point tolerance.
"""
import argparse
from collections import Counter, defaultdict
from functools import lru_cache
import json
from pathlib import Path
import sympy as s

b, t, v = s.symbols("b t v", real=True, nonzero=True)
VARIABLES = (b, t, v)
I = s.I
sn = 2*v/(1+v*v)
kk = (1-v*v)/(1+v*v)
x = (t*t-b-b*b*sn*sn)/(b+1)
c = b+(x+1)/(sn*sn)
sigma = -2+4*sn*sn


def clean(z):
    return s.factor(s.cancel(z))


def head(X, S):
    K = clean(-1/X)
    F = clean(S*(1-X))
    E = clean((1/X-1)/S)
    return (s.Matrix([[K,E],[clean(F*K),clean(F*E+1/K)]]),
            s.Matrix([[1,0],[clean(-K*F),K]]), (K,E,F))


def crossing(left, right):
    k,e,f = left
    l,g,h = right
    A0, B0 = -1/k, -1/l
    d = clean(1-e*h)
    output = [
        (clean(l*d), clean((d*g+e*(d*l-1/l))/k), clean(k*h/d)),
        (clean(k/d), clean(e/(l*d)), clean(l*(d*f+h*(d/k-k))))]
    # Formal complete-color five-shape expression; NOT the mixed-color symbol.
    symbols = [(1,clean(B0)),(1,clean(1/d)),(1,clean(1/A0)),
               (-1,clean(B0/d)),(-1,clean(1/(d*A0)))]
    return output, symbols


@lru_cache(None)
def vectors(z):
    """log|z| and dArg(z), in a factor basis with conjugates identified."""
    numerator, denominator = s.fraction(s.cancel(z))
    norm = defaultdict(lambda:s.Integer(0))
    argument = defaultdict(lambda:s.Integer(0))
    for poly, sign in [(numerator,1),(denominator,-1)]:
        constant, factors = s.factor_list(poly,*VARIABLES,extension=I)
        for factor, exponent in factors:
            polynomial = s.Poly(factor,*VARIABLES,extension=I)
            leading = polynomial.LC()
            factor = polynomial.monic().as_expr()
            constant *= leading**exponent
            conjugate = s.Poly(s.conjugate(factor).expand(),
                               *VARIABLES,extension=I).monic().as_expr()
            if s.srepr(factor) <= s.srepr(conjugate):
                key, orientation = factor, 1
            else:
                key, orientation = conjugate, -1
            norm[("polynomial",key)] += sign*exponent
            if factor != conjugate:
                argument[("polynomial",key)] += sign*orientation*exponent
        # KEEP Gaussian rational units: |a+ib|² is a positive rational.
        norm_squared = s.factor(constant*s.conjugate(constant))
        assert norm_squared.is_Rational and norm_squared>0
        for prime,exponent in s.factorint(s.numer(norm_squared)).items():
            norm[("prime",prime)] += s.Rational(sign*exponent,2)
        for prime,exponent in s.factorint(s.denom(norm_squared)).items():
            norm[("prime",prime)] -= s.Rational(sign*exponent,2)
    return dict(norm),dict(argument)


def differential_certificate(atoms, forces):
    tensor = defaultdict(lambda:s.Integer(0))
    def add(norm, argument, coefficient):
        for n,en in norm.items():
            for a,ea in argument.items():
                tensor[n,a] += coefficient*en*ea
    for coefficient,z in atoms:
        if not z.free_symbols:
            continue
        nz,az = vectors(z)
        nc,ac = vectors(1-z)
        # dD(z)=log|z| dArg(1-z)-log|1-z| dArg(z).
        add(nz,ac,coefficient)
        add(nc,az,-coefficient)
    for weight,phase,coefficient in forces:
        nw,_ = vectors(weight)
        _,ap = vectors(phase)
        add(nw,ap,-coefficient)
    nonzero = {key:value for key,value in tensor.items() if value}
    assert not nonzero, nonzero
    return len(tensor)


def valuation_at_one(z):
    numerator,denominator = s.fraction(s.cancel(z))
    numerator_order=denominator_order=0
    while s.expand(numerator.subs(v,1)) == 0:
        numerator=s.cancel(numerator/(v-1))
        numerator_order+=1
    while s.expand(denominator.subs(v,1)) == 0:
        denominator=s.cancel(denominator/(v-1))
        denominator_order+=1
    order=numerator_order-denominator_order
    leading_numerator=numerator.subs(v,1)
    leading_denominator=denominator.subs(v,1)
    leading=clean(leading_numerator/leading_denominator)
    if order==0:
        assert clean(leading-s.conjugate(leading))==0
    return {"order":order,"leading":str(leading),
            "uncancelled_leading_numerator":str(leading_numerator),
            "uncancelled_leading_denominator":str(leading_denominator),
            "finite_unit_real":True if order==0 else None}


def physical_domain_certificate(atoms):
    """No reduced shape has a 0/0 point on the positive critical domain."""
    xx=s.Symbol("positive_x", real=True, positive=True)
    dd=1+v*v
    substitution=xx*(b+1)+b+4*b*b*v*v/dd**2
    r1=b*b*v*v+2*b*v*v-t*t*dd**2/4-v**4/4+3*v*v/2-s.Rational(1,4)
    rx=b*b*v*v+b*dd**2/4-t*t*dd**2/4
    r2=(b*b*v**6-6*b*b*v**4+b*b*v*v-2*b*v**6-4*b*v**4
        -2*b*v*v-t*t*v**8/4+t*t*v**6+5*t*t*v**4/2+t*t*v*v
        -t*t/4-v**8/4-v**6-3*v**4/2-v*v-s.Rational(1,4))
    rp=b*v*v+(t*t+1)*dd**2/4
    rc=(b*b*v*v+I*b*t*v**4/2-I*b*t/2+b*v**4/2+b*v*v+b/2
        -t*t*dd**2/4+I*t*v**4/2-I*t/2+v**4/4+v*v/2+s.Rational(1,4))
    # Independently expected physical reductions, with all positive factors retained.
    expected=[
        -(b+1)*dd**2*(xx+1-2*sn**2)/4,
        -xx*(b+1)*dd**2/4,
        -(b+1)*dd**4*(xx+1-2*xx*sn**2)/4,
        (b+1)*dd**2*(xx+1+b*sn**2)/4]
    for p,e in zip([r1,rx,r2,rp],expected):
        assert clean(p.subs(t*t,substitution)-e)==0
    assert clean(s.im(rc)-(b+1)*t*(v**4-1)/2)==0
    def monic(p):
        return s.Poly(p,*VARIABLES,extension=I).monic().as_expr()
    allowed={monic(p) for p in [b,b+1,v,v-1,v+1,v-I,v+I,r1,rx,r2,rp,rc]}
    checked=0
    for _,z in atoms:
        for polynomial in s.fraction(s.cancel(z)):
            _,factors=s.factor_list(polynomial,*VARIABLES,extension=I)
            for factor,_ in factors:
                assert monic(factor) in allowed, factor
                checked+=1
    # The only possibly vanishing factors are r1 and r2. Their two
    # equations imply xx=1 and sn²=1, outside 0<v<1.
    return checked


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,default=Path(__file__).with_name(
        "research_critical_signed_green_word_regulator_results.json"))
    args=parser.parse_args()
    counts=Counter()
    pin=(t-I*b*kk)/(t+I*b*kk)
    pout=(t-I*c*kk)/(t+I*c*kk)
    Ai,L1,h1=head(-x/b,-pin)
    G2,L2,h2=head(-b,1)
    P=(L1.inv()*G2*L1*Ai).applyfunc(clean)
    assert clean(s.trace(P)-sigma)==0
    counts["exact_main_product_trace"]+=1
    # This is the raw determinant-one lift -i C^{-1} at R0=-1.
    aux=((2*P-sigma*s.eye(2))/(4*sn*kk)).applyfunc(clean)
    assert clean(s.det(aux)-1)==0 and s.trace(aux)==0
    assert (aux*aux+s.eye(2)).applyfunc(clean)==s.zeros(2)
    counts["exact_trace_zero_auxiliary_identities"]+=3
    L=(L2*L1).applyfunc(clean)
    nyb=(x-1)+b*(x+2*kk*kk-1)+2*I*kk*t
    nyc=(x-1)-c*(x+2*kk*kk-1)-2*I*kk*t
    nxb=x*(1-x)+b*(1+x*(2*kk*kk-1))+2*I*x*kk*t
    nxc=x*(1-x)-c*(1+x*(2*kk*kk-1))-2*I*x*kk*t
    gout=clean(nyb*(1-c)/(nyc*(1+b)))
    _,_,o1=head(x/c,-gout*pout)
    _,_,o2=head(c,gout)
    # 2pi dh = log b dArg pin - log c dArg pout
    #           -log x dArg(Ex_input/Ex_output), since y=1.
    forces=[(clean(b),clean(pin),1),(clean(c),clean(pout),-1),
            (clean(x),clean(nxb/nxc),-1)]
    records=[]
    for lift in [1,-1]:
        G3=(L*(lift*aux)*L.inv()).applyfunc(clean)
        h3=tuple(clean(a) for a in (G3[0,0],G3[0,1],
                                    G3[1,0]/G3[0,0]))
        heads=[h1,h2,h3]
        atoms=[]
        for position in [1,0,0,1]:
            replacement,symbols=crossing(*heads[position:position+2])
            heads[position:position+2]=replacement
            atoms+=symbols
        for actual,expected in zip(heads,[o1,o2,h3]):
            for a,e in zip(actual,expected):
                assert clean(a-e)==0
                counts["exact_returned_head_coordinates"]+=1
        print("actual word closure PASS, lift",lift,flush=True)
        tensor_size=differential_certificate(atoms,forces)
        counts["exact_zero_differential_tensors"]+=1
        print("exact regulator differential PASS, lift",lift,flush=True)
        counts["physical_shape_factor_incidences"]+=physical_domain_certificate(atoms)
        counts["exact_physical_factor_reductions"]+=5
        calibration=[]
        for coefficient,shape in atoms:
            item=valuation_at_one(shape)
            item.update({"coefficient":int(coefficient),"shape":str(shape)})
            calibration.append(item)
            counts["exact_shape_endpoint_valuations"]+=1
        records.append({"auxiliary_central_lift":lift,
                        "expanded_tensor_positions":tensor_size,
                        "endpoint_order_counts":dict(Counter(
                            str(a["order"]) for a in calibration)),
                        "actual_twenty_shapes":calibration})
    result={"status":"PASS","counts":dict(counts),
            "field":"Q(i)(b,T,v), y=1, x=(T^2-b-b^2*s^2)/(b+1), s=2v/(1+v^2)",
            "scope":"FORMAL complete-color five-shape identity on the universal R0=-1 mixed Gauss word. Auxiliary color factors are OMITTED; actual mixed-source/regulator identification is WITHDRAWN. Exact matrix closure and formal differential/calibration only.",
            "lifts":records}
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":"PASS","counts":dict(counts),
                      "output":str(args.output)},indent=2))


if __name__=="__main__":
    main()
