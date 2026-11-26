# Exact angular candidates for full conditional-source support bounds

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This note retains the neighboring angle in the whole finite-product bound.
After subtracting a geometric supporting plane, its angular maximum reduces
to endpoints and roots of a quadratic or sextic, together with explicit
Fourier-branch boundaries. It supplies no numerical supporting-plane budget.

## 1. The actual product and Fourier envelopes

Fix a row fraction \(u=j/N\in[0,1]\), a height \(h\), and put
\[
 \rho=e^{2\pi h},\quad
 L_h(x)=\log|1-\rho e^{-2\pi ix}|,\qquad
 I_h(u,\beta)=\int_0^u L_h(\beta+t)\,dt .
 \tag{1}
\]
Integrable logarithmic zeros are included in this definition. For the
original product \(p_j(Y)=(rY;r)_j\), \(r=e^{-2\pi i/N}\),
\[
 |p_j(e^{-2\pi i(\beta+ih)})|
       \le N^A\exp\{N I_h(j/N,\beta)\}.                         \tag{2}
\]
This bound is uniform in all rows, the whole real angular period, and a
fixed compact height interval. To see this even through zeros, truncate
\(L_h\) below \(-\log N\). Its total variation is \(O(\log N)\);
the integral increases by \(O(1/N)\), uniformly on such height intervals.
The shifted Riemann upper estimate is consequently \(O(\log N)\).
At a literal zero the product vanishes and the inequality remains valid.
This is the same finite-product argument as in
[the seam bound](research_mixed_boundary_strip_bounds.md#2-a-product-bound-that-includes-the-whole-finite-period),
without maximizing over \(\beta\).

Use the original branch
\[
 \nu_h(\beta)=-\Re g(\beta+ih),\qquad
 K_h=2\pi\max(h,0),\qquad 0<\beta<1.
 \tag{3}
\]
Its one-sided continuous values and derivative are
\[
 \nu_h(0)=\pi\max(h,0),\quad
 \nu_h(1)=-\pi\max(h,0),\quad
 \nu_h'(\beta)=-L_h(\beta).
 \tag{4}
\]
For negative heights the endpoint values follow from the original
dilogarithm primitive; for positive heights use its exact reflection
identity. At zero height they follow by continuity.

For \(\sigma\in\{0,1\}\), retain the selected-alias normalization:
\[
 W_{h,\sigma}(\beta)
   =\max\{\nu_h(\beta),K_h\}-2\pi\sigma h.
 \tag{5}
\]
This is the true upper exponent of the original Fourier polynomial,
including its forcing part, rather than a replacement by the factorial
branch. More precisely, for every \(\delta>0\), on the actual height band
\(-.057\le h\le.02\),
\[
 |d_N(Y)Y^{-N\sigma}|
 \le C_\delta N^A
       \exp N\{W_{h,\sigma}(\beta)+\delta\},\qquad 0\le\beta\le1.
 \tag{6}
\]
On compact subintervals of \((0,1)\), this is the
[absolute Fourier comparison](research_mixed_fourier_weight_continuation.md#5-a-criterion-for-relative-exponential-accuracy).
Here is why its extension to the two seams does not discard a term.
Iterate the exact recurrence
\[
 d_N(r^{-1}Y)=(1-Y)d_N(Y)
                 +\frac{Y}{N^2}\sum_{k=0}^{N-1}Y^k.            \tag{7}
\]
On a sufficiently small angular strip about the seam the multiplier
has modulus less than \(1/2\), uniformly on this height band.
The forcing has upper rate \(K_h\). Starting at a small positive
angle, the absolute comparison has rate
\(\max(\nu_h,K_h)+o(1)=K_h+o(1)\), uniformly in \(h\);
this follows from (4) and continuity, including \(h=0\).
Thus the contracting recurrence gives rate \(K_h+o(1)\) on both
sides of the seam. Since \(\max(\nu_h,K_h)\ge K_h\), this proves
(6) there too. Finally multiply by the literal factor \(Y^{-N\sigma}\).
No Fourier alias or forcing term has been removed.

For an own type \(\epsilon\in\{0,1\}\) and real tangent slope \(\kappa\),
the angular part of the local upper exponent is therefore
\[
 A(\beta)=I_h(u,\beta)+\frac{\epsilon}{2}W_{h,\sigma}(\beta)
                         -\kappa\beta .
 \tag{8}
\]
Other row-dependent terms are independent of \(\beta\) and remain
outside this maximization. If the original complex supporting derivative
is \(p\), then \(\kappa=\Re p\). Its height term
\(\Re[p\,i(h-h_*)]=-\Im(p)(h-h_*)\) must also be retained as a
constant in that fixed-height comparison. Equation (8) does not suppress it.

## 2. Branches and stationary polynomials

Write \(\theta=2\pi\beta\), \(\omega=2\pi u\), and
\[
 D_0=1+\rho^2-2\rho\cos\theta,\qquad
 D_1=1+\rho^2-2\rho\cos(\theta+\omega).
 \tag{9}
\]
On an open interval avoiding zeros and Fourier branch changes,
let \(q=\epsilon\) when \(\nu_h>K_h\), and let \(q=0\) when
\(\nu_h<K_h\). If \(\epsilon=0\), simply take \(q=0\) everywhere.
The derivative is exactly
\[
 A'(\beta)=\tfrac12\log D_1-\tfrac{2+q}{4}\log D_0-\kappa.
 \tag{10}
\]
The selected-alias term in (5) is constant in \(\beta\); it changes
the objective value but not this equation.

Set \(t=\tan(\pi\beta)\), away from \(\beta=1/2\), and define
\[
 \begin{split}
 a(t)&=(1-\rho)^2+(1+\rho)^2t^2,\\
 b(t)&=1+\rho^2-2\rho\cos\omega
          +4\rho\sin\omega\,t
          +(1+\rho^2+2\rho\cos\omega)t^2.
 \end{split}
 \tag{11}
\]
Then \(D_0=a/(1+t^2)\) and \(D_1=b/(1+t^2)\). Every regular
stationary point is exactly a real root of the following polynomial,
filtered by its interval and its indicated Fourier branch:
\[
 \begin{array}{ll}
 q=0:& P_0(t)=b(t)-e^{2\kappa}a(t)=0,\\[2mm]
 q=1:& P_1(t)=b(t)^2(1+t^2)-e^{4\kappa}a(t)^3=0 .
 \end{array}                                                    \tag{12}
\]
The first polynomial has degree at most two; the second degree at
most six. The logarithms in (10) have positive arguments on these
regular intervals, so (12) introduces no sign ambiguity from squaring.

The sextic is never identically zero: at \(t=i\),
\[
                    P_1(i)=64e^{4\kappa}\rho^3\ne0.            \tag{13}
\]
The quadratic is identically zero precisely when
\(u\in\{0,1\}\) and \(\kappa=0\). Indeed such an identity means
\(D_1=e^{2\kappa}D_0\) for the whole circle. Their equal averages
force \(e^{2\kappa}=1\), and their nonzero first Fourier coefficients
then force \(e^{i\omega}=1\). Conversely these conditions plainly
give the identity. On every corresponding \(q=0\) branch, (8) is
constant, so endpoints suffice. This includes \(I_h(0,\beta)=0\)
and \(I_h(1,\beta)=K_h\).

## 3. The full candidate set, including seams and degeneracies

**Theorem 1.** Fix any closed angular interval
\([\ell,r]\subseteq[0,1]\). The maximum of the actual envelope (8)
equals its maximum over the following finite candidate set:

1. Both endpoints \(\ell,r\).
2. The tangent pole \(\beta=1/2\), when it belongs to the interval.
3. The zeros of \(D_0D_1\). These occur only at \(h=0\), and are
   the points \(\beta=0,1,1-u\) that belong to the interval.
4. If \(\epsilon=1\), every Fourier switching point
   \(\nu_h(\beta)=K_h\) in the interval.
5. Every regular real root of (12) whose inverse tangent lies in
   the interval and satisfies the branch condition used in (10).

An identically zero \(P_0\) contributes its branch endpoints instead
of a continuum of candidates. Repeated roots and coinciding candidates
are retained once; neither a derivative sign change nor simplicity
is required for inclusion.

*Proof.* The objective is continuous on the closed interval, including
every logarithmic product zero. Split it at items 1--4. On each remaining
open piece it is differentiable and obeys (10). A nonconstant interior
maximum satisfies (12). The degenerate constant pieces have the same
value at their endpoints. Each nonzero polynomial has finitely many
roots; the Fourier boundaries are finite as follows.

Since \(\nu_h'=-\tfrac12\log D_0\), its critical angles satisfy
\(\cos(2\pi\beta)=\rho/2\). For \(\rho\ge2\), it is decreasing
apart from a possible isolated zero derivative; here \(h>0\),
and (4) implies \(\nu_h<K_h\) everywhere. If \(0<\rho<2\), put
\[
                   \beta_0=\frac{\arccos(\rho/2)}{2\pi}.
 \tag{14}
\]
The function increases on \((0,\beta_0)\), decreases on
\((\beta_0,1-\beta_0)\), and increases on \((1-\beta_0,1)\).
For \(h\le0\), reflection gives
\(\nu_h(1-\beta)=-\nu_h(\beta)\), hence its only interior
crossing of \(K_h=0\) is \(1/2\). For \(h>0\), both endpoint
values are strictly below \(K_h\), as is the entire last
increasing interval. There are at most two crossings, on the
first increasing and middle decreasing intervals; a tangency at
\(\beta_0\) is included. These monotone intervals provide exact
one-dimensional brackets for any branch-crossing certification.

The tangent map must be inverted separately on
\((0,1/2)\) and \((1/2,1)\). A point at its pole remains in item 2,
even if the polynomial loses its top coefficient. At \(h=0\),
the integral in (1) is finite through a zero; items 1 and 3 keep
these removable or nondifferentiable cases without dividing by
\(D_0\) or \(D_1\). In particular the cases \(u=0,1\) are evaluated
by their exact constant integrals, never by subtracting two infinite
logarithms. This exhausts every maximum. \(\square\)

All objective values must be evaluated using (8), with the original
one-sided branches and the complete alias normalization. Squared
polynomial equations alone do not authorize discarding a Fourier
switch, moving a tangent-pole endpoint, or replacing the maximum in (5).

## 4. Application scope and reproduction

The theorem applies row by row to the whole original finite product.
One may now maximize over the remaining row variable, adding the unchanged
first-product, sine-factorial, and full complex supporting-plane terms.
Proving that final maximum lies below the geometric plane is a separate
inequality. No such inequality, contour deformation, or mixed-word source
asymptotic is claimed here.

    python3 experiments/check_mixed_angular_support_candidates.py

The checker verifies the exact tangent substitutions, differentiated
stationary equations, degree and degeneracy identities, and normalization
bookkeeping. These are algebraic checks, not sampled finite kernels.
