# Factorial atoms and exact current supports for fixed short cores

Research note, 3 November 2026.

There is an exact contour construction for every fixed original
circle-tree source, but positive gluing at one configuration is not a
global current estimate. This note separates the parts that extend
uniformly from the adjacent \((-3,-3)\) calculation. It proves a finite
facet rule for all mixed currents and a quantitative horizontal
Hessian criterion directly for the original Newton factors. Neither
criterion depends on a bound for the number of crossings or vertices.
The constants and the number of faces may depend on the fixed source.

The resulting statements are source identities and analytic estimates,
not a new general partial-filling asymptotic. In particular, no
nonzero cycle coefficient is inferred just from a positive endpoint.

## 1. What can be compiled without changing the source

Use the original Newton basis, crossing matrix, turn and trace from
[arbitrary-power compilation](research_arbitrary_power_source_compilation.md).
The main meridian is at its original complete value, so the full
pair relation is \(P_N=0\). Free auxiliary boundary variables and
their normal derivatives remain present. The additional covariant
edge weights of a moving main meridian are not silently identified
with this source.
Put \(D=N-1\) and \(q=e^{\pi i/N}\). A signed unit crossing is

\[
 (M_\sigma)_{kj}=\kappa^\sigma(-1)^k
       q^{\sigma k(j+1)}\frac{S_k}{S_jS_{k-j}},
 \qquad 0\le j\le k\le D,\quad \sigma=\pm1.                 \tag{1}
\]

Every fixed power is a finite chain of these actual matrices. A
binary product uses the exact tensor

\[
 \mu_{ijr}=
 \frac{S_{i+j}S_r}
 {S_iS_jS_{r-i}S_{r-j}S_{i+j-r}},
 \qquad \max(i,j)\le r\le i+j\le D,                          \tag{2}
\]

and a turn replaces a label by \(D-j\). The original closure
selects the coefficient of \(e_D\). Thus expanding an actual
finite expression gives a finite sum over integral affine
inequalities. The number of labels and inequalities is independent
of \(N\). In a rooted expression one keeps each unfixed wire
label as an integer coordinate; turns are integral affine
substitutions, not new congruences. A final prescribed output label
is fixed rather than summed. This is an ordinary primitive lattice.

At a free boundary one keeps the entire ordinary polynomial

\[
 e_j(w)=S_j^{-2}\prod_{a=0}^{j-1}(c_a-w),                     \tag{3}
\]

or the product of these polynomials when several wires meet that
unfilled variable. No reduction is made there. Consequently (1)--(3)
retain the original normal derivatives at repeated roots and every
ordinary free-boundary derivative. All \(\kappa\) factors,
quadratic phases and the \(-1\) in \(D=N-1\) remain explicit.
This is just the coefficient-level proof of the existing compiler;
it requires no geometric choices.

The exact factorial expression need not extend holomorphically to
the whole bounding box. The pole of (2) at \(N=3,(i,j,r)=(2,2,0)\)
is already proved in
[the divisor criterion](research_factorial_rectangle_divisor_criterion.md).
Nor does a high Newton leaf have the same single regular factorial
phase as a low leaf on the whole boundary period. These are actual
restrictions on a global factorial chart.

However, on any retained compact polytope on which every factorial
argument has fixed normalized slack from zero and one, the canonical
factorial interpolation is holomorphic on every fixed product of
imaginary intervals. The \(O(N^{-1})\) offsets and half-grid cell
boundaries preserve that slack at sufficiently large levels. The
cell construction below therefore applies to that original retained
sum, in any dimension. Removing its complementary real states is
a separate source estimate.

## 2. A finite facet rule for all mixed currents

Let \(P_N\) be a finite integral polytope with indicator

\[
 \chi_N(\ell)=\prod_{f=1}^F
       {\bf1}_{a_f\cdot\ell\ge b_{f,N}},
 \qquad a_f\in\mathbb Z^d\setminus\{0\}.                    \tag{4}
\]

The normalized polytopes converge to a fixed compact polytope

\[
 P=\{r:a_f\cdot r\ge\beta_f\},\qquad
 b_{f,N}=N\beta_f+O(1).                                     \tag{5}
\]

The normals, their supports, and the number of inequalities are
fixed. Redundant inequalities cause no difficulty.

For \(V\subseteq\{1,\ldots,d\}\) define the original mixed
difference

\[
 \Delta_V\chi_N(\ell)=
 \sum_{\delta\in\{0,1\}^{V}}(-1)^{|\delta|}
                             \chi_N(\ell+\delta).           \tag{6}
\]

