#!/usr/bin/env python3
"""One fixed set of sixteen prepared-cap face/alias supporting planes.

Untrusted CPython binary64 proposals have no proof role. The certificate
uses the full original interface-root square, original endpoint branch,
Arb256 values/gradients, and exact signed whole-domain support terms.
The prepared-action record and writer pins must be filled after review.
"""
import argparse
import cmath
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import platform
import sys


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = 'notes/research_mixed_prepared_cap_face_alias_protocol.md'
SOURCE = 'repro/results/research-three-four-source-interface.json'
SOURCE_WRITER = 'experiments/check_three_four_source_interface.py'
ACTION = 'repro/results/research-mixed-prepared-cap-action.json'
ACTION_WRITER = 'experiments/evaluate_mixed_prepared_cap_action.py'
ACTION_PROOF = 'notes/research_mixed_prepared_cap_action_enclosure.md'
OUTPUT = ROOT/'repro/results/research-mixed-prepared-cap-face-alias-budget.json'
PINNED = {
    PROTOCOL: '0340e96f1ab5add62dc15358be1804a77f19ed8a1ca9070bfa2c1fbbca6d8720',
    SOURCE: '9218011f3f5d41ff15835f74ccf83ccfeb266beea112c67607fa1eaef96ba9dd',
    SOURCE_WRITER: 'e9d009fdf8712a7577bd9220c8bbf6c2f8fd1d3eefece969cad45357d8a45f91',
    ACTION: '271c82db6397ef6de1749ff05a75faba9b94f318587f2765d0aaf7126a373239',
    ACTION_WRITER: '04d020578e4baba74385c49835382b6eb1642d8aa905d409cc8f8898ea19c04c',
    ACTION_PROOF: '8bbe001bf4c5093cd8ddf209a266d55da9a64521b2aa3b0562e9351c5d1a5e55',
    'notes/research_mixed_prepared_three_four_cap_source.md':
        'b875087d250f0a1178f46518c0ba67472aefa739f8bdb8ccf352c5c01edea104',
    'notes/research_mixed_prepared_cap_typed_height_rectangle.md':
        'a422d9e21071411b6ce30e516f2c6636c7c7f3512e96137aa43a01a76a9430a2',
    'notes/research_mixed_prepared_cap_physical_tail_reduction.md':
        '66f1bd355b51037f06e221a9ec911f4e1e544b681cd5763afa7476c35810f3b0',
    'notes/research_mixed_prepared_cap_full_source_criterion.md':
        'd31ec52de4af1d68269bcdb992ee1802bbe889649bf4f16b19bd440b16452807',
    'notes/research_mixed_prepared_three_four_cap_critical_curve.md':
        'e29f73574faba8f7f7f7196e63dadbd169287cf29cd72904a8257ebb54d2184f',
    'notes/research_mixed_endpoint_cap_rectangle.md':
        '9211d45bdd031c908690a723ebcd4b40a34fed90f44858301a809ee5901c15e8',
    'notes/research_mixed_fourier_boundary_critical_existence.md':
        'f7a910f0a2c67701a5dc5c0eb3e5fe8c6dcf20d6a83dbd4876c2363a46fabda6',
}
NAMES = ('s', 't', 'p', 'q')
BOUNDS = ((F(27, 100), F(49, 100)), (F(11, 50), F(1, 2)),
          (F(1, 5), F(21, 50)), (F(1, 5), F(21, 50)))
HEIGHTS = ((F(-11, 200), F(1, 25)), (F(-9, 125), F(21, 1000)),
           (F(-51, 500), F(3, 200)), (F(-51, 500), F(3, 200)))
PRECISION, ITERATIONS, QUANTIZATION = 256, 32, 10**12
CLAMP = F(1, 100000000)
FAR_UPPER = F(146, 75)
PRIMITIVES = ('half_minus_u', 'u', 's_minus_u', 'st', 'tp', 'pq', 't', 'p', 'q')
GP_NAMES = ('s_minus_u', 'st', 'tp', 'pq', 't', 'p', 'q')
COEFFICIENTS = (-2, -3, -1, 1, 1, 1, -2, -3, -1)
RIGOROUS_LIMITS = dict(pi=1, exp=160, sqrt=16, log=161, dilog=161)
FLOAT_LIMITS = dict(exp=5120, sqrt=512, log=5121)


