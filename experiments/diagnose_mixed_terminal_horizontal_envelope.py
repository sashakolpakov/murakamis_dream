#!/usr/bin/env python3
"""Four canonical suffixes and log-only lower tests of a terminal majorant.

The existing source theorem is an upper bound. A positive value here
obstructs that horizontal-envelope method only, never the original source.
No dilogarithm, target optimizer, subdivision, alternate seed, or retry.
"""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_horizontal_envelope_diagnostic.md'
PINNED = {'notes/research_mixed_terminal_horizontal_envelope_diagnostic.md': 'ea1e6d1daf4b8e3822a198de1f63f4f211061761af8bdd01d641b4d8f930ad72', 'notes/research_mixed_terminal_concave_profile_envelope.md': '6d71c0470a9fe1598cdc46459ffcda98f807eb84c1be8bc2810517706a744ddd', 'notes/research_mixed_terminal_selected_height_rows.md': 'f282382e106a7669592ae5bf2755c307613a72780b957e3966e5b21ba9bb03e3', 'notes/research_mixed_terminal_three_selected_height_completion.md': 'e3fea31226612be459f23e8cec8773503e562799cced20b36efcc0e4cd70e186', 'notes/research_mixed_terminal_four_selected_height_completion.md': '5b688d2adf67895f430a2fef77a5d98fcb8ac74846ebc2bbe1027cd6e3414127', 'notes/research_mixed_terminal_height_tangent_sign.md': '6c3279537ff354ca91d654292ac4154745b50dbeb967480bf1416d582dca185c', 'notes/research_mixed_full_unselected_plateau.md': 'abd5dcddc9ed5057b6658bd8b7b60922540fd664c0c5c794135b19c1678c62a6', 'notes/research_mixed_prefix_residual_localization.md': '5590b49394d112be5f5d23e7f20c31225bce8f1c19e6d3fd1dc3aa1ce40f0434', 'notes/research_mixed_open_word_hessian.md': '21556711a3ac410ce7d3e4dda0d3a6395cd7ee2a69993d82f5f8325c6e7dad23', 'notes/research_mixed_open_word_critical_localization.md': 'a3f8a0f781abd43f8ca17321171081ba37c91b284f83f22a4f7ae34e270424fa', 'notes/research_mixed_open_word_endpoint_rectangles.md': 'ac5603badc00d42e98d17a1c5948cae011a6abd991d5249fa61d4224a829ad07', 'notes/research_mixed_cyclic_critical_localization.md': 'ccb8b144e6068c434059b707cd13d9aed8bb88a40e7fa0cf0e6bc655bff7fa71', 'notes/research_mixed_cyclic_critical_height_bounds.md': '39dff66057a82bc974aa38d65e39a13f508024440bd4e3936783c1c37fe290a9', 'notes/research_mixed_second_selected_horizontal_concavity.md': 'dac208b242a8dd24f1ce0c29e15775bd343554e0cb0141e2ad84c0fe64312ca8', 'notes/research_mixed_plateau_window_concave_profiles.md': 'ba03fd9804c63274b8015532d3c176a044e9b7f0bdd34d69331f420522c88d19', 'repro/results/research-mixed-open-word-critical-localization.json': 'ac2991d4cd5b7a78d202a237efebf98a9ad7ab77b6bacc4ab82568b8aa3cdad5', 'repro/results/research-mixed-open-word-critical-localization-replay.json': '2b5d91f8fbfa860d978f7b2076270b33bbe40d7410d39e91c9733e41b03ec247', 'repro/results/research-mixed-cyclic-block-localization.json': '757108a2f2ef6d8d468584abcba8585772aa4ea6b59d0d2b424253a63e7f32de', 'repro/results/research-mixed-cyclic-block-localization-replay.json': 'bdfda6be30db2aa0bdd3673b7165a3345a42dfc5566d401de86878d4176ad745', 'repro/results/research-mixed-cyclic-block-boundary-images.json': '83edaffd36f7fbcb37a41c06ff6f31572ca2936487cae9fb48e66e8c20b8fc35', 'repro/results/research-mixed-cyclic-block-boundary-images-replay.json': '897da8260b13a8f794bde41a8ee64421ce14eb74b211075103295456c3e0ccd1', 'repro/results/research-mixed-terminal-three-alias-reserve.json': '039094505d49f8736485224fceaf280de836bba635301b1fa669e51c2d9fd483', 'repro/results/research-mixed-terminal-four-alias-reserve.json': '6ff887ab81798ea4e237dfaf39cbd99f17cfecda367bc4e551f92ea61da351d0', 'notes/research_mixed_terminal_four_coupled_source_continuation.md': 'ee52ddb19be76ed0147a2e23309f2feafd812b4f8758eecabdd3096b8f0b0830', 'notes/research_mixed_terminal_four_oriented_source_continuation.md': '24f47fef461d375afa59a338476a1f19d901b29e1d461208440771cc8926eca9', 'notes/research_mixed_endpoint_inverse_filter.md': '20a73200b9180b0e69a3307e338a4b841c3a9ff6c583ce63b23d2426859c83da'}
NAMES = ('e', 'xi', 't', 'a', 's')
RADIUS = F(1, 10**30)
HEIGHTS = (F(0), F(1, 100), F(7, 500))
CENTERS = ((F(7, 20), -F(1, 100)), (F(3, 10), -F(13, 250)))
INITIAL = (
    (('.407', '.009'), ('.230', '.063'), ('.335', '-.025'),
     ('.30', '-.052'), ('.30', '-.052')),
    (('.348', '-.035'), ('.225', '.036'), ('.298', '-.064'),
     ('.30', '-.052'), ('.30', '-.052')),
)
COMMON = {
    'e': ('.33', '.47', '-.09', '.08'),
    'xi': ('.21', '.25', '.01', '.10'),
    't': ('.23', '.45', '-.12', '.12'),
    'a': ('.23', '.45', '-.12', '.12'),
    's': ('.23', '.45', '-.12', '.12'),
}
TYPED = (
    {'e': ('.376', '.438', '-.019', '.037'),
     'xi': ('.218', '.242', '.049', '.077'),
     't': ('.278', '.391', '-.072', '.021')},
    {'e': ('.333', '.363', '-.051', '-.019'),
     'xi': ('.217', '.234', '.027', '.045'),
     't': ('.246', '.350', '-.108', '-.020')},
)


