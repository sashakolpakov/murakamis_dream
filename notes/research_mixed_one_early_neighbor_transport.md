# Moving a coordinate with one early neighbor

Research proof, 4 November 2026. The local transport inequality is
reduced to a complete family of rational parameter boxes. Its outward
cover has passed; the canonical and separate replay records give the
verification status of that cover. Numerical minimization only proposed
the auxiliary constants. Every accepted box requires an outward
inequality on the entire box.

We use the phases, contours and fixed sets of the
[frozen-early transport argument](research_mixed_frozen_early_transport.md).
An early coordinate belongs to \(E=[.1,.12]\); a plateau coordinate
belongs to \(P=[.22,.45]\). The two cutoffs rise from zero at .1 to
one at .22 and .12, respectively. Write them as \(\rho\) and
\(\widehat\rho\), and put \(H=.014\).

Let \(i\) be a moving coordinate that currently attains the smallest
moving real value \(t\in[.12,.22]\). Suppose exactly one of its two
neighbors is early. Denote that neighbor by \(e\), and the other by
\(n\). Let \(o\) be the next position beyond \(n\), away from \(i\).
Types three and four are the two original crossing types; their
indicators in the phase \(\phi_{\eta\epsilon}\) are zero and one.
All gradients below are derivatives of those original holomorphic
phases, with their fixed logarithmic branches and normalization.

## 1. Which heights move

The contour heights at \(i\) and \(e\) are fixed while this minimum
is raised. Thus their height derivative coefficients are both zero.
The only possibly changing height in the three incidences entering
the local transport inequality is the one at \(n\). If its closed
neighborhood contains an early position, or if it is selected, this
derivative coefficient is also zero. Otherwise it equals
\(c_n=\Im r_n\), where \(r\) is the original geometric critical
point. In the latter case
\[
 \Im z_n=c_n\rho(t),\qquad x_n,x_o\in[t,.45].                 \tag{1}
\]
Indeed, the moving center belongs to that neighborhood, and its other
two real coordinates are no smaller than \(t\). Neither can be an
isolated position between two early coordinates: one of its neighbors
is non-early. If \(o\) is early, the derivative coefficient at \(n\)
is zero instead, and (1) is not used.

Set \(G_j=\partial_{z_j}\Phi\), where \(\Phi\) is the cyclic
sum of block phases. The required local inequality is therefore
\[
 \Re G_i+\min\{-c_n\Im G_n/.12,0\}\ge0                     \tag{2}
\]
when that coefficient is active, and simply \(\Re G_i\ge0\)
otherwise. Equivalently, in the active case we must bound both
switches \(\xi=0,1\) in
\[
 \Re G_i-\xi c_n\Im G_n/.12.                              \tag{3}
\]
No height derivative is assigned to a selected coordinate merely
because its actual height is nonzero.

## 2. The correlated early heights

Put \(u=x_e-.1\in[0,.02]\). At a type-three position the
geometric height coefficient lies in \([-.03,.02]\); at type four
it lies in \([-.057,-.02]\). The actual early height and the
center height consequently belong to the following intervals:
\[
 J_3(u)=[-u/4,u/6],\qquad
 J_4(u)=[-19u/40,7u/10].                                  \tag{4}
\]
For an unselected position this follows by multiplying its coefficient
by a fraction no larger than \(u/.12\). For a selected type-four
position the upper endpoint is \(H u/.02=7u/10\). The intervals
in (4) include both possibilities, without identifying selection
with a height derivative.

In particular the center height lies in
\[
 J_3^*=[-.005,1/300],\qquad J_4^*=[-.0095,.014].             \tag{5}
\]
The correlation with \(u\) in (4) matters when the center is type
four and the early neighbor is on the right. In the other cases it
is harmless to enlarge the center interval to (5). We keep (4) for
the early coordinate in every case.

## 3. The non-early neighbor and its outer argument

