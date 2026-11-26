#!/usr/bin/env python3
"""Eight fixed single-height tangent bounds for the original paired source.

The float Newton iterations only choose rational supporting points. The
proof uses the full saved root square, original complex phase and gradients,
and the pinned whole-box concavity theorem. No alternate proposal, adaptive
precision, reference-root solve, refinement or retry is provided.
"""
import argparse
import cmath
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = 'notes/research_mixed_contracted_pair_eight_aliases_protocol.md'
THEORY = 'notes/research_mixed_contracted_pair_enlarged_rectangle.md'
CONTOUR = 'notes/research_mixed_contracted_pair_simultaneous_contour.md'
SOURCE = 'repro/results/research-three-four-source-interface.json'
ROOT_SCRIPT = 'experiments/check_three_four_source_interface.py'
PACKET_RECORDS = (
    ('repro/results/research-three-vertex-mixed-reference.json',
     'experiments/certify_three_vertex_mixed_reference.py'),
    ('repro/results/research-power-four-index-contours.json',
     'experiments/certify_power_four_index_contours.py'),
)
PINNED = {
    PROTOCOL: 'd4e8d57d702d08a011d566322eb558bc7d28e170aba10083eee30334f4bdba67',
    THEORY: '597761e942e2956554fe4f25d22de0156838a880e37c04e4fa8fe843e087f0fc',
    CONTOUR: '296a692927f547863ae32cea467f8dc5813ad953bff0a88e72b2a781ca4911db',
    'notes/research_mixed_contracted_pair_enlarged_tail_reduction.md':
        '5652cc1d58beabc5929ef6ff9103abfa3415c06a747338ee1bb2b40efa654eda',
    'notes/research_mixed_contracted_pair_rectangle.md':
        'a784131ce05513342bf86af5c531a5419ad38234f876dbfa9bb22ddbafa5340a',
    'notes/research_mixed_contracted_pair_outer_index_elimination.md':
        '231d52a52fab4f5eb2f10cb7fa721f7be586181c2f2407d9a587cf43370fbf5f',
    'notes/research_exact_vertical_current_regrouping.md':
        'fbc3bfe6015cfbdfffb4c11d07738fd435b1ad1a871b6be29cee9c2ed5542ad7',
    SOURCE: '9218011f3f5d41ff15835f74ccf83ccfeb266beea112c67607fa1eaef96ba9dd',
    ROOT_SCRIPT: 'e9d009fdf8712a7577bd9220c8bbf6c2f8fd1d3eefece969cad45357d8a45f91',
    'notes/research_three_vertex_mixed_reference_packet.md':
        '71e5b3c4ad29bdfe49d4fb1c95dc658e86f19ff2656621b6bcf495222b59b849',
    'notes/research_mixed_contracted_phase.md':
        'e9e1291b0befb6e552f1e4ae272afc547ec058f68ae9915c7116bbb6b331ac00',
    'repro/results/research-three-vertex-mixed-reference.json':
        'be27579fe6329c85d9617d00a7299ef67d75d1342ad7b0af5b589838c82650f2',
    'repro/results/research-power-four-index-contours.json':
        '10c9deacd149b8130867c659a1fb45d5793e4b318ea85424e8656dcdad71e79a',
    'notes/research_power_four_source_packet.md':
        '6d572795eb2482e988c3761d2d56910b48d8f0a9459b6db44f3ca7365328087a',
}
NAMES = ('s', 't', 'p', 'q')
BOUNDS = ((F(1, 4), F(1, 2)), (F(1, 5), F(9, 20)),
          (F(1, 5), F(21, 50)), (F(1, 5), F(21, 50)))
HEIGHTS = ((F(-3, 100), F(3, 200)), (F(-3, 100), F(3, 200)),
           (F(-11, 200), F(3, 200)), (F(-11, 200), F(3, 200)))
PRECISION = 256
ITERATIONS = 32
CLAMP = F(1, 100000000)
DENOMINATOR = 10**12
ACTION_LOWER = F(3781, 2500)
REQUESTED_GAP = F(1, 100000)
TARGET = ACTION_LOWER-REQUESTED_GAP


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def interval_record(lo, hi):
    require(lo <= hi, 'reversed interval')
    return dict(finite=True, lower_rational=str(lo), upper_rational=str(hi))