def sha(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            digest.update(block)
    return digest.hexdigest()


def bindings():
    if not PINNED:
        raise ValueError('unfinished fixed protocol bindings')
    out = dict(PINNED)
    for name, expected in out.items():
        if sha(ROOT/name) != expected:
            raise ValueError('changed fixed input: '+name)
    out[str(Path(__file__).resolve().relative_to(ROOT))] = sha(Path(__file__))
    return out


def gradient(values, outside, epsilon, xp, log, sin, cos, pi, ii):
    e, xi, t, a, s = values
    half = xp(1)/2
    def jp(z):
        return log(2*sin(pi*z))
    return [
        -jp(e-xi)+jp(e+t)-epsilon*jp(e)
        +ii*pi*(xi-t+epsilon*(e-half)),
        2*log(cos(pi*xi))+log(sin(pi*(e-xi)))-3*log(sin(pi*xi))+ii*pi*e,
        jp(e+t)+jp(t+a)-(2+epsilon)*jp(t)
        +ii*pi*(a-e+epsilon*(t-half)),
        jp(a+s)+jp(t+a)-3*jp(a)+ii*pi*(t-s+a-half),
        jp(a+s)+jp(s+outside)-3*jp(s)+ii*pi*(outside-a+s-half),
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    inputs = bindings()
    # No arithmetic provider is imported before all proof/data bindings pass.
    import mpmath as mp
    from flint import acb, arb, ctx
    ctx.prec = 256
    pi, ii = arb.pi(), acb(0, 1)
    counts = {'reference_proposals': 0, 'original_residual_evaluations': 0,
              'marginal_enclosures': 0, 'lower_tests': 0,
              'dilogarithm_evaluations': 0, 'target_optimizations': 0,
              'finite_quantum_sums': 0, 'parameter_subdivisions': 0,
              'alternate_seeds': 0, 'precision_retries': 0}

    def rat(x):
        x = F(x)
        return arb(x.numerator)/arb(x.denominator)

    def ends(x):
        if not x.is_finite():
            raise ValueError('nonfinite interval')
        return F(str(x.lower().fmpq())), F(str(x.upper().fmpq()))

    def record_pair(lo, hi):
        return {'finite': True, 'lower_rational': str(lo), 'upper_rational': str(hi)}

    def record(x):
        return record_pair(*ends(x))

    def crecord(x):
        return {'real': record(x.real), 'imag': record(x.imag)}

    def ball(lo, hi):
        out = arb(rat((lo+hi)/2), rat((hi-lo)/2).upper())
        actual_lo, actual_hi = ends(out)
        if not (actual_lo <= lo <= hi <= actual_hi):
            raise ValueError('Arb conversion failed exact endpoint containment')
        return out

    def cp(pair):
        return acb(rat(pair[0]), rat(pair[1]))

    def check_domain(center, epsilon):
        checks, squares = {}, {}
        for name, (x, y) in zip(NAMES, center):
            real, imag = (x-RADIUS, x+RADIUS), (y-RADIUS, y+RADIUS)
            squares[name] = {'real': record_pair(*real), 'imag': record_pair(*imag)}
            lo, hi, low, high = map(F, COMMON[name])
            common = lo < real[0] <= real[1] < hi and low < imag[0] <= imag[1] < high
            if not common:
                raise ValueError('localization square outside common product: '+name)
            typed_bounds = TYPED[epsilon].get(name, ('.24', '.36', '-.102', '-.001'))
            lo, hi, low, high = map(F, typed_bounds)
            typed = lo < real[0] <= real[1] < hi and low < imag[0] <= imag[1] < high
            if not typed:
                raise ValueError('localization square outside typed source rectangle: '+name)
            checks[name] = {'common_product_verified': True, 'typed_rectangle_verified': True,
                            'common_bounds': COMMON[name], 'typed_bounds': typed_bounds}
        # The completed own-four source also retains the necessary coupled
        # input scope: reduced disk, oriented floor, and inverse feasibility.
        # Original equations reconstruct the opposite/external legs as s,b;
        # the latter is exactly a reduced typed-disk center.
        for name, disk_type in (('a', 1), ('s', 1), ('t', epsilon)):
            z = center[NAMES.index(name)]
            cx, cy = CENTERS[disk_type]
            rr = F(83, 1000) if disk_type == 0 else F(3, 50)
            distance = (abs(z[0]-cx)+RADIUS)**2+(abs(z[1]-cy)+RADIUS)**2
            if not distance < rr**2:
                raise ValueError('localization square not in original typed disk: '+name)
            checks[name]['typed_disk_squared_distance_upper_rational'] = str(distance)
            checks[name]['typed_disk_radius_squared_rational'] = str(rr**2)
        if epsilon == 1:
            a_floor = center[NAMES.index('a')][0]-RADIUS
            if not a_floor > F(259, 1000):
                raise ValueError('oriented own-four incoming floor not certified')
            checks['a']['oriented_real_floor_rational'] = str(a_floor)
            checks['a']['oriented_threshold_rational'] = '259/1000'
        return checks, squares

    pi_lo, pi_hi = ends(pi)
    mu_lower = F(6, 49)*pi_lo
    cases = []
    for beta, epsilon in itertools.product((0, 1), repeat=2):
        row = {'beta': beta, 'epsilon': epsilon,
               'outside_coordinate': list(map(str, CENTERS[beta])),
               'initial_coordinates': [list(z) for z in INITIAL[epsilon]],
               'status': 'inconclusive', 'suffix_realization_claimed': False,
               'source_comparison_claimed': False}
        try:
            counts['reference_proposals'] += 1
            with mp.workdps(80):
                b = mp.mpc(*(mp.mpf(v.numerator)/v.denominator for v in CENTERS[beta]))
                initial = tuple(mp.mpc(x, y) for x, y in INITIAL[epsilon])
                def function(*values):
                    return gradient(values, b, epsilon, mp.mpf, mp.log,
                                    mp.sin, mp.cos, mp.pi, mp.j)
                solution = mp.findroot(function, initial, maxsteps=30,
                                       tol=mp.mpf('1e-55'), verify=True)
                printed = [[mp.nstr(z.real, 60), mp.nstr(z.imag, 60)] for z in solution]
            center = [[F(v) for v in z] for z in printed]
            row['proposed_centers'] = printed
            checks, squares = check_domain(center, epsilon)
            row['domain_checks'], row['coordinate_enclosures'] = checks, squares
            counts['original_residual_evaluations'] += 1
            residual = gradient(list(map(cp, center)), cp(CENTERS[beta]), epsilon, arb,
                                lambda z: z.log(), lambda z: z.sin(), lambda z: z.cos(), pi, ii)
            r2 = sum(max(abs(v) for v in ends(part))**2
                     for value in residual for part in (value.real, value.imag))
            threshold = mu_lower**2*RADIUS**2
            row.update(original_gradient_residual=list(map(crecord, residual)),
                       residual_squared_upper_rational=str(r2),
                       residual_threshold_rational=str(threshold),
                       accretivity_lower_rational=str(mu_lower), radius_rational=str(RADIUS))
            if not r2 < threshold:
                raise ValueError('original residual does not certify prescribed radius')
            row['canonical_reference_certified'] = True
            q = {name: acb(ball(F(z['real']['lower_rational']), F(z['real']['upper_rational'])),
                           ball(F(z['imag']['lower_rational']), F(z['imag']['upper_rational'])))
                 for name, z in squares.items()}
            def gp(z):
                if not (z.real > 0 and z.real < 1):
                    raise ValueError('marginal argument outside original regular strip')
                return (1-(-2*pi*ii*z).exp()).log()
            counts['marginal_enclosures'] += 1
            p = gp(q['a']+q['t'])-3*gp(q['a'])/2+2*pi*ii*q['t']
            row['allocated_terminal_marginal'] = crecord(p)
            row['actual_marginal_input_enclosures'] = {name: crecord(q[name]) for name in ('a', 't')}
            p_lo, p_hi = ends(p.imag)
            # The exact saved localization endpoints suffice for Delta. The
            # Arb marginal was evaluated on outward boxes containing them.
            c_lo, c_hi = [F(squares['a']['imag'][key]) for key in ('lower_rational', 'upper_rational')]
            tests = []
            for h in HEIGHTS:
                delta = (h-c_hi, h-c_lo)
                products = [d*pv for d in delta for pv in (p_lo, p_hi)]
                lower = min(products)-h*pi_hi
                upper = max(products)-h*pi_lo
                tests.append({'height_rational': str(h), 'delta': record_pair(*delta),
                              'product_corner_rationals': list(map(str, products)),
                              'L': record_pair(lower, upper),
                              'positive_majorant_trial_proved': lower > 0})
                counts['lower_tests'] += 1
            row.update(lower_tests=tests, status='canonical reference and lower tests certified',
                       all_allowed_heights_obstructed=(F(tests[0]['L']['lower_rational']) > 0
                                                     and F(tests[2]['L']['lower_rational']) > 0))
        except Exception as error:
            row['error'] = type(error).__name__+': '+str(error)
        cases.append(row)
        print(json.dumps({'beta': beta, 'epsilon': epsilon, 'status': row['status'],
                          'all_allowed_heights_obstructed': row.get('all_allowed_heights_obstructed'),
                          'error': row.get('error')}), flush=True)
    changed = [name for name, digest in inputs.items() if sha(ROOT/name) != digest]
    result = {'status': 'complete fixed diagnostic' if not changed and all(
                  row['status'] == 'canonical reference and lower tests certified' for row in cases)
                  else 'inconclusive fixed diagnostic',
              'cases': cases, 'counts': counts, 'precision_bits': 256,
              'proposal_precision_digits': 80, 'proposal_maxsteps': 30,
              'proposal_tolerance': '1e-55', 'proposal_saved_digits': 60,
              'pi': record(pi), 'heights_rational': list(map(str, HEIGHTS)),
              'input_sha256': inputs, 'changed_inputs': changed,
              'whole_source_sign_claimed': False, 'uniform_domain_sign_claimed': False,
              'full_378_profile_pass_performed': False}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as stream:
        stream.write(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'record_sha256': sha(args.output)}), flush=True)


if __name__ == '__main__':
    main()