class GuardFailure(Exception):
    pass


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
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                    allow_nan=False).encode()).hexdigest()


def interval(lo, hi):
    require(lo <= hi, 'reversed interval')
    return dict(finite=True, lower_rational=str(lo), upper_rational=str(hi))


def source_interval(value):
    require(isinstance(value, list) and len(value) == 2,
            'prepared-action interval schema')
    lo, hi = map(F, value)
    require(lo <= hi, 'prepared-action interval reversed')
    return lo, hi


def inventory():
    cases = []
    for kind in ('face', 'alias'):
        for j, name in enumerate(NAMES):
            for side in (0, 1):
                heights = [F(0)]*4
                target = [list(v) for v in BOUNDS]
                if kind == 'face':
                    target[j] = [BOUNDS[j][side]]*2
                    free = [i for i in range(4) if i != j]
                else:
                    heights[j] = HEIGHTS[j][side]
                    free = list(range(4))
                cases.append(dict(name=kind+':'+name+':'+('lower', 'upper')[side],
                    kind=kind, coordinate=j, side=side, free_coordinates=free,
                    target_rational=[[str(a), str(b)] for a, b in target],
                    heights_rational=list(map(str, heights))))
    return cases


def solve(matrix, rhs):
    n = len(rhs)
    require(n in (3, 4) and len(matrix) == n and
            all(len(row) == n for row in matrix), 'proposal solve dimensions')
    a = [list(row)+[value] for row, value in zip(matrix, rhs)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(a[row][col]))
        require(math.isfinite(a[pivot][col]) and a[pivot][col] != 0,
                'singular/nonfinite binary64 Newton system')
        a[col], a[pivot] = a[pivot], a[col]
        for row in range(col+1, n):
            ratio = a[row][col]/a[col][col]
            for j in range(col, n+1):
                a[row][j] -= ratio*a[col][j]
    x = [0.0]*n
    for row in reversed(range(n)):
        x[row] = (a[row][n]-sum(a[row][j]*x[j]
                               for j in range(row+1, n)))/a[row][row]
    require(all(math.isfinite(v) for v in x), 'nonfinite Newton step')
    return x


