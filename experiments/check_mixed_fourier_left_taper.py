#!/usr/bin/env python3
"""One fixed interval certificate for the two left-contour derivatives."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
THEORY = 'notes/research_mixed_fourier_left_taper_reduction.md'
PROTOCOL = 'notes/research_mixed_fourier_left_taper_protocol.md'
WALL = 'repro/results/research-mixed-fourier-wall-degree-separation.json'
WALL_WRITER = 'experiments/check_mixed_fourier_wall_degree_separation.py'
SOURCE = 'repro/results/research-mixed-fourier-boundary-update.json'
WRITER = 'experiments/check_mixed_fourier_boundary_update.py'
ORIGINAL = 'repro/results/research-three-four-source-interface.json'
ORIGINAL_WRITER = 'experiments/check_three_four_source_interface.py'
OUTPUT = ROOT / 'repro/results/research-mixed-fourier-left-taper.json'
PINS = {
    THEORY: 'eb64296ffe3ad8849a3350f1155ca34d30bbc34003ff7a397a513e6b143d5801',
    PROTOCOL: 'af9426ee67af62acc8cec618f8dd27c647e0b9fff958b87dc87c4573d9c936c3',
    WALL: '4b2f7b4da3bc30a485041e9530092bd0206fe4eaaf889f1d3981d0fdd1288846',
    WALL_WRITER: '142d1f2911ba727d1a1ea230a2a9cdeb189ec827a2b6398c337cf648474627db',
    SOURCE: '5d4cb057cb82ca4fff826ad768012480fd6f51afe66d3f5c632e48983cf17514',
    WRITER: '5017a53b6417630f1cab1e9c4be3f71d3ad24256af1ca67a8edd8faf0be0b1cc',
    ORIGINAL: '9218011f3f5d41ff15835f74ccf83ccfeb266beea112c67607fa1eaef96ba9dd',
    ORIGINAL_WRITER: 'e9d009fdf8712a7577bd9220c8bbf6c2f8fd1d3eefece969cad45357d8a45f91',
}
K_CANONICAL = '00f030c9a079403c2811e9b1c0dcca898ca8d912f4c11c0e338b3cc655a89591'
ROOT_CANONICAL = 'f04e925c094ba2f2c6723d3321cb58ac4988255b52e3408c2895b662bcf1cf8f'
NX, NL, PRECISION, SCALE = 512, 256, 256, 2**40
X0, X1, L0, L1 = F(1, 100), F(11, 50), F(0), F(51, 110)
EXPECTED = dict(pi=1, log_Y=1, circle_exp=3*NX,
                radial_exp=NX*NL, source_log=4*NX*NL)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                      allow_nan=False).encode()).hexdigest()


def saved_interval(value):
    require(value['finite'] is True, 'nonfinite saved input')
    lo, hi = F(value['lower_rational']), F(value['upper_rational'])
    require(lo <= hi, 'reversed saved input')
    return lo, hi


def run(result, expected_script):
    inputs = result['input_sha256']

    def bind(name, expected):
        path = ROOT / name
        require(not Path(name).is_absolute() and path.resolve().is_relative_to(ROOT)
                and path.resolve() != OUTPUT.resolve(), 'invalid input path')
        require(isinstance(expected, str) and len(expected) == 64
                and all(c in '0123456789abcdef' for c in expected), 'invalid pin')
        if name in inputs:
            require(inputs[name] == expected, 'conflicting pin: '+name)
        actual = sha(path)
        require(actual == expected, 'input hash mismatch: '+name)
        inputs[name] = actual

    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    bind(own, expected_script)
    for name, expected in PINS.items():
        bind(name, expected)
    result.update(script_path=own, script_sha256=inputs[own],
                  protocol_sha256=inputs[PROTOCOL], theory_sha256=inputs[THEORY])
    wall = json.loads((ROOT/WALL).read_text())
    require(wall['status'] == 'passed' and wall['all_cells_passed'] is True
            and wall['all_inputs_unchanged'] is True
            and wall['degree_root_separation_certified'] is True,
            'incomplete inherited Wall certificate')
    require(wall['script_path'] == WALL_WRITER
            and wall['script_sha256'] == inputs[WALL_WRITER], 'Wall writer mismatch')
    require(wall['input_sha256'] == wall['input_sha256_after'], 'Wall bindings changed')
    for name, expected in wall['input_sha256'].items():
        bind(name, expected)
    source = json.loads((ROOT/SOURCE).read_text())
    require(source['status'] == 'passed' and source['inclusion_certified'] is True
            and source['all_inputs_unchanged'] is True
            and source['full_analytic_inventory_completed'] is True,
            'incomplete original boundary certificate')
    require(source['script_path'] == WRITER and source['script_sha256'] == inputs[WRITER],
            'boundary writer mismatch')
    require(source['input_sha256'] == source['input_sha256_after'],
            'boundary bindings changed')
    for name, expected in source['input_sha256'].items():
        bind(name, expected)
    original = json.loads((ROOT/ORIGINAL).read_text())
    require(original['status'] == 'passed'
            and original['script_sha256'] == inputs[ORIGINAL_WRITER],
            'original root writer/status mismatch')
    for name, expected in original['dependencies_sha256'].items():
        bind(name, expected)
    certificate = original['root_certificate']
    reference = source['reference']
    require(canonical(certificate) == ROOT_CANONICAL
            == reference['root_certificate_canonical_sha256'], 'root identity mismatch')
    require(reference['path'] == ORIGINAL and reference['sha256'] == inputs[ORIGINAL]
            and reference['writer_path'] == ORIGINAL_WRITER
            and reference['writer_sha256'] == inputs[ORIGINAL_WRITER]
            and reference['original_success_and_associations_verified'] is True,
            'original source association mismatch')
    center = list(map(F, certificate['center']))
    radius = F(certificate['complex_disk_radius'])
    require(len(center) == 2 and radius > 0, 'invalid full root square')
    square = [[c-radius, c+radius] for c in center]
    require(square == [list(map(F, axis)) for axis in reference['full_square_rational']],
            'full root square changed')
    constants = source['constants']
    require(constants['K_formula'] == '1/(1+2*a-4*a*a)'
            and constants['K_denominator_nonzero'] is True, 'original Y formula changed')
    for i, axis in enumerate(('real', 'imag')):
        lo, hi = saved_interval(constants['full_original_root_square'][axis])
        require(lo <= square[i][0] <= square[i][1] <= hi, 'root containment lost')
    require(canonical(constants['K']) == K_CANONICAL
            == wall['source']['K_canonical_sha256'], 'full Y enclosure identity')
    require(constants['K'] == wall['source']['K'], 'Wall Y enclosure mismatch')
    result['source'] = dict(path=SOURCE, sha256=inputs[SOURCE], Y=constants['K'],
                           Y_canonical_sha256=K_CANONICAL,
                           root_certificate_canonical_sha256=ROOT_CANONICAL,
                           full_original_root_square=reference['full_square_rational'])

    # No analytic library is imported before all saved-source checks above.
    from flint import arb, acb, ctx
    ctx.prec = PRECISION

    def ar(value):
        value = F(value)
        return arb(value.numerator)/arb(value.denominator)

    def ends(value):
        require(value.is_finite(), 'nonfinite interval')
        return F(str(value.lower().fmpq())), F(str(value.upper().fmpq()))

    def ball(lo, hi):
        require(lo <= hi, 'reversed input interval')
        value = arb(ar((lo+hi)/2), ar((hi-lo)/2).upper())
        low, high = ends(value)
        require(low <= lo <= hi <= high, 'interval conversion not outward')
        return value

    def evaluate(name, operation):
        result['analytic_calls'][name]['attempted'] += 1
        require(result['analytic_calls'][name]['attempted'] <= EXPECTED[name],
                'analytic inventory exceeded: '+name)
        value = operation()
        require(value.is_finite(), 'nonfinite analytic output: '+name)
        result['analytic_calls'][name]['completed'] += 1
        return value

    def right_log(value, name):
        require(ends(value.real)[0] > 0, 'logarithm right-half-plane guard')
        result['log_guards_passed'] += 1
        return evaluate(name, value.log)

    def quantize(value):
        lo, hi = ends(value)
        lower, upper = (lo*SCALE).__floor__(), (hi*SCALE).__ceil__()
        require(F(lower, SCALE) <= lo <= hi <= F(upper, SCALE),
                'saved quantization not outward')
        return [lower, upper]

    Y = acb(*(ball(*saved_interval(constants['K'][axis])) for axis in ('real', 'imag')))
    pi = evaluate('pi', arb.pi)
    log_Y = right_log(Y, 'log_Y')
    ii = acb(0, 1)
    lambdas = [ball(L0+(L1-L0)*j/NL, L0+(L1-L0)*(j+1)/NL) for j in range(NL)]
    minimum = None
    for i in range(NX):
        result['active_cell'] = [i, None]
        x = ball(X0+(X1-X0)*i/NX, X0+(X1-X0)*(i+1)/NX)
        circle = [evaluate('circle_exp', lambda offset=offset:
                           (-2*pi*ii*(x+ar(offset))).exp())
                  for offset in (F(0), F(1, 8), F(1, 2))]
        row = dict(x_index=i, cells=[])
        result['rows'].append(row)
        for j, lam in enumerate(lambdas):
            result['active_cell'] = [i, j]
            r = evaluate('radial_exp', lambda: (-2*pi*lam*x).exp())
            rlo, rhi = ends(r)
            require(rlo > 0, 'nonpositive radius enclosure')
            Q = r*circle[0]
            common = log_Y-right_log(1-Q, 'source_log')-right_log(1-Y*Q, 'source_log')
            bounds = []
            for endpoint in circle[1:]:
                target = endpoint.real+lam*endpoint.imag
                blo, bhi = ends(target)
                tlo = min(rlo, max(rlo/2, blo))
                thi = min(rhi, max(rhi/2, bhi))
                t = ball(tlo, thi)
                D = common+right_log(1-t*endpoint, 'source_log')
                bounds.extend(quantize(D.real+lam*D.imag))
            row['cells'].append(bounds)
            result['visited_cells'] += 1
            lower = min(bounds[0], bounds[2])
            minimum = lower if minimum is None else min(minimum, lower)
            if lower > 0:
                result['passed_cells'] += 1
            else:
                result['inconclusive_cells'].append([i, j])
        if (i+1) % 64 == 0:
            print(f'Completed {i+1}/{NX} fixed x intervals; '
                  f'inconclusive cells: {len(result["inconclusive_cells"])}', flush=True)
    result['active_cell'] = None
    require(len(result['rows']) == NX
            and all(row['x_index'] == i and len(row['cells']) == NL
                    for i, row in enumerate(result['rows'])), 'incomplete grid')
    require(result['visited_cells'] == NX*NL, 'cell inventory mismatch')
    require(all(result['analytic_calls'][name] == dict(attempted=count, completed=count)
                for name, count in EXPECTED.items()), 'analytic inventory incomplete')
    require(result['log_guards_passed'] == 1+4*NX*NL, 'branch inventory incomplete')
    result['minimum_lower_integer'] = minimum
    result['minimum_lower_rational'] = str(F(minimum, SCALE))
    result['input_sha256_after'] = {name: sha(ROOT/name) for name in inputs}
    result['all_inputs_unchanged'] = inputs == result['input_sha256_after']
    require(result['all_inputs_unchanged'], 'inputs changed during execution')
    result['positivity_certified'] = not result['inconclusive_cells']
    result['status'] = 'passed' if result['positivity_certified'] else 'inconclusive'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--expected-script-sha256', required=True)
    args = parser.parse_args()
    result = dict(schema='mixed-fourier-left-taper-v1', status='initializing',
                  scope='Only both minimized directional phase derivatives on the fixed rectangle.',
                  theory_path=THEORY, protocol_path=PROTOCOL,
                  precision_bits=PRECISION, x_cells=NX, lambda_cells=NL,
                  x_range=list(map(str, (X0, X1))), lambda_range=list(map(str, (L0, L1))),
                  interval_encoding='Four integers per cell: H_minus lower/upper, H_plus lower/upper; divide by 2^40.',
                  interval_scale=SCALE, rows=[], input_sha256={},
                  analytic_calls={name: dict(attempted=0, completed=0) for name in EXPECTED},
                  expected_analytic_calls=EXPECTED, log_guards_passed=0,
                  visited_cells=0, passed_cells=0, inconclusive_cells=[],
                  root_solves=0, quantum_source_evaluations=0, optimizations=0,
                  refinements=0, precision_changes=0, retries=0, source_replays=0,
                  positivity_certified=False, all_inputs_unchanged=False, errors=[])
    # No second invocation may overwrite an existing result, even a failed one.
    with OUTPUT.open('x') as stream:
        try:
            run(result, args.expected_script_sha256)
        except BaseException as exc:
            result['status'] = 'error'
            result['positivity_certified'] = False
            result['errors'].append(f'{type(exc).__name__}: {exc}')
        finally:
            json.dump(result, stream, sort_keys=True, separators=(',', ':'), allow_nan=False)
            stream.write('\n')
            stream.flush()
    print(json.dumps({key: result[key] for key in
                      ('status', 'visited_cells', 'passed_cells', 'positivity_certified', 'errors')}))
    return 0 if result['status'] == 'passed' else 1


if __name__ == '__main__':
    sys.exit(main())
