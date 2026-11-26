# A complete transition-cap source beside the real right half

Research theorem, 5 November 2026. One argument lies on the left transition
cap and the other on the real right half-period. The result bounds the
original finite conditional source, including every row and both Fourier
alternatives. It is a local block estimate, not a mixed-region assembly.

## 1. Exact target domain and statement

Use the original allocated modulus and geometric tangent of
[the right-half block theorem](research_mixed_right_half_block_bound.md).
One target is real, \(x\in[1/2,1]\). Write the other as \(y+ih\), where

\[
 1/10\le y\le11/50,\qquad r(y)=\frac{y-1/10}{3/25}.
 \tag{1}
\]

The allowed heights are the following independent bands:

\[
\begin{array}{c|c}
\text{moving type and selection}&\text{allowed height}\hline
3&-\frac3{100}r(y)\le h\le\frac1{50}r(y)\\
4\text{ unselected}&-\frac{57}{1000}r(y)\le h\le0\\
4\text{ selected}&0\le h\le\frac7{500}\min\{6r(y),1\}.
\end{array}
\tag{2}
\]

These bands include further attenuation by either neighboring cutoff.
In particular the selected cap reaches its full height at \(y=.12\),
not at the slow cutoff \(y=.22\). No correlation between height and a
particular reference is required beyond (2). Every selection at the real
right target is allowed.

**Theorem 1.** For each fixed cyclic three/four word, let \(\Gamma\)
be the original full complex tangent at an actual adjacent critical pair.
Uniformly on (1)--(2), in both orientations, the complete allocated block
satisfies

\[
 B_N\le C N^A\exp N\{\Re\Gamma-1/2000\}.
 \tag{3}
\]

The estimate holds for all sufficiently large integer levels, with both
parities and all original selected factors retained. It is an upper bound
for the sum of absolute rows. No conditional saddle packet at the right
argument is asserted.

## 2. All original rows and the same-height small-angle reduction

Let \(\epsilon\) be the own block's type-four indicator, \(\beta\)
the moving argument's indicator, and \(c=1\) when that argument is first.
Let \(\sigma\) be its selected indicator. The six distinct source
orientations are

\[
 (\epsilon,\beta,c)\in
 \{(0,0,0),(1,1,0),(0,0,1),(0,1,1),(1,0,1),(1,1,1)\}.
 \tag{4}
\]

At right angle \(x=1/2\), retain the complete envelope

\[
 \begin{split}
 E(u,y;h)={}&I_0(u,1/2)+I_h(u,y)-(2+\epsilon)J(u)-2\pi chu\\
 &+\frac\beta2\{\max(\nu_h(y),2\pi h_+)-2\pi\sigma h\},
 \qquad 0\le u\le1.
 \end{split}
 \tag{5}
\]

Here \(I_h,J,\nu_h\) have exactly the original definitions of
[the full right-half reduction](research_mixed_right_half_source_reduction.md).
The first-argument chirp is included in its original orientation. The
right target's true Fourier rate is zero, including its seam, and its
selected frequency has unit modulus.

Both actual real tangent slopes lie strictly between \(-1/5\) and
\(1/4\). The complete right-angle reduction therefore reduces the
supporting-plane comparison to \(x=1/2\) or \(x=1\), with its extra
angular stationary candidate absorbed by the stated row inequalities.
At \(x=1\), the complete
[all-endpoint source](research_mixed_all_endpoint_support.md) and
[remaining orientation](research_mixed_43_endpoint_support.md) already
give finite gap \(1/2000\) throughout the larger physical height bands.

At \(x=1/2\), for \(y\ge.13\), the lower rows reduce to

\[
 1/5\le u\le1/2,
 \quad\text{and the upper rows reduce to }u=1/2\text{ or }u=1.
 \tag{6}
\]

The upper-row statement is
[the full high-row endpoint reduction](research_mixed_high_row_endpoint_reduction.md).
Both reductions keep the same \(y,h\) and the same tangent slopes.

For \(y\in[.1,.13]\), the small-angle lower-row argument instead
moves \(y\) to \(.13\) at the **same height**, retaining the term
\(-\kappa y\) throughout. The
[small-angle high-row theorem](research_mixed_small_angle_high_rows.md)
does the same for every \(u\ge1/2\). Its hypothesis
\(|h|\le.03\) holds: (2) gives height ranges
\([-.0075,.005]\), \([-.01425,0]\), or \([0,.014]\) there.
Thus the required degenerate profiles at \(y=.13\) include the full
fast-selected height \(.014\). They are not the narrower profiles of
the old quadratic taper. The imaginary-height term of the geometric
plane is unchanged by this move.

## 3. A finite family of complete source supports

Use four rational angle profiles:

\[
 Y_0=\{13/100\},\quad Y_1=[13/100,4/25],\quad
 Y_2=[4/25,19/100],\quad Y_3=[19/100,11/50].
 \tag{7}
\]

For \(Y=[l,v]\), set \(r_v=(v-.1)/.12\). The height endpoint
pairs are \((-.03r_v,.02r_v)\) for type three,
\((-.057r_v,0)\) for unselected type four, and \((0,.014)\)
for selected type four. At \(Y_0\) this gives precisely the three
same-height ranges just stated. These independent rectangles contain
all targets after the reductions. There are 72 profiles across (4)
and all selections.

