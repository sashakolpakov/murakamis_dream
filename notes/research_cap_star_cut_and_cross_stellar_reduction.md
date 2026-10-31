# Cap-star cuts and exact CROSS stellar elimination

31 October 2026. **analytical research theorem.**
Unpublished. Original unit face demands and the original protected MAIN
edge are retained throughout. Sections 1–2
are source-flow statements at the stationary classification;
sections 3–5 are exact classical entropy surgery. No finite signed
coupon identity, universal cap exclusion, or volume theorem is asserted.

## 1. A matching edge opposite a cap forces an outgoing overload

Let T be a simple triangulated sphere whose triangle pairs are the
original ports and whose unpaired edges form the simple MAIN
quadrangulation Q. Fix protected adjacent vertices u,v. Name a residual
cap

\[
\begin{gathered}
F=(u,A,v,C),\qquad (u,A,C),\ (u,v,C),\qquad \text{matching edge }uC,\\
q_{F,A}=1-\nu,\quad q_{F,C}=\nu,\quad 0<\nu<\tfrac12,\quad L_A=L_C>0.
\end{gathered}\tag{1}
\]

All ordinary demands are one and all ordinary incidences are positive.
Assume the classification into complete CROSS, strict Green,
and residual marked caps. We do not assume that the other A ports are
CROSS.

Suppose the opposite edge Av EXISTS in T. Bipartiteness of Q implies
that it is MATCHING: A and v have the same color, whereas uA and uv
are MAIN. The simple cycle uAv bounds two disks. Let D be the closed
side not containing C and let r be its number of interior vertices.
They are all ordinary. Euler gives exactly 2r+1 triangles in D.
The only paired edge on its boundary is Av. Thus D contains r WHOLE
ports and one triangle from a unique crossing port E. Write Z for E's
middle on the D side and W for its middle on the other side; its outer
vertices are A,v. Z is interior unless D is the single face uAv, when
Z=u. W is outside D.

Let a_D be the sum of the original A loads of the r whole ports in D.
Every whole port supplies one, irrespective of its CROSS/Green/cap
type. Their total interior contribution is r-a_D, because u,v have
zero load and A is the only other boundary vertex. The only further
interior contribution is q_(E,Z). The original r interior demands
therefore give

\[
a_D=q_{E,Z}.\tag{2}
\]

This includes r=0, where both sides are zero. At A, add the original
cap load, the whole inside contributions and E's outer load. All
other contributions are nonnegative. Consequently

\[
q_{E,A}+q_{E,Z}\le\nu,\qquad
q_{E,W}=1-q_{E,A}-q_{E,Z}\ge1-\nu>\tfrac12.\tag{3}
\]

In particular E is NOT CROSS. This proof never assigns half-supply to
a Green triangle: only whole original port supplies and exclusive
middle incidences are counted. Equivalently, if E were CROSS, its
inside half supplies 1/2, forcing at least 1/2 A load from the disk
and E together, contrary to (1).

If E is Green, W is its child and the exact common-weight relation
implies L_W>L_A (the other outer v is protected). Thus the cap has an
outgoing strict increase in child weight. If E is another cap, its
other zero incidence must be Z=u. Hence D is a single triangle and
E is the other port adjacent to the original mark. Its split nu'
satisfies nu'<=nu. The inequality is strict whenever an additional
positive A incidence remains outside F and E. Equality can only occur
when A belongs exclusively to those two ports; no classification of
that residual topology is needed here.

One immediate useful condition is therefore:

\[
\text{Every }A\text{-neighbor other than }F\text{ is CROSS}
\quad\Longrightarrow\quad Av\notin E(T).\tag{4}
\]

The converse is not asserted. Nor does absence of Av imply Q-degree
two: the bipyramid/K_(2,n) examples have absent opposite apex edge and
arbitrarily many original A incidences.

## 2. A maximal component containing a cap gives an applicable CROSS star

Form the graph on ordinary faces whose edges are the residual caps,
each joining its ordinary outer to its overloaded child. Orient each
edge toward its child. All weights in a connected component agree.
There are at most TWO cap edges, from the two original triangles
adjacent to uv, and no loops because the port vertices are distinct.
Thus the only possible graph cycle is a parallel two-edge pair.

That parallel case forces the four actual triangles
uAC,uvC,uAv,vAC. They exhaust the simple triangulated sphere. With
both ports capped its total sharp value is zero. It is excluded at
the positive-value classified data considered here. Consequently
every cap component is a TREE. This uses the actual at-most-two-mark
incidence; it is not an arbitrary cap-graph assumption.

Demand one implies that every vertex has cap indegree at most one.
A tree on n vertices has n-1 edges, so it has exactly one indegree-zero
root, and all other vertices have indegree one. In a nontrivial tree
choose a leaf other than the root. It is a cap child A and is incident
to exactly one cap F.

