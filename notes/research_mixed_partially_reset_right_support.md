# A weak full-source bound for a partially reset plateau leg beside the right half

Research proof, 5 November 2026. The target is the original finite
block with one real right-half argument and one plateau argument.
The plateau height may be any fraction of its prescribed height.
The conclusion is a positive defect ceiling, sufficient for a
separate low-incidence budget; it is not a negative block gap.

## 1. Original source and target heights

Retain the full finite kernel, actual Fourier polynomial, original
normalization and allocated modulus of
[the right-half block theorem](research_mixed_right_half_block_bound.md),
equations (1)--(5). At an actual critical pair \((a,b)\), let
\(\Gamma\) be its full complex tangent, including both height terms.
The ordered type indicators are \((\eta,\epsilon)\).

One target argument is \(x\in[1/2,1]\), with height zero. The other
is \(y+ih\), with
\[
 P=[11/50,9/20],\qquad y\in P,\qquad
 h=t h_0,\quad 0\le t\le1,
 \quad
 h_0=\begin{cases}
 \text{its actual critical height},&\text{unselected},\\
 7/500,&\text{selected type four}.
 \end{cases}
 \tag{1}
\]
Every permitted selection at the real right argument is allowed.
Its selected frequency has modulus one, and its true Fourier weight
has zero upper exponential rate. At the moving argument both Fourier
alternatives and its selected frequency remain literal.

**Theorem 1.** For each fixed cyclic word, uniformly over (1), the
original allocated finite block satisfies
\[
 B_N\le C N^A\exp N\{\Re\Gamma+1/100\}
 \tag{2}
\]
at all sufficiently large integer levels, with both parities retained.
The two orientations are included. Reference legs are the actual
cyclic legs, not arbitrary independent points of their enclosing
rectangles. No conditional phase packet is asserted at a right-half
argument.

## 2. The missing zero-height source profiles

The original right-angle reduction keeps the other angle \(y\) fixed
when \(y\ge.13\). It moves low row indices to \(u=1/5\) when
needed to absorb an additional right-angle candidate. Thus on \(P\)
it reduces the right angle to \(x=1/2\) or \(x=1\), without moving
\(y\) outside \(P\). The separate small-angle move to \(y=.13\)
is not used. At \(x=1/2\), the complete high-row reduction on
\(y\in[.13,.5]\) bounds the upper rows by \(u=1/2\) or \(u=1\),
at the same angle and height. Consequently the new source check
only needs
\[
 (u,y)\in[1/5,1/2]\times P,
 \qquad\text{and}\qquad u=1,\ y\in P.
 \tag{3}
\]
These reductions are the full original-row inequalities in
[right-half source reduction](research_mixed_right_half_source_reduction.md)
and [high-row endpoint reduction](research_mixed_high_row_endpoint_reduction.md).
They retain every row and the actual tangent slopes
\(-1/5<\Re\Gamma_j<1/4\).

Let \(\beta\) be the type-four indicator of the moving argument.
At its new height zero, \(J(y)=\Re g(y)<0\) on \(P\), so the
larger true Fourier alternative is \(-J(y)\). The full core exponent
is exactly
\[
 E_{\epsilon\beta}(u,y)
   =J(1/2+u)+J(u+y)-(2+\epsilon)J(u)
                         -(1+\beta/2)J(y).
 \tag{4}
\]
The original first-argument chirp has modulus one at zero height.
At the raw row-one endpoint its exponent is
\[
                       E_{\epsilon\beta}(1,y)=-\beta J(y)/2.
 \tag{5}
\]
Equations (4)--(5) do not identify the complete sum with its cancelled
endpoint value. They bound the raw rows after the proved reductions.

For \(\beta=1\), construct the twenty new support values
\[
 S_{\epsilon}(\kappa)=
 \max\left\{
 \sup_{[1/5,1/2]\times P}(E_{\epsilon1}-\kappa y),\
 \sup_{y\in P}(-J(y)/2-\kappa y)\right\},
 \quad\epsilon=0,1,\quad
 \kappa=-1/5+j/20,\quad0\le j\le9.
 \tag{6}
\]
The [core concavity theorem](research_mixed_right_half_concavity.md)
gives joint concavity of (4) on (3). At any rational interior trial
point, its affine tangent bounds the entire rectangle; maximizing
that affine function requires only its corners. The one-dimensional
endpoint (5) is concave and is treated the same way. The checker
evaluates both tangent bounds outward and stores a strict rational
upper value. An optimizer proposes trial points only; its convergence
or stationary status is never an acceptance premise. Continuity
includes the endpoint \(u=1/2\).