**Theorem 1 (facet-cover rule).** If (6) is nonzero, there is a
set \(\mathcal F\) of facets such that:

1. each selected facet indicator changes on the cube
   \(\ell+\{0,1\}^{V}\);
2. \(V\subseteq\bigcup_{f\in\mathcal F}\operatorname{supp}a_f\);
3. \(\ell/N\) is within \(O(N^{-1})\) of \(P\) and of every
   selected supporting hyperplane.

In particular, its limiting support lies on the corresponding
nonempty face intersection of \(P\). The constants depend only
on the finite list of normals.

*Proof.* Take \(\mathcal F\) to be all indicators that change on
this cube. If some \(i\in V\) lies in none of their supports,
each changing indicator is independent of \(\delta_i\). Every
other indicator is constant on the cube. The entire product is
therefore independent of \(\delta_i\), and its two terms cancel
in (6), a contradiction. This proves the cover property.

A changing indicator satisfies

\[
 |a_f\cdot\ell-b_{f,N}|
               \le\sum_{i\in V}|a_{fi}|.                    \tag{7}
\]

Also, a nonzero alternating sum has at least one vertex at which
\(\chi_N=1\). That vertex is a bounded distance from \(\ell\).
These facts prove the normalized distance assertions. Compactness
then proves the assertion about limiting face intersections.
The statement only concerns fixed nonempty strata that occur for
arbitrarily large \(N\); a finite list of empty limiting
intersections contributes no further asymptotic stratum. \(\square\)

Use the exact one-cell kernels and orientations of
[the retained-polytope contour](research_three_crossing_retained_polytope_contour.md),
now in \(d\) coordinates. Fix positive heights \(H_i\) and
principal signs \(\epsilon_i\). The same tensor identity gives

\[
 \sum_\ell\chi_N(\ell)f_N(\ell/N)
 =\sum_{V,\ell}\Delta_V\chi_N(\ell)
   \sum_{s\in\{\pm1\}^{V^c}}
       \Bigl(\prod_{i\in V}\mathsf V_i^{\ell_i}\Bigr)
       \Bigl(\prod_{i\notin V}\mathsf H_{i,s_i}^{\ell_i}\Bigr)f_N.
                                                               \tag{8}
\]

This follows by exactly the same finite telescoping in each
coordinate. All mixed coefficients, not just their supports, are
still the integers (6). In particular, several finite-difference
directions can live on one slanted facet. They need not be supported
in higher codimension.

Suppose imaginary convexity is available on the retained tube.
After including the exact kernel penalty, vertical coordinates can
be reduced to heights \(-H_i,0,H_i\). A horizontal coordinate
always has nonzero height. Theorem 1 therefore gives the following
finite list sufficient for every current:

\[
 \boxed{\quad
  r\in F_{\mathcal F}:=P\cap
       \bigcap_{f\in\mathcal F}\{a_f\cdot r=\beta_f\},
  \qquad
  \{i:t_i=0\}\subseteq
       \bigcup_{f\in\mathcal F}\operatorname{supp}a_f,
  \quad t_i\in\{-H_i,0,H_i\}.\quad}                          \tag{9}
\]

Only nonempty face intersections are needed. This is a safe list;
it may contain states whose exact mixed difference vanishes. That
overcount can be removed by (6), but cannot invalidate an upper
bound. The exact penalty is

\[
                   2\pi\sum_i(-\epsilon_i t_i)_+.             \tag{10}
\]

For the diagonal constraint \(x-z\ge p\), its normal touches
only \(x,z\). Consequently a current on that face alone must
keep \(y\) at a nonzero horizontal height. Intersecting it
with a \(y\) cutoff permits all three heights in all three
coordinates. This recovers both the old diagonal-face rule and
the new 27-state edge in
[the intermediate-period proof](research_three_crossing_middle_period_current_bounds.md).
It also explains why the two sheets of \(\Delta_x\Delta_z\)
must be retained rather than regarded as isolated corners.

The principal horizontal in (8) has coefficient exactly \(+1\)
and kernel product \(1+O(e^{-cN})\). This holds for every
fixed source, before estimating any other piece. It is the exact
local coefficient needed once the other pieces have strict gaps;
it does not itself exclude their cancellation with it.

## 3. The original horizontal Hessian is an atom incidence form

Write

