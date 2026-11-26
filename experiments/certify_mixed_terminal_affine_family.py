#!/usr/bin/env python3
"""One prescribed affine-family certificate on each complete input disk.

Four old central proposals, four fixed radii per family. No new roots,
subdivision, adaptive radii, analytic primitives, or source sums.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_affine_family_certificate.md'
SOURCE = 'repro/results/research-mixed-terminal-horizontal-envelope-diagnostic.json'
AUDIT = 'repro/results/research-mixed-terminal-horizontal-envelope-saved-audit.json'
CHECKER = 'experiments/check_mixed_terminal_horizontal_envelope_record.py'
PINNED = {
    SOURCE: 'ca58c35640f1e2894f35b0f2c841029ff28b1c4af8411c1a12da012ace09059b',
    AUDIT: 'bedf680b3f57c799980517f7aa6178a7f9c5a0890bac8528947e9018baf7a4de',
    CHECKER: '23545f9f66ec7ba9e2ddb89410f9c198a64f4d615b95df4d346bc2083936cdcb',
    'notes/research_mixed_terminal_horizontal_envelope_diagnostic.md':
        'ea1e6d1daf4b8e3822a198de1f63f4f211061761af8bdd01d641b4d8f930ad72',
    'notes/research_mixed_terminal_one_parameter_transport.md':
        '1fdc3b445ea4a43319f16eeee20e739d608d7133b5471ccb40042174affefddd',
}
NAMES = ('e', 'xi', 't', 'a', 's')
CENTERS = ((F(7, 20), -F(1, 100)), (F(3, 10), -F(13, 250)))
DISK_RADII = (F(9, 100), F(8, 125))
ERROR_RADII = tuple(map(F, ('1/500', '1/1000', '1/200', '1/200', '1/100')))
MULTIPLIERS = tuple(map(F, ('1/4', '1/2', '1', '2')))
COMMON = (('.33', '.47', '-.09', '.08'),
          ('.21', '.25', '.01', '.10')) + (('.23', '.45', '-.12', '.12'),) * 3


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def gradient(q, b, epsilon, pi, ii, log, sin, cos):
    e, xi, t, a, s = q
    half = (pi*0+1)/2
    def j(z):
        return log(2 * sin(pi * z))
    return [
        -j(e-xi)+j(e+t)-epsilon*j(e)+ii*pi*(xi-t+epsilon*(e-half)),
        2*log(cos(pi*xi))+log(sin(pi*(e-xi)))-3*log(sin(pi*xi))+ii*pi*e,
        j(e+t)+j(t+a)-(2+epsilon)*j(t)+ii*pi*(a-e+epsilon*(t-half)),
        j(a+s)+j(t+a)-3*j(a)+ii*pi*(t-s+a-half),
        j(a+s)+j(s+b)-3*j(s)+ii*pi*(b-a+s-half),
    ]


def jacobian(q, b, epsilon, pi, ii, cot, tan):
    e, xi, t, a, s = q
    def jp(z):
        return pi * cot(pi * z)
    U, V, W, X, Y = map(jp, (e-xi, e+t, t+a, a+s, s+b))
    zero = q[0] * 0
    J = [[zero for _ in range(5)] for _ in range(5)]
    J[0][0] = -U+V-epsilon*jp(e)+ii*pi*epsilon
    J[1][1] = -2*pi*tan(pi*xi)-U-3*jp(xi)
    J[2][2] = V+W-(2+epsilon)*jp(t)+ii*pi*epsilon
    J[3][3] = X+W-3*jp(a)+ii*pi
    J[4][4] = X+Y-3*jp(s)+ii*pi
    for i, j, z in ((0, 1, U+ii*pi), (0, 2, V-ii*pi),
                    (2, 3, W+ii*pi), (3, 4, X-ii*pi)):
        J[i][j] = J[j][i] = z
    return J, Y+ii*pi


def matvec(A, x):
    return [sum(a*b for a, b in zip(row, x)) for row in A]


def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(5))
             for j in range(5)] for i in range(5)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    inputs = dict(PINNED)
    for name, digest in inputs.items():
        if sha(ROOT/name) != digest:
            raise ValueError('changed pinned input: '+name)
    source = json.loads((ROOT/SOURCE).read_text())
    audit = json.loads((ROOT/AUDIT).read_text())
    if not (audit['status'] == 'passed' and audit['source_path'] == SOURCE
            and audit['source_sha256'] == inputs[SOURCE]
            and audit['checker_sha256'] == inputs[CHECKER]
            and source['status'] == 'complete fixed diagnostic'
            and source['changed_inputs'] == []):
        raise ValueError('source/audit association failed')
    for name, digest in source['input_sha256'].items():
        if name in inputs and inputs[name] != digest:
            raise ValueError('conflicting source binding: '+name)
        if sha(ROOT/name) != digest:
            raise ValueError('changed inherited binding: '+name)
        inputs[name] = digest
    for name, digest in audit.get('input_sha256', {}).items():
        if name in inputs and inputs[name] != digest:
            raise ValueError('conflicting audit binding: '+name)
        if sha(ROOT/name) != digest:
            raise ValueError('changed inherited audit binding: '+name)
        inputs[name] = digest
    for name in (PROOF, Path(__file__).relative_to(ROOT).as_posix()):
        inputs[name] = sha(ROOT/name)
    if [(c['beta'], c['epsilon']) for c in source['cases']] != [(0, 0), (0, 1), (1, 0), (1, 1)]:
        raise ValueError('wrong case inventory')

    import mpmath as mp
    from flint import arb, acb, ctx
    ctx.prec = 256
    pi, ii = arb.pi(), acb(0, 1)
    counts = dict(inverse_proposals=0, derivative_proposals=0,
                  central_residual_evaluations=0, affine_jacobian_evaluations=0,
                  full_jacobian_evaluations=0, candidates=0,
                  root_solves=0, subdivisions=0, precision_retries=0,
                  primitive_evaluations=0, quantum_source_evaluations=0)

    def rat(x):
        x = F(x)
        return arb(x.numerator)/arb(x.denominator)

    def ends(x):
        if not x.is_finite():
            raise ArithmeticError('nonfinite ball')
        return F(str(x.lower().fmpq())), F(str(x.upper().fmpq()))

    def record(x):
        lo, hi = ends(x)
        return dict(lower_rational=str(lo), upper_rational=str(hi))

    def crecord(z):
        return dict(real=record(z.real), imag=record(z.imag))

    def exact_complex(pair):
        return acb(rat(pair[0]), rat(pair[1]))

    def rectangle(pair, radius):
        parts = []
        for coord in pair:
            lo, hi = coord-radius, coord+radius
            out = arb(rat(coord), rat(radius).upper())
            blo, bhi = ends(out)
            if not blo <= lo <= hi <= bhi:
                raise ArithmeticError('rectangle conversion lost an endpoint')
            parts.append(out)
        return acb(*parts)

    def regular(q, b):
        e, xi, t, a, s = q
        for z in (e-xi, e+t, e, xi, t+a, t, a+s, a, s, s+b):
            if not (z.real > 0 and z.real < 1):
                raise ValueError('original logarithm argument left regular strip')
        if not (xi.real > 0 and xi.real < rat(F(1, 2))):
            raise ValueError('cosine logarithm left original strip')

    def in_common(q):
        return all(z.real > rat(F(bounds[0])) and z.real < rat(F(bounds[1]))
                   and z.imag > rat(F(bounds[2])) and z.imag < rat(F(bounds[3]))
                   for z, bounds in zip(q, COMMON))

    def absupper(z):
        return ends(abs(z))[1]

    def jball(q, b, epsilon):
        regular(q, b)
        return jacobian(q, b, epsilon, pi, ii,
                        lambda z: z.cot(), lambda z: z.tan())

    cases = []
    for saved in source['cases']:
        beta, epsilon = saved['beta'], saved['epsilon']
        row = dict(beta=beta, epsilon=epsilon, status='inconclusive', candidates=[])
        try:
            if not (saved['canonical_reference_certified'] is True
                    and tuple(map(F, saved['outside_coordinate'])) == CENTERS[beta]):
                raise ValueError('central reference not certified/associated')
            center = [tuple(map(F, v)) for v in saved['proposed_centers']]
            bcenter, radius = CENTERS[beta], DISK_RADII[beta]
            with mp.workdps(80):
                def mpr(x):
                    x = F(x)
                    return mp.mpf(x.numerator)/x.denominator
                qm = [mp.mpc(*map(mpr, z)) for z in center]
                bm = mp.mpc(*map(mpr, bcenter))
                Jm, Lm = jacobian(qm, bm, epsilon, mp.pi, mp.j, mp.cot, mp.tan)
                Bm = mp.matrix(Jm)**-1
                um = [-Bm[i, 4]*Lm for i in range(5)]
                def printed(z):
                    return [mp.nstr(z.real, 60), mp.nstr(z.imag, 60)]
                Bprinted = [[printed(Bm[i, j]) for j in range(5)] for i in range(5)]
                uprinted = [printed(z) for z in um]
            counts['inverse_proposals'] += 1
            counts['derivative_proposals'] += 1
            B = [[exact_complex(z) for z in rr] for rr in Bprinted]
            u = [exact_complex(z) for z in uprinted]
            q0, b0 = list(map(exact_complex, center)), exact_complex(bcenter)
            bfull = rectangle(bcenter, radius)
            affine_widths = [radius*absupper(z) for z in u]
            qaff = [rectangle(z, w) for z, w in zip(center, affine_widths)]
            row.update(center=[[str(x) for x in z] for z in center],
                       parameter_center=list(map(str, bcenter)),
                       parameter_radius_rational=str(radius),
                       inverse_proposal=Bprinted, derivative_proposal=uprinted,
                       affine_halfwidths_rational=list(map(str, affine_widths)),
                       affine_coordinate_box=dict(zip(NAMES, map(crecord, qaff))))
            regular(q0, b0)
            f0 = gradient(q0, b0, epsilon, pi, ii,
                          lambda z: z.log(), lambda z: z.sin(), lambda z: z.cos())
            counts['central_residual_evaluations'] += 1
            c = matvec(B, f0)
            Ja, La = jball(qaff, bfull, epsilon)
            counts['affine_jacobian_evaluations'] += 1
            response = matvec(Ja, u)
            response[4] += La
            v = matvec(B, response)
            cplus, vplus = list(map(absupper, c)), list(map(absupper, v))
            resid = [x+radius*y for x, y in zip(cplus, vplus)]
            row.update(preconditioned_center_residual=list(map(crecord, c)),
                       preconditioned_affine_derivative=list(map(crecord, v)),
                       affine_residual_upper_rational=list(map(str, resid)))
            for multiplier in MULTIPLIERS:
                counts['candidates'] += 1
                rho = [multiplier*x for x in ERROR_RADII]
                candidate = dict(multiplier_rational=str(multiplier),
                                 error_radii_rational=list(map(str, rho)),
                                 status='inconclusive')
                try:
                    qfull = [rectangle(z, w+err)
                             for z, w, err in zip(center, affine_widths, rho)]
                    candidate['full_coordinate_box'] = dict(zip(NAMES, map(crecord, qfull)))
                    candidate['inside_original_common_domain'] = in_common(qfull)
                    if not candidate['inside_original_common_domain']:
                        raise ValueError('candidate box not inside original common domain')
                    Jfull, _ = jball(qfull, bfull, epsilon)
                    counts['full_jacobian_evaluations'] += 1
                    BJ = matmul(B, Jfull)
                    E = [[int(i == j)-BJ[i][j] for j in range(5)] for i in range(5)]
                    Eplus = [[absupper(z) for z in rr] for rr in E]
                    linear = [sum(z*r for z, r in zip(rr, rho)) for rr in Eplus]
                    margins = [r-l-v for r, l, v in zip(rho, linear, resid)]
                    eta = max(l/r for l, r in zip(linear, rho))
                    candidate.update(preconditioned_error_matrix=[list(map(crecord, rr)) for rr in E],
                                     error_matrix_upper_rational=[list(map(str, rr)) for rr in Eplus],
                                     linear_error_upper_rational=list(map(str, linear)),
                                     contraction_upper_rational=str(eta),
                                     inclusion_margin_rational=list(map(str, margins)),
                                     criterion_verified=all(m > 0 for m in margins))
                    if candidate['criterion_verified']:
                        candidate['status'] = 'uniform affine enclosure certified'
                except Exception as error:
                    candidate['error'] = type(error).__name__+': '+str(error)
                row['candidates'].append(candidate)
            if any(c['status'] == 'uniform affine enclosure certified' for c in row['candidates']):
                row['status'] = 'uniform affine family certified'
        except Exception as error:
            row['error'] = type(error).__name__+': '+str(error)
        cases.append(row)
        print(json.dumps(dict(beta=beta, epsilon=epsilon, status=row['status'],
                              candidate_statuses=[c['status'] for c in row['candidates']],
                              error=row.get('error'))), flush=True)
    changed = [name for name, digest in inputs.items() if sha(ROOT/name) != digest]
    successful = sum(c['status'] == 'uniform affine family certified' for c in cases)
    result = dict(status='completed fixed protocol' if not changed and len(cases) == 4 else 'input failure',
                  certified_families=successful, cases=cases, counts=counts,
                  precision_bits=256, proposal_digits=80, saved_proposal_digits=60,
                  input_sha256=inputs, changed_inputs=changed,
                  all_full_disk_families_certified=(successful == 4 and not changed),
                  uniform_source_bound_claimed=False, knot_theorem_claimed=False)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as stream:
        stream.write(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status=result['status'], certified_families=successful,
                          sha256=sha(args.output))), flush=True)


if __name__ == '__main__':
    main()
