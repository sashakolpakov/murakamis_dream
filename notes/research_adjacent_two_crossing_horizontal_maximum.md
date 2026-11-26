# The unique maximum on the shifted horizontal contour

Research proof, 2 November 2026. On the horizontal contour through the
selected critical point of the adjacent power-two pair, the real action
has exactly one maximum. This statement holds on the whole closed
low-index triangle, not only on a small neighborhood of the critical
point. A short analytic estimate handles the part with first coordinate
at least one half. A rational interval certificate handles the remaining
square and proves a fixed gap outside a local rectangle.

This is a statement about one contour. It does not justify replacing
the finite double sum by its integral over this contour. Connecting
faces and the other terms of the lattice residue formula require
separate estimates.

An [elementary alternative](research_adjacent_two_crossing_horizontal_dominance.md)
uses four rational gradient inequalities to move every possible maximum
into the same rectangle, then proves strict concavity there. It needs no
box subdivision. The certificate below gives an independent verification
and the explicit exterior gap \(1/10000\).

## 1. The contour and the theorem

Use the canonical phase of
[the exact adjacent-pair calculation](research_adjacent_two_crossing_pair.md):
\[
 W(z,w;0)=J(z+w)-3J(z)-6J(w)+J(2w)
        +i\pi(z^2-zw+w^2/2+z+w/2).
 \tag{1}
\]
Here \(J\) is the primitive of \(\log(2\sin\pi z)\)
continued from \(0<z<1\), with its real additive constant fixed
by \(J(0)=0\). Set
\[
 h_x=\frac{3\log2}{4\pi},\qquad
 h_y=\frac{\log7}{4\pi},\qquad
 f(a,b)=\operatorname{Re}W(a+ih_x,b+ih_y;0).
 \tag{2}
\]
The real parameter domain is
\[
 \mathcal T=\{(a,b):0\le b\le1/2,\quad0\le a\le1-b\}.
 \tag{3}
\]
All the arguments in (1) have positive imaginary part on this contour.
The formula extends continuously to the boundary of (3), with the same
logarithmic branches.

Write
\[
 a_* =\frac1{2\pi}\arctan\frac{\sqrt7}{5},\qquad b_* =\frac14,
 \qquad M=f(a_*,b_*).
 \tag{4}
\]
The unexponentiated critical equations in the adjacent-pair calculation
prove \(\nabla f(a_*,b_*)=0\). This exact stationarity is an input
here; it is not inferred from sampled values.

**Theorem.** The point \((a_*,b_*)\) is the unique maximizer of
\(f\) on \(\mathcal T\). Put
\[
 R=[3/50,1/10]\times[23/100,27/100].
 \tag{5}
\]
Then
\[
 -\nabla^2 f\succeq2I\quad\text{on }R,
 \qquad
 f\le M-\frac1{10000}\quad\text{on }\mathcal T\setminus R.
 \tag{6}
\]
In particular the following quantitative bound holds throughout
\(\mathcal T\):
\[
 f(a,b)\le M-
 \min\left\{\frac1{10000},(a-a_*)^2+(b-b_*)^2\right\}.
 \tag{7}
\]
It follows that every fixed neighborhood of the selected point has a
strict exterior action gap on this horizontal contour.

## 2. An absolutely convergent formula for the real action

Define
\[
 r_x=\frac1{\sqrt8},\quad r_y=\frac1{\sqrt7},\quad
 r_{xy}=\frac1{\sqrt{56}},\quad r_{2y}=\frac17,
\]
\[
 Z_x=r_xe^{2\pi ia},\quad Z_y=r_ye^{2\pi ib},\quad
 Z_{xy}=r_{xy}e^{2\pi i(a+b)},\quad
 Z_{2y}=r_{2y}e^{4\pi ib}.
\]
Substituting the normalized dilogarithm formula for \(J\) gives
\[
 \begin{split}
 f(a,b)={}&c_0+c_xa+c_yb\\
 &+\frac1{2\pi}\operatorname{Im}
       \{3\operatorname{Li}_2(Z_x)+6\operatorname{Li}_2(Z_y)
          -\operatorname{Li}_2(Z_{xy})
          -\operatorname{Li}_2(Z_{2y})\},
 \end{split}
 \tag{8}
\]
where
\[
 c_0=\frac{\log7}{4},\qquad
 c_x=-3\log2+\frac{\log7}{2}<0,\qquad
 c_y=\frac{3\log2-\log7}{2}>0.
 \tag{9}
\]
Each dilogarithm in (8) is its absolutely convergent power series
inside the unit disk. The formula therefore has no branch selection
left to perform during the certificate.

