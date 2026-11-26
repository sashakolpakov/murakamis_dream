#!/usr/bin/env python3
"""Outward bounds for the first entrance source on a larger real interval.

The certified central critical point is reused with its recorded enclosure.
A separate full rectangular cover bounds the actual kernel's real curvature.
No sampled value or numerical optimizer is used for acceptance.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=192)
    ap.add_argument('--output', type=Path,
                    default=ROOT/'repro/results/research-three-first-entrance-real-budgets.json')
    args = ap.parse_args()
    ctx.prec = args.precision
    pi, ii = arb.pi(), acb(0, 1)

    def a(value):
        value = Q(value)
        return arb(value.numerator)/value.denominator

    def interval(lo, hi):
        return arb(a((lo+hi)/2), a((hi-lo)/2))

    xh = acb(arb(1)/6, arb(2).log()/(2*pi))
    k0 = 4*pi/21*(2*arb(3).sqrt()-3*ii)
    kmag, alpha, D = abs(k0), k0.real, 5+arb(21).sqrt()

    def kernel(x, y):
        X, Y = (2*pi*ii*x).exp(), (2*pi*ii*y).exp()
        al, be = 1/X-1, 1/Y-1
        delta = 1-2*(al+be)+(al-be)**2
        assert delta.imag > 0
        root = delta.sqrt()
        U, V = (1+al-be-root)/2, (1-al+be-root)/2
        assert U.real < 0 and U.imag < 0 and V.real < 0 and V.imag < 0
        assert abs(X*U) < 1 and abs(Y*V) < 1
        Ux = (-2*pi*ii/X)*(1-U)/root
        xx = -Ux/(U*(1-X*U))+2*pi*ii*X*(1-U)/((1-X)*(1-X*U))
        py = -V.log()+(1-Y*V).log()-(1-Y).log()-pi*ii
        return xx, py

    author_path = ROOT/'repro/results/research-three-first-entrance-critical.json'
    replay_path = ROOT/'repro/results/research-three-first-entrance-critical-replay.json'
    author, replay = map(lambda p: json.loads(p.read_text()), (author_path, replay_path))
    assert author['status'] == replay['status'] == 'passed'
    assert replay['artifact_sha256'] == sha256(author_path.read_bytes()).hexdigest()
    for path, digest in author['dependencies_sha256'].items():
        assert sha256((ROOT/path).read_bytes()).hexdigest() == digest, path
    assert author['script_sha256'] == sha256((ROOT/'experiments/certify_three_first_entrance_critical.py').read_bytes()).hexdigest()
    assert replay['script_sha256'] == sha256((ROOT/'experiments/replay_three_first_entrance_critical.py').read_bytes()).hexdigest()
    zc = acb(*map(arb, author['center']['coordinate_parts'][2]))
    displacement = zc-xh
    _, derivative = kernel(zc, xh)
    drift_lower = (k0*D*displacement**2).real/2-a('.3')*kmag*abs(displacement)**2
    checks = []

    def positive(name, value):
        assert value > 0, (name, str(value))
        checks.append({'name': name, 'positive_margin': str(value)})

    positive('center action drift exceeds minus .000066', drift_lower+a('.000066'))
    positive('center real phase slope below .00215', a('.00215')-abs(derivative.real))
    positive('actual normalized center gradient below .0057', a('.0057')-abs(derivative/k0))

    # This is an exact multiplicity-one rectangular partition of both real
    # parameters. Every accepted cell encloses its entire closed rectangle.
    curvature_count = 0
    curvature_minimum = None
    for j in range(320):
        tlo, thi = Q(-1, 50)+Q(j, 8000), Q(-1, 50)+Q(j+1, 8000)
        for k in range(144):
            wlo, whi = Q(-9, 1000)+Q(k, 8000), Q(-9, 1000)+Q(k+1, 8000)
            xx, _ = kernel(xh+interval(tlo, thi), xh+interval(wlo, whi))
            loss = -xx.real
            assert loss > a('9.4'), (j, k, str(loss))
            curvature_minimum = loss.lower() if curvature_minimum is None else min(curvature_minimum, loss.lower())
            curvature_count += 1
    assert curvature_count == 320*144
    assert Q(-1, 50)+Q(320, 8000) == Q(1, 50)
    assert Q(-9, 1000)+Q(144, 8000) == Q(9, 1000)

    R, W, P1 = a('.005'), a('.009'), a('.0113')
    # The cubic phase estimate is used only on |input|<=.005,
    # |output|<=.009, which lies in its proved symmetric domain.
    positive('both real endpoint derivatives point outward',
             a('9.3')*R-P1+5*alpha*R-2*alpha*W-9*kmag*(R+W)**2)
    positive('real annulus combined curvature exceeds18', a('9.3')+a('9.4')-18)
    Breal = a('.000066')+a('.00215')*W+a('4.9')*W**2
    assert Breal.contains(a(Q(1929, 4_000_000)))
    positive('middle principal input gap above .000019',
             a('6.15')*a('.01')**2-P1*a('.01')-Breal-a('.000019'))
    positive('absolute input error gap above .000117', a('.0006')-Breal-a('.000117'))
    positive('far input gap above .000267', a('.00075')-Breal-a('.000267'))
    positive('middle quadratic loss increases', 2*a('6.15')*a('.01')-P1)
    positive('restored source error below real output floor',
             a('1.9113')+a('.646')-Breal-a('2.38'))

    B2 = a('.000066')+P1**2/(4*a('2.95'))
    H = a('.0057')
    positive('sharper global real envelope slack below .000077', a('.000077')-B2)
    # The stronger A=1.45 comparison implies every weaker A in [0,1.45].
    # Both sides use cap .03 here. The comparison increases with distance.
    positive('sharper full-period envelope holds already from radius .005',
             kmag*H*R+a('.05')*R**2-B2)
    positive('local source curvature dominates global coefficient1.45', 4-a('1.45'))

    paths = [
        'notes/research_three_first_entrance_real_extension.md',
        'notes/research_three_first_entrance_source.md',
        'notes/research_three_prepared_cap_real_extension.md',
        'notes/research_three_vertex_input_rectangle.md',
        'notes/research_three_vertex_two_wire_large_cap_bound.md',
        'notes/research_three_vertex_large_cap_height_bound.md',
        'notes/research_three_phase_graph_transform.md',
        'notes/research_three_vertex_real_input_union.md',
        'notes/research_three_first_entrance_real_critical.md',
        'repro/results/research-three-vertex-real-input-union.json',
        'repro/results/research-three-vertex-real-input-union-replay.json',
        'repro/results/research-three-first-entrance-real-critical.json',
        'repro/results/research-three-first-entrance-real-critical-replay.json',
        str(author_path.relative_to(ROOT)), str(replay_path.relative_to(ROOT)),
    ]
    result = {
        'status': 'passed', 'precision_bits': ctx.prec,
        'scalar_comparison_count': len(checks), 'scalar_comparisons': checks,
        'kernel_real_curvature_cells': curvature_count,
        'exact_real_parameter_cover': [['-1/50', '1/50'], ['-9/1000', '9/1000']],
        'kernel_real_curvature_lower': str(curvature_minimum),
        'center_action_drift_lower': str(drift_lower),
        'center_phase_derivative': str(derivative),
        'actual_normalized_center_gradient': str(abs(derivative/k0)),
        'real_output_cost': str(Breal), 'sharper_global_slack': str(B2),
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependencies_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'scope': 'Real complementary budgets and actual center sharpening for the original first entrance source. The actual union-domain kernel and real critical V sectors are separate proved inputs. No repeatable source induction is asserted.'
    }
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(f'Passed {len(checks)} scalar comparisons and {curvature_count} real curvature boxes.')
    print('Actual normalized center gradient:', result['actual_normalized_center_gradient'])
    print('Real output cost:', Breal)
    print('Sharper global slack:', B2)


if __name__ == '__main__':
    main()
