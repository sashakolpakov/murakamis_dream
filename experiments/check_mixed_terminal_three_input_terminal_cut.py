#!/usr/bin/env python3
"""One saved-only terminal-coordinate cut bound: 32 vertices, 64 rational gains."""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_three_input_terminal_cut_transfer.md'
SOURCE = 'repro/results/research-mixed-terminal-three-input-budget.json.gz'
AUDIT = 'repro/results/research-mixed-terminal-three-input-budget-saved-audit.json'
CORE = 'experiments/certify_mixed_terminal_three_input_budget.py'
GAIN = 'experiments/certify_mixed_terminal_four_input_integral_budget.py'
CHECK = 'experiments/check_mixed_terminal_four_input_integral_budget.py'
REFINED = 'repro/results/research-mixed-terminal-quadratic-residual-refinement.json'
AFFINE = 'repro/results/research-mixed-terminal-correlated-affine-family.json'
PINNED = {
    PROOF: 'd8d22b1fc9b08faadefca6cdd6659bf4ab576715493a98aef6693ff9148e0277',
    SOURCE: '18f5260f3fcd18461d8dd2859d515d9c5180f53127e917debd628ebcf26a0dec',
    AUDIT: '665135dfaa440e31b34281aebb3844845ce7d8e242dc52a9f65aaf31982c2257',
    CORE: '2cdcccac8295666d120d6db4b53e7862bd7e14e538a7e37f854f1b2177bd6dab',
    GAIN: '3b806591d88cd461ab7764a6f9c704a048d9c33edb88834a32dbc59a99c91388',
    CHECK: 'd38f41d186bf31d3255861c45cb0500d1a21a4eb1bfd4d366c6a956efc614bf4',
    REFINED: '2834576c2a443c9ffd24032277b5f253d9a85eac17d3f754905812e822a9a331',
    AFFINE: '51b702aa6ea44aa5891bc1146a7d5c0d22686cd814f9bbe5d9c4c63b9a16f9e1',
}


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT/path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs = dict(PINNED)
    inputs[own] = sha(ROOT/own)
    counts = dict(vertices=0, rational_gains=0, independent_checks=0,
                  analytic_evaluations=0, reference_evaluations=0, retries=0)
    out = dict(status='initializing', input_sha256=inputs, counts=counts,
               proof_path=PROOF, source_path=SOURCE, audit_path=AUDIT,
               target_gap_rational='1/10000', vertices=[], target_passed=False,
               whole_source_theorem_proved=False, knot_theorem_proved=False)
    fatal = None
    try:
        for path, digest in inputs.items():
            assert sha(ROOT/path) == digest, path
        audit = json.loads((ROOT/AUDIT).read_text())
        assert audit['status'] == 'passed' and audit['changed_inputs'] == []
        assert audit['source_path'] == SOURCE and audit['source_sha256'] == PINNED[SOURCE]
        for path, digest in audit['input_sha256'].items():
            assert path not in inputs or inputs[path] == digest, path
            assert sha(ROOT/path) == digest, path
            inputs[path] = digest
        with gzip.open(ROOT/SOURCE, 'rt') as stream:
            source = json.load(stream)
        assert source['status'] == 'completed fixed protocol' and source['changed_inputs'] == []
        c = module('terminal_cut_saved_core', CORE)
        gain = module('terminal_cut_exact_gain', GAIN)
        check = module('terminal_cut_gain_checker', CHECK)
        row = source['cases'][1]
        new = json.loads((ROOT/REFINED).read_text())['cases'][1]
        affine = json.loads((ROOT/AFFINE).read_text())['cases'][1]
        assert (row['beta'], row['epsilon']) == (0, 1)
        assert audit['cases'][1]['source_case_canonical_sha256'] == c.canonical_sha(row)
        assert row['source_associations']['refinement'] == c.canonical_sha(new)
        assert row['source_associations']['affine'] == c.canonical_sha(affine)
        assert new['affine_case_canonical_sha256'] == c.canonical_sha(affine)
        assert row['center_exact'] == new['center_exact'] == affine['center']
        assert row['response_exact'] == new['response_exact'] == affine['response_exact']
        assert row['posterior_radii_rational'] == new['posterior_radii_rational']
        assert F(row['parameter_radius_rational']) == c.RADIUS == F(9, 100)
        assert tuple(map(F, row['parameter_center'])) == c.PARAMETER_CENTER
        centers = dict(zip(c.NAMES, (tuple(map(F, x)) for x in row['center_exact'])))
        responses = dict(zip(c.NAMES, (tuple(map(F, x)) for x in row['response_exact'])))
        eta = dict(zip(c.NAMES, map(F, row['posterior_radii_rational'])))
        candidate, = [x for x in affine['candidates'] if F(x['multiplier_rational']) == 2]
        term, = [x for x in affine['primitive_terms'] if x['name'] == 't+a']
        full, = [x['full_curvature'] for x in candidate['full_primitive_terms'] if x['name'] == 't+a']
        center = c.exact_sum(centers['t'], centers['a'])
        response = c.exact_sum(responses['t'], responses['a'])
        rt, rt_witness = c.norm(c.cx(response))
        wta = c.RADIUS*rt+eta['t']+eta['a']
        ra, ra_witness = c.norm(c.cx(responses['a']))
        wa = c.RADIUS*ra+eta['a']
        out['full_tube'] = dict(center_exact=list(map(str, center)),
            response_exact=list(map(str, response)), response_modulus=rt_witness,
            a_response_modulus=ra_witness, radius_rational=str(wta),
            a_radius_rational=str(wa), original_guard=full)
        assert tuple(map(F, term['center_exact'])) == tuple(map(F, full['center_exact'])) == center
        assert full['regular'] and full['stage'] == 'full'
        assert wta <= F(full['radius_upper_rational'])
        lo, hi = map(F, full['real_interval_rational'])
        assert 0 < lo < hi < 1
        mt = F(full['curvature_upper_rational'])
        assert mt >= c.iv(full['curvature_bound'])[1] > 0
        cut = row['cuts'][0]
        assert cut['name'] == 'cut_left' and F(cut['tau_rational']) == F(3, 20)
        assert F(cut['full_argument_radius_rational']) == wa
        assert tuple(map(F, cut['center_exact'])) == (centers['a'][0]+F(3, 20), centers['a'][1])
        mc = F(cut['curvature_upper_rational'])
        assert mc == c.iv(cut['curvature_bound'])[1] > 0
        pi = c.iv(source['constants']['pi'])
        ipi = (c.Z, pi)
        gp_ta = c.ca(c.cv(term['center_j']),
                     c.cm(ipi, c.cx((F(1, 2)-center[0], -center[1]))))
        gpp_ta = c.csub(c.cv(term['center_j_prime']), ipi)
        D0 = c.ca(c.csub(c.cv(cut['gprime']), gp_ta),
                  c.cm(c.cs(ipi, 2), c.cx((F(3, 20)-centers['t'][0], -centers['t'][1]))))
        Dt = c.csub(c.cn(gpp_ta), c.cs(ipi, 2))
        Da = c.csub(c.cv(cut['gsecond']), gpp_ta)
        LD = c.ca(c.cm(Dt, c.cx(responses['t'])), c.cm(Da, c.cx(responses['a'])))
        rho = c.norm(Dt)[0]*eta['t']+c.norm(Da)[0]*eta['a']+(mc*wa*wa+mt*wta*wta)/2
        delta = c.iv(row['height_displacement'])
        assert delta[0] > 0
        UT, signed = c.signed_product(D0, LD, rho, responses['a'], eta['a'],
                                     c.H-centers['a'][1], delta, -1)
        width = c.RADIUS*c.norm(LD)[0]+rho
        RT = D0[0][0]-width, D0[0][1]+width
        RS = c.iv(cut['ReD'])
        combined = max(RT[0], RS[0]), min(RT[1], RS[1])
        US = F(cut['signed_product']['upper_rational'])
        out['marginal'] = dict(D0=c.cr(D0), Dt=c.cr(Dt), Da=c.cr(Da), L=c.cr(LD),
            rho_rational=str(rho), signed_product=signed,
            terminal_real_interval=c.rec(RT), previous_real_interval=c.rec(RS),
            intersection_rational=list(map(str, combined)),
            terminal_upper_rational=str(UT), previous_upper_rational=str(US))
        assert combined[0] <= combined[1]
        means = {k: c.iv(v) for k, v in row['normalized_Imcot_means'].items()}
        weighted = {k: c.iv(v) for k, v in row['weighted_Recot_means'].items()}
        factor = c.mul(c.mul(pi, delta), delta)
        assert factor == c.iv(row['integrated_values']['pi_delta_squared'])
        normalized = c.sub(c.sub(c.sc(weighted['a'], 3), weighted['s']), weighted['cut_left'])
        W = c.mul(factor, normalized)
        trial = min(US, UT)+W[1]-2*pi[0]*c.H
        parameters = [c.mul(pi, delta), means['a'], means['s'], means['cut_left'], combined]
        assert parameters[0] == c.iv(row['kappa'])
        costs = dict(s=F(88, 5), a=F(49, 5)*(1+F(1, 2)+F(3, 5)))
        out.update(trial_upper_rational=str(trial), W=c.rec(W),
            parameter_order=['kappa', 'Ia', 'Is', 'Icut', 'ReD'],
            parameter_intervals=list(map(c.rec, parameters)),
            costs_rational={n: str(v) for n, v in costs.items()})
        for bits in product((0, 1), repeat=5):
            k, ia, iss, icut, realD = [x[bit] for x, bit in zip(parameters, bits)]
            forces = dict(s=k*(1-iss), a=realD+k*(3*ia-iss-icut-1))
            vertex = dict(endpoint_bits=list(bits), forces_rational={n: str(v) for n, v in forces.items()}, gains={}, checks={})
            out['vertices'].append(vertex)
            total = F(0)
            for name, K in costs.items():
                ref = c.iv(row['individual_supports'][name]['real'])
                target = (F('.22'), F('.5') if name == 's' else F('.45'))
                assert c.contained(target, ref)
                upper, witness = gain.gain(c.ex(forces[name]), ref, target, K)
                counts['rational_gains'] += 1
                checked, detail = check.check_gain(witness, c.ex(forces[name]), ref, target, K)
                counts['independent_checks'] += 1
                assert upper == checked
                vertex['gains'][name], vertex['checks'][name] = witness, detail
                total += upper
            vertex['budget_upper_rational'] = str(trial+total)
            counts['vertices'] += 1
        assert counts['vertices'] == 32 and counts['rational_gains'] == counts['independent_checks'] == 64
        budget = max(F(v['budget_upper_rational']) for v in out['vertices'])
        old, = [x for x in row['comparisons'] if x['label'] == 'four:0' and x['nu'] == 1]
        family = old['source_association']['source_family']
        assert old['source_association']['source_family_canonical_sha256'] == c.canonical_sha(family)
        assert family['series'] == 'four' and family['family'] == 0
        assert family['complete_finite_coverage'] and not family['null_jobs_unresolved']
        bare = F(family['uniform_bare_upper_rational'])
        assert bare == F(old['source_association']['bare_upper_rational'])
        assert bare == max(F(j['decoded_upper_rational']) for j in family['contributing_jobs'])
        result = budget+bare
        out.update(status='completed fixed saved-only protocol',
            source_case_canonical_sha256=c.canonical_sha(row), source_family=family,
            bare_upper_rational=str(bare), budget_upper_rational=str(budget),
            comparison_upper_rational=str(result), previous_comparison=old,
            strictly_negative=result < 0, target_passed=result < -F(1, 10000))
    except (Exception, KeyboardInterrupt) as exc:
        fatal = exc
        out.update(status='failed fixed protocol', error=dict(type=type(exc).__name__, message=str(exc)), target_passed=False)
    out['changed_inputs'] = [p for p, digest in inputs.items() if not (ROOT/p).is_file() or sha(ROOT/p) != digest]
    if out['changed_inputs']:
        out.update(status='changed inputs', target_passed=False)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as stream:
        json.dump(out, stream, sort_keys=True, indent=2)
        stream.write('\n')
    print(json.dumps(dict(status=out['status'], counts=counts, target_passed=out['target_passed'], output_sha256=sha(args.output))), flush=True)
    if fatal is not None:
        raise fatal
    if out['changed_inputs']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
