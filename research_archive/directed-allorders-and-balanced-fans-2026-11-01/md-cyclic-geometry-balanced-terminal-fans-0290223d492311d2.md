# Two-sided terminal fans and complete-radius balance

Private working theorem, 1 November 2026. The conclusion concerns an
actual augmented diagram and its one marked complete packing. It is not
a claim that arbitrary cyclic contractions reduce to the scalar kernels
of a tangle-operation tree.

## 1. Input and the local geometric operation

Start with a connected augmented diagram whose labeled white
triangulation is a simple triangulated sphere and whose matching pairs
are the original crossing-circle ports. Retain the original marked MAIN
edge and its two protected zero curvatures. Assume the supplied positive
complete packing is the original geometric certificate. An original port
has ordered weights

\[
(x,b,c,y),\qquad A=x+y>0,\qquad P=xy,\qquad
\delta=P/A^2\in[0,1/4].                                      \tag{1}
\]

Its matching edge is \(xy\), and its two shaded triangles are
\((x,b,y)\) and \((x,c,y)\). The letters in (1) denote circle curvatures,
not independent choices of radii for different source factors.

Stellarly subdivide the first triangle by its positive interstice circle

\[
b_1=A+b+2\sqrt{Ab+P}.                                      \tag{2}
\]

Retain \(xy\) as the old matching edge and match the other two new
triangles along \(bb_1\). Thus the two resulting ports have unordered
outer/middle pairs

\[
\begin{array}{c|c|c}
 &\text{outer pair}&\text{middle pair}\\ \hline
\text{retained port}&(x,y)&(b_1,c)\\
\text{new port}&(b,b_1)&(x,y).
\end{array}                                                   \tag{3}
\]

Their oriented four-leg frames are inherited from the local disk
insertion, rather than chosen afterwards from this table.

This is a literal terminal-tangle insertion. In the endpoint convention
of `actual_all_circle_octahedral_decomposition.md`, take the unturned
old box \(P_v=T^{-1}h_v\), with exposed tuple
\((v_3,v_0,v_1,v_2)\). If \(x_1,x_2\) are its two current output
neighbors, inserting \(h_w\) immediately after \(P_v\) replaces

\[
\begin{array}{c|c}
v_1-x_1&v_1-w_1,\quad w_2-x_1\\
v_2-x_2&v_2-w_0,\quad w_3-x_2.
\end{array}                                                   \tag{4}
\]

The endpoint calculation uses only this framed product collar. The
outside arcs may belong to an arbitrary fixed diagram; they need not
come from a tree. The left insertion replaces \(v_3-x_3\) by \(v_3-w_3,w_0-x_3\), and \(v_0-x_0\) by \(v_0-w_2,w_1-x_0\). It gives the second side without changing the inherited frame.
The octahedron in that reference attaches to precisely the shaded face
being subdivided. Its three other shaded faces give (3), with the old
and new white boundary cycles fixed by (4).

All old circles remain fixed. The new disk lies in the chosen
interstice, and the positive Descartes solution is (2). The supporting
planes and opposite ideal vertices are those of the regular octahedron
attached across the old ideal triangle; this is also the literal
construction in `actual_smoothing_fixed_radius_gap.md`, Section 5.
Consequently the same complete labeled certificate extends to the new
diagram. This attaches one regular octahedron in each projection copy,
so the augmented volume increases by \(2v_{\mathrm{oct}}\) per insertion.
This geometric statement uses the face attachment, not just its volume.

The protected zeros remain zero. Their marked MAIN edge is a boundary
edge of every subdivision containing it and is not removed. The
formulas include a zero middle and one zero outer curvature. In the
case with two protected lines, (2) is the corresponding positive
interstice disk between those lines. Since \(A>0\), no three-zero
triangle occurs.

## 2. Exact fan recurrence and even counts

Repeat the operation only at the retained port, on the same side. Put
\(t_j=\sqrt{Ab_j+P}\). Direct substitution into (2) gives

\[
t_{j+1}=t_j+A,\qquad
b_j=b+2j\sqrt{Ab+P}+j^2A.                                  \tag{5}
\]

The positive square root is essential here. Normalize

\[
u=\sqrt{b/A+\delta},\qquad v=\sqrt{c/A+\delta}.
\]

