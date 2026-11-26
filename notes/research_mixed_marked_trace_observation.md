# Marked traces, homogeneous buffers, and the ordinary observation

Research deduction, 5 November 2026. This note concerns the original
finite matrices. It gives an exact limitation of homogeneous-three
trace tests and two observation estimates. It proves no vanishing of
an actual mixed-word coefficient and no new open-source asymptotic.

## 1. The original rank-one insertion

Fix \(N\ge2\), put \(D=N-1\), \(q=e^{\pi i/N}\), and
\(\kappa=q^{D^2/2}\). Let \(M\) be the original Newton crossing,
\(J\) index reversal, and
\[
 A_n=JM^n,\qquad H=M^*M>0,\qquad
 W=A_{n_1}\cdots A_{n_m},\quad n_j\in\{3,4\}.
 \tag{1}
\]
Here \(X^*\) is conjugate transpose, while \(X^T\) is transpose.
The ordinary vector is \(v(z)=(e_0(z),\ldots,e_D(z))^T\), where
\[
 e_l(z)=\frac{\prod_{a=0}^{l-1}(2\cos((2a+1)\pi/N)-z)}{S_l^2},
 \qquad S_l=\prod_{a=1}^l2\sin(\pi a/N),\quad S_0=1.
 \tag{2}
\]
These are the full degree-\(D\) polynomials, at both level parities.
The [positive-three similarity](research_positive_three_crossing_cycle.md),
equations (4)--(7), gives
\[
 \widetilde W:=MWM^{-1}
   =\kappa^m\prod_{j=1}^m HM^{n_j-3}.
 \tag{3}
\]
For arbitrary ordinary colors \(z,w\), define the actual cap insertion
\[
 Q= Mv(w)v(z)^TM^{-1}.
 \tag{4}
\]
Then, exactly,
\[
 C_N(z,w):=v(z)^TWv(w)=\operatorname{tr}(\widetilde WQ),\qquad
 \operatorname{tr}(A_3^kW)
       =\kappa^k\operatorname{tr}(H^k\widetilde W).
 \tag{5}
\]
For the first equality, cycle the factors inside the trace; for the
second use \(MA_3M^{-1}=\kappa H\). The same formulas hold with
ordinary derivatives of either \(v\). No conjugate is inserted into
the physical observation. In particular \(Q\) need not be Hermitian.

The [full cyclic theorem](research_mixed_full_cyclic_period.md) controls
the second quantity for each fixed \(k\) and word. It does not state a
marked-trace theorem for (4), or uniformity when \(k\) grows with \(N\).

## 2. What all homogeneous buffer tests miss

Write \(H=\sum_\lambda\lambda\Pi_\lambda\) for its orthogonal spectral
resolution, grouping equal eigenvalues. Every buffer trace in (5)
depends only on the numbers
\(\operatorname{tr}(\Pi_\lambda\widetilde W)\). It contains no
off-diagonal block of \(\widetilde W\) between distinct eigenspaces.
When an eigenspace has dimension greater than one, the tests retain
only its block trace. Thus even \([H,Q]=0\) would not imply that
\(Q\) is a polynomial in \(H\).

**Proposition 1.** If \([H,Q]\ne0\), there is a matrix \(X\) such that
\[
 \operatorname{tr}(H^kX)=0\quad(k\ge0),\qquad
 \operatorname{tr}(XQ)=\|[H,Q]\|_{\mathrm{HS}}^2>0.
 \tag{6}
\]
One may take \(X=[H,[H,Q^*]]\), where \([B,C]=BC-CB\).

*Proof.* The trace of a commutator with \(H\), multiplied by any power
of \(H\), is zero. Put \(Z=[H,Q]\). Since \(H=H^*\),
\([H,Q^*]=-Z^*\). Cyclicity gives
\[
 \operatorname{tr}([H,[H,Q^*]]Q)
   =\operatorname{tr}([H,Q^*][Q,H])
   =\operatorname{tr}(Z^*Z).
 \tag{7}
\]
This proves both statements. \(\square\)

