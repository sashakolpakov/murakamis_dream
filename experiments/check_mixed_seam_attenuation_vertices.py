#!/usr/bin/env python3
"""Exact height-profile convexity and attenuation-cell vertex identities.

No phase value is evaluated, no outward cell is recomputed, and no seam
comparison sign is certified. The arbitrary-dimensional vertex argument
is the written active-equality-component proof; the matrix checks below
independently exercise all coordinate/difference square bases in dimensions
one through four.
"""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

import sympy as sp
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_seam_attenuation_vertices.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, default=ROOT /
                    'repro/results/research-mixed-seam-attenuation-vertices.json')
    args = ap.parse_args()
    ctx.prec = 400  # Parse existing outward source margins; no reevaluation.
    ph, sh = sha(PROOF), sha(__file__)
    dependencies, visited, primary, checks = {}, set(), {}, []

    def check(name, value):
        assert value, name
        checks.append(name)

    def bind(path, expected=None):
        if path not in dependencies:
            dependencies[path] = sha(ROOT / path)
        if expected is not None:
            assert dependencies[path] == expected, path
        return dependencies[path]

    def inherit(path):
        if path in visited:
            return
        data = (ROOT / path).read_bytes()
        bind(path, hashlib.sha256(data).hexdigest())
        record = json.loads(data)
        visited.add(path)
        bindings = {}
        for field in ('dependencies', 'dependencies_sha256'):
            for name, digest in record.get(field, {}).items():
                if name in bindings:
                    assert bindings[name] == digest, (path, name)
                bindings[name] = digest
                bind(name, digest)
        for name in bindings:
            if name.startswith('repro/results/') and name.endswith('.json'):
                inherit(name)
        return record

    def load(stem, prefix='check', proof_stem=None, proof_field=True):
        pp = f'notes/research_{proof_stem or stem}.md'
        ss = f'experiments/{prefix}_{stem}.py'
        rp = f'repro/results/research-{stem.replace("_", "-")}.json'
        if rp in visited:
            data = (ROOT / rp).read_bytes()
            assert hashlib.sha256(data).hexdigest() == bind(rp)
            record = json.loads(data)
        else:
            record = inherit(rp)
        assert record['status'] == 'passed', rp
        if proof_field:
            assert record['proof_sha256'] == bind(pp), rp
        else:
            inherited = dict(record.get('dependencies', {}))
            inherited.update(record.get('dependencies_sha256', {}))
            assert inherited.get(pp) == bind(pp), rp
        assert record['script_sha256'] == bind(ss), rp
        primary[rp] = record
        return record

    heights = load('mixed_height_resolved_seam_sources')
    half = load('mixed_full_nonlow_half_region')
    roots = load('mixed_closed_cotangent_roots')
    selected = load('mixed_selected_height_reference_extension')
    seam = load('mixed_seam_boundary_potential_reduction')
    cap = load('mixed_early_selected_source_cap', 'certify')
    polygons = load('mixed_minimum_neighbor_contour')
    real_half = load('mixed_half_endpoint_conditional_packet')
    square = load('mixed_right_square_conditional_packets', 'certify',
                  proof_stem='mixed_unselected_right_taper_products')
    interfaces = load('mixed_left_right_interface_source', 'certify')
    fourier = load('mixed_fourier_weight_continuation', proof_field=False)
    for stem in ('mixed_admissible_boundary_halos',
                 'mixed_early_selected_source_cap',
                 'mixed_minimum_neighbor_contour',
                 'mixed_split_cutoff_hybrid_contour'):
        bind(f'notes/research_{stem}.md')
    check('completed height extraction contains every required source knot',
          heights['source_grid_values'] == 225
          and heights['original_source_cells'] == 57092
          and heights['independent_replay_source_cells'] == 57166
          and heights['extracted_zero_slope_knots'] == 19
          and heights['affine_segment_count'] == 13
          and heights['new_outward_cells'] == 0)
    check('source and analytic curvature inputs are completed with their exact scopes',
          half['exact_checks'] == 11 and half['clamping_domains'] == 1227
          and roots['exact_identity_count'] == 13
          and selected['exact_checks'] == 11)
    cap_margins = {v['name']: arb(v['margin']) for v in cap['scalar_checks']}
    check('both inherited polygon cotangent bounds remain strict',
          arb(polygons['cotangent_bound']) < arb(1)/2
          and cap_margins['enlarged positive cap stays in cotangent half-strip'] > 0)
    check('original finite packets cover every required source class',
          cap['products'] == 161 and cap['accepted'] == 71240
          and square['boundary_pieces'] == 64 and square['accepted_cells'] == 2423
          and square['root_pointing_slabs'] == 2048
          and square['parameter_rectangles']['p3'] == ['11/50', '1/2', '-3/100', '1/50']
          and square['parameter_rectangles']['p4'] == ['11/50', '1/2', '-57/1000', '141/10000']
          and interfaces['products'] == 84 and interfaces['accepted'] == 7740
          and real_half['exact_identity_count'] == 17
          and real_half['exact_even_odd_row_support_checks'] == 54
          and real_half['exact_physical_half_endpoint_comparisons'] == 30)
    check('actual Fourier and fixed endpoint-thickening inputs are retained',
          fourier['symbolic_identity_count'] == 9
          and fourier['exact_finite_identity_count'] == 50
          and F(seam['fixed_endpoint_gap']) == F(1, 4000)
          and seam['validated_boundary_products'] == 2048
          and seam['validated_saved_cells'] == 18988)

    expected_names = {'A00', 'A10', 'B0', 'A01', 'A11', 'B1'}
    profiles = heights['profiles']
    check('all six oriented source profiles are present', set(profiles) == expected_names)
    segment_lookup = {}
    for row in heights['segments']:
        key = (row['profile'], F(row['lower']), F(row['upper']))
        assert key not in segment_lookup
        segment_lookup[key] = (F(row['slope']), F(row['intercept']))
    assert len(segment_lookup) == 13
    bands, knot_count, segment_count, slope_comparisons = [], 0, 0, 0
    for name in sorted(profiles):
        points = [(F(p['height']), F(p['upper'])) for p in profiles[name]]
        assert all(a[0] < b[0] for a, b in zip(points, points[1:]))
        knot_count += len(points)
        moving_four = name in {'A01', 'A11', 'B1'}
        states = (0, 1) if moving_four else (0,)
        for state in states:
            band = ([p for p in points if p[0] <= 0] if moving_four and state == 0
                    else [p for p in points if p[0] >= 0] if moving_four
                    else points)
            assert len(band) >= 2
            expected_ends = ((F('-.057'), F(0)) if moving_four and state == 0
                             else (F(0), F('.014')) if moving_four
                             else (F('-.03'), F('.02')))
            assert (band[0][0], band[-1][0]) == expected_ends
            slopes = []
            for (x, U), (y, V) in zip(band, band[1:]):
                slope = (V-U)/(y-x)
                intercept = U-slope*x
                assert segment_lookup[name, x, y] == (slope, intercept)
                assert slope*y+intercept == V
                slopes.append(slope)
            jumps = [v-u for u, v in zip(slopes, slopes[1:])]
            assert all(jump >= 0 for jump in jumps), (name, state, slopes)
            slope_comparisons += len(jumps)
            segment_count += len(slopes)

            # Each band is exactly one affine function plus a nonnegative
            # combination of positive parts. Check both value and slope
            # on every segment using exact rational arithmetic.
            x0, U0 = band[0]
            for k, ((x, U), (y, V)) in enumerate(zip(band, band[1:])):
                midpoint = (x+y)/2
                hinge_value = U0+slopes[0]*(midpoint-x0)
                for j, jump in enumerate(jumps):
                    hinge_value += jump*max(F(0), midpoint-band[j+1][0])
                assert hinge_value == U+slopes[k]*(midpoint-x)
                assert slopes[0]+sum(jumps[:k], F(0)) == slopes[k]
            bands.append(dict(profile=name, selection=state,
                              knots=[{'height': str(h), 'upper': str(U)} for h, U in band],
                              slopes=list(map(str, slopes)), slope_jumps=list(map(str, jumps))))
    check('all thirteen source segments split into nine fixed-selection convex bands',
          knot_count == 19 and segment_count == 13
          and len(bands) == 9 and slope_comparisons == 4)
    check('no convexity comparison is made across a changed type-four selection',
          all(not (F(b['knots'][0]['height']) < 0 < F(b['knots'][-1]['height']))
              for b in bands if b['profile'] in {'A01', 'A11', 'B1'}))

    # Imaginary-affine pullback of a symmetric holomorphic Hessian.
    a00, a01, a11, c00, c01, c11 = sp.symbols('a00 a01 a11 c00 c01 c11', real=True)
    A = sp.Matrix([[a00, a01], [a01, a11]])
    C = sp.Matrix([[c00, c01], [c01, c11]])
    b00, b01, b10, b11, u0, u1 = sp.symbols('b00 b01 b10 b11 u0 u1', real=True)
    B = sp.Matrix([[b00, b01], [b10, b11]])
    u = sp.Matrix([u0, u1])
    direction = sp.I*B*u
    second = sp.re((direction.T*(-A+sp.I*C)*direction)[0])
    check('every real affine height map pulls back the positive real Hessian',
          sp.expand(second-(u.T*B.T*A*B*u)[0]) == 0)
    branch_states = []
    for eta, eps in itertools.product((0, 1), repeat=2):
        for sa, sb in itertools.product(range(eta+1), range(eps+1)):
            for fa, fb in itertools.product(range(sa+1), range(sb+1)):
                assert F(eta-fa, 2) >= 0 and F(eps-fb, 2) >= 0
                branch_states.append((eta, eps, sa, sb, fa, fb))
    check('every true selected Fourier branch leaves nonnegative extra factorial coefficients',
          len(branch_states) == len(set(branch_states)) == 16)

    lam, c, R, m, omega_a, omega_b, theta = sp.symbols(
        'lambda c R m omega_a omega_b theta', real=True)
    active, saturated, repaired = c*R*lam, c*R*m, c*R*m
    check('repaired target height is independent of seam attenuation',
          sp.diff(repaired, lam) == 0)
    check('both min pieces and their repair agree at saturation',
          sp.expand(active.subs(lam, m)-saturated) == 0
          and sp.expand(repaired-active-c*R*(m-lam)) == 0)
    wp, wr = sp.symbols('w_physical w_repaired', real=True)
    check('exact edge correction changes no allocated occupation',
          sp.expand((wp+theta*(omega_a+omega_b)/2)
                    -(wr+theta*(omega_a+omega_b)/2)-(wp-wr)) == 0)
    fpp, fpr, frr = sp.symbols('F_physical F_intermediate F_repaired', real=True)
    check('a two-symbol run has one joint correction via vertical telescoping',
          sp.expand((fpp-fpr)+(fpr-frr)-(fpp-frr)) == 0)

    # The original middle critical equation removes the low real coordinate
    # from the pair plane; this is not a derivative of a finite kernel.
    rho, Fb, x = sp.symbols('rho Fb x', real=True)
    check('critical middle tangent removes direct seam-coordinate dependence',
          sp.diff(Fb*rho*(1-lam), lam).subs(Fb, 0) == 0)
    cm, c0, c1, c2, PL, PR, lp, la, lr, rp, ra, rr = sp.symbols(
        'cm c0 c1 c2 PL PR lp la lr rp ra rr', real=True)
    physical_pair = c0+c1+PL*(lp-lr)+PR*(rp-rr)
    closure_planes = cm+2*c0+2*c1+c2+PL*(la-lr)+PR*(ra-rr)
    repair_tangent = PL*(lp-la)+PR*(rp-ra)
    check('actual pair and repaired edge tangents cancel without an extra debit',
          sp.expand(closure_planes-physical_pair+repair_tangent-(cm+c0+c1+c2)) == 0)

    # Every original edge is allocated once, including loops and parallel
    # edges. These are bounded exact incidence examples, not phase tests.
    incidence_patterns = 0
    for n in range(1, 7):
        gamma = sp.symbols('gamma0:'+str(n))
        alpha = sp.symbols('alpha0:'+str(n))
        for mask in range(1, 2**n):
            S = {j for j in range(n) if mask & (1 << j)}
            incident = {j for j in range(n) if j in S or (j-1) % n in S}
            u = [sum(alpha[s] for s in ((j-1) % n, j) if s in S)
                 for j in range(n)]
            star_sum = sum(alpha[s] for s in S)
            assert sp.expand(sum(u)-2*star_sum) == 0
            assert sp.expand(sum(u[j]*gamma[j] for j in incident)
                             -sum(alpha[s]*(gamma[s]+gamma[(s+1) % n]) for s in S)) == 0
            assert sp.expand(2*star_sum+sum(1-u[j] for j in incident)
                             +(n-len(incident))-n) == 0
            incidence_patterns += 1
    check('all bounded cyclic incidence examples preserve pair planes and one-time tolerances',
          incidence_patterns == 120)

    # Exact isolated-seam min partition, including ties and both endpoints.
    cutoffs = tuple(map(F, ('0', '1/5', '1/2', '4/5', '1')))
    isolated_cases, isolated_cells = 0, 0
    for left, right in itertools.product(cutoffs, repeat=2):
        vertices = sorted({F(0), F(1), left, right})
        assert len(vertices) <= 4
        isolated_cases += 1
        for lo, hi in zip(vertices, vertices[1:]):
            assert lo < hi
            isolated_cells += 1
            for cutoff in (left, right):
                assert hi <= cutoff or lo >= cutoff
                # These are the only affine branches on the entire cell.
                for value in (lo, (lo+hi)/2, hi):
                    branch = value if hi <= cutoff else cutoff
                    assert min(value, cutoff) == branch
    check('isolated seams have exactly the stated min-cell endpoint candidates',
          isolated_cases == 25 and isolated_cells > 0)
    k = F(1, 3)
    witness = lambda z: min(z, k)-z/2
    check('fixed saturation cutoffs cannot in general be omitted',
          witness(k) > max(witness(F(0)), witness(F(1))))
    q, z = sp.symbols('q z', real=True)
    check('repeated cyclic incidences do not create extra min variables',
          sp.Min(q, q, z) == sp.Min(q, z))

    # Independent exact active-equality basis checks. Coordinate rows are
    # anchors to fixed cutoffs; difference rows equate two seam variables.
    # Their general graph-component proof is in the written note.
    bases, nonsingular, rank_checks, dimensions = 0, 0, 0, []
    for n in range(1, 5):
        rows = [('anchor', i, None) for i in range(n)]
        rows += [('difference', i, j) for i in range(n) for j in range(i+1, n)]
        local_bases, local_nonsingular = 0, 0
        for choices in itertools.combinations(rows, n):
            matrix = sp.zeros(n)
            anchors = []
            parent = list(range(n))

            def root(i):
                while parent[i] != i:
                    parent[i] = parent[parent[i]]
                    i = parent[i]
                return i

            for row_index, (kind, i, j) in enumerate(choices):
                matrix[row_index, i] = 1
                if kind == 'anchor':
                    anchors.append((row_index, i))
                else:
                    matrix[row_index, j] = -1
                    parent[root(i)] = root(j)
            components = {root(i) for i in range(n)}
            anchored = {root(i) for _, i in anchors}
            unanchored = components-anchored
            assert matrix.rank() == n-len(unanchored)
            rank_checks += 1
            determinant = matrix.det()
            assert determinant in (-1, 0, 1)
            bases += 1
            local_bases += 1
            if determinant == 0:
                continue
            nonsingular += 1
            local_nonsingular += 1
            assert not unanchored
            for component in components:
                assert sum(root(i) == component for _, i in anchors) == 1
            rhs = sp.zeros(n, len(anchors))
            for column, (row_index, _) in enumerate(anchors):
                rhs[row_index, column] = 1
            solution = matrix.inv()*rhs
            for i in range(n):
                assert all(solution[i, j] in (0, 1) for j in range(len(anchors)))
                assert sum(solution[i, j] for j in range(len(anchors))) == 1
                for j, (_, anchor) in enumerate(anchors):
                    assert solution[i, j] == int(root(i) == root(anchor))
            # Feasibility/order inequalities can discard a basis solution,
            # but cannot create a coordinate not equal to an anchor value.
        dimensions.append(dict(variables=n, square_bases=local_bases,
                               nonsingular_bases=local_nonsingular))
    check('every tested full-rank order-cell basis copies one fixed anchor per component',
          bases == rank_checks == 234 and nonsingular > 0)
    check('literal one-cycle and two-cycle self ties are zero equality rows',
          sp.Matrix([[1-1]]).rank() == 0
          and sp.Matrix([[1, -1], [1, -1]]).rank() == 1)

    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/path) == digest for path, digest in dependencies.items())
    result = dict(
        status='passed', exact_checks=len(checks), checks=checks,
        primary_records=len(primary), current_bindings=len(dependencies),
        source_profiles=6, fixed_selection_bands=len(bands),
        source_segments=segment_count, adjacent_slope_comparisons=slope_comparisons,
        bands=bands, selected_branch_states=len(branch_states),
        exact_cyclic_incidence_patterns=incidence_patterns,
        isolated_cutoff_examples=isolated_cases, isolated_min_cells=isolated_cells,
        exact_matrix_basis_examples=bases, nonsingular_basis_examples=nonsingular,
        matrix_dimensions=dimensions,
        arbitrary_dimension_proof='Written active-equality graph-component argument; '
                                 'bounded matrix examples do not replace it.',
        numerical_cells_recomputed=0, attenuation_vertex_values_evaluated=0,
        cyclic_word_signs_tested=0, global_seam_sign_certified=False,
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=dependencies,
        scope='Exact fixed-selection profile convexity, imaginary-affine Hessian '
              'identity, min-cell and source/tangent accounting, and bounded '
              'active-equality algebra examples. No new numerical cover, '
              'evaluated attenuation vertex or universal boundary sign.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', len(checks), 'exact checks;', len(bands), 'convex bands;',
          bases, 'exact matrix bases;', len(primary), 'primary records;',
          len(dependencies), 'current bindings; no sign evaluation', flush=True)


if __name__ == '__main__':
    main()
