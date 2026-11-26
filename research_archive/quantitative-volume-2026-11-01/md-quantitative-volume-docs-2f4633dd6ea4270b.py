from pathlib import Path
import hashlib, json, shutil

root=Path('/private/tmp/murakamis_dream-publication')
archive=Path('/Users/sasha/volume-conjecture/research_archive/quantitative-volume-2026-11-01')
archive.mkdir(parents=True,exist_ok=True)
changed=[]
def write(rel,s):
    p=root/rel
    if p.exists():
        h=hashlib.sha256(p.read_bytes()).hexdigest()[:16]
        shutil.copy2(p,archive/(p.stem+'-before-'+h+p.suffix))
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(s)
    changed.append(rel)
def read(rel):return (root/rel).read_text()
def replace_section(s,heading,new):
    start=s.index(heading)
    end=s.find('\n## ',start+len(heading))
    if end<0:end=len(s)
    return s[:start]+new.rstrip()+'\n'+s[end:]

s=Path('/private/tmp/md-all-circle-volume-publication/theorem-and-exposition.md').read_text()
s=s.replace('The edge and peripheral rows\nare Lagrangian,', 'The edge and peripheral rows\nare Lagrangian,')
s=s.replace('Developing this triangulation with the earlier marked representation',
'''The [marked gluing theorem](general_marked_multicusp_gluing_rigidity.md)
proves this for the mixed choice of main meridian and auxiliary longitudes.

Developing this triangulation with the earlier marked representation''')
s=s.replace('The original surgery homology changes the\naugmented preferred longitude by',
'''The [continuation proof](actual_all_circle_preferred_cusp.md) gives the
representation comparison and the original peripheral words in detail.
The longitude after surgery is kept as a fixed boundary word along the
path; it becomes the preferred longitude of the smooth knot complement
at the endpoint. The original surgery homology changes the
augmented preferred longitude by''')
write('notes/actual_all_circle_quantitative_volume.md',s)

s=read('notes/actual_all_circle_curvature_filling_limit.md')
first=s.index('\n\n')
end=s.index('\n## 1.')
s=s[:first]+'''

The number of branches incident to a crossing circle can supply part of
the estimate previously obtained by taking its twist number large.
This note proves the finite-sum limit under an explicit inequality in
those two integers. The [volume theorem](actual_all_circle_quantitative_volume.md)
combines it with the ordered octahedral decomposition and positive
filling path. The limiting action is therefore the volume of the
original knot complement throughout the stated class, including the
short coefficients permitted by the inequality.
'''+s[end:]
s=s.replace('Keep the original strictness, ordered branches,\norientations, knot pattern, primitive cut and zero framing.',
'''Keep the ordered branches, orientations, knot pattern, primitive cut
and zero framing. For the literal construction defined in the
[volume theorem](actual_all_circle_quantitative_volume.md), the strict
angle condition follows inductively from the product intervals; it is
not a further restriction on these trees.''')
s=s.replace('Short, even zero, crossing powers are permitted by the trace algebra\nand this certificate. Actual volume identification still requires the\nseparate finite geometric completion certificate in Section 11.\nNo new unconditional short-twist volume theorem is asserted here.',
'''Short, even zero, crossing powers are permitted by this certificate.
Section 11 explains how the companion geometric proofs identify the
action with the actual knot volume under the same bound.''')
s=s.replace('[the earlier the earlier', '[the earlier').replace('The earlier [the earlier source transfer theorem]', 'The [earlier source transfer theorem]')
s=replace_section(s,'## 11. What remains for actual volume equality',r'''## 11. Identification with the knot volume

Small angular variables do not imply that the primitive meridian
logarithms are small: a high-degree circle collects contributions from
many edges. The geometric proof therefore follows the entire path of
filling equations, with its logarithm branches retained.

The [ordered decomposition](actual_all_circle_octahedral_decomposition.md)
cuts the original augmented exterior into two octahedra per tree edge.
Its literal strand matchings retain every face pairing, half twist and
primitive peripheral path. The [angular construction](actual_all_circle_angular_octahedra.md)
subdivides these octahedra into eight positive tetrahedra per edge on
the chart ( |	au_v|<10^{-2}). Section 7 places the whole path

[
 Psi_{	au_v}+rac{i n_v	au_v}{2pi}=ic,qquad 0le cle1,
]

inside this chart. The [completion proof](actual_all_circle_geometric_completion.md)
computes the actual periods

[
 U_v=-2piPsi_{	au_v}-iepsilon_v	au_v,qquad
 V_v=2i	au_v,qquad U_v+p_vV_v=-2pi ic.
]

It verifies that the primitive slope bounds a tube of cone angle
(2pi c). At (c=1) the tube is smooth, the auxiliary fillings
are precisely the original surgeries, and the main knot cusp remains
complete. The same proof fixes the additive volume constant at the
complete augmented link and integrates the boundary-corrected action.
It gives

[
 2pioperatorname{Re}mathcal C(mathbf1)
             =operatorname{Vol}(S^3setminus K).
]

Thus the analytic conclusion above is an actual uniform volume theorem
under (2). The [preferred-cusp continuation](actual_all_circle_preferred_cusp.md)
also identifies the first correction geometrically. This establishes
the summed criterion, not arbitrary short fillings or a criterion for
graphs with cycles.''')
write('notes/actual_all_circle_curvature_filling_limit.md',s)

