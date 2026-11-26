# The complete three-four kernel and its geometric contribution

Research theorem, 7 November 2026. The original three-four kernel
has a nonzero geometric leading term near its alternating boundary
parameters. The proof estimates the complete finite source, including
its physical tails and every discrete Fourier correction. Both
quantitative comparisons used below have been certified with the
fixed procedures and immutable records identified in this note.

## 1. The function and its two global comparisons

Let
\[
 \mathcal K_{34,N}(x,y)=h_N(x)^T A_{3,N}A_{4,N}h_N(y)
\]
be the original finite boundary kernel, with all its ordinary-color
terms and normalizations. Its exact four-index formula is equation
(2) of [the contracted-source proof](research_mixed_contracted_pair_rectangle.md).
In particular its support is
\[
 i,j,k,l\ge0,\qquad i+j<N,\quad j+k<N,\quad k+l<N.
\]
For the normalized indices, its closed support is
\(\Omega=\{s,t,p,q\ge0:s+t\le1,\ t+p\le1,\ p+q\le1\}\).
The phase \(\mathcal F\), symbol \(b\), and unit scalar
\(\kappa_N^3\) are those of that formula. No sum over an index
is replaced by its absolute value before the shared-wire contraction.

Write \(x_0\) for the original alternating boundary parameter,
\(z_*=(z_3,z_3,z_4,z_4)\) for the original critical point, and
\[
 M=\Re\mathcal F(z_*;x_0,x_0)
       =\Re\Phi_3(x_0,x_0)+\Re\Phi_4(x_0,x_0).
\]
Use the enlarged real box and the original imaginary intervals from
[the enlarged-rectangle theorem](research_mixed_contracted_pair_enlarged_rectangle.md):
\[
 C'=[1/4,1/2]\times[1/5,9/20]\times[1/5,21/50]^2.
\]
The two global comparisons used in the proof are:

