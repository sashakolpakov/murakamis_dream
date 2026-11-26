#!/usr/bin/env python3
"""One saved-only 16-vertex terminal-four factorial comparison.

Only exact rational arithmetic and integer square roots. The old
elementary endpoints and the new certified posterior errors are inputs.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_shared_force_vertices.md'
SOURCE = 'repro/results/research-mixed-terminal-four-input-integral-budget.json'
AUDIT = 'repro/results/research-mixed-terminal-four-input-integral-budget-saved-audit.json'
GAIN = 'experiments/certify_mixed_terminal_four_input_integral_budget.py'
GAIN_CHECKER = 'experiments/check_mixed_terminal_four_input_integral_budget.py'
REFINED = 'repro/results/research-mixed-terminal-quadratic-residual-refinement.json'
REFINED_PROOF = 'notes/research_mixed_terminal_quadratic_residual_refinement.md'
REFINED_CHECKER = 'experiments/check_mixed_terminal_quadratic_residual_refinement.py'
POSTERIOR = 'repro/results/research-mixed-terminal-split-taylor-completion.json'
PINNED = {
    PROOF: '2134390846790b38b6e6451a010d0660e0b7f21fb913739a339173a9771b4a78',
    SOURCE: '9831e8bdbc884cfc0b0c99dbc7f92245403988ae7dc4bbbba86b5606c5a1575e',
    AUDIT: 'cda9eef92856387d0ec0dccca6311512bb980034a07832ab89a99a7bc733d6c3',
    GAIN: '3b806591d88cd461ab7764a6f9c704a048d9c33edb88834a32dbc59a99c91388',
    GAIN_CHECKER: 'd38f41d186bf31d3255861c45cb0500d1a21a4eb1bfd4d366c6a956efc614bf4',
    REFINED: '2834576c2a443c9ffd24032277b5f253d9a85eac17d3f754905812e822a9a331',
    REFINED_PROOF: 'f012610187e14b824fdfeea730bc71ffde1660687ffbdcc491bc945c6a54d596',
    REFINED_CHECKER: '251fc4b3c656201ab5451287577baddb4d4be8122ff34a1318078de0f8501a05',
    POSTERIOR: 'e04521450e1973658cbd602aa0a8f54d4c7d40c968b4b90d65374d570981c617',
}
H = F(1, 100)


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1048576), b''):
            h.update(chunk)
    return h.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()


def interval(value):
    # The audit uses endpoint-only records; the original run adds finite=True.
    if 'finite' in value:
        assert value['finite'] is True
    lo, hi = F(value['lower_rational']), F(value['upper_rational'])
    assert lo <= hi
    return lo, hi


def record(value):
    return dict(lower_rational=str(value[0]), upper_rational=str(value[1]))


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def mul(x, y):
    vals = [a*b for a in x for b in y]
    return min(vals), max(vals)


def contains(outer, inner):
    return outer[0] <= inner[0] <= inner[1] <= outer[1]


def forbidden(*args, **kwargs):
    raise AssertionError('forbidden original evaluator/checker main')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    inputs = dict(PINNED)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs[own] = sha(ROOT/own)
    result = dict(status='initializing', proof_path=PROOF, proof_sha256=PINNED[PROOF],
        source_path=SOURCE, source_sha256=PINNED[SOURCE], audit_sha256=PINNED[AUDIT],
        refinement_sha256=PINNED[REFINED], checker_path=own, checker_sha256=inputs[own],
        input_sha256=inputs, beta=1, epsilon=1, nu=1, vertices=[],
        counts=dict(vertices=0, scalar_cubic_gains=0, independent_gain_checks=0,
            analytic_callbacks=0, original_primitives=0, roots=0, reference_evaluations=0,
            subdivisions=0, retries=0), uniform_factorial_main_gap_proved=False,
        all_four_main_comparisons_proved=False, finite_source_theorem_proved=False,
        global_knot_theorem_proved=False)
    error = None
    try:
        def bind(name, digest):
            assert name not in inputs or inputs[name] == digest, name
            assert sha(ROOT/name) == digest, name
            inputs[name] = digest
        for name, digest in list(inputs.items()):
            bind(name, digest)
        source, audit, refinement, posterior = [json.loads((ROOT/p).read_text())
            for p in (SOURCE, AUDIT, REFINED, POSTERIOR)]
        for data in (source, audit, refinement, posterior):
            assert data['changed_inputs'] == []
            for key in ('input_sha256', 'dependencies_sha256'):
                for name, digest in data.get(key, {}).items():
                    bind(name, digest)
        assert source['status'] == 'completed fixed protocol' and source['all_four_budgets_enclosed']
        assert audit['status'] == 'passed' and audit['source_path'] == SOURCE
        assert audit['source_sha256'] == inputs[SOURCE] and audit['checker_sha256'] == inputs[GAIN_CHECKER]
        assert audit['verified_cotangent_boxes'] == 96 and audit['verified_fourier_budgets'] == 4
        assert audit['epsilon_zero_both_gap_rational'] == '1/400'
        assert audit['epsilon_one_forced_gap_rational'] == '1/150'
        assert refinement['status'] == 'completed fixed saved-only protocol'
        assert refinement['proof_sha256'] == inputs[REFINED_PROOF]
        assert refinement['checker_sha256'] == inputs[REFINED_CHECKER]
        assert refinement['source_path'] == POSTERIOR and refinement['source_sha256'] == inputs[POSTERIOR]
        assert [(c['beta'], c['epsilon']) for c in refinement['cases']] == [(0,0),(0,1),(1,0),(1,1)]
        old = source['cases'][1]; saved = audit['cases'][1]; refined = refinement['cases'][3]
        prior = posterior['posterior_enclosures'][3]
        for c in (old, saved, refined, prior):
            assert (c['beta'], c['epsilon']) == (1,1)
        assert old['source_entry_canonical_sha256'] == canonical_sha(prior)
        assert refined['source_posterior_canonical_sha256'] == canonical_sha(prior)
        assert refined['exact_linear_system_verified'] is True
        for key in ('center_exact','response_exact','parameter_center','parameter_radius_rational'):
            assert refined[key] == prior[key] == old[key]
        assert tuple(map(F, refined['parameter_center'])) == (F('.30'),-F('.052'))
        assert F(refined['parameter_radius_rational']) == F(8,125)
        assert all(0 <= F(new) <= F(previous) for new, previous in zip(
            refined['posterior_radii_rational'],prior['posterior_radii_rational']))
        result['refinement_case_canonical_sha256'] = canonical_sha(refined)
        result['old_case_canonical_sha256'] = canonical_sha(old)
        result['center_exact'] = refined['center_exact']
        result['response_exact'] = refined['response_exact']
        result['posterior_radii_rational'] = refined['posterior_radii_rational']
        result['coordinate_enclosures'] = refined['coordinate_enclosures']
        for name in ('e','xi','t','a','s'):
            for part in ('real','imag'):
                assert contains(interval(old['individual_supports'][name][part]),
                                interval(refined['coordinate_enclosures'][name][part]))
        pi = interval(source['constants']['pi'])
        old_delta = interval(old['height_displacement'])
        assert mul(pi,old_delta) == interval(saved['kappa'])
        means = {name:(F(0),F(0)) for name in ('a','s','t')}
        for slab in old['slabs']:
            assert F(slab['weight_rational']) == F(1,16)
            for name in means:
                value = interval(slab['nodes'][name]['cotangent']['imag'])
                means[name] = add(means[name],mul(value,(F(1,16),F(1,16))))
        assert means == {name:interval(v) for name,v in saved['normalized_Imcot_means'].items()}
        height = interval(refined['coordinate_enclosures']['a']['imag'])
        delta = H-height[1],H-height[0]
        assert delta[0] > 0 and contains(old_delta,delta)
        kappa = mul(pi,delta)
        V = interval(old['normalized_integrals']['V'])
        assert V == interval(saved['normalized_integrals']['V'])
        W_new = mul(mul(kappa,delta),V)
        W_old = interval(old['W']); W_upper = min(W_old[1],W_new[1])
        trial = W_upper-2*pi[0]*H
        result['parameter_intervals'] = dict(kappa=record(kappa),
            Ia=record(means['a']),Is=record(means['s']),It=record(means['t']))
        result['value_narrowing'] = dict(pi=record(pi),old_delta=record(old_delta),
            delta=record(delta),normalized_V=record(V),old_W=record(W_old),new_W=record(W_new),
            chosen_W_upper_rational=str(W_upper),trial_upper_rational=str(trial))

        # Both modules have only standard-library imports and definitions at top level.
        # Their original mains are never called, and no analytic module is imported.
        modules = []
        for name, path in (('frozen_exact_cubic_gains',GAIN),('frozen_exact_gain_audit',GAIN_CHECKER)):
            spec = importlib.util.spec_from_file_location(name,ROOT/path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            module.main = forbidden
            modules.append(module)
        gain_module, check_module = modules
        targets = ((F('.22'),F('.5')),(F('.22'),F('.45')),(F('.22'),F('.4')))
        centers = [interval(refined['coordinate_enclosures'][name]['real']) for name in ('s','a','t')]
        coefficients = (F(88,5),F(98,5),F(88,5))
        for bits in product((0,1),repeat=4):
            k,ia,iss,it = [bound[bit] for bound,bit in zip((kappa,means['a'],means['s'],means['t']),bits)]
            forces = (k*(1-iss),k*(3*ia-iss-it-1),-k*(1+it))
            vertex = dict(endpoint_bits=list(bits),parameters_rational=list(map(str,(k,ia,iss,it))),
                forces_rational=dict(zip(('s','a','t'),map(str,forces))),gains={})
            result['vertices'].append(vertex)
            result['counts']['vertices'] += 1
            total = F(0)
            for name, force, center, target, K in zip(('s','a','t'),forces,centers,targets,coefficients):
                upper,witness = gain_module.gain((force,force),center,target,K)
                result['counts']['scalar_cubic_gains'] += 1
                verified,_ = check_module.check_gain(witness,(force,force),center,target,K)
                result['counts']['independent_gain_checks'] += 1
                assert upper == verified
                vertex['gains'][name] = witness
                total += upper
            vertex['gain_sum_upper_rational'] = str(total)
            vertex['budget_upper_rational'] = str(trial+total)
        assert result['counts']['vertices'] == 16
        assert result['counts']['scalar_cubic_gains'] == result['counts']['independent_gain_checks'] == 48
        worst = max(F(v['budget_upper_rational']) for v in result['vertices'])
        result['worst_budget_upper_rational'] = str(worst)
        result['attaining_vertices'] = [v['endpoint_bits'] for v in result['vertices']
                                       if F(v['budget_upper_rational']) == worst]
        result['uniform_factorial_main_gap_proved'] = worst < 0
        result['all_four_main_comparisons_proved'] = worst < 0
        result['new_factorial_gap_rational'] = str(-worst) if worst < 0 else None
        result['common_all_four_gap_rational'] = str(min(F(1,400),F(1,150),-worst)) if worst < 0 else None
        result['status'] = 'completed fixed saved-only protocol'
    except Exception as exc:
        error = exc
        result['status'] = 'failed saved-data calculation'
        result['error'] = dict(type=type(exc).__name__,message=str(exc))
    result['changed_inputs'] = [name for name,digest in inputs.items() if sha(ROOT/name) != digest]
    if result['changed_inputs']:
        result['status'] = 'changed inputs'
        result['uniform_factorial_main_gap_proved'] = result['all_four_main_comparisons_proved'] = False
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x',encoding='utf-8') as stream:
        json.dump(result,stream,separators=(',',':'));stream.write('\n')
    print(json.dumps(dict(status=result['status'],counts=result['counts'],
        uniform_factorial_main_gap_proved=result['uniform_factorial_main_gap_proved'],
        output_sha256=sha(args.output))))
    if error is not None:raise error


if __name__ == '__main__':main()
