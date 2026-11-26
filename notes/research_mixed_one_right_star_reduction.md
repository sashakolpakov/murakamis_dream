# A finite local domain for one adjacent right coordinate

Research deduction, 5 November 2026. This note reduces the conservative
whole minimum-flow derivative with exactly one adjacent right incidence
to explicit finite families with at most five real parameters. It does
not prove that those families are nonnegative. Both chirp orientations,
all three permitted endpoint states, and the true Fourier alternatives
are retained. No new parameter cover or finite-source theorem is used.

## 1. Original functions and the minimum-flow domain

Let a type indicator be \(\alpha=0\) for type three and \(\alpha=1\)
for type four. Use the original normalized primitive and allocated
conditional phase
\[
\begin{split}
 g(z)&=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},\\
 Q_\epsilon(s;a,b)
   &=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias,\\
 \phi_{\eta\epsilon}(a,b)
   &=Q_\epsilon(s_*(a,b);a,b)
      -(1+\eta/2)g(a)-(1+\epsilon/2)g(b).
\end{split}                                                     \tag{1}
\]
Every branch in (1) is the original zero logarithmic lift. Define
\[
 \rho(x)=\min\{(x-.1)/.12,1\},\qquad H=.014,\qquad
 R(x)=
 \begin{cases}
  1,&.12\le x\le.45,\\
  400(.5-x)^2,&.45\le x\le.5.
 \end{cases}                                                     \tag{2}
\]
Only \(x\ge.12\) is used below. All right coordinates have already
been fixed at \(.5\) by the
[complete raw-row reduction](research_mixed_complex_right_row_reduction.md).
There are no collar, deep-low or early coordinates in this local
statement. Every other real coordinate is at least the moving minimum
\[
                         .12\le t\le.22.                       \tag{3}
\]
The word and its actual critical reference are fixed. Its unselected
height coefficients lie in
\[
 C_3=[-.03,.02],\qquad C_4=[-.057,-.02].                         \tag{4}
\]
Replacing a correlated reference window by independent intervals (4)
is an enlargement for the sufficient inequality, not an assertion
that every resulting height tuple is an actual critical reference.

The three states are \(U_3,U_4,S_4\): unselected type three,
unselected type four, and selected type four. A selected state's
actual height coefficient is \(H\); its coefficient of height change
in this flow is zero. Put \(r=\rho(t)\). If \(c\) denotes an
unselected original coefficient, the moving center and its nonright
neighbor have targets
\[
\begin{array}{c|cc}
 &U_3\text{ or }U_4&S_4\\ \hline
 z_c&t+ic_c r&t+iH\\
 z_n&y+ic_nR(y)r&y+iHR(y)
\end{array}
 \qquad t\le y\le.5.                                          \tag{5}
\]
This follows literally from the row-dependent minimum in the
[split-cutoff hybrid](research_mixed_split_cutoff_hybrid_contour.md):
the center belongs to the neighbor's closed three-position
neighborhood and realizes its smallest slow cutoff. All fast cutoffs
are already one. The value \(y=.5\) is an allowed closure of the
nonright parameter domain; its height and height velocity are zero.

For unselected states set
\[
 b_c=c_c/.12,\qquad b_n=c_nR(y)/.12,
 \qquad v_c=1+i\chi_c b_c,\qquad v_n=i\chi_n b_n,
 \qquad \chi_c,\chi_n\in\{0,1\}.                               \tag{6}
\]
At a selected state set its \(b\) and its \(\chi\) to zero.
The coefficients \(c_c,c_n\) in (6) remain the original coefficients
in (4), even though their target heights in (5) have the additional
factor \(r\).

## 2. The exact whole-star expressions

For a raw edge meeting \(.5\), write
\[
 K_{\alpha,d}(z,u)
   =g'(z+u)-(1+\alpha/2)g'(z)+2\pi i d u,\qquad
                    u\in\{1/5,2/5\}.                         \tag{7}
\]
Here \(d=1\) means that the moving A target is the first argument.
The right endpoint's type changes the optimizing raw row, but does
not occur in (7). The
[row bracket and endpoint theorem](research_mixed_raw_row_stationarity.md),
equations (3)--(13), apply to every physical right endpoint type.