Suppose this component's common weight is maximal among ALL
non-CROSS-child weights (both Green and cap children). The leaf A
cannot also be a Green child because its cap load exceeds 1/2. Nor
can it be any Green input: that Green's child would have strictly
larger weight than L_A. The classification therefore implies that
EVERY other original A-incident port is CROSS. In particular its
opposite edge Av is absent by (4). Its original CROSS-star load is
exactly nu in (0,1/2), as required by the
[whole-star spectral estimate](research_cap_cross_shared_star_spectral_gap.md).

This proves the following structural alternative whenever caps exist:

* if a nontrivial cap component (one containing a cap) attains the
  largest non-CROSS-child weight, an
  applicable single-cap / all-other-neighbors-CROSS star exists,
  without any restriction on Q-degree(A);
* otherwise some Green child has weight strictly larger than EVERY
  component containing a cap. No CROSS-only cap star is asserted in
  this case.

In particular ALL cap-only classified positive-value data have an
applicable star, even when both residual caps occur and even when
every cap child has Q-degree greater than two. The exact whole-star
theorem applies to that selected star at its stated weighted
radii. Its improvement is relative to that weighted envelope, not
automatically relative to Phi or a whole Fourier period.

The second alternative is real remaining scope. Selecting only the
largest component CONTAINING A CAP does not eliminate an incident
Green input whose child lies at larger weight outside every such
component. The
cut (3) gives a precise original-flow instance of such escalation.
The argument does not prove that all cap-bearing maxima satisfy the
first alternative, nor does it eliminate an isolated maximal Green.

## 3. An exactly solvable complete triangle refinement

Use the original half-triangle entropy and its weighted potential

\[
\begin{aligned}
\mathcal C(\alpha)&=\sum_{i=1}^3f(\alpha_i),\qquad \sum_i\alpha_i=\tfrac12,\\
Q(a,b,c)&=\max_\alpha\left\{\mathcal C(\alpha)+\sum_i\alpha_i\log a_i\right\},\\
f'(s)&=\log\cot(\pi s),\qquad f(0)=f(\tfrac12)=0.
\end{aligned}\tag{5}
\]

For positive a,b,c put D=sqrt(ab+bc+ca). Its maximizing angles are
alpha_a=atan(a/D)/pi and cyclically. Subdivide the triangle by a new
ordinary vertex of weight

\[
w=a+b+c+2D.\tag{6}
\]

The three new triangle roots are

\[
\sqrt{ab+(a+b)w}=a+b+D,
\]

and its cyclic versions. Tangent addition, with positive denominator
and sum below pi/2, gives the UNSQUARED angle identity

\[
\arctan\frac{a}{a+b+D}+\arctan\frac{a}{a+c+D}
=\arctan\frac aD.\tag{7}
\]

Indeed the tangent of the left side is a/D, and both individual angles
are positive with their sum below pi/2. Thus old corner loads add
exactly as before, and the new w load is 3/2-1/2=1.

The derivative of sum Q(a,b,w)-log w with respect to log w is the
new w load minus one. It is strictly increasing, going from -1 to
1/2. Its unique zero is (6). Differentiating its minimum in the three
old log weights and using (7) shows that its difference from Q(a,b,c)
is constant on the connected positive octant. The exact identity is

\[
\begin{aligned}
\inf_{w>0}\{Q(a,b,w)+Q(b,c,w)+Q(c,a,w)-\log w\}
&=Q(a,b,c)+\kappa_*,\\
\kappa_*&=4f(\tfrac14)=\frac{v_{\mathrm{oct}}}{\pi}.
\end{aligned}\tag{8}
\]

Here is an absolute calibration, not only a differential assertion.
At a=b=c=1 the old angles are all 1/6, w=3+2sqrt(3), and every new
triangle has angles (1/12,1/12,1/3). Since f(1/3)=f(1/6), the entropy
gain is 6f(1/12). The absolutely convergent Fourier expansion

\[
f(t)=\frac1\pi\sum_{\substack{n\ge1\\n\ \mathrm{odd}}}
\frac{\sin(2\pi nt)}{n^2},
\]

has sum_(j=0)^2 f(t+j/3)=f(3t)/3. At t=1/12, using the same
periodic extension and f(5/12)=f(1/12), f(3/4)=-f(1/4), this gives
6f(1/12)=4f(1/4), proving the constant in (8). Formula (8) extends
to protected zero weights by the closed entropy convention.

## 4. Fixed-boundary identity, including every protected zero

Fix ANY closed old triangle allocation alpha>=0 of total 1/2. In the
three refined triangle simplexes, impose total new-vertex load one
and the SAME three old aggregate boundary loads alpha. Then

\[
\max\sum_{\text{three new triangles}}\mathcal C
=\mathcal C(\alpha)+\kappa_*.\tag{9}
\]

For clarity, this is a compact concave optimization identity. Its
fiber is nonempty at every alpha: at a pure old boundary vertex place
1/4 there and 1/4 at w in each of its two incident rows, and put a
pure 1/2 w load in the opposite row; convex combinations give every
alpha. The resulting value function is concave and upper
semicontinuous on the closed half-simplex. Its weighted conjugate is
the left side of (8), by elementary finite-dimensional concave
duality with the single w target. The conjugate of C+kappa_* is the
right side. Equality of the conjugates proves (9), including its
boundary. This argument does not require finite boundary multipliers.