The type-three moving profiles need no new source values. Their old
height endpoints are \(-.03\) and \(.02\), and the original core
envelopes are convex in height. Hence their zero-height supports are
bounded by \((2/5)S_{-.03}+(3/5)S_{.02}\) on the larger old angle
interval \([.13,.5]\), which contains \(P\). All six ordered
source orientations are thereby represented. Convexity in \(\kappa\)
permits upper chords between adjacent or enclosing support-grid values;
no extrapolation outside \([-1/5,1/4]\) is used.

## 3. Actual geometric reference comparison

Use the original three-vertex window and the six logarithmic variables
of [the core reference certificate](research_mixed_right_core_support.md).
Its whole-product branch is an established input. With window legs
\(a=t_0,b=t_1\), and conditional root \(s=s_1\), form the original
allocated phase \(\phi(a,b)\), gradients \(p_a,p_b\), and
\[
                         C=\phi-p_a a-p_b b.
 \tag{7}
\]
For a support chord \(A\kappa+B\), the upper source defect is
bounded by
\[
 B-\Re\{C+p_a x+p_b y\},\qquad
 (x,y)=(1/2,-A)\quad\text{or}\quad(-A,1/2).
 \tag{8}
\]
The affine evaluation at \(-A\) is algebraic; it is not an
unproved source estimate at that angle.

The checker verifies that (8) is strictly less than \(1/200\)
on all \(8\cdot4\cdot16=512\) actual-window external-boundary
products. It includes both orientations on each product. A fresh
point Newton self-map gives the midpoint value. The complete-cell
Schur Hessian and six-variable response give
\[
 dp_a=\phi_{aa}\,da+\phi_{ab}\,db,
 \qquad dp_b=\phi_{ab}\,da+\phi_{bb}\,db,
 \qquad dC=-a\,dp_a-b\,dp_b.
 \tag{9}
\]
The finite Neumann response keeps the residual, four corrections,
and its \(\rho^5/(1-\rho)\) weighted tail. Norm maxima take
explicit outward upper endpoints. Whole-cell mean-value errors
include both complex reference directions. Exact prefix-free covers
of mass one are required on every boundary product.

For fixed raw source variables, its defect from the original plane
is a real part of a holomorphic function of either external reference.
The compact source supremum is separately subharmonic. The original
window branch precedes this maximum-principle argument. Therefore
the boundary certificate proves, for actual references throughout
the products, the zero-height core ceiling
\[
                         E-\Re\Gamma<1/200.
 \tag{10}
\]
Short cyclic words occur by periodic repetition of the reference
window; their original incidences and phase normalization are retained.

## 4. Partial heights and the complete finite rows

At the prescribed nonzero height \(h_0\) in (1), the frozen core
profiles already have the stronger support gap \(1/500\).
Their profile rectangles contain all actual prescribed plateau
heights, including type-three heights of either sign and the selected
height \(H\). At zero height use (10). For each fixed \(u,y\)
in (3), the original core envelope, including the maximum of the
two true Fourier alternatives, is convex in height. The row-one
envelope has the same property. Subtracting the geometric plane
is affine in height and preserves convexity. Interpolating between
\(0\) and \(h_0\), for each fixed actual reference, therefore
keeps the upper ceiling \(1/200\) on the whole segment (1).
This interpolation does not use a maximum principle in a reference
whose target height is changing.

The complete right-angle and high-row reductions of Section 2 now
give that ceiling on every original row at the right endpoint
\(1/2\). At the other right endpoint \(1\), the existing
all-endpoint theorem already has a strict finite-source gap on the
full physical height bands. Combining the two endpoint bounds with
the full right-angle reduction controls every right angle in
\([1/2,1]\). No small-angle profile at \(.13\), omitted upper
row, or off-grid stationary packet is used in this step.

Uniform finite-product bounds add polynomial factors and the actual
Fourier upper bound adds an arbitrarily small fixed rate tolerance.
Choose the total tolerance below \(1/200\), once for this block.
The raw support ceiling (10) then yields (2). The selected factor at
the real right coordinate has modulus one; at the moving coordinate
its exact linear height correction remains in every interpolated
Fourier branch. Thus all selected indicators, forcing terms, original
level powers and integer-level parities are retained.

The useful new conclusion is the weak positive ceiling (2) for a
partially reset plateau leg. It may be charged to a separately proved
low-source loss. This note does not perform that allocation or control
a block with moving real coordinate below \(.22\) or above \(.45\).

```sh
python3 experiments/certify_mixed_partially_reset_right_support.py --precision 256
python3 experiments/certify_mixed_partially_reset_right_support.py --precision 320 --input repro/results/research-mixed-partially-reset-right-support.json --output /tmp/research-mixed-partially-reset-right-support-review.json
```

The saved replay rechecks the rational source tangents and every
stored reference subdivision. Original-window root proposals remain
subject to complete interval self-maps; cached bounds are not evidence.