After \(j\) insertions on the first side and \(k\) on the second,

\[
b_j=A[(u+j)^2-\delta],\qquad
c_k=A[(v+k)^2-\delta].                                    \tag{6}
\]

There are even nonnegative integers \(j,k\) with

\[
U=u+j\ge4,\qquad V=v+k\ge4,\qquad |U-V|\le1.              \tag{7}
\]

Indeed choose an integer \(m\) nearest \(-(u-v)/2\). Then
\(|u-v+2m|\le1\). Set \(j=2(L+m)\), \(k=2L\), and take the
integer \(L\) large enough to make both counts nonnegative and both
quantities in (7) at least four. Adding the same even count to both
sides preserves the difference condition.

Give each inserted terminal an odd crossing power. Its turned
four-terminal pairing is the crossing pairing, so an even stack has
the identity pairing and creates no internal component. Hence these
two even fans preserve the original box's four-endpoint pairing. In
particular a specified knot parity pattern of the core remains a knot
pattern. The new fillings may have independently chosen sufficiently
large odd positive or negative powers. This preserves endpoint
connectivity, not the isotopy type of the filled core knot.

## 3. An exact integral for the source-normalized triangle action

Let \(F(x,b,y)\) be the complete triangle action with the original
determinant, beta and half-forced-product normalization. Its exact
entropy definition is

\[
F(x,b,y)=\max_{\alpha_x+\alpha_b+\alpha_y=1/2}
\left\{\sum_j f(\alpha_j)+\alpha_x\log x+
\alpha_b\log b+\alpha_y\log y\right\},                     \tag{8}
\]

