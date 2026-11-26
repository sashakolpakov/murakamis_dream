from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import shutil

public = Path('/private/tmp/murakamis_dream-publication')
workspace = Path('/Users/sasha/volume-conjecture')
archive = workspace / 'research_archive/curvature-filling-2026-11-01'
archive.mkdir(parents=True, exist_ok=True)

private_sources = [
 '/private/tmp/md-curvature-supported-short-crossing-analytic-certificate.md',
 '/private/tmp/md-all-circle-uniform-gaussian-check.md',
 '/private/tmp/md-main-meridian-marked-a-factor-interface-and-jet-obstruction.md',
 '/private/tmp/md-short-filling-geometric-certificate-and-real-chamber-obstruction.md',
 '/private/tmp/md-audit-all-circle-curvature-packet.py',
 '/private/tmp/md-all-circle-curvature-packet-results.json',
]
for name in private_sources:
    src = Path(name)
    data = src.read_bytes()
    target = archive / (src.stem + '-' + hashlib.sha256(data).hexdigest()[:12] + src.suffix)
    if not target.exists():
        target.write_bytes(data)

changed = []
def save(relative, data):
    path = public / relative
    if path.exists():
        old = path.read_bytes()
        previous = archive / 'publication-before' / relative
        previous.parent.mkdir(parents=True, exist_ok=True)
        if not previous.exists():
            previous.write_bytes(old)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(data)
    changed.append(relative)

text = Path(private_sources[0]).read_text()
text = text.replace('# A curvature-supported certificate for fixed crossing powers',
                    '# A quantitative quantum limit allowing short twists at large junctions')
text = text.replace('1 November 2026. Private derivation; no publication changes.',
'''The earlier filling theorem requires every surviving twist number to be large. Here the number of branches incident to a crossing circle can supply part of the required estimate. The result is a limit for the actual quantum invariant under an explicit inequality involving these two integers. Its limiting value is a specified complex critical action. A geometric completion argument is still needed to identify that value with the volume of the filled knot complement when the twist numbers fall outside the earlier theorem.''')
text = text.replace('The conservative sufficient condition proposed and proved below is',
                    'The following conservative sufficient condition will be proved:')
text = text.replace('The graph and all powers are fixed before \\(N\\) tends to infinity.',
'''The graph and all powers are fixed before \\(N\\) tends to infinity.

The invariant in the conclusion is the reduced, zero-framed ADO polynomial \\(F_N(M)\\), normalized to one on the unknot. Its complete value is \\(F_N(1)=K_N(K)\\). Set \\(q_N=e^{\\pi i/N}\\) and \\(M=q_N^s\\). The explicit elementary factors are
\\[
H_N(s)=\\frac{\\sin(\\pi s)}{N\\sin(\\pi s/N)},\\qquad
A_N(s)=q_N^{a(D)s^2/2},\\qquad a(D)=-w(D)-\\sum_v n_v.
\\]
Here \\(w(D)\\) is the writhe of the fixed original diagram. The [scalar calculation](actual_main_meridian_exact_scalar.md) specifies the same framing convention, including all orientation types. The critical action in the limit is defined in Sections 4 and 7.''')
stems = ['actual_main_meridian_direct_crossing_trace','actual_main_meridian_grouped_wire_packet',
 'actual_main_meridian_joint_filling_transform','actual_main_meridian_source_bounds',
 'actual_main_meridian_exact_scalar','general_original_source_long_filling_transfer',
 'actual_pretzel_long_filling_charge_selection']
labels = ['the exact crossing trace','the finite sum over internal edge indices',
 'the joint Fourier calculation','bounds for the full polynomial traces',
 'the crossing and framing scalar','the earlier source transfer theorem',
 'the pretzel filling calculation']
for stem,label in zip(stems,labels):
    assert (public/'notes'/f'{stem}.md').exists(), stem
    # These occurrences are bare prose references in the private report.
    text = re.sub(r'(?<![(/])\b'+re.escape(stem)+r'\b(?!\.md)', f'[{label}]({stem}.md)', text)
text = text.replace('The finite-wire cotangent errors have larger fixed edge losses\nfrom Section 5.',
                    'The finite-sum contour errors have larger fixed edge losses from Section 5.')
start = text.index('The independent private geometric derivation')
end = text.index('If this certificate\nholds on the branch here',start)
text = text[:start]+'''A sufficient geometric completion argument must retain positively oriented cells in the original exterior, verify the complete face-transition words and total angle \\(2\\pi\\) at every interior edge, and compute the logarithmic periods on the original primitive cusp curves. Those are the geometric checks needed in the [marked completion argument](general_source_regulator_hyperbolic_equality.md). Near the complete structure they are already proved there. The short-twist condition of this note does not itself put the original peripheral logarithms in that neighborhood. '''+text[end:]
text += '''

## Reproducing the edge calculations

The [elementary Newton estimates](all_circle_uniform_newton_bounds.md) give a second direct proof of the uniform discarded-state and complex-strip bounds. The exact edge equations and finite samples of that strip inequality can be checked with:

```sh
python3 repro/run_research_checks.py curvature-fillings
```

The [script](../experiments/audit_all_circle_curvature_packet.py) verifies four symbolic identities and samples the printed complex inequality at both even and odd levels. Its [recorded output](../experiments/all_circle_curvature_packet_results.json) states that finite scope. The uniform inequalities, contour argument and asymptotic conclusion are proved above; the script does not establish geometric completion.
'''
assert '/private/' not in text and 'independent private' not in text
save('notes/actual_all_circle_curvature_filling_limit.md',text)