\[
 J(x)=\int_0^x\log(2\sin\pi t)\,dt,
 \qquad
 \mathcal V(a,b,c)=-J(a)-J(b)-J(c),\quad a+b+c=1.              \tag{11}
\]

A unit-crossing factorial phase is exactly

\[
 J(x)-J(y)-J(x-y)=\mathcal V(1-x,y,x-y).                       \tag{12}
\]

Its sign changes only its specified imaginary quadratic phase.
For a Newton product put

\[
 p=z-x,\quad q_0=z-y,\quad r=x+y-z,\quad w=1-x-y.
\]

The identities proved in the original Newton variational theorem are

\[
 \begin{split}
 g(a)&=2\mathcal V(a,1/2-a,1/2),\\
 m(x,y,z)&=\mathcal V(y,x,w)
   +\mathcal V(p,q_0,2r+w)
   +\mathcal V(p+q_0,r,r+w).
 \end{split}                                                  \tag{13}
\]

These are exact holomorphic identities on a common regular branch,
not only identities of real values. Hence the complete low-boundary
phase of a compiled source has the form

\[
 \Phi(v)=\sum_{\tau}c_\tau\mathcal V(a_\tau(v))
                               +i Q(v),\qquad c_\tau>0,        \tag{14}
\]

with integral affine angle maps and a real quadratic polynomial
\(Q\). All original charges and signed crossing phases are in
\(Q\); none is replaced by an absolute value. Factors with
fixed crossing sign use the specified interpolation
\((-1)^k=e^{\sigma i\pi k}\), so their imaginary leading term is
\(\sigma i\pi(1/2+x+xy)\), as in
[the original crossing interpolation](research_corner_newton_source_transport.md).
Changing this lift requires transferring the corresponding lattice
mode as well; it does not justify retaining the old current penalties.
Factors with
fixed zero arguments, for example the first crossing applied to
\(e_0\), must first be evaluated exactly. They are not strict
atoms to which the following estimate is applied.

For a real variation \(v\), the exact horizontal form is

\[
 -\Re\Phi''[v,v]
    =\pi\sum_\tau c_\tau\sum_{a\in\tau}
              \Re\cot(\pi a)\,(d a[v])^2.                    \tag{15}
\]

Thus the relevant object is a constrained cotangent form. It is
not generally a graph Laplacian with nonnegative individual edge
weights: an angle with real part greater than \(1/2\) has a
negative cotangent weight. The angle-sum constraints matter.

**Theorem 2 (uniform complex atom strip).** Let
\(0<\delta\le1/3\). Suppose every atom in (14) has

\[
 \delta\le\Re a\le1-2\delta,
 \qquad |\Im a|\le\eta_\delta,
 \qquad
 \eta_\delta=\frac1\pi\operatorname{arsinh}
                    \frac{\sin^2(\pi\delta)}{\sqrt{24}}.      \tag{16}
\]

Let \(L_\tau\) take a primitive variation to the variations
of the first two angles of atom \(\tau\). Then

\[
 -\Re\Phi''\ \succeq\
 \frac{\pi\sin(\pi\delta)}8
                  \sum_\tau c_\tau L_\tau^T L_\tau.           \tag{17}
\]

In particular, it is positive definite whenever the combined
angle-incidence map is injective. The estimate is independent of
the number of atoms and their signs of crossing. It holds on every
convex retained region satisfying (16).

*Proof.* At real angles \(a+b+c=1\), the two-coordinate
cotangent matrix is

\[
 K_0=\begin{pmatrix}
 \cot\pi a+\cot\pi c&\cot\pi c\\
 \cot\pi c&\cot\pi b+\cot\pi c
 \end{pmatrix}.                                               \tag{18}
\]

It is positive definite and has determinant one. Each cotangent
has absolute value at most \(\cot(\pi\delta)\), so
\(\lambda_{\max}(K_0)\le4\cot(\pi\delta)\). Therefore

\[
                   K_0\succeq\frac{\sin(\pi\delta)}4 I.      \tag{19}
\]

For \(s\in[\delta,1-2\delta]\) and real \(t\),

\[
 \Re\cot\pi(s+it)
       =\frac{\sin(2\pi s)}{\cosh(2\pi t)-\cos(2\pi s)}.
\]

Consequently

\[
 |\Re\cot\pi(s+it)-\cot\pi s|
       \le\frac{\sinh^2(\pi t)}{\sin^3(\pi\delta)}.          \tag{20}
\]

