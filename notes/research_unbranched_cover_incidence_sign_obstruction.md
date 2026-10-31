# Why an unbranched exterior cover does not repair the replicated incidence sign obstruction

Unpublished research lemma, 31 October 2026. Full independent analytical and topological-scope reviews: root and geometry, PASS. This is a
source-preserving cover obstruction, not a fractional atomization argument
and not an assertion that all covers of a link exterior are trivial.

## 1. The proposed construction and the exact scope

Let D be an actual certified marked simple-white plat. Keep its original
white triangulated sphere, pairing of the two triangles at each port,
and protected adjacent MAIN faces u,v. At a port e write the four original
face labels as (x,b,c,y); its two actual shaded triangles have white
incidence sets (x,b,y) and (x,c,y). Their common outer edge xy is MATCHING.
The four labels are distinct. In particular the two outer faces cannot
both be the protected MAIN pair, so at least one outer face is ordinary.

Let B be the original supported bipartite incidence graph: one node for
each port and each ordinary white face, and one edge for every supported
port/face incidence. Write \(\varepsilon_{e,f}\in\mathbf F_2\) for the literal incidence sign
character in the selected source chamber. All exact scalar modes remain
separate. A row gauge and common face signs would solve

\[
 \varepsilon_{e,f}=\kappa_e+\gamma_f\quad\text{in }\mathbf F_2.
 \tag{1}
\]

For the strict straddling LEFT chamber the entries are (0,0,1,0), and
RIGHT is reflected; the argument below allows any chamber whose two
triangle copies of a common outer incidence have the SAME character.
This includes the actual characters in the current regular-window route.

The suggested repair is an actual finite unbranched cover of the original
drilled exterior, with unchanged source chamber and q data on every copy
of each port, followed by the original cut-ball fan construction. To make
that construction source-preserving, it must assign one signed clock to
each lifted white face and allow local row/triangle gauges, with each
lifted incidence retaining its base character. We allow different gauges
on the two triangle halves; this is weaker than requiring a single gauge
on an entire lifted port. Magnitudes may vary between sheets. No averaging
of q, no change of chamber between sheets, and no new incidence signs are
permitted in this particular proposal.

**Theorem.** Under these hypotheses, such a lifted sign assignment exists
on an exterior cover only if (1) already has a solution on the original
supported graph B. Conversely, if (1) is soluble, its signs pull back to
every cover (and the identity cover suffices for this sign issue). Thus
an unbranched cover cannot remove a nontrivial original incidence class
within the proposed source-preserving construction, in any degree.

This is only a necessary sign test for the original group/fan sewing.
Solving it does not supply the other geometric, source-asymptotic, boundary,
or regulator hypotheses of that construction.

## 2. Resolve ports before discussing topology

Let H be the white--triangle incidence graph of ONE original cut ball.
There is one node \(t_{e,+}\) for (x,b,y), one \(t_{e,-}\) for (x,c,y), and one
node per original white face. There is one edge for each triangle corner.
This is the radial graph of the actual white triangulated sphere, not an
abstract replacement of its ribbon structure. Let H' remove only the two
protected white nodes and their incident edges. No ordinary face is removed.

Pull the source character to H' by

\[
 \varepsilon_H(t_{e,+},f)=\varepsilon_{e,f},\qquad
 \varepsilon_H(t_{e,-},f)=\varepsilon_{e,f}.
 \tag{2}
\]

The following elementary equivalence is the key algebraic point:

\[
 \varepsilon_H\text{ is a coboundary on }H'
 \quad\Longleftrightarrow\quad
 \varepsilon\text{ is a coboundary on }B.
 \tag{3}
\]

The forward implication is worth proving explicitly. If

\[
 \varepsilon_H(t,f)=\kappa_t+\gamma_f,
\]

choose an ordinary outer face o of port e. Both halves are incident to o
and have the same prescribed character there. Hence

\[
 \kappa_{e,+}+\gamma_o=\varepsilon_{e,o}
                    =\kappa_{e,-}+\gamma_o,
\]

so \(\kappa_{e,+}=\kappa_{e,-}\). Their common value defines \(\kappa_e\) in (1).
The converse simply copies a row gauge to both halves.

There is also an explicit cycle version. In any supported B cycle, replace
a passage f--e--g by f--t--g if the two faces lie in one half. If it must
pass from b to c, choose an ordinary outer o and use

\[
 b\;--\;t_{e,+}\;--\;o\;--\;t_{e,-}\;--\;c.
\]

The two added outer characters cancel in \(\mathbf F_2\). Each B cycle therefore
gives a closed H' walk with the SAME sign sum. Thus every original
nonzero cycle has a specific resolved witness; protected zero targets
cannot hide it.

## 3. Why the resolved obstruction cannot survive inside a lifted ball

The topological input is the ACTUAL cut described in
[original cut-ball construction](general_augmented_plat_matching_geometry.md), §§1--4. Cut along the
projection sphere and the original crossing half disks. Opening each
specified half disk cancels its semicircle handle. Each resulting piece
is a genuine ball with the original labeled white/shaded boundary.
Compact truncation of its ideal vertices retains a genuine compact ball.
The truncated rectangles at main and auxiliary contacts are boundary
disks, not deleted holes in that ball.

