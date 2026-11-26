from pathlib import Path
import json, hashlib

pub=Path('/private/tmp/murakamis_dream-publication')
tmp=Path('/private/tmp')
before=tmp/'md-general-public-before'
paths=[]

def put(rel,data):
    p=pub/rel
    old=before/rel
    if p.exists() and not old.exists():
        old.parent.mkdir(parents=True,exist_ok=True)
        old.write_bytes(p.read_bytes())
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_bytes(data if isinstance(data,bytes) else data.encode())
    paths.append(rel)

for name in ['actual_main_meridian_high_fourier_reflection','actual_main_meridian_component_pressure','actual_main_meridian_general_component_comparison']:
    put('notes/'+name+'.md',(tmp/(name+'.md')).read_bytes())
for suffix in ['tex','pdf','svg','png']:
    put('book/figures/main-meridian-reflected-turn-fusion.'+suffix,(tmp/('md-main-meridian-reflected-turn-fusion.'+suffix)).read_bytes())
for name in ['audit_main_meridian_high_fourier_reflection.py','high_fourier_reflection_results.json']:
    put('experiments/'+name,(tmp/name).read_bytes())

rel='repro/research_check_groups.json'
d=json.loads((pub/rel).read_text())
assert not any(g['name']=='general-components' for g in d['groups'])
d['groups'].append({'name':'general-components','description':'Exact high-index Fourier coefficients, trace-difference cancellation and full Frobenius fusion at both level parities.','commands':[['python3','experiments/audit_main_meridian_high_fourier_reflection.py']]})
put(rel,json.dumps(d,indent=2,ensure_ascii=False)+'\n')

rel='book/catalog.json'
d=json.loads((pub/rel).read_text())
d.update({
 'actual_main_meridian_high_fourier_reflection':['Source and transport','A reflected trace bound for one high Newton index'],
 'actual_main_meridian_component_pressure':['Geometry and volume','Positive boundary pressures and deletion of turns in Conway product trees'],
 'actual_main_meridian_general_component_comparison':['Source and transport','Main-meridian estimates for arbitrary Conway product regions'],
 'audit_main_meridian_high_fourier_reflection':['Audits and data','Exact high-index Fourier differences and full Frobenius fusion'],
 'high_fourier_reflection_results':['Audits and data','Recorded exact Fourier and fusion identities']
})
put(rel,json.dumps(d,indent=2,ensure_ascii=False)+'\n')

rel='book/chapters/audits.md'
s=(pub/rel).read_text()
new='''## Arbitrary multiplication regions

The [general component theorem](../../notes/actual_main_meridian_general_component_comparison.md) permits connected groups of product junctions of any fixed size and valence. Its new finite identities can be checked with one command:

```sh
python3 repro/run_research_checks.py general-components
```

The program constructs each Newton polynomial over an exact cyclotomic number field. It compares its Laurent coefficients with the formula in the [Fourier reflection proof](../../notes/actual_main_meridian_high_fourier_reflection.md), and independently divides products by the deformed polynomial relation. Subtracting the complete trace must cancel the first Fourier term. A further calculation verifies fusion in the full quotient algebra, including inputs whose values at repeated roots vanish but whose derivative contributions remain nonzero.

The [recorded results](../../experiments/high_fourier_reflection_results.json) cover levels two through twelve, including both parities: 36 high-index polynomials, 721 trace differences and 33 fusion identities. These are exact finite algebra checks. The uniform Fourier loss, comparison of positive maxima and passage to the filled knot complement are proved in the three companion notes; the finite checks do not establish those analytical or geometric conclusions.

'''
assert '## Arbitrary multiplication regions' not in s
s=s.replace('## Trivalent multiplication regions\n',new+'## Trivalent multiplication regions\n',1)
put(rel,s)

