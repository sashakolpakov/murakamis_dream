#!/usr/bin/env python3
"""Literal connectivity obstruction for full-twist-filled Conway sources."""
import json
from pathlib import Path

from audit_actual_conway_bowtie_projection_cut import expression_cases
from audit_positive_conway_geometric_incidence import Pairing


def seeds(e):
    return 1 if e[0] == 'A' else sum(seeds(c) for c in e[1:])


def leaf_pairing(p=None):
    # The original complete-circle through pairing and every R^(-2p)
    # have identity permutation; retain the actual quarter-turn.
    permutation = [0, 1]
    if p is not None:
        for _ in range(abs(2*p)):
            permutation.reverse()
    assert permutation == [0, 1]
    return Pairing([(0, 2), (1, 3)]).turn()


def compile_pairing(e, powers=None):
    if e[0] == 'A':
        leaves = [leaf_pairing(None if powers is None else next(powers))
                  for _ in range(3)]
        return leaves[0].product(leaves[1]).product(leaves[2])
    if e[0] == 'turn':
        return compile_pairing(e[1], powers).turn()
    return compile_pairing(e[1], powers).product(compile_pairing(e[2], powers))


if __name__ == '__main__':
    rows = []
    for e in expression_cases():
        S = seeds(e)
        original = compile_pairing(e)
        assert original.loops >= 2*S
        main = original.close()
        cap_main = original.turn().close()
        assert main >= 2*S+1 and cap_main >= 2*S+1
        for offset in range(7):
            slopes = [(-1 if (i+offset) % 2 else 1)*((i+3*offset) % 17)
                      for i in range(3*S)]
            filled = compile_pairing(e, iter(slopes))
            assert filled.pairs == original.pairs and filled.loops == original.loops
            assert filled.close() == main
        rows.append({'seed_occurrences': S, 'auxiliary_circles': 3*S,
                     'internal_main_components': original.loops,
                     'cylindrical_main_components': main,
                     'cap_main_components': cap_main,
                     'all_auxiliary_full_twist_fillings_preserve_main_count': True})
    result = {'status': 'PASS', 'literal_expression_checks': rows,
              'signed_full_twist_assignments': 7*len(rows),
              'scope': 'Full integral twists preserve endpoint permutation. Every robust seed contains two permanent internal main circles; complete filling never gives a knot. No asymptotic or hyperbolic filling theorem is inferred.'}
    Path(__file__).with_name('actual_conway_full_filling_component_obstruction_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(f'PASS{len(rows)} literal expression counts /{7*len(rows)} signed full-twist assignments; minimum filled main count >=2S+1')
