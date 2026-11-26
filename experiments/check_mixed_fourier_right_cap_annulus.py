#!/usr/bin/env python3
"""Fixed saved-input rational annulus crossing test; no analytic evaluator.

Eight charts, 64 closed cells per chart, 19 necessary polynomial filters,
and degree-14 Bernstein bounds. No refinement, alternate filter, or retry.
The full witness is streamed to one exclusively created deterministic gzip.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import io
import json
from math import comb
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'repro/results/research-mixed-fourier-boundary-update.json'
WRITER = 'experiments/check_mixed_fourier_boundary_update.py'
ORIGINAL = 'repro/results/research-three-four-source-interface.json'
ORIGINAL_WRITER = 'experiments/check_three_four_source_interface.py'
THEORY = 'notes/research_mixed_fourier_right_cap_correlated_endpoint.md'
PROTOCOL = 'notes/research_mixed_fourier_right_cap_annulus_protocol.md'
OUTPUT = ROOT/'repro/results/research-mixed-fourier-right-cap-annulus.json.gz'
PINNED = {
    SOURCE: '5d4cb057cb82ca4fff826ad768012480fd6f51afe66d3f5c632e48983cf17514',
    WRITER: '5017a53b6417630f1cab1e9c4be3f71d3ad24256af1ca67a8edd8faf0be0b1cc',
    ORIGINAL: '9218011f3f5d41ff15835f74ccf83ccfeb266beea112c67607fa1eaef96ba9dd',
    ORIGINAL_WRITER: 'e9d009fdf8712a7577bd9220c8bbf6c2f8fd1d3eefece969cad45357d8a45f91',
    THEORY: '38702ab726d7dae6dd16e8630df17a5916e43c1efaf055503f51432ad9f1eab6',
    PROTOCOL: '3069c8412a7a9b58e0c55597462d437394be15030ebf239f77e81f198b8d2e90',
    'notes/research_mixed_typed_last_row_envelopes.md':
        '5732f40ffc086acddb21632a5d6af3e4905ebad38f97e62e89953802b1bdd10d',
    'notes/research_mixed_fourier_boundary_critical_existence.md':
        'f7a910f0a2c67701a5dc5c0eb3e5fe8c6dcf20d6a83dbd4876c2363a46fabda6',
    'notes/research_mixed_contracted_pair_enlarged_rectangle.md':
        '597761e942e2956554fe4f25d22de0156838a880e37c04e4fa8fe843e087f0fc',
}
DEGREE = 14
CELLS = 64
RADII = (F(2, 3), F(3, 2))
FILTER_NAMES = (
    'B_negative_real', 'B_negative_imaginary',
    'Q_radial_lower', 'Q_radial_upper', 'Q_negative_imaginary',
    'Q_right_sector', 'Q_left_sector', 'Q_real_upper',
    'S_radial_lower', 'S_radial_upper', 'S_negative_imaginary',
    'S_right_sector', 'S_left_sector', 'S_real_upper',
    'A_radial_lower', 'A_radial_upper', 'A_negative_imaginary',
    'A_right_sector', 'A_left_sector',
)
EXPECTED = dict(charts=8, cells=512, polynomial_uppers=9728,
                bernstein_intervals=145920)


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


# Real intervals have exact Fraction endpoints; no division by an interval.
def point(value):
    value = F(value)
    return value, value


ZERO = point(0)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def neg(a):
    return -a[1], -a[0]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    values = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return min(values), max(values)


def scale(a, value):
    return mul(a, point(value))


def read_interval(value):
    require(value['finite'] is True, 'nonfinite saved interval')
    lo, hi = F(value['lower_rational']), F(value['upper_rational'])
    require(lo <= hi, 'reversed saved interval')
    return lo, hi


def encode(a):
    require(a[0] <= a[1], 'reversed constructed interval')
    return [str(a[0]), str(a[1])]


# Complex intervals are (real interval, imaginary interval).
def cp(real=0, imag=0):
    return point(real), point(imag)


CZ = cp()


def cadd(a, b):
    return add(a[0], b[0]), add(a[1], b[1])


def cneg(a):
    return neg(a[0]), neg(a[1])


def csub(a, b):
    return cadd(a, cneg(b))


def cmul(a, b):
    return (sub(mul(a[0], b[0]), mul(a[1], b[1])),
            add(mul(a[0], b[1]), mul(a[1], b[0])))


def conj(a):
    return a[0], neg(a[1])


# Lists are increasing-power polynomials in the SAME real parameter t.
# They are never interval-evaluated in t during rational-map construction.
def padd(a, b):
    return [cadd(a[i] if i < len(a) else CZ,
                 b[i] if i < len(b) else CZ)
            for i in range(max(len(a), len(b)))]


def psub(a, b):
    return padd(a, [cneg(z) for z in b])


def pmul(a, b):
    out = [CZ for _ in range(len(a)+len(b)-1)]
    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            out[i+j] = cadd(out[i+j], cmul(av, bv))
    return out


def ppow(a, exponent):
    out = [cp(1)]
    for _ in range(exponent):
        out = pmul(out, a)
    return out


def pconj(a):
    return [conj(z) for z in a]


def pencode(a):
    return [[encode(z[0]), encode(z[1])] for z in a]


def radd(a, b):
    return [add(a[i] if i < len(a) else ZERO,
                b[i] if i < len(b) else ZERO)
            for i in range(max(len(a), len(b)))]


def rscale(a, value):
    return [scale(z, value) for z in a]


def rsub(a, b):
    return radd(a, rscale(b, -1))


def invariants(n, d):
    # Taking the real part is valid even if interval overestimation leaves
    # a nonzero imaginary interval in the mathematically real norm square.
    norm_d = [z[0] for z in pmul(d, pconj(d))]
    norm_n = [z[0] for z in pmul(n, pconj(n))]
    product = pmul(n, pconj(d))
    return norm_d, norm_n, [z[0] for z in product], [z[1] for z in product]


def own_filters(n, d):
    t, r, x, i = invariants(n, d)
    return [
        rsub(r, rscale(t, F(21, 40)**2)),
        rsub(rscale(t, F(500, 503)**2), r),
        rsub(rscale(i, -1), rscale(t, F(2, 5))),
        rsub(rscale(x, -1), rscale(i, F(1, 15))),
        rsub(x, rscale(i, F(5, 6))),
        rsub(rscale(t, F(1, 16)), x),
    ]


def incoming_filters(n, d):
    t, r, x, i = invariants(n, d)
    return [
        rsub(r, rscale(t, F(1, 4))),
        rsub(rscale(t, F(43, 28)**2), r),
        rsub(rscale(i, -1), rscale(t, F(1, 5))),
        rsub(rscale(x, -1), rscale(i, F(1, 15))),
        rsub(x, rscale(i, F(9, 4))),
    ]


def construct_chart(y, radius, quadrant):
    one = [cp(1)]
    ypoly = [y]
    rotation = (cp(1), cp(0, 1), cp(-1), cp(0, -1))[quadrant]
    d = [cp(1), cp(0, -1)]
    n = [cmul(cp(radius), rotation), cmul(cp(0, radius), rotation)]
    u = psub(d, pmul(ypoly, n))
    v = padd(pmul(ypoly, d), pmul(psub(one, pmul([cp(2)], ypoly)), n))
    uv = pmul(u, v)
    big_d = pmul(ypoly, uv)
    big_n = psub(psub(pmul(padd(ypoly, one), uv),
                     pmul(ypoly, ppow(u, 2))),
                 pmul(psub(one, ypoly), ppow(v, 2)))
    e = psub(pmul(big_d, v), pmul(big_n, u))
    na = pmul(e, ppow(big_d, 2))
    da = padd(pmul(pmul(big_n, e), big_d),
               pmul(ppow(psub(big_d, big_n), 3), v))
    require(len(u) == len(v) == 2 and len(big_d) == len(big_n) == 3,
            'Q/S rational degree inventory')
    require(len(na) == len(da) == 8, 'A rational degree inventory')
    tb, _, xb, ib = invariants(n, d)
    polynomials = [
        rsub(rscale(xb, -1), rscale(tb, radius/10)),
        rsub(rscale(ib, -1), rscale(tb, 2*radius/5)),
    ] + own_filters(u, v) + own_filters(big_n, big_d) + incoming_filters(na, da)
    require(len(polynomials) == len(FILTER_NAMES) == 19, 'filter inventory')
    for i, poly in enumerate(polynomials):
        require(len(poly) <= DEGREE+1, 'filter degree exceeded')
        polynomials[i] = poly + [ZERO]*(DEGREE+1-len(poly))
    original = dict(d=d, n=n, U=u, V=v, D=big_d, N=big_n, E=e, N_A=na, D_A=da)
    return original, polynomials


def bernstein(poly, cell):
    require(len(poly) == DEGREE+1, 'unpadded power polynomial')
    a, step = F(cell, CELLS), F(1, CELLS)
    shifted = [ZERO for _ in range(DEGREE+1)]
    # t=a+step*u, including the exact 0**0=1 constant substitution.
    for power in range(DEGREE+1):
        for j in range(power+1):
            factor = comb(power, j)*a**(power-j)*step**j
            shifted[j] = add(shifted[j], scale(poly[power], factor))
    out = []
    for k in range(DEGREE+1):
        value = ZERO
        for j in range(k+1):
            value = add(value, scale(shifted[j], F(comb(k, j), comb(DEGREE, j))))
        out.append(value)
    return shifted, out


def elementary_witnesses(out):
    def check(name, left, relation, right):
        left, right = F(left), F(right)
        ok = left < right if relation == '<' else left == right
        item = dict(name=name, left=str(left), relation=relation,
                    right=str(right), passed=ok)
        out.append(item)
        require(ok, 'elementary witness: '+name)

    def exp_upper(x):
        require(0 < x < 3, 'exponential majorant domain')
        return 1+x+x*x/(2*(1-x/3))

    pi_lo, pi_hi = F(157, 50), F(22, 7)
    x = F(2041, 5000)
    check('annulus exponential argument', x, '=', F(13, 100)*pi_lo)
    check('annulus cubic exact surplus', 1+x+x*x/2+x**3/6-F(3, 2),
          '=', F(2137369921, 750000000000))
    check('annulus cubic positive', 0, '<', F(2137369921, 750000000000))
    check('own negative-height argument', F(51, 250)*pi_hi, '<', F(321, 500))
    check('own exp majorant value', exp_upper(F(321, 500)), '=', F(249449, 131000))
    check('own exp majorant surplus', F(40, 21)-F(249449, 131000),
          '=', F(1571, 2751000))
    check('own exp majorant bound', F(249449, 131000), '<', F(40, 21))
    check('own upper-radius pi bound', 3, '<', pi_lo)
    check('own upper-radius identity', 1/(1+F(3, 500)), '=', F(500, 503))
    check('angle v lower', F(879, 1000), '<', F(7, 25)*pi_lo)
    check('angle v upper', F(7, 25)*pi_hi, '=', F(22, 25))
    check('sine positive fifth input', F(7, 8), '<', F(879, 1000))
    check('sine negative seventh input', F(22, 25), '<', F(9, 10))
    sine = F(879, 1000)-F(22, 25)**3/6+F(7, 8)**5/120-F(9, 10)**7/5040
    cosine = 1-F(879, 1000)**2/2+F(22, 25)**4/24
    check('own sine polynomial', F(96, 125), '<', sine)
    check('own cosine polynomial', cosine, '<', F(16, 25))
    check('own imaginary product', F(21, 40)*F(96, 125), '=', F(252, 625))
    check('own imaginary bound', F(2, 5), '<', F(252, 625))
    check('own left sector ratio', F(16, 25)/F(96, 125), '=', F(5, 6))
    check('right-sector angle endpoint', pi_hi/50, '=', F(11, 175))
    check('right-sector denominator positive', 0, '<', 1-F(11, 175)**2/2)
    check('right-sector tangent majorant',
          F(11, 175)/(1-F(11, 175)**2/2), '<', F(1, 15))
    check('own real upper radial correction', 159*pi_hi, '<', 500)
    check('incoming lower-radius argument', F(27, 125)*pi_hi, '<', F(17, 25))
    check('incoming lower exp value', exp_upper(F(17, 25)), '=', F(5739, 2900))
    check('incoming lower exp bound', F(5739, 2900), '<', 2)
    check('incoming upper-radius argument', F(17, 125)*pi_hi, '<', F(3, 7))
    check('incoming upper exp value', exp_upper(F(3, 7)), '=', F(43, 28))
    check('incoming sine angle', F(21, 50), '<', F(67, 500)*pi_lo)
    check('incoming sine bound', F(2, 5), '<', F(21, 50)-F(21, 50)**3/6)
    check('incoming left sector tangent', F(4, 9), '<', F(21, 50)+F(21, 50)**3/3)
    check('beta cosine-sector angle', F(27, 250), '<', F(9, 250)*pi_lo)
    check('beta cosine-sector sine', F(1, 10), '<', F(27, 250)-F(27, 250)**3/6)
    check('beta sine-sector angle', F(21, 50), '<', F(17, 125)*pi_lo)
    return out


class RecordStream:
    """Keep only one cell in memory and still close partial records on failure."""
    def __init__(self, stream):
        self.stream = stream
        self.chart_open = False
        self.charts_written = 0
        self.cells_written = 0
        stream.write('{"schema":"annulus-crossing-v1","charts":[')

    def dump(self, value):
        json.dump(value, self.stream, separators=(',', ':'), sort_keys=True,
                  allow_nan=False)

    def start_chart(self, metadata):
        require(not self.chart_open, 'chart already open')
        if self.charts_written:
            self.stream.write(',')
        self.stream.write('{"construction":')
        self.dump(metadata)
        self.stream.write(',"cells":[')
        self.chart_open = True
        self.cells_written = 0

    def cell(self, data):
        require(self.chart_open, 'cell without chart')
        if self.cells_written:
            self.stream.write(',')
        self.dump(data)
        self.cells_written += 1

    def end_chart(self, status):
        require(self.chart_open, 'ending absent chart')
        self.stream.write('],"status":')
        self.dump(status)
        self.stream.write('}')
        self.chart_open = False
        self.charts_written += 1
        self.stream.flush()

    def finish(self, summary):
        if self.chart_open:
            self.end_chart('calculation_failure')
        self.stream.write('],"summary":')
        self.dump(summary)
        self.stream.write('}\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-sha', required=True)
    args = parser.parse_args()
    # No bound computation happens before exclusive creation. Huge exact
    # integer strings are necessary witness data, not untrusted input.
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    inputs = {}
    counts = {key: 0 for key in EXPECTED}
    result = dict(status='initializing', input_sha256=inputs, counts=counts,
        expected_counts=EXPECTED, excluded_cells=0, unexcluded_cells=[],
        analytic_evaluations=0, source_replays=0, root_solves=0,
        gain_evaluations=0, proposals=0, refinements=0, retries=0,
        annulus_certified=False, actual_auxiliary_K3_certified=False,
        errors=[], elementary_witnesses=[], filter_order=list(FILTER_NAMES), degree=DEGREE,
        chart_radii=list(map(str, RADII)), cells_per_chart=CELLS,
        fallback='none', interval_encoding='[lower_rational,upper_rational]',
        complex_encoding='[real_interval,imag_interval]',
        coefficient_order='increasing powers; Bernstein index 0 through 14',
        scope='Correlated actual endpoint domain only; outgoing halfweight and whole right-cap signs remain unpaid.')

    def bind(name, expected):
        require(isinstance(name, str) and not Path(name).is_absolute() and
                (ROOT/name).resolve().is_relative_to(ROOT), 'invalid input path')
        require(isinstance(expected, str) and len(expected) == 64 and
                all(c in '0123456789abcdef' for c in expected), 'invalid SHA pin')
        if name in inputs:
            require(inputs[name] == expected, 'conflicting binding: '+name)
        actual = sha(ROOT/name)
        require(actual == expected, 'input hash mismatch: '+name)
        inputs[name] = actual

    with OUTPUT.open('xb') as raw:
        with gzip.GzipFile(filename='', mode='wb', fileobj=raw, mtime=0) as zipped:
            with io.TextIOWrapper(zipped, encoding='utf-8', newline='\n') as stream:
                record = RecordStream(stream)
                try:
                    for name, expected in PINNED.items():
                        bind(name, expected)
                    own = str(Path(__file__).resolve().relative_to(ROOT))
                    bind(own, args.script_sha)
                    result.update(script_path=own, script_sha256=inputs[own],
                                  protocol_path=PROTOCOL, theory_path=THEORY)
                    source = json.loads((ROOT/SOURCE).read_text())
                    require(source['status'] == 'passed' and
                            source['inclusion_certified'] is True and
                            source['all_inputs_unchanged'] is True and
                            source['full_analytic_inventory_completed'] is True,
                            'original boundary certificate incomplete')
                    require(source['script_path'] == WRITER and
                            source['script_sha256'] == inputs[WRITER], 'original writer')
                    before = source['input_sha256']
                    require(before == source['input_sha256_after'] and
                            len(before) == source['input_binding_count'] == 20,
                            'old before/after bindings')
                    for name, expected in before.items():
                        bind(name, expected)
                    require(source['visited_arcs'] == source['passed_arcs'] == 512 and
                            source['failed_arcs'] == source['inconclusive_arcs'] == 0,
                            'old boundary inventory')
                    require([a['index'] for a in source['arcs']] == list(range(512)) and
                            all(a['status'] == 'passed' for a in source['arcs']),
                            'old boundary arc associations')
                    require(F(source['maximum_squared_distance']['upper_rational']) <
                            F(41, 500)**2, 'old radius .082 association')
                    original = json.loads((ROOT/ORIGINAL).read_text())
                    require(original['status'] == 'passed' and
                            original['script_sha256'] == inputs[ORIGINAL_WRITER],
                            'original algebraic reference')
                    for name, expected in original['dependencies_sha256'].items():
                        bind(name, expected)
                    reference = source['reference']
                    require(reference['path'] == ORIGINAL and
                            reference['sha256'] == inputs[ORIGINAL] and
                            reference['writer_path'] == ORIGINAL_WRITER and
                            reference['writer_sha256'] == inputs[ORIGINAL_WRITER] and
                            reference['original_success_and_associations_verified'] is True,
                            'boundary-to-reference association')
                    certificate = original['root_certificate']
                    require(canonical(certificate) ==
                            reference['root_certificate_canonical_sha256'],
                            'original root certificate identity')
                    center = list(map(F, certificate['center']))
                    radius = F(certificate['complex_disk_radius'])
                    require(len(center) == 2 and radius > 0 and
                            center == list(map(F, reference['center_rational'])) and
                            radius == F(reference['radius_rational']),
                            'original square center/radius')
                    square = [[c-radius, c+radius] for c in center]
                    require(square == [list(map(F, v)) for v in
                                       reference['full_square_rational']], 'full square identity')
                    constants = source['constants']
                    require(constants['K_formula'] == '1/(1+2*a-4*a*a)' and
                            constants['K_denominator_nonzero'] is True, 'original K formula')
                    for i, part in enumerate(('real', 'imag')):
                        outer = read_interval(constants['full_original_root_square'][part])
                        require(outer[0] <= square[i][0] <= square[i][1] <= outer[1],
                                'full original square containment')
                    y = tuple(read_interval(constants['K'][part])
                              for part in ('real', 'imag'))
                    result['source'] = dict(path=SOURCE, sha256=inputs[SOURCE],
                        writer_sha256=inputs[WRITER], K=constants['K'],
                        K_formula=constants['K_formula'], reference=reference,
                        K_canonical_sha256=canonical(constants['K']),
                        analytic_enclosures_inherited=True)
                    elementary_witnesses(result['elementary_witnesses'])
                    for radius_index, radius in enumerate(RADII):
                        for quadrant in range(4):
                            chart_index = 4*radius_index+quadrant
                            result['active_chart'] = dict(index=chart_index,
                                radius_rational=str(radius), quadrant=quadrant)
                            original_polys, filters = construct_chart(y, radius, quadrant)
                            metadata = dict(result['active_chart'],
                                complex_polynomials={name: pencode(poly)
                                    for name, poly in original_polys.items()},
                                filter_power_coefficients=[
                                    dict(name=name, intervals=[encode(v) for v in poly])
                                    for name, poly in zip(FILTER_NAMES, filters)])
                            record.start_chart(metadata)
                            for cell in range(CELLS):
                                entry = dict(index=cell, parameter_rational=[
                                    str(F(cell, CELLS)), str(F(cell+1, CELLS))],
                                    filters=[], status='initializing',
                                    first_excluding_filter=None)
                                try:
                                    for name, poly in zip(FILTER_NAMES, filters):
                                        shifted, coefficients = bernstein(poly, cell)
                                        upper = max(v[1] for v in coefficients)
                                        entry['filters'].append(dict(name=name,
                                            substituted_power_intervals=[encode(v) for v in shifted],
                                            bernstein_intervals=[encode(v) for v in coefficients],
                                            upper_rational=str(upper), excludes=upper < 0))
                                        counts['polynomial_uppers'] += 1
                                        counts['bernstein_intervals'] += len(coefficients)
                                        if upper < 0 and entry['first_excluding_filter'] is None:
                                            entry['first_excluding_filter'] = name
                                    excluded = entry['first_excluding_filter'] is not None
                                    entry['status'] = 'excluded' if excluded else 'unexcluded'
                                    if excluded:
                                        result['excluded_cells'] += 1
                                    else:
                                        result['unexcluded_cells'].append([chart_index, cell])
                                    counts['cells'] += 1
                                except BaseException as exc:
                                    entry.update(status='calculation_failure', error=repr(exc))
                                    raise
                                finally:
                                    record.cell(entry)
                            record.end_chart('complete')
                            counts['charts'] += 1
                    require(counts == EXPECTED, 'complete fixed inventory')
                    result['all_cells_excluded'] = result['excluded_cells'] == EXPECTED['cells']
                    result['status'] = 'passed' if result['all_cells_excluded'] else 'inconclusive'
                    result.pop('active_chart', None)
                except BaseException as exc:
                    result['status'] = 'calculation_failure'
                    result['errors'].append(repr(exc))
                finally:
                    after = {}
                    for name, expected in inputs.items():
                        try:
                            after[name] = sha(ROOT/name)
                            require(after[name] == expected, 'input changed: '+name)
                        except BaseException as exc:
                            result['status'] = 'calculation_failure'
                            result['errors'].append(repr(exc))
                    result['input_sha256_after'] = after
                    result['input_binding_count'] = len(inputs)
                    result['all_inputs_unchanged'] = after == inputs
                    certified = (result['status'] == 'passed' and
                                 counts == EXPECTED and
                                 result['excluded_cells'] == EXPECTED['cells'] and
                                 result['all_inputs_unchanged'])
                    result['annulus_certified'] = certified
                    result['actual_auxiliary_K3_certified'] = certified
                    record.finish(result)
    print(json.dumps({key: result[key] for key in
          ('status', 'counts', 'excluded_cells', 'input_binding_count',
           'all_inputs_unchanged', 'annulus_certified')}, sort_keys=True))
    print(json.dumps(dict(output=str(OUTPUT.relative_to(ROOT)),
                          compressed_sha256=sha(OUTPUT)), sort_keys=True))
    if result['status'] == 'calculation_failure':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