The three angle rows in two-coordinate form are
\((1,0),(0,1),(-1,-1)\); the norm of the sum of their outer
products is three. By (16), the perturbation of (18) therefore
has norm at most \(\sin(\pi\delta)/8\). Subtracting this
from (19), multiplying by \(\pi\), and summing the exact
incidence forms proves (17). The imaginary quadratic has zero
horizontal real Hessian, at every fixed height. \(\square\)

This supplies a direct test in the original factorial variables.
For regular primitive expressions its incidence injectivity is
elementary: a crossing atom detects both its wire variations;
the first product atom detects its two inputs and the second then
detects its output; a leaf detects its leaf variation. If every
unfixed coordinate occurs in one of those regular factors, their
common kernel is zero. If a source has extra constraints or fixed
degenerate factors, one checks injectivity after imposing exactly
those constraints. Acyclicity is not a substitute for that check,
and cycles do not invalidate the form estimate.

## 4. An exact limitation of the proposed global Laplacian shortcut

Even the requirement that every individual cotangent weight be
nonnegative is too restrictive for crossing chains. Two consecutive
strict crossings with labels \(0<z<y<x<1\) have angle triples
\((1-x,y,x-y)\) and \((1-y,z,y-z)\). If all six real angles are
at most \(1/2\), then both \(y\le1/2\) and \(1-y\le1/2\), hence
\(y=1/2\). There is no open full-dimensional chamber of this type.
The constrained positive form, rather than positivity of each
cotangent separately, is essential already for two crossing blocks.

All real tetrahedral angle triples are strictly concave. This does
not make their entire factorial strip horizontally concave.
Consider the single original crossing atom with angles

\[
 (a,b,c)=\left(\frac34,\frac18+iH,\frac18-iH\right),
 \qquad H=\frac{\log2}{2\pi}.                                \tag{21}
\]

All real parts lie strictly between zero and one, the sum is one,
and every canonical factorial remains on its original regular
strip. On the allowed real variation \((-2,1,1)\), its
cotangent energy is

\[
 \sum\Re\cot(\pi a)\,(d a)^2
 =-4+\frac{2}{(5\sqrt2/4)-1}<0.                              \tag{22}
\]

The inequality is equivalent to \(10\sqrt2>12\). This is an
exact failure of horizontal accretivity within a single
factorial chart. It is not a counterexample to positive original
gluing at a selected geometric point; that is a further condition
on the point. It shows why that condition must be verified along
the proposed contour rather than inferred for every height from
the real angle simplex.

There is an independent original-source obstruction to dropping
the current estimates. The already proved adjacent source has
positive geometric gluing, but its radial homotopy contains the
real face point

\[
 (x,y,z)=(1/2,1/4,1/4),\qquad
             \Re\Xi=\frac{11G}{2\pi}>\frac85,                \tag{23}
\]

whereas its selected action is less than \(1.54\). This exact
comparison is recorded in the retained-polytope note. Thus even
for a path with the required positive geometry, independent
absolute bounds on all radial faces cannot prove the needed gap.
The successful cellwise proof uses the nonzero tangential heights
forced by (9), followed by actual source bounds for the other
faces. Positive local geometry alone supplies neither step.

## 5. What this gives for the next connected core

For a fixed original short core there is now a finite, source-preserving
procedure:

1. Compile its actual crossings, turns and products, keeping the
   ordinary boundary polynomials and every original offset.
2. Choose strict retained factorial chambers; prove the removed
   real bands by estimates for the original source.
3. Verify the atom-incidence inequality (17), or a sharper exact
   Hessian inequality, on each required fixed-height chamber.
4. Generate every face/height case by (9), retaining its exact
   finite-difference coefficient from (6). A concave face is
   bounded by tangent planes at its vertices, with penalty (10).

There is no additional unknown local intersection number for the
principal horizontal: (8) fixes its coefficient to \(+1\).
What remains to prove for a new core is that this principal piece
contains its original marked stationary point, with nonzero local
density, and that every generated nonprincipal piece and removed
real band has a strict gap. The primitive currents, parity and
normal data have not been exchanged for a different source.

The atom theorem gives an explicit broad class of globally
concave retained chambers, and the facet theorem gives their
complete finite current list. They do not show that every
hyperbolic short core admits such chambers or satisfies those
current inequalities. The existing zero-power subtree theorem
already proves the nonoscillatory case in arbitrary size; the
new adjacent \((-3,-3)\) proof proves a further oscillatory
case by additional global bounds. No larger volume-conjecture
coverage is asserted merely from the compilation above.
