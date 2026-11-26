#!/usr/bin/env python3
"""Directed prepared-cap critical chart and original source current bounds.

Exact rational parameters cover [-.006,.007]+i[-.004125,0] relative to xh.
Every critical cell receives its own analytic Newton self-map. Original
joint concavity turns 56 outward supporting planes into full current
bounds. The completed source and four-chain closure are written proofs.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import time
import mpmath as mp
from flint import arb,acb,ctx
from certify_three_prepared_central_currents import function as current_value_gradient
ROOT=Path(__file__).resolve().parents[1]

def rat(value):
    q=Q(value)
    return arb(q.numerator)/q.denominator

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision',type=int,default=192)
    ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-three-four-source-chart.json')
    args=ap.parse_args();ctx.prec=args.precision;mp.mp.dps=55;start=time.monotonic()
    pi,ii=arb.pi(),acb(0,1)
    xh=acb(arb(1)/6,arb(2).log()/(2*pi))
    k0=4*pi/21*(2*arb(3).sqrt()-3*ii)
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
    nx,ny,width=104,33,Q(1,8000)
    for i in range(nx):
        for j in range(ny):
            a=Q(-3,500)+i*width;b=a+width
            c=Q(-33,8000)+j*width;d=c+width
            yc=xh+acb(rat((a+b)/2),rat((c+d)/2))
            ybox=xh+acb(rectangle(a,b),rectangle(c,d))
            ymp=mp.mpf(1)/6+1j*mp.log(2)/(2*mp.pi)+mpq((a+b)/2)+1j*mpq((c+d)/2)
            xm,tm=mp.findroot(lambda x,t:mp_system(x,t,ymp),(.1773+.1013j,1.534-.979j))
            strings=[rational_center(xm),rational_center(tm)]
            centers=[point(*v)for v in strings]
            pr=rat(width)/arb(2).sqrt();radii=[pr*arb(7)/20,pr]
            residual=system(*centers,yc)[0]
            variation=abs(retained(centers[0],ybox)['pxy'])*pr
            boxes=[acb(z.real+arb(0,r),z.imag+arb(0,r))for z,r in zip(centers,radii)]
            _,J,data,(bxx,bxt,ftt)=system(*boxes,ybox)
            contractions=[];self_margins=[]
            for row in range(2):
                con=sum(abs(acb(int(row==col))-sum(C[row][k]*J[k][col]for k in range(2)))*radii[col]
                        for col in range(2))/radii[row]
                disp=abs(sum(C[row][k]*residual[k]for k in range(2)))+abs(C[row][1])*variation
                margin=radii[row]-disp-con*radii[row]
                assert con<arb(1)/10 and margin>0,(i,j,row,con,margin)
                contractions.append(str(con));self_margins.append(str(margin))
            margins=in_joint_box(*boxes,data)
            s,t=ii*data['U'].log()/(2*pi),ii*data['V'].log()/(2*pi)
            margins += [boxes[0].real-rat('.176'),rat('.179')-boxes[0].real,
                        boxes[1].real-rat('1.5'),rat('1.55')-boxes[1].real,
                        s.real-rat('.31'),rat('.39')-s.real,t.real-rat('.31'),rat('.39')-t.real,
                        s.imag+rat('.008'),rat('.008')-s.imag,t.imag+rat('.017'),rat('.012')-t.imag,
                        data['delta'].imag if 'delta'in data else (1-2*((1/data['X']-1)+(1/data['Y']-1))+((1/data['X']-1)-(1/data['Y']-1))**2).imag,
                        1-abs(data['X']*data['U']),1-abs(data['Y']*data['V']),
                        s.real+t.real-rat('.5'),1-s.real-t.real]
            assert all(v>0 for v in margins),(i,j,list(map(str,margins)))
            outgoing=data['pyy']-data['pxy']**2/(bxx-bxt*bxt/ftt+data['pxx'])
            defect=abs(outgoing/k0+arb(21).sqrt())
            assert defect<arb(1)/2,(i,j,defect)
            cells.append({'cell':[i,j],'output_box':[[str(a),str(b)],[str(c),str(d)]],
                          'centers':strings,'radii':list(map(str,radii)),
                          'contractions':contractions,'self_map_margins':self_margins,
                          'coordinate_enclosures':[str(z)for z in[*boxes,s,t]],
                          'branch_domain_margins':list(map(str,margins)),
                          'normalized_hessian_defect':str(defect)})
        if i%16==0:print('critical row',i,'/',nx,flush=True)
    assert len(cells)==3432
    # Accepted points from the older certificate are only proposals.
    # Every value and derivative is freshly recomputed on the new domains.
    proposal_path=ROOT/'repro/results/research-three-prepared-central-currents.json'
    proposals=json.loads(proposal_path.read_text())['domains']
    bounds=[(Q(7,50),Q(1,5)),(Q(0),Q(9,5)),(Q(1,4),Q(9,20)),
            (Q(1,4),Q(9,20)),(Q(1,6)-Q(3,500),Q(1,6)+Q(7,1000))]
    base=[Q(10135869,10**8),-Q(97895510,10**8),Q(300831,10**8),-Q(629803,10**8)]
    def domains():
        for axis,end,hs,ht,hy in product((2,3),(0,1),(-Q(1,125),Q(1,125)),(-Q(17,1000),Q(3,250)),(-Q(33,8000),Q(0))):
            bb=list(bounds);bb[axis]=(bb[axis][end],)*2;h=base[:];h[2]=hs;h[3]=ht
            yield('index_side',axis,end,str(hs),str(ht),str(hy)),bb,h+[hy],Q(19107,10000)
        for hs,ht,hy in product((-Q(1,125),Q(1,125)),(-Q(17,1000),Q(3,250)),(-Q(33,8000),Q(0))):
            h=base[:];h[2]=hs;h[3]=ht
            yield('alias',str(hs),str(ht),str(hy)),bounds,h+[hy],Q(39,20)
        for axis,end,hy in product(range(4),(0,1),(-Q(33,8000),Q(0))):
            bb=list(bounds);bb[axis]=(bb[axis][end],)*2
            yield('translation_face',axis,end,str(hy)),bb,base+[hy],Q(19107,10000)
    planes=[]
    for old,(key,bb,h,target)in zip(proposals,domains(),strict=True):
        z=list(map(Q,old['support_point']))
        if key==('translation_face',0,1,'0'):
            # A new rational proposer is needed on the enlarged right
            # wire face. Only its fresh outward support value is used.
            z=list(map(Q,['1/5','14489142665853911/10000000000000000',
                          '737102089513349/2000000000000000',
                          '3174998186778547/10000000000000000',
                          '1643664376504509/10000000000000000']))
        assert all(a<=v<=b for v,(a,b)in zip(z,bb))
        value,gradient=current_value_gradient(z,h)
        upper=value+sum(max((g*rat(a-v)).upper(),(g*rat(b-v)).upper())for g,(a,b),v in zip(gradient,bb,z))
        assert upper<rat(target),(key,upper,target)
        planes.append({'domain':list(key),'bounds':[[str(a),str(b)]for a,b in bb],
                       'heights':list(map(str,h)),'support_point':list(map(str,z)),
                       'threshold':str(target),'support_upper':str(upper)})
    assert len(planes)==56
    scalar=[rat(Q(19107,10000))-rat(Q(39,20))+2*pi/125,
            rat(Q(27,40))*rat(Q(21,1000))**2-rat(Q(1,4000)),
            rat(Q(3,8))*rat(Q(3,50))**2-rat(Q(1,4000)),
            rat(Q(7,880))*rat(Q(1,4))**2-rat(Q(1,4000))]
    assert all(v>0 for v in scalar)
    deps=['notes/research_three_prepared_cap_quantified_source.md',
          'notes/research_three_phase_graph_transform.md',
          'notes/research_three_vertex_joint_concavity.md',
          'experiments/certify_three_prepared_central_currents.py',
          str(proposal_path.relative_to(ROOT))]
    proof='notes/research_three_chain_four_closure.md'
    if(ROOT/proof).exists():deps.insert(0,proof)
    result={'status':'passed','precision_bits':args.precision,
            'scope':'Exact directed critical chart and original supporting-plane currents, not by itself a source asymptotic.',
            'output_rectangle':[['-3/500','7/1000'],['-33/8000','0']],
            'grid':[nx,ny],'exact_rational_cover':True,'critical_cells':cells,'critical_cell_count':len(cells),
            'preconditioner':[[str(z)for z in row]for row in C],
            'support_planes':planes,'support_plane_count':len(planes),'scalar_margins':list(map(str,scalar)),
            'elapsed_seconds':time.monotonic()-start,'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest()for p in deps}}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',len(cells),'critical cells,',len(planes),'planes,',len(scalar),'scalars',flush=True)

if __name__=='__main__':main()
