#!/usr/bin/env python3
"""Fixed nine-face tangent test for the original contracted physical tail.

Float Newton proposals are untrusted. Only the exact rational support point,
the pinned concavity theorem and outward Arb bounds certify a face. No root
search, parameter grid, adaptive step, refinement or retry is permitted.
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
PROTOCOL = 'notes/research_mixed_contracted_pair_nine_faces_protocol.md'
THEORY = 'notes/research_mixed_contracted_pair_nine_face_tail.md'
SOURCE = 'repro/results/research-three-four-source-interface.json'
ROOT_SCRIPT = 'experiments/check_three_four_source_interface.py'
PRIMITIVE_SOURCE = 'experiments/check_power_four_real_complement.py'
PACKET_RECORDS = (
    ('repro/results/research-three-vertex-mixed-reference.json',
     'experiments/certify_three_vertex_mixed_reference.py'),
    ('repro/results/research-power-four-index-contours.json',
     'experiments/certify_power_four_index_contours.py'),
)
PINNED = {
    PROTOCOL: '957aadc2dfc00126dd8474d0f3159081001c565326401adeb8f9d69fe43cfa74',
    THEORY: 'fb68bce3c63f60d5aa5bc24469ccfba7120e6d424a9d89f7e902c5ca58c71b7b',
    'notes/research_mixed_contracted_pair_rectangle.md':
        'a784131ce05513342bf86af5c531a5419ad38234f876dbfa9bb22ddbafa5340a',
    'notes/research_mixed_contracted_pair_outer_index_elimination.md':
        '231d52a52fab4f5eb2f10cb7fa721f7be586181c2f2407d9a587cf43370fbf5f',
    SOURCE: '9218011f3f5d41ff15835f74ccf83ccfeb266beea112c67607fa1eaef96ba9dd',
    ROOT_SCRIPT: 'e9d009fdf8712a7577bd9220c8bbf6c2f8fd1d3eefece969cad45357d8a45f91',
    PRIMITIVE_SOURCE: '11ca74230988087ce69a2c25c9adefeef5f6229f13ab82fe7d736876bb6ffa09',
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
BOUNDS = ((F(1, 4), F(9, 20)), (F(1, 4), F(9, 20)),
          (F(1, 5), F(21, 50)), (F(1, 5), F(21, 50)))
PRECISION = 256
ITERATIONS = 32
CLAMP = F(1, 100000000)
DENOMINATOR = 10**12
ACTION_LOWER = F(3781, 2500)
REQUESTED_GAP = F(1, 100000)
TARGET = ACTION_LOWER-REQUESTED_GAP
FAR_UPPER = F(2261, 1500)


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


def face_inventory():
    result = []
    for i, name in enumerate(NAMES):
        for side, value in zip(('lower', 'upper'), BOUNDS[i]):
            result.append(dict(name=name+'='+str(value), fixed_index=i,
                fixed_rational=str(value), central_side=side))
    result.append(dict(name='s=0', fixed_index=0, fixed_rational='0'))
    for face in result:
        face['free_indices'] = [i for i in range(4) if i != face['fixed_index']]
        face['bounds_rational'] = [[str(a), str(b)] for a, b in BOUNDS]
    return result


def solve_three(matrix, rhs):
    """Deterministic partial-pivot Gaussian solve, used only for proposals."""
    a = [list(row)+[value] for row, value in zip(matrix, rhs)]
    require(len(a) == 3 and all(len(row) == 4 for row in a), 'solve dimensions')
    for col in range(3):
        pivot = max(range(col, 3), key=lambda row: abs(a[row][col]))
        require(math.isfinite(a[pivot][col]) and a[pivot][col] != 0,
                'singular/nonfinite float proposal system')
        a[col], a[pivot] = a[pivot], a[col]
        for row in range(col+1, 3):
            multiplier = a[row][col]/a[col][col]
            for j in range(col, 4):
                a[row][j] -= multiplier*a[col][j]
    x = [0.0]*3
    for row in (2, 1, 0):
        x[row] = (a[row][3]-sum(a[row][j]*x[j]
                    for j in range(row+1, 3)))/a[row][row]
    require(all(math.isfinite(v) for v in x), 'nonfinite float Newton step')
    return x


def proposal_derivatives(y, K):
    """Original real rate's gradient/Hessian; no phase values are used."""
    s, t, p, q = y
    rho = abs(K)

    def jp(v):
        return math.log(2*math.sin(math.pi*v))

    def jpp(v):
        return math.pi/math.tan(math.pi*v)

    def external(v):
        z = K*cmath.exp(-2j*math.pi*v)
        return (math.log(rho)-math.log(abs(1-z)),
                2*math.pi*z.imag/abs(1-z)**2)

    es, hs = external(s)
    eq, hq = external(q)
    grad = [jp(s+t)+es, jp(s+t)+jp(t+p)-2*jp(t),
            jp(t+p)+jp(p+q)-3*jp(p), jp(p+q)-jp(q)+eq]
    st, tp, pq = jpp(s+t), jpp(t+p), jpp(p+q)
    hess = [[0.0]*4 for _ in range(4)]
    for i, value in enumerate((st+hs, st+tp-2*jpp(t),
                              tp+pq-3*jpp(p), pq-jpp(q)+hq)):
        hess[i][i] = value
    for i, value in enumerate((st, tp, pq)):
        hess[i][i+1] = hess[i+1][i] = value
    require(all(math.isfinite(v) for v in grad+sum(hess, [])),
            'nonfinite float proposal derivatives')
    return grad, hess