summary=r'''## An explicit bound that also permits some short twists

There is a numerical criterion for a second, precisely specified
construction. Take any finite ordered tree with at least one edge.
At each vertex place an integer two-strand braid. Stack the turned
child tangles on their prescribed sides of that braid, and use a
terminal vertex for the cylindrical closure. The order and turns are
part of the diagram. Following all strands must give one knot, without
an additional component closed inside a tangle.

To describe its geometry, replace each integer braid by a crossing
circle and retain its parity as a half twist. Every junction in this
tree has such a circle. Let (d_v) be its number of incident tree
edges and (n_v) its signed number of half-twists. The
[quantitative theorem](../../notes/actual_all_circle_quantitative_volume.md)
proves that

[
 sum_vrac{d_v}{d_v^2+n_v^2}le2^{-25}
]

implies hyperbolicity and the Kashaev volume limit for the original
knot complement. The whole tree and all integers are fixed before
(N) tends to infinity. Both parities of (N) are included. The same
theorem gives the uniform meridian profile on (M=e^{pi i s/N}),
(|s|le R<1), with the first correction determined by the preferred
cusp shape.

This bound has two useful consequences. If the tree has (E) edges,
then (|n_v|ge8192sqrt E) at every vertex suffices. Short powers are
also possible: start with any ordered tree on (m) vertices, with any
fixed powers, and attach (B) terminal circles to each vertex. If the
added powers have magnitudes at least (B), the sum is less than
(2m/B). Hence (Bge2^{26}m) suffices, provided the resulting strand
pairing is a knot. These very large constants make the result explicit;
they are not proposed as sharp thresholds.

A product junction without a braid can be represented by the identity
braid (R^0). Adding its crossing circle changes the augmented link;
filling it on the specified zero-twist slope recovers the original
diagram. Its contribution to the criterion is (1/d_v). This can
help at a high-degree junction, but does not give a free way to remove
the numerical hypothesis.

The volume identification is proved under the same inequality. The
actual augmented exterior has two octahedra per tree edge. Their
positive deformations keep the original primitive filling curves;
the final cone angle is exactly (2pi), so the filled metric is
smooth. The boundary-corrected action equals its volume, with the
constant fixed at the complete augmented link. The finite-sum proof
then supplies the nonzero contribution and bounds every competing
region. Neither of these two arguments is left as a hypothesis.

This theorem does not cover arbitrary short-twist arborescent knots.
The following long-net-twist theorem covers other presentations and
allows junctions without crossing circles without the displayed
degree condition.

'''
s=read('book/chapters/results.md')
idx=s.index('## Arbitrarily many tangles')
s=s[:idx]+summary+s[idx:]
write('book/chapters/results.md',s)

