#!/usr/bin/env python3
"""Actual marked circle fixtures, full Jacobian, source angles and line flags.

The audit does not identify the auxiliary primitive collar word.
"""
import argparse
import cmath
import itertools
import json
from pathlib import Path
import numpy as np
import sympy as sp


def symbolic():
    x,b,y,s=sp.symbols('x b y s',positive=True)
    c=sp.sqrt(1-s*s);T=sp.sqrt(b*(x+y)+x*y+b*b*s*s);D=(x+y)**2-4*x*y*s*s
    E=x+y+2*b*s*s+2*s*T
    co=(x*(y-x)+b*(y+x*(1-2*s*s)))/((x+b)*sp.sqrt(D));si=2*x*c*T/((x+b)*sp.sqrt(D))
    checks=[co*co+si*si-1,
            c*(co*sp.diff(si,s)-si*sp.diff(co,s))/2+x*(sp.diff(E,x)/E-sp.diff(D,x)/(2*D)),
            -b*s/T+b*sp.diff(E,b)/E]
    X,r,C,S=sp.symbols('X r C S',real=True);H=r*(1+C)
    for upper in (True,False):
        cy=r if upper else H-r;cp=X+sp.I*cy;cm=X-sp.I*cy
        P=(sp.I/r)*sp.Matrix([[cm+2*sp.I*H,r*r-cp*cm-2*sp.I*H*cp],[1,-cp]]) if upper else (-sp.I/r)*sp.Matrix([[cm,r*r-cp*cm],[1,-cp]])
        point=X+(r*S if upper else -r*S)+(sp.I*H if upper else 0)
        vec=sp.Matrix([point,1]);lam=-C+sp.I*S
        checks.extend([P.det()-1,sp.trace(P)+2*C])
        checks.extend(list(P*vec-lam*vec))
        checks.extend(list(P.inv()*vec-(-C-sp.I*S)*vec))
    for value in checks:
        val=sp.cancel(value)
        if val.has(S):
            num,den=sp.fraction(val);num=sp.rem(sp.Poly(num,S),sp.Poly(S*S-(1-C*C),S)).as_expr();val=num/den
        assert sp.simplify(val)==0,val
    return {'exact_gradient_and_ordered_line_identities':len(checks)}


def fixtures():
    # Tetrahedral white graph = original ideal-octahedral checkerboard fixture.
    yield {'name':'actual_tetrahedral_white_sphere','triangles':[(0,1,2),(0,1,3),(0,2,3),(1,2,3)],
           'lower':0,'upper':1,'circles':{2:(0.,.5,.5),3:(1.,.5,.5)},'matching':[(0,2),(1,3)],'fixed':2}
    # Octahedral white graph = original ideal-cuboctahedral checkerboard fixture.
    rt=np.sqrt(2.)
    yield {'name':'actual_octahedral_white_sphere','triangles':[(p,j,(j+1)%4) for p in (4,5) for j in range(4)],
           'lower':0,'upper':4,'circles':{1:(0.,.5,.5),2:(rt/2,.75,.25),3:(rt,.5,.5),5:(rt/2,.25,.25)},
           'matching':[(0,1),(1,2),(2,3),(0,3)],'fixed':1}