If the switch in (3) is zero, the height of \(n\) may be released
into the following polygon, with \(x\in[t,.45]\):
\[
 \begin{array}{ll}
 \Omega_3(t):&-.03\rho(x)\le h\le .02\rho(x),\\
 \Omega_4(t):&-.057\rho(x)\le h\le H.
 \end{array}                                               \tag{6}
\]
These polygons include active, frozen and selected heights of the
indicated type. Their lower boundaries have a corner at .22; the
upper boundary of \(\Omega_3\) has one there as well. Thus their
boundaries consist of six and five straight segments, respectively.
For fixed center, the switch-zero expression is the real part of a
holomorphic function of \(z_n\). Its minimum is attained on these
segments. This is a boundary reduction in a complex variable, not
an assumption of concavity after inserting the contour cutoff.

If the switch is one, use (1). The allowed interval for \(c_n\)
depends on its two neighboring types. Combining the
[three-position enclosures](research_mixed_neighbor_conditioned_critical_boxes.md),
the [consecutive-four bound](research_mixed_four_before_four_height.md)
and the [three consecutive four bound](research_mixed_three_consecutive_four_height.md) give the following
intervals. The stronger entry for \((4,4,4)\) is a required input
to the certificate, not a conclusion of numerical sampling here.
\[
\begin{array}{c|c@{\qquad}c|c}
\text{types around }n&c_n&\text{types around }n&c_n\\\hline
(3,3,3)&[-.010,.010]&(4,3,3)&[-.017,.002]\\
(3,3,4)&[-.017,-.002]&(4,3,4)&[-.025,-.011]\\
(3,4,3)&[-.049,-.030]&(4,4,3)&[-.054,-.036]\\
(3,4,4)&[-.057,-.048]&(4,4,4)&[-.057,-.053].
\end{array}                                                \tag{7}
\]
The order in this table is the original cyclic order. Thus it is
\((o,n,i)\) when \(n\) is left of \(i\), and \((i,n,o)\)
when it is right of \(i\).

The outer argument \(z_o\) is released into (6). When its type is
three and the neighboring type at \(n\) is four, its lower bound
can be improved to \(-.025\rho(x_o)\). To see this, inspect the
four type-three-middle rows of the original three-position table:
all have lower height at least -.025. Multiplication by any fraction
between zero and \(\rho(x_o)\) preserves the asserted lower bound.
We need no improvement to its upper bound. All type-four outer
heights use the unchanged second polygon in (6).

For fixed center, neighbor and coefficient \(c_n\), the active
expression (3) is the real part of a holomorphic function of \(z_o\).
Its minimum therefore occurs on the five or six indicated boundary
segments. All these polygons lie in the established cotangent chamber
and enlarged source cap. The conditional holomorphic branch exists
on their interiors before the maximum principle is used. There is
no analogous boundary reduction in the remaining real parameters.

## 4. Splitting the derivative into its two incident blocks

When the early neighbor is left of the center, write
\[
 E=\Re\partial_2\phi(z_e,z_i),\qquad
 O_\xi=\Re\partial_1\phi(z_i,z_n)-\xi c_n\Im G_n/.12.
                                                               \tag{8}
\]
When it is right of the center, write
\[
 E=\Re\partial_1\phi(z_i,z_e),\qquad
 O_\xi=\Re\partial_2\phi(z_n,z_i)-\xi c_n\Im G_n/.12.
                                                               \tag{9}
\]
In (8) the active neighbor derivative is
\(G_n=\partial_2\phi(z_i,z_n)+\partial_1\phi(z_n,z_o)\);
in (9) it is
\(G_n=\partial_2\phi(z_o,z_n)+\partial_1\phi(z_n,z_i)\).
Every phase carries its indicated pair of original types.

For a type-three center no adjustment is needed: the proposed
inequalities are \(E>0\) and \(O_\xi>0\).
For a type-four center with early neighbor on the left, they are
\[
                         E+1/5>0,\qquad O_\xi-1/5>0.         \tag{10}
\]
For a type-four center with early neighbor on the right, put
\[
                \gamma(h)=4|h|-53/1000,\quad h=\Im z_i,
\]
and use
\[
                         E-\gamma(h)>0,\qquad
                         O_\xi+\gamma(h)>0.                \tag{11}
\]
The adjustments cancel exactly in either sum. They change neither
the contour nor the rate function. The two closed intervals \(h\le0\)
and \(h\ge0\) are checked separately in (11), so the adjustment is
affine on each domain and its derivative is retained.

