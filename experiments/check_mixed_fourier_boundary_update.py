#!/usr/bin/env python3
"""Fixed whole-circle inclusion test for the original Fourier boundary map.

Uses the complete previously certified interface-root square. There are
exactly 512 prescribed arcs at 256 bits, with no reference solve, proposal,
refinement, alternative logarithm branch, precision change or retry.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
THEORY = 'notes/research_mixed_fourier_boundary_update.md'
PROTOCOL = 'notes/research_mixed_fourier_boundary_update_protocol.md'
SOURCE = 'repro/results/research-three-four-source-interface.json'
WRITER = 'experiments/check_three_four_source_interface.py'
OUTPUT = ROOT/'repro/results/research-mixed-fourier-boundary-update.json'
PINNED = {
    THEORY: '9ff05c7f6eb759d53a3717e57b475c58904ccd35d5c232e1abdbe8b35ec49f74',
    PROTOCOL: 'cc8176390334bf39e0c9cf1894fbba0ed520eee811eaf26835f3010e4e6feffd',
    SOURCE: '9218011f3f5d41ff15835f74ccf83ccfeb266beea112c67607fa1eaef96ba9dd',
    WRITER: 'e9d009fdf8712a7577bd9220c8bbf6c2f8fd1d3eefece969cad45357d8a45f91',
    'notes/research_three_four_source_interface.md':
        '65155a670d3da22f84cf9992eed17d7ad666d6d6e9b2e88fda06088e1069c123',
    'notes/research_mixed_contracted_phase.md':
        'e9e1291b0befb6e552f1e4ae272afc547ec058f68ae9915c7116bbb6b331ac00',
    'notes/research_mixed_open_word_critical_localization.md':
        'a3f8a0f781abd43f8ca17321171081ba37c91b284f83f22a4f7ae34e270424fa',
    'notes/research_mixed_cyclic_critical_localization.md':
        'ccb8b144e6068c434059b707cd13d9aed8bb88a40e7fa0cf0e6bc655bff7fa71',
    'notes/research_mixed_open_word_hessian.md':
        '21556711a3ac410ce7d3e4dda0d3a6395cd7ee2a69993d82f5f8325c6e7dad23',
    'notes/research_mixed_alternating_cap_phase_entrance.md':
        '98ff4eceddadd9cefd08cb2cc01c01a2ab656799fa6580df78c250da425cbf50',
    'notes/research_mixed_three_four_joint_coercivity.md':
        '27200c4d320cf0f6063c34a3f9ab7eb5faca2b2a54a14fc3b6421d52ff597e41',
}
PRECISION = 256
ARC_COUNT = 512
Q_CENTER = (F(3, 10), F(-13, 250))
Q_RADIUS = F(8, 125)
B_CENTER = (F(7, 20), F(-1, 100))
DISTANCE_SQUARED_LIMIT = F(81, 10000)
EXPECTED_COUNTS = {'pi': 1, 'circle_exp': ARC_COUNT,
                   'shape_exp': ARC_COUNT, 'principal_log': ARC_COUNT}


class GuardFailure(Exception):
    """A containing rectangle did not certify a required domain guard."""


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
    data = json.dumps(value, sort_keys=True, separators=(',', ':'),
                      allow_nan=False).encode()
    return hashlib.sha256(data).hexdigest()


def interval_record(lo, hi):
    require(lo <= hi, 'reversed rational interval')
    return dict(finite=True, lower_rational=str(lo), upper_rational=str(hi))


def rational_square(lo, hi):
    require(lo <= hi, 'reversed square input')
    lower = F(0) if lo <= 0 <= hi else min(lo*lo, hi*hi)
    return lower, max(lo*lo, hi*hi)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=OUTPUT)
    args = parser.parse_args()
    require(args.output.resolve() == OUTPUT.resolve(),
            'this protocol has one prescribed output path')
    # Exclusive output creation precedes source parsing and every analytic call.
    with args.output.open('x') as stream:
        inputs = {}
        counters = {name: dict(attempted=0, completed=0)
                    for name in EXPECTED_COUNTS}
        result = dict(status='initializing', precision_bits=PRECISION,
            script_path=str(Path(__file__).resolve().relative_to(ROOT)),
            theory_path=THEORY, protocol_path=PROTOCOL,
            input_sha256=inputs, analytic_calls=counters, arcs=[],
            fixed_protocol=dict(arc_count=ARC_COUNT,
                maximum_analytic_calls=EXPECTED_COUNTS,
                root_solves=0, proposals=0, optimizers=0, gain_calls=0,
                subdivisions=0, precision_changes=0, branch_retries=0),
            source_scope='Whole-D4 Fourier boundary-map inclusion only; no narrower prepared-root image, source tail, alias or whole-message claim.',
            q_center_rational=list(map(str, Q_CENTER)),
            q_radius_rational=str(Q_RADIUS),
            b_center_rational=list(map(str, B_CENTER)),
            distance_squared_limit_rational=str(DISTANCE_SQUARED_LIMIT),
            inclusion_certified=False, errors=[])

        def bind(name, expected):
            require(isinstance(name, str) and
                    (ROOT/name).resolve().is_relative_to(ROOT.resolve()),
                    'invalid binding path')
            require(isinstance(expected, str) and len(expected) == 64,
                    'malformed source pin: '+name)
            if name in inputs:
                require(inputs[name] == expected, 'conflicting pin: '+name)
            actual = sha(ROOT/name)
            require(actual == expected, 'source hash mismatch: '+name)
            inputs[name] = actual

        try:
            for name, expected in PINNED.items():
                bind(name, expected)
            own = result['script_path']
            bind(own, sha(ROOT/own))
            result.update(script_sha256=inputs[own],
                          theory_sha256=inputs[THEORY],
                          protocol_sha256=inputs[PROTOCOL])
            reference = json.loads((ROOT/SOURCE).read_text())
            require(reference['status'] == 'passed', 'original reference status')
            require(reference['script_sha256'] == inputs[WRITER],
                    'original reference writer association')
            inherited = reference['dependencies_sha256']
            require(isinstance(inherited, dict) and inherited,
                    'missing original dependency bindings')
            for name, expected in inherited.items():
                bind(name, expected)
            certificate = reference['root_certificate']
            require(isinstance(certificate['center'], list) and
                    len(certificate['center']) == 2, 'root center schema')
            center = tuple(map(F, certificate['center']))
            radius = F(certificate['complex_disk_radius'])
            require(radius > 0, 'nonpositive original root radius')
            result['reference'] = dict(path=SOURCE, sha256=inputs[SOURCE],
                writer_path=WRITER, writer_sha256=inputs[WRITER],
                root_certificate_canonical_sha256=canonical(certificate),
                center_rational=list(map(str, center)),
                radius_rational=str(radius),
                full_square_rational=[[str(c-radius), str(c+radius)]
                                      for c in center],
                inherited_dependency_count=len(inherited),
                original_success_and_associations_verified=True)

            # All source bindings are checked before Flint is imported.
            from flint import arb, acb, ctx
            ctx.prec = PRECISION

            def ar(value):
                value = F(value)
                return arb(value.numerator)/arb(value.denominator)

            def ends(value):
                if not value.is_finite():
                    raise ArithmeticError('nonfinite rigorous enclosure')
                return (F(str(value.lower().fmpq())),
                        F(str(value.upper().fmpq())))

            def rec(value):
                if not value.is_finite():
                    return dict(finite=False, display=str(value))
                return interval_record(*ends(value))

            def crec(value):
                return dict(real=rec(value.real), imag=rec(value.imag))

            def save_complex(destination, name, value):
                destination[name] = crec(value)
                ends(value.real)
                ends(value.imag)
                return value

            def ball(lo, hi, destination, name):
                require(lo <= hi, 'reversed prescribed interval: '+name)
                value = arb(ar((lo+hi)/2), ar((hi-lo)/2).upper())
                destination[name] = dict(prescribed=interval_record(lo, hi),
                                         enclosure=rec(value))
                low, high = ends(value)
                require(low <= lo <= hi <= high,
                        'interval conversion not outward: '+name)
                destination[name]['outward_containment_verified'] = True
                return value

            def nonzero(value):
                rlo, rhi = ends(value.real)
                ilo, ihi = ends(value.imag)
                return rhi < 0 or rlo > 0 or ihi < 0 or ilo > 0

            def analytic(name, function):
                counters[name]['attempted'] += 1
                require(counters[name]['attempted'] <= EXPECTED_COUNTS[name],
                        'analytic inventory exceeded: '+name)
                value = function()
                counters[name]['completed'] += 1
                return value

            constants = result['constants'] = {}
            conversions = constants['rational_input_conversions'] = {}
            root = acb(*(ball(c-radius, c+radius, conversions, name)
                         for c, name in zip(center, ('root_real', 'root_imag'))))
            save_complex(constants, 'full_original_root_square', root)
            denominator = save_complex(constants, 'K_denominator',
                                       1+2*root-4*root*root)
            require(nonzero(denominator), 'original K denominator not separated')
            K = save_complex(constants, 'K', 1/denominator)
            constants['K_formula'] = '1/(1+2*a-4*a*a)'
            constants['K_denominator_nonzero'] = True
            pi = analytic('pi', arb.pi)
            constants['pi'] = rec(pi)
            pi_lo, pi_hi = ends(pi)
            require(3 < pi_lo <= pi_hi < 4, 'pi enclosure guard')
            ii = acb(0, 1)
            qc = acb(*(ball(v, v, conversions, name) for v, name in
                       zip(Q_CENTER, ('q_center_real', 'q_center_imag'))))
            qr = ball(Q_RADIUS, Q_RADIUS, conversions, 'q_radius')
            bc = acb(*(ball(v, v, conversions, name) for v, name in
                       zip(B_CENTER, ('b_center_real', 'b_center_imag'))))

            for index in range(ARC_COUNT):
                row = dict(index=index, status='initializing', stage='input',
                    parameter_rational=[str(F(index, ARC_COUNT)),
                                        str(F(index+1, ARC_COUNT))],
                    guards={})
                result['arcs'].append(row)
                result['active_arc'] = index

                def guard(name, condition):
                    row['guards'][name] = bool(condition)
                    if not condition:
                        raise GuardFailure(name)

                try:
                    arc_inputs = row['rational_input_conversions'] = {}
                    theta = ball(F(index, ARC_COUNT), F(index+1, ARC_COUNT),
                                 arc_inputs, 'theta')
                    row['stage'] = 'circle_exp'
                    circle_argument = save_complex(row, 'circle_exp_argument',
                                                   2*pi*ii*theta)
                    omega = save_complex(row, 'circle_exp',
                        analytic('circle_exp', circle_argument.exp))
                    q = save_complex(row, 'q', qc+qr*omega)
                    row['stage'] = 'shape_exp'
                    shape_argument = save_complex(row, 'shape_exp_argument',
                                                  -2*pi*ii*q)
                    Q = save_complex(row, 'Q',
                        analytic('shape_exp', shape_argument.exp))
                    row['stage'] = 'mobius'
                    numerator = save_complex(row, 'numerator', 1-K*Q)
                    denominator = save_complex(row, 'denominator', K+(1-2*K)*Q)
                    guard('numerator_nonzero', nonzero(numerator))
                    guard('denominator_nonzero', nonzero(denominator))
                    B = save_complex(row, 'B', numerator/denominator)
                    guard('B_nonzero', nonzero(B))
                    guard('B_strict_lower_half_plane', ends(B.imag)[1] < 0)
                    row['stage'] = 'principal_log'
                    logB = save_complex(row, 'principal_log_B',
                        analytic('principal_log', B.log))
                    log_imag_lo, log_imag_hi = ends(logB.imag)
                    guard('log_imag_strictly_above_minus_pi',
                          log_imag_lo > -pi_lo)
                    guard('log_imag_strictly_below_zero', log_imag_hi < 0)
                    row['stage'] = 'boundary_image'
                    b = save_complex(row, 'b', -logB/(2*pi*ii))
                    blo, bhi = ends(b.real)
                    guard('b_real_strictly_above_zero', blo > 0)
                    guard('b_real_strictly_below_half', bhi < F(1, 2))
                    row['stage'] = 'squared_distance'
                    difference = save_complex(row, 'b_minus_center', b-bc)
                    dr, di = difference.real, difference.imag
                    real_square, imag_square = dr**2, di**2
                    square_sum = real_square+imag_square
                    row['arb_squared_distance'] = dict(
                        real_square=rec(real_square), imag_square=rec(imag_square),
                        sum=rec(square_sum))
                    # These exact endpoint squares are independent outward
                    # witnesses. No equality with Arb's rounded endpoints is
                    # assumed or needed.
                    rlo, rhi = rational_square(*ends(dr))
                    ilo, ihi = rational_square(*ends(di))
                    rational_hi = rhi+ihi
                    arb_hi = ends(square_sum)[1]
                    row['rational_squared_distance'] = dict(
                        real_square=interval_record(rlo, rhi),
                        imag_square=interval_record(ilo, ihi),
                        sum=interval_record(rlo+ilo, rational_hi))
                    upper = max(arb_hi, rational_hi)
                    row.update(arb_distance_test=arb_hi < DISTANCE_SQUARED_LIMIT,
                        rational_distance_test=rational_hi < DISTANCE_SQUARED_LIMIT,
                        conservative_squared_distance_upper_rational=str(upper),
                        strict_margin_rational=str(DISTANCE_SQUARED_LIMIT-upper),
                        stage='complete')
                    row['status'] = ('passed' if row['arb_distance_test'] and
                                     row['rational_distance_test'] else 'inconclusive')
                except GuardFailure as exc:
                    row.update(status='inconclusive', guard_failure=str(exc),
                               error_type=type(exc).__name__)
                except Exception as exc:
                    row.update(status='failed', error=str(exc),
                               error_type=type(exc).__name__)
                    result['errors'].append(dict(arc=index, stage=row['stage'],
                        error_type=type(exc).__name__, error=str(exc)))

            require([row['index'] for row in result['arcs']] ==
                    list(range(ARC_COUNT)), 'original arc inventory')
            result['visited_arcs'] = len(result['arcs'])
            result['passed_arcs'] = sum(row['status'] == 'passed'
                                       for row in result['arcs'])
            result['inconclusive_arcs'] = sum(row['status'] == 'inconclusive'
                                             for row in result['arcs'])
            result['failed_arcs'] = sum(row['status'] == 'failed'
                                       for row in result['arcs'])
            result['full_analytic_inventory_completed'] = all(
                counters[name]['attempted'] == count and
                counters[name]['completed'] == count
                for name, count in EXPECTED_COUNTS.items())
            bounded = [row for row in result['arcs']
                       if 'conservative_squared_distance_upper_rational' in row]
            if bounded:
                worst = max(bounded, key=lambda row:
                    F(row['conservative_squared_distance_upper_rational']))
                result['maximum_squared_distance'] = dict(arc=worst['index'],
                    upper_rational=worst['conservative_squared_distance_upper_rational'],
                    strict_margin_rational=worst['strict_margin_rational'])
            result['inclusion_certified'] = (
                result['passed_arcs'] == ARC_COUNT and
                result['full_analytic_inventory_completed'] and not result['errors'])
            result['status'] = ('passed' if result['inclusion_certified'] else
                                'failed' if result['errors'] else 'inconclusive')
        except Exception as exc:
            result['status'] = 'failed'
            result['inclusion_certified'] = False
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
                    after[name] = dict(error_type=type(exc).__name__,
                                       error=str(exc))
                    changed.append(name)
            result['input_sha256_after'] = after
            result['changed_inputs'] = changed
            result['input_binding_count'] = len(inputs)
            result['all_inputs_unchanged'] = not changed
            if changed:
                result['status'] = 'failed'
                result['inclusion_certified'] = False
                result['errors'].append(dict(stage='final_bindings',
                                             changed_inputs=changed))
            result.pop('active_arc', None)
            json.dump(result, stream, indent=2, sort_keys=True, allow_nan=False)
            stream.write('\n')

    print(json.dumps(dict(status=result['status'],
        inclusion_certified=result['inclusion_certified'],
        visited_arcs=result.get('visited_arcs', len(result['arcs'])),
        passed_arcs=result.get('passed_arcs', 0),
        analytic_calls=counters, input_bindings=len(inputs),
        all_inputs_unchanged=result['all_inputs_unchanged'],
        output=str(args.output), output_sha256=sha(args.output)), sort_keys=True))
    return 0 if result['status'] in ('passed', 'inconclusive') else 1


if __name__ == '__main__':
    sys.exit(main())
