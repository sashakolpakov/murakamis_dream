#!/usr/bin/env python3
"""One fixed proposal, original residual and action enclosure for prepared 34.

Existence is inherited from the completed Fourier boundary update. No
root-existence search, input refinement, retry, face or alias evaluation.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform
import sys
import traceback


ROOT = Path(__file__).resolve().parents[1]
THEORY = 'notes/research_mixed_prepared_cap_action_enclosure.md'
PROTOCOL = 'notes/research_mixed_prepared_cap_action_evaluation.md'
SOURCE = 'repro/results/research-three-four-source-interface.json'
SOURCE_WRITER = 'experiments/check_three_four_source_interface.py'
BOUNDARY = 'repro/results/research-mixed-fourier-boundary-update.json'
BOUNDARY_WRITER = 'experiments/check_mixed_fourier_boundary_update.py'
OUTPUT = ROOT/'repro/results/research-mixed-prepared-cap-action.json'
PINNED = {
    'notes/research_mixed_prepared_cap_action_enclosure.md':
        '8bbe001bf4c5093cd8ddf209a266d55da9a64521b2aa3b0562e9351c5d1a5e55',
    'notes/research_mixed_prepared_cap_action_evaluation.md':
        '157fe4a6131f771a736bc787434c92200f1681e3081529433f502f3402497ffb',
    'repro/results/research-three-four-source-interface.json':
        '9218011f3f5d41ff15835f74ccf83ccfeb266beea112c67607fa1eaef96ba9dd',
    'experiments/check_three_four_source_interface.py':
        'e9d009fdf8712a7577bd9220c8bbf6c2f8fd1d3eefece969cad45357d8a45f91',
    'repro/results/research-mixed-fourier-boundary-update.json':
        '5d4cb057cb82ca4fff826ad768012480fd6f51afe66d3f5c632e48983cf17514',
    'experiments/check_mixed_fourier_boundary_update.py':
        '5017a53b6417630f1cab1e9c4be3f71d3ad24256af1ca67a8edd8faf0be0b1cc',
    'notes/research_mixed_fourier_boundary_update_protocol.md':
        'cc8176390334bf39e0c9cf1894fbba0ed520eee811eaf26835f3010e4e6feffd',
    'notes/research_mixed_fourier_boundary_update.md':
        '9ff05c7f6eb759d53a3717e57b475c58904ccd35d5c232e1abdbe8b35ec49f74',
    'notes/research_mixed_fourier_boundary_critical_existence.md':
        'f7a910f0a2c67701a5dc5c0eb3e5fe8c6dcf20d6a83dbd4876c2363a46fabda6',
    'notes/research_mixed_prepared_three_four_cap_source.md':
        'b875087d250f0a1178f46518c0ba67472aefa739f8bdb8ccf352c5c01edea104',
    'notes/research_mixed_prepared_three_four_cap_critical_curve.md':
        'e29f73574faba8f7f7f7196e63dadbd169287cf29cd72904a8257ebb54d2184f',
    'notes/research_mixed_prepared_cap_typed_height_rectangle.md':
        'a422d9e21071411b6ce30e516f2c6636c7c7f3512e96137aa43a01a76a9430a2',
    'notes/research_mixed_endpoint_action_calibration.md':
        '7e037e72fdf623dd754175ade12663fe90846dd5b137dc028104622a652c392d',
    'notes/research_mixed_prefix_residual_localization.md':
        '5590b49394d112be5f5d23e7f20c31225bce8f1c19e6d3fd1dc3aa1ce40f0434',
    'notes/research_mixed_open_word_hessian.md':
        '21556711a3ac410ce7d3e4dda0d3a6395cd7ee2a69993d82f5f8325c6e7dad23',
    'notes/research_mixed_contracted_pair_enlarged_rectangle.md':
        '597761e942e2956554fe4f25d22de0156838a880e37c04e4fa8fe843e087f0fc',
    'notes/research_three_vertex_mixed_reference_packet.md':
        '71e5b3c4ad29bdfe49d4fb1c95dc658e86f19ff2656621b6bcf495222b59b849',
    'notes/research_mixed_endpoint_cap_rectangle.md':
        '9211d45bdd031c908690a723ebcd4b40a34fed90f44858301a809ee5901c15e8',
}
REQUIRED_PINS = (THEORY, PROTOCOL, SOURCE, SOURCE_WRITER, BOUNDARY,
                 BOUNDARY_WRITER,
                 'notes/research_mixed_fourier_boundary_critical_existence.md')
NAMES = ('u', 's', 't', 'p', 'q')
ARG_NAMES = ('half_minus_u', 'u', 's_minus_u', 's_plus_t',
             't_plus_p', 'p_plus_q', 't', 'p', 'q')
INITIAL = tuple(tuple(map(F, pair)) for pair in
    (('.230', '.063'), ('.407', '.009'), ('.3345', '-.0255'),
     ('.30', '-.052'), ('.30', '-.052')))
DOMAINS = tuple(tuple(map(F, row)) for row in
    (('.21', '.25', '.01', '.10'), ('.33', '.47', '-.09', '.08'),
     ('.23', '.45', '-.12', '.12'), ('.23', '.45', '-.12', '.12'),
     ('.23', '.45', '-.12', '.12')))
STEPS = 32
PROPOSAL_DPS = 80
PRECISION = 256
INSET = F(1, 10**8)
GRID = 10**50
RADIUS = F(1, 10**16)
MU_LOWER = F(471, 1225)
ACTION_ERROR = 60*RADIUS**2
EXPECTED_PROPOSAL = {'exp': 288, 'log': 321}
EXPECTED_ANALYTIC = {'pi': 1, 'exp': 9, 'log': 11, 'dilog': 11}


class GuardFailure(Exception):
    """A prescribed containing interval did not verify a domain guard."""


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def sha(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            digest.update(block)
    return digest.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def quantize(value):
    """Nearest GRID fraction of an exact fraction, with ties to even."""
    scaled = F(value)*GRID
    lower, remainder = divmod(scaled.numerator, scaled.denominator)
    if 2*remainder > scaled.denominator or (
            2*remainder == scaled.denominator and lower % 2):
        lower += 1
    return F(lower, GRID)


def original_gradient(x, gp, outgoing_log, logk, pi, ii):
    u, s, t, p, q = x
    h, gu, su, st, tp, pq, gt, gpv, gq = gp
    return [2*h-3*gu+su+pi*ii*(1-6*u+2*s),
            st-su+2*pi*ii*u,
            st+tp-2*gt+2*pi*ii*p,
            tp+pq-3*gpv+2*pi*ii*t,
            pq-gq-outgoing_log+logk]


def original_hessian(x, gpp, outgoing_product, pi, ii):
    h, gu, su, st, tp, pq, gt, gp, gq = gpp
    zero = pi*0
    H = [[zero for _ in range(5)] for _ in range(5)]
    H[0][0] = -2*h-3*gu-su-6*pi*ii
    H[0][1] = H[1][0] = su+2*pi*ii
    H[1][1] = st-su
    H[1][2] = H[2][1] = st
    H[2][2] = st+tp-2*gt
    H[2][3] = H[3][2] = tp+2*pi*ii
    H[3][3] = tp+pq-3*gp
    H[3][4] = H[4][3] = pq
    H[4][4] = pq-gq-2*pi*ii*outgoing_product/(1-outgoing_product)
    return H


def arguments(x, half):
    u, s, t, p, q = x
    return (half-u, u, s-u, s+t, t+p, p+q, t, p, q)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=OUTPUT)
    args = parser.parse_args()
    require(args.output.resolve() == OUTPUT.resolve(),
            'this protocol has one prescribed output path')
    with args.output.open('x') as stream:
        inputs = {}
        proposal_counts = {k: {'attempted': 0, 'completed': 0}
                           for k in EXPECTED_PROPOSAL}
        analytic_counts = {k: {'attempted': 0, 'completed': 0}
                           for k in EXPECTED_ANALYTIC}
        result = dict(schema='mixed-prepared-cap-action-v1',
            status='initializing', script_path=str(Path(__file__).resolve().relative_to(ROOT)),
            theory_path=THEORY, protocol_path=PROTOCOL, input_sha256=inputs,
            precision_bits=PRECISION, proposal_decimal_digits=PROPOSAL_DPS,
            proposal_calls=proposal_counts, analytic_calls=analytic_counts,
            proposal_history=[], analytic_events=[], guards={}, errors=[],
            prescribed_radius_rational=str(RADIUS),
            action_error_radius_rational=str(ACTION_ERROR),
            action_certified=False,
            fixed_protocol=dict(steps=STEPS, first_half_steps=8,
                coordinate_names=NAMES, initial=[[str(a), str(b)] for a, b in INITIAL],
                domain_rectangles=[[str(v) for v in row] for row in DOMAINS],
                clamp_inset_rational=str(INSET), quantization_denominator=str(GRID),
                maximum_proposal_calls=EXPECTED_PROPOSAL,
                maximum_rigorous_calls=EXPECTED_ANALYTIC,
                new_existence_tests=0, root_refinements=0, parameter_covers=0,
                precision_changes=0, retries=0, face_evaluations=0, alias_evaluations=0),
            source_scope='Original prepared-34 critical action and coordinates only; no physical/alias sign or whole-source conclusion.')

        def bind(name, expected):
            require(isinstance(name, str) and
                    (ROOT/name).resolve().is_relative_to(ROOT.resolve()),
                    'invalid input path')
            require(isinstance(expected, str) and len(expected) == 64,
                    'unset or malformed pin: '+name)
            if name in inputs:
                require(inputs[name] == expected, 'conflicting input pin: '+name)
            actual = sha(ROOT/name)
            require(actual == expected, 'input hash mismatch: '+name)
            inputs[name] = actual

        def stage(name):
            result['active_stage'] = name

        def guard(name, condition, operands):
            result['guards'][name] = dict(passed=bool(condition), operands=operands)
            if not condition:
                raise GuardFailure(name)

        try:
            stage('provenance')
            require(all(p in PINNED for p in REQUIRED_PINS), 'literal pins incomplete')
            for name, expected in PINNED.items():
                bind(name, expected)
            own = result['script_path']
            bind(own, sha(ROOT/own))
            result['script_sha256'] = inputs[own]
            result['theory_sha256'] = inputs[THEORY]
            result['protocol_sha256'] = inputs[PROTOCOL]
            source = json.loads((ROOT/SOURCE).read_text())
            require(source['status'] == 'passed', 'original interface status')
            require(source['script_sha256'] == inputs[SOURCE_WRITER],
                    'original interface writer association')
            require(source['dependencies_sha256'], 'missing source dependencies')
            for name, expected in source['dependencies_sha256'].items():
                bind(name, expected)
            boundary = json.loads((ROOT/BOUNDARY).read_text())
            require(boundary['status'] == 'passed' and boundary['inclusion_certified'],
                    'boundary-update existence premise failed')
            require(boundary['passed_arcs'] == 512 and boundary['visited_arcs'] == 512,
                    'incomplete fixed boundary inventory')
            require(boundary['all_inputs_unchanged'] and
                    boundary['input_sha256'] == boundary['input_sha256_after'],
                    'boundary input change')
            require(boundary['script_sha256'] == inputs[BOUNDARY_WRITER],
                    'boundary writer association')
            for name, expected in boundary['input_sha256'].items():
                bind(name, expected)
            require(boundary['input_sha256'][SOURCE] == inputs[SOURCE],
                    'boundary uses a different original algebraic input')
            certificate = source['root_certificate']
            require(len(certificate['center']) == 2, 'original root center schema')
            center = tuple(map(F, certificate['center']))
            radius = F(certificate['complex_disk_radius'])
            require(radius == F(1, 10**26), 'original root radius changed')
            require(boundary['reference']['root_certificate_canonical_sha256'] ==
                    canonical(certificate), 'boundary root-certificate association')
            result['reference'] = dict(path=SOURCE, sha256=inputs[SOURCE],
                writer_path=SOURCE_WRITER, writer_sha256=inputs[SOURCE_WRITER],
                root_certificate_canonical_sha256=canonical(certificate),
                center_rational=list(map(str, center)), radius_rational=str(radius),
                full_square_rational=[[str(c-radius), str(c+radius)] for c in center],
                existence_path=BOUNDARY, existence_sha256=inputs[BOUNDARY],
                original_existence_and_associations_verified=True)

            # All source pins and inherited manifests precede numerical imports.
            stage('fixed_proposal')
            import mpmath as mp
            result['environment'] = dict(python=sys.version, platform=platform.platform(),
                                         mpmath_version=mp.__version__)
            with mp.workdps(PROPOSAL_DPS):
                def mr(value):
                    value = F(value)
                    return mp.mpf(value.numerator)/value.denominator

                def mc(pair):
                    return mp.mpc(mr(pair[0]), mr(pair[1]))

                def finite(z):
                    return bool(mp.isfinite(z.real) and mp.isfinite(z.imag))

                def mrec(z):
                    require(finite(z), 'nonfinite proposal value')
                    return [mp.nstr(z.real, 85), mp.nstr(z.imag, 85)]

                def call(kind, operand):
                    counter = proposal_counts[kind]
                    counter['attempted'] += 1
                    result['active_proposal_call'] = dict(kind=kind,
                        ordinal=counter['attempted'], operand=mrec(operand))
                    require(counter['attempted'] <= EXPECTED_PROPOSAL[kind],
                            'proposal call ceiling exceeded')
                    value = mp.exp(operand) if kind == 'exp' else mp.log(operand)
                    require(finite(value), 'nonfinite proposal '+kind)
                    counter['completed'] += 1
                    return value

                def solve(H, f, witness):
                    A = [list(row)+[rhs] for row, rhs in zip(H, f)]
                    witness['pivot_rows'] = []
                    for j in range(5):
                        pivot = max(range(j, 5), key=lambda i:
                                    A[i][j].real**2+A[i][j].imag**2)
                        witness['pivot_rows'].append(pivot)
                        require(A[pivot][j] != 0, 'zero proposal pivot')
                        A[j], A[pivot] = A[pivot], A[j]
                        denominator = A[j][j]
                        A[j] = [a/denominator for a in A[j]]
                        for i in range(5):
                            if i == j:
                                continue
                            factor = A[i][j]
                            A[i] = [a-factor*b for a, b in zip(A[i], A[j])]
                    answer = [A[i][-1] for i in range(5)]
                    require(all(finite(z) for z in answer), 'nonfinite proposal solve')
                    return answer

                a0 = mc(center)
                k0 = 1/(1+2*a0-4*a0*a0)
                logk0 = call('log', k0)
                result['proposal_input'] = dict(algebraic_center=mrec(a0),
                    K=mrec(k0), logK=mrec(logk0), certified_input=False)
                x = [mc(pair) for pair in INITIAL]
                ii, pi = mp.j, mp.pi
                for n in range(STEPS):
                    row = dict(step=n, status='started', point_before=[mrec(z) for z in x],
                               damping_rational='1/2' if n < 8 else '1')
                    result['proposal_history'].append(row)
                    result['active_proposal_step'] = n
                    zs = arguments(x, mr(F(1, 2)))
                    row['primitive_arguments'] = [mrec(z) for z in zs]
                    exps = [call('exp', -2*pi*ii*z) for z in zs]
                    gp = [call('log', 1-v) for v in exps]
                    out = k0*exps[-1]
                    outgoing_log = call('log', 1-out)
                    gpp = [2*pi*ii*v/(1-v) for v in exps]
                    f = original_gradient(x, gp, outgoing_log, logk0, pi, ii)
                    H = original_hessian(x, gpp, out, pi, ii)
                    row['gradient'] = [mrec(z) for z in f]
                    row['hessian'] = [[mrec(z) for z in line] for line in H]
                    d = solve(H, f, row)
                    row['solve'] = [mrec(z) for z in d]
                    damping = mr(F(1, 2) if n < 8 else F(1))
                    raw = [z-damping*v for z, v in zip(x, d)]
                    row['point_unclamped'] = [mrec(z) for z in raw]
                    x = [mp.mpc(max(mr(lo+INSET), min(mr(hi-INSET), z.real)),
                                max(mr(bot+INSET), min(mr(top-INSET), z.imag)))
                         for z, (lo, hi, bot, top) in zip(raw, DOMAINS)]
                    row['point_after'] = [mrec(z) for z in x]
                    row['status'] = 'completed'

                def exact_mpf(value):
                    require(mp.isfinite(value), 'nonfinite final proposal component')
                    sign, mantissa, exponent, _ = value._mpf_
                    mantissa, exponent = int(mantissa), int(exponent)
                    answer = (F(mantissa*(2**exponent)) if exponent >= 0 else
                              F(mantissa, 2**(-exponent)))
                    return -answer if sign else answer

                exact_binary = [(exact_mpf(z.real), exact_mpf(z.imag)) for z in x]
                exact = [(quantize(re), quantize(im)) for re, im in exact_binary]
                result['proposal_final_binary_rational'] = [list(map(str, v)) for v in exact_binary]
                result['proposal_rational'] = [list(map(str, v)) for v in exact]
                result['proposal_completed'] = len(result['proposal_history']) == STEPS
            require(all(proposal_counts[k]['completed'] == v for k, v in EXPECTED_PROPOSAL.items()),
                    'fixed proposal inventory not complete')

            stage('rational_domain')
            result['proposed_coordinate_squares'] = {}
            for name, (re, im), (lo, hi, bot, top) in zip(NAMES, exact, DOMAINS):
                square = dict(real=[str(re-RADIUS), str(re+RADIUS)],
                              imag=[str(im-RADIUS), str(im+RADIUS)])
                result['proposed_coordinate_squares'][name] = square
                guard('coordinate_domain_'+name,
                      lo < re-RADIUS < re+RADIUS < hi and
                      bot < im-RADIUS < im+RADIUS < top,
                      dict(square=square, domain=list(map(str, (lo, hi, bot, top)))))

            stage('rigorous_input')
            from flint import arb, acb, ctx
            import flint
            ctx.prec = PRECISION
            result['environment']['python_flint_version'] = getattr(flint, '__version__', None)

            def ends(value):
                if not value.is_finite():
                    raise ArithmeticError('nonfinite rigorous enclosure')
                return F(str(value.lower().fmpq())), F(str(value.upper().fmpq()))

            def rec(value):
                return list(map(str, ends(value)))

            def crec(value):
                return dict(real=rec(value.real), imag=rec(value.imag))

            conversions = result['rational_input_conversions'] = {}

            def ar(value):
                value = F(value)
                return arb(value.numerator)/arb(value.denominator)

            def point(value, name):
                value = F(value)
                enclosure = ar(value)
                lo, hi = ends(enclosure)
                conversions[name] = dict(rational=str(value), enclosure=rec(enclosure),
                                         outward_containment_verified=lo <= value <= hi)
                require(lo <= value <= hi, 'rational point not enclosed: '+name)
                return enclosure

            def ball(lo, hi, name):
                value = arb(ar((lo+hi)/2), ar((hi-lo)/2).upper())
                a, b = ends(value)
                conversions[name] = dict(prescribed=list(map(str, (lo, hi))),
                    enclosure=rec(value), outward_containment_verified=a <= lo <= hi <= b)
                require(a <= lo <= hi <= b, 'rational interval not enclosed: '+name)
                return value

            def analytic(kind, name, operand, function, real=False):
                row = dict(kind=kind, name=name, status='started',
                           input=None if operand is None else crec(operand))
                result['analytic_events'].append(row)
                counter = analytic_counts[kind]
                counter['attempted'] += 1
                require(counter['attempted'] <= EXPECTED_ANALYTIC[kind],
                        'rigorous analytic inventory exceeded: '+kind)
                value = function()
                row['output'] = rec(value) if real else crec(value)
                row['status'] = 'completed'
                counter['completed'] += 1
                return value

            def nonzero(value):
                rl, rh = ends(value.real)
                il, ih = ends(value.imag)
                return rl > 0 or rh < 0 or il > 0 or ih < 0

            def off_cut(value, start):
                _, rh = ends(value.real)
                il, ih = ends(value.imag)
                return rh < start or il > 0 or ih < 0

            def log_guard(value, name):
                rl, _ = ends(value.real)
                il, ih = ends(value.imag)
                guard(name, rl > 0 or il > 0 or ih < 0, crec(value))

            a = acb(ball(center[0]-radius, center[0]+radius, 'root_real'),
                    ball(center[1]-radius, center[1]+radius, 'root_imag'))
            denominator = 1+2*a-4*a*a
            guard('K_denominator_nonzero', nonzero(denominator), crec(denominator))
            K = 1/denominator
            result['algebraic_input_enclosure'] = crec(a)
            result['K_enclosure'] = crec(K)
            kr, ki = ends(K.real), ends(K.imag)
            k_mod2_upper = max(abs(v) for v in kr)**2+max(abs(v) for v in ki)**2
            guard('K_original_first_quadrant_disk', kr[0] > 0 and ki[0] > 0 and
                  k_mod2_upper < 1, dict(K=crec(K), modulus_squared_upper=str(k_mod2_upper)))
            pi = analytic('pi', 'pi', None, arb.pi, real=True)
            ii = acb(0, 1)
            log_guard(K, 'K_log_branch')
            logK = analytic('log', 'log_K', K, K.log)
            guard('K_dilog_branch', off_cut(K, F(1)), crec(K))
            liK = analytic('dilog', 'Li2_K', K, lambda: K.polylog(2))
            result['constants'] = dict(pi=rec(pi), logK=crec(logK), Li2K=crec(liK))
            values = [acb(point(re, name+'_real'), point(im, name+'_imag'))
                      for name, (re, im) in zip(NAMES, exact)]
            zs = arguments(values, arb(1)/2)
            primitive_rows = result['primitive_records'] = []
            exps, gp = [], []
            for name, z in zip(ARG_NAMES, zs):
                stage('primitive_'+name)
                row = dict(name=name, argument=crec(z), status='started')
                primitive_rows.append(row)
                lo, hi = ends(z.real)
                guard(name+'_original_strip', 0 < lo <= hi < 1, crec(z))
                exponent = -2*pi*ii*z
                ez = analytic('exp', name+'_exp', exponent, exponent.exp)
                row['exponential'] = crec(ez)
                guard(name+'_dilog_cut', off_cut(ez, F(1)), crec(ez))
                logarg = 1-ez
                log_guard(logarg, name+'_log_branch')
                prime = analytic('log', name+'_gprime', logarg, logarg.log)
                row['gprime'] = crec(prime)
                exps.append(ez)
                gp.append(prime)
                row['status'] = 'gradient_ready'
            stage('outgoing_incidence')
            outgoing = K*exps[-1]
            result['outgoing_product'] = crec(outgoing)
            guard('outgoing_original_lower_halfplane', ends(outgoing.imag)[1] < 0,
                  crec(outgoing))
            outarg = 1-outgoing
            log_guard(outarg, 'outgoing_log_branch')
            outgoing_log = analytic('log', 'outgoing_log', outarg, outarg.log)
            residual = original_gradient(values, gp, outgoing_log, logK, pi, ii)
            result['original_gradient_residual'] = [crec(z) for z in residual]
            norm2 = sum(max(abs(v) for v in ends(component))**2
                        for z in residual for component in (z.real, z.imag))
            threshold = MU_LOWER**2*RADIUS**2
            result['residual_squared_norm_upper_rational'] = str(norm2)
            result['accretivity_lower_rational'] = str(MU_LOWER)
            result['required_squared_residual_upper_rational'] = str(threshold)
            result['strict_residual_test'] = norm2 < threshold

            stage('original_action')
            gs = []
            for name, ez, row in zip(ARG_NAMES, exps, primitive_rows):
                li = analytic('dilog', name+'_Li2', ez, lambda: ez.polylog(2))
                value = (li-pi*pi/6)/(2*pi*ii)
                row['dilogarithm'] = crec(li)
                row['g'] = crec(value)
                row['status'] = 'completed'
                gs.append(value)
            liout = analytic('dilog', 'outgoing_Li2', outgoing,
                             lambda: outgoing.polylog(2))
            u, s, t, p, q = values
            h, gu, su, st, tp, pq, gt, gpv, gq = gs
            polynomial = pi*ii*(arb(1)/4+u+2*s*u-3*u*u+2*t*p)
            incidence = (q-arb(1)/2)*logK-(liout-liK)/(2*pi*ii)
            value = -2*h-3*gu-su+st+tp+pq-2*gt-3*gpv-gq+polynomial+incidence
            result['action_polynomial'] = crec(polynomial)
            result['action_incidence'] = crec(incidence)
            result['original_action_at_proposal'] = crec(value)
            require(all(analytic_counts[k]['completed'] == v for k, v in EXPECTED_ANALYTIC.items()),
                    'rigorous analytic inventory incomplete')
            result['full_analytic_inventory_completed'] = True
            if result['strict_residual_test']:
                re, im = ends(value.real), ends(value.imag)
                result['action_enclosure'] = dict(
                    real=[str(re[0]-ACTION_ERROR), str(re[1]+ACTION_ERROR)],
                    imag=[str(im[0]-ACTION_ERROR), str(im[1]+ACTION_ERROR)])
                result['M_lower_rational'] = str(re[0]-ACTION_ERROR)
                result['certified_radius_rational'] = str(RADIUS)
                result['coordinate_enclosures'] = result['proposed_coordinate_squares']
                result['action_certified'] = True
                result['status'] = 'passed'
            else:
                result['status'] = 'inconclusive'
                result['inconclusive_reason'] = 'prescribed original-gradient radius test failed'
        except GuardFailure as exc:
            result['status'] = 'inconclusive'
            result['errors'].append(dict(stage=result.get('active_stage'),
                error_type=type(exc).__name__, error=str(exc), traceback=traceback.format_exc()))
        except Exception as exc:
            result['status'] = 'failed'
            result['errors'].append(dict(stage=result.get('active_stage'),
                error_type=type(exc).__name__, error=str(exc), traceback=traceback.format_exc()))
        finally:
            after, changed = {}, []
            for name, before in inputs.items():
                try:
                    after[name] = sha(ROOT/name)
                    if after[name] != before:
                        changed.append(name)
                except Exception as exc:
                    after[name] = dict(error_type=type(exc).__name__, error=str(exc))
                    changed.append(name)
            result['input_sha256_after'] = after
            result['changed_inputs'] = changed
            result['input_binding_count'] = len(inputs)
            result['all_inputs_unchanged'] = not changed
            if changed:
                result['status'] = 'failed'
                result['errors'].append(dict(stage='final_bindings', changed_inputs=changed))
            if result['status'] != 'passed':
                result['action_certified'] = False
                result.pop('action_enclosure', None)
                result.pop('M_lower_rational', None)
                result.pop('certified_radius_rational', None)
                result.pop('coordinate_enclosures', None)
            json.dump(result, stream, indent=2, sort_keys=True, allow_nan=False)
            stream.write('\n')
    print(json.dumps(dict(status=result['status'], action_certified=result['action_certified'],
        M_lower_rational=result.get('M_lower_rational'), analytic_calls=analytic_counts,
        proposal_calls=proposal_counts, input_bindings=len(inputs),
        all_inputs_unchanged=result['all_inputs_unchanged'], output=str(args.output),
        output_sha256=sha(args.output)), sort_keys=True))
    return 0 if result['status'] in ('passed', 'inconclusive') else 1


if __name__ == '__main__':
    sys.exit(main())
