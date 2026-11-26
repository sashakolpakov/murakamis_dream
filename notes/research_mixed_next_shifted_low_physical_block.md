# The lower physical block on a displaced incoming segment

Research deduction, 7 November 2026. The product of the two lower
physical row groups in the original selected first-three source has
the same strict affine bound on the entire displaced horizontal
segment \(1/2+i h_a\) to \(7/10+i h_a\). This transports positive
row bounds already supplied by the original source proof. It does
not transport an estimate of a cancelling cap or conditional sum.
No numerical evaluation or replay is used.

## 1. Fixed rows and the actual reference

Use the ordinary-next canonical family of
[the selected right-segment theorem](research_mixed_second_selected_first_three_right_segment.md),
Sections 1--2:
\[
 (a_*,u_*,z_*,v_*,b_*)=(r_1,s_2^*,r_2,s_3^*,r_3),
 \qquad(\epsilon_1,\epsilon_2,\epsilon_3)=(0,1,\beta),
 \qquad\beta\in\{0,1\}.
 \tag{1}
\]
Both conditional indices are ordinary. Keep its actual external
coordinate \(s_4^*\), its original action and marginal, and its
affine target \(\Lambda_{123}(b)\). In particular
\[
 h=h_a=\Im a_*\in(-9/125,0),\qquad
 P=[11/50,9/20],\quad H=1/100.
 \tag{2}
\]
No independent enlargement of the reference boxes is made.

Write
\[
 \begin{gathered}
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad
 p_j(X)=(rX;r)_j,\quad X_x=e^{-2\pi i(x+ih)},\\
 z=y+iH,\quad b=w+i\Im b_*,\quad
 Y=e^{-2\pi iz},\quad Z=e^{-2\pi ib},\quad y,w\in P .
 \end{gathered}
 \tag{3}
\]
The fixed physical sets are
\[
 \mathcal J_N=\{0\le j<N:j/N\le27/100\},\qquad
 \mathcal K_N=\{0\le k<N:k/N\le3/40\}.
 \tag{4}
\]
They do not depend on the transported coordinate \(x\). Define the
literal lower factors and their positive row sums by
\[
 \begin{split}
 U_N^-(\omega,X)
   &=\sum_{j\in\mathcal J_N}H_N(\omega,r^{-j})p_j(X)/P_j,\\
 C_N^-(X,Y)
   &=\sum_{k\in\mathcal K_N}X^{-k}p_k(X)p_k(Y)/P_k^3,\\
 A_N(\omega,X)
   &=\sum_{j\in\mathcal J_N}
                |H_N(\omega,r^{-j})p_j(X)/P_j|,\\
 B_N(X,Y)
   &=\sum_{k\in\mathcal K_N}
                |X^{-k}p_k(X)p_k(Y)/P_k^3|.
 \end{split}
 \tag{5}
\]
Each \(H_N\) is its whole coherent endpoint polynomial; no modulus
is taken inside its own Newton sum. Put
\[
 W_{\beta,N}(Y,Z)
   =|d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)|\,|d_N(Z)|^{\beta/2}.
 \tag{6}
\]
For \(\beta=0\) the last factor is identically one, including at
zeros of \(d_N\). The complete third conditional polynomial and
both Fourier alternatives are retained.

**Theorem.** For every prescribed \(\tau>0\), all sufficiently large
\(N\), both parities, and uniformly on (1)--(3),
\[
 \boxed{\quad
 A_N(\omega,X_x) B_N(X_x,Y) W_{\beta,N}(Y,Z)
 \le C_\tau N^{M_\tau}
       e^{N\{\Lambda_{123}(b)-1/400+\tau\}},
 \quad \frac12\le x\le\frac7{10},\quad -2\le\omega\le2 .
 \quad}
 \tag{7}
\]
In particular (7) bounds the modulus of the product with \(U_N^-\)
and \(C_N^-\) in place of their positive row sums. After choosing
the tolerance and absorbing polynomial factors, the finite gap
can be \(1/800\). Fixed ordinary-color derivatives and small
complete-color neighborhoods have the same rate with their
usual polynomial costs and prescribed tolerance.

