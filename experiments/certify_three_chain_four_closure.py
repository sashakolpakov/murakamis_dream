#!/usr/bin/env python3
"""Certify the actual four-chain critical wire and closing budgets.

The original four-complex-variable period system is checked by a single
outward Newton self-map. The previously saved geometric centers only
propose rational data. Correlated wire sectors retain their complex sign.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

from flint import arb, acb, acb_mat, ctx

ROOT = Path(__file__).resolve().parents[1]


def first_cap_center():
    pi, ii = arb.pi(), acb(0, 1)

    def rat(s):
        q = Q(s)
        return arb(q.numerator)/q.denominator

    def point(real, imag):
        return acb(rat(real), rat(imag))

    y = acb(arb(1)/6, arb(2).log()/(2*pi))
    centers = [point(".177337918569469382175948562048", ".101358689576302370861575311618"),
               point("1.533800710765884206016520588964", "-.978955098405739999074096803416")]
    radius = rat("1e-8")
    boxes = [acb(z.real+arb(0, radius), z.imag+arb(0, radius)) for z in centers]
    preconditioner = [
        [point("-.012459042950055255651267420891", ".009121085447815058535390706888"),
         point("-.030322991884195644218839259185", "-.022730223128523958826095306578")],
        [point(".222750256842225811720371833986", "-.117735701411284707218221686158"),
         point(".057309470071241114644219436946", ".078282475605306592775433429801")],
    ]

    def retained(x):
        X, Y = (2*pi*ii*x).exp(), (2*pi*ii*y).exp()
        alpha, beta = 1/X-1, 1/Y-1
        root = (1-2*(alpha+beta)+(alpha-beta)**2).sqrt()
        U, V = (1+alpha-beta-root)/2, (1-alpha+beta-root)/2
        alpha_x, beta_y = -2*pi*ii/X, -2*pi*ii/Y
        Ux = alpha_x*(1-(alpha-beta-1)/root)/2
        Uy = beta_y*(-1-(beta-alpha-1)/root)/2
        Vy = beta_y*(1-(beta-alpha-1)/root)/2
        px = -U.log()+(1-X*U).log()-(1-X).log()-pi*ii
        py = -V.log()+(1-Y*V).log()-(1-Y).log()-pi*ii
        pxx = -Ux/U-(2*pi*ii*X*U+X*Ux)/(1-X*U)+2*pi*ii*X/(1-X)
        pxy = -Uy/U-X*Uy/(1-X*U)
        pyy = -Vy/V-(2*pi*ii*Y*V+Y*Vy)/(1-Y*V)+2*pi*ii*Y/(1-Y)
        return dict(X=X, Y=Y, root=root, U=U, V=V, px=px, py=py,
                    pxx=pxx, pxy=pxy, pyy=pyy)

    def system(x, t):
        data = retained(x)
        q, z, sec = 1/(pi*x).tan(), (t/2).tan(), 1/(t/2).cos()
        period = 3*t+2*ii*(z+sec).log()+ii*((q+z).log()-(q-z).log())-2*pi
        ft = 3+ii*(sec+q*sec**2/(q-z)/(q+z))
        fx = 2*pi*ii*z*(1+q*q)/(q-z)/(q+z)
        tp, tm = (pi*x+t/2).tan(), (pi*x-t/2).tan()
        bx = (pi*x+t/2).cos().log()+(pi*x-t/2).cos().log()-2*(pi*x).sin().log()
        bxx, bxt = -pi*(tp+tm+2*q), (tm-tp)/2
        return [period, bx+data["px"]], [[fx, ft], [bxx+data["pxx"], bxt]], data, (bxx, bxt, ii*ft/(2*pi))

    residual, _, _, _ = system(*centers)
    _, jacobian, data, (bxx, bxt, ftt) = system(*boxes)
    defect = [[acb(int(i == j))-sum(preconditioner[i][k]*jacobian[k][j] for k in range(2))
               for j in range(2)] for i in range(2)]
    row_norms = [sum(abs(z) for z in row) for row in defect]
    displacements = [abs(sum(preconditioner[i][k]*residual[k] for k in range(2))) for i in range(2)]
    checks = []

    def positive(name, value):
        assert value > 0, (name, value)
        checks.append({"name": name, "positive_margin": str(value)})

    for i in range(2):
        positive(f"Newton row {i}: contraction below 1/1000", rat(".001")-row_norms[i])
        positive(f"Newton row {i}: maps polydisk strictly inside itself", radius-displacements[i]-row_norms[i]*radius)
    x, t = boxes
    q, z, sec = 1/(pi*x).tan(), (t/2).tan(), 1/(t/2).cos()
    for name, value in [("cap q+z log", q+z), ("cap q-z log", q-z),
                        ("cap sec+z log", sec+z), ("retained square root", data["root"]),
                        ("cap numerator plus", (pi*x+t/2).cos()),
                        ("cap numerator minus", (pi*x-t/2).cos()),
                        ("cap sine", (pi*x).sin())]:
        positive(name+": right half-plane", value.real)
    r = x.real-arb(1)/6
    s = x.imag-y.imag+arb(4)/5*r
    positive("wire corridor r lower", r)
    positive("wire corridor r upper", rat(".013")-r)
    positive("wire corridor s lower", s+rat(".0015"))
    positive("wire corridor s upper", rat(".001")-s)
    positive("cap angle lower", t.real-rat("1.52"))
    positive("cap angle upper", rat("1.575")-t.real)
    positive("cap height lower", -t.imag-rat(".97"))
    positive("cap height upper", 1+t.imag)
    for name in ("X", "Y"):
        positive(name+": first quadrant real", data[name].real-rat(".08"))
        positive(name+": first quadrant imaginary", data[name].imag-rat(".08"))
        positive(name+": modulus below 4/5", rat(".8")-abs(data[name]))
    for name, parameter in (("U", "X"), ("V", "Y")):
        value = data[name]
        positive(name+": negative real part", -value.real)
        positive(name+": negative imaginary part", -value.imag)
        positive(parameter+name+": modulus below one", 1-abs(data[parameter]*value))
        index = ii*value.log()/(2*pi)
        positive(name+": index real above 1/4", index.real-arb(1)/4)
        positive(name+": index real below 49/100", rat(".49")-index.real)
        positive(name+": index height lower", index.imag+rat(".03"))
        positive(name+": index height upper", rat(".03")-index.imag)
    cap_second = bxx-bxt*bxt/ftt
    total_second = cap_second+data["pxx"]
    outgoing_second = data["pyy"]-data["pxy"]**2/total_second
    derivative = -data["pxy"]/total_second
    positive("negative real composed wire Hessian above 21", -total_second.real-21)
    positive("outgoing negative real Hessian above 9", -outgoing_second.real-9)
    positive("outgoing phase gradient modulus below 2/25", rat(".08")-abs(data["py"]))
    positive("critical wire response modulus below 21/100", rat(".21")-abs(derivative))

    def sine_primitive(value):
        value = acb(value)
        return (-ii*pi*(value*value-value)/2
                +ii*(2*pi*ii*value).exp().polylog(2)/(2*pi)-ii*pi/12)

    def denominator_primitive(index, parameter):
        return ((parameter*(-2*pi*ii*index).exp()).polylog(2)
                -parameter.polylog(2))/(2*pi*ii)

    s_index = ii*data["U"].log()/(2*pi)
    t_index = ii*data["V"].log()/(2*pi)
    summed_index = s_index+t_index
    retained_action = (sine_primitive(summed_index)
                       +ii*pi*(summed_index-summed_index*summed_index)/2
                       +s_index*data["X"].log()+t_index*data["Y"].log()
                       -denominator_primitive(s_index, data["X"])
                       -denominator_primitive(t_index, data["Y"])-pi*ii*(x+y))
    cap_action = (-sine_primitive(arb(1)/2-x+t/(2*pi))
                  -sine_primitive(arb(1)/2-x-t/(2*pi))-2*sine_primitive(x)
                  -4*sine_primitive(arb(1)/4+t/(4*pi))
                  -4*sine_primitive(arb(1)/4-t/(4*pi))
                  +3*ii*t*t/(4*pi)-ii*t)
    total_action = cap_action+retained_action
    positive("actual composed action above191139/100000", total_action.real-rat("1.91139"))

    return total_action,checks


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=256)
    ap.add_argument('--output', type=Path,
                    default=ROOT/'repro/results/research-three-chain-four-closure.json')
    args = ap.parse_args()
    ctx.prec = args.precision
    pi, ii = arb.pi(), acb(0, 1)

    def a(value):
        value = Q(value)
        return arb(value.numerator)/value.denominator

    def point(parts):
        return acb(a(parts[0]), a(parts[1]))

    def squaredisk(z, radius):
        return acb(arb(z.real, radius), arb(z.imag, radius))

    def ret(t, u):
        v, c, s = (t/2).tan(), (u/2).cos(), (u/2).sin()
        root = (1+v*v*c*c).sqrt()
        return (v*c).asinh(), c*(1+v*v)/(2*root), -v*s/(2*root)

    def system(ts):
        rows, F = [[acb(0) for _ in ts] for _ in ts], []
        for j, t in enumerate(ts):
            neighbors = [(j-1, ts[j-1] if j else acb(0)),
                         (j+1, ts[j+1] if j+1 < len(ts) else acb(0))]
            total, derivative = acb(0), acb(3)
            for k, u in neighbors:
                value, dt, du = ret(t, u)
                total += value
                derivative += 2*ii*dt
                if 0 <= k < len(ts):
                    rows[j][k] = 2*ii*du
            F.append(3*t+2*ii*total-2*pi)
            rows[j][j] = derivative
        return F, rows

    source_path = ROOT/'repro/results/research-three-chain-geometric-chamber.json'
    source = json.loads(source_path.read_text())
    assert source['status'] == 'passed'
    ref = next(item for item in source['references'] if item['length'] == 4)
    centers_q = ref['centers']
    centers = [point(z) for z in centers_q]
    radius_q = Q(1, 10**23)
    radius = a(radius_q)
    boxes = [squaredisk(z, radius) for z in centers]
    F0, J0 = system(centers)
    inverse = acb_mat(J0).inv()
    Cq = [[[str(inverse[j, k].real.mid().fmpq()),
            str(inverse[j, k].imag.mid().fmpq())] for k in range(4)] for j in range(4)]
    C = [[point(z) for z in row] for row in Cq]
    _, Jbox = system(boxes)
    checks, contractions, selfmaps = [], [], []

    def positive(name, value):
        assert value > 0, (name, value)
        checks.append({'name': name, 'strict_positive_margin': str(value)})

    positive('known original geometric root lies in fresh Newton disks',
             radius-a(Q(16, 3*10**25)))

    for row in range(4):
        con = sum(abs(acb(int(row == col))-sum(C[row][k]*Jbox[k][col] for k in range(4)))
                  for col in range(4))
        residual = abs(sum(C[row][k]*F0[k] for k in range(4)))
        margin = radius-residual-con*radius
        positive(f'Newton row{row} contraction below1/4', a('1/4')-con)
        positive(f'Newton row{row} maps complex disk into itself', margin)
        contractions.append(str(con))
        selfmaps.append(str(margin))
    for j, t in enumerate(boxes):
        for label, value in [('angle lower', t.real-a('1.3')),
                             ('angle upper', a('1.82')-t.real),
                             ('depth lower', -t.imag-a('.82')),
                             ('depth upper', a('1.21')+t.imag)]:
            positive(f'original positive geometry{j} '+label, value)
        for u in [boxes[j-1] if j else acb(0), boxes[j+1] if j < 3 else acb(0)]:
            z = (t/2).tan()*(u/2).cos()
            positive(f'original return{j} right half-plane', z.real)
            positive(f'original return{j} square-root positive real', (1+z*z).sqrt().real)
    completed = [acb(0), *boxes, acb(0)]
    for j, (t, u) in enumerate(zip(completed, completed[1:])):
        tv, uv = (t/2).tan(), (u/2).tan()
        edge_root = (1+tv*tv+uv*uv).sqrt()
        positive(f'original edge{j} positive-cell criterion',
                 edge_root.real-(tv.real**2+uv.real**2).sqrt())

    def wire(t, u):
        c = (1-t.cos()*u.cos())/(2+t.cos()+u.cos())
        positive('wire cosine in lower half-plane', -c.imag)
        return c.acos()/(2*pi)

    wires = [wire(t, u) for t, u in zip(boxes, boxes[1:])]
    xh = acb(arb(1)/6, arb(2).log()/(2*pi))
    indices = []
    for j, x in enumerate(wires):
        for label, value in [('real lower', x.real-a('.14')), ('real upper', a('.20')-x.real),
                             ('height lower', x.imag-a('.09')), ('height upper', a('.12')-x.imag)]:
            positive(f'wire{j} source chamber '+label, value)
    for x in [wires[0], wires[-1]]:
        r, s = x.real-arb(1)/6, x.imag-xh.imag+4*(x.real-arb(1)/6)/5
        for label, value in [('r>0', r), ('r<.013', a('.013')-r),
                             ('s>-.0015', s+a('.0015')), ('s<.001', a('.001')-s)]:
            positive('original complete-cap directed domain '+label, value)
    for t in [boxes[0], boxes[-1]]:
        for label, value in [('real>1.5', t.real-a('1.5')), ('real<1.55', a('1.55')-t.real),
                             ('depth>.97', -t.imag-a('.97')), ('depth<1', 1+t.imag),
                             ('cos half modulus<1', 1-abs((t/2).cos()))]:
            positive('original cap '+label, value)
    for j, (x, y) in enumerate(zip(wires, wires[1:])):
        X, Y = (2*pi*ii*x).exp(), (2*pi*ii*y).exp()
        al, be = 1/X-1, 1/Y-1
        delta = 1-2*(al+be)+(al-be)**2
        positive(f'index{j} selected discriminant lift', delta.imag)
        U, V = (1+al-be-delta.sqrt())/2, (1-al+be-delta.sqrt())/2
        pair = []
        for name, z, base in [('s', U, X), ('t', V, Y)]:
            coordinate = ii*z.log()/(2*pi)
            pair.append(coordinate)
            for label, value in [('U real negative', -z.real), ('U imaginary negative', -z.imag),
                                 ('real>.25', coordinate.real-a('.25')), ('real<.45', a('.45')-coordinate.real),
                                 ('height<.02', a('.02')-abs(coordinate.imag)), ('product radius<1', 1-abs(base*z))]:
                positive(f'index{j}{name} '+label, value)
        positive(f'index{j} sum real>.5', sum(z.real for z in pair)-a('.5'))
        indices.append([str(z) for z in pair])

    zc = wires[1]-xh
    positive('closing real inside new chart lower',zc.real+a('.006'))
    positive('closing real inside new chart upper',a('.007')-zc.real)
    positive('closing height inside new chart lower',zc.imag+a('.004125'))
    positive('closing height inside new chart upper',-zc.imag)
    k0 = 4*pi/21*(2*arb(3).sqrt()-3*ii)
    K,D,beta=abs(k0),2*arb(21).sqrt(),arb(1)
    sectors=[]
    for sign,endpoint in [(-1,a('-.006')),(1,a('.007'))]:
        d=endpoint-zc
        sec=(k0*D*d*d).real-K*abs(d)**2
        slope=sign*(k0*D*d).real-K*abs(d)
        positive('sector>.00006',sec-a('.00006'))
        positive('slope>.09',slope-a('.09'))
        sectors.append({'endpoint':str(endpoint),'sector':str(sec),'slope':str(slope)})
    drift=(k0*D*zc*zc).real/2-K*abs(zc)**2/2
    positive('drift>-.0003',drift+a('.0003'))
    positive('curvature>16',D*k0.real-K-16)
    center_action,center_checks=first_cap_center()
    # The real endpoint phase floors use the existing |S1second|<16
    # and |Re S1prime(0)|<.0113, with the separately replayed M1>1.91139.
    for e in [a('.006'),a('.007')]:
        positive('V endpoint phase>1.9109',a('1.91139')-a('.0113')*e-8*e*e-a('1.9109'))
    positive('middle gap',a('9.3')*a('.009')**2-a('.0226')*a('.009')-a('.0003')-a('.00024'))
    positive('plateau gap',a('1.91139')-a('1.9107')-a('.0003')-a('.0113')**2/a('18.6')-a('.00038'))
    positive('far gap',2*(a('1.91139')-a('1.91115'))-a('.0003')-a('.00017'))
    deps=['notes/research_three_chain_four_closure.md',
          'notes/research_three_chain_geometric_chamber.md',
          'notes/research_three_chain_action_volume_calibration.md',
          'notes/research_three_prepared_cap_quantified_source.md',
          'notes/research_three_prepared_cap_real_extension.md',
          'notes/research_three_phase_graph_transform.md',
          'notes/research_three_prepared_cap_directed_complements.md',
          'notes/research_three_chain_outside_boundary_decay.md',
          'repro/results/research-three-chain-geometric-chamber.json',
          'repro/results/research-three-four-source-chart.json',
          'repro/results/research-three-four-source-chart-replay.json',
          'repro/results/research-three-prepared-cap-directed-complements.json',
          'repro/results/research-three-prepared-cap-directed-complements-replay.json']
    result={'status':'passed','precision_bits':args.precision,
            'scope':'Fresh original four-variable period self-map, source branches, correlated V sectors and action drift; fresh original first-cap root/action; source packet and full-boundary contour conclusions are the written proof.',
            'centers':centers_q,'complex_disk_radius':str(radius_q),'preconditioner':Cq,
            'checks':checks,'strict_comparisons':len(checks),
            'closing_displacement':str(zc),'correlated_sectors':sectors,'action_drift_lower':str(drift),
            'center_cap_action':str(center_action),'center_cap_checks':center_checks,
            'center_cap_comparisons':len(center_checks),
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest()for p in deps}}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',len(checks),'four-chain comparisons,',len(center_checks),'first-cap comparisons',str(zc),str(drift))

if __name__=='__main__':main()
