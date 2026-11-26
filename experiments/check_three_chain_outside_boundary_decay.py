#!/usr/bin/env python3
"""Check the cap-domain and scalar inputs of outside-boundary decay.

This reuses validated critical-coordinate boxes and checks all their
inclusions in the actual free-edge domain. It does not rerun Newton
certification or numerically replace the written contour/compactness
argument which supplies a positive outside-loss constant.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=192)
    ap.add_argument('--output', type=Path,
                    default=ROOT/'repro/results/research-three-chain-outside-boundary-decay.json')
    args = ap.parse_args()
    ctx.prec = args.precision

    def a(value):
        value = Q(value)
        return arb(value.numerator)/value.denominator

    checks = []
    def positive(name, value):
        assert value > 0, (name, value)
        checks.append({'name': name, 'strict_positive_margin': str(value)})

    positive('selected real angle is below pi/2', arb.pi()/2-a('1.55'))
    positive('selected depth is below 1.07', a('1.07')-1)
    positive('entire rounded cap box has |cos(t/2)| below1',
             1-(arb(1).cosh()+a('1.5').cos())/2)
    positive('true-disk complete action stays above absolute plateau',
             a('1.9113')-a('.08')*a('.005')-7*a('.005')**2-a('1.9107'))
    P, A, r = a('.0113'), a('1.45'), a('.01')
    minimum_profile = a('1.9113')+P*r-A*r*r
    positive('real capped profile exceeds plateau', minimum_profile-a('1.9107'))
    positive('real capped profile exceeds original far-arc rate', minimum_profile-a('1.91115'))
    positive('original two-vertex corner below plateau', a('1.9107')-a('1.715'))
    positive('restored chain corner retains positive gap', a(Q(31, 600)))

    seed_path = 'repro/results/research-three-phase-graph-transform.json'
    real_path = 'repro/results/research-three-prepared-cap-real-critical.json'
    seed = json.loads((ROOT/seed_path).read_text())
    real = json.loads((ROOT/real_path).read_text())
    assert seed['status'] == real['status'] == 'passed'
    # Inclusions in a stored Newton box are useful only if its original
    # proof inputs and certificate implementation still match this tree.
    inherited_hash_checks = 0
    for record in (seed, real):
        hashes = record.get('sha256', record.get('dependencies_sha256', {}))
        assert hashes, 'inherited certificate lacks dependency hashes'
        for relative_path, expected in hashes.items():
            actual = sha256((ROOT/relative_path).read_bytes()).hexdigest()
            assert actual == expected, ('stale inherited input', relative_path)
            inherited_hash_checks += 1
    real_script = ROOT/'experiments/certify_three_prepared_cap_real_critical.py'
    assert sha256(real_script.read_bytes()).hexdigest() == real['script_sha256']
    inherited_hash_checks += 1
    counts = {'complex_output_seed_cells': 0, 'real_output_critical_cells': 0}
    minima = {}

    def cap_inclusion(label, real_part, depth):
        margins = {
            'a>1.5': real_part-a('1.5'),
            'a<1.55': a('1.55')-real_part,
            'H>.97': depth-a('.97'),
            'H<1': 1-depth,
            '|cos(t/2)|<1': 1-(depth.cosh()+real_part.cos())/2,
        }
        for name, value in margins.items():
            assert value > 0, (label, name, value)
            lower = value.lower()
            if name not in minima or lower < minima[name]:
                minima[name] = lower

    # Newton centers/radii are retained exactly; this is tighter than the
    # deliberately rounded human-readable coordinate summaries.
    for j, cell in enumerate(seed['seed_cells']):
        cr, ci = map(a, cell['centers'][1])
        radius = arb(cell['radii'][1])
        cap_inclusion(('seed', j), arb(cr, radius), -arb(ci, radius))
        counts['complex_output_seed_cells'] += 1
    assert counts['complex_output_seed_cells'] == 4096
    for j, cell in enumerate(real['cells']):
        real_part, imaginary_part = map(arb, cell['coordinate_parts'][1])
        cap_inclusion(('real', j), real_part, -imaginary_part)
        counts['real_output_critical_cells'] += 1
    assert counts['real_output_critical_cells'] == 399

    dependencies = [
        'notes/research_three_chain_outside_boundary_decay.md',
        'notes/research_pair_free_boundary_kernel.md',
        'notes/research_free_boundary_half_charge_observation.md',
        'notes/research_three_prepared_cap_quantified_source.md',
        'notes/research_three_prepared_cap_real_extension.md',
        'notes/research_three_cap_wire_complement.md',
        'notes/research_three_cap_central_source.md',
        'notes/research_three_first_entrance_source.md',
        'notes/research_three_first_entrance_real_extension.md',
        'notes/research_three_larger_source_propagation.md',
        'notes/research_three_chain_fourier_corner_transfer.md',
        'notes/research_three_larger_source_closure.md',
        'notes/research_network_whole_boundary_decay.md',
        'notes/research_componentwise_short_filling_stability.md',
        seed_path, real_path,
    ]
    result = {
        'status': 'passed', 'precision_bits': args.precision,
        'scope': 'Outward inclusion checks on 4096 validated complex-output and 399 validated real-output cap critical boxes, plus eight scalar preparation/domain reserves. Existing Newton and exact-cover validations are reused, not rerun. The positive outside-decay constant, all original contour estimates, off-color source propagation and final strip argument are the written proof, not numerically certified here.',
        'strict_scalar_comparisons': len(checks), 'comparisons': checks,
        'critical_box_counts': counts,
        'critical_domain_checks': 5*sum(counts.values()),
        'inherited_provenance_checks': inherited_hash_checks,
        'minimum_domain_margins': {k: str(v) for k, v in minima.items()},
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependencies_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
    }
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['status', 'strict_scalar_comparisons',
                    'critical_box_counts', 'critical_domain_checks']}, indent=2))


if __name__ == '__main__':
    main()
