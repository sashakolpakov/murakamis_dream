# A matched spherical triangulation has the original general Morse source

31 October 2026. Internally reviewed research theorem. This is a finite
topology/source extension, not a volume asymptotic and not a claim that a
new presentation has a prescribed flat-plat width.

## 1. Input, conclusion, and the local ordering

Let \(\mathcal T\) be a finite connected triangular cellulation of the
oriented sphere, with a perfect matching \(D\) of its cubic dual
\(\Delta\). Assume every paired pair of triangles has a four-sided disk
as its union, with four distinct white vertices. Equivalently, begin
with a connected spherical quadrangulation \(\mathcal Q\), choose one
embedded diagonal in each quadrilateral, and triangulate along those
diagonals. Parallel edges produced by a choice of diagonals are not
silently identified. They are allowed as cellulation data here. A
positive geometric certificate, when needed, is a separate hypothesis.

There are \(2R\) triangles, \(R\) matched pairs, and \(R+2\) white
vertices. For each quadrilateral choose the oriented cyclic order
\((x,b,y,c)\), with chosen diagonal \(xy\). The two triangles are
\((x,b,y)\) and \((x,c,y)\). The local box frame is input middle \(b\),
output middle \(c\), left outer \(x\), right outer \(y\). Reversing
this frame later would require its actual duality adapter; no such
unrecorded reversal is part of the construction.

The construction below gives a genuine augmented link in \(S^3\), with
\(R\) labeled twice-punctured crossing disks, whose original cut graph
is \((\Delta,D)\). It has a general Morse diagram containing exactly
these \(R\) recorded two-strand boxes and no other crossing. In the
fixed frames, any full original coupons
\(f_e(\Omega)R^{\epsilon_e}\) have exactly the homogeneous source
\[
 P(L)=\prod_{e=1}^R H_{f_eR^{\epsilon_e}}
       (L_{x_e},L_{b_e},L_{c_e},L_{y_e}).             \tag{1}
\]
For any MAIN edge between faces \(a,b\), the original raw one-mark
contraction is exactly
\[
 I_N=[\prod_{f\ne a,b}L_f^{N-1}]\,P\big|_{L_a=L_b=0}.
 \tag{2}
\]
It is independent of the selected MAIN edge. The formula uses the
original turns, reduced mark, all full crossing scalars, and complete
root Hermite data. No level factor is suppressed.

## 2. Inverting the actual crossing-disk cut

Embed the cubic dual \(\Delta\) on the sphere. Choose disjoint small
regular-neighborhood disks around the matched edges and their endpoint
vertices. Because \(D\) is a perfect matching, these disks are disjoint
and meet the other edges in four boundary terminals each. Contracting
each disk gives a connected plane four-valent graph \(G\), with
\(R\) vertices and \(2R\) edges.

At one disk label the four terminals cyclically \(0,1,2,3\) so that
the two original matched vertices group terminals \((1,2)\) and
\((3,0)\). These are the two shaded half-disk sectors. Draw the
**physical untwisted main strands** with the other planar pairing
\[
                   (0,1),\qquad(2,3).              \tag{3}
\]
These arcs are disjoint. Join the terminals outside the disks along
the original nonmatching dual edges. The result is a finite union of
embedded circles in the projection sphere. Each circle meets a box,
because every piece came from the finite four-terminal construction.

One must not identify these circles with the abstract cycles of
\(\Delta\setminus D\): the latter uses the shaded grouping
\((1,2),(3,0)\), whereas the physical strands use (3).

In a disjoint three-ball neighborhood of each disk put the standard
perpendicular crossing circle and its twice-punctured spanning disk,
meeting exactly the two strands in (3). All its labels and its collar
orientation are inherited from the chosen local box frame. This is an
explicit link embedded in \(S^3\); no abstract three-manifold
realization theorem is needed.

Cut it along the projection sphere and open each original upper and
lower half disk. The two shaded triangles at the box have the original
labels
\[
 S_0=(O,C_1,C_2),\qquad S_1=(O,C_3,C_0).
\]
The untwisted within-copy gluing fixes \(O\) and sends
\(C_1\mapsto C_0\), \(C_2\mapsto C_3\). Thus the cut is literally
the inverse of sections 1–4 of
[original matching-graph cut](general_augmented_plat_matching_geometry.md). Its medial
boundary graph is the medial graph of the supplied \(\Delta\), with
every original white face and matching edge retained. The proof there
that opening the disjoint half disks gives two balls is local and
does not use a plat sweep; it therefore applies to this construction.

