#!/usr/bin/env python3
"""Actual signed reflection prefixes of the ideal RA cuboctahedron."""
import argparse
import itertools
import json
from pathlib import Path
import sympy as S


def simp(x):
    return S.simplify(S.expand_complex(x))


def H(n):
    n0,n1,n2,n3=n
    return S.Matrix([[n0-n3,-n1+S.I*n2],[-n1-S.I*n2,n0+n3]])


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    rt=S.sqrt(2)
    E=S.Matrix([[0,-1],[1,0]])
    # Every listed normal is unit spacelike. Shaded triangles have
    # n=(sqrt2,sx,sy,sz), whites n=(1,+/-sqrt2 e_i).
    whites={}
    for axis in range(3):
        for sign in [-1,1]:
            vec=[S.Integer(1),S.Integer(0),S.Integer(0),S.Integer(0)]
            vec[axis+1]=sign*rt
            whites[axis,sign]=S.Matrix(vec)
    shaded=[S.Matrix([rt,*ss]) for ss in itertools.product([-1,1],repeat=3)]
    vertices=[]
    for zero in range(3):
        for signs in itertools.product([-1,1],repeat=2):
            vec=[S.Integer(1)]+[S.Integer(0)]*3
            for axis,sign in zip([i for i in range(3) if i!=zero],signs):
                vec[axis+1]=sign/rt
            vertices.append(S.Matrix(vec))
    def lor(v,w):
        return -v[0]*w[0]+sum(v[i]*w[i] for i in range(1,4))
    supporting=0
    for n in list(whites.values())+shaded:
        assert S.simplify(lor(n,n)-1)==0
        for p in vertices:
            val=S.simplify(lor(n,p))
            assert val.is_nonpositive
            supporting+=1
    orthogonal=0
    for ss,n in zip(itertools.product([-1,1],repeat=3),shaded):
        for axis in range(3):
            assert S.simplify(lor(n,whites[axis,ss[axis]]))==0
            orthogonal+=1
    # Mark the actual main edge with ideal point (1,1,0)/sqrt2.
    # Matching edges flip the cube x-coordinate, so this z-edge is main.
    pmark=S.Matrix([1,1/rt,1/rt,0])
    z0=(1-S.I)/rt
    g=S.Matrix([[0,-1],[1,-z0]])
    gi=g.inv()
    hs={key:(gi.conjugate().T*H(n)*gi).applyfunc(simp) for key,n in whites.items()}
    ref=hs[0,1]
    assert simp(ref[0,0])==0 and simp(ref.det()+1)==0
    br=ref[0,1]
    assert simp(br*S.conjugate(br)-1)==0
    jr=E*ref.conjugate()
    qs={}
    prefix_checks=0
    for key,hf in hs.items():
        assert simp(hf.det()+1)==0
        af=hf[0,0]
        assert af.is_nonnegative
        assert (af==0)==(S.simplify(lor(whites[key],pmark))==0)
        q=(E*hf.conjugate()*jr.conjugate()).applyfunc(simp)
        assert simp(q.det()-1)==0
        assert simp(q[1,0]+af*S.conjugate(br))==0
        qs[key]=q
        prefix_checks+=1
    cases=[]
    # For matching in x, the middle white is x and the outers are y,z.
    # The two orders retain both actual orientations of the half disk.
    for ss in itertools.product([-1,1],repeat=3):
        for order in [(1,0,2),(2,0,1)]:
            keys=[(axis,ss[axis]) for axis in order]
            aa=[hs[k][0,0] for k in keys]
            pattern=''.join('0' if a==0 else '2' for a in aa)
            assert pattern in ['002','022','200','202','220','222']
            record={'pattern':pattern,'white_faces':keys}
            if aa[0]!=0 and aa[1]!=0:
                xx=simp(-qs[keys[0]][1,0]/qs[keys[1]][1,0])
                assert xx.is_negative
                record['finite_X']=str(xx)
            if aa[1]!=0 and aa[2]!=0:
                yy=simp(-qs[keys[1]][1,0]/qs[keys[2]][1,0])
                assert yy.is_negative
                record['finite_Y']=str(yy)
            if aa[0]!=0 and aa[2]!=0:
                tt=simp(qs[keys[0]][1,0]/qs[keys[2]][1,0])
                assert tt.is_positive
                record['finite_T']=str(tt)
            # Literal two puncture lifts have trace -2, not arbitrary +/-.
            A=(qs[keys[1]]*qs[keys[0]].inv()).applyfunc(simp)
            B=(qs[keys[2]]*qs[keys[1]].inv()).applyfunc(simp)
            assert simp(S.trace(A)+2)==0
            assert simp(S.trace(B)+2)==0
            assert simp(S.trace(B*A)+2)==0
            cases.append(record)
    q,X,Y=S.symbols('q X Y',nonzero=True)
    assert S.simplify(q*(X/q)-X)==0
    assert S.simplify(q**-1/(Y/q)-Y**-1)==0
    # All based punctures on one main component are conjugate to J^{+/-1}.
    # If that puncture fixes the marked cusp, the conjugator is a cusp
    # translation. Check BOTH exact resulting orientations and prefix lifts.
    r,s,rho,z0,aa=S.symbols('r s rho z0 aa',nonzero=True)
    def prefix_trace(mat):
        a0,b0,c0,d0=mat[0,0],mat[0,1],mat[1,0],mat[1,1]
        return -c0*r*r/s+(a0-d0+c0/s)*r+d0+b0*s
    def leading_quadratic(mat):
        return S.expand(prefix_trace(mat)).coeff(r,2)*rho**2
    one_main_cases=[]
    for eps in [-1,1]:
        puncture=-S.Matrix([[1,eps],[0,1]])
        other=S.Matrix([[aa,-(aa+1)**2/(4*eps)],[4*eps,-2-aa]])
        assert S.simplify(other.det()-1)==0
        assert S.trace(puncture*other)==-2
        assert S.trace(other*puncture)==-2
        for lift in [-1,1]:
            upper=lift*S.Matrix([[1,z0],[0,1]])
            # 200: Q1=upper, Q2=B Q1, Q0=A^{-1} Q1.
            w=other.inv()*upper
            l1=prefix_trace(upper)
            l2=prefix_trace(puncture*upper)
            kap=S.simplify(-leading_quadratic(w)/l1)
            finite=S.simplify(-l1/l2)
            assert S.simplify(kap+4*eps*rho**2/(s*(1+z0*s)))==0
            assert S.simplify(finite-(1+z0*s)/(1+(z0+eps)*s))==0
            assert S.simplify((finite-1)/(kap*finite)-s**2/(4*rho**2))==0
            one_main_cases.append({'pattern':'200','orientation':eps,'prefix_lift':lift})
            # 002: Q0=upper, Q1=A Q0, Q2=B A Q0.
            l0=prefix_trace(upper)
            l1=prefix_trace(puncture*upper)
            outer=other*puncture*upper
            finite=S.simplify(-l0/l1)
            kap=S.simplify(-l1/leading_quadratic(outer))
            assert S.simplify(kap-s*(1+(z0+eps)*s)/(4*eps*rho**2))==0
            assert S.simplify(finite-(1+z0*s)/(1+(z0+eps)*s))==0
            assert S.simplify(kap*(1-finite)-s**2/(4*rho**2))==0
            one_main_cases.append({'pattern':'002','orientation':eps,'prefix_lift':lift})
    result={'status':'PASS','fixture':'actual ideal right-angled cuboctahedron; cube matching in x; marked main edge in z',
            'exact_supporting_inequalities':supporting,'exact_right_angles':orthogonal,
            'actual_signed_prefix_matrices':prefix_checks,'ordered_actual_disk_triples':len(cases),
            'half_index_identities':2,'one_main_signed_Bessel_cases':len(one_main_cases),
            'patterns':sorted(set(c['pattern'] for c in cases)),
            'cases':cases,'one_main_cases':one_main_cases,
            'scope':'Source-lift geometry, signs and both primitive Bessel calibrations; no global period.'}
    target=args.output or Path(__file__).with_name('actual_right_angled_resonant_prefix_signs_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('cases','one_main_cases')},indent=2))


if __name__=='__main__':
    main()