s=read('book/chapters/frontier.md')
s=s.replace('The remaining questions include short net twists,', 'The remaining questions include short net twists outside the explicit criterion below,')
s=s.replace('A small nonzero surviving twist remains a limitation.', 'A small nonzero surviving twist remains outside this long-net-twist theorem; the quantitative circle-tree theorem below covers some such cases.')
s=s.replace('Short surviving twists, trees or twist numbers growing with $N$,', 'Short surviving twists outside the criterion below, trees or twist numbers growing with $N$,')
s=replace_section(s,'## How short twists can enter the analytic estimate',r'''## Short twists covered by the quantitative theorem

For the ordered tree construction in which every junction carries a
crossing circle, the [quantitative theorem](../../notes/actual_all_circle_quantitative_volume.md)
now proves both the finite-sum asymptotic and its geometric volume
interpretation under

[
 sum_vrac{d_v}{d_v^2+n_v^2}le2^{-25}.
]

Here (d_v) is the number of branches at the circle and (n_v) is
its fixed signed crossing power. The original strand pairing must
give a knot. A large degree can compensate for a short or zero power;
the [results chapter](results.md#an-explicit-bound-that-also-permits-some-short-twists)
gives concrete sufficient bounds and the construction in words.

The earlier analytic proof left one geometric issue: its small angular
coordinates did not force the accumulated primitive meridian logs to
be small. That issue is resolved for this class. The original ordered
cut gives two octahedra per tree edge. Their positive deformations
retain the complete face maps and the primitive periods throughout a
cone-angle path from zero to (2pi). Its endpoint is a smooth metric
on the original knot complement. The calibrated action is its volume.
The preferred main-cusp calculation also continues along this path,
so the first meridian correction has the same geometric meaning.

The remaining question is to enlarge this numerical region and the
class of constructions. The bound is conservative, arbitrary short
coefficients need not satisfy it, and the proof does not cover graphs
with cycles or growing trees. The selected classical geometric factor
of the quantum recurrence also remains a separate problem. No missing
global source theorem is being assumed for the knots that do satisfy
the displayed criterion.''')
write('book/chapters/frontier.md',s)

s=read('README.md')
idx=s.index('The [closure extension]')
s=s[:idx]+r'''There is also an [explicit numerical theorem](https://sashakolpakov.github.io/murakamis_dream/notes/actual_all_circle_quantitative_volume.html)
for ordered trees with a crossing circle at every junction. If (d_v)
is the number of incident branches and (n_v) its signed crossing
power, then

[
sum_vrac{d_v}{d_v^2+n_v^2}le2^{-25}
]

gives hyperbolicity and the volume limit whenever the original strand
pairing gives a knot. For (E) tree edges, requiring every
(|n_v|ge8192sqrt E) suffices. The sharper summed condition also
allows short or zero powers at high-degree junctions. Its proof
constructs the original knot complement from positive ideal cells
and controls the full finite invariant. The constant is conservative.

'''+s[idx:]
write('README.md',s)

s=read('book/chapters/index.md')
s=s.replace('The theorem below applies to specified constructions in this family, with sufficiently many twists in each designated region.', 'The results below give sufficient conditions on specified constructions in this family. One requires long net twists; another gives an explicit bound that can also permit short twists at junctions with many branches.')
idx=s.index('## Why the proof has both')
s=s[:idx]+r'''## A numerical condition for trees of crossing circles

For an ordered tree with a crossing circle at every junction, let
(d_v) count the branches at that circle and let (n_v) be its signed
crossing power. The [quantitative theorem](../../notes/actual_all_circle_quantitative_volume.md)
proves hyperbolicity and the same volume limit if the strand pairing
is a knot and

[
 sum_vrac{d_v}{d_v^2+n_v^2}le2^{-25}.
]

The [results chapter](results.md#an-explicit-bound-that-also-permits-some-short-twists)
defines this tangle construction and gives explicit consequences.
For a tree with (E) edges, twists of magnitude at least
(8192sqrt E) suffice. A circle with many incident branches can
instead carry a short power. The bound is deliberately conservative,
and the tree stays fixed while (N) grows.

This theorem includes the geometric step: the limiting action is the
volume of the original knot complement. The new manuscript chapter
explains the actual octahedral cut, its positive deformation and the
primitive filling slopes. It also derives the first meridian correction
from the preferred longitude of the knot.

'''+s[idx:]
s=s.replace('The TeX manuscript proves an earlier included family; the companion strict-tree estimates and exact tangle reduction give the extension stated here.', 'The earlier chapters of the TeX manuscript prove an included family; the companion strict-tree estimates and exact tangle reduction give this extension. A further manuscript chapter proves the quantitative circle-tree result below.')
write('book/chapters/index.md',s)

