#!/usr/bin/env python3
"""Independent replay of the first-entrance real-output critical certificate.

No author module, numerical root solver, or finite-difference derivative
is used. Retained second derivatives are obtained by eliminating the
original two index Hessian; cap derivatives use the cosine/asinh phase.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import argparse,json,time
import sympy as sp

from flint import arb,acb,ctx

ROOT=Path(__file__).resolve().parents[1]


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision',type=int,default=256)
    ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-three-first-entrance-real-critical-replay.json')
    args=ap.parse_args();ctx.prec=args.precision;start=time.monotonic()
    path=ROOT/'repro/results/research-three-first-entrance-real-critical.json'
    data=json.loads(path.read_text());assert data['status']=='passed'
    # Independently verify the algebraic reduction used to make the
    # unsummed Schur calculation sharp enough for a ball replay.
    u,v=sp.symbols('u v');X=1/(1+u-u*v);Y=1/(1+v-u*v);T=1-u*v;root=1-u-v
    a=u*v/T;left=X*u/(1-X*u);right=Y*v/(1-Y*v)
    core=sp.Matrix([[a-left,a],[a,a-right]])
    cross=sp.diag(1/(1-X*u),1/(1-Y*v))
    direct=sp.diag(X/(1-X)-left,Y/(1-Y)-right)
    schur=direct-cross.T*core.inv()*cross
    target=sp.Matrix([[(1-u)/T*(1/(1-X)+1/(X*X*u*root)),1/(X*Y*T*root)],
                      [1/(X*Y*T*root),(1-v)/T*(1/(1-Y)+1/(Y*Y*v*root))]])
    algebra=[]
    for i,j in [(0,0),(0,1),(1,1)]:
        assert sp.factor(schur[i,j]-target[i,j])==0
        algebra.append(f'original index Schur entry {i}{j}')
    q,t=sp.symbols('q t');tp=(1+q*t)/(q-t);tm=(1-q*t)/(q+t)
    assert sp.factor(tp+tm-2*q*(1+t*t)/(q*q-t*t))==0
    assert sp.factor((tm-tp)/2+t*(1+q*q)/(q*q-t*t))==0
    algebra.extend(['original cosine cap angular Hessian','original cosine cap mixed Hessian'])
    p=arb.pi();ii=acb(0,1);R=arb(1)/200
    xh=acb(arb(1)/6,arb(2).log()/(2*p))
    k0=4*p/21*(2*arb(3).sqrt()-3*ii);D=5+arb(21).sqrt()

    def rat(v):
        v=Q(v);return arb(v.numerator)/v.denominator

    def point(v):return acb(rat(v[0]),rat(v[1]))

    C=[[point(z)for z in row]for row in data['rational_preconditioner']]
    assert len(C)==3 and all(len(row)==3 for row in C)

    def retained(x,y):
        X,Y=(2*p*ii*x).exp(),(2*p*ii*y).exp()
        alpha,beta=1/X-1,1/Y-1
        discriminant=1-2*(alpha+beta)+(alpha-beta)**2
        root=discriminant.sqrt()
        U,V=(1+alpha-beta-root)/2,(1-alpha+beta-root)/2
        first,second=ii*U.log()/(2*p),ii*V.log()/(2*p)
        # Original unsummed phase Hessian and its exact Schur complement.
        common=U*V/(1-U*V);left=X*U/(1-X*U);right=Y*V/(1-Y*V)
        ss=2*p*ii*(common-left);tt=2*p*ii*(common-right);st=2*p*ii*common
        sx=2*p*ii/(1-X*U);ty=2*p*ii/(1-Y*V)
        xx=2*p*ii*(X/(1-X)-left);yy=2*p*ii*(Y/(1-Y)-right)
        # Eliminate the exact stationary identities
        # 1-XU=X(1-UV), 1-YV=Y(1-UV), 1-U-V=root before
        # interval evaluation. This is the original index Schur form,
        # without the severe interval cancellation of a generic inverse.
        T=1-U*V
        hxx=2*p*ii*(1-U)/T*(1/(1-X)+1/(X*X*U*root))
        hxy=2*p*ii/(X*Y*T*root)
        hyy=2*p*ii*(1-V)/T*(1/(1-Y)+1/(Y*Y*V*root))
        px=2*p*ii*first+(1-X*U).log()-(1-X).log()-p*ii
        py=2*p*ii*second+(1-Y*V).log()-(1-Y).log()-p*ii
        return dict(X=X,Y=Y,U=U,V=V,indices=[first,second],delta=discriminant,
                    px=px,py=py,hxx=hxx,hxy=hxy,hyy=hyy)

    def cap(x,tau):
        plus=p*x+tau/2;minus=p*x-tau/2
        lp,lm=plus.cos().log(),minus.cos().log()
        cx=lp+lm-2*(p*x).sin().log()
        ct=(lp-lm)/(2*p)-(tau/2).tan().asinh()/p+3*ii*tau/(2*p)-ii
        cxx=-p*(plus.tan()+minus.tan()+2/(p*x).tan())
        cxt=(minus.tan()-plus.tan())/2
        ctt=-(plus.tan()+minus.tan()+2/(tau/2).cos())/(4*p)+3*ii/(2*p)
        return cx,ct,cxx,cxt,ctt

    def system(x,tau,z,w):
        old,new=retained(x,z),retained(z,w)
        cx,ct,cxx,cxt,ctt=cap(x,tau)
        residual=[-2*p*ii*ct,cx+old['px'],old['py']+new['px']]
        jac=[[-2*p*ii*cxt,-2*p*ii*ctt,acb(0)],
             [cxx+old['hxx'],cxt,old['hxy']],
             [old['hxy'],acb(0),old['hyy']+new['hxx']]]
        seed_second=old['hyy']-old['hxy']**2/(cxx-cxt*cxt/ctt+old['hxx'])
        total=seed_second+new['hxx']
        outgoing=new['hyy']-new['hxy']**2/total
        return residual,jac,old,new,total,outgoing

    count=0;sectors=0;smallest_sector=None;smallest_newton=None;largest_contraction=arb(0)
    branch_comparisons=0

    def positive(name,value,identifier):
        nonlocal branch_comparisons
        assert value>0,(identifier,name,value)
        branch_comparisons+=1

    def verify(identifier,item,wc,wbox,pr,radii):
        nonlocal count,sectors,smallest_sector,smallest_newton,largest_contraction
        centers=[point(z)for z in item['centers']];assert len(centers)==3
        for text,value in zip(item['radii'],radii):assert arb(text).contains(value),(identifier,'radius',text,value)
        boxes=[acb(z.real+arb(0,r),z.imag+arb(0,r))for z,r in zip(centers,radii)]
        residual=system(*centers,wc)[0]
        variation=abs(retained(centers[2],wbox)['hxy'])*pr
        _,J,old,new,total,outgoing=system(*boxes,wbox)
        for row in range(3):
            contraction=sum(abs(acb(int(row==col))-sum(C[row][j]*J[j][col]for j in range(3)))*radii[col]
                            for col in range(3))/radii[row]
            displacement=abs(sum(C[row][j]*residual[j]for j in range(3)))+abs(C[row][2])*variation
            margin=radii[row]-displacement-contraction*radii[row]
            assert contraction<rat(Q(1,4))and margin>0,(identifier,'Newton row',row,contraction,margin)
            largest_contraction=max(largest_contraction,contraction.upper())
            smallest_newton=margin.lower()if smallest_newton is None else min(smallest_newton,margin.lower())
        x,tau,z=boxes
        positive('true incoming source disk',R-abs(z-xh),identifier)
        for name,wire in [('old',x),('new',z)]:
            for suffix,value in [('real lower',wire.real-rat('.14')),('real upper',rat('.20')-wire.real),
                                 ('height lower',wire.imag-rat('.09')),('height upper',rat('.12')-wire.imag)]:
                positive(name+' '+suffix,value,identifier)
        for name,value in [('cap real lower',tau.real),('cap real upper',rat('1.8')-tau.real),
                           ('cap height lower',1+tau.imag),('cap height upper',-tau.imag-rat('.97'))]:
            positive(name,value,identifier)
        for label,d,leftwire,rightwire in [('old',old,x,z),('new',new,z,wbox)]:
            positive(label+' upper quadratic branch',d['delta'].imag,identifier)
            for name,U,X,index,wire in zip(['first','second'],[d['U'],d['V']],[d['X'],d['Y']],d['indices'],[leftwire,rightwire]):
                for suffix,value in [('U real negative',-U.real),('U imag negative',-U.imag),
                                     ('index lower',index.real-rat('.25')),('index upper',rat('.45')-index.real),
                                     ('index height',rat('.03')-abs(index.imag)),('root-product radius',1-abs(X*U)),
                                     ('index minus wire lower',(index-wire).real),
                                     ('index minus wire upper',rat('.5')-(index-wire).real)]:
                    positive(label+' '+name+' '+suffix,value,identifier)
            positive(label+' sum index lower',sum(i.real for i in d['indices'])-rat('.5'),identifier)
            positive(label+' sum index upper',1-sum(i.real for i in d['indices']),identifier)
        q,t,sec=1/(p*x).tan(),(tau/2).tan(),1/(tau/2).cos()
        for name,value in [('q+tan',q+t),('q-tan',q-t),('sec+tan',sec+t),
                           ('cos+', (p*x+tau/2).cos()),('cos-',(p*x-tau/2).cos()),('sin',(p*x).sin())]:
            positive('cap log '+name,value.real,identifier)
        positive('combined Hessian loss18',-total.real-18,identifier)
        positive('outgoing real curvature below9.8',rat('9.8')+outgoing.real,identifier)
        positive('outgoing real curvature above9.3',-outgoing.real-rat('9.3'),identifier)
        positive('outgoing normalized Hessian defect below.18',rat('.18')-abs(outgoing/k0+arb(21).sqrt()),identifier)
        for sign in [-1,1]:
            delta=sign*R-(z-xh)
            sector=(k0*D*delta*delta).real-rat('.752')*abs(k0)*abs(delta)**2
            positive('correlated endpoint sector',sector-rat(Q(1,2*10**6)),identifier)
            positive('outward real endpoint derivative',sign*(k0*D*delta).real-rat('.752')*abs(k0)*abs(delta),identifier)
            smallest_sector=sector.lower()if smallest_sector is None else min(smallest_sector,sector.lower())
            sectors+=1
            if identifier=='center':
                positive('opposite oriented Gaussian sectors',sign*((k0*D).sqrt()*delta).real,identifier)
        count+=1

    verify('center',data['center'],xh,xh,arb(0),[rat('1e-12')]*3)
    intervals=[]
    for j,cell in enumerate(data['cells']):
        lo,hi=map(Q,cell['real_output_interval']);assert Q(-9,1000)<=lo<hi<=Q(9,1000)
        intervals.append((lo,hi));mid=(lo+hi)/2
        # Replay each stored interval in eight exact subintervals. A
        # single explicit preconditioned Newton step at each midpoint
        # merely proposes new rational centers; the full outward
        # self-map below proves every refined root enclosure anew.
        for part in range(8):
            a,b=lo+(hi-lo)*part/8,lo+(hi-lo)*(part+1)/8
            wc=xh+rat((a+b)/2);wbox=xh+rat(a).union(rat(b));pr=rat((b-a)/2)
            initial=[point(z)for z in cell['centers']]
            residual=system(*initial,wc)[0]
            proposal=[initial[row]-sum(C[row][k]*residual[k]for k in range(3))for row in range(3)]
            rational_centers=[[str(Q(z.real.mid().str(70,radius=False))),
                               str(Q(z.imag.mid().str(70,radius=False)))]for z in proposal]
            radii=[rat('.05')*pr,rat('.15')*pr,rat('.24')*pr]
            refined={'centers':rational_centers,'radii':list(map(str,radii))}
            verify((j,part),refined,wc,wbox,pr,radii)
    intervals.sort()
    assert len(intervals)==data['cell_count']
    assert intervals[0][0]==Q(-9,1000) and intervals[-1][1]==Q(9,1000)
    assert all(a[1]==b[0]for a,b in zip(intervals,intervals[1:]))
    assert count==8*len(intervals)+1 and sectors==2*count
    assert data['sector_lower_bound']=='1/2000000' and data['Hessian_defect']=='94/125'
    for f,h in data['dependencies_sha256'].items():assert sha256((ROOT/f).read_bytes()).hexdigest()==h,f
    assert sha256((ROOT/'experiments/certify_three_first_entrance_real_critical.py').read_bytes()).hexdigest()==data['script_sha256']
    result={'status':'passed','precision_bits':args.precision,'real_interval_cells':len(intervals),
            'exact_algebraic_identities':algebra,
            'exact_multiplicity_one_interval_cover':True,'refined_subintervals':8*len(intervals),'Newton_polydisks':count,
            'correlated_endpoint_sectors':sectors,'branch_comparisons':branch_comparisons,
            'maximum_weighted_Newton_contraction':str(largest_contraction),
            'minimum_Newton_self_map_margin':str(smallest_newton),
            'minimum_correlated_sector':str(smallest_sector),
            'center_opposite_Gaussian_sectors':True,
            'method':'Independent original cosine/asinh cap derivatives and unsummed two-index Hessian Schur complements; eight exact subintervals per author cell, one explicit Newton step proposes rational centers, full outward self-maps reprove all roots; no optimizer or author import.',
            'scope':'Real-interval Newton/branch and correlated sector replay, true incoming disk inclusion, outgoing Hessian. V-contours use the full .752 Hessian remainder; no source complement is asserted.',
            'artifact_sha256':sha256(path.read_bytes()).hexdigest(),
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'elapsed_seconds':time.monotonic()-start}
    args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
