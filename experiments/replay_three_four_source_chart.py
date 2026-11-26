#!/usr/bin/env python3
"""Independent directed chart replay using the unsummed index Hessian.

No author module or numerical root solver is imported. The parameter cover,
complex Newton disks, root branches, condensed source Hessian, and all56
current planes are recomputed. Current values use the independent reflected
cap and negative-frequency retained primitives.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import time
from flint import arb,acb,ctx
import sympy as sp
from replay_three_prepared_central_currents import value_gradient
ROOT=Path(__file__).resolve().parents[1]

def rat(q):
    q=Q(q);return arb(q.numerator)/q.denominator

def point(parts):return acb(rat(parts[0]),rat(parts[1]))
def interval(a,b):return arb(rat((a+b)/2),rat((b-a)/2))

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision',type=int,default=256)
    ap.add_argument('--artifact',type=Path,default=ROOT/'repro/results/research-three-four-source-chart.json')
    ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-three-four-source-chart-replay.json')
    args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic()
    data=json.loads(args.artifact.read_text());assert data['status']=='passed'
    pi,ii=arb.pi(),acb(0,1);twopi=2*pi*ii
    xh=acb(arb(1)/6,arb(2).log()/(2*pi));k0=4*pi/21*(2*arb(3).sqrt()-3*ii)
    def retained(x,y):
        X,Y=(twopi*x).exp(),(twopi*y).exp();alpha,beta=1/X-1,1/Y-1
        delta=(alpha-beta)**2-2*(alpha+beta)+1
        root=delta.sqrt();U=(1+alpha-beta-root)/2;V=(1-alpha+beta-root)/2
        s,t=ii*U.log()/(2*pi),ii*V.log()/(2*pi)
        av,bv,cv=U*V/(1-U*V),X*U/(1-X*U),Y*V/(1-Y*V)
        # Simplify the unsummed Schur complement at the exact stationary
        # identities before interval evaluation. Checked symbolically below.
        rr=1-U-V
        pxx=twopi*(1-U)/(1-X*U)*(1/(X*U*rr)+X/(1-X))
        pxy=twopi/(X*Y*rr*(1-U*V))
        pyy=twopi*(1-V)/(1-Y*V)*(1/(Y*V*rr)+Y/(1-Y))
        px=twopi*s+(1-X*U).log()-(1-X).log()-pi*ii
        return dict(X=X,Y=Y,U=U,V=V,s=s,t=t,delta=delta,px=px,pxx=pxx,pxy=pxy,pyy=pyy)
    def system(x,tau,y):
        d=retained(x,y);q=1/(pi*x).tan();z=(tau/2).tan();sec=1/(tau/2).cos()
        period=3*tau+2*ii*(z.asinh()+(z/q).atanh())-2*pi
        ft=3+ii*(sec+q*sec**2/(q*q-z*z));fx=2*pi*ii*z*(1+q*q)/(q*q-z*z)
        cp,cm=(pi*x+tau/2).cos(),(pi*x-tau/2).cos()
        bx=cp.log()+cm.log()-2*(pi*x).sin().log()
        tp,tm=(pi*x+tau/2).tan(),(pi*x-tau/2).tan()
        bxx=-pi*(tp+tm+2*q);bxt=(tm-tp)/2;ftt=ii*ft/(2*pi)
        return [period,bx+d['px']],[[fx,ft],[bxx+d['pxx'],bxt]],d,(bxx,bxt,ftt)
    C=[[point(['-.012459042950055255651267420891','.009121085447815058535390706888']),
        point(['-.030322991884195644218839259185','-.022730223128523958826095306578'])],
       [point(['.222750256842225811720371833986','-.117735701411284707218221686158']),
        point(['.057309470071241114644219436946','.078282475605306592775433429801'])]]
    seen=set();critical=[];width=Q(1,8000);pr=rat(width)/arb(2).sqrt();radii=[7*pr/20,pr]
    for cell in data['critical_cells']:
        i,j=cell['cell'];assert 0<=i<104 and 0<=j<33 and(i,j)not in seen;seen.add((i,j))
        a,b=Q(-3,500)+i*width,Q(-3,500)+(i+1)*width
        c,d=Q(-33,8000)+j*width,Q(-33,8000)+(j+1)*width
        assert [[Q(z)for z in row]for row in cell['output_box']]==[[a,b],[c,d]]
        yc=xh+acb(rat((a+b)/2),rat((c+d)/2));yb=xh+acb(interval(a,b),interval(c,d))
        centers=[point(z)for z in cell['centers']]
        boxes=[acb(arb(z.real,r),arb(z.imag,r))for z,r in zip(centers,radii)]
        residual=system(*centers,yc)[0];variation=abs(retained(centers[0],yb)['pxy'])*pr
        _,J,dd,(bxx,bxt,ftt)=system(*boxes,yb)
        cons=[];margins=[]
        for row in range(2):
            con=sum(abs(acb(int(row==col))-sum(C[row][k]*J[k][col]for k in range(2)))*radii[col]for col in range(2))/radii[row]
            disp=abs(sum(C[row][k]*residual[k]for k in range(2)))+abs(C[row][1])*variation
            margin=radii[row]-disp-con*radii[row]
            assert con<arb(1)/4 and margin>0,(i,j,row,con,margin)
            cons.append(str(con));margins.append(str(margin))
        x,tau=boxes;s,t=dd['s'],dd['t']
        assert x.real>rat('.176')and x.real<rat('.179')and x.imag>rat('.09')and x.imag<rat('.12')
        assert tau.real>rat('1.5')and tau.real<rat('1.55')and tau.imag>-1 and tau.imag<-rat('.97')
        assert all(z.real>rat('.31')and z.real<rat('.39')for z in(s,t))
        assert s.imag>-rat('.008')and s.imag<rat('.008')and t.imag>-rat('.017')and t.imag<rat('.012')
        assert dd['delta'].imag>0
        assert all(z.real<0 and z.imag<0 for z in(dd['U'],dd['V']))
        assert abs(dd['X']*dd['U'])<1 and abs(dd['Y']*dd['V'])<1
        assert s.real+t.real>rat('.5')and s.real+t.real<1
        q=1/(pi*x).tan();z=(tau/2).tan();sec=1/(tau/2).cos()
        assert all(v.real>0 for v in[q+z,q-z,z+sec,(pi*x+tau/2).cos(),(pi*x-tau/2).cos(),(pi*x).sin()])
        outgoing=dd['pyy']-dd['pxy']**2/(bxx-bxt*bxt/ftt+dd['pxx'])
        defect=abs(outgoing/k0+arb(21).sqrt())
        assert defect<arb(1)/2,(i,j,defect)
        critical.append({'cell':[i,j],'contractions':cons,'self_map_margins':margins,'hessian_defect':str(defect)})
        if len(seen)%500==0:print('independent critical cells',len(seen),flush=True)
    assert len(seen)==3432 and seen==set(product(range(104),range(33)))
    B=[(Q(7,50),Q(1,5)),(Q(0),Q(9,5)),(Q(1,4),Q(9,20)),(Q(1,4),Q(9,20)),(Q(1,6)-Q(3,500),Q(1,6)+Q(7,1000))]
    H=[Q(10135869,10**8),-Q(97895510,10**8),Q(300831,10**8),-Q(629803,10**8)]
    def expected():
        for axis,end,hs,ht,hy in product((2,3),(0,1),(-Q(1,125),Q(1,125)),(-Q(17,1000),Q(3,250)),(-Q(33,8000),Q(0))):
            b=B[:];b[axis]=(b[axis][end],)*2;h=H[:];h[2]=hs;h[3]=ht
            yield('index_side',axis,end,str(hs),str(ht),str(hy)),b,h+[hy],Q(19107,10000)
        for hs,ht,hy in product((-Q(1,125),Q(1,125)),(-Q(17,1000),Q(3,250)),(-Q(33,8000),Q(0))):
            h=H[:];h[2]=hs;h[3]=ht
            yield('alias',str(hs),str(ht),str(hy)),B,h+[hy],Q(39,20)
        for axis,end,hy in product(range(4),(0,1),(-Q(33,8000),Q(0))):
            b=B[:];b[axis]=(b[axis][end],)*2
            yield('translation_face',axis,end,str(hy)),b,H+[hy],Q(19107,10000)
    wanted={key:(b,h,target)for key,b,h,target in expected()};seen_planes=set();bounds=[]
    for plane in data['support_planes']:
        key=tuple(plane['domain']);assert key in wanted and key not in seen_planes;seen_planes.add(key)
        b,h,target=wanted[key]
        assert [[Q(v)for v in row]for row in plane['bounds']]==[list(z)for z in b]
        assert list(map(Q,plane['heights']))==h and Q(plane['threshold'])==target
        z=list(map(Q,plane['support_point']));assert all(a<=v<=c for v,(a,c)in zip(z,b))
        val,g=value_gradient(z,h)
        upper=val+sum(max((gg*rat(a-v)).upper(),(gg*rat(c-v)).upper())for gg,v,(a,c)in zip(g,z,b))
        assert upper<rat(target),(key,upper,target)
        bounds.append(str(upper))
    assert len(seen_planes)==56 and seen_planes==set(wanted)
    scalar=[rat('1.9107')-rat('1.95')+2*pi/125,
            rat(Q(27,40))*rat(Q(21,1000))**2-rat(Q(1,4000)),
            rat(Q(3,8))*rat(Q(3,50))**2-rat(Q(1,4000)),
            rat(Q(7,880))*rat(Q(1,4))**2-rat(Q(1,4000))]
    assert all(v>0 for v in scalar)
    uu,vv=sp.symbols('U V');xx=1/(1+uu-uu*vv);yy=1/(1+vv-uu*vv)
    av=uu*vv/(1-uu*vv);bv=xx*uu/(1-xx*uu);cv=yy*vv/(1-yy*vv)
    det=bv*cv-av*(bv+cv)
    identities=[det-uu*vv*(1-uu-vv)/(1-uu*vv)**2,
        xx/(1-xx)-bv-(av-cv)/((1-xx*uu)**2*det)
        -(1-uu)/(1-xx*uu)*(1/(xx*uu*(1-uu-vv))+xx/(1-xx)),
        av/((1-xx*uu)*(1-yy*vv)*det)-1/(xx*yy*(1-uu-vv)*(1-uu*vv)),
        yy/(1-yy)-cv-(av-bv)/((1-yy*vv)**2*det)
        -(1-vv)/(1-yy*vv)*(1/(yy*vv*(1-uu-vv))+yy/(1-yy))]
    assert all(sp.cancel(z)==0 for z in identities)
    assert data['script_sha256']==sha256((ROOT/'experiments/certify_three_four_source_chart.py').read_bytes()).hexdigest()
    for p,h in data['dependencies_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    imports=['experiments/replay_three_prepared_central_currents.py','experiments/replay_three_cap_wire_complement.py','experiments/replay_three_vertex_directed_packet.py']
    result={'status':'passed','precision_bits':args.precision,'critical_cells':critical,'critical_cell_count':len(critical),
            'support_plane_count':len(bounds),'support_upper_bounds':bounds,'scalar_margins':list(map(str,scalar)),
            'exact_rational_cover':True,'method':'Original asinh/atanh periods and unsummed index-Hessian Schur complement; independent negative-frequency current primitives. No author module imported.',
            'exact_stationary_Schur_identities':len(identities),
            'elapsed_seconds':time.monotonic()-start,'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'artifact_sha256':sha256(args.artifact.read_bytes()).hexdigest(),
            'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest()for p in imports}|data['dependencies_sha256']}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',len(critical),'critical cells,',len(bounds),'planes,',len(scalar),'scalars',flush=True)

if __name__=='__main__':main()