Insert a recorded half twist \(\epsilon_e\in\{0,1,-1\}\) in a box
when desired. Its original shaded maps are precisely the cross-copy
maps in that same cut theorem. Both nonzero signs have the same
terminal permutation but retain their different disk-framed peripheral
paths. The external graph and the local polynomial frame are unchanged.

## 3. A knot parity pattern exists, without a bridge-width assertion

Start with the untwisted physical circles of section 2. Form a finite
graph whose vertices are these circles and whose edge at a box joins
the two circles passing through that box (a loop is allowed). This
graph is connected: otherwise the union of boxes and outside arcs,
and therefore the connected four-valent graph \(G\), would split.

Choose a spanning tree. Give its boxes odd parity and all other boxes
even parity. Switching a tree box from (3) to the odd pairing
\((0,2),(1,3)\) joins two distinct current circles into one. Process
the tree edges in any order: after any subset, its connected tree
components are exactly the merged circles, so the next edge still
joins two different circles. Thus the final main link has one
component. Each odd sign may independently be chosen \(+1\) or \(-1\).

Filling box \(e\) with any integer power \(n_e\) of that parity
preserves this one-component property. The original convention is
\(n_e=\epsilon_e-2p_e\), where \(p_e\) is the integer full-twist
filling coordinate in the recorded local disk framing. Arbitrarily
large independent positive or negative powers of the chosen parity
are available. This says nothing about minimal bridge number or a
specified original flat width.

## 4. Producing the original finite Morse tensor network

Choose a point outside the disks as infinity. In each disk use its
given orientation-preserving parametrization to draw two vertical
strands, with terminals \(1,2\) at the input and \(0,3\) at the
output. The local quadrilateral is then exactly
\((x,b,y,c)\) in section 1. The finitely many disjoint disks can be
placed in such plane charts independently; this fixes, rather than
transports or resets, their ordered four-leg frames.
More explicitly, straighten each chosen disk parametrization in its
own disjoint collar, and extend those collar changes to an
orientation-preserving plane isotopy. The remaining outside arcs are
then drawn between the resulting boundary endpoints. Thus the local
vertical charts belong to one global plane drawing; no ribbon normal
twist or permutation of a coupon's legs is introduced.

Smooth the outside arcs and perturb their height functions away from
the disks. There are finitely many ordinary nondegenerate maxima and
minima, all at distinct heights after another small perturbation. No
new crossing or ribbon twist is required. This is a general Morse
diagram, with arbitrary cups/caps between recorded box heights. It
need not be a plat with all cups below and all caps above the boxes.

Evaluate it using exactly the original complete module \(V_d\), its
regular self-duality \(J\), all four original turns, the original
checked crossings and Casimir coupons, and one exposed original
reduced cap. Upward/downward arcs carry the corresponding actual
module or dual; their physical frames are related by \(J\), not by
an independently reset diagonal insertion. Since the complete object
is self-dual, these are the same original finite matrices in the
ordered balanced head frames. This is the usual original ribbon
tangle evaluation on the explicitly constructed diagram.

There is no new normalization ambiguity. For fixed \(N\), the regular
generic lift uses \(\widetilde g=(-1)^HK\), with
\(J^{-t}J=\widetilde g\), which specializes literally to
\(g=K^{1-N}\). Its two traces agree on every endomorphism in the
tensor-generated integral-weight category. The full proof, including
duals and regular root specialization, is in sections 2–3 of
[all-MAIN mark and general Morse compiler](research_arbitrary_main_edge_mark_transport.md); it is independent
of a flat layout. Its snakes prove invariance under the Morse
interchanges just used. Its spherical trace exchange exposes any
selected MAIN edge as a top cap while keeping every coupon disk fixed.

The cut network is a regular generic intertwiner on \(V_d\) or its
dual. Its \(K\) weights are distinct and its internal \(F\) arrows
nonzero, so it is scalar. Its ordinary closure is
\((-1)^d[N]_q\) times that scalar. Equality of closed spherical
readings, followed by regular specialization, proves independence of
the reduced marked scalar from the MAIN edge. No root quantum
dimension is divided by zero. This argument works on any component
because all the complete colors agree.

## 5. General Morse winding and the full original coefficient

