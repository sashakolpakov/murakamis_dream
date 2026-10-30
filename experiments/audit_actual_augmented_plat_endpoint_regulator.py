#!/usr/bin/env python3
"""Exact endpoint Hahn / literal crossing-circle regulator comparison.

All symbolic identities are in Q(T,a,b). The independent crossing graph uses
only the original physical Gauss rule, not the Hahn momentum equations.
"""
from collections import defaultdict
import json
from pathlib import Path
import mpmath as mp
import sympy as sp

T, a, b = sp.symbols('T a b', nonzero=True)
VARIABLES = (T, a, b)
def rat(x): return sp.factor(x)
def mat(x): return x.applyfunc(rat)

def head(X, S):
    K, F, E = -1/X, S*(1-X), (1/X-1)/S
    low = sp.Matrix([[1, 0], [-K*F, K]])
    G = sp.Matrix([[K, E], [F*K, F*E+1/K]])
    return mat(G), mat(low), tuple(map(rat, (K,E,F)))

def positive_or_negative_crossing(left, right, sign):
    k,e,f = left
    l,g,h = right
    A, B = rat(-1/k), rat(-1/l)
    if sign == 1:
        d = rat(1-e*h)
        c = rat(1/d)
        output = ((l*d, (d*g+e*(d*l-1/l))/k, k*h/d),
                  (k/d, e/(l*d), l*(d*f+h*(d/k-k))))
        atoms = [(1,B),(1,c),(1,1/A),(-1,B*c),(-1,c/A)]
    else:
        c = rat(1-(B/A)*g*f)
        output = ((l*c, k*g, f+h/k-f/(l*l*c)),
                  (k/c, l*e+g-k*k*g/c, f/l))
        atoms = [(1,A),(1,c),(1,1/B),(-1,A*c),(-1,c/B)]
    return [tuple(map(rat, h)) for h in output], [(e,rat(z)) for e,z in atoms]

def multiplicative_vector(z):
    out = defaultdict(int)
    for poly,sign in zip(sp.fraction(rat(z)), (1,-1)):
        constant,factors = sp.factor_list(poly,*VARIABLES)
        for prime,power in sp.factorint(abs(sp.numer(constant))).items():
            out['constant:'+str(prime)] += sign*power
        for prime,power in sp.factorint(abs(sp.denom(constant))).items():
            out['constant:'+str(prime)] -= sign*power
        for factor,power in factors:
            out[str(factor)] += sign*power
    return {k:v for k,v in out.items() if v}

def wedge(atoms):
    out = defaultdict(int)
    for epsilon,z in atoms:
        assert z not in (0,1)
        for x,ex in multiplicative_vector(z).items():
            for y,ey in multiplicative_vector(1-z).items():
                if x != y:
                    out[tuple(sorted((x,y)))] += epsilon*ex*ey*(1 if x<y else -1)
    return {k:v for k,v in out.items() if v}

