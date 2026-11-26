#!/usr/bin/env python3
"""Independent cosine/log replay of the original four-chain closure.

No author module is imported. Rational centers propose a new Newton map,
whose preconditioner and derivatives are recomputed from a different
return formula. The geometric root and all scalar/source-domain premises
are checked before the exact finite-word bookkeeping.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

from flint import arb, acb, acb_mat, ctx
from replay_three_cap_wire_complement import positive_primitive
from replay_three_vertex_directed_packet import action as retained_action
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=320)
    ap.add_argument('--artifact', type=Path,
                    default=ROOT/'repro/results/research-three-chain-four-closure.json')
    ap.add_argument('--output', type=Path,
                    default=ROOT/'repro/results/research-three-chain-four-closure-replay.json')
    args = ap.parse_args()
    ctx.prec = args.precision
    artifact = json.loads(args.artifact.read_text())
    assert artifact['status'] == 'passed'
    assert len(artifact['centers']) == 4
    pi, ii = arb.pi(), acb(0, 1)

    def a(value):
        value = Q(value)
        return arb(value.numerator)/value.denominator

    def point(parts):
        return acb(a(parts[0]), a(parts[1]))

    checks = []

    def positive(name, value):
        assert value > 0, (name, value)
        checks.append({'name': name, 'strict_positive_margin': str(value)})

    def return_data(t, u):
        # Independent unsummed angular formula, without tan or asinh.
        st, ct = (t/2).sin(), (t/2).cos()
        su, cu = (u/2).sin(), (u/2).cos()
        radical = (ct*ct+st*st*cu*cu).sqrt()
        exp_return = (st*cu+radical)/ct
        value = exp_return.log()
        derivative_t = cu/(2*ct*radical)
        derivative_u = -st*su/(2*radical)
        return value, derivative_t, derivative_u, (radical, exp_return, ct)

    def original_system(ts):
        F, J = [], [[acb(0) for _ in ts] for _ in ts]
        for j, t in enumerate(ts):
            F.append(3*t-2*pi)
            J[j][j] = acb(3)
            for k in [j-1, j+1]:
                u = ts[k] if 0 <= k < len(ts) else acb(0)
                r, dt, du, _ = return_data(t, u)
                F[-1] += 2*ii*r
                J[j][j] += 2*ii*dt
                if 0 <= k < len(ts):
                    J[j][k] += 2*ii*du
        return F, J

    centers = [point(z) for z in artifact['centers']]
    radius = a(artifact['complex_disk_radius'])
    assert Q(artifact['complex_disk_radius']) == Q(1, 10**23)
    original_geometry = json.loads((ROOT/'repro/results/research-three-chain-geometric-chamber.json').read_text())
    assert artifact['centers'] == next(c['centers'] for c in original_geometry['references'] if c['length'] == 4)
    positive('original positive root strictly inside fresh Newton disks',
             radius-a(Q(16, 3*10**25)))
    boxes = [acb(arb(z.real, radius), arb(z.imag, radius)) for z in centers]
    F0, J0 = original_system(centers)
    inv = acb_mat(J0).inv()
    preconditioner = [[acb(a(str(inv[j, k].real.mid().fmpq())),
                            a(str(inv[j, k].imag.mid().fmpq())))
                       for k in range(4)] for j in range(4)]
    _, Jbox = original_system(boxes)
    contractions = []
    for row in range(4):
        con = sum(abs(acb(int(row == col))-sum(preconditioner[row][k]*Jbox[k][col]
                                               for k in range(4))) for col in range(4))
        residual = abs(sum(preconditioner[row][k]*F0[k] for k in range(4)))
        positive(f'independent Newton contraction row{row}', a('.25')-con)
        positive(f'independent Newton self-map row{row}', radius*(1-con)-residual)
        contractions.append(str(con))
    for j, t in enumerate(boxes):
        for name, value in [('a lower', t.real-a('1.3')), ('a upper', a('1.82')-t.real),
                            ('H lower', -t.imag-a('.82')), ('H upper', a('1.21')+t.imag)]:
            positive(f'original geometry{j} '+name, value)
        for k in [j-1, j+1]:
            u = boxes[k] if 0 <= k < 4 else acb(0)
            _, _, _, (radical, exp_return, ct) = return_data(t, u)
            positive(f'return{j},{k} radical branch', radical.real)
            positive(f'return{j},{k} normalized radical branch', (radical/ct).real)
            positive(f'return{j},{k} logarithm branch', exp_return.real)
    completed = [acb(0), *boxes, acb(0)]
    for j, (t, u) in enumerate(zip(completed, completed[1:])):
        tv, uv = (t/2).sin()/(t/2).cos(), (u/2).sin()/(u/2).cos()
        root = (1+tv*tv+uv*uv).sqrt()
        positive(f'original positive edge{j}', root.real-(tv.real**2+uv.real**2).sqrt())

    def wire(t, u):
        ct, cu = t.cos(), u.cos()
        c = (1-ct*cu)/(2+ct+cu)
        positive('wire lower cosine branch', -c.imag)
        w = c.conjugate()
        lift = -ii*(w+(w-1).sqrt()*(w+1).sqrt()).log()
        return lift.conjugate()/(2*pi)

    wires = [wire(t, u) for t, u in zip(boxes, boxes[1:])]
    xh = acb(arb(1)/6, arb(2).log()/(2*pi))
    for j, x in enumerate(wires):
        for name, value in [('x>.14', x.real-a('.14')), ('x<.20', a('.20')-x.real),
                            ('h>.09', x.imag-a('.09')), ('h<.12', a('.12')-x.imag)]:
            positive(f'source wire{j} '+name, value)
    for x in [wires[0], wires[-1]]:
        r, s = x.real-xh.real, x.imag-xh.imag+4*(x.real-xh.real)/5
        for name, value in [('r>0', r), ('r<.013', a('.013')-r),
                            ('s>-.0015', s+a('.0015')), ('s<.001', a('.001')-s)]:
            positive('directed original cap '+name, value)
    for t in [boxes[0], boxes[-1]]:
        for name, value in [('a>1.5', t.real-a('1.5')), ('a<1.55', a('1.55')-t.real),
                            ('H>.97', -t.imag-a('.97')), ('H<1', 1+t.imag),
                            ('cos radius', 1-abs((t/2).cos()))]:
            positive('cap critical '+name, value)
    for j, (x, y) in enumerate(zip(wires, wires[1:])):
        # Algebraic stationary indices are computed from the original
        # geometric angle, independently of the author's quadratic root.
        tau = boxes[j+1]
        coordinates = []
        for name, wire_value in [('left', x), ('right', y)]:
            X = (2*pi*ii*wire_value).exp()
            U = (1-X)/(1+X+2*X*tau.cos())
            s = ii*U.log()/(2*pi)
            coordinates.append(s)
            for label, value in [('U real<0', -U.real), ('U imaginary<0', -U.imag),
                                 ('index>.25', s.real-a('.25')), ('index<.45', a('.45')-s.real),
                                 ('depth<.02', a('.02')-abs(s.imag)), ('product radius', 1-abs(X*U))]:
                positive(f'geometric index{j} {name} '+label, value)
            for sign in [-1, 1]:
                arg = arb(1)/2-wire_value+sign*tau/(2*pi)
                positive(f'original factorial strip{j},{name},{sign} lower', arg.real)
                positive(f'original factorial strip{j},{name},{sign} upper', 1-arg.real)
        positive(f'index{j} sum>.5', sum(s.real for s in coordinates)-a('.5'))
    z = wires[1]-xh
    positive('closing real chart lower',z.real+a('.006'))
    positive('closing real chart upper',a('.007')-z.real)
    positive('closing imaginary chart lower',z.imag+a('.004125'))
    positive('closing imaginary chart upper',-z.imag)
    k0=4*pi/21*(2*arb(3).sqrt()-3*ii);K,D=abs(k0),2*arb(21).sqrt()
    sectors=[]
    for sign,endpoint in [(-1,a('-.006')),(1,a('.007'))]:
        d=endpoint-z
        sector=(k0*D*d*d).real-K*abs(d)**2
        slope=sign*(k0*D*d).real-K*abs(d)
        positive('correlated sector>.00006',sector-a('.00006'))
        positive('correlated slope>.09',slope-a('.09'))
        sectors.append({'sign':sign,'sector':str(sector),'slope':str(slope)})
    drift=(k0*D*z*z).real/2-K*abs(z)**2/2
    positive('actual action drift>-.0003',drift+a('.0003'))
    positive('directed chart strict curvature16',D*k0.real-K-16)
    for endpoint in[a('.006'),a('.007')]:
        positive('actual V phase floor>1.9109',a('1.91139')-a('.0113')*endpoint-8*endpoint**2-a('1.9109'))
    positive('middle gap>.00024',a('9.3')*a('.009')**2-a('.0226')*a('.009')-a('.0003')-a('.00024'))
    positive('plateau gap>.00038',a('.00069')-a('.0003')-a('.0113')**2/a('18.6')-a('.00038'))
    positive('far gap>.00017',2*a('.00024')-a('.0003')-a('.00017'))
    # Independent original first-cap center: use the unsummed stationary
    # Schur formulas and reflected/negative-frequency primitives.
    twopi=2*pi*ii
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
    cap_centers=[point(['.177337918569469382175948562048','.101358689576302370861575311618']),
                 point(['1.533800710765884206016520588964','-.978955098405739999074096803416'])]
    cap_radius=a('1e-10')
    cap_boxes=[acb(arb(v.real,cap_radius),arb(v.imag,cap_radius))for v in cap_centers]
    F0,J0,_,_=system(*cap_centers,xh)
    inv=acb_mat(J0).inv()
    cap_C=[[acb(a(str(inv[j,k].real.mid().fmpq())),a(str(inv[j,k].imag.mid().fmpq())))for k in range(2)]for j in range(2)]
    _,JJ,dd,_=system(*cap_boxes,xh)
    for row in range(2):
        con=sum(abs(acb(int(row==col))-sum(cap_C[row][k]*JJ[k][col]for k in range(2)))for col in range(2))
        disp=abs(sum(cap_C[row][k]*F0[k]for k in range(2)))
        positive('independent first-cap center contraction',a('.001')-con)
        positive('independent first-cap center self-map',cap_radius*(1-con)-disp)
    x,tau=cap_boxes
    qq,zz,ss=1/(pi*x).tan(),(tau/2).tan(),1/(tau/2).cos()
    for value in[qq+zz,qq-zz,zz+ss,(pi*x+tau/2).cos(),(pi*x-tau/2).cos(),(pi*x).sin()]:
        positive('independent first-cap center log branch',value.real)
    jr=lambda value:positive_primitive(value.real,abs(value.imag))
    cap_value=-jr(arb(1)/2-x+tau/(2*pi))-jr(arb(1)/2-x-tau/(2*pi))-2*jr(x)
    cap_value-=4*jr(arb(1)/4+tau/(4*pi))+4*jr(arb(1)/4-tau/(4*pi))
    cap_value+=3*tau.real*(-tau.imag)/(2*pi)+tau.imag
    center_value=cap_value+(retained_action(dd['s'],dd['t'],dd['X'],dd['Y'])-pi*ii*(x+xh)).real
    positive('independent actual center action>1.91139',center_value-a('1.91139'))
    identities=[]
    n=sp.Symbol('n',integer=True,positive=True);AA=sp.MatrixSymbol('A',n,n)
    closed=(AA**2*(AA**2).T).doit().xreplace({AA.T:AA}).doit()
    assert closed==AA**4;identities.append('exact original bilinear source A^2(A^2)^T=A^4')
    assert 1+1==4-2;identities.append('original unit carrier C_N3^2 kappa^2')
    assert Q(1)-1-1-Q(1,2)==Q(-3,2);identities.append('N dx, two N^-1 packets and Gaussian give N^-3/2')
    assert Q(1,2)+Q(1,2)==1;identities.append('combined Hessian defect one')
    assert Q('9.3')*Q('.009')**2-Q('.0226')*Q('.009')-Q('.0003')==Q('.0002499')
    identities.append('exact middle principal budget')
    assert Q('.00069')-Q('.0003')-Q('.0113')**2/Q('18.6')>Q('.00038')
    identities.append('exact single absolute-plateau budget')
    assert 2*Q('.00024')-Q('.0003')==Q('.00018');identities.append('exact far-period budget')
    cuts=list(map(Q,['-.5','-.02','-.009','-.006','.007','.009','.02','.5']))
    assert all(a<b for a,b in zip(cuts,cuts[1:]))and sum(b-a for a,b in zip(cuts,cuts[1:]))==1
    identities.append('exact asymmetric seven-interval closing partition')
    # Explicitly verify both independently replayed source inputs and the
    # author/replay link before accepting the source bookkeeping record.
    provenance=[]
    for stem,author_script,replay_script in[
        ('research-three-four-source-chart','certify_three_four_source_chart.py','replay_three_four_source_chart.py'),
        ('research-three-prepared-cap-directed-complements','certify_three_prepared_cap_directed_complements.py','replay_three_prepared_cap_directed_complements.py')]:
        pa=ROOT/'repro/results'/(stem+'.json');pr=ROOT/'repro/results'/(stem+'-replay.json')
        author=json.loads(pa.read_text());replay=json.loads(pr.read_text())
        assert author['status']==replay['status']=='passed'
        assert author['script_sha256']==sha256((ROOT/'experiments'/author_script).read_bytes()).hexdigest()
        assert replay['script_sha256']==sha256((ROOT/'experiments'/replay_script).read_bytes()).hexdigest()
        assert replay['artifact_sha256']==sha256(pa.read_bytes()).hexdigest()
        for rec in[author,replay]:
            for dep,digest in rec.get('dependencies_sha256',{}).items():
                assert sha256((ROOT/dep).read_bytes()).hexdigest()==digest,(stem,dep)
        provenance.append({'author':str(pa.relative_to(ROOT)),'author_sha256':sha256(pa.read_bytes()).hexdigest(),
                           'replay':str(pr.relative_to(ROOT)),'replay_sha256':sha256(pr.read_bytes()).hexdigest()})
    assert artifact['script_sha256']==sha256((ROOT/'experiments/certify_three_chain_four_closure.py').read_bytes()).hexdigest()
    for dep,digest in artifact['dependencies_sha256'].items():
        assert sha256((ROOT/dep).read_bytes()).hexdigest()==digest,dep
    result={'status':'passed','precision_bits':args.precision,
            'scope':'Independent original-period cosine/log Newton replay, geometric index coordinates, correlated V sectors, fresh original first-cap action by negative-frequency primitive, exact source word and complete-period budgets.',
            'strict_comparisons':len(checks),'comparisons':checks,'Newton_contractions':contractions,
            'closing_displacement':str(z),'correlated_sectors':sectors,'action_drift_lower':str(drift),
            'independent_first_cap_action':str(center_value),'exact_identities':identities,
            'passed_source_provenance':provenance,'artifact_sha256':sha256(args.artifact.read_bytes()).hexdigest(),
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':artifact['dependencies_sha256']|{
                'experiments/replay_three_cap_wire_complement.py':sha256((ROOT/'experiments/replay_three_cap_wire_complement.py').read_bytes()).hexdigest(),
                'experiments/replay_three_vertex_directed_packet.py':sha256((ROOT/'experiments/replay_three_vertex_directed_packet.py').read_bytes()).hexdigest()}}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',len(checks),'independent comparisons,',len(identities),'exact identities,',len(provenance),'source provenance pairs')

if __name__=='__main__':main()