Protected old vertices remain exactly zero, because their total load
is zero and every refined corner is nonnegative. Every other original
face target remains unchanged. There is no redefinition of a mark.

Consequently replacing one CROSS triangle by these three CROSS
triangles, with one new ordinary demand, adds EXACTLY kappa_* to the
maximum of any fixed classical source sector for which the replaced
triangle is CROSS. It adds the SAME constant to complete capacity
Phi. This holds with arbitrary unchanged outside rows, even signed
Green entropy rows, since (9) is a pointwise fixed-boundary identity
before the outside maximization. Conversely an ordinary degree-three
vertex all of whose incident triangles are CROSS can be eliminated
with this constant, provided none of its incidences belongs to a
non-CROSS row and the relevant outside row bookkeeping is retained.

At the purely triangle-flow level, removal gives the smaller simple
sphere when there are more than four old vertices. The intermediate
pairing need not itself be an actual coupon matching. Section 5 gives
a particular refinement whose matching is actual; no arbitrary
elimination is silently promoted to a physical tensor identity.

## 5. Actual matched refinements can raise cap-child degree indefinitely

Suppose a cap has the degree-two patch

\[
F=(u,A,v,C),\qquad E=(A,u,C,Z),
\]

with E CROSS. Its triangles are uAC,uvC and uAZ,ACZ, paired across
uC and AZ respectively. Stellar-subdivide ONLY ACZ by an ordinary W.
Keep the original pair across AZ but replace its ACZ half by AWZ.
Pair the other two new triangles ACW,CZW across CW. The new actual
ports, in harmless middle/outer frame conventions, are

\[
F\text{ unchanged},\qquad E'=(A,u,W,Z),\qquad
E''=(C,A,Z,W).\tag{10}
\]

All four vertices of each port are distinct. The simple MAIN graph
remains bipartite: W has the same color as C,u, while A,Z share the
other color. Every old MAIN edge is retained. The old face weights and circle-packing
disks, and the cap data, are retained. The original port E is REPLACED:
its AZ-paired half ACZ becomes AWZ, and the other two new triangles form
the additional port E''. This does not retain the old coupon disk or
assert equality of old and new links. Q-degree(A) increases by one. Subdivide the
new AZ-adjacent triangle AWZ and repeat: after m steps the SAME cap
child has Q-degree 2+m.

For the sector with the cap fixed as cap and all these neighbor rows
CROSS, (9) gives, for each fixed cap split and then after maximizing
that split,

\[
\begin{aligned}
M_{\mathrm{cap}}(\mathrm{refined})&=M_{\mathrm{cap}}(\mathrm{old})+m\kappa_*,\\
\Phi(\mathrm{refined})&=\Phi(\mathrm{old})+m\kappa_*.
\end{aligned}\tag{11}
\]

Thus the sector's deficit or excess relative to complete volume is
EXACTLY unchanged. Positive stationary data also lift explicitly:
use (6) at each insertion. Every old total face load and weight is
unchanged, the cap still has L_A=L_C and the same nu, and each new
ordinary demand equals one. Newly introduced ordinary angles are
positive unless an incident vertex was one of the original protected
zeros; those zeros remain zero. A stationary cap-only datum is a
sector maximum by concavity of the remaining CROSS entropy and
linearity of the cap row.

This proves a structural limitation of valence-only arguments:
stationary cap-star data and their sector value relative to Phi can
be transported to arbitrarily high cap-child incidence degree. It
does NOT produce a high seed, assert that the refined datum is a
maximum over every non-CROSS assignment, or preserve a particular
flat plat word or filled knot. It constructs actual matched-sphere
sources and an exact classical sector identity. In this particular
refinable class, high degree is reducible back to the seed by (9).

Most importantly, (9) does not transport the finite signed cap/CROSS
contraction theorem. Replacing individual positive CROSS coefficients
inside an alternating cap sum loses its cancellation. No inequality
between those finite signed sums is inferred from entropy surgery.

## Dependencies

- [Full-fiber stationary classification](research_full_fiber_sharp_stationary_classification.md): original common weights, ordinary positivity, and residual cap classification.
- [Exact Green spectral maximum](research_sharp_green_spectral_maximum.md): strict Green weight order and the original closed sharp entropy.
- [Triangle entropy and its weighted potential](actual_triangle_entropy_algebraic_balance.md): the half-triangle Q and f normalization.
- [Exact cap/CROSS incidence](research_cap_cross_incidence_and_disjoint_assembly.md): the internal-face criterion and its matching requirement.
- [Matched-sphere Morse sources](research_matched_sphere_morse_source.md): actual sources for the simple matched spheres in (10), not equality of the different sources.

The stellar refinement retains the old circle-packing data but replaces the coupon E and changes its matching as in (10). It is not a finite signed-source identity or an assertion that the original knot is unchanged.

No numerical audit is needed or claimed. The results do not assert a
coefficient lower rate, finite signed-source rewiring, a universal
Green elimination, or a global spectral/filled-volume bound.