def data(epsilon, high=False):
    Z, W = (a-1)/(a+1), (b-1)/(b+1)
    U, V = T*(a-1)**2/(T*a*a+1), T*(b-1)**2/(T*b*b+1)
    Y = lambda X,z: rat(-(1-X)*(T*z+X)/((X-z)*(T-X)))
    D = rat(Z*W*(T-U)*(T-V)/((T*Z+U)*(T*W+V)))
    G1,L1,h1 = head(V/T if high else V,Y(V,W))
    G2,L2,h2 = head(1/V if high else T/V,1)
    A, B = G1, mat(L1.inv()*G2*L1)
    P = mat(B*A)
    H = mat(P+sp.eye(2))
    assert mat(H*H) == sp.zeros(2)
    assert rat(sp.trace(P)+2) == 0
    if high:
        Aout,_,out1 = head(U/T,D*Y(V,W))
        _,_,out2 = head(1/U,D*Y(U,Z)*Y(V,W))
    else:
        Aout,_,out1 = head(U,1/(D*Y(U,Z)))
        _,_,out2 = head(T/U,1/D)
    bc = rat(sp.trace((H*A-A*H)*Aout)/32)
    expected = (2*T*a*b-T*a-T*b+a+b-2)/(2*(T+1)*(a-1)*(b-1))
    assert rat(bc-expected) == 0
    transport = mat(sp.eye(2)+bc*H)
    assert mat(transport*A*transport.inv()-Aout) == sp.zeros(2)
    aux_global = -(sp.eye(2)+(sp.Rational(epsilon,2)-bc)*H)
    aux_raw = mat((L2*L1)*aux_global*(L2*L1).inv())
    aux = (aux_raw[0,0],aux_raw[0,1],rat(aux_raw[1,0]/aux_raw[0,0]))
    heads = [h1,h2,aux]
    crossings=[]
    word=[(1,1),(0,1),(0,1),(1,1)]+([(0,epsilon)] if epsilon else [])
    for position,sign in word:
        out,atoms=positive_or_negative_crossing(heads[position],heads[position+1],sign)
        heads[position:position+2]=out
        crossings += atoms
    for actual,expected_head in zip(heads,(out1,out2,aux)):
        assert all(rat(x-y)==0 for x,y in zip(actual,expected_head))
    hahn=[]
    for X,z in ((U,Z),(V,W)):
        hahn += [(-1,rat(X)),(-1,rat(T/X)),(2,rat(z)),(2,rat(-1/z)),
                 (1,rat(X/z)),(1,rat(-T*z/X))]
    return hahn,crossings,bc

def bloch_wigner(z):
    return mp.im(mp.polylog(2,z))+mp.log(abs(z))*mp.arg(1-z)

def main():
    mp.mp.dps=65
    points=[(mp.mpc('.7','.3'),mp.mpc('1.4','.2'),mp.mpc('-.8','.6')),
            (mp.mpc('-1.2','.4'),mp.mpc('.6','-.3'),mp.mpc('1.7','.5')),
            (mp.mpf(2),mp.mpf(3),mp.mpf(5))]
    rows=[]
    for epsilon,high in [(e,h) for h in (False,True) for e in (0,1,-1)]:
        source,actual,bc=data(epsilon,high)
        ws,wa=wedge(source),wedge(actual)
        assert ws==wa
        assert not wedge(source+[(-e,z) for e,z in actual])
        fs=[(e,sp.lambdify(VARIABLES,z,'mpmath')) for e,z in source]
        fa=[(e,sp.lambdify(VARIABLES,z,'mpmath')) for e,z in actual]
        values=[]
        for point in points:
            vsource=mp.fsum(e*bloch_wigner(f(*point)) for e,f in fs)
            vactual=mp.fsum(e*bloch_wigner(f(*point)) for e,f in fa)
            assert abs(vsource-vactual)<mp.mpf('1e-52')
            if all(mp.im(v)==0 for v in point): assert abs(vsource)+abs(vactual)<mp.mpf('1e-52')
            values.append({'source_regulator':str(vsource),'actual_regulator':str(vactual),
                           'absolute_error':float(abs(vsource-vactual))})
        rows.append({'epsilon':epsilon,'physical_chamber':'high' if high else 'low','actual_crossing_count':4+bool(epsilon),
                     'all_nine_final_Gauss_coordinates_match':True,
                     'centralizer_coefficient':str(bc),
                     'common_wedge_nonzero_coefficients':len(ws),
                     'common_wedge':[[x,y,int(n)] for (x,y),n in sorted(ws.items())],
                     'exact_wedge_difference':[],
                     'hahn_atoms':[[e,str(z)] for e,z in source],
                     'actual_crossing_atoms':[[e,str(z)] for e,z in actual],
                     'regulator_checks':values})
    out={'status':'PASS','comparisons':rows,
         'scope':'Exact complete endpoint local regulator normalization, all three retained parities, both regular physical degree chambers. No selected cycle, amplitude, or asymptotic assertion.'}
    Path(__file__).with_name('actual_augmented_plat_endpoint_regulator_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS 6 exact rational crossing-circle comparisons, 54 final Gauss coordinates, 6 full wedge identities, 18 regulator checks')
if __name__=='__main__':main()