Differentiating this convergent series gives
\[
 f_a=c_x-3\log|1-Z_x|+\log|1-Z_{xy}|,
 \tag{10}
\]
\[
 f_b=c_y-6\log|1-Z_y|+\log|1-Z_{xy}|
                                +2\log|1-Z_{2y}|.
 \tag{11}
\]
These formulas are also used to bound the action between the rational
centers of the covering boxes and their faces.

## 3. The part with \(a\ge1/2\)

For \(1/2\le a\le1\),
\(\operatorname{Im}\operatorname{Li}_2(r e^{2\pi ia})\le0\)
whenever \(0<r<1\). One direct proof differentiates in \(r\):
the imaginary part of \(-\log(1-re^{2\pi ia})/r\) has the
sign of \(\sin2\pi a\), and the value starts at zero.
Moreover the linear part of (8), for \(a\ge1/2\),
\(0\le b\le1/2\), is at most
\[
 c_0+\frac{c_x+c_y}{2}
             =\frac{\log7-3\log2}{4}<0.
 \tag{12}
\]
For \(|z|\le r<1\),
\[
 |\operatorname{Li}_2(z)|
    \le r+\frac{r^2}{4(1-r)}.
 \tag{13}
\]
Use \(r_y<2/5\), \(r_{2y}=1/7\), and \(r_{xy}<1/7\).
Equations (8), (12), and (13), together with \(\pi>157/50\),
give
\[
 f(a,b)<
 \frac{6(7/15)+2(25/168)}{2\pi}
 <\frac{32525}{65940}<\frac12.
 \tag{14}
\]
Thus this entire portion is below the selected value
\(M>3/4\), already proved by the rational action bound in
[the extreme-index estimate](research_adjacent_two_crossing_global_tails.md).
It remains to treat the square \([0,1/2]^2\), which is contained
in \(\mathcal T\).

## 4. The local Hessian and a global Taylor remainder

Let
\[
 A=\operatorname{Re}\cot\pi(a+ih_x),\quad
 B=\operatorname{Re}\cot\pi(b+ih_y),\quad
 D=\operatorname{Re}\tan\pi(b+ih_y),
\]
\[
 C=\operatorname{Re}\cot\pi(a+b+i(h_x+h_y)).
\]
The exact real Hessian is
\[
 \nabla^2 f=
 \pi\begin{pmatrix}C-3A&C\\C&C-4B-2D\end{pmatrix}.
 \tag{15}
\]
Here the identity \(\cot2z=(\cot z-\tan z)/2\) has
combined the two terms arising from \(J(w)\) and \(J(2w)\).
For a radius \(r\) and real coordinate \(t\), the quantities
needed in (15) are rational functions of ordinary sine and cosine:
\[
 \operatorname{Re}\cot\pi(t+ih)
       =\frac{2r\sin2\pi t}{1-2r\cos2\pi t+r^2},
\]
\[
 \operatorname{Re}\tan\pi(t+ih)
       =\frac{2r\sin2\pi t}{1+2r\cos2\pi t+r^2},
 \qquad r=e^{-2\pi h}.
 \tag{16}
\]
Every denominator is strictly positive.

The rational interval evaluation of (16) over \(R\) gives, in
particular,
\[
 f_{aa}<-\frac{18}{5},\qquad
 f_{bb}<-\frac{53}{5},\qquad
 |f_{ab}|<\frac45.
 \tag{17}
\]
The full saved bounds are tighter. The two diagonal-dominance margins
in (17) are greater than two, so (17) proves the first assertion of
(6). The same certificate verifies
\[
 \tan(2\pi\cdot3/50)<\frac{\sqrt7}{5}
                  <\tan(2\pi\cdot1/10).
 \tag{18}
\]
Monotonicity of tangent on this interval proves that the exact
stationary point (4) lies inside \(R\). Thus it is the unique
maximum on \(R\), and any rational point of \(R\) supplies
a lower bound for \(M\).

There is also a simple bound for Taylor's remainder on every covering
box. For \(r<1\), the absolute values of both cotangent and tangent
in (16) are at most \((1+r)/(1-r)\). Using
\(r_x<3/8\), \(r_y<2/5\), and \(r_{xy}<1/7\) in (15)
gives
\[
 |f_{aa}|\le\frac{119\pi}{15},\quad
 |f_{ab}|\le\frac{4\pi}{3},\quad
 |f_{bb}|\le\frac{46\pi}{3}.
\]
Both absolute row sums are below \(64\), so
\[
 \|\nabla^2 f\|_{\mathrm{op}}<64.
 \tag{19}
\]
Consequently a box centered at \((a_0,b_0)\), with half-widths
\(d_a,d_b\), has the rigorous action upper bound
\[
 f\le f(a_0,b_0)+|f_a(a_0,b_0)|d_a
              +|f_b(a_0,b_0)|d_b+32(d_a^2+d_b^2).
 \tag{20}
\]
This bound, rather than a sample value alone, is checked on every box.

