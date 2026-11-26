from pathlib import Path
import json,shutil
root=Path('/private/tmp/murakamis_dream-publication');tmp=Path('/private/tmp');changed=set(json.loads((tmp/'md-trivalent-initial-changed.json').read_text()))
mapping={
 'actual_main_meridian_trivalent_component_bound.md':'notes/actual_main_meridian_trivalent_component_bound.md',
 'actual_main_meridian_trivalent_filled_volume.md':'notes/actual_main_meridian_trivalent_filled_volume.md',
 'md-audit-trivalent-return-comparison.py':'experiments/audit_main_meridian_trivalent_components.py',
 'md-trivalent-return-comparison-results.json':'experiments/trivalent_return_comparison_results.json',
}
for ext in ['tex','svg','png','pdf']:
 mapping['md-trivalent-bare-components.'+ext]='book/figures/trivalent-bare-components.'+ext
for source,target in mapping.items():shutil.copyfile(tmp/source,root/target);changed.add(target)
p=root/'notes/actual_main_meridian_trivalent_filled_volume.md';s=p.read_text();s=s.replace('The existing two-leaf knot qualification is retained.','For a strict two-leaf construction, retain the knot-producing parity pattern containing a pure leaf; the two-odd-leaf link pattern is excluded.')
s=s.replace('Assume the [strict source condition](actual_conway_all_strict_tree_long_twist_volume.md): the original leaf angles lie in \\((0,1/2)\\), and every retained multiplication gate has','Assume the [strict source condition](actual_conway_all_strict_tree_long_twist_volume.md): there is an assignment of original leaf angles in \\((0,1/2)\\) for which every retained multiplication gate satisfies')
anchor='There is no size bound on the second type of component.'
assert anchor in s;s=s.replace(anchor,'![Two possible trivalent bare components, with all outside attachments included in the degree count.](../book/figures/trivalent-bare-components.svg)\n\n'+anchor,1)
s=s.replace('The exact scalar ledger is proved in [the filled-meridian normalization](actual_main_meridian_filled_volume.md), Section 2.','The exact scalar ledger is proved in [the framing and crossing calculation](actual_main_meridian_exact_scalar.md).')
p.write_text(s)
p=root/'notes/actual_main_meridian_trivalent_component_bound.md';s=p.read_text()+r'''

## Reproducing the finite calculations

Run the dedicated group from the repository root:

```sh
python3 repro/run_research_checks.py trivalent-components
```

The [program](../experiments/audit_main_meridian_trivalent_components.py) constructs the original Newton polynomials over exact cyclotomic fields, divides their products by \(P_0+\Delta\), and extracts the closing trace. It then compares that independently obtained trace with the complete and additional tensor formulas. The [saved results](../experiments/trivalent_return_comparison_results.json) cover levels two through ten, including old supported triples with an internal index above one half and the smallest possible total degree in the additional support. The program also checks the unchanged pairing, the endpoint permutation of the six physical types, and the elementary algebra used in the boundary derivative.

Python and SymPy are sufficient. These are finite algebraic checks. The simultaneous inequality, the strict exponential gap, and the passage to the filled volume are proved in the text and its companion theorem.
''';p.write_text(s)
p=root/'repro/research_check_groups.json';d=json.loads(p.read_text());assert not any(g['name']=='trivalent-components' for g in d['groups']);d['groups'].append({'name':'trivalent-components','description':'Exact Newton quotient traces, old and additional cubic support, complete pairing, endpoint normalization and physical orientation types. The analytic component bound and filled-volume theorem have separate proofs.','commands':[['python3','experiments/audit_main_meridian_trivalent_components.py']]});p.write_text(json.dumps(d,indent=2)+'\n');changed.add(str(p.relative_to(root)))
p=root/'book/catalog.json';d=json.loads(p.read_text());d.update({
 'actual_main_meridian_trivalent_component_bound':['Source and transport','Simultaneous boundary comparison for arbitrary trivalent product regions'],
 'actual_main_meridian_trivalent_filled_volume':['Source and transport','Uniform meridian volume and cusp profile with arbitrary trivalent regions'],
 'audit_main_meridian_trivalent_components':['Audits and data','Exact cyclotomic cubic traces and physical orientation types'],
 'trivalent_return_comparison_results':['Audits and data','Recorded exact trivalent-component calculations'],
});p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n');changed.add(str(p.relative_to(root)))
p=root/'book/chapters/audits.md';s=p.read_text();pos=s.index('\n## ');s=s[:pos]+r'''
## Trivalent multiplication regions

The [component theorem](../../notes/actual_main_meridian_trivalent_component_bound.md) has one reproduction command:

```sh
python3 repro/run_research_checks.py trivalent-components
```

The script constructs the Newton polynomials and performs division by the deformed polynomial relation in exact cyclotomic fields. It checks every cubic index triple through level ten, using symmetry to avoid repeated calculations. This includes internal indices above one half, zero and half endpoints, both parities, and the actual turn types. It also checks the elementary identities used in the simultaneous boundary comparison.

The script uses Python and SymPy and has no numerical approximations. It checks the finite algebra; the proof supplies the concavity argument, the uniform gap, and the complex estimates needed for the [filled-knot theorem](../../notes/actual_main_meridian_trivalent_filled_volume.md).
''' +s[pos:];p.write_text(s);changed.add(str(p.relative_to(root)))
p=root/'book/figures.md';s=p.read_text()+r'''

## Connected trees of trivalent product junctions

![A path and a branching tree, each with degree three at every bare junction and with circle-operator attachments shown.](figures/trivalent-bare-components.svg)

The open vertices are product junctions without a crossing-circle operator. Each has three incident branches, counting the attachments to the filled vertices. These graphs record tangle operations: consecutive unturned products have already been grouped, and every displayed edge is a physical quarter-turn. A fixed tree of any size is allowed by the [trivalent meridian theorem](../notes/actual_main_meridian_trivalent_filled_volume.md).

[Vector drawing](figures/trivalent-bare-components.svg) · [PDF](figures/trivalent-bare-components.pdf) · [TikZ source](figures/trivalent-bare-components.tex)
''';p.write_text(s);changed.add(str(p.relative_to(root)))
(tmp/'md-trivalent-publication-paths.json').write_text(json.dumps(sorted(changed),indent=2)+'\n')
print(json.dumps({'source_files':len(changed)}))