For each fixed height and each analytic Fourier branch
\(q\in\{0,\beta\}\), the core in (6) is jointly concave in
\((u,y)\), by
[the original core concavity theorem](research_mixed_right_half_concavity.md).
The actual maximum of its two branches is convex in height; the raw
row-one profile is convex in height as well. Subtracting the complete
complex tangent adds only an affine function of height. Consequently
the endpoint-height comparisons bound every height in the rectangles.
They also cover \(h=0\) without deleting either Fourier expression.

For each profile \(p\), certify the ten values

\[
 S_p(\kappa)=\max\left\{
  \sup_{[1/5,1/2]\times Y}(E-\kappa y),\quad
  \sup_{y\in Y}(E(1,y;h)-\kappa y)\right\},
 \quad\kappa=-1/5+j/20,\quad0\le j\le9.
 \tag{8}
\]

The source checker evaluates outward tangent bounds at rational trial
points, separately for both branches. Joint concavity bounds the full
core rectangle by the tangent's corner maximum. The raw row-one branch
is concave in \(y\) and has the same one-dimensional tangent bound.
Optimizer output supplies trial points only; its success flag or
stationarity is not an acceptance premise. Membership in the rectangle
and the outward upper bound are checked explicitly. Continuity includes
\(u=1/2\), product zeros and degenerate \(Y_0\).

For clarity, put \(G_H(v)=\Re g(v-iH)\), \(H=|h|\). The original
branch in (5), after subtracting \(\kappa y\), equals

\[
 \begin{split}
 J(1/2+u)+G_H(y+u)&-(1+q/2)G_H(y)-(2+\epsilon)J(u)\\
 &+2\pi(h_+-ch)u+\pi h_+(\beta-q/2)-\beta\pi\sigma h
       -(\kappa+q\pi h_+)y.
 \end{split}
 \tag{9}
\]

This formula is valid at either height sign and retains the true forcing
branch \(q=0\). At \(u=1\), periodicity of \(G_H\) and \(J\)
gives the exact raw endpoint expression used by the checker. It is not
replaced by a coherently cancelled endpoint value.

## 4. The original geometric plane

Use every three-vertex window, both external types, and all external
boundary products in the established typed rectangles
\(R_3=[.30,.39]+i[-.03,.02]\),
\(R_4=[.27,.33]+i[-.057,-.02]\). Its holomorphic branch is
already proved before any maximum-principle reduction. With actual
middle legs \(a,b\), define
\(C=\phi-p_a a-p_b b\), \(p_j=\phi_j\), in the original
absolute phase calibration.

A support chord \(A\kappa+B\) bounds (8) between its grid values,
since a supremum of affine functions is convex in \(\kappa\).
For a fixed profile height \(h\), the full defect is bounded by

\[
 B-\Re\{C+p_a z_1+p_b z_2\},\qquad
 (z_1,z_2)=(1/2,-A+ih)\ \text{or}\ (-A+ih,1/2).
 \tag{10}
\]

The value \(-A\) is only an affine evaluation of the supporting plane;
it does not assert source control at that auxiliary angle.

Original six-variable affine Newton enclosures and a fresh midpoint
Newton enclosure control (10). The complete Schur response retains
\(dp_j=\sum_k\phi_{jk}\,dr_k\) and
\(dC=-a\,dp_a-b\,dp_b\). Its finite Neumann expansion includes
the initial residual, four corrections and the weighted fifth-power
tail. All norm maxima use explicit outward upper endpoints. Whole-cell
complex mean-value errors retain the height \(h\) in (10).

On each of the \(8\cdot4\cdot16=512\) boundary products, exact
prefix-free rational covers of mass one certify (10) strictly below
\(-1/1000\), for all matching source profiles and selections.
For fixed raw source variables, the defect is harmonic in either
external reference. Its compact supremum is separately subharmonic.
The boundary certificate therefore extends throughout the reference
products. Actual cyclic references, including periodic lifts of lengths
one and two, are included. No independent arbitrary inner reference is
substituted for the original window root.

## 5. Passage to the complete finite source

The original product/Riemann bounds control every finite row with an
arbitrarily small common exponential tolerance and a polynomial factor.
They include all product zeros and the top row. The actual Fourier
upper bounds keep the forced recurrence through both right seams.
The moving angle is bounded away from zero, so its two Fourier
expressions in (5) are uniform over the full compact target bands.
Their selected frequency corrections remain literal.

Choose one total tolerance less than \(1/2000\) in this passage at
\(x=1/2\). The certified phase margin \(1/1000\) leaves the finite
gap in (3). At \(x=1\), use the already proved finite endpoint
gap without spending another tolerance. The full angular and row
reductions then give (3) for the original sum of absolute rows.
All scalar level factors and allocated half-weights are unchanged.

```sh
python3 experiments/certify_mixed_transition_right_support.py --precision 256
python3 experiments/certify_mixed_transition_right_support.py --precision 320 \
  --input repro/results/research-mixed-transition-right-support.json \
  --output /tmp/research-mixed-transition-right-support-review.json
```

Saved mode rechecks the rational tangent witnesses and every original
reference cell with outward arithmetic. The source inequalities,
reference covers and all inherited proof/script/record hashes must be
complete and current. This theorem alone does not control a full mixed
left/right configuration, an open chain or the entire period.