def alias_inventory():
    result = []
    for j, name in enumerate(NAMES):
        for sign, height in zip(('negative', 'positive'), HEIGHTS[j]):
            heights = [F(0)]*4
            heights[j] = height
            result.append(dict(name=name+':'+sign, coordinate=name,
                height_index=j, height_rational=str(height),
                heights_rational=list(map(str, heights)),
                real_bounds_rational=[[str(a), str(b)] for a, b in BOUNDS]))
    return result


def solve_four(matrix, rhs):
    """Deterministic partial-pivot solve, used only for float proposals."""
    a = [list(row)+[value] for row, value in zip(matrix, rhs)]
    require(len(a) == 4 and all(len(row) == 5 for row in a), 'solve dimensions')
    for col in range(4):
        pivot = max(range(col, 4), key=lambda row: abs(a[row][col]))
        require(math.isfinite(a[pivot][col]) and a[pivot][col] != 0,
                'singular/nonfinite float proposal system')
        a[col], a[pivot] = a[pivot], a[col]
        for row in range(col+1, 4):
            multiplier = a[row][col]/a[col][col]
            for j in range(col, 5):
                a[row][j] -= multiplier*a[col][j]
    x = [0.0]*4
    for row in (3, 2, 1, 0):
        x[row] = (a[row][4]-sum(a[row][j]*x[j]
                    for j in range(row+1, 4)))/a[row][row]
    require(all(math.isfinite(v) for v in x), 'nonfinite float Newton step')
    return x


def proposal_derivatives(y, heights, K):
    """Original complex derivatives, then real parts; no phase-value calls."""
    s, t, p, q = [complex(v, float(h)) for v, h in zip(y, heights)]
    two_pi_i = 2j*math.pi

    def gp(v):
        return cmath.log(1-cmath.exp(-two_pi_i*v))

    def gpp(v):
        z = cmath.exp(-two_pi_i*v)
        return two_pi_i*z/(1-z)

    def external(v):
        z = K*cmath.exp(-two_pi_i*v)
        return cmath.log(K)-cmath.log(1-z), -two_pi_i*z/(1-z)

    es, hs = external(s)
    eq, hq = external(q)
    grad = [gp(s+t)+es, gp(s+t)+gp(t+p)-2*gp(t)+two_pi_i*p,
            gp(t+p)+gp(p+q)-3*gp(p)+two_pi_i*t,
            gp(p+q)-gp(q)+eq]
    st, tp, pq = gpp(s+t), gpp(t+p), gpp(p+q)
    hess = [[0j]*4 for _ in range(4)]
    for i, value in enumerate((st+hs, st+tp-2*gpp(t),
                              tp+pq-3*gpp(p), pq-gpp(q)+hq)):
        hess[i][i] = value
    for i, value in enumerate((st, tp+two_pi_i, pq)):
        hess[i][i+1] = hess[i+1][i] = value
    real_grad = [v.real for v in grad]
    real_hess = [[v.real for v in row] for row in hess]
    require(all(math.isfinite(v) for v in real_grad+sum(real_hess, [])),
            'nonfinite float proposal derivatives')
    return real_grad, real_hess