## 5. The rational certificate on the complement of \(R\)

The standalone verifier is
[verify_adjacent_two_crossing_horizontal_maximum.py](../experiments/verify_adjacent_two_crossing_horizontal_maximum.py).
It uses exact rational endpoints with outward integer rounding at scale
\(10^{40}\). Its arithmetic engine is the existing
[two-leaf certificate engine](../experiments/verify_conway_two_leaf_block_alias_certificate.py),
whose elementary remainder bounds are written in
[the arithmetic proof](../papers/conway-source-bounds/arithmetic.tex).
The verifier rejects Python's optimized mode, since the imported engine
uses assertions for its interval preconditions.

Here are the additional ingredients specific to this certificate.
Square roots of the rational radii are enclosed by integer square roots
at the fixed scale. Sine and cosine values at rational angles use the
engine's Taylor enclosure. On an interval their endpoint values are
supplemented by every enclosed stationary point, so the whole range is
covered. Logarithms in (10)–(11) are evaluated as
\(\tfrac12\log((1-\operatorname{Re}Z)^2+
(\operatorname{Im}Z)^2)\), with positive interval arguments.
The first 40 dilogarithm terms are summed by complex interval
multiplication; their omitted tail has absolute value at most
\[
 \frac{r^{41}}{41^2(1-r)},
 \tag{21}
\]
using an outward upper bound for \(r\).

The rational reference point is \(p_0=(31/400,1/4)\in R\).
Its certified action enclosure is
\[
 \begin{split}
 f(p_0)\in\bigg[
 &\frac{8488512240121050839959216258013143125213}{10^{40}},\\
 &\frac{8488512240121050840048429491203272531822}{10^{40}}
 \bigg].
 \end{split}
 \tag{22}
\]
Both endpoints are approximately \(0.8488512240121051\); the
rational endpoints, not this decimal display, are used in the proof.
Denote the lower endpoint by \(L\). Section 4 proves \(M\ge L\).

Cut the square at the two coordinates of each pair of faces of \(R\).
The eight other resulting rectangles cover its complement. The verifier
subdivides a rectangle at the midpoint of its longer side until the
interval upper bound from (20) is strictly below
\[
 L-\frac1{10000}.
 \tag{23}
\]
Every successful box and its rational action bound are saved. No
floating-point optimizer or sampled maximum is used in this process.
The final certificate consists of 171 accepted boxes, obtained after
334 examined boxes and at most nine subdivisions along a branch.
The accepted boxes and \(R\) have total area exactly \(1/4\);
more fundamentally, each subdivision replaces its parent by its two
exact closed halves, so the construction preserves coverage.

The [saved certificate](../repro/results/research-adjacent-two-crossing-horizontal-maximum.json)
records every rectangle, action upper bound, local Hessian interval,
and source hash. Its least accepted gap below \(L\) is greater
than \(0.0001279\), hence exceeds the required \(1/10000\).
Reproduce the complete rational verification with

```sh
python3 experiments/verify_adjacent_two_crossing_horizontal_maximum.py --output repro/results/research-adjacent-two-crossing-horizontal-maximum.json
```

Equations (20)–(23) prove \(f\le M-1/10000\) on the square
outside \(R\). Equation (14) proves the same, with a much larger
gap, on the rest of \(\mathcal T\). On \(R\), integrate the
Hessian bound in (6) along the segment from the exact stationary point
to obtain \(f\le M-\|(a,b)-(a_*,b_*)\|^2\).
This proves (6), (7), and uniqueness.

## 6. Scope of this contour result

The exact extreme-index theorem permits the original finite sum to be
restricted to a compact subpolygon of \(\mathcal T\), with an
exponential error. The present theorem proves the required horizontal
action maximum and exterior loss for that entire subpolygon.

Neither result estimates the connecting faces between the original
finite contour and this shifted contour. Nor does it remove the
nonconstant terms of the exact cotangent or Poisson kernel. In
particular, another height sign need not have a smaller absolute
action after its lattice penalty is included. The finite-source
asymptotic therefore remains a separate step; the positive local
Hessian and this global horizontal maximum alone do not establish it.
