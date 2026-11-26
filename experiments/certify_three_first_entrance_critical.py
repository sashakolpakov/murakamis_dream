#!/usr/bin/env python3
"""Original first-entrance critical branch on the true output circle.

Three complex unknowns: old cap wire, cap angle, new integration wire.
Exact rational angular cover, outward complex Newton self-maps, and
endpoint Gaussian sectors. Numerical roots only propose rational data.
"""

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import time

import mpmath as mp
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=192)
    parser.add_argument('--mesh', type=int, default=64)
    parser.add_argument('--max-cells', type=int, default=20000)
    parser.add_argument('--output', type=Path,
                        default=ROOT/'repro/results/research-three-first-entrance-critical.json')
    args = parser.parse_args()
    ctx.prec, mp.mp.dps = args.precision, 60
    start = time.monotonic()
    pi, ii = arb.pi(), acb(0, 1)
    xh = acb(arb(1)/6, arb(2).log()/(2*pi))
    xhm = mp.mpf(1)/6+1j*mp.log(2)/(2*mp.pi)
    R = arb(1)/200
    k0 = 4*pi/21*(2*arb(3).sqrt()-3*ii)
    D = 5+arb(21).sqrt()

    def rat(q):
        q = Q(q)
        return arb(q.numerator)/q.denominator

    def interval(lo, hi):
        return arb(rat((lo+hi)/2), rat((hi-lo)/2))

    def point(parts):
        return acb(rat(parts[0]), rat(parts[1]))

    def rational(z):
        return [str(Q(str(z.real))), str(Q(str(z.imag)))]

    def mp_retained(x, y):
        X, Y = mp.exp(2j*mp.pi*x), mp.exp(2j*mp.pi*y)
        al, be = 1/X-1, 1/Y-1
        root = mp.sqrt(1-2*(al+be)+(al-be)**2)
        U, V = (1+al-be-root)/2, (1-al+be-root)/2
        return (-mp.log(U)+mp.log(1-X*U)-mp.log(1-X)-mp.pi*1j,
                -mp.log(V)+mp.log(1-Y*V)-mp.log(1-Y)-mp.pi*1j)

    def mp_system(x, tau, z, w):
        px, py = mp_retained(x, z)
        newpx = mp_retained(z, w)[0]
        q, t, sec = 1/mp.tan(mp.pi*x), mp.tan(tau/2), 1/mp.cos(tau/2)
        period = 3*tau+2j*mp.log(t+sec)+1j*(mp.log(q+t)-mp.log(q-t))-2*mp.pi
        bx = mp.log(mp.cos(mp.pi*x+tau/2))+mp.log(mp.cos(mp.pi*x-tau/2))-2*mp.log(mp.sin(mp.pi*x))
        return period, bx+px, py+newpx

    def retained(x, y):
        X, Y = (2*pi*ii*x).exp(), (2*pi*ii*y).exp()
        al, be = 1/X-1, 1/Y-1
        delta = 1-2*(al+be)+(al-be)**2
        root = delta.sqrt()
        U, V = (1+al-be-root)/2, (1-al+be-root)/2
        ax, by = -2*pi*ii/X, -2*pi*ii/Y
        Ux, Uy, Vy = ax*(1-U)/root, by*U/root, by*(1-V)/root
        px = -U.log()+(1-X*U).log()-(1-X).log()-pi*ii
        py = -V.log()+(1-Y*V).log()-(1-Y).log()-pi*ii
        pxx = -Ux/(U*(1-X*U))+2*pi*ii*X*(1-U)/((1-X)*(1-X*U))
        pxy = -Uy/(U*(1-X*U))
        pyy = -Vy/(V*(1-Y*V))+2*pi*ii*Y*(1-V)/((1-Y)*(1-Y*V))
        return dict(X=X, Y=Y, U=U, V=V, delta=delta,
                    px=px, py=py, pxx=pxx, pxy=pxy, pyy=pyy)

    def system(x, tau, z, w):
        old, new = retained(x, z), retained(z, w)
        q, t, sec = 1/(pi*x).tan(), (tau/2).tan(), 1/(tau/2).cos()
        period = 3*tau+2*ii*(t+sec).log()+ii*((q+t).log()-(q-t).log())-2*pi
        ft = 3+ii*(sec+q*sec**2/(q-t)/(q+t))
        fx = 2*pi*ii*t*(1+q*q)/(q-t)/(q+t)
        tp, tm = (pi*x+tau/2).tan(), (pi*x-tau/2).tan()
        bx = (pi*x+tau/2).cos().log()+(pi*x-tau/2).cos().log()-2*(pi*x).sin().log()
        bxx, bxt, ftt = -pi*(tp+tm+2*q), (tm-tp)/2, ii*ft/(2*pi)
        residual = [period, bx+old['px'], old['py']+new['px']]
        jacobian = [[fx, ft, acb(0)],
                    [bxx+old['pxx'], bxt, old['pxy']],
                    [old['pxy'], acb(0), old['pyy']+new['pxx']]]
        seed_second = old['pyy']-old['pxy']**2/(bxx-bxt*bxt/ftt+old['pxx'])
        total_second = seed_second+new['pxx']
        return residual, jacobian, old, new, seed_second, total_second

    center_mp = mp.findroot(lambda x, tau, z: mp_system(x, tau, z, xhm),
                            (.1777+.1009j, 1.532-.98j, xhm+.00215-.00188j))
    center_q = [rational(z) for z in center_mp]
    center = [point(z) for z in center_q]
    jc = mp.matrix(mp.jacobian(lambda x, tau, z: mp_system(x, tau, z, xhm), center_mp))
    Cq = [[rational(z) for z in row] for row in (jc**-1).tolist()]
    C = [[point(z) for z in row] for row in Cq]

    def verify(centers, boxes, radii, wc, wbox, parameter_radius):
        residual = system(*centers, wc)[0]
        variation = abs(retained(centers[2], wbox)['pxy'])*parameter_radius
        _, J, old, new, seed_second, total_second = system(*boxes, wbox)
        contractions, margins = [], []
        for row in range(3):
            con = sum(abs(acb(int(row == col))-sum(C[row][k]*J[k][col] for k in range(3)))*radii[col]
                      for col in range(3))/radii[row]
            disp = abs(sum(C[row][k]*residual[k] for k in range(3)))+abs(C[row][2])*variation
            margin = radii[row]-disp-con*radii[row]
            if not con < rat(Q(1,4)) or not margin > 0:
                return None, 'Newton'
            contractions.append(str(con))
            margins.append(str(margin))
        checks = {}

        def pos(name, value):
            if not value > 0:
                raise ArithmeticError(name)
            checks[name] = str(value)

        x, tau, z = boxes
        try:
            pos('new wire strictly inside prepared source disk', R-abs(z-xh))
            for name, val in [('old wire', x), ('new wire', z)]:
                pos(name+' real lower', val.real-rat('.14'))
                pos(name+' real upper', rat('.20')-val.real)
                pos(name+' imaginary lower', val.imag-rat('.09'))
                pos(name+' imaginary upper', rat('.12')-val.imag)
            pos('cap real lower', tau.real)
            pos('cap real upper', rat('1.8')-tau.real)
            pos('cap imaginary lower', 1+tau.imag)
            pos('cap imaginary upper', -tau.imag-rat('.97'))
            for number, data in enumerate([old, new]):
                pos(f'root{number} upper branch', data['delta'].imag)
                indices = [ii*data[name].log()/(2*pi) for name in ['U', 'V']]
                for name, U, index, X in zip(['first', 'second'], [data['U'], data['V']],
                                            indices, [data['X'], data['Y']]):
                    pos(f'{number} {name} U real negative', -U.real)
                    pos(f'{number} {name} U imaginary negative', -U.imag)
                    pos(f'{number} {name} index real lower', index.real-rat('.25'))
                    pos(f'{number} {name} index real upper', rat('.45')-index.real)
                    pos(f'{number} {name} index height', rat('.03')-abs(index.imag))
                    pos(f'{number} {name} root-product radius', 1-abs(X*U))
                pos(f'{number} total real index above half', sum(i.real for i in indices)-rat('.5'))
                pos(f'{number} total real index below one', 1-sum(i.real for i in indices))
            q, t, sec = 1/(pi*x).tan(), (tau/2).tan(), 1/(tau/2).cos()
            for name, val in [('q+tan', q+t), ('q-tan', q-t), ('sec+tan', sec+t),
                              ('cos+', (pi*x+tau/2).cos()), ('cos-', (pi*x-tau/2).cos()),
                              ('sin', (pi*x).sin())]:
                pos('cap log '+name, val.real)
            response = -new['pxy']/total_second
            pos('combined Hessian real loss above 18', -total_second.real-18)
            for sign in [-1, 1]:
                delta = sign*R-(z-xh)
                sector = (k0*D*delta**2).real-rat('.6')*abs(k0)*abs(delta)**2
                pos(f'endpoint {sign} Gaussian sector beyond one millionth', sector-rat(Q(1,10**6)))
        except ArithmeticError as exc:
            return None, str(exc)
        return {'Newton_contractions': contractions, 'Newton_self_map_margins': margins,
                'margins': checks,
                'coordinate_parts': [[val.real.str(40, more=True), val.imag.str(40, more=True)]
                                     for val in boxes],
                'critical_displacement': (z-xh).str(40, more=True),
                'critical_response': response.str(40, more=True),
                'incoming_phase_Hessian': seed_second.str(40, more=True),
                'combined_phase_Hessian': total_second.str(40, more=True)}, None

    cr = rat('1e-12')
    cboxes = [acb(z.real+arb(0, cr), z.imag+arb(0, cr)) for z in center]
    center_data, error = verify(center, cboxes, [cr]*3, xh, xh, arb(0))
    assert center_data is not None, error
    center_data.update({'centers': center_q, 'radii': [str(cr)]*3})

    pending = [(Q(j,args.mesh), Q(j+1,args.mesh)) for j in reversed(range(args.mesh))]
    cells, rejected, visits = [], {}, 0
    while pending:
        lo, hi = pending.pop()
        visits += 1
        assert visits <= args.max_cells, 'Explicit visit budget exhausted'
        mid = (lo+hi)/2
        wc = xh+R*(2*pi*ii*rat(mid)).exp()
        wbox = xh+R*acb(0, 2*pi*interval(lo,hi)).exp()
        wm = xhm+mp.exp(2j*mp.pi*mp.mpf(mid.numerator)/mid.denominator)/200
        cm = mp.findroot(lambda x, tau, z: mp_system(x,tau,z,wm), tuple(center_mp))
        cq = [rational(z) for z in cm]
        cp = [point(z) for z in cq]
        # Arc distance to its middle is <= pi*R*(hi-lo).
        pr = pi*R*rat(hi-lo)
        radii = [rat('.05')*pr, rat('.15')*pr, rat('.24')*pr]
        boxes = [acb(z.real+arb(0,r), z.imag+arb(0,r)) for z,r in zip(cp,radii)]
        data, error = verify(cp,boxes,radii,wc,wbox,pr)
        if data is None:
            assert hi-lo > Q(1,2**20), (lo,hi,error)
            rejected[error] = rejected.get(error,0)+1
            pending.extend([(mid,hi),(lo,mid)])
            continue
        data.update({'angle_fraction_interval': [str(lo),str(hi)],
                     'centers': cq, 'radii': list(map(str,radii)),
                     'output_parts': [wbox.real.str(40,more=True),wbox.imag.str(40,more=True)]})
        cells.append(data)
        if len(cells)%256 == 0:
            print(f'Accepted {len(cells)}; visited {visits}; pending {len(pending)}',flush=True)
    assert cells[0]['angle_fraction_interval'][0] == '0'
    assert cells[-1]['angle_fraction_interval'][1] == '1'
    assert all(cells[i]['angle_fraction_interval'][1] == cells[i+1]['angle_fraction_interval'][0]
               for i in range(len(cells)-1))
    deps = ['notes/research_three_entrance_critical_branches.md',
            'notes/research_three_phase_graph_transform.md',
            'notes/research_three_prepared_cap_quantified_source.md',
            'notes/research_three_vertex_joint_concavity.md',
            'notes/research_three_vertex_input_rectangle.md']
    result = {'status':'passed','precision_bits':args.precision,
              'scope':'Actual first-entrance three-complex-variable critical branch on the true output circle, endpoint Gaussian sectors, and critical derivative. Analytic maximum/minimum principles extend these bounds to the disk; no complementary source bound is certified here.',
              'angle_cover':['0','1'],'cell_count':len(cells),'visited_cells':visits,
              'rejected_reasons':rejected,'center':center_data,'cells':cells,
              'rational_preconditioner':Cq,
              'sector_lower_bound':'1/1000000',
              'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},
              'elapsed_seconds':time.monotonic()-start}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ['status','cell_count','visited_cells','elapsed_seconds']},indent=2))


if __name__ == '__main__':
    main()