Here the all-MAIN compiler is repeated on the new diagram itself;
there is no assumed old flat diagram whose coefficient is being
transported. Choose the marked edge's adjacent face \(a\) as exterior
and expose a top cap, with \(b\) its inside face. A connected
four-valent graph has no bridge (the parity of degrees in either
component would contradict one crossing edge), so these two faces are
distinct. The finger move preserves their labels.

Put \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\). In literal left-to-right
head order \((i,j)\), both original left/right cups and both caps are
\[
 p_{ij}=Nq^{-d^2+di}\,1_{i+j=d},\qquad
 \ell_{ij}=N^{-1}q^{di}\,1_{i+j=d}.                 \tag{4}
\]
The exposed original mark, after the whole-source conservation forces
its two remaining heads to sum to \(d\), is
\(m_{ij}=N^{-2}q^{dj}\). This is a consequence of the full source,
not an early restriction of the unrestricted marked matrix. Its
contraction with its original cup is exactly one.

At every fixed coupon the original adapter is
\[
              N^{-1}H_e(x,b,c,y)/(bc)^{d/2}.        \tag{5}
\]
Let \(M_f\) count middle incidences at boxes and \(T_f\) count outside
turns minus inside turns in face \(f\), temporarily including the
ordinary cap that will be marked. Round each fixed local box in its
actual frame. Each middle passage contributes \(+\pi\) to the
boundary turning index and the two outer passages have net zero;
inside turns contribute \(+\pi\) and outside turns \(-\pi\).
The bounded face winding is \(+1\) and exterior winding \(-1\),
counting repeated boundary occurrences. Therefore
\[
 M_f-T_f=2\ (f\ne a),\qquad M_a-T_a=-2.           \tag{6}
\]
This is the face-boundary proof in section 6 of the all-MAIN theorem,
which uses only the local boxes and Morse arcs, not their vertical
ordering or a flat gap forest.

All ordinary turns and (5) thus give
\(L_a^d\prod_{f\ne a}L_f^{-d}\). The exact mark/cap ratio is
\(N^{-1}(L_b/L_a)^d\). If there are \(k'\) cups, there are \(k'\)
caps; their complete powers of \(N\) give
\(N^{k'}N^{-(k'-1)}N^{-2}=N^{-1}\). Their recorded \(q\)-constants
cancel, just as in (4). The whole marked summand is consequently
\[
              N^{-R-1}\frac{P(L)}{\prod_{f\ne a,b}L_f^d}.
 \tag{7}
\]

The integral conserved-head lattice is the original cycle lattice of
the connected spherical graph. Bending edges does not change it.
Integration across dual paths identifies it primitively with face
potentials modulo their common constant. There are \(R+2\) faces,
thus \(R+1\) independent grids after \(L_a=1\). For odd \(N\) use
\(L_f=Q^{p_f}\). For even \(N\), the cochain which is one on MAIN
edges and zero on matching edges is closed: each triangle has two
MAIN edges. Since the sphere is simply connected it integrates to
\(t_f\in\mathbb F_2\), with \(t_a=0,t_b=1\); use
\(L_f=q^{t_f}Q^{p_f}\).

The local full-polynomial adapter first imposes the canonical physical
head support, killing all wrong unwrapped totals. Supported states and
primitive grids then correspond exactly. Only coherent integrated
face-log lifts are varied; no arbitrary individual head reset is
used. The \(N^{R+1}\) grid count cancels (7). Nonnegative exponents of
total degree \(dR\) leave only the alias
\(n_a=n_b=0\), \(n_f=d\) otherwise: those \(R\) ordinary minimum
degrees already exhaust the total. The even coset character is one
there. This proves exactly (2), with no additional factor of \(N\).

## 6. Original signed filling powers and their whole spectral functional

Replace the \(e\)-th box by its actual \(R^{n_e}\), where the signed
integer \(n_e\ne0\) is fixed before \(N\). The exact local identity
\[
 R^{n_e}=q^{n_ed^2/4}
       \exp\!\left(\frac{n_e K(\Omega)}{2\hbar}\right),
 \quad \hbar=2\pi i/N,\quad K(z)=\operatorname{arccosh}(-z/2)^2,
 \tag{8}
\]
retains all Hermite derivatives and every crossing scalar. It is the
fixed-root identity of [exact original signed crossing powers](actual_direct_long_power_source.md).
The explicit Gaussian/resolvent numerator functional is also recorded in
[exact Gaussian/resolvent functional](actual_gaussian_resolvent_numerator_and_cap.md).
Different boxes do not need to commute; their ordered tensor
contraction is multilinear in the local matrices.