rel='book/figures.md'
s=(pub/rel).read_text()
new='''## Reflecting an index and combining two product junctions

![Three diagrams show a trace-difference bound, its reflected complete pairing, and the fused product junction with all five exterior branches retained.](figures/main-meridian-reflected-turn-fusion.png)

The vertices represent multiplication and trace operations on tangle polynomials. In the left panel, a physical quarter-turn joins two equal indices \\(h\\). The left trace is the difference \\(\\delta\\phi_s=\\phi_s-\\phi_0\\) between its moving-meridian and complete values. The [Fourier estimate](../notes/actual_main_meridian_high_fourier_reflection.md) bounds this difference after replacing \\(h\\) at that endpoint by \\(r=N-1-h\\). All other branches, denoted collectively by \\(F\\) and \\(G\\), remain attached.

The middle panel therefore has complementary labels \\(r+h=N-1\\). Summing this positive complete pairing gives exactly the single trace \\(\\phi_0(FG)\\), shown on the right. The three branches from the first junction and two from the second give the five displayed branches. Their order is inherited from the original ordered products.

The first arrow is an upper estimate; the second is an algebra identity. Deleting the turn in this comparison can change the represented link. The [pressure theorem](../notes/actual_main_meridian_component_pressure.md) proves that the new positive maximum is no larger than the original one, and a strict Fourier estimate controls the case of equal maxima. The invariant and the hyperbolic volume in the final theorem still belong to the original diagram. This comparison is what allows the [general component proof](../notes/actual_main_meridian_general_component_comparison.md) to treat junctions of arbitrary valence.

[SVG](figures/main-meridian-reflected-turn-fusion.svg) · [PDF](figures/main-meridian-reflected-turn-fusion.pdf) · [TikZ source](figures/main-meridian-reflected-turn-fusion.tex)

'''
assert '## Reflecting an index and combining' not in s
s=s.replace('## A tree whose product junctions can be estimated\n',new+'## A separated example of the product tree\n',1)
s=s.replace('The two outer junctions carry no unturned crossing-circle operator;', 'This is a simple instance of the general theorem above. The two outer junctions carry no unturned crossing-circle operator;',1)
put(rel,s)

rel='notes/actual_main_meridian_preferred_cusp.md'
s=(pub/rel).read_text().replace('Section 9 gives a quantum consequence for the narrower class in which a moving-meridian asymptotic has already been proved. Its long-twist analytic hypotheses are stated there;', 'Section 9 gives the quantum consequence for these strict presentations when the fixed signed twists are independently sufficiently long. Those analytic hypotheses are stated there;')
put(rel,s)
rel='notes/actual_main_meridian_exact_scalar.md'
s=(pub/rel).read_text().replace('The moving-meridian asymptotic in Section 6 has narrower hypotheses. In particular the broader complete-value volume theorem for strict Conway trees does not, by itself, supply that moving profile.', 'The moving-meridian asymptotic in Section 6 additionally requires a strict presentation and independently sufficiently long fixed signed twists. The exact scalar calculation itself requires neither a large-level limit nor the analytical estimates used to prove that profile.')
put(rel,s)
rel='notes/actual_main_meridian_source_bounds.md'
s=(pub/rel).read_text().replace('The previously established complete-meridian filled-knot equalities remain separate results. A limiting normalized meridian profile and a general estimate for adjacent bare junctions also remain open.', 'The [general component comparison](actual_main_meridian_general_component_comparison.md) extends the source bound to arbitrary connected bare regions. The separate [filled-meridian theorem](actual_main_meridian_filled_volume.md) proves the normalized profile and the filled knot-complement volume limit, using additional local and joint filling estimates.')
put(rel,s)
rel='notes/actual_main_meridian_auxiliary_color_gap.md'
s=(pub/rel).read_text().replace('The [component extension](actual_main_meridian_component_extension.md) supplies the same argument for adjacent bare junctions satisfying its path condition.', 'The [general component theorem](actual_main_meridian_general_component_comparison.md), Sections 6–8, supplies the same norm and angular interfaces for arbitrary adjacent bare junctions. The earlier [component extension](actual_main_meridian_component_extension.md) remains a special case.')
put(rel,s)
rel='notes/actual_main_meridian_newton_compiler.md'
s=(pub/rel).read_text().replace('The subsequent [component extension](actual_main_meridian_component_extension.md) controls adjacent bare junctions under a finite path condition. The [filled-meridian theorem](actual_main_meridian_filled_volume.md) then proves a normalized profile and a uniform knot-volume limit on these microscopic disks, with additional complex-contour and geometric arguments.', 'The [general component comparison](actual_main_meridian_general_component_comparison.md) now removes that separation condition: it controls every fixed connected group of bare junctions, with arbitrary valences. The [filled-meridian theorem](actual_main_meridian_filled_volume.md) proves a normalized profile and a uniform knot-volume limit for the full strict-tree class with independently sufficiently long fixed signed twists, using additional complex-contour and geometric arguments.')
put(rel,s)

(tmp/'md-general-installed-paths.json').write_text(json.dumps(paths,indent=2)+'\n')
print(json.dumps({'installed_or_updated':len(paths),'paths':paths},indent=2))
