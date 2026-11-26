#!/usr/bin/env python3
"""Critical branch of the actual prepared cap on real output +/- .02.

The two-variable system and its Jacobian are the original phase equations.
Numerical roots propose rational centers only. Every accepted parameter
interval uses an outward complex Newton self-map. This is a critical-branch
certificate, not a full-source complementary-contour estimate.
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
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=192)
    ap.add_argument('--mesh', type=int, default=256)
    ap.add_argument('--output', type=Path,
                    default=ROOT/'repro/results/research-three-prepared-cap-real-critical.json')
    args = ap.parse_args()
    assert args.mesh > 0
    ctx.prec, mp.mp.dps = args.precision, 60
    start = time.monotonic()
    pi, ii = arb.pi(), acb(0, 1)
    xh = acb(arb(1)/6, arb(2).log()/(2*pi))
    k0 = 4*pi/21*(2*arb(3).sqrt()-3*ii)

    def rat(q):
        q = Q(q)
        return arb(q.numerator)/q.denominator

    def interval(lo, hi):
        return arb(rat((lo+hi)/2), rat((hi-lo)/2))

    def point(re, im):
        return acb(rat(re), rat(im))

    def retained(x, y):
        X, Y = (2*pi*ii*x).exp(), (2*pi*ii*y).exp()
        alpha, beta = 1/X-1, 1/Y-1
        delta = 1-2*(alpha+beta)+(alpha-beta)**2
        root = delta.sqrt()
        U, V = (1+alpha-beta-root)/2, (1-alpha+beta-root)/2
        ax, by = -2*pi*ii/X, -2*pi*ii/Y
        Ux, Uy, Vy = ax*(1-U)/root, by*U/root, by*(1-V)/root
        px = -U.log()+(1-X*U).log()-(1-X).log()-pi*ii
        py = -V.log()+(1-Y*V).log()-(1-Y).log()-pi*ii
        pxx = -Ux/(U*(1-X*U))+2*pi*ii*X*(1-U)/((1-X)*(1-X*U))
        pxy = -Uy/(U*(1-X*U))
        pyy = -Vy/(V*(1-Y*V))+2*pi*ii*Y*(1-V)/((1-Y)*(1-Y*V))
        return dict(X=X, Y=Y, U=U, V=V, delta=delta, root=root,
                    px=px, py=py, pxx=pxx, pxy=pxy, pyy=pyy)

    def system(x, tau, y):
        data = retained(x, y)
        q, z, sec = 1/(pi*x).tan(), (tau/2).tan(), 1/(tau/2).cos()
        period = 3*tau+2*ii*(z+sec).log()+ii*((q+z).log()-(q-z).log())-2*pi
        ft = 3+ii*(sec+q*sec**2/(q-z)/(q+z))
        fx = 2*pi*ii*z*(1+q*q)/(q-z)/(q+z)
        tp, tm = (pi*x+tau/2).tan(), (pi*x-tau/2).tan()
        bx = (pi*x+tau/2).cos().log()+(pi*x-tau/2).cos().log()-2*(pi*x).sin().log()
        bxx, bxt = -pi*(tp+tm+2*q), (tm-tp)/2
        return ([period, bx+data['px']],
                [[fx, ft], [bxx+data['pxx'], bxt]], data, (bxx, bxt, ii*ft/(2*pi)))

    def mp_system(x, tau, y):
        X, Y = mp.exp(2j*mp.pi*x), mp.exp(2j*mp.pi*y)
        al, be = 1/X-1, 1/Y-1
        U = (1+al-be-mp.sqrt(1-2*(al+be)+(al-be)**2))/2
        px = -mp.log(U)+mp.log(1-X*U)-mp.log(1-X)-mp.pi*1j
        q, z, sec = 1/mp.tan(mp.pi*x), mp.tan(tau/2), 1/mp.cos(tau/2)
        per = 3*tau+2j*mp.log(z+sec)+1j*(mp.log(q+z)-mp.log(q-z))-2*mp.pi
        bx = mp.log(mp.cos(mp.pi*x+tau/2))+mp.log(mp.cos(mp.pi*x-tau/2))-2*mp.log(mp.sin(mp.pi*x))
        return per, bx+px

    # Same rational preconditioner as the independently audited disk
    # certificate. Its validity here is checked on every new interval.
    C = [[point('-.012459042950055255651267420891', '.009121085447815058535390706888'),
          point('-.030322991884195644218839259185', '-.022730223128523958826095306578')],
         [point('.222750256842225811720371833986', '-.117735701411284707218221686158'),
          point('.057309470071241114644219436946', '.078282475605306592775433429801')]]

    # Recheck the center in a tiny polydisk rather than taking a rounded
    # diagnostic derivative as input to the finite-entrance estimates.
    central_centers = [point('.177337918569469382175948562048', '.101358689576302370861575311618'),
                       point('1.533800710765884206016520588964', '-.978955098405739999074096803416')]
    cr = rat('1e-10')
    central_boxes = [acb(z.real+arb(0, cr), z.imag+arb(0, cr)) for z in central_centers]
    cres = system(*central_centers, xh)[0]
    _, cjac, cd, _ = system(*central_boxes, xh)
    center_checks = []
    for row in range(2):
        con = sum(abs(acb(int(row == col))-sum(C[row][k]*cjac[k][col] for k in range(2)))
                  for col in range(2))
        disp = abs(sum(C[row][k]*cres[k] for k in range(2)))
        assert con < rat(Q(1,1000)) and disp+con*cr < cr
        center_checks.append({'contraction': str(con), 'self_map_margin': str(cr-disp-con*cr)})
    assert abs(cd['py'].real) < rat(Q(113,10000))
    assert abs(cd['py']/k0) < rat(Q(69,2500))
    center_derivatives = {'phase_gradient': str(cd['py']),
                          'absolute_real_slope_bound': '113/10000',
                          'normalized_gradient_modulus_bound': '69/2500',
                          'Newton_checks': center_checks}

    cells = []
    base_width = Q(1, 25*args.mesh)
    pending = [(Q(-1, 50)+j*base_width, Q(-1, 50)+(j+1)*base_width)
               for j in reversed(range(args.mesh))]
    visited = 0
    while pending:
        lo, hi = pending.pop()
        width = hi-lo
        j = visited
        visited += 1
        assert visited <= 10000, 'Explicit interval budget exhausted'
        mid = (lo+hi)/2
        ymp = mp.mpf(1)/6+1j*mp.log(2)/(2*mp.pi)+mp.mpf(mid.numerator)/mid.denominator
        xm, tm = mp.findroot(lambda x, tau: mp_system(x, tau, ymp),
                            (.1773+.1013j, 1.534-.979j))
        centers_q = [[str(Q(str(z.real))), str(Q(str(z.imag)))] for z in [xm, tm]]
        centers = [point(*parts) for parts in centers_q]
        yc, ybox = xh+rat(mid), xh+interval(lo, hi)
        pr = rat(width)/2
        radii = [rat(Q(7, 20))*pr, pr]
        boxes = [acb(z.real+arb(0, r), z.imag+arb(0, r)) for z, r in zip(centers, radii)]
        residual = system(*centers, yc)[0]
        variation = abs(retained(centers[0], ybox)['pxy'])*pr
        _, J, data, (bxx, bxt, ftt) = system(*boxes, ybox)
        contractions, self_margins = [], []
        for row in range(2):
            contraction = sum(abs(acb(int(row == col))-sum(C[row][k]*J[k][col] for k in range(2)))*radii[col]
                              for col in range(2))/radii[row]
            displacement = abs(sum(C[row][k]*residual[k] for k in range(2)))+abs(C[row][1])*variation
            margin = radii[row]-displacement-contraction*radii[row]
            assert contraction < rat(Q(1, 4)), (j, row, contraction)
            assert margin > 0, (j, row, margin)
            contractions.append(str(contraction))
            self_margins.append(str(margin))

        wire, tau = boxes
        indices = [ii*data[name].log()/(2*pi) for name in ['U', 'V']]
        margins = {}

        def positive(name, value):
            assert value > 0, (j, name, value)
            margins[name] = str(value)

        for name, value, re_lo, re_hi, im_lo, im_hi in [
                ('wire', wire, Q(14,100), Q(20,100), Q(9,100), Q(12,100)),
                ('cap', tau, Q(0), Q(9,5), Q(-1), Q(-97,100)),
                ('first index', indices[0], Q(1,4), Q(9,20), Q(-3,100), Q(3,100)),
                ('second index', indices[1], Q(1,4), Q(9,20), Q(-3,100), Q(3,100))]:
            positive(name+' lower real', value.real-rat(re_lo))
            positive(name+' upper real', rat(re_hi)-value.real)
            positive(name+' lower imaginary', value.imag-rat(im_lo))
            positive(name+' upper imaginary', rat(im_hi)-value.imag)
        for name in ['X', 'Y']:
            positive(name+' first quadrant real', data[name].real)
            positive(name+' first quadrant imaginary', data[name].imag)
            positive(name+' modulus below one', 1-abs(data[name]))
        for name in ['U', 'V']:
            positive(name+' lower-left real', -data[name].real)
            positive(name+' lower-left imaginary', -data[name].imag)
        positive('square root upper branch', data['delta'].imag)
        positive('first denominator radius', 1-abs(data['X']*data['U']))
        positive('second denominator radius', 1-abs(data['Y']*data['V']))
        positive('total real index above half', sum(v.real for v in indices)-rat(Q(1,2)))
        positive('total real index below one', 1-sum(v.real for v in indices))
        for name, value in [('first', indices[0]-wire), ('second', indices[1]-ybox)]:
            positive(name+' real index-wire positive', value.real)
            positive(name+' real index-wire below half', rat(Q(1,2))-value.real)
        q, z, sec = 1/(pi*wire).tan(), (tau/2).tan(), 1/(tau/2).cos()
        for name, value in [('q+tan', q+z), ('q-tan', q-z), ('sec+tan', z+sec),
                            ('cos+', (pi*wire+tau/2).cos()),
                            ('cos-', (pi*wire-tau/2).cos()), ('sin', (pi*wire).sin())]:
            positive('cap log '+name, value.real)
        total_second = bxx-bxt*bxt/ftt+data['pxx']
        outgoing = data['pyy']-data['pxy']**2/total_second
        positive('negative composed wire Hessian above 20', -total_second.real-20)
        if not -outgoing.real > rat(Q(93,10)):
            assert width > base_width/256, ('curvature refinement limit', lo, hi)
            mid = (lo+hi)/2
            pending.extend([(mid, hi), (lo, mid)])
            continue
        positive('negative outgoing real Hessian above 9.3', -outgoing.real-rat(Q(93,10)))
        positive('outgoing Hessian modulus below 16', 16-abs(outgoing))
        positive('wire response modulus below .22', rat(Q(11,50))-abs(data['pxy']/total_second))
        cells.append({'output_interval': [str(lo), str(hi)], 'centers': centers_q,
                      'radii': list(map(str, radii)), 'Newton_contractions': contractions,
                      'Newton_self_map_margins': self_margins,
                      'coordinate_enclosures': [z.str(40, more=True) for z in [wire, tau]+indices],
                      'coordinate_parts': [[z.real.str(40, more=True), z.imag.str(40, more=True)]
                                           for z in [wire, tau]+indices],
                      'outgoing_phase_gradient': data['py'].str(40, more=True),
                      'outgoing_phase_Hessian': outgoing.str(40, more=True),
                      'composed_wire_Hessian': total_second.str(40, more=True),
                      'margins': margins})
    assert cells[0]['output_interval'][0] == '-1/50'
    assert cells[-1]['output_interval'][1] == '1/50'
    assert all(cells[j]['output_interval'][1] == cells[j+1]['output_interval'][0]
               for j in range(len(cells)-1))
    deps = ['notes/research_three_phase_graph_transform.md',
            'notes/research_three_cap_first_attachment.md',
            'notes/research_three_vertex_joint_concavity.md',
            'notes/research_three_vertex_central_index_chart.md']
    result = {'status': 'passed', 'precision_bits': args.precision, 'mesh': args.mesh,
              'cell_count': len(cells), 'visited_cells': visited, 'cells': cells,
              'center_derivatives': center_derivatives,
              'scope': 'Actual critical branch on the real output interval [-.02,.02], with rational parameter cover, complex Newton self-maps, original branch tests, coordinate boxes and nondegenerate Schur Hessians. No complementary source contour or phase-class invariant bound is asserted.',
              'branch_gluing': 'The roots lie in the convex original phase chamber: arbitrary-height joint-index Hessian Lemma1 and the unchanged cap Hessian box give strictly accretive symmetric joint Hessian and hence injective complex gradient. Every overlapping parameter neighborhood therefore selects the same root; the center agrees with the previously certified branch.',
              'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependencies_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},
              'elapsed_seconds': time.monotonic()-start}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in ['status', 'precision_bits', 'cell_count', 'elapsed_seconds']}, indent=2))


if __name__ == '__main__':
    main()