where \(f'(t)=\log\cot(\pi t)\), \(f(0)=f(1/2)=0\), and zero
weights force zero allocation. The complete stationary middle load is

\[
\frac{\partial F}{\partial\log b}
=\frac1\pi\arctan\frac{b}{\sqrt{Ab+P}}.                   \tag{9}
\]

These are the calibrated identities in
`actual_triangle_entropy_algebraic_balance.md` and
`actual_cross_cofactor_marked_action.md`; no additive entropy constant
is available to change.

Homogeneity of (8) gives
\(F(x,b,y)-\tfrac12\log b=F(x/b,1,y/b)\to0\) as \(b\to\infty\).
For completeness, the vertex allocation to the middle has value zero.
Any maximizing allocations along a sequence with the two outer weights
tending to zero must have their outer allocations tending to zero:
otherwise the bounded continuous entropy cannot offset the negative
log-weight term. Their entropy then tends to zero, proving the upper
limit as well. Integrating (9) from infinity therefore gives exactly

\[
F(x,b,y)=\tfrac12\log b+R(b),\qquad
R(b)=\frac1\pi\int_b^\infty
\arctan\frac{\sqrt{At+P}}t\,\frac{dt}{t}>0.                \tag{10}
\]

The integral converges by its \(O(t^{-3/2})\) integrand. It is also
valid when one outer curvature is zero.

Using \(P\ge0\), monotonicity of arctangent, and
\(\arctan z\ge z-z^3/3\) for \(z\ge0\), we obtain

\[
R(b)\ge \frac2\pi\sqrt{A/b}
-\frac2{9\pi}(A/b)^{3/2}.                                \tag{11}
\]

## 4. Strict balance at the retained port

Assume (7), and exchange the two sides if necessary so that
\(U\ge V\). Put \(b'=A(U^2-\delta)\),
\(c'=A(V^2-\delta)\). They are positive. Since
\(w\mapsto 2w-2w^3/9\) is increasing on the range in use,
(11) and \(\delta\le1/4\), \(U,V\ge4\), give

\[
R(b')+R(c')\ge
\frac2\pi\left(\frac1U+\frac1V\right)
-\frac2{9\pi}\left(\frac1{U^3}+\frac1{V^3}\right)
\ge\frac{643}{180\pi V}.                                 \tag{12}
\]

For the last inequality use \(U\le V+1\le5V/4\) and
\(V^{-3}\le(16V)^{-1}\). On the other hand,

\[
\frac12\log(b'/c')
=\int_V^U\frac{t}{t^2-\delta}\,dt
\le\frac{64}{63V}.                                      \tag{13}
\]

The rational bound \(\pi<22/7\) proves

\[
\frac{643}{180\pi}-\frac{64}{63}
>\frac{3347}{27720}>0.                                  \tag{14}
\]

It follows from (10)--(14) that the original retained port has

\[
F(x,b',y)+F(x,c',y)-\max(\log b',\log c')
>\frac{3347}{27720\min(U,V)}>0.                          \tag{15}
\]

Thus it satisfies the true complete-radius balance condition, including
the source's exact absolute normalization. The simpler algebraic
sufficient test need not hold here; using it instead of (10) would lose
the construction.

## 5. Every added port already balances

At an insertion with current middle \(b\), the new port has outer sum
\(A'=b+b_1\) and middle pair \((x,y)\). From (2),

\[
A'\ge A=x+y\ge\max(x,y).
\]

Consequently

\[
(A'+x)(A'+y)\ge\max(x^2,y^2).                            \tag{16}
\]

The source-normalized entropy inequality
\(F(a,t,d)\ge\tfrac12\log(a+t+d)\), strict when two weights are
positive, shows that (16) implies the required strict balance for every
positive middle. A zero middle needs no logarithm; its overloaded
one-sided finite sector is absent. Since \(A'>0\), this covers all
protected-zero cases too.

Later fan steps subdivide only the retained port's triangle. No
previously added port changes again. Performing the construction at
different original ports likewise preserves their already fixed
curvatures and all previously settled ports. There are finitely many
original ports. Hence the procedure terminates with one actual marked
complete packing in which every port balances strictly.

The construction therefore proves a geometric realization theorem:
every fixed certified simple-white core has a finite two-sided terminal
decoration, with even fan sizes, preserving its knot endpoint pairing
and original marked edge, whose entire complete packing satisfies the
true radius-balance inequalities. The sizes depend on the original
packing; no uniform count or bridge-width assertion is made.

## 6. What happens to the shared magnetic-flow graph

This refinement does not turn a cyclic source into a scalar tree source.
In the cubic dual, the old shaded vertex \((x,b,y)\), whose matching
edge is \(xy\), is replaced along its nonmatching physical cycle by

\[
(x,b,w)\;--\;(x,y,w)\;--\;(y,b,w).
\tag{17}
\]

The old matching edge remains incident to the middle vertex. The new
matching edge \(bw\) joins the first and last vertices. Thus, after
collapsing each physical W/\(\pi\) cycle as in
`actual_matching_graph_shared_cycle_fourier_compiler.md`, the new edge
is a loop at the old cycle vertex. The existing cycle incidences are
unchanged, and the integral flow lattice acquires one independent loop
coordinate. Any cups/caps used to draw the local Morse collar remain
bivalent and do not change this topological statement.

In particular this is not a bridge attachment. Pair-local decorations
do not erase the original cyclic magnetic channels. The potential
advantage of this particular construction is its shared-radius bound,
not a claim of scalar-kernel factorization.

## 7. Exact source and the remaining analytic interface

The final matched sphere has an actual general Morse realization and
the exact original coefficient source of
`research_matched_sphere_morse_source.md`. In that theorem the whole
source is the product of the original four-leg polynomials, extracted
at the original ordinary targets, with the two protected variables set
to zero; all actual turns, cups/caps, half-index phases and reduced mark
are retained. The finite full-Hermite filling functional is also the
original one. There is therefore a genuine source for the decorated
diagram, not merely an entropy model.

The currently stated complete-radius filling theorem and its local
packet inputs begin with a marked flat plat. The terminal insertion can
introduce intermediate cups/caps. This note does not silently replace
that hypothesis by a general Morse presentation, nor claim that a
platification preserves every designated disk and source frame.
To conclude the full long-filling volume theorem for these decorated
cores, one must verify that the exact Morse coefficient and primitive
geometric dictionary supply every hypothesis of the existing packet,
global CROSS and whole-period theorems. The local one-sided estimates
and the strict balance in (15)--(16) already use only this shared
coefficient and its actual complete radii. A proof of the remaining
interface would yield the full invariant conclusion for independently
long fixed fillings of the decorated diagram, with its own original
knot complement as the target.

No volume statement for the undecorated core, no short-filling theorem,
and no claim that increasing valence alone forces balance is contained
in the construction. In fact a one-sided fan sends one middle curvature
to infinity with the other fixed and eventually violates balance.