def run_fixture(fx):
    tri=fx['triangles'];lower,upper=fx['lower'],fx['upper'];circles=fx['circles'];finite=sorted(circles)
    edges=sorted({tuple(sorted((t[i],t[j]))) for t in tri for i,j in ((0,1),(0,2),(1,2))})
    matching=[tuple(sorted(e)) for e in fx['matching']];assert all(sum(set(e).issubset(t) for e in matching)==1 for t in tri)
    marked=tuple(sorted((lower,upper)));assert marked not in matching
    edges.remove(marked)
    keys=[(f,k) for f in finite for k in range(3) if (f,k)!=(fx['fixed'],0)]
    assert len(keys)==len(edges)==3*len(finite)-1
    complete=np.array([circles[f][k] for f,k in keys],complex)
    def unpack(z):
        ans={f:list(map(complex,circles[f])) for f in finite}
        for key,value in zip(keys,z):ans[key[0]][key[1]]=value
        return ans
    def system(z,delta):
        obj=unpack(z);F=[];J=[]
        for e in edges:
            I=cmath.cos(2*np.pi*delta[matching.index(e)]) if e in matching else 1
            row={k:0j for k in keys};f,g=e
            if f in (lower,upper) or g in (lower,upper):
                line=f if f in (lower,upper) else g;v=g if line==f else f
                X,Y,r=obj[v];sgn=1 if line==lower else -1
                value=Y-r*I if line==lower else 1-Y-r*I
                row[(v,1)]=sgn;row[(v,2)]=-I
            else:
                X,Y,r=obj[f];Z,W,t=obj[g];dx=X-Z;dy=Y-W
                value=dx*dx+dy*dy-r*r-t*t-2*I*r*t
                for key,val in [((f,0),2*dx),((g,0),-2*dx),((f,1),2*dy),((g,1),-2*dy),((f,2),-2*r-2*I*t),((g,2),-2*t-2*I*r)]:
                    if key in row:row[key]=val
            F.append(value);J.append([row[k] for k in keys])
        return np.array(F),np.array(J)
    zero=np.zeros(len(matching));F,J=system(complete,zero);assert np.max(abs(F))<1e-13
    singular=np.linalg.svd(J,compute_uv=False);assert min(singular)>.05
    cases=[];max_balance=max_residual=max_eigen=0.;angle_count=branch_count=width_count=0
    for index in range(1,13):
        delta=np.array([(.001*index*(j+1)/len(matching))*(1 if index%2 else 1+.35j) for j in range(len(matching))])
        z=complete.copy()
        for _ in range(12):
            F,J=system(z,delta)
            if max(abs(F))<1e-13:break
            z-=np.linalg.solve(J,F)
        F,J=system(z,delta);res=max(abs(F));assert res<1e-12
        max_residual=max(max_residual,res);obj=unpack(z);l={f:1/obj[f][2] for f in finite};l[lower]=l[upper]=0
        face_sum={f:0j for f in finite}
        for row in tri:
            edge=next(e for e in matching if set(e).issubset(row));x,y=edge;b=next(f for f in row if f not in edge)
            de=delta[matching.index(edge)];xx,bb,yy=l[x],l[b],l[y]
            if sum(abs(v)>1e-12 for v in (xx,bb,yy))==1:
                angles={f:(np.pi if abs(l[f])>1e-12 else 0j) for f in row}
            else:
                ss=cmath.sin(np.pi*de);cc=cmath.cos(np.pi*de);T=cmath.sqrt(bb*(xx+yy)+xx*yy+bb*bb*ss*ss);D=(xx+yy)**2-4*xx*yy*ss*ss
                thb=2*cmath.atan(bb*cc/T) if abs(bb)>1e-12 else 0j
                if abs(xx)<1e-12:thx=0j
                elif abs(yy)<1e-12:thx=np.pi-thb
                else:
                    co=(xx*(yy-xx)+bb*(yy+xx*cmath.cos(2*np.pi*de)))/((xx+bb)*cmath.sqrt(D))
                    thx=cmath.acos(co)
                angles={x:thx,b:thb,y:np.pi-thx-thb}
            for f,a in angles.items():
                if f in face_sum:face_sum[f]+=a
            angle_count+=1
        error=max(abs(v-2*np.pi) for v in face_sum.values());assert error<1e-10
        max_balance=max(max_balance,error)
        for row in tri:
            if lower in row and upper in row:
                v=next(f for f in row if f in finite);edge=next(e for e in matching if set(e).issubset(row));de=delta[matching.index(edge)]
                assert abs(l[v]-2*cmath.cos(np.pi*de)**2)<1e-11;width_count+=1
        def reflection(face,plus=True):
            sign=1 if plus else -1
            if face==lower:return (-sign*1j)*np.eye(2)
            if face==upper:return (sign*1j)*np.array([[1,sign*2j],[0,1]],complex)
            X,Y,r=obj[face];cp=X+sign*1j*Y;cm=X-sign*1j*Y
            return np.array([[cp,r*r-cp*cm],[1,-cm]],complex)/r
        for e in edges:
            P=reflection(e[1],True)@reflection(e[0],False)
            de=delta[matching.index(e)] if e in matching else 0
            assert abs(np.linalg.det(P)-1)<1e-11
            assert abs(np.trace(P)+2*cmath.cos(2*np.pi*de))<1e-11
            if e in matching:
                for direction in (-1,1):
                    lam=-cmath.exp(direction*2j*np.pi*de)
                    vec=np.array([P[0,1],lam-P[0,0]]) if abs(P[0,1])>abs(P[1,0]) else np.array([lam-P[1,1],P[1,0]])
                    err=np.linalg.norm(P@vec-lam*vec)/np.linalg.norm(vec);assert err<1e-11
                    max_eigen=max(max_eigen,err);branch_count+=1
        cases.append({'maximum_delta':float(max(abs(delta))),'complex_parameters':bool(index%2==0),'source_angle_balance_error':float(error)})
    return {'fixture':fx['name'],'Jacobian_dimension':len(keys),'complete_minimum_singular_value':float(min(singular)),
            'deformed_patterns':len(cases),'actual_triangle_angle_checks':angle_count,'selected_matching_eigenlines':branch_count,'shared_strip_width_checks':width_count,
            'maximum_equation_residual':float(max_residual),'maximum_source_angle_balance_error':float(max_balance),'maximum_eigenline_error':float(max_eigen),'samples':cases}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='experiments/actual_marked_deformed_circle_pattern_results.json');args=ap.parse_args()
    data={'status':'PASS','symbolic':symbolic(),'actual_marked_fixtures':[run_fixture(f) for f in fixtures()],
          'scope':'Exact local gradient/line identities and the full finite line-circle Jacobian on original octahedral/cuboctahedral checkerboard fixtures, real and complex deformations, actual source face forces, shared strips and ordered matching eigenlines. No auxiliary primitive collar, regulator or full mixed-source assertion.'}
    Path(args.output).write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))
if __name__=='__main__':main()
