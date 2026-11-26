# Selected first-prefix bounds over the full real color period

Research deduction, 6 November 2026. The complete-color five-profile
upper envelope for the selected first type-four cap also bounds its
literal polynomial at every real ordinary color. Consequently the
completed first-only and first-two-selected prefix comparisons retain
their gaps on the full real color period. The proof uses the whole
endpoint coefficient and its physical-row bounds; it assumes no
positivity or modulus domination for a canceled cap sum.

## 1. The literal cap and its original five profiles

Put \(q=e^{\pi i/N}\), \(r=q^{-2}\), \(P_i=(r;r)_i\), and
\(p_i(X)=(rX;r)_i\). Keep the original cap
\[
 U_{1,N}(w,X)=\sum_{i=0}^{N-1}
                \frac{H_N(w,r^{-i})p_i(X)}{P_i^2}.
 \tag{1}
\]
All Newton factors, ordinary-color normalizations and both level
parities are those in the exact source. Fix an actual first-four
reference of a word of length at least three. Its original private
height is \(h_e=\Im e_*\). Let
\[
 P=[.22,.45],\qquad z=y+iH,\qquad
 H\in\{7/625,1/100\},\qquad y\in P.
 \tag{2}
\]
These are exactly the selected heights of the completed first-only
comparisons and the simultaneous first-two comparison.

Use the original complete-color phase
\[
 \Psi(e,z)=S(e)+J(e+z)-J(z)-i\pi ez-g(e)
 \tag{3}
\]
and the same five real upper profiles as the
[selected-cap finite reduction](research_mixed_selected_four_three_finite_reduction.md),
equation (6):
\[
 \begin{split}
 A_0(y)&=\max_{.27\le x\le.49}\Re\Psi(x+ih_e,z),\\
 A_L(y)&=\Re\Psi(.27,z),\qquad
 A_R(y)=\Re\Psi(.49,z),\\
 A_-(y)&=\max_{.27\le x\le.49}\Re\Psi(x-.055i,z)-.11\pi,\\
 A_+(y)&=\max_{.27\le x\le.49}\Re\Psi(x+.04i,z)-.08\pi,\\
 \mathcal A_H(y)&=\max(A_0,A_L,A_R,A_-,A_+).
 \end{split}
 \tag{4}
\]
The private real cuts have height zero. None is replaced by a
main-height value or by a far-color critical point.

**Theorem 1.** For every \(\eta>0\), uniformly on the actual
reference families and (2),
\[
 |U_{1,N}(-2\cos\theta,e^{-2\pi iz})|
       \le C_\eta N^{a_\eta}
                e^{N\{\mathcal A_H(y)+\eta\}},
       \qquad -\pi\le\theta\le\pi.
 \tag{5}
\]
This is an upper envelope for the unchanged signed source (1).
It does not compare its modulus to
\(|U_{1,N}(-2,e^{-2\pi iz})|\).

*Regular currents.* The original exact interpolation in the
[cap contour theorem](research_mixed_cap_outer_contour_reduction.md),
equation (4), is
\[
 D_N(e)^{-1}\mathcal C_N(e,w)\,
   \frac{\widehat P_N(N(e+z))}
        {\widehat P_N(Nz)\widehat P_N(Ne)}.
 \tag{6}
\]
It equals the literal summand of (1) on every retained physical
index. Its zero-mode residue coefficient is \(+N\).
Only the complete coefficient \(\mathcal C_N(e,w)\) depends on
the ordinary color. Theorem 1 of
[endpoint real-color decay](research_mixed_endpoint_real_color_decay.md)
bounds that entire coefficient, including revived Newton rows, by
\[
 |\mathcal C_N(e,-2\cos\theta)|
   \le C N^a
       e^{N\{\Re S(e)-c(1-\cos\theta)\}},
 \quad e\in[.27,.49]+i[-.055,.04].
 \tag{7}
\]
Its normalization is the one used in (6); the exact
\(H_N=G_N\mathcal C_N\) identity and the \(D_N\) conversion
are retained, not replaced by a leading asymptotic term.

Drop the favorable angular loss in (7) and insert the remaining
upper into each current of the exact residue identity. All other
factors are color independent, so the upper phase is precisely (3).
The same complete-color vertical convexity, real-cut endpoints and
linear alias penalties therefore give (4), including every join
and both halves of every vertical alias. These arguments apply to
the upper phase, not to the logarithm or Hessian of a far-color
finite source. Poles, normal terms, signs and half-grid cuts of
the original identity are unchanged.

*Compact physical tails.* The physical-index assertion of endpoint
real-color decay applies uniformly on every compact subinterval
of \((0,1)\). In particular the remaining compact tails have the
same complete-color rate
\[
 R_1(t,z)=\Re S(t)+
       \int_0^t\log|1-e^{2\pi H-2\pi i(y+x)}|\,dx-J(t).
 \tag{8}
\]
At positive height the exact numerator reflection is
\[
 \int_0^t\log|1-e^{2\pi H-2\pi i(y+x)}|\,dx
 =2\pi Ht+
   \int_0^t\log|1-e^{-2\pi H-2\pi i(y+x)}|\,dx.
 \tag{9}
\]
The term \(2\pi Ht\) is retained: this cap has no incoming
monomial that could cancel it. The monotonicity proof in Section 2
of the selected-cap reduction bounds these compact tails by their
original real anchors \(A_L,A_R\). It is a property of (8), so
it remains valid after the real-color coefficient upper is inserted.
No monotonicity of a new color-dependent phase is required.