The graph H can be represented on this boundary by face centers and arcs
through their actual common edges. The white--triangle adjacency is the
dual radial adjacency of that labeled medial cellulation. In particular
every H' loop is null-homotopic in the cut ball. Removing protected nodes
from the graph does not remove the protected faces or the filling disks
from the manifold. A small MAIN-contact radial four-cycle bounds a disk
through the corresponding truncated cusp rectangle; larger supported
cycles are no less contractible in the ball. The boundary of one such
rectangle is not itself a main-cusp meridian: a genuine meridional curve
on the assembled cusp torus traverses the appropriate identified
rectangles. One cannot assign nontrivial meridional monodromy to the
perimeter of a single retained rectangle.

For example, the original six-port chart in
[exact face-sign criterion](research_spectral_face_sign_cocycle.md) has triangles (5,7,0) at the
output of port3 and (6,5,7) at the input of port5. Their shared edge
(5,7) is MAIN. The nonzero sign cycle

\[
 \mathrm{port}_3\;--\;\mathrm{face}_7\;--\;\mathrm{port}_5
 \;--\;\mathrm{face}_5\;--\;\mathrm{port}_3
\]

is already the resolved four-cycle around that one contact. Its
obstruction is a contractible disk relation, not a choice of a main
component's meridional monodromy. The general proof does not depend
on this example or assert that its chosen chamber is a full maximum.

For any unbranched covering \(p:Y'\to Y\), pull back the characteristic map of
this compact cut ball. Since the ball is simply connected, each lift is
an actual copy of the entire ball with the same boundary incidence data.
This statement does not require a regular, connected, or double cover.
It remains true when the original shaded pairing sends a half to another
copy, as in a retained half twist: that pairing changes which lifted
balls are glued, not the incidence within a single lifted ball.

Now examine just ONE lifted ball. The proposed common signed clocks give
one \(\gamma\) for each of its ordinary white faces. Each shaded triangle has
its allowed local gauge \(\kappa_t\), possibly coming from a different lifted
port than the other half with the same base label. Because every port
copy retains the base chamber, their incidence relations are exactly (2).
Consequently \(\varepsilon_H\) MUST be a coboundary on H'. Equation (3) forces the
original \(\varepsilon\) to be exact on B. This proves the theorem.

Equivalently, if a graph voltage cover is being interpreted as actual
sheet transition data, all of its resolved H' loop voltages must vanish
because those loops bound disks in one original ball. A nonzero B cycle
has the same-voltage H' witness from §2, violating this necessary extension
relation. Such a graph cover does not extend over the original cut ball;
it is not an exterior cover with the required source incidence dictionary.

## 4. Relation to more general covering criteria

For an independently specified graph map \(i:G\to Y\), a binary voltage
character extends to a double cover of Y precisely when its class lies
in the image of

\[
 i^*:H^1(Y;\mathbf F_2)\longrightarrow H^1(G;\mathbf F_2).
\]

Equivalently it must annihilate the kernel of \(H_1(G;\mathbf F_2)\to H_1(Y;\mathbf F_2)\).
At the presentation level one must also respect every attaching relation;
for permutation-valued finite covers the product of the gluing permutations
around each actual relation is the identity. Agreement of meridional
monodromies along a component is one necessary check, not a substitute
for the ball and edge relations.

No canonical map of the already-collapsed source graph B to Y should be
assumed without checking the two shaded halves and their repeated outer
incidences. The resolved ball graph is what gives the decisive relation
here. The theorem does not claim that every failure to extend a \(\mathbf Z/2\)
character prevents every unrelated finite cover. It proves directly that
ANY proposed exterior cover carrying the replicated original signs and
common-face sewing would already solve (1) on one lifted ball.

## 5. What this rules out, and what it leaves open

This obstruction is different from
[fractional-cover obstruction](research_fractional_cover_star_obstruction.md). There is no atomization,
no change of angle allocations between sheets, and no Jensen loss in
this argument. Replicating q exactly avoids that earlier problem but does
not avoid the contractible resolved sign loop.

It rules out repairing an inconsistent real source sign chamber solely by
passing to an unbranched cover while retaining the original two-ball
white-face and port dictionary. Therefore dividing a hypothetical cover
representation volume by its degree cannot bypass this sign obstruction
under those hypotheses.

It does not rule out a construction that changes the chamber or local
generating function on different copies, changes the projected incidence
data, inserts new defect surfaces, or uses a branched cover. Those would
need their own exact source/action comparison and fundamental-chain proof.
It also does not prove a source upper bound from the unresolved magnitude
and phase-cancellation estimates.

Dependencies inspected: [exact face-sign criterion](research_spectral_face_sign_cocycle.md),
[conditional signed group sewing](research_regular_signed_spectral_group_sewing.md),
[original cut-ball construction](general_augmented_plat_matching_geometry.md) §§1--4,
[original paired fundamental chain](actual_fejer_signed_cut_ball_regulator.md) §3, and the fractional-cover
obstruction above. Geometry independently checked the resolved cut-ball
argument and the ordinary-outer gauge identification. Root subsequently completed a full independent review, PASS. No numerical audit is needed for this finite graph/topological
implication.