Formula (7) does not silently discard a selected Fourier branch.
For an unselected moving state the original row branch is exactly
(7). For a selected center \(t\le.22\), the established strict
inequality
\[
 -\Re g(t+iH)-2\pi H>3/40                                    \tag{8}
\]
from the [selected branch theorem](research_mixed_selected_minimum_flow_obstruction.md)
selects the factorial Fourier alternative. Its marginal is
\(K_{1,d}+\pi i\); since \(v_c=1\), the added term has zero real
contribution. A selected neighbor has \(v_n=0\). All other selected
targets are stationary in this local derivative. Equivalently,
their complete corrections
\(\max\{\Re g(z),-2\pi\Im z\}\) have zero derivative here.
Unselected type-four targets have nonpositive heights, so their
factorial alternative dominates; at \(y=.5\) a possible tie is
multiplied by zero velocity.

First take the orientation
\[
                  o\longrightarrow n\longrightarrow c
                       \longrightarrow R .
\]
For an A outer target \(z_o\), define
\[
\begin{split}
 G_c^\rightarrow
   &=\partial_2\phi_{\alpha_n\alpha_c}(z_n,z_c)
                         +K_{\alpha_c,1}(z_c,u_c),\\
 G_n^\rightarrow
   &=\partial_1\phi_{\alpha_n\alpha_c}(z_n,z_c)
                         +\partial_2\phi_{\alpha_o\alpha_n}(z_o,z_n),\\
 D^\rightarrow
   &=\Re\{v_cG_c^\rightarrow+v_nG_n^\rightarrow\}.
\end{split}                                                     \tag{9}
\]
For the reverse orientation
\[
                  R\longrightarrow c\longrightarrow n
                       \longrightarrow o
\]
the literal expression is
\[
\begin{split}
 G_c^\leftarrow
   &=K_{\alpha_c,0}(z_c,u_c)
                         +\partial_1\phi_{\alpha_c\alpha_n}(z_c,z_n),\\
 G_n^\leftarrow
   &=\partial_2\phi_{\alpha_c\alpha_n}(z_c,z_n)
                         +\partial_1\phi_{\alpha_n\alpha_o}(z_n,z_o),\\
 D^\leftarrow
   &=\Re\{v_cG_c^\leftarrow+v_nG_n^\leftarrow\}.
\end{split}                                                     \tag{10}
\]
In both formulas \(u_c\) takes both endpoints \(1/5,2/5\).
No imaginary balancing gauge and no separate-half positivity
assumption occurs.

If \(o\) is right instead of A, replace the outer partial in (9)
by \(K_{\alpha_n,0}(z_n,u_n)\), or in (10) by
\(K_{\alpha_n,1}(z_n,u_n)\). For a nonzero \(b_n\), the minimizing
height-only row is exactly
\[
\begin{array}{c|cc}
 &b_n>0&b_n<0\\ \hline
 (9),\ d=0&1/5&2/5\\
 (10),\ d=1&2/5&1/5 .
\end{array}                                                     \tag{11}
\]
If \(b_n\chi_n=0\), its row is immaterial. One may instead test
both \(u_n\) endpoints as a stronger sufficient condition. A type-three
coefficient interval can be split at zero to use the exact table.

**Proposition 1.** At every actual target configuration in (3), with
exactly one adjacent right incidence, the conservative local
minimum-flow derivative is bounded below by the minimum of (9) or
(10) over the indicated switches and row endpoints, evaluated on
its original shared coefficients and targets. It therefore suffices
to prove that all the displayed functions are nonnegative on any
containing local parameter domains.

**Proof.** With the actual optimizing raw row retained, minimizing
the two switches gives
\[
 \Re G_c+\min\{-b_c\Im G_c,0\}
                    +\min\{-b_n\Im G_n,0\}.                 \tag{12}
\]
The right neighbor has zero height and zero velocity. These are
precisely the remaining contributions in the conservative local
criterion of the
[minimum-level argument](research_mixed_minimum_level_transport.md),
with the own right profile retained in \(b_n\).
At fixed shared variables, the moving-real raw contribution is
concave in its row and hence bounded below by its two endpoint
values. The height-only raw contribution has the monotonicity in
(11). Applying those bounds to each physical raw edge gives
(9)--(12). They do not require raw derivatives to dominate coherent
derivatives; that stronger statement is false.