def propose(case, K, row):
    heights = list(map(F, case['heights_rational']))
    y = [float((lo+hi)/2) for lo, hi in BOUNDS]
    row['proposal'] = dict(method='fixed clamped Newton; untrusted',
        initial_real_coordinates=y[:], fixed_heights_rational=list(map(str, heights)),
        iterations=[])
    for iteration in range(ITERATIONS):
        entry = dict(index=iteration, coordinates_before=y[:])
        row['proposal']['iterations'].append(entry)
        gradient, hessian = proposal_derivatives(y, heights, K)
        entry.update(real_gradient=gradient, real_hessian=hessian)
        step = solve_four(hessian, gradient)
        damping = 0.5 if iteration < 8 else 1.0
        entry.update(newton_step=step, damping=damping)
        for i, delta in enumerate(step):
            lo, hi = BOUNDS[i]
            y[i] = min(float(hi-CLAMP), max(float(lo+CLAMP), y[i]-damping*delta))
        entry['coordinates_after'] = y[:]
    support = [F(round(v*DENOMINATOR), DENOMINATOR) for v in y]
    require(len(row['proposal']['iterations']) == ITERATIONS, 'iteration inventory')
    row['proposal']['final_real_coordinates'] = y
    row['support_real_coordinates_rational'] = dict(zip(NAMES, map(str, support)))
    row['support_quantization_denominator'] = DENOMINATOR
    for i, (lo, hi) in enumerate(BOUNDS):
        require(lo < support[i] < hi, 'rational support outside real box: '+NAMES[i])
    require(all(0 < support[i]+support[i+1] < 1 for i in range(3)),
            'support sum outside original regular strip')
    require(sum(h != 0 for h in heights) == 1 and
            heights[case['height_index']] == F(case['height_rational']),
            'single-height association')
    row['exact_support_in_box'] = True
    return support, heights


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT/
        'repro/results/research-mixed-contracted-pair-eight-aliases.json')
    args = parser.parse_args()
    # Exclusive output creation precedes every analytic or proposal evaluation.
    with args.output.open('x') as stream:
        inputs = {}
        result = dict(status='initializing', precision_bits=PRECISION,
            scope='Eight full-box horizontal alias bounds only; physical-tail and join bounds and whole-source assembly are separate.',
            protocol_path=PROTOCOL, proof_path=THEORY, contour_path=CONTOUR,
            script_path=str(Path(__file__).resolve().relative_to(ROOT)),
            input_sha256=inputs, cases=[], pending_cases=alias_inventory(),
            action_lower_rational=str(ACTION_LOWER), target_rational=str(TARGET),
            requested_gap_rational=str(REQUESTED_GAP),
            fixed_protocol=dict(case_count=8, real_dimension=4,
                iterations_per_case=ITERATIONS, damping_rational=['1/2']*8+['1']*24,
                clamp_margin_rational=str(CLAMP), support_denominator=DENOMINATOR,
                adaptive_refinement=False, early_convergence=False, retries=False),
            analytic_support_evaluations=0,
            reference_root_solves=0, new_reference_proposals=0)

        def bind(name, expected):
            require(isinstance(expected, str) and len(expected) == 64,
                    'pending/malformed source pin: '+name)
            if name in inputs:
                require(inputs[name] == expected, 'conflicting source pin: '+name)
            actual = sha(ROOT/name)
            require(actual == expected, 'source hash mismatch: '+name)
            inputs[name] = expected

        try:
            for name, expected in PINNED.items():
                bind(name, expected)
            own = result['script_path']
            bind(own, sha(ROOT/own))
            result['script_sha256'] = inputs[own]
            result['protocol_sha256'] = inputs[PROTOCOL]
            result['proof_sha256'] = inputs[THEORY]
            result['contour_sha256'] = inputs[CONTOUR]
            reference = json.loads((ROOT/SOURCE).read_text())
            require(reference['status'] == 'passed', 'reference status')
            require(reference['script_sha256'] == inputs[ROOT_SCRIPT],
                    'reference script association')
            for name, digest in reference['dependencies_sha256'].items():
                bind(name, digest)
            result['inherited_packet_records'] = []
            for name, writer in PACKET_RECORDS:
                packet = json.loads((ROOT/name).read_text())
                require(packet['status'] == 'passed', 'packet status: '+name)
                bind(writer, packet['script_sha256'])
                for dependency, digest in packet['dependencies_sha256'].items():
                    bind(dependency, digest)
                require(packet['reference']['record'] == SOURCE and
                        packet['reference']['sha256'] == inputs[SOURCE],
                        'packet root association: '+name)
                complement = packet['real_complement_input']
                bind(complement['record'], complement['sha256'])
                result['inherited_packet_records'].append(dict(path=name,
                    sha256=inputs[name], generating_script=writer,
                    source_association_verified=True, dependency_hashes_verified=True))
            certificate = reference['root_certificate']
            center = tuple(map(F, certificate['center']))
            radius = F(certificate['complex_disk_radius'])
            require(len(center) == 2 and radius > 0, 'root square metadata')
            result['reference'] = dict(path=SOURCE, sha256=inputs[SOURCE],
                root_certificate_canonical_sha256=canonical(certificate),
                root_center_rational=list(map(str, center)), radius_rational=str(radius),
                root_square_rational=[[str(c-radius), str(c+radius)] for c in center],
                script_and_dependency_hashes_verified=True)

            # No Flint import or numerical proposal occurs before all bindings.
            from flint import arb, acb, ctx
            ctx.prec = PRECISION

            def ar(value):
                value = F(value)
                return arb(value.numerator)/arb(value.denominator)

            def ends(value):
                require(value.is_finite(), 'nonfinite rigorous enclosure')
                return F(str(value.lower().fmpq())), F(str(value.upper().fmpq()))

            def rec(value):
                lo, hi = ends(value)
                return interval_record(lo, hi)

            def crec(value):
                return dict(real=rec(value.real), imag=rec(value.imag))

            def ball(lo, hi):
                out = arb(ar((lo+hi)/2), ar((hi-lo)/2).upper())
                low, high = ends(out)
                require(low <= lo <= hi <= high, 'root square conversion was not outward')
                return out

            root = acb(*(ball(c-radius, c+radius) for c in center))
            denominator = 1+2*root-4*root*root
            require(abs(denominator) > 0, 'rational K denominator is not separated')
            K = 1/denominator
            rho = abs(K)
            require(rho > 0 and rho < 1 and K.real > 0 and K.imag > 0,
                    'original unit-disk first-quadrant branch guard')
            pi, ii = arb.pi(), acb(0, 1)
            logK, dilogK = K.log(), K.polylog(2)
            result['constants'] = dict(actual_root_square=crec(root),
                rational_K_denominator=crec(denominator), K=crec(K), rho=rec(rho),
                log_K=crec(logK), pi=rec(pi), dilogarithm_K=crec(dilogK),
                K_formula='1/(1+2*a-4*a*a)')
            proposal_root = complex(float(center[0]), float(center[1]))
            proposal_K = 1/(1+2*proposal_root-4*proposal_root*proposal_root)
            result['untrusted_proposal_K'] = [proposal_K.real, proposal_K.imag]

            for case in alias_inventory():
                row = dict(case=case, status='initializing')
                result['cases'].append(row)
                result['active_case'] = case['name']
                try:
                    support, heights = propose(case, proposal_K, row)
                    zz = [acb(ar(v), ar(h)) for v, h in zip(support, heights)]
                    row['support_complex_coordinates_rational'] = {
                        name: [str(v), str(h)]
                        for name, v, h in zip(NAMES, support, heights)}
                    for value, exact_re, exact_im in zip(zz, support, heights):
                        lo, hi = ends(value.real)
                        require(lo <= exact_re <= hi, 'real support conversion containment')
                        lo, hi = ends(value.imag)
                        require(lo <= exact_im <= hi, 'height conversion containment')
                    row['support_input_enclosures'] = dict(zip(NAMES, map(crec, zz)))
                    s, t, p, q = zz
                    arguments = dict(st=s+t, tp=t+p, pq=p+q, t=t, p=p, q=q)
                    row['primitive_arguments'] = {
                        name: crec(v) for name, v in arguments.items()}
                    gg, gp = {}, {}
                    row['original_primitive_records'] = primitive_records = {}
                    for name, value in arguments.items():
                        entry = dict(argument=crec(value))
                        primitive_records[name] = entry
                        require(value.real > 0 and value.real < 1,
                                'original g strip guard: '+name)
                        shape = (-2*pi*ii*value).exp()
                        one_minus = 1-shape
                        entry.update(exponential=crec(shape), one_minus=crec(one_minus))
                        require(shape.imag > 0 or shape.imag < 0 or shape.real < 1,
                                'principal dilogarithm cut guard: '+name)
                        require(one_minus.real > 0 or one_minus.imag > 0 or one_minus.imag < 0,
                                'original logarithm cut guard: '+name)
                        require(abs(one_minus) > 0, 'original g prime separation: '+name)
                        dilog = shape.polylog(2)
                        gg[name] = (dilog-pi*pi/6)/(2*pi*ii)
                        gp[name] = one_minus.log()
                        entry.update(dilogarithm=crec(dilog),
                            g=crec(gg[name]), g_prime=crec(gp[name]),
                            regular_strip_and_original_branch_verified=True)
                    integrals, external_prime = {}, {}
                    row['external_primitive_records'] = external_records = {}
                    for name, value in (('s', s), ('q', q)):
                        entry = dict(argument=crec(value))
                        external_records[name] = entry
                        shape = K*(-2*pi*ii*value).exp()
                        one_minus = 1-shape
                        entry.update(exponential=crec(shape), one_minus=crec(one_minus))
                        require(abs(shape) < ar(F(7, 10)),
                                'original external disk guard: '+name)
                        require(one_minus.real > 0, 'external original logarithm guard: '+name)
                        dilog = shape.polylog(2)
                        integrals[name] = (dilog-dilogK)/(2*pi*ii)
                        external_prime[name] = logK-one_minus.log()
                        entry.update(dilogarithm=crec(dilog),
                            I=crec(integrals[name]), incidence_derivative=crec(external_prime[name]),
                            original_disk_and_branch_verified=True)
                    phase = (gg['st']+gg['tp']+gg['pq']-2*gg['t']-3*gg['p']-gg['q']
                        +2*pi*ii*t*p+(s+q-1)*logK-integrals['s']-integrals['q'])
                    gradient = [gp['st']+external_prime['s'],
                        gp['st']+gp['tp']-2*gp['t']+2*pi*ii*p,
                        gp['tp']+gp['pq']-3*gp['p']+2*pi*ii*t,
                        gp['pq']-gp['q']+external_prime['q']]
                    real_gradient = [value.real for value in gradient]
                    height = F(case['height_rational'])
                    debit = 2*pi*ar(abs(height))
                    upper = phase.real-debit
                    row['phase_at_support'] = crec(phase)
                    row['phase_real_at_support'] = rec(phase.real)
                    row['gradient_at_support'] = dict(zip(NAMES, map(crec, gradient)))
                    row['real_gradient_at_support'] = dict(zip(NAMES, map(rec, real_gradient)))
                    row['fourier_debit'] = dict(height_rational=str(height),
                        absolute_height_rational=str(abs(height)),
                        coefficient_of_pi_rational=str(2*abs(height)),
                        interval=rec(debit))
                    row['debited_rate_at_support'] = rec(upper)
                    row['support_terms'] = []
                    for i, (lo, hi) in enumerate(BOUNDS):
                        displacements = (lo-support[i], hi-support[i])
                        products = [real_gradient[i]*ar(d) for d in displacements]
                        endpoint_uppers = [product.upper() for product in products]
                        chosen = max(endpoint_uppers)
                        row['support_terms'].append(dict(coordinate=NAMES[i],
                            displacement_rationals=list(map(str, displacements)),
                            endpoint_products=list(map(rec, products)),
                            endpoint_upper_rationals=[str(ends(v)[1]) for v in endpoint_uppers],
                            chosen_upper_rational=str(ends(chosen)[1])))
                        upper += chosen
                    upper_fraction = ends(upper)[1]
                    row['whole_box_tangent_bound'] = rec(upper)
                    row['whole_box_upper_rational'] = str(upper_fraction)
                    row['strict_target_margin_rational'] = str(TARGET-upper_fraction)
                    row['strict_comparison'] = upper_fraction < TARGET
                    row['status'] = 'passed' if row['strict_comparison'] else 'inconclusive'
                    result['analytic_support_evaluations'] += 1
                except Exception as error:
                    row['status'] = 'failed'
                    row['error'] = dict(type=type(error).__name__, message=str(error))
                result['pending_cases'] = [
                    c for c in result['pending_cases'] if c['name'] != case['name']]
                result['active_case'] = None
            require(len(result['cases']) == 8 and not result['pending_cases'],
                    'eight-case inventory mismatch')
            valid = all(row['status'] in ('passed', 'inconclusive') for row in result['cases'])
            passed = valid and all(row['strict_comparison'] for row in result['cases'])
            result['all_eight_support_bounds_valid'] = valid
            result['all_eight_strict_comparisons_pass'] = passed
            result['status'] = 'passed' if passed else ('inconclusive' if valid else 'failed')
            if valid:
                worst = max(F(row['whole_box_upper_rational']) for row in result['cases'])
                result['maximum_alias_upper_rational'] = str(worst)
                result['alias_gap_lower_rational'] = str(ACTION_LOWER-worst)
            result['physical_tail_claim'] = False
            result['whole_source_claim'] = False
        except BaseException as error:
            result['status'] = 'failed'
            result['error'] = dict(type=type(error).__name__, message=str(error))
        finally:
            changes = []
            for name, expected in inputs.items():
                try:
                    actual = sha(ROOT/name)
                except OSError:
                    actual = None
                if actual != expected:
                    changes.append(dict(path=name, expected=expected, actual=actual))
            result['changed_inputs'] = changes
            result['input_binding_count'] = len(inputs)
            if changes:
                result['status'] = 'failed'
            json.dump(result, stream, indent=2, sort_keys=True, allow_nan=False)
            stream.write('\n')
        print(json.dumps(dict(status=result['status'], cases=len(result['cases']),
            support_bounds=result['analytic_support_evaluations'],
            changed_inputs=len(result['changed_inputs']))))
        return 0 if result['status'] == 'passed' else 1


if __name__ == '__main__':
    sys.exit(main())