The hypothesis occurs for the actual complete ordinary vector already
at \(N=3\). The exact calculation in
[the positive-three note, Section 7](research_positive_three_crossing_cycle.md)
has \(v(-2)=(1,1,0)^T\) and three distinct eigenvalues of
\(\kappa^{-1}A_3\), with three nonzero spectral weights. Hence \(v\)
is not an \(A_3\) eigenvector. Since \(v^Tv=2\ne0\), commutation of
\(A_3\) with \(vv^T\) would force \(A_3v\) to be proportional to \(v\).
Similarity therefore gives \([H,Q]\ne0\).

The matrix \(X\) in (6) is an algebraic test matrix, **not an asserted
mixed word**. Thus (6) rules out reconstruction of the ordinary
functional from homogeneous-buffer trace functionals on the whole
matrix space. It does not prove a counterexample within the specified
word family, or rule out additional identities of that family.

For any polynomial \(P\), the exact error and elementary bound are
\[
 C_N-\operatorname{tr}(\widetilde WP(H))
   =\operatorname{tr}(\widetilde W(Q-P(H))),\qquad
 |\text{error}|\le\|\widetilde W\|\,\|Q-P(H)\|_1.
 \tag{8}
\]
Here \(\|\cdot\|\), \(\|\cdot\|_1\), and
\(\|\cdot\|_{\mathrm{HS}}\) denote operator, trace, and
Hilbert--Schmidt norms. Since \(P(H)\) commutes with \(H\),
\[
 \|Q-P(H)\|_1\ge\frac{\|[H,Q]\|_1}{2\|H\|}.
 \tag{9}
\]
This is a limitation of matrix-norm approximation, not a lower bound
on its pairing with the particular \(\widetilde W\).

## 3. A source-adapted off-diagonal reduction

Set
\[
 Q_{\rm diag}=\sum_\lambda\Pi_\lambda Q\Pi_\lambda,\qquad
 B_Q=\sum_{\lambda\ne\mu}
        \frac{\Pi_\lambda Q\Pi_\mu}{\lambda-\mu}.
 \tag{10}
\]
This is an exact finite sum; distinct eigenvalues have nonzero
denominator. Then
\[
 Q-Q_{\rm diag}=[H,B_Q],\qquad
 \boxed{\ C_N-\operatorname{tr}(\widetilde WQ_{\rm diag})
       =\operatorname{tr}([\widetilde W,H]B_Q).\ }
 \tag{11}
\]
Thus the required error can be estimated on the actual transported
source, rather than by approximating \(Q\) uniformly on all matrices.
If \(F_j=HM^{n_j-3}\), the product rule gives
\[
 [\widetilde W,H]
   =\kappa^m\sum_{j:n_j=4}
        F_1\cdots F_{j-1}\,H[M,H]\,F_{j+1}\cdots F_m.
 \tag{12}
\]
Only original type-four insertions occur. In particular the
off-diagonal term is exactly zero for a homogeneous-three word.
For a general word, (11) bounds its absolute value by
\(\|[\widetilde W,H]\|\,\|B_Q\|_1\), or by the sum of the
individual absolute observations in (12). No smallness of these terms
or lower bound on the diagonal term is asserted. Small spectral gaps
can make \(B_Q\) large. Even in the homogeneous-three case, the
diagonal weights of the actual cap have different phases, as the
same \(N=3\) calculation explicitly shows.

## 4. A quantitative buffered observation criterion