text = Path(private_sources[1]).read_text()
text = text.replace('This calculation checks two inputs to the proposed extension beyond independently large twist integers.',
 'This note proves two uniform estimates used in the [quantitative filling limit](actual_all_circle_curvature_filling_limit.md).')
text = text.replace('`actual_main_meridian_source_bounds`',
 '[the full polynomial trace bounds](actual_main_meridian_source_bounds.md)')
save('notes/all_circle_uniform_newton_bounds.md',text)
save('experiments/audit_all_circle_curvature_packet.py',Path(private_sources[4]).read_text())
save('experiments/all_circle_curvature_packet_results.json',Path(private_sources[5]).read_text())

path='repro/research_check_groups.json'
data=json.loads((public/path).read_text())
assert not any(g['name']=='curvature-fillings' for g in data['groups'])
data['groups'].append({'name':'curvature-fillings',
 'description':'Exact edge-action identities and finite complex-strip checks for the quantitative short-twist criterion; no filled-volume certification.',
 'commands':[['python3','experiments/audit_all_circle_curvature_packet.py']]})
save(path,json.dumps(data,indent=2)+'\n')

path='book/catalog.json'
data=json.loads((public/path).read_text())
data.update({
 'actual_all_circle_curvature_filling_limit':['Source and transport','A quantitative quantum limit allowing short twists at large junctions'],
 'all_circle_uniform_newton_bounds':['Source and transport','Uniform Newton bounds for trees with a crossing circle at every junction'],
 'audit_all_circle_curvature_packet':['Audits and data','Exact edge actions and finite complex Gaussian checks'],
 'all_circle_curvature_packet_results':['Audits and data','Recorded edge identities and complex-strip samples'],
})
save(path,json.dumps(data,indent=2)+'\n')
path='book/collections.json'
data=json.loads((public/path).read_text())
collection=next(c for c in data if c['id']=='moving-meridian')
collection['notes'] += ['actual_all_circle_curvature_filling_limit','all_circle_uniform_newton_bounds']
collection['scope'] += ' A separate quantitative analytic limit allows some short twists at large circle junctions; its extension to the actual filled volume still needs a geometric completion proof.'
save(path,json.dumps(data,indent=2)+'\n')

path='book/chapters/frontier.md'
text=(public/path).read_text()
marker='## The moving-meridian growth already established'
assert marker in text
section=r'''## How short twists can enter the analytic estimate

There is now a quantitative extension of the finite-sum argument for trees in which every junction carries an original crossing-circle operator. The vertices of this tree represent those circles, and its edges represent the quarter-turns joining their ordered products. Let \(d_v\) be the number of edges incident to a vertex and \(n_v\) its signed crossing power. These integers describe the fixed presentation; neither grows with the quantum level.

The [new estimate](../../notes/actual_all_circle_curvature_filling_limit.md) proves the logarithmic limit and the same normalized meridian profile under the explicit condition

\[
\sum_v\frac{d_v}{d_v^2+n_v^2}\le2^{-25}.
\]

The limiting value is \(2\pi\operatorname{Re}\mathcal C(\mathbf1)\), where \(\mathcal C(\mathbf1)\) is the critical value of the original joint Fourier action at the first positive integer frequency in every variable. The proof shows that this contribution is nonzero and that the other frequencies and discarded states are exponentially smaller. It does not assume those conclusions as hypotheses.

A large twist makes its summand small. A large number of incident branches can also make it small, even if that vertex has zero or one crossing. For example, a star with \(B\) branches has a central contribution at most \(1/B\). If every terminal crossing power has magnitude at least \(B\), the total is less than \(2/B\). The conservative displayed bound therefore permits an arbitrary fixed central power once \(B\ge2^{26}\). These constants are intentionally coarse; the example establishes that the criterion is nonempty, not that it is practical at small crossing numbers. The original knot and parity conditions still apply.

The geometric question remains distinct. At a high-degree circle the angular variables can be small while the primitive meridian logarithm accumulates a full turn. The earlier proof of smooth filling near the complete logarithms cannot be invoked solely from that angular estimate. To extend the knot-volume theorem to these short-twist cases, one must construct the positively oriented cells with their original face identifications and verify the actual primitive logarithmic periods. Until that is done, the new result is an explicit quantum limit; its limiting constant is not being advertised as the hyperbolic volume outside the already covered long-filling cases.

'''
text=text.replace(marker,section+marker)
save(path,text)

path='book/chapters/audits.md'
text=(public/path).read_text()
marker='## Arbitrary multiplication regions'
section='''## The quantitative short-twist estimate

The [analytic criterion](../../notes/actual_all_circle_curvature_filling_limit.md) uses an explicit two-variable action on every edge and a uniform estimate for Newton polynomials on a complex strip. Its focused checks run with:

```sh
python3 repro/run_research_checks.py curvature-fillings
```

Python, SymPy and mpmath are required. The program verifies the wire critical equation, two derivatives of the selected action, and its Hessian determinant symbolically. It then checks 990 complex-strip samples at 70-digit precision, including even and odd levels from 160 to 256. The [saved results](../../experiments/all_circle_curvature_packet_results.json) also record the constants separating the first critical action from the discarded-state bounds. These samples check the formulas; the proof supplies their uniform validity. No test in this group certifies the topology or the hyperbolic volume of a short-filled knot.

'''
assert marker in text
save(path,text.replace(marker,section+marker))

for relative in changed:
    target=workspace/relative
    target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(public/relative,target)
record={'updated_utc':datetime.now(timezone.utc).isoformat(),
 'source_paths':changed,'archive':str(archive),
 'scope':'Explicit analytic limit; short-twist geometric completion remains open.'}
Path('/private/tmp/md-curvature-publication-paths.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
