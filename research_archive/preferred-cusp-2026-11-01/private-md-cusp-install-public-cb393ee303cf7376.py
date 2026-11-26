from pathlib import Path
import json,shutil
root=Path('/private/tmp/murakamis_dream-publication');tmp=Path('/private/tmp')
changed=json.loads((tmp/'md-cusp-initial-changed.json').read_text())
mapping={
 'md-publish-main-meridian-scalar.md':'notes/actual_main_meridian_exact_scalar.md',
 'md-publish-main-meridian-preferred-cusp.md':'notes/actual_main_meridian_preferred_cusp.md',
 'md-audit-main-meridian-scalar.py':'experiments/audit_main_meridian_exact_scalar.py',
 'md-main-meridian-scalar-results.json':'experiments/main_meridian_exact_scalar_results.json',
 'audit_main_meridian_preferred_cusp.py':'experiments/audit_main_meridian_preferred_cusp.py',
 'main_meridian_preferred_cusp_results.json':'experiments/main_meridian_preferred_cusp_results.json',
}
for ext in ['tex','pdf','svg','png']:
 mapping['md-main-cusp-longitude-shear.'+ext]='book/figures/main-cusp-longitude-shear.'+ext
for source,target in mapping.items():
 shutil.copyfile(tmp/source,root/target);changed.append(target)
p=root/'notes/actual_main_meridian_exact_scalar.md'
s=p.read_text()+r'''

## 8. Reproducing the finite identities

The [exact scalar script](../experiments/audit_main_meridian_exact_scalar.py) starts from the two mixed positive crossings, obtains the inverse crossings, and composes signed words with their actual starting and ending orders. It also derives the integer grading from the six turn phases, checks compatible products and turns on finite expression trees, and compares the shifted-grid exponents as rational polynomials. Its [recorded results](../experiments/main_meridian_exact_scalar_results.json) list the inputs and the scope of the checks.

To run the scalar checks together with the geometric matrix identities, use the repository runner:

```sh
python3 repro/run_research_checks.py meridian-cusp
```

The scalar script uses Python's standard library; the geometric script also requires SymPy. These computations check local algebra. The physical tensor formulas, the longitude's topology, and the uniform asymptotic estimates are supplied by the proofs, rather than by a finite list of examples.
'''
p.write_text(s)
p=root/'notes/actual_main_meridian_preferred_cusp.md';s=p.read_text();old='Fix a presentation in this analytic class and its original knot and parity pattern.';assert old in s;s=s.replace(old,old+' In the strict two-leaf knot case, retain the linked theorem’s pure-leaf qualification.');p.write_text(s)
p=root/'book/catalog.json';d=json.loads(p.read_text());d.update({
 'actual_main_meridian_exact_scalar':['Source and transport','Exact framing and crossing scalar in the meridian profile'],
 'actual_main_meridian_preferred_cusp':['Geometry and volume','Preferred knot-cusp shape from the original face maps and surgeries'],
 'audit_main_meridian_exact_scalar':['Audits and data','Exact signed crossing words and typed scalar composition'],
 'main_meridian_exact_scalar_results':['Audits and data','Recorded exact scalar computations'],
 'audit_main_meridian_preferred_cusp':['Audits and data','Exact meridian frames, face transports and filling signs'],
 'main_meridian_preferred_cusp_results':['Audits and data','Recorded rational identities for the preferred cusp formula'],
});p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n');changed.append(str(p.relative_to(root)))
p=root/'repro/research_check_groups.json';d=json.loads(p.read_text());assert not any(g['name']=='meridian-cusp' for g in d['groups']);d['groups'].append({'name':'meridian-cusp','description':'Exact scalar composition and geometric meridian-frame identities for the preferred-cusp correction. These finite checks support the local calculations; they do not replace the topology or the asymptotic proof.','commands':[['python3','experiments/audit_main_meridian_exact_scalar.py','--output','experiments/main_meridian_exact_scalar_results.json'],['python3','experiments/audit_main_meridian_preferred_cusp.py']]});p.write_text(json.dumps(d,indent=2)+'\n');changed.append(str(p.relative_to(root)))
p=root/'book/chapters/audits.md';s=p.read_text();pos=s.index('\n## ');s=s[:pos]+r'''
## The preferred cusp correction

The exact crossing and framing calculation and the geometric longitude calculation can be reproduced together:

```sh
python3 repro/run_research_checks.py meridian-cusp
```

The scalar program composes signed crossing words and compatible typed products from their local formulas, retaining negative powers and both orders of opposite colors. It also checks the shifted-grid phase algebra. The geometric program verifies the rational meridian frames, the product and turn coordinate maps, the two half-twist signs, and the longitude correction under surgery. Python and SymPy are sufficient.

The [scalar proof](../../notes/actual_main_meridian_exact_scalar.md) and [longitude proof](../../notes/actual_main_meridian_preferred_cusp.md) explain the global conclusions. The programs check their local identities; the identification of the preferred peripheral curves and the uniform large-level estimate are arguments in those proofs.
''' + s[pos:];p.write_text(s);changed.append(str(p.relative_to(root)))
p=root/'book/figures.md';s=p.read_text()+r'''

## The preferred longitude after filling crossing circles

![Two fundamental parallelograms of the same filled cusp lattice. The meridian is fixed; the preferred longitude differs from the augmented longitude by four meridians in the illustrated case.](figures/main-cusp-longitude-shear.svg)

The blue vector is the image of the augmented longitude on the filled knot cusp. To obtain the preferred longitude, add \(\sum_i p_i\ell_i^2\) meridians, where \(p_i\) is the filling coefficient and \(\ell_i\) is the linking number with crossing circle \(i\). The drawing uses one coefficient \(p=1\) and \(|\ell|=2\), so the orange vector differs by four meridians. The [longitude proof](../notes/actual_main_meridian_preferred_cusp.md) derives this correction in the homology of the actual filled complement.

[Vector drawing](figures/main-cusp-longitude-shear.svg) · [PDF](figures/main-cusp-longitude-shear.pdf) · [TikZ source](figures/main-cusp-longitude-shear.tex)
''';p.write_text(s);changed.append(str(p.relative_to(root)))
p=root/'book/chapters/results.md';s=p.read_text();old='The full modified-trace invariant has exactly the displayed normalized profile because its modified dimension cancels \\(H_N\\).';assert old in s;s=s.replace(old,old+'\n\n![The preferred longitude on the filled cusp: the same Euclidean lattice with the augmented and surgery-corrected choices of longitude.](../figures/main-cusp-longitude-shear.svg)');p.write_text(s)
(tmp/'md-cusp-publication-paths.json').write_text(json.dumps(sorted(set(changed)),indent=2)+'\n')
print(json.dumps({'source_paths':len(set(changed))}))