For the early half only, we may put the center real coordinate equal
to .22. With all heights and the early argument fixed,
\[
 \frac{dE}{dt}=\Re\partial_{ii}^2\phi<0.                   \tag{12}
\]
The strict inequality is the established negative real Hessian of the
conditional phase on the small-height domain. The adjustments in
(10)--(11) do not depend on \(t\). Consequently the early half at
every smaller \(t\) is bounded below by its value at .22. The
correlated intervals (4) are kept while making this reduction.

## 5. The finite inequalities to certify

There are eight early cases: two center types, two early types and
two orientations. There are eight switch-zero other cases: two center
types, two neighbor types and two orientations. There are sixteen
switch-one other cases, with the two possible outer types added.
Splitting (11) at height zero and using the polygon boundaries gives
175 charts covering these thirty-two cases: ten early charts,
55 switch-zero neighbor charts, and 110 switch-one outer charts.

The early boxes use \(u\), the early height coefficient in (4), and
the center height from (4) or (5). The other boxes use \(t\), the
neighbor real coordinate, the relevant polygon segment parameter,
the center height in (5), and, for switch one, the coefficient in
(7). Every endpoint is rational. In particular the dependence of
\(\rho(t)\), of the moving polygon vertices, and of \(\gamma\)
must be included in each full-cell derivative bound.

**Proposition 1.** The positive half inequalities on the complete
175-chart cover imply (2) for every moving center with exactly one
early neighbor. This conclusion requires every chart, with both
height signs and every indicated polygon side retained. Adding the result for
[centers with no early neighbor](research_mixed_frozen_outer_half_stencils.md)
then supplies the local hypothesis in the frozen-early transport
argument. A center with two early neighbors is already fixed and its
incident blocks are controlled directly.

For short cycles there is no extra assumption of distinct released
variables. A two-vertex cycle cannot have exactly one early incidence:
its two neighbors coincide and the non-early vertex is fixed. In a
three-cycle the active other-neighbor case is impossible if its
neighborhood contains the early position; it is then a switch-zero
case. In every admissible active case, releasing equal cyclic
variables independently only enlarges the tested domain.

This conclusion concerns phase transport on the left region. It
does not control the right transition, mix low or right coordinates
into this region, or establish stability under arbitrary short knot
fillings.


## 6. Verifying the complete cover

The saved cover has 354,894 accepted leaves, 716,155 visited nodes,
and 6,542 reductions to a minimizing endpoint. The outward calculation
used 192-bit arithmetic. The canonical checker reevaluates the cover at
256 bits; the separate implementation uses 320 bits and independent
sine-logarithm root equations, explicit cotangent derivatives, and
explicit derivatives of all parameter maps.

Each leaf encloses the original logarithmic root by a rational affine
Newton self-map. Its phase gradient and condensed Hessian give a
whole-box mean-value lower bound for the adjusted half expression.
A direct interval lower bound is also permitted. Either acceptance
criterion must be strictly positive. A monotonicity reduction is used
only after the corresponding derivative has one strict sign on the
whole box; the checker then retains the minimizing endpoint. Binary
splits divide an exact rational interval in half. Reconstructing the
entire split tree, and consuming every saved node, verifies that no
part of any chart is omitted.

The two implementations retain the derivative of the active coefficient
in the product with the neighboring gradient. They also retain the
moving polygon endpoints, the correlated early heights and the signed
slope of the auxiliary function in (11). The independent implementation
writes polygon edges as a fixed endpoint plus a parameter times the
edge vector; this avoids an unnecessary interval enlargement without
altering either the edge or its derivatives.

Before and after a replay, the checker verifies the proof, scripts,
saved cover and imported inputs against their recorded hashes. It also
compares the eight intervals in (7) with the original geometric records,
including the two stronger type-four bounds. The ordered list of all
175 charts is fixed in the checker. Neither saved decimal minima nor
floating root proposals can make a leaf pass.

The reproduction commands keep their new results separate from the
canonical records:

```sh
python3 experiments/certify_mixed_one_early_neighbor_transport.py --precision 256 --input repro/results/research-mixed-one-early-neighbor-transport.json --output /tmp/research-mixed-one-early-neighbor-transport-review.json
python3 experiments/replay_mixed_one_early_neighbor_transport.py --precision 320 --jobs 3 --output /tmp/research-mixed-one-early-neighbor-transport-independent-review.json
```