*Extreme physical rows.* For \(i/N\le.01\), exact physical support
gives Newton indices \(l/N\le i/N<1/2\). The zero-safe Newton
bound \(V_\theta\le V_0\) on that lower half preserves the old
endpoint estimate, including
\(|p_i(X)|\le(1+e^{.042\pi})^i\); its rate ceiling is \(1/4\).

For \(i/N=1-\delta\ge.99\), use the physical entropy inequalities
of endpoint real-color decay, equations (5) and (15). Below one
half, \(V_\theta\le V_0\); above one half use only
\(V_\theta\le0\). Thus the common endpoint entropy ceiling is
still less than \(3/5\). The stronger negative complete-color
upper-half entropy is not used. Exact factorial reflection and
the literal identity
\[
 p_i(X)=\frac{1-X^N}{\prod_{j=i+1}^N(1-r^jX)}
 \tag{10}
\]
give the same bound as the selected reduction:
\[
 |p_i(X)|\le2e^{2\pi NH}(20/19)^{N-i},\qquad
 \frac35+2\pi H+\frac1{100}\log(40/19)<\frac34.
 \tag{11}
\]
The residual reciprocal factorial has nonpositive rate in this
sector. These are bounds for the original sums; no physical
Newton row is deleted because it vanishes at a different color.
Both endpoint ceilings are below \(A_0>199/250\), by the
selected reduction and its
[wider original-height proof](research_mixed_selected_four_three_last_rows.md),
Section 5. That proof uses the actual first-cap reference and
complete-color phase only.

Thus all compact and extreme tails have the same original
profile upper, or a constant already absorbed by \(A_0\).
Adding finitely many original currents and rows, with one total
tolerance, proves (5). \(\square\)

## 2. The completed selected prefix gaps are unchanged

Every other factor in the completed prefix products is independent
of the ordinary left color. Their complete selected weights are
also independent of it. Therefore (5) replaces precisely the
small-color cap-envelope input in each finite reduction, leaving
all already proved profile comparisons and original affine terms
unchanged.

**Corollary 2.** At every real \(w_L\in[-2,2]\), with the exact
source domains, targets, outgoing halfweights and marginals of
the following theorems, their raw local deficits remain:

| Selected prefix | Raw deficit | Original theorem |
|---|---:|---|
| First position, next type three, height \(7/625\) | \(1/2000\) | [First-four/next-three full product](research_mixed_selected_four_three_full_product.md) |
| First position, next type four, height \(1/100\) | \(1/2000\) | [First-four/next-four full product](research_mixed_selected_four_four_full_product.md) |
| First two positions, next type three or four, both heights \(1/100\) | \(3/1000\) | [Double-selected plateau completion](research_mixed_double_selected_plateau_completion.md), Section 1 |

For example the last row states, for every \(\eta>0\),
\[
 \begin{split}
 &|U_{1,N}(w_L,X_1)C_{1,N}(X_1,X_2)
      C_{\beta,N}(X_2,X_3)
      d_N(X_1)X_1^{-N}d_N(X_2)X_2^{-N}|
                          |d_N(X_3)|^{\beta/2}\\
 &\hspace{12mm}\le C_\eta N^{a_\eta}
       e^{N\{\Lambda_{123}-3/1000+\eta\}},
 \qquad w_L\in[-2,2],\quad\beta=0,1 .
 \end{split}
 \tag{12}
\]
Both complete-weight alternatives at each selected node remain.
Their branch restrictions are pointwise inequalities for the
complete weights, not deletions of source summands.

In particular all cap/right-cut and alias reductions, the joint
ordinary last-row comparison, and the 17,728 main/left-cap
comparisons from the double-selection theorem refer to the same
complete-color profiles as before. No separate comparison of the
absolute values of two complex cap sums is involved.

Every fixed ordinary-color derivative has the same exponent with
a larger polynomial factor. For fixed targets the holomorphic
integer-weighted product is a polynomial in \(w_L\) of degree at
most \(N-1\). The degree/Laurent maximum principle followed by
Cauchy on circles of radius \(N^{-2}\) transfers a uniform real
interval bound to its fixed derivatives with polynomial cost,
including the ramification points \(w_L=\pm2\). Allocate the
color-independent outgoing modulus halfweight after differentiation.
The previous fixed small complex disks also remain available;
no full-width complex strip is inferred merely from (5).

## 3. Consequence for the already defined partial plateau source

Use exactly the selection set, contours and polynomial
\(\mathcal Z_N^{\mathrm{first\ two+int}}\) of the double-selected
plateau completion. If position one is selected, Corollary 2
supplies its prefix estimate over all real left colors.
If it is unselected, equation (14) of endpoint real-color decay
supplies the original first-cap supporting-plane upper over that
period, including in the second-only selected comparison.
The other factors retain their established color-independent
bounds. The unselected terminal factor has its completed
[real-color supporting-plane bound](research_mixed_terminal_real_color_decay.md).

Hence every nonempty permitted selected sector has its same
common finite gap \(1/6400\) over the full real color square.
The genuine unselected plateau has its established outside-angle
gap \(\delta_\rho>0\). Finite summation and the triangle inequality
give the real boundary gap
\[
                     \min(\delta_\rho,1/6400)
 \tag{13}
\]
for this enlarged restricted polynomial. Its original small-color
nonzero packet, normalization, degree bound and parities are
unchanged. The
[open-source stability lemma](research_mixed_open_source_stability_reduction.md)
therefore supplies the corresponding fixed thin angular-strip
bound for this same restricted polynomial.

The local real-color estimates also pass through any already
justified disjoint left/right window assembly, with its original
halfweights, tangent cancellations and minimum of local gaps.
They do not resolve overlapping windows, missing selected sets,
nonplateau sectors, or the calibrated complement estimate for
the entire open source. No whole-word or new knot-family theorem
is concluded.