Define the full spectral numerator using the newly constructed
original source,
\[
 S_N(\boldsymbol\sigma)
 =[\prod_{f\ne a,b}L_f^d]
   \left.\prod_e H_{V_N(\sigma_e)}\right|_{L_a=L_b=0}.
 \tag{9}
\]
Applying the original matrix Fourier/Hermite functional separately at
each box gives exactly
\[
\begin{split}
 I_{N,\mathbf n}={}&q^{\frac{d^2}{4}\sum_e n_e}(-i)^R
 \sum_{\boldsymbol\ell\in(\mathbb Z\setminus\{0\})^R}
  \Bigl(\prod_e\ell_e\Bigr)(-1)^{(N+1)\sum_e\ell_e}\\
 &\ \times\int_{[-1/2,1/2]^R}
  \Bigl(\prod_e\sin(2\pi\delta_e)\Bigr)
  S_N(-2\cos(2\pi\boldsymbol\delta))\\
 &\ \times\exp\!\left\{N\sum_e
       [\pi i n_e\delta_e^2+2\pi i\ell_e\delta_e]\right\}
      d\boldsymbol\delta .
\end{split}\tag{10}
\]
This is the same local source-independent finite functional as in
section 1 of [original whole spectral period](general_localized_unit_charge_filling_period.md).
Its charge-zero absence and whole-domain absolute summability hold
before any geometric estimate. The proof uses the local matrix
identity, the entire finite-degree numerator, and its original sine
endpoint factors; it does not use a plat sweep. All side currents in
a subsequent contour deformation would still have to be retained.

The raw scalar in (10) is the actual original reduced ribbon
contraction of the filled link constructed above. Its conversion to
the specified zero-framed enhanced Kashaev convention is the original
recorded framing/component character. At complete color its modulus
is one; for a knot the enhanced component sign is one. If instead
using the full one-cut modified convention, retain its additional
\(i^{N+3}/N\). These exact distinctions are proved in
[complete source normalization](actual_complete_augmented_source_normalization.md), using
local crossing/duality identities and scalar cut maps; they do not
depend on the bridge count. No extra quantum dimension, semicircle
normalization, or exponential basis factor has appeared here.

For the complete augmented link, the original local crossing-circle
contraction is still its exact \(L_N\) coupon, with its one ordinary
auxiliary trace and no extra modified dimension. Thus (1)–(2) apply
to that source too. A geometric certificate identifies its two cut
balls with the original right-angled polyhedron and gives the actual
augmented exterior, as in section 2; a volume asymptotic requires
its own verified analytic hypotheses.

## 7. Scope needed by a diagonal-choice argument

This theorem constructs an actual source for **each** diagonal choice
on the fixed quadrangulation. The constructed links for different
choices need not be isotopic, their marked coefficient polytopes need
not coincide, and no projected sector or physical operator is moved
from one choice to another. The common quadrangulation supplies a
common finite combinatorial indexing only.

Every original target, half-index coset, retained half-twist and
disk-framed signed filling coordinate has now been supplied for that
choice. Consequently a proposed complete-capacity-maximizing choice
can refer to a genuine original source rather than a formal entropy
model. This does not by itself prove its global source estimate,
local filling packet, nonzero period, hyperbolicity, or volume limit.
Those hypotheses must be checked on the chosen diagram. In
particular no old flat-plat gap forest or prescribed bridge width
has been transported merely by constructing a general Morse source.

## Internal review and limits

Root and geometry independently read the complete written topology/source
proof and gave full analytical/source PASS, including the local collar
straightening, the actual terminal pairing, and the new-network winding
compiler. Cluster independently read section 6 and gave a full targeted
source/normalization PASS, retaining the Hermite data, ordered multilinearity,
whole-domain charge series, and separate framing/modified scalars.

All finite matrix ingredients are the previously reviewed original duality,
homogeneous source, all-MAIN compiler, and local full-Hermite filling
functional. No new numerical audit is asserted for this constructive proof.
No global spectral comparison, filling asymptotic, prescribed plat width,
or equality between sources from different diagonal choices is claimed.