def argument_dict(s, t, p, q, u):
    return dict(zip(PRIMITIVES, (F(1, 2)-u, u, s-u, s+t, t+p, p+q, t, p, q)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=OUTPUT)
    args = parser.parse_args()
    require(args.output.resolve() == OUTPUT.resolve(), 'sole prescribed output path')
    with args.output.open('x') as stream:
        inputs = {}
        rigorous = {k: dict(attempted=0, completed=0) for k in RIGOROUS_LIMITS}
        floating = {k: dict(attempted=0, completed=0) for k in FLOAT_LIMITS}
        result = dict(status='initializing', protocol_path=PROTOCOL,
            script_path=str(Path(__file__).resolve().relative_to(ROOT)),
            input_sha256=inputs, cases=[], pending_cases=inventory(), errors=[],
            precision_bits=PRECISION, rigorous_calls=rigorous,
            floating_calls=floating, proposal_derivative_attempts=0,
            proposal_derivative_completions=0, complete_source_comparison=False,
            scope='Sixteen prepared-cap tangent bounds against its original certified action; no full outgoing-period or arbitrary-message conclusion.',
            fixed_protocol=dict(case_count=16, proposal_steps_per_case=ITERATIONS,
                proposal_arithmetic='CPython binary64 math/cmath',
                proposal_clamp_rational=str(CLAMP), quantization=QUANTIZATION,
                rigorous_limits=RIGOROUS_LIMITS, floating_limits=FLOAT_LIMITS,
                root_solves=0, gain_calls=0, refinements=0, retries=0),
            far_physical_upper_rational=str(FAR_UPPER))

        def bind(name, expected):
            require(isinstance(name, str) and
                    (ROOT/name).resolve().is_relative_to(ROOT.resolve()), 'binding path')
            require(isinstance(expected, str) and len(expected) == 64,
                    'pending/malformed pin: '+name)
            if name in inputs:
                require(inputs[name] == expected, 'conflicting pin: '+name)
            require(sha(ROOT/name) == expected, 'input hash mismatch: '+name)
            inputs[name] = expected

        try:
            for name, digest in PINNED.items():
                bind(name, digest)
            own = result['script_path']
            bind(own, sha(ROOT/own))
            result.update(script_sha256=inputs[own], protocol_sha256=inputs[PROTOCOL])
            source = json.loads((ROOT/SOURCE).read_text())
            require(source['status'] == 'passed' and
                    source['script_sha256'] == inputs[SOURCE_WRITER],
                    'original root status/writer association')
            for name, digest in source['dependencies_sha256'].items():
                bind(name, digest)
            certificate = source['root_certificate']
            require(len(certificate['center']) == 2, 'root center schema')
            center = tuple(map(F, certificate['center']))
            radius = F(certificate['complex_disk_radius'])
            require(radius > 0, 'full original radius required')
            result['reference'] = dict(path=SOURCE, sha256=inputs[SOURCE],
                root_certificate_canonical_sha256=canonical(certificate),
                center_rational=list(map(str, center)), radius_rational=str(radius),
                square_rational=[[str(c-radius), str(c+radius)] for c in center])
            action = json.loads((ROOT/ACTION).read_text())
            require(action['status'] == 'passed' and
                    action['script_sha256'] == inputs[ACTION_WRITER] and
                    action['all_inputs_unchanged'] is True, 'action status/writer')
            require(action['input_sha256'] == action['input_sha256_after'],
                    'action before/after bindings')
            require(action['input_sha256'][SOURCE] == inputs[SOURCE] and
                    action['input_sha256'][ACTION_PROOF] == inputs[ACTION_PROOF],
                    'action original root/proof association')
            for name, digest in action['input_sha256'].items():
                bind(name, digest)
            action_radius = F(action['certified_radius_rational'])
            error_radius = F(action['action_error_radius_rational'])
            require(action_radius > 0 and error_radius == 60*action_radius**2,
                    'action quadratic error radius')
            for part in ('real', 'imag'):
                alo, ahi = source_interval(action['original_action_at_proposal'][part])
                elo, ehi = source_interval(action['action_enclosure'][part])
                require((elo, ehi) == (alo-error_radius, ahi+error_radius),
                        'action enclosure enlargement: '+part)
            M_lower = F(action['M_lower_rational'])
            require(M_lower == source_interval(action['action_enclosure']['real'])[0],
                    'action lower endpoint')
            result['prepared_action'] = dict(path=ACTION, sha256=inputs[ACTION],
                writer_path=ACTION_WRITER, writer_sha256=inputs[ACTION_WRITER],
                action_enclosure=action['action_enclosure'],
                original_action_at_proposal=action['original_action_at_proposal'],
                certified_radius_rational=str(action_radius),
                action_error_radius_rational=str(error_radius),
                M_lower_rational=str(M_lower), original_associations_verified=True)
            require(platform.python_implementation() == 'CPython' and
                    sys.float_info.radix == 2 and sys.float_info.mant_dig == 53 and
                    sys.float_info.max_exp == 1024, 'CPython binary64 required')
            result['proposal_runtime'] = dict(python=sys.version, platform=platform.platform(),
                radix=sys.float_info.radix, mantissa_bits=sys.float_info.mant_dig,
                maximum_exponent=sys.float_info.max_exp)

            # No Flint import or floating proposal occurs before complete preflight.
            from flint import arb, acb, ctx
            ctx.prec = PRECISION

            def call(table, limits, name, function):
                table[name]['attempted'] += 1
                require(table[name]['attempted'] <= limits[name],
                        'call inventory exceeded: '+name)
                value = function()
                table[name]['completed'] += 1
                return value

            def fc(name, value):
                out = call(floating, FLOAT_LIMITS, name,
                           lambda: getattr(cmath, name)(value))
                require(math.isfinite(out.real) and math.isfinite(out.imag),
                        'nonfinite floating '+name)
                return out

            def rc(name, function):
                return call(rigorous, RIGOROUS_LIMITS, name, function)

            def ar(value):
                value = F(value)
                return arb(value.numerator)/arb(value.denominator)

            def ends(value):
                if not value.is_finite():
                    raise ArithmeticError('nonfinite rigorous enclosure')
                return F(str(value.lower().fmpq())), F(str(value.upper().fmpq()))

            def rec(value):
                return interval(*ends(value)) if value.is_finite() else dict(
                    finite=False, display=str(value))

            def crec(value):
                return dict(real=rec(value.real), imag=rec(value.imag))

            def save(where, name, value):
                where[name] = crec(value)
                ends(value.real)
                ends(value.imag)
                return value

            def ball(lo, hi, where, name):
                value = arb(ar((lo+hi)/2), ar((hi-lo)/2).upper())
                where[name] = dict(prescribed=interval(lo, hi), enclosure=rec(value))
                outlo, outhi = ends(value)
                require(outlo <= lo <= hi <= outhi, 'outward input conversion: '+name)
                where[name]['containment_verified'] = True
                return value

            def nonzero(value):
                a, b = ends(value.real)
                c, d = ends(value.imag)
                return a > 0 or b < 0 or c > 0 or d < 0

            def modulus_square_upper(value):
                lo, hi = ends(value.real)
                low, high = ends(value.imag)
                return max(lo*lo, hi*hi)+max(low*low, high*high)

            constants = result['constants'] = {}
            conversions = constants['rational_inputs'] = {}
            root = acb(*(ball(c-radius, c+radius, conversions, name)
                         for c, name in zip(center, ('root_real', 'root_imag'))))
            save(constants, 'full_root_square', root)
            denominator = save(constants, 'K_denominator', 1+2*root-4*root*root)
            require(nonzero(denominator), 'original K denominator')
            K = save(constants, 'K', 1/denominator)
            Ksq = modulus_square_upper(K)
            constants['K_squared_modulus_upper_rational'] = str(Ksq)
            require(Ksq < 1 and ends(K.real)[0] > 0 and ends(K.imag)[0] > 0,
                    'original K disk and logarithm branch')
            pi = rc('pi', arb.pi)
            constants['pi'] = rec(pi)
            pi_lo, pi_hi = ends(pi)
            require(3 < pi_lo <= pi_hi < 4, 'pi enclosure')
            ii = acb(0, 1)
            logK = save(constants, 'log_K', rc('log', K.log))
            dilogK = save(constants, 'dilog_K', rc('dilog', lambda: K.polylog(2)))
            float_root = complex(float(center[0]), float(center[1]))
            float_K = 1/(1+2*float_root-4*float_root*float_root)
            float_logK = fc('log', float_K)
            result['untrusted_proposal_K'] = [float_K.real, float_K.imag]

            def float_derivatives(y, heights):
                result['proposal_derivative_attempts'] += 1
                require(result['proposal_derivative_attempts'] <= 512,
                        'proposal derivative inventory')
                s, t, p, q = [complex(v, float(h)) for v, h in zip(y, heights)]
                c = 2j*math.pi
                disc = 1-2*fc('exp', c*s)
                omega = (1j+fc('sqrt', disc))/2
                u = (fc('log', 1+1j*omega)-fc('log', 1-1j*omega))/c
                arguments = argument_dict(s, t, p, q, u)
                shapes = {name: fc('exp', -c*z) for name, z in arguments.items()}
                gp = {name: fc('log', 1-shapes[name]) for name in GP_NAMES}
                gpp = {name: c*z/(1-z) for name, z in shapes.items()}
                outgoing = float_K*shapes['q']
                external_prime = float_logK-fc('log', 1-outgoing)
                external_second = -c*outgoing/(1-outgoing)
                grad = [gp['st']-gp['s_minus_u']+c*u,
                        gp['st']+gp['tp']-2*gp['t']+c*p,
                        gp['tp']+gp['pq']-3*gp['p']+c*t,
                        gp['pq']-gp['q']+external_prime]
                buu = (-2*gpp['half_minus_u']-3*gpp['u']
                       -gpp['s_minus_u']-3*c)
                bsu = gpp['s_minus_u']+c
                diag = (gpp['st']-gpp['s_minus_u']-bsu*bsu/buu,
                        gpp['st']+gpp['tp']-2*gpp['t'],
                        gpp['tp']+gpp['pq']-3*gpp['p'],
                        gpp['pq']-gpp['q']+external_second)
                hess = [[0j]*4 for _ in range(4)]
                for j in range(4):
                    hess[j][j] = diag[j]
                for j, value in enumerate((gpp['st'], gpp['tp']+c, gpp['pq'])):
                    hess[j][j+1] = hess[j+1][j] = value
                grad = [z.real for z in grad]
                hess = [[z.real for z in row] for row in hess]
                require(all(math.isfinite(z) for z in grad+sum(hess, [])),
                        'nonfinite real proposal derivatives')
                result['proposal_derivative_completions'] += 1
                return grad, hess

            for case in inventory():
                row = dict(case=case, status='initializing', valid=False, stage='proposal',
                           guards={}, proposal=dict(iterations=[]))
                result['cases'].append(row)
                result['active_case'] = case['name']

                def guard(name, value):
                    row['guards'][name] = bool(value)
                    if not value:
                        raise GuardFailure(name)

                try:
                    heights = list(map(F, case['heights_rational']))
                    target = [tuple(map(F, v)) for v in case['target_rational']]
                    free = case['free_coordinates']
                    y = [float((a+b)/2) for a, b in target]
                    row['proposal']['initial_coordinates'] = y[:]
                    for step in range(ITERATIONS):
                        entry = dict(index=step, coordinates_before=y[:])
                        row['proposal']['iterations'].append(entry)
                        grad, hess = float_derivatives(y, heights)
                        matrix = [[hess[i][j] for j in free] for i in free]
                        rhs = [grad[i] for i in free]
                        entry.update(real_gradient=grad, free_real_hessian=matrix)
                        delta = solve(matrix, rhs)
                        damping = 0.5 if step < 8 else 1.0
                        entry.update(newton_step=delta, damping=damping)
                        for j, value in zip(free, delta):
                            lo, hi = target[j]
                            y[j] = min(float(hi-CLAMP), max(float(lo+CLAMP),
                                                          y[j]-damping*value))
                        require(all(math.isfinite(v) for v in y), 'proposal coordinates')
                        entry['coordinates_after'] = y[:]
                    support = [F(round(F.from_float(v)*QUANTIZATION), QUANTIZATION)
                               if j in free else target[j][0]
                               for j, v in enumerate(y)]
                    for j, (lo, hi) in enumerate(target):
                        require(lo <= support[j] <= hi, 'rational trial domain')
                        if j in free:
                            require(lo < support[j] < hi, 'free trial interior')
                    row['support_real_rational'] = list(map(str, support))
                    row['proposal']['final_binary64_coordinates'] = y[:]
                    row['stage'] = 'rigorous_inputs'
                    data = row['rigorous'] = {}
                    conversion = data['rational_inputs'] = {}
                    zz = [acb(ball(v, v, conversion, name+'_real'),
                              ball(h, h, conversion, name+'_imag'))
                          for name, v, h in zip(NAMES, support, heights)]
                    data['support_complex'] = dict(zip(NAMES, map(crec, zz)))
                    s, t, p, q = zz
                    row['stage'] = 'endpoint_branch'
                    endpoint = data['endpoint'] = {}
                    disc_exp = save(endpoint, 'exponential', rc('exp', (2*pi*ii*s).exp))
                    disc = save(endpoint, 'discriminant', 1-2*disc_exp)
                    guard('endpoint_discriminant_real_above_one', ends(disc.real)[0] > 1)
                    sqrt_disc = save(endpoint, 'square_root', rc('sqrt', disc.sqrt))
                    guard('endpoint_sqrt_positive_real', ends(sqrt_disc.real)[0] > 0)
                    omega = save(endpoint, 'omega', (ii+sqrt_disc)/2)
                    plus = save(endpoint, 'log_plus_argument', 1+ii*omega)
                    minus = save(endpoint, 'log_minus_argument', 1-ii*omega)
                    guard('endpoint_log_plus_positive_real', ends(plus.real)[0] > 0)
                    guard('endpoint_log_minus_positive_real', ends(minus.real)[0] > 0)
                    lp = save(endpoint, 'log_plus', rc('log', plus.log))
                    lm = save(endpoint, 'log_minus', rc('log', minus.log))
                    u = save(endpoint, 'u', (lp-lm)/(2*pi*ii))
                    guard('endpoint_u_real_positive', ends(u.real)[0] > 0)
                    guard('endpoint_u_real_below_s', ends(u.real)[1] < support[0])
                    guard('endpoint_u_imag_positive', ends(u.imag)[0] > 0)
                    row['stage'] = 'original_primitives'
                    # Acb arithmetic only: do not pass a Fraction directly to Flint.
                    arguments = dict(zip(PRIMITIVES,
                        (ar(F(1, 2))-u, u, s-u, s+t, t+p, p+q, t, p, q)))
                    records = data['primitives'] = {}
                    gg, gp, shapes = {}, {}, {}
                    for name in PRIMITIVES:
                        z = arguments[name]
                        item = records[name] = dict(argument=crec(z))
                        guard('primitive_strip:'+name,
                              ends(z.real)[0] > 0 and ends(z.real)[1] < 1)
                        shape = save(item, 'exponential', rc('exp', (-2*pi*ii*z).exp))
                        shapes[name] = shape
                        log_argument = save(item, 'log_argument', 1-shape)
                        cut_safe = (ends(shape.real)[1] < 1 or
                                    ends(shape.imag)[0] > 0 or ends(shape.imag)[1] < 0)
                        guard('primitive_dilog_cut:'+name, cut_safe)
                        guard('primitive_log_branch:'+name,
                              ends(log_argument.real)[0] > 0 or
                              ends(log_argument.imag)[0] > 0 or
                              ends(log_argument.imag)[1] < 0)
                        dilog = save(item, 'dilogarithm',
                                     rc('dilog', lambda z=shape: z.polylog(2)))
                        gg[name] = save(item, 'g', (dilog-pi*pi/6)/(2*pi*ii))
                        if name in GP_NAMES:
                            gp[name] = save(item, 'g_prime', rc('log', log_argument.log))
                    row['stage'] = 'outgoing_incidence'
                    ext = data['outgoing'] = {}
                    KQ = save(ext, 'KQ', K*shapes['q'])
                    KQsq = modulus_square_upper(KQ)
                    ext['squared_modulus_upper_rational'] = str(KQsq)
                    guard('outgoing_strict_disk', KQsq < F(49, 100))
                    one_minus = save(ext, 'log_argument', 1-KQ)
                    guard('outgoing_log_positive_real', ends(one_minus.real)[0] > 0)
                    dilog_out = save(ext, 'dilogarithm',
                                     rc('dilog', lambda: KQ.polylog(2)))
                    log_out = save(ext, 'logarithm', rc('log', one_minus.log))
                    ell = save(ext, 'ell',
                        (q-ar(F(1, 2)))*logK-(dilog_out-dilogK)/(2*pi*ii))
                    row['stage'] = 'phase_and_gradient'
                    polynomial = save(data, 'imaginary_polynomial',
                        pi*ii*(ar(F(1, 4))+u-3*u*u+2*s*u+2*t*p))
                    value = save(data, 'phase',
                        sum(c*gg[name] for c, name in zip(COEFFICIENTS, PRIMITIVES))
                        +polynomial+ell)
                    gradient = [gp['st']-gp['s_minus_u']+2*pi*ii*u,
                        gp['st']+gp['tp']-2*gp['t']+2*pi*ii*p,
                        gp['tp']+gp['pq']-3*gp['p']+2*pi*ii*t,
                        gp['pq']-gp['q']+logK-log_out]
                    data['gradient'] = dict(zip(NAMES, map(crec, gradient)))
                    row['stage'] = 'rational_support'
                    terms = row['support_terms'] = []
                    for name, grad, point, (lo, hi) in zip(NAMES, gradient, support, target):
                        gl, gh = ends(grad.real)
                        dl, dh = lo-point, hi-point
                        products = [gl*dl, gl*dh, gh*dl, gh*dh]
                        terms.append(dict(coordinate=name,
                            gradient_real=interval(gl, gh),
                            displacement_rational=[str(dl), str(dh)],
                            four_products_rational=list(map(str, products)),
                            upper_rational=str(max(products))))
                    phase_upper = ends(value.real)[1]
                    debit_lower = 2*pi_lo*sum(map(abs, heights))
                    upper = phase_upper+sum(F(v['upper_rational']) for v in terms)-debit_lower
                    row.update(valid=True, phase_upper_rational=str(phase_upper),
                        alias_debit_lower_rational=str(debit_lower),
                        upper_rational=str(upper), gap_lower_rational=str(M_lower-upper),
                        strict_comparison=upper < M_lower,
                        status='passed' if upper < M_lower else 'inconclusive', stage='complete')
                except GuardFailure as exc:
                    row.update(status='inconclusive', error_type=type(exc).__name__,
                               guard_failure=str(exc))
                except Exception as exc:
                    row.update(status='failed', error_type=type(exc).__name__, error=str(exc))
                    result['errors'].append(dict(case=case['name'], stage=row['stage'],
                        error_type=type(exc).__name__, error=str(exc)))

            require([row['case'] for row in result['cases']] == inventory(),
                    'full prescribed case inventory')
            result['visited_cases'] = len(result['cases'])
            result['valid_cases'] = sum(row['valid'] for row in result['cases'])
            result['passed_cases'] = sum(row['status'] == 'passed' for row in result['cases'])
            result['full_inventory_completed'] = (
                result['proposal_derivative_attempts'] == 512 and
                result['proposal_derivative_completions'] == 512 and
                all(table[name]['attempted'] == limit and
                    table[name]['completed'] == limit
                    for table, limits in ((rigorous, RIGOROUS_LIMITS),
                                          (floating, FLOAT_LIMITS))
                    for name, limit in limits.items()))
            if result['valid_cases'] == 16:
                maxima = {}
                for kind in ('face', 'alias'):
                    worst = max((row for row in result['cases'] if row['case']['kind'] == kind),
                                key=lambda row: F(row['upper_rational']))
                    maxima[kind] = dict(case=worst['case']['name'],
                                       upper_rational=worst['upper_rational'])
                all_upper = max(FAR_UPPER, *(F(v['upper_rational']) for v in maxima.values()))
                gap = M_lower-all_upper
                result['maxima'] = maxima
                result['complete_upper_rational'] = str(all_upper)
                result['gap_lower_rational'] = str(gap)
                result['far_physical_strict_comparison'] = FAR_UPPER < M_lower
                result['complete_source_comparison'] = (
                    gap > 0 and result['full_inventory_completed'] and not result['errors'])
            result['status'] = ('passed' if result['complete_source_comparison'] else
                                'failed' if result['errors'] else 'inconclusive')
        except Exception as exc:
            result['status'] = 'failed'
            result['complete_source_comparison'] = False
            result['errors'].append(dict(stage='preflight_or_global',
                error_type=type(exc).__name__, error=str(exc)))
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
            result.update(input_sha256_after=after, changed_inputs=changed,
                          input_binding_count=len(inputs), all_inputs_unchanged=not changed)
            if changed:
                result['status'] = 'failed'
                result['complete_source_comparison'] = False
            result.pop('active_case', None)
            json.dump(result, stream, indent=2, sort_keys=True, allow_nan=False)
            stream.write('\n')
    print(json.dumps(dict(status=result['status'],
        complete_source_comparison=result['complete_source_comparison'],
        visited_cases=result.get('visited_cases', len(result['cases'])),
        valid_cases=result.get('valid_cases', 0), passed_cases=result.get('passed_cases', 0),
        rigorous_calls=rigorous, proposal_derivative_completions=result['proposal_derivative_completions'],
        input_bindings=len(inputs), all_inputs_unchanged=result['all_inputs_unchanged'],
        output=str(args.output), output_sha256=sha(args.output)), sort_keys=True))
    return 0 if result['status'] in ('passed', 'inconclusive') else 1


if __name__ == '__main__':
    sys.exit(main())