For simultaneous minima, an affected unselected row height changes
once. Summing conservative local quantities may count a negative
height term more than once and omits positive terms, so it still
bounds the total flow derivative from below. The selected
corrections stay constant by (8) and stationarity of their other
coordinates. This establishes the sufficient implication, not its
unproved sign hypothesis. \(\square\)

For a three-cycle with one right vertex, the two outer right
appearances in (9) or (10) are the same physical vertex but the two
raw edges have separate rows and are both retained. In a two-cycle,
an A vertex has two right incidences when its other vertex is right;
that belongs to the two-adjacent-right case, not to this proposition.
There is no one-cycle with exactly one adjacent right incidence.
Coincident outer variables in longer short cycles may be released
independently to enlarge a parameter domain; no physical incidence
may be deleted.

## 3. Exact containing regions for the outer A target

Fix \(t,y\) and the center/neighbor states and coefficients.
Write \(x=\Re z_o\). The literal outer slow suppression satisfies
\[
 t\le x\le.5,\qquad
 r\le\lambda_o\le m(x,y):=\min\{\rho(x),\rho(y)\}.              \tag{13}
\]
Indeed its other, unspecified neighbor has real coordinate at least
\(t\); only that fourth coordinate has been released. The shared
neighbor \(y\) has not been replaced by an independent cutoff.
After enlarging the outer original height coefficient to its full
typed interval, the following compact regions contain every target:
\[
\begin{split}
 \mathcal O_3(t,y)
   &=\{x+ih:t\le x\le.5,\
        -.03R(x)m(x,y)\le h\le .02R(x)m(x,y)\},\\
 \mathcal O_{4,U}(t,y)
   &=\{x+ih:t\le x\le.5,\
        -.057R(x)m(x,y)\le h\le-.02R(x)r\},\\
 \mathcal O_{4,S}
   &=\{x+iHR(x):t\le x\le.5\}.
\end{split}                                                     \tag{14}
\]
The two-dimensional regions have positive width for \(x<.5\);
both end at \(.5\).

For clarity, the containing source domains have already been proved.
At \(x\le.22\), (14) lies in the type-three triangle or enlarged
type-four cap of the
[early-selected source theorem](research_mixed_early_selected_source_cap.md).
At \(.22\le x\le.45\) it lies in the typed plateau rectangles.
At \(.45\le x\le.5\),
\(R(x)\le20(.5-x)\), so it lies in the right triangles of the
[complete interface theorem](research_mixed_left_right_interface_source.md).
The full
[right-square packet](research_mixed_unselected_right_taper_products.md),
Theorem 1, covers the plateau/right products. The early-cap,
interface and right-square products agree on overlaps by uniqueness
of the original zero-lift root. In particular, they give holomorphy
on a neighborhood of every closed outer region in (14), for every
fixed admitted neighbor target, including the real endpoint \(.5\).
No new complex packet is inferred merely from root uniqueness.

Put \(b=\min\{y,.22\}\). The boundaries in (14) are explicit:

* \(\partial\mathcal O_3\) consists of its left vertical segment
  at \(x=t\), and its lower and upper curves on each of
  \([t,b]\), \([b,.45]\), \([.45,.5]\). There are seven arcs.
* \(\partial\mathcal O_{4,U}\) has its left vertical segment,
  three lower arcs on those intervals, and two upper arcs on
  \([t,.45]\), \([.45,.5]\). There are six arcs.
* \(\mathcal O_{4,S}\) has the two curves on
  \([t,.45]\), \([.45,.5]\).