s=read('book/chapters/geometry.md')
idx=s.index('## The strict-tree construction')
s=s[:idx]+r'''## The geometric proof for the explicit degree-and-twist bound

The [quantitative theorem](../../notes/actual_all_circle_quantitative_volume.md)
uses a particularly simple decomposition of the actual exterior.
Each vertex of its ordered tree is a crossing circle, and each tree
edge supplies one octahedron in each projection half. Inserting a
terminal child attaches an octahedron along a shaded crossing-disk
triangle. Reading the four strand joins shows that its other three
shaded faces are exactly the new disk faces. The adjacent white
projection faces join in their original order.

![One octahedron is attached along the shaded triangle of a projection half. Equal labels are identified with opposite boundary orientations. The two vertices O_v and O_w belong to the parent and child crossing circles; A, B, C and D are main-strand ends.](../figures/octahedral-page-attachment.svg)

There are (E) octahedra in each half for a tree with (E) edges.
The [ordered decomposition proof](../../notes/actual_all_circle_octahedral_decomposition.md)
retains the left and right insertion order, the actual rotations of
child balls, and the single original half twist at each circle. These
data determine the original manifold and its primitive cusp curves.

The [angular formulas](../../notes/actual_all_circle_angular_octahedra.md)
subdivide the pair of octahedra into eight ideal tetrahedra. All shapes
are (i) at the complete point and remain positively oriented for
(|\tau_v|<10^{-2}). The numerical bound of the theorem puts the
entire path of filling equations inside this chart. Along the path,
the actual primitive slope has logarithmic period (-2\pi i c),
with (0\le c\le1). Its angular period is therefore (2\pi c).

The [completion argument](../../notes/actual_all_circle_geometric_completion.md)
proves that each auxiliary end is a punctured metric tube with these
periods. At (c=1), its core is smooth. Attaching these cores performs
the original surgeries, while the main cusp remains complete. The
boundary correction to the complex action cancels the filling term;
the resulting real value is the volume of this knot complement.
The constant is fixed by the complete augmented link, whose volume
is (2E\,v_8), where (v_8) is the volume of a regular ideal
octahedron.

This argument allows the full meridian logarithm to accumulate one
turn even when each angular variable is small. It is the step needed
for the short powers permitted by the criterion. The
[main-cusp continuation](../../notes/actual_all_circle_preferred_cusp.md)
then compares the marked representations and follows the preferred
longitude to the smooth endpoint.

'''+s[idx:]
write('book/chapters/geometry.md',s)

s=read('book/chapters/audits.md')
s=replace_section(s,'## The quantitative short-twist estimate',r'''## Checks for the quantitative volume theorem

The [quantitative theorem](../../notes/actual_all_circle_quantitative_volume.md)
has one reproduction command:

```sh
python3 repro/run_research_checks.py curvature-fillings
```

Python, SymPy and mpmath are required. The group runs three programs.
The first checks four edge-action identities symbolically and 990
complex Gaussian samples at 70-digit precision, at levels 160 through
256. The second verifies 46 rational identities for the actual
octahedra, including the odd half-twist face returns, and seven bounds
used in the positive angular chart. The third compares the literal
tangle strand compiler with an octahedral attachment construction on
128 finite trees. It checks 448 left or right attachments, the
resulting colored face cycles and signed disk pairings, and 28 symbolic
peripheral and regulator identities.

The saved outputs are the [analytic checks](../../experiments/all_circle_curvature_packet_results.json),
[local geometric checks](../../experiments/two_octahedron_angular_edge_block_results.json)
and [ordered attachment checks](../../experiments/ordered_octahedron_pages_results.json).
Each records its finite scope. The arbitrary-tree induction, the
metric completion and the uniform asymptotic estimates are written
proofs; finite samples do not establish those conclusions. The
[geometric chapter](geometry.md#the-geometric-proof-for-the-explicit-degree-and-twist-bound)
explains how the proof identifies the original knot complement.''')
write('book/chapters/audits.md',s)

