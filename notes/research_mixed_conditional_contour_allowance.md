# An upper bound with an allowed error in the exponential rate

Research deduction, 5 November 2026. The endpoint comparisons have a
strict reserve. Consequently the next conditional factor need not have
a full asymptotic expansion, or even an upper bound at exactly its
critical rate. This note gives a sufficient weaker estimate directly
from the original finite sum and its index contour. The geometric
critical point and the finite sum remain the ones already defined in
the conditional-source proofs.

## 1. The finite sum and the quantities to bound

Let \(\epsilon\in\{0,1\}\), \(r=e^{-2\pi i/N}\), and
\(P_j=(r;r)_j\). With the marked factorial \(\widehat P_N\)
from [the canonical-source definition](research_mixed_three_canonical_conditional.md),
put
\[
 \mathcal L_{\epsilon,N}(A,B)=
 \widehat P_N(NA)\widehat P_N(NB)
 \sum_{j=0}^{N-1}
 \frac{e^{2\pi iAj}(r^{NA+1};r)_j(r^{NB+1};r)_j}
      {P_j^{2+\epsilon}}.
 \tag{1}
\]
In particular, the rows that vanish at physical integer colors have
not been removed. Write
\[
 Q(s)=g(s+A)+g(s+B)-(2+\epsilon)g(s)+2\pi iAs,
 \qquad M=\Re Q(s_*),
 \tag{2}
\]
where \(g\) has the original logarithmic lift and \(Q'(s_*)=0\)
is the continued geometric critical point. All parameter sets below
are compact; constants may depend on them, but not on \(N\).

Use the fixed index rectangle
\[
 R=[\ell,u]+i[-h,h],\qquad
 \ell=3/20,\quad u=49/100,\quad h=1/5.
 \tag{3}
\]
Assume \(A,B\in\mathcal Q=\{.23<\Re z<.45,
|\Im z|<.12\}\), and assume that the original critical point
lies strictly inside \(R\), uniformly on the compact parameter set.
The regular factorial strips contain a neighborhood of this entire
rectangle. The [central curvature lemma](research_mixed_conditional_image_contours.md)
then supplies
\[
                         -\Re Q''(s)>1/8\qquad(s\in R).
 \tag{4}
\]
The root-containment assumption is substantive. Membership in the
larger cotangent chamber alone is not a substitute for it.

For real \(v\in[0,1]\), let \(H(v)\) be the full absolute-row
rate, including rows beyond the physical support:
\[
\begin{split}
 H(v)={}&\Re g(A)+\Re g(B)
 +\int_0^v\log|1-e^{-2\pi i(A+x)}|\,dx\\
 &+\int_0^v\log|1-e^{-2\pi i(B+x)}|\,dx
 -(2+\epsilon)J(v)-2\pi v\Im A.
\end{split}
 \tag{5}
\]
Zeros in these integrals are interpreted by their integrable limits.
Define the nonnegative allowance
\[
\begin{split}
 D(A,B)=\max\bigg\{&0,
 \sup_{v\in[0,\ell]\cup[u,1]}H(v)-M,\\
 &\sup_{x\in[\ell,u]}\Re Q(x+ih)-2\pi h-M,\\
 &\sup_{x\in[\ell,u]}\Re Q(x-ih)-2\pi h-M\bigg\}.
\end{split}
 \tag{6}
\]
Thus \(D\) records only how far the real tails or the two horizontal
alias contours can exceed the geometric action. It does not estimate
the central real rows separately: those rows must be summed before
their contour is moved to the critical height.

## 2. The upper-bound lemma

**Lemma 1.** Under the preceding assumptions, for every \(\eta>0\)
there are constants \(C_\eta,B_\eta\) such that, for every
sufficiently large integer \(N\),
\[
 |\mathcal L_{\epsilon,N}(A,B)|
 \le C_\eta N^{B_\eta}
          \exp\{N(M+D(A,B)+\eta)\}.
 \tag{7}
\]
The bound is uniform on the compact parameter set and includes both
parities. No nonzero leading coefficient is asserted.

*Proof.* The finite-product upper estimates used in the
[complex-neighbor continuation](research_mixed_four_conditional_complex_neighbors.md)
give, uniformly for all real rows,
\[
 |\text{row }j|\le C_\eta N^{B_\eta}
                  e^{N(H(j/N)+\eta/4)}.
 \tag{8}
\]
For general parameters in a compact subset of \(\mathcal Q^2\),
the same estimate follows by replacing each logarithm of a numerator
modulus by \(\log(|1-e^{-2\pi i(A+x)}|+\delta)\).
Its Riemann sums have a uniform bounded error for fixed
\(\delta>0\). The integral error tends uniformly to zero as
\(\delta\downarrow0\): the only possible singularities are simple
real zeros, and their local error is
\(O(\delta(1+|\log\delta|))\). The denominator factorials
retain their uniform \(O(\log N)\) endpoint error. This proves
(8) without differentiating through a zero. Summing at most \(N\)
tail rows gives their part of (7).

Choose half-grid cuts \(\ell_N,u_N\) tending to \(\ell,u\).
The exact central interpolation is the same marked-factorial
interpolation as in the canonical-source proof. On a neighborhood
of \(R\) it has a uniform upper bound
\(C N^B e^{N\Re Q(s)}\). Its cotangent contour formula has
the unchanged coefficient \(N/(2i)\). The constant modes combine
to \(+N\) times the real central integral. The remaining modes
have factors bounded by \(Ce^{-2\pi Nh}\) on the horizontal
sides, and \(2e^{-2\pi N|y|}\) on a half-grid vertical side.

Move the zero-mode integral to the height \(y_* =\Im s_*\),
retaining its two endpoint integrals. On the new horizontal segment,
stationarity and (4) give
\[
 \Re Q(x+iy_*)\le M-\frac1{16}(x-\Re s_*)^2\le M.
 \tag{9}
\]
For a real cut \(c\in\{\ell,u\}\),
\(\Re Q(c)=H(c)\le M+D\). At the other end of a zero-mode
endpoint segment, (9) bounds the phase by \(M\). The function
\(y\mapsto\Re Q(c+iy)\) is convex by (4). Its value anywhere
on that segment is therefore at most \(M+D\).

On each of \([-h,0]\) and \([0,h]\), the weighted vertical
alias rate
\[
                  \Re Q(c+iy)-2\pi|y|
 \tag{10}
\]
is also convex. At \(y=0\) it is at most \(M+D\); at
\(y=\pm h\) the same bound follows from (6). Hence every
vertical alias integral obeys (7). The horizontal aliases obey
it directly by (6). No current has been omitted.

The phase is continuous on a slightly enlarged central rectangle,
and \(H\) is uniformly continuous including its integrable-zero
walls. Half-grid rounding therefore costs \(o(N)\), uniformly.
The finitely many contour pieces and at most \(N\) real rows
cost only a polynomial. Assigning the remaining tolerance once
proves (7). \(\square\)

The proof needs no strict tail gap and no Gaussian evaluation. If
one establishes \(D\le d\), it gives an upper rate \(M+d\).
To obtain fixed parameter derivatives, the same assumptions and
allowance must hold on a complex neighborhood, perhaps with a
slightly larger \(d\). Cauchy's estimate then applies on smaller
neighborhoods. A bound only on a real parameter path does not itself
justify derivatives transverse to that path.

## 3. The right tail without a monotonicity assumption

The left-tail estimate already proved in the contour-reduction note
gives \(H'>1/2\) on \((0,\ell]\). Its maximum is \(H(\ell)\).
For the right tail put \(w=-\cot\pi v\), and define
\[
\begin{split}
 p_{A,B,\epsilon}(w)={}&4^{-\epsilon}
 e^{2\pi(\Im B-\Im A)}
 |\cos\pi A-w\sin\pi A|^2\\
 &\qquad\cdot|\cos\pi B-w\sin\pi B|^2(1+w^2)^\epsilon-1.
\end{split}
 \tag{11}
\]
For real \(w\) this is a real polynomial of degree four or six,
and it equals \(e^{2H'(v)}-1\) wherever the numerator factors
are nonzero. Its leading coefficient is strictly positive because
\(\sin\pi A\) and \(\sin\pi B\) are nonzero.

**Lemma 2.** The maximum of \(H\) on \([u,1]\) is attained at
\(u\), at \(1\), or at a point \(v\in(u,1)\) for which
\(p_{A,B,\epsilon}(-\cot\pi v)=0\).

*Proof.* Away from numerator-zero walls, an interior maximum has
\(H'=0\), which is precisely (11). At a numerator-zero wall
strictly inside \((u,1)\), the logarithm of that factor tends to
\(-\infty\) from both sides, while the other terms in \(H'\)
are bounded above there. Thus \(H'<0\) on a punctured
neighborhood and \(H\) decreases across the wall. Such a point
is not a local maximum. Continuity includes the endpoint \(1\).
These alternatives exhaust the compact interval. \(\square\)

There are at most six candidate interior points. They must all be
retained; this lemma does not select a convenient algebraic branch.
The earlier condition that the right-tail polynomial stay below one
on an initial interval remains an efficient sufficient test. It is
not a necessary condition for (7), and failure of that test does not
show that the finite-source bound fails.

## 4. How much allowance the endpoint argument can afford

Let \(z=b+ik\) be the second coordinate on its actual vertical
path, and keep the third reference \(r_3\) fixed. The
[type-three phase comparison](research_mixed_three_first_vertical_phase.md)
proves that the first-pair upper rate plus the following allocated
phase is below its reference rate by more than \(3/100\) for
prefix \(33\), and more than \(3/125\) for prefix \(43\).
The [type-four comparison](research_mixed_four_first_vertical_phase.md)
retains a reserve \(1/20\) for prefixes \(34\) and \(44\),
including the two allowed Fourier alternatives.

Suppose the complete next factor, with exactly its allocated
Fourier halfweights, has upper rate at most its allocated phase
plus \(1/100+\eta\), uniformly on the required path. Then the
literal product of the first pair and that next factor has a
strict loss \(1/100\) for every prefix. Indeed the smallest
reserve is \(3/125\), and
\[
 \frac3{125}-\frac1{100}-\frac1{400}
       =\frac{23}{2000}>\frac1{100}.
 \tag{12}
\]
One total tolerance below \(1/400\), after combining the
factors, is therefore sufficient. The other three reserves are
larger. The original stationarity equations cancel the shared
supporting tangents exactly; no independent height-reset error
is added.

For the canonical sum, Lemma 1 bounds the excess by \(D\).
Passing to the literal conditional factor subtracts the same two
marked factorial actions from both sides. The allocated Fourier
weights add their actual upper rates to both sides. Hence a proof
of \(D\le1/100\), together with those existing weight bounds,
is enough. It is unnecessary to prove a nonzero asymptotic, or a
sharp \(D=0\) bound, along the entire deformation.

This is a sufficient reduction, not an assertion that \(D\le1/100\)
has been established. Root containment, the real-tail allowance,
and the alias allowance still have to be checked on the actual
paths. Bounds on the remaining open-source regions are separate.

For the first-collar application there is now a more direct route.
The [second-three transport](research_mixed_three_first_source_transport.md)
and [second-four transport](research_mixed_four_fixed_contour_transport.md)
keep the original reference contour fixed and bound its integrand
after changing the external height. They prove the required finite
upper estimates without locating the moving critical point in (3).
Thus the sufficient criterion (6) is retained for other applications;
its unresolved moving-root hypothesis is no longer an obstruction
to that particular first-collar estimate.