## 2. The starting bounds are positive row bounds

Let \(a_0=1/2+ih\), and retain the original cap plane
\[
 B_U(1/2)=
 \Re T_0(a_*)-\Re p_L(1/2-\Re a_*)
       -\frac1{2500000}(1/2-\Re a_*)^2 .
 \tag{8}
\]
The actual attached equation is \(T_0'(a_*)+p_L=0\).

The compact physical-tail proof of the
[real-color envelope, Section 1](research_mixed_boundary_window_real_color_envelopes.md),
equations (8)--(9), estimates the modulus of each complete endpoint
coefficient before the positive sum over physical private rows.
For the present type-three cap its row rate is
\[
 R_0(e,a_0)=\Re S(e)+
       \int_0^e\log|1-e^{-2\pi i(a_0+s)}|\,ds .
 \tag{9}
\]
The [upper-target extension, Theorem 2](research_mixed_cap_upper_target_extension.md)
extends that very same lower-tail proof to \(\Re a_0=1/2\).
On \(0<e\le.27\) the smoothed incoming radius exceeds \(1/2\),
and the doubled-angle cosine is below \(1/5\). Together with the
original \(\lambda'(.27)>27/50\) and \(\lambda''<0\), this makes
(9) strictly increasing on every compact lower interval.
Its endpoint value is the original real-cut phase
\(\Re\Psi(.27,a_0)\).

The true lower private end has its separate literal rate \(<1/4\);
this is the endpoint estimate in the same envelope proof, not an
extension of a compact complex-index packet to zero. The source
proof therefore gives the positive-sum bound
\[
 A_N(\omega,X_{1/2})
 \le C_\tau N^{M_\tau}
       \exp N\{\max(\Re\Psi(.27,a_0),1/4)+\tau\}.
 \tag{10}
\]
The real-color estimate is coefficientwise in the complete \(H_N\);
it supplies (10) uniformly for \(\omega\in[-2,2]\).

[Complete upper-target cap support, Sections 2--3](research_mixed_cap_upper_target_completion.md)
puts the real-cut profile below \(B_U(1/2)\), and proves
\(B_U(1/2)>149/200>1/4\). Thus
\[
             A_N(\omega,X_{1/2})
             \le C_\tau N^{M_\tau}e^{N\{B_U(1/2)+\tau\}}.
 \tag{11}
\]
This inference uses its real-cut and true-end comparisons separately;
it does not replace a positive tail by the modulus of the whole cap.
The possible row exactly at \(e=.27\) obeys the same continuous
cut-rate estimate.

For the first conditional factor use the original phase
\[
 Q(t;a,z)=g(a+t)+g(z+t)-3g(t)-g(a)-g(z)+2\pi iat .
 \tag{12}
\]
At real \(0<t\le3/40\), Section 5 of the
[selected right-segment proof](research_mixed_second_selected_first_three_right_segment.md)
bounds its exact force, including the carrier, from below:
the incoming modulus is at least one, the outgoing modulus exceeds
\(9/10\), and the own denominator is less than \((4/5)^3\).
Consequently the physical row rate strictly increases to \(3/40\).
The zero-safe finite-product bound includes \(k=0\) and any row
exactly at the cut. It gives
\[
 B_N(X_{1/2},Y)
 \le C_\tau N^{M_\tau}
               e^{N\{\Re Q(3/40;a_0,z)+\tau\}} .
 \tag{13}
\]
Again this is a sum of absolute values of physical rows.

Finally, the pointwise moving-cut comparison in Sections 5--6
of that proof pays
\[
 B_U(1/2)+\Re Q(3/40;a_0,z)
 \tag{14}
\]
against every original third-factor source profile and each of the
two full selected-weight alternatives, with raw loss \(1/400\)
relative to \(\Lambda_{123}(b)\). Its cut is exactly
\(\ell(1/2)=23/40-1/2=3/40\). Combining those sourcewise
comparisons, then summing the third factor with its unchanged
norms and currents, proves
\[
 A_N(\omega,X_{1/2})B_N(X_{1/2},Y)W_{\beta,N}(Y,Z)
 \le C_\tau N^{M_\tau}e^{N\{\Lambda_{123}(b)-1/400+\tau\}}.
 \tag{15}
\]
All finite tolerances in (10)--(15) are chosen inside one total
prescribed tolerance. No cancellation in either initial outer
row sum is needed for (15).

## 3. Exact transport of both physical groups

Apply [fixed-height row contraction](research_incoming_fixed_height_row_contraction.md),
Proposition 1, with
\[
                  d_1=1/5,\qquad \eta=3/100 .
 \tag{16}
\]
For the cap rows,
\[
 d_1+j/N\le1/5+27/100=47/100=1/2-\eta,
 \tag{17}
\]
and the same condition holds for the smaller conditional set.
The original products are nonzero on this incoming range, even
at \(h=0\); the original endpoint coefficients or outgoing factors
may still vanish, and their zeros are kept.

Use \(m=0\) for the cap and \(m=1\) for the conditional carrier.
Every factor independent of \(x\) stays fixed. Proposition 1 gives
the exact inequalities at every level
\[
 A_N(\omega,X_x)\le A_N(\omega,X_{1/2}),\qquad
 B_N(X_x,Y)\le B_N(X_{1/2},Y),
                    \quad 1/2\le x\le7/10 .
 \tag{18}
\]
More precisely each row retains the explicit contraction in
equation (4) of that proposition; the zero row has contraction
one. The third factor and both selected weights are unchanged
in this transport. Equations (15)--(18) prove (7).

No positivity of the complex diagonal quotient is asserted.
Only its modulus is used, on positive sums for which the original
initial source bound has just been established.

## 4. Derivatives, the original measure, and remaining rows

The physical-index endpoint theorem supplies the all-real bounds
for each complete \(H_N\) separately. Markov on those polynomials,
before the positive sum, gives fixed ordinary derivatives in
(10)--(11) with polynomial costs. Their established small
complete-color disks give the corresponding complex-color
upper estimates. The other factors are color independent, so
(18) preserves these conclusions without changing a denominator,
carrier, or ordinary observation.

The row sets (4) remain fixed. At any fixed base reference the
strict angular margin (17) and the zero-safe product bounds
permit small fixed neighborhoods of the outside variables.
Keep the reference heights, original suffix contours, and
affine normalization fixed at that base when taking derivatives.
The original complete third-factor estimate has the same local
persistence. After an arbitrarily small rate allowance, Cauchy's
formula gives the usual fixed mixed derivatives of the literal
integer-weighted truncated product. No modulus halfweight is
differentiated or divided out on the whole outgoing plateau.
Near its actual nonzero outgoing reference, the same permitted
normalization as in the selected right-segment theorem applies.

The exact contribution on the displaced first-coordinate segment is
\[
 N\int_{1/2}^{7/10}
 U_N^-(\omega,X_x)C_N^-(X_x,Y)
       d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)\,dx .
 \tag{19}
\]
Here \(a=x+ih\), so \(da=dx\); no factor of \(i\) is inserted.
Equation (7) bounds (19), with its original outgoing halfweight.
The second selected integral, if taken, keeps its own factor \(N\).
The two densities and bounded path lengths cost only polynomial
factors.

This is a bound for the low/low block (4), not for either complete
first factor. The mixed and upper row groups, their coherent contour
currents, and the new far vertical connector remain in any full
contour replacement. Nothing here identifies a physical row set
with a continuous arc, removes a Fourier sector, or proves a
complete \(343\) or \(344\) asymptotic.