s=read('book/chapters/manuscript.md')
idx=s.index('## How to read the proof')
s=s[:idx]+r'''## The quantitative circle-tree chapter

A further chapter treats a different explicit description of the
tangle construction: every vertex of an ordered tree carries an
integer braid, and each child tangle is turned before it is stacked
on the prescribed side of its parent braid. A terminal root gives
the cylindrical closure. The strand pairing must give one knot.

For vertex degree (d_v) and crossing power (n_v), the condition

[
 sum_vrac{d_v}{d_v^2+n_v^2}le2^{-25}
]

gives the volume limit. It also gives a uniform profile as the
meridian moves by order (1/N), with its first correction expressed
by the preferred cusp shape. The [full statement](../../notes/actual_all_circle_quantitative_volume.md)
defines every framing factor and gives numerical sufficient bounds.
Some short powers are allowed at sufficiently high-degree vertices;
the earlier long-twist chapters retain their own construction class.

The chapter illustrates an actual octahedral attachment and explains
why it recovers the original exterior. Positive tetrahedra continue
along the filling path until the primitive cone angle is (2\pi).
This constructs the smooth knot complement whose volume appears in
the quantum limit. Detailed companion proofs supply every face map,
peripheral word and uniform constant used by the argument.

'''+s[idx:]
s=s.replace('The PDF retains its own theorem and proof.', 'The earlier PDF chapters retain their own theorem and proof; the new quantitative chapter is described next.')
s=s.replace('## Reproduce the finite certificates\n', '## Reproduce the finite certificates\n\nThe quantitative chapter uses `python3 repro/run_research_checks.py curvature-fillings`. The [checks chapter](audits.md#checks-for-the-quantitative-volume-theorem) describes its three programs and their finite scope.\n')
write('book/chapters/manuscript.md',s)

s=read('book/figures.md')
idx=s.find('\n## ')
if idx<0:idx=len(s)
s=s[:idx]+r'''

## Attaching an octahedron in the original tangle cut

![An octahedron attaches to a projection half along a shaded disk triangle. The parent and child circle vertices are O_v and O_w; the four equatorial vertices are the corresponding strand ends.](figures/octahedral-page-attachment.svg)

The blue triangle on the left is a boundary face of the existing
projection half. The blue triangle on the right is glued to it with
the opposite boundary orientation. Equal labels specify the vertex
identifications. The new vertex (O_w) belongs to the inserted child
crossing circle, while (O_v) belongs to its parent. The other three
crossing-disk triangles are listed in the
[decomposition proof](../notes/actual_all_circle_octahedral_decomposition.md).
The same attachment is made in the other projection half.

This is the local step in the arbitrary-tree induction; the picture
does not prescribe Euclidean lengths. The [geometric chapter](chapters/geometry.md#the-geometric-proof-for-the-explicit-degree-and-twist-bound)
explains the positive hyperbolic realization and the filling path.
Download the [vector PDF](figures/octahedral-page-attachment.pdf) or
the [TikZ source](figures/octahedral-page-attachment.tex).
'''+s[idx:]
write('book/figures.md',s)

catalog=json.loads(read('book/catalog.json'))
entries={
 'actual_all_circle_quantitative_volume':['Equality results','Explicit degree-and-twist volume theorem'],
 'actual_all_circle_octahedral_decomposition':['Geometry','Original ordered exterior and primitive cusp paths'],
 'actual_all_circle_angular_octahedra':['Geometry','Positive octahedral chart and full face maps'],
 'actual_all_circle_geometric_completion':['Geometry','Primitive smooth filling and calibrated knot volume'],
 'actual_all_circle_preferred_cusp':['Geometry','Preferred longitude along the positive filling path'],
 'actual_all_circle_curvature_filling_limit':['Equality results','Quantitative finite-sum proof; geometric companions supplied'],
}
catalog.update(entries)
write('book/catalog.json',json.dumps(catalog,indent=2,ensure_ascii=False)+'\n')
collections=json.loads(read('book/collections.json'))
for c in collections:
    if c['id'] in ['equality','moving-meridian','geometry']:
        adds=list(entries) if c['id']=='equality' else [k for k in entries if (c['id']=='geometry' and k!='actual_all_circle_curvature_filling_limit') or (c['id']=='moving-meridian' and k in ['actual_all_circle_quantitative_volume','actual_all_circle_preferred_cusp'])]
        c['notes']=adds+[k for k in c['notes'] if k not in adds]
    if c['id']=='equality':
        c['scope']+=' A second explicit criterion, sum d_v/(d_v^2+n_v^2)<=2^-25, proves the volume limit for ordered circle trees and permits some short powers at high-degree vertices.'
write('book/collections.json',json.dumps(collections,indent=2,ensure_ascii=False)+'\n')
Path('/private/tmp/md-quantitative-volume-docs-paths.json').write_text(json.dumps(changed,indent=2)+'\n')
print(json.dumps({'changed':changed,'archive':str(archive)},indent=2))
