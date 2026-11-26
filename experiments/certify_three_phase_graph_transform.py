#!/usr/bin/env python3
"""Outward analytic phase-class certificate, not a full-source contour test.

The retained Hessian uses a finite Taylor polynomial with a proved Cauchy
tail. The prepared seed uses parameter-dependent analytic Newton balls.
Numerical root solving chooses rational centers only.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import time

import mpmath as mp
from flint import arb, acb, ctx


ORDER = 8


def rat(v):
    v = Q(v)
    return arb(v.numerator)/v.denominator


class Series:
    """Total-degree truncated bivariate series with outward coefficients."""
    def __init__(self, value=0):
        self.c = dict(value) if isinstance(value, dict) else {(0,0):acb(value)}

    def __add__(self, other):
        other = other if isinstance(other,Series) else Series(other)
        out = dict(self.c)
        for key,value in other.c.items():
            out[key] = out.get(key,acb(0))+value
        return Series(out)
    __radd__ = __add__

    def __neg__(self): return Series({k:-v for k,v in self.c.items()})
    def __sub__(self, other): return self + (-other if isinstance(other,Series) else -acb(other))
    def __rsub__(self, other): return Series(other)+(-self)

    def __mul__(self, other):
        other = other if isinstance(other,Series) else Series(other)
        out = {}
        for (a,b),v in self.c.items():
            for (c,d),w in other.c.items():
                if a+b+c+d <= ORDER:
                    key = a+c,b+d
                    out[key] = out.get(key,acb(0))+v*w
        return Series(out)
    __rmul__ = __mul__

    def inverse(self):
        constant = self.c[(0,0)]
        q = 1-self/constant
        q.c[(0,0)] = acb(0)
        total,term = Series(1),Series(1)
        for _ in range(ORDER):
            term = term*q
            total = total+term
        return total/constant

    def __truediv__(self, other):
        return self*(other.inverse() if isinstance(other,Series) else 1/acb(other))
    def __rtruediv__(self, other): return Series(other)*self.inverse()
    def __pow__(self, exponent):
        assert exponent >= 0
        value = Series(1)
        for _ in range(exponent): value = value*self
        return value


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision",type=int,default=192)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    ctx.prec=args.precision
    mp.mp.dps=50
    pi,ii=arb.pi(),acb(0,1)
    xh=acb(arb(1)/6,arb(2).log()/(2*pi))
    k0=4*pi/21*(2*arb(3).sqrt()-3*ii)
    rho=(5-arb(21).sqrt())/2
    checks=[]

    def positive(name,value):
        assert value>0,(name,str(value))
        checks.append({"name":name,"margin":str(value)})

    # Coarse bounds on the larger analytic polydisk radius 1/50.
    rr=Q(22,175)
    exp_upper=1+rr+rr**2/(2*(1-rr/3))
    positive("exp(pi/25)<23/20",rat(Q(23,20)-exp_upper))
    positive("sqrt(7)>13/5",rat(7-Q(13,5)**2))
    positive("sqrt(7-39/25)>23/10",rat(7-Q(39,25)-Q(23,10)**2))
    positive("critical U displacement below23/50",rat(Q(23,50)-Q(3,10)-Q(39,245)))
    uder=Q(429,35)
    xx_bound=(uder/Q(27,50)+(Q(44,7)*Q(1679,2000)+Q(23,40)*uder)/Q(321,2000)
              +Q(44,7)*Q(23,17))/Q(12,5)+5
    xy_bound=uder/(Q(27,50)*Q(321,2000))/Q(12,5)+2
    positive("larger-polydisk diagonal remainder below64",rat(64-xx_bound))
    positive("larger-polydisk mixed remainder below64",rat(64-xy_bound))

    def expaxis(axis):
        return Series({(j,0) if axis==0 else (0,j):
                       (2*pi*ii)**j/math.factorial(j) for j in range(ORDER+1)})
    X0=acb(arb(1)/4,arb(3).sqrt()/4)
    X,Y=X0*expaxis(0),X0*expaxis(1)
    a,b=1/X-1,1/Y-1
    a.c[(0,0)]=b.c[(0,0)]=-ii*arb(3).sqrt()
    delta=1-2*(a+b)+(a-b)**2
    delta0=acb(1,4*arb(3).sqrt())
    e=delta/delta0-1
    e.c[(0,0)]=acb(0)
    root,term,coefficient=Series(1),Series(1),Q(1)
    for j in range(1,ORDER+1):
        term=term*e
        coefficient=coefficient*(Q(1,2)-(j-1))/j
        root=root+rat(coefficient)*term
    root=root*acb(2,arb(3).sqrt())
    U,V=(1+a-b-root)/2,(1-a+b-root)/2
    ax,by=-2*pi*ii/X,-2*pi*ii/Y
    Ux,Uy,Vy=ax*(1-U)/root,by*U/root,by*(1-V)/root
    pxx=-Ux/U-(2*pi*ii*X*U+X*Ux)/(1-X*U)+2*pi*ii*X/(1-X)
    pxy=-Uy/U-X*Uy/(1-X*U)
    pyy=-Vy/V-(2*pi*ii*Y*V+Y*Vy)/(1-Y*V)+2*pi*ii*Y/(1-Y)
    q=arb(1)/4
    tail=64*q**(ORDER+1)*((ORDER+2)-(ORDER+1)*q)/(1-q)**2
    kernel=[]
    for name,series in (("xx",pxx/k0+5),("xy",pxy/k0-2),("yy",pyy/k0+5)):
        polynomial=sum(abs(value)*rat(Q(1,200))**sum(key) for key,value in series.c.items())
        bound=polynomial+tail
        positive("kernel "+name+" remainder below1/10",arb(1)/10-bound)
        kernel.append({"entry":name,"polynomial_bound":str(polynomial),"tail":str(tail),
                       "total_bound":str(bound),
                       "coefficients":{f"{i},{j}":str(v) for (i,j),v in sorted(series.c.items())}})

    def retained(x,y):
        X,Y=(2*pi*ii*x).exp(),(2*pi*ii*y).exp()
        a,b=1/X-1,1/Y-1
        r=(1-2*(a+b)+(a-b)**2).sqrt()
        U,V=(1+a-b-r)/2,(1-a+b-r)/2
        ax,by=-2*pi*ii/X,-2*pi*ii/Y
        Ux,Uy,Vy=ax*(1-U)/r,by*U/r,by*(1-V)/r
        px=-U.log()+(1-X*U).log()-(1-X).log()-pi*ii
        py=-V.log()+(1-Y*V).log()-(1-Y).log()-pi*ii
        pxx=-Ux/U-(2*pi*ii*X*U+X*Ux)/(1-X*U)+2*pi*ii*X/(1-X)
        pxy=-Uy/U-X*Uy/(1-X*U)
        pyy=-Vy/V-(2*pi*ii*Y*V+Y*Vy)/(1-Y*V)+2*pi*ii*Y/(1-Y)
        return dict(X=X,Y=Y,U=U,V=V,px=px,py=py,pxx=pxx,pxy=pxy,pyy=pyy)

    def system(x,t,y):
        d=retained(x,y)
        q,z,sec=1/(pi*x).tan(),(t/2).tan(),1/(t/2).cos()
        period=3*t+2*ii*(z+sec).log()+ii*((q+z).log()-(q-z).log())-2*pi
        ft=3+ii*(sec+q*sec**2/(q-z)/(q+z))
        fx=2*pi*ii*z*(1+q*q)/(q-z)/(q+z)
        tp,tm=(pi*x+t/2).tan(),(pi*x-t/2).tan()
        bx=(pi*x+t/2).cos().log()+(pi*x-t/2).cos().log()-2*(pi*x).sin().log()
        bxx,bxt=-pi*(tp+tm+2*q),(tm-tp)/2
        return [period,bx+d['px']],[[fx,ft],[bxx+d['pxx'],bxt]],d,(bxx,bxt,ii*ft/(2*pi))

    def point(a,b):return acb(rat(a),rat(b))
    C=[[point('-.012459042950055255651267420891','.009121085447815058535390706888'),
        point('-.030322991884195644218839259185','-.022730223128523958826095306578')],
       [point('.222750256842225811720371833986','-.117735701411284707218221686158'),
        point('.057309470071241114644219436946','.078282475605306592775433429801')]]
    initial=[point('.177337918569469382175948562048','.101358689576302370861575311618'),
             point('1.533800710765884206016520588964','-.978955098405739999074096803416')]
    initial_boxes=[acb(z.real+arb(0,'1e-8'),z.imag+arb(0,'1e-8')) for z in initial]
    d0=retained(initial_boxes[0],xh)
    positive("actual prepared centered gradient below7/250",rat(Q(7,250))-abs(d0['py']/k0))

    def mp_system(x,t,y):
        X,Y=mp.exp(2j*mp.pi*x),mp.exp(2j*mp.pi*y)
        a,b=1/X-1,1/Y-1
        U=(1+a-b-mp.sqrt(1-2*(a+b)+(a-b)**2))/2
        px=-mp.log(U)+mp.log(1-X*U)-mp.log(1-X)-1j*mp.pi
        q,z,sec=1/mp.tan(mp.pi*x),mp.tan(t/2),1/mp.cos(t/2)
        per=3*t+2j*mp.log(z+sec)+1j*(mp.log(q+z)-mp.log(q-z))-2*mp.pi
        bx=mp.log(mp.cos(mp.pi*x+t/2))+mp.log(mp.cos(mp.pi*x-t/2))-2*mp.log(mp.sin(mp.pi*x))
        return per,bx+px

    def rectangle(a,b):return rat((a+b)/2)+arb(0,rat((b-a)/2))
    def mpq(q):return mp.mpf(q.numerator)/q.denominator
    def rational_center(z):return [str(Q(str(z.real))),str(Q(str(z.imag)))]
    def in_joint_box(x,t,d):
        margins=[x.real-rat('.14'),rat('.20')-x.real,x.imag-rat('.09'),rat('.12')-x.imag,
                 t.real,rat('1.8')-t.real,-t.imag-rat('.97'),1+t.imag]
        for z in (d['U'],d['V']):
            margins.extend((-z.real,-z.imag))
            index=ii*z.log()/(2*pi)
            margins.extend((index.real-rat('.25'),rat('.45')-index.real,
                            rat('.02')-abs(index.imag)))
        q,z,sec=1/(pi*x).tan(),(t/2).tan(),1/(t/2).cos()
        for arg in (q+z,q-z,z+sec,(pi*x+t/2).cos(),(pi*x-t/2).cos(),(pi*x).sin()):
            margins.append(arg.real)
        return margins

    cells=[]
    mesh=64
    width=Q(1,100*mesh)
    start=time.time()
    for i in range(mesh):
        for j in range(mesh):
            a=Q(-1,200)+i*width;b=a+width
            c=Q(-1,200)+j*width;d=c+width
            yc=xh+acb(rat((a+b)/2),rat((c+d)/2))
            ybox=xh+acb(rectangle(a,b),rectangle(c,d))
            ymp=mp.mpf(1)/6+1j*mp.log(2)/(2*mp.pi)+mpq((a+b)/2)+1j*mpq((c+d)/2)
            xm,tm=mp.findroot(lambda x,t:mp_system(x,t,ymp),(.1773+.1013j,1.534-.979j))
            strings=[rational_center(xm),rational_center(tm)]
            centers=[point(*v) for v in strings]
            pr=rat(width)/arb(2).sqrt()
            radii=[pr*arb(7)/20,pr]
            residual=system(*centers,yc)[0]
            variation=abs(retained(centers[0],ybox)['pxy'])*pr
            boxes=[acb(z.real+arb(0,r),z.imag+arb(0,r)) for z,r in zip(centers,radii)]
            _,J,data,(bxx,bxt,ftt)=system(*boxes,ybox)
            contractions=[];self_margins=[]
            for row in range(2):
                contraction=sum(abs(acb(int(row==col))-sum(C[row][k]*J[k][col] for k in range(2)))*radii[col]
                                for col in range(2))/radii[row]
                displacement=abs(sum(C[row][k]*residual[k] for k in range(2)))+abs(C[row][1])*variation
                assert contraction<arb(1)/10
                margin=radii[row]-displacement-contraction*radii[row]
                assert margin>0
                contractions.append(str(contraction));self_margins.append(str(margin))
            joint_margins=in_joint_box(*boxes,data)
            assert all(v>0 for v in joint_margins),(i,j,list(map(str,joint_margins)))
            outgoing=data['pyy']-data['pxy']**2/(bxx-bxt*bxt/ftt+data['pxx'])
            defect=abs(outgoing/k0+arb(21).sqrt())
            assert defect<arb(1)/2,(i,j,str(defect))
            cells.append({"cell":[i,j],"output_box":[[str(a),str(b)],[str(c),str(d)]],
                          "centers":strings,"radii":list(map(str,radii)),
                          "Newton_contractions":contractions,"self_map_margins":self_margins,
                          "joint_domain_margins":list(map(str,joint_margins)),
                          "coordinate_enclosures":[str(boxes[0]),str(boxes[1]),
                                                   str(ii*data['U'].log()/(2*pi)),str(ii*data['V'].log()/(2*pi))],
                          "seed_derivative_defect":str(defect)})
        if i%16==0:print(f"seed row {i}/{mesh}; {len(cells)} cells",flush=True)
    assert {(i,j) for i,j in (v['cell'] for v in cells)} == {(i,j) for i in range(mesh) for j in range(mesh)}

    # Exact analytic graph-transform margins (constants rounded only after
    # the outward inequalities have been proved).
    radius=rat(Q(1,200));B=arb(1)/2;eps=arb(1)/10;H=rat(Q(3,100));aa=rho/2
    contraction=aa*(B+eps)
    response=rho*(1+eps/2)/(1-contraction)
    outgoing=(rho*(B+eps)+eps)*response+rho*eps+eps
    positive("self-map radius reserve",radius-rho*radius-aa*(H+(B+2*eps)*radius))
    positive("implicit contraction below63/1000",rat(Q(63,1000))-contraction)
    positive("wire response and gradient contraction below47/200",rat(Q(47,200))-response)
    positive("outgoing derivative defect below9/50",rat(Q(9,50))-outgoing)
    positive("cap real Hessian above8",(arb(21).sqrt()*k0.real-abs(k0)*B)-8)
    positive("wire total real Hessian above18",((5+arb(21).sqrt())*k0.real-abs(k0)*(B+eps))-18)
    positive("seed Hessian modulus below14",14-abs(k0)*(arb(21).sqrt()+B))
    positive("seed disk action above19107/10000",rat(Q(19113,10000))-rat(Q(2,25))*radius-7*radius**2-rat(Q(19107,10000)))
    root=Path(__file__).resolve().parents[1]
    dependencies=[Path(__file__).resolve(),root/'notes/research_three_cap_first_attachment.md',
                  root/'repro/results/research-three-cap-first-attachment.json',
                  root/'notes/research_three_vertex_local_composition.md',
                  root/'notes/research_three_vertex_joint_concavity.md',
                  root/'notes/research_three_cap_central_source.md',
                  root/'notes/research_three_vertex_bidisk_packet.md']
    proof=root/'notes/research_three_phase_graph_transform.md'
    if proof.exists():dependencies.append(proof)
    result={"status":"passed","precision_bits":ctx.prec,"scope":"Analytic phase class and actual prepared critical branch. No uniform seed source packet, complementary source bound, or full-chain coefficient is inferred.",
            "kernel_Taylor_order":ORDER,"larger_analytic_radius":"1/50","class_disk_radius":"1/200",
            "kernel_bounds":kernel,"seed_mesh":mesh,"seed_cells":cells,"seed_cell_count":len(cells),
            "exact_square_cover":True,"preconditioner":[[str(z) for z in row] for row in C],
            "graph_contraction":str(contraction),"wire_response":str(response),
            "outgoing_derivative_bound":str(outgoing),"scalar_checks":checks,
            "elapsed_seconds":time.time()-start,
            "sha256":{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies}}
    output=args.output or root/'repro/results/research-three-phase-graph-transform.json'
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(f"Passed3 Taylor bounds, {len(cells)} seed cells, {len(checks)} scalar comparisons. {output}",flush=True)


if __name__=='__main__':main()