1. The original real rate \(E\) has a strict gap below \(M\)
   on the complete physical complement of \(\operatorname{int}C'\).
   The [enlarged tail reduction](research_mixed_contracted_pair_enlarged_tail_reduction.md)
   and the [saved-gradient transport protocol](research_mixed_contracted_pair_saved_face_transport_protocol.md)
   specify a finite sufficient check.
2. Each of the eight full-box quantities
   \[
   B_{j,\pm}:=\max_{u\in C'}\{
      \Re\mathcal F(u+ih_{j,\pm}e_j;x_0,x_0)
                      -2\pi|h_{j,\pm}|\}
   \]
   lies strictly below \(M\). Their heights are
   \(h_{s,-}=h_{t,-}=-3/100\),
   \(h_{p,-}=h_{q,-}=-11/200\), and
   \(h_{j,+}=3/200\). The
   [eight-alias protocol](research_mixed_contracted_pair_eight_aliases_protocol.md)
   fixes these comparisons with their original Fourier penalties.

The earlier failed faces at \(s=9/20\) and \(t=1/4\)
belong to the interior of this enlarged coherent region. Their
[recorded rate excesses](research_mixed_contracted_pair_nine_faces_diagnosis.md)
remain true. Neither comparison asks for the false old-complement bound.

The first comparison is established by the
[saved-gradient transport record](../repro/results/research-mixed-contracted-pair-saved-face-transport.json),
SHA-256
`1f202cbccfc276a54b4e80e70d8ad1c30d182b3420b0c00a9daba5951a78e6c4`.
It verifies all nine affine comparisons, retaining all 36 signed
support terms, with every one of its 39 input bindings unchanged.
The largest face upper bound is below \(150464/100000\). The far-region bound
therefore dominates and gives
\[
 \sup_{\Omega\setminus\operatorname{int}C'} E
       \le2261/1500<M-19/3750<M-1/200.
 \tag{P}
\]
This is a deduction from the written domain proofs and exact
recombination of saved interval endpoints. The failed old calculation
was not repeated or overwritten.

The second comparison is established by the
[eight-alias record](../repro/results/research-mixed-contracted-pair-eight-aliases.json),
SHA-256
`c9ab53fcb11dadc5461bf3968ff0d4cfe423861c2dbd90394a9872627facd9a1`.
Its eight outward tangent bounds all pass, with all 35 source
bindings unchanged. In exact rational comparisons the largest
upper bound is less than \(73/50\). Hence every one of the
eight horizontal rates satisfies
\[
                         B_{j,\pm}<73/50<M-1/20.
 \tag{A}
\]
The fixed checker used the original full root square and primitive
constants. Its floating-point steps only chose rational supporting
points; the inequalities are outward global tangent bounds on the
strictly concave full box. No stationary-point approximation is
assumed to be exact.

## 2. The whole-kernel theorem

**Theorem.** There is a fixed complex neighborhood \(U\) of
\((x_0,x_0)\), independent of \(N\), on which
\[
 \mathcal K_{34,N}(x,y)=
 \kappa_N^3 N^{-1/2}B_{34}(x,y)
          e^{N\Phi_{34}(x,y)}(1+O_U(N^{-1})).
 \tag{1}
\]
Here \(z_*(x,y)\) is the continued original critical point,
\[
 \Phi_{34}(x,y)=\mathcal F(z_*(x,y);x,y),\qquad
 B_{34}(x,y)=
 \frac{(2\pi)^2 b(z_*(x,y);x,y)}
             {\sqrt{\det[-\mathcal F''(z_*(x,y);x,y)]}}.
 \tag{2}
\]
Both functions are holomorphic, \(B_{34}\) is nowhere zero on
\(U\), and the square root is its original accretive branch.
The error in (1), after the displayed normalization, has
\(O(N^{-1})\) derivatives of every fixed order on smaller
neighborhoods. The statement holds along the full sequence of
integer levels, including both parities.

In particular, at the reference,
\[
       \lim_{N\to\infty}N^{-1}
                  \log|\mathcal K_{34,N}(x_0,x_0)|=M.
 \tag{3}
\]
More precisely, there are fixed \(c,C>0\) such that, for every
sufficiently large integer \(N\),
\[
 cN^{-1/2}e^{NM}\le |\mathcal K_{34,N}(x_0,x_0)|
                              \le CN^{-1/2}e^{NM}.
 \tag{4}
\]
Thus this is a lower bound for the original complex sum, as well
as an upper bound.

*Proof.* The proof keeps separate the local Gaussian error and the
exponentially smaller part of the original finite source.

First choose half-grid cuts enclosing precisely the central lattice
indices. Their real box \(C'_N\) differs from \(C'\) by
\(O(N^{-1})\). All three support sums are bounded strictly below
one on a fixed neighborhood of this box. The exact finite identity
in [simultaneous contour transport](research_mixed_contracted_pair_simultaneous_contour.md)
is therefore available on the enlarged rectangle:
\[
 \mathcal K_{34,N}=\mathcal P_N+\mathcal M_N
                                  -\mathcal J_N+\mathcal A_N.
 \tag{5}
\]
Here \(\mathcal P_N\) contains all physical rows outside the
central box; \(\mathcal M_N\) is the fourfold zero-frequency
integral at the critical heights; \(\mathcal J_N\) consists of
the joining face integrals under one common height translation;
and \(\mathcal A_N\) is the complete discrete lattice correction.
Its 255 grouped terms, or 624 terms after splitting the two vertical
sides, include all original Fourier denominators and signs. Formula
(5) is an equality of the full original functions.

Comparison (P) bounds \(\mathcal P_N\). Uniform factorial
estimates hold up to the physical triangular faces, with errors of
order \(\log N\) in the exponent. There are at most \(N^4\)
rows. Consequently these errors and the number of rows cost only
a polynomial, leaving a strict exponential gap. Prohibited rows
with a sum equal to \(N\) are zero; a two-sided logarithmic
estimate for such a zero row is unnecessary.

Next consider \(\mathcal J_N\). At reference critical heights,
strict horizontal concavity gives a positive gap on every central
face, since the real critical point is strictly inside \(C'\).
At height zero, (P) gives a gap on those same faces.
The real part of the phase is convex along the common imaginary
translation. Its value at any intermediate height is bounded by
the larger endpoint value. This proves a strict gap on every
joining face in (5), including their intersections. Half-grid
displacements use only a smaller fixed gap.

For \(\mathcal A_N\), the original gradient strip proves
\[
 W(u,v)=\Re\mathcal F(u+iv)-2\pi\sum_j|v_j|
\]
decreases as any absolute height increases, with the other
coordinates fixed. A term containing a vertical side has a real
coordinate on a central face. Reducing its heights to zero bounds
its rate by that physical-face rate. A term containing only
horizontal factors has a nonzero height vector. Retain any one
of its nonzero heights and reduce the others to zero. The resulting
upper rate is one of the eight quantities bounded in (A).
The exact alias denominators are bounded away from zero for large
\(N\), and the contour lengths and prefactors again cost only
powers of \(N\). Hence all lattice corrections are exponentially
smaller than \(e^{NM}\).

It remains to evaluate \(\mathcal M_N\). The original symbol
expansion, including its outside scalar, is
\[
 F_N(z;x,y)=\kappa_N^3N^{-5/2}
             b(z;x,y)e^{N\mathcal F(z;x,y)}(1+O(N^{-1})).
\]
The lattice integral contributes \(N^4\); its nondegenerate
four-variable Gaussian contributes \((2\pi/N)^2\).
Strict concavity makes the selected critical point the unique
maximum on this horizontal contour. The local stationary-phase
calculation therefore gives precisely (1)--(2). Its coefficient
is nonzero because every factor of \(b\) is nonzero on the
regular domain and the Hessian is accretive. This uses the actual
local symbol of (5), without identifying coefficients merely from
agreement of two critical equations.

All estimates just used have strict margins on compact sets. The
implicit function theorem continues the critical point inside the
regular rectangle. Shrinking a fixed endpoint neighborhood preserves
the factorial and denominator margins, the physical and alias gaps,
and the positive distance to the contour faces. The main contour
may be moved locally to the continued critical point with the same
joining estimates. Thus, on a slightly larger neighborhood than
\(U\), the sum of the other terms in (5) is bounded by
\[
       C N^b\exp\{N(\Re\Phi_{34}(x,y)-\delta)\}
\]
for fixed \(C,b,\delta>0\). This is smaller than the Gaussian
error in (1). The complete normalized remainder is holomorphic;
Cauchy estimates on nested neighborhoods prove its fixed-order
derivative bounds. All source and lattice identities were retained
for both parities. Finally \(|\kappa_N|=1\) and the nonzero
coefficient in (2) give (4), and then (3). \(\square\)

## 3. Scope of this conclusion

The theorem concerns the complete finite kernel near its specified
complex boundary parameters. It controls the nonzero geometric
contribution against every other term of that kernel. It supplies no
estimate for an arbitrary incoming boundary function outside this neighborhood.
Iteration in a larger tangle still requires such a whole-function
estimate and control of the transported remainder. Nor is the open
kernel in (3) itself a knot invariant. A knot-volume conclusion
requires the original closure and its geometric action, and the
finite-exception goal still requires arbitrary fixed short pieces.