Each nonvertical arc is parametrized by
\[
                 x=a+(b'-a)v,\qquad 0\le v\le1,              \tag{15}
\]
using its listed endpoints \(a,b'\) and the corresponding height
formula in (14). The left vertical arc uses affine height
interpolation. Zero-length arcs at \(y=t\) or \(t=.22\) may be
retained as points. On \([t,b]\), \(m=\rho(x)\); on the next
two intervals \(m=\rho(b)\). Thus all height curves are linear,
constant or quadratic. Splitting at \(y=.22\) removes the only
minimum in these finite parametrizations.

**Proposition 2.** For fixed shared center/neighbor variables and
switches, it suffices to test (9) or (10) on the outer curves just
listed. If \(\chi_n b_n=0\), the outer target and its type disappear
from the inequality.

**Proof.** The only outer dependence is respectively
\[
 \Re\{v_n\partial_2\phi_{\alpha_o\alpha_n}(z_o,z_n)\},
 \qquad
 \Re\{v_n\partial_1\phi_{\alpha_n\alpha_o}(z_n,z_o)\}.          \tag{16}
\]
These are real parts of holomorphic functions of \(z_o\).
The minimum principle therefore places their minimum on the
boundary of each two-dimensional region (14). Convexity of those
regions is unnecessary. The selected region is already a curve,
so all of it is retained. The other terms of (9)--(10) are constant
in \(z_o\). This proves the proposition. \(\square\)

There is an optional simpler enlargement. The outer selection
correction has zero derivative, so the same allocated type-four
function in (16) applies in both outer states. One may replace their
union by
\[
 \widehat{\mathcal O}_4(t,y)=
 \{x+ih:t\le x\le.5,\
              -.057R(x)m(x,y)\le h\le HR(x)\}.                \tag{17}
\]
It remains inside the already proved source union. Its boundary
has six arcs: one left vertical, three lower, and two upper arcs.
This gives seven type-three and six type-four outer arcs instead of
seven, six and two separate-state arcs. Equation (17) is an analytic
enlargement for (16); it does not assert that an unselected physical
type-four contour has positive height or the same Fourier rate
there. Positivity on the enlarged boundary would be sufficient,
but has not been proved.

## 4. What a complete local certificate would have to check

Choose either orientation, the center and neighbor from
\(\{U_3,U_4,S_4\}\), their permitted switches, the two center row
endpoints, and an outer A state/arc or an outer R edge. The right
vertex types need no additional marginal functions by (7).
Every outer-A family is a function of at most
\[
                 (t,\ y,\ c_c,\ c_n,\ v),                   \tag{18}
\]
where selected states remove their corresponding coefficient.
The domains of \(t,y\) are the triangle
\(.12\le t\le.22,\ t\le y\le.5\); the coefficient intervals are
(4), and \(v\in[0,1]\) is the explicit boundary parameter (15).
The pieces \(y\le.22\), \(.22\le y\le.45\), and
\(.45\le y\le.5\) retain every cutoff and right-profile formula.
All shared occurrences of these variables must use the same values.
If \(\chi_n=0\), the outer disappears and there are at most four
parameters. If the neighbor is selected, it also has no height
coefficient, leaving at most three. For an outer R edge, (11)
likewise leaves at most four continuous parameters.

The
[outward all-four face check](../repro/diagnostics/2026-11-05-right-minimum-four-face/README.md)
proves \(D^\rightarrow>1/50\) on one of these outer-R faces:
both A reals equal \(.22\), both A states are \(U_4\), and their
original height coefficients range independently over \(C_4\).
Its saved higher-precision replay checks the same fifteen cells.
Compact continuity gives an unquantified one-sided neighborhood of
that face with the targets and velocities distinguished as in (5)--(6).
It supplies no bound on the remaining families in (18).

To complete one-adjacent-right minimum transport, one must still
prove the whole functions (9)--(10) nonnegative throughout the
listed domains, or replace them by another valid sufficient
inequality. No monotonicity in \(t\) or \(y\), and no positivity
of the old separately gauged halves, is assumed here. A center
with no adjacent right vertex but a right vertex at distance two
is a separate local class. Purely coherent halves with a neighbor
above \(.45\) also retain a nonzero unselected coefficient
\(cR(y)\), which can be above \(-.02\); the old plateau-height
checks cannot be imported for them without a new domain argument.
Consequently this reduction does not yet imply a whole-period
asymptotic or an enlarged knot-family theorem.