Suppose \(W=A_3^aVA_3^b\), with \(a,b\ge1\), and set
\(\widetilde V=MVM^{-1}\). Suppose also that the largest eigenvalue
\(L\) of \(H\) is simple, with projection \(P_0\), and put
\[
 B=H/L,\quad \eta=\|B-P_0\|<1,\quad
 q_0=\operatorname{tr}(P_0Q),\quad
 v_0=\operatorname{tr}(P_0\widetilde V),\quad
 d_k=\operatorname{tr}(B^k)-1.
 \tag{13}
\]
The trace-norm operator limit in
[the positive-three theorem, equations (12)--(14)](research_positive_three_crossing_cycle.md)
has simple eigenvalues \(\varrho^{j+1/2}\), where
\(\varrho=(5-\sqrt{21})/2\). It therefore supplies simplicity and a
uniform \(\eta<1\) for all sufficiently large \(N\). Direct expansion of
\(B^a=P_0+(B^a-P_0)\) and its right-hand analogue gives
\[
 \begin{split}
 |\kappa^{-a-b}L^{-a-b}C_N-q_0v_0|
 &\le\|\widetilde V\|\,\|Q\|_1
       (\eta^a+\eta^b+\eta^{a+b}),\\
 |\kappa^{-a-b}L^{-a-b}\operatorname{tr}(W)-v_0|
 &\le\|\widetilde V\|\,d_{a+b}.
 \end{split}
 \tag{14}
\]
The second line uses cyclicity and positivity of
\(B^{a+b}-P_0\). Subtraction therefore proves
\[
 \boxed{\ |C_N-q_0\operatorname{tr}(W)|
 \le L^{a+b}\|\widetilde V\|
 \left[\|Q\|_1(\eta^a+\eta^b+\eta^{a+b})
            +|q_0|d_{a+b}\right].\ }
 \tag{15}
\]
This is a sufficient transfer criterion with the original cap intact:
if its right side is \(o(|q_0\operatorname{tr}(W)|)\) and \(q_0\ne0\),
the buffered ordinary coefficient inherits the marked leading term.
Neither condition is supplied by the unmarked cyclic theorem.
In particular a polynomially accurate operator limit need not resolve
an exponentially small cap overlap. The
[actual cap spectral estimates](research_positive_three_crossing_cap_seed.md)
exhibit precisely this scale issue for specified positive cap states;
they do not identify those states with the ordinary vector in (4).

## 5. A bound using the actual physical endpoint data

There is an all-parity upper bound for the omitted observation.
Write \(k_4=\#\{j:n_j=4\}\),
\[
 c=2\int_0^{5/6}\log(2\sin\pi t)\,dt,\qquad
 M_\infty=4G_{\rm Cat}/\pi,
 \tag{16}
\]
where \(G_{\rm Cat}\) is Catalan's constant. The full physical
value-and-normal estimates in
[the positive-three note, Proposition 8](research_positive_three_crossing_cycle.md)
give, uniformly for real ordinary colors in \([-2,2]\),
\[
 \|v(z)^TM^{-1}\|\le C N^a e^{NM_\infty/2},\qquad
 \|Mv(w)\|\le C N^a e^{N(c+M_\infty/2)}.
 \tag{17}
\]
For the first inequality one uses the exact physical identities for
inverse multiplication and then the full Hermite interpolation of the
vector polynomial. It is not an off-grid eigenvector assertion.
The second follows from the same boundary-vector bound and
\(\|M\|=O(e^{Nc})\). Fixed ordinary derivatives only change a power
of \(N\).

Consequently \(\|Q\|_1\le CN^a e^{N(c+M_\infty)}\).
Spectral pinching is contractive in trace norm, so
\(\|Q-Q_{\rm diag}\|_1\le2\|Q\|_1\). Combining this with (3) and
\(\|H\|=\|M\|^2\) proves
\[
 \left|C_N-\operatorname{tr}(\widetilde WQ_{\rm diag})\right|
 \le C N^a
       \exp N\{(2m+k_4+1)c+M_\infty\}.                 \tag{18}
\]
This saves one crossing-norm factor compared with treating
\(v(z)^TM^{-1}\) by an arbitrary matrix norm. It is a bound for
the actual observation, with all physical normals retained. Its
exponent has not been shown below the local open geometric action,
so it supplies no noncancellation conclusion. A sharper estimate of
the actual commutator observations in (12), rather than of their
ambient matrix norms, is the concrete remaining target in this route.

The complementary estimates (11), (15), and (18) are exact finite-level
targets for an observation argument. The existing
[mixed positive-metric obstruction](research_mixed_three_four_operator_obstruction.md)
and [original overlap examples](research_original_almost_invariance_and_observation.md)
preclude discarding their cap factors or treating every type-four
insertion as positive. No finite exceptions, knot closure, or complete
open-source lower bound follows here.

The [ordinary Casimir-mark deduction](research_mixed_ordinary_boundary_casimir_mark.md)
gives a more specific representation at the complete physical color:
an exact Fejér idempotent at odd levels, and an explicitly forced
resolvent observation at even levels.