def propose(face, K, row):
    free = face['free_indices']
    y = [float((lo+hi)/2) for lo, hi in BOUNDS]
    y[face['fixed_index']] = float(F(face['fixed_rational']))
    row['proposal'] = dict(method='fixed clamped Newton; untrusted',
        initial_coordinates=y[:], iterations=[])
    for iteration in range(ITERATIONS):
        entry = dict(index=iteration, coordinates_before=y[:])
        row['proposal']['iterations'].append(entry)
        gradient, hessian = proposal_derivatives(y, K)
        g = [gradient[i] for i in free]
        matrix = [[hessian[i][j] for j in free] for i in free]
        entry.update(gradient=g, hessian=matrix)
        step = solve_three(matrix, g)
        damping = 0.5 if iteration < 8 else 1.0
        entry.update(newton_step=step, damping=damping)
        for i, delta in zip(free, step):
            lo, hi = BOUNDS[i]
            y[i] = min(float(hi-CLAMP), max(float(lo+CLAMP), y[i]-damping*delta))
        entry['coordinates_after'] = y[:]
    support = [F(round(v*DENOMINATOR), DENOMINATOR) for v in y]
    support[face['fixed_index']] = F(face['fixed_rational'])
    require(len(row['proposal']['iterations']) == ITERATIONS, 'iteration inventory')
    for i in free:
        lo, hi = BOUNDS[i]
        require(lo < support[i] < hi, 'rational support outside free face interval')
    require(support[face['fixed_index']] == F(face['fixed_rational']),
            'fixed coordinate changed')
    require(all(0 < support[i]+support[i+1] < 1 for i in range(3)),
            'support sum outside original regular strip')
    row['proposal']['final_coordinates'] = y
    row['support_coordinates_rational'] = dict(zip(NAMES, map(str, support)))
    row['support_quantization_denominator'] = DENOMINATOR
    row['exact_support_in_face'] = True
    return support


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT/
        'repro/results/research-mixed-contracted-pair-nine-faces.json')
    args = parser.parse_args()
    # Exclusive creation occurs before any analytic or proposal evaluation.
    with args.output.open('x') as stream:
        inputs = {}
        result = dict(status='initializing', precision_bits=PRECISION,
            scope='Nine full-face physical-tail tangent bounds only; no nonmain complex contour current or whole-source conclusion.',
            protocol_path=PROTOCOL, proof_path=THEORY,
            script_path=str(Path(__file__).resolve().relative_to(ROOT)),
            input_sha256=inputs, faces=[], pending_faces=face_inventory(),
            action_lower_rational=str(ACTION_LOWER), target_rational=str(TARGET),
            requested_gap_rational=str(REQUESTED_GAP), far_region_upper_rational=str(FAR_UPPER),
            fixed_protocol=dict(face_count=9, free_dimension=3,
                iterations_per_face=ITERATIONS, damping_rational=['1/2']*8+['1']*24,
                clamp_margin_rational=str(CLAMP), support_denominator=DENOMINATOR,
                adaptive_refinement=False, early_convergence=False, retries=False),
            analytic_support_evaluations=0)

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
            reference = json.loads((ROOT/SOURCE).read_text())
            require(reference['status'] == 'passed', 'reference status')
            require(reference['script_sha256'] == inputs[ROOT_SCRIPT], 'reference script association')
            for name, digest in reference['dependencies_sha256'].items():
                bind(name, digest)
            result['inherited_packet_records'] = []
            for name, writer in PACKET_RECORDS:
                packet = json.loads((ROOT/name).read_text())
                require(packet['status'] == 'passed', 'packet record status: '+name)
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

            # Flint and numerical work begin only after every inherited binding.
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
            logrho = rho.log()
            dilogK = K.polylog(2)
            result['constants'] = dict(actual_root_square=crec(root),
                rational_K_denominator=crec(denominator), K=crec(K), rho=rec(rho),
                log_rho=rec(logrho), pi=rec(pi), dilogarithm_K=crec(dilogK),
                K_formula='1/(1+2*a-4*a*a)')
            proposal_root = complex(float(center[0]), float(center[1]))
            proposal_K = 1/(1+2*proposal_root-4*proposal_root*proposal_root)
            result['untrusted_proposal_K'] = [proposal_K.real, proposal_K.imag]

            # These are the same J/I formulas as in the pinned
            # check_power_four_real_complement.py; no prior main is imported.
            def J(v):
                value = acb(v)
                return (-ii*pi*(value*value-value)/2
                    +ii*(2*pi*ii*value).exp().polylog(2)/(2*pi)-ii*pi/12).real

            def I(v, z):
                return ((z.polylog(2)-dilogK)/(2*pi*ii)).real

            inventory = face_inventory()
            for face in inventory:
                row = dict(face=face, status='initializing')
                result['faces'].append(row)
                result['active_face'] = face['name']
                try:
                    support = propose(face, proposal_K, row)
                    yy = [ar(v) for v in support]
                    for value, exact in zip(yy, support):
                        lo, hi = ends(value)
                        require(lo <= exact <= hi, 'support conversion containment')
                    row['support_input_enclosures'] = dict(zip(NAMES, map(rec, yy)))
                    s, t, p, q = yy
                    arguments = dict(st=s+t, tp=t+p, pq=p+q, t=t, p=p, q=q)
                    for value in arguments.values():
                        require(value > 0 and value < 1, 'factorial support argument not regular')
                    row['factorial_arguments'] = {name: rec(v) for name, v in arguments.items()}
                    jj, jp = {}, {}
                    row['sine_primitives'] = jj_record = {}
                    row['sine_primitive_derivatives'] = jp_record = {}
                    for name, value in arguments.items():
                        jj[name] = J(value)
                        jj_record[name] = rec(jj[name])
                        sine = (pi*value).sin()
                        require(sine > 0, 'sine-primitive derivative logarithm guard')
                        jp[name] = (2*sine).log()
                        jp_record[name] = dict(sine=rec(sine), derivative=rec(jp[name]))
                    hh, hp = {}, {}
                    row['external_primitives'] = external_record = {}
                    for name, value, exact in (('s', s, support[0]), ('q', q, support[3])):
                        entry = dict(input=rec(value))
                        external_record[name] = entry
                        z = K*(-2*pi*ii*value).exp()
                        separation = abs(1-z)
                        require(separation > 0, 'external logarithm denominator guard')
                        integral = arb(0) if exact == 0 else I(value, z)
                        hh[name] = value*logrho-integral
                        hp[name] = logrho-separation.log()
                        entry.update(z=crec(z), denominator_modulus=rec(separation),
                            integral=rec(integral), exact_zero_integral=(exact == 0),
                            H=rec(hh[name]), derivative=rec(hp[name]))
                    value = (-logrho+jj['st']+jj['tp']+jj['pq']
                             -2*jj['t']-3*jj['p']-jj['q']+hh['s']+hh['q'])
                    gradient = [jp['st']+hp['s'], jp['st']+jp['tp']-2*jp['t'],
                        jp['tp']+jp['pq']-3*jp['p'], jp['pq']-jp['q']+hp['q']]
                    row['E_at_support'] = rec(value)
                    row['gradient_at_support'] = dict(zip(NAMES, map(rec, gradient)))
                    row['support_terms'] = []
                    upper = value
                    for i in face['free_indices']:
                        lo, hi = BOUNDS[i]
                        displacements = (lo-support[i], hi-support[i])
                        products = [gradient[i]*ar(d) for d in displacements]
                        endpoint_uppers = [product.upper() for product in products]
                        chosen = max(endpoint_uppers)
                        # No zero cap: both signed endpoint products are retained.
                        row['support_terms'].append(dict(coordinate=NAMES[i],
                            displacement_rationals=list(map(str, displacements)),
                            endpoint_products=list(map(rec, products)),
                            endpoint_upper_rationals=[str(ends(v)[1]) for v in endpoint_uppers],
                            chosen_upper_rational=str(ends(chosen)[1])))
                        upper += chosen
                    upper_fraction = ends(upper)[1]
                    row['whole_face_tangent_bound'] = rec(upper)
                    row['whole_face_upper_rational'] = str(upper_fraction)
                    row['strict_target_margin_rational'] = str(TARGET-upper_fraction)
                    row['strict_comparison'] = upper_fraction < TARGET
                    row['status'] = 'passed' if row['strict_comparison'] else 'inconclusive'
                    result['analytic_support_evaluations'] += 1
                except Exception as error:
                    row['status'] = 'failed'
                    row['error'] = dict(type=type(error).__name__, message=str(error))
                result['pending_faces'] = [f for f in result['pending_faces'] if f['name'] != face['name']]
                result['active_face'] = None
            require(len(result['faces']) == 9 and not result['pending_faces'], 'face inventory mismatch')
            valid = all(row['status'] in ('passed', 'inconclusive') for row in result['faces'])
            passed = valid and all(row['strict_comparison'] for row in result['faces'])
            result['all_nine_support_bounds_valid'] = valid
            result['all_nine_strict_comparisons_pass'] = passed
            result['status'] = 'passed' if passed else ('inconclusive' if valid else 'failed')
            if valid:
                worst = max(F(row['whole_face_upper_rational']) for row in result['faces'])
                tail = max(worst, FAR_UPPER)
                result['maximum_face_upper_rational'] = str(worst)
                result['whole_physical_complement_upper_rational'] = str(tail)
                result['physical_complement_gap_lower_rational'] = str(ACTION_LOWER-tail)
            result['nonmain_complex_contour_claim'] = False
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
        print(json.dumps(dict(status=result['status'],
            faces=len(result['faces']), support_bounds=result['analytic_support_evaluations'],
            changed_inputs=len(result['changed_inputs']))))
        return 0 if result['status'] == 'passed' else 1


if __name__ == '__main__':
    sys.exit(main())
