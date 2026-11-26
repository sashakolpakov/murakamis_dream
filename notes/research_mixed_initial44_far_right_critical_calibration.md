# Calibrating the conditional critical term on the far right interval

Private written deduction, 10 November 2026. A sharper lower bound for
the original cap comparison plane pays the complete positive cap
envelope against the continued conditional critical exponential.
The incoming coordinate ranges over every compact subinterval of
\([7/8,1)\). This does not replace the conditional finite sum by
its critical exponential.

## 1. The original cap marginal has a sharper elementary bound

Use the actual initial four/four reference of
[the cap-floor theorem](research_mixed_initial44_sharper_half_face_floor.md),
with its unchanged bare cap action \(T\), allocated action
\(L_1=T-g/2\), and constants
\[
 .246<a_0<.350,\qquad r=e^{2\pi c}<9/10,\qquad
 \kappa=1/2500000.
 \tag{1}
\]
The source proves \(\Re T(a_*)>1\). Its equations (7) and (11)
give positive moduli \(N_e,D\) satisfying
\[
 \Re T'(a_*)=\log(N_e/D),\qquad
 N_e^2>1+\frac{324}{625}r^2+\frac{36}{125}r,\qquad
 D^2<1+r^2+\frac65r .
 \tag{2}
\]
These are bounds at the same coupled geometric reference; no
independent cap reference is substituted.

Multiplying the two inequalities in (2) by \(625\) and \(361\)
respectively gives
\[
 625N_e^2-361D^2
 >264-37r^2-\frac{1266}{5}r
 >\frac{123}{20}>0 .
 \tag{3}
\]
For the last comparison the quadratic decreases for \(r\ge0\);
substitution of \(r=9/10\) gives exactly \(123/20\).
Thus \(N_e/D>19/25\).

The required logarithmic estimate has a positive-series proof.
For \(0<t<1\),
\[
 \operatorname{artanh}t
 =t+\sum_{n\ge1}\frac{t^{2n+1}}{2n+1}
 \le t+\frac{t^3}{3(1-t^2)}.
\]
At \(t=3/22\) this implies
\[
 \log(25/19)
 =2\operatorname{artanh}(3/22)
 \le\frac{1434}{5225}<\frac{11}{40}.
 \tag{4}
\]
The final cross-product difference is
\(11\cdot5225-40\cdot1434=115>0\).
Consequently
\[
                    \Re T'(a_*)>-\frac{11}{40}.
 \tag{5}
\]

Keep the original half-face planes
\[
\begin{split}
 B_T&=\Re T(a_*)+\Re T'(a_*)(1/2-a_0)
                       -\kappa(1/2-a_0)^2,\\
 B_*&=\Re L_1(a_*)+\Re L_1'(a_*)(1/2-a_0)
                       -\kappa(1/2-a_0)^2 .
\end{split}
 \tag{6}
\]
Since \(0<1/2-a_0<127/500\), the preceding inequalities give
\[
 B_T>1-\frac{11}{40}\frac{127}{500}-\kappa
          =\frac{18603}{20000}-\kappa .
 \tag{7}
\]
The cap-floor theorem's original convexity argument, its equations
(15)--(16), proves \(B_*\ge B_T\). It concerns the same
normalization and remains unchanged. In particular,
\[
 \boxed{\quad B_*>\frac{223}{240}+\frac1{1200}.\quad}
 \tag{8}
\]
Indeed \(18603/20000-223/240=59/60000\), and subtracting
\(1/1200\) leaves \(3/20000>\kappa\).

## 2. Transport of the original conditional action

Retain the parameters and supporting planes of
[the original action calibration](research_mixed_initial44_lower_right_action_calibration.md):
\[
 b=z+id,\qquad z\in[11/50,9/20],\qquad
 -.102\le d\le-.001,\qquad a_L=1/2+ic.
\]
Write \(\Theta(a,b)\) for the original critical value of
\[
 Q(s;a,b)=g(s+a)+g(s+b)-3g(s)-g(a)-g(b)+2\pi ias .
 \tag{9}
\]
The original calibration, equations (7) and (17), gives
\[
\begin{split}
 \Re\Theta(a_L,b)-\tfrac12\Re g(b)&\le B_R(z),\\
 B_*+B_R(z)&=\Lambda(z)
  -(\kappa+\kappa_R)(1/2-a_0)^2-\kappa_R(z-b_0)^2,
 \qquad \kappa_R=8\kappa/9 .
\end{split}
 \tag{10}
\]
Here \(\Lambda\) is the unchanged affine action of the pair,
and \(b_0\) is the second coordinate of its original reference.

Equation (17) of
[the half-face height theorem](research_mixed_initial44_half_face_height_connections.md)
shows that this same critical action decreases as the incoming
height increases from \(c\) to zero at real part \(1/2\).
The [unit-circle multiplier theorem](research_mixed_four_conditional_unit_multiplier.md)
then shows that it decreases along the whole real interval
\([1/2,1)\). Thus
\[
       \Re\Theta(x,b)\le\Re\Theta(1/2,b)
                         \le\Re\Theta(a_L,b),\qquad 1/2\le x<1 .
 \tag{11}
\]
Only the height segment at \(1/2\) uses the sign of the multiplier's
imaginary part. The later real transport uses its modulus alone.
No vertical monotonicity on the added real arc is assumed.

## 3. The complete cap multiplying the critical exponential

Use the literal cap \(U_{1,N}\), Fourier polynomial \(d_N\), and
outgoing weight from
[the far-right physical-envelope theorem](research_mixed_initial44_far_right_physical_envelope.md).
For \(X=e^{-2\pi ix}\), \(Y=e^{-2\pi ib}\), that theorem gives
\[
 |U_{1,N}(w,X)|\le C_\tau N^{A_\tau}
                    e^{N(223/240+\tau)},\qquad 7/8\le x\le1,
 \tag{12}
\]
uniformly for real ordinary colors \(w\in[-2,2]\), with every
finite cap index retained. Its Fourier estimates retain
\[
 |d_N(X)X^{-N\epsilon}|\le C_{\rho,\tau}N^{A_{\rho,\tau}}e^{N\tau},
 \qquad
 |d_N(Y)|^{1/2}\le C_\tau N^{A_\tau}
                          e^{N(-\Re g(b)/2+\tau)}
 \tag{13}
\]
on \(7/8\le x\le1-\rho\), for each fixed \(0<\rho<1/8\)
and \(\epsilon=0,1\). The selected monomial has modulus one.
Neither Fourier polynomial is divided out.

**Theorem 1.** On those targets, for both level parities and either
first Fourier choice, the complete cap times the original critical
exponential satisfies
\[
\begin{split}
 &|U_{1,N}(w,X)d_N(X)X^{-N\epsilon}|\,|d_N(Y)|^{1/2}
                                           e^{N\Re\Theta(x,b)}\\
 &\quad\le C_{\rho,\tau}N^{A_{\rho,\tau}}
 \exp N\left\{\Lambda(z)-\kappa_R(z-b_0)^2
       -(\kappa+\kappa_R)(1/2-a_0)^2-\frac1{1200}+\tau\right\}.
\end{split}
 \tag{14}
\]
The same assertion holds on the sufficiently small fixed
ordinary-color neighborhoods and for the fixed derivatives of
the cap supplied by the far-right theorem.

*Proof.* Multiply (12)--(13) and use (8), (10), and (11).
Divide the requested total allowance among the finitely many
upper estimates. The ordinary-color continuation changes only
the cap; all other factors are constant multipliers for that
argument. This proves (14). \(\square\)

The theorem includes the complete cap, but only the critical
exponential of the conditional factor. A complete conditional
contour bound, its physical middle rows, and the interval from
\(7/10\) to \(7/8\) require separate comparisons. The result
alone is not a whole-period or knot-volume theorem.

## Direct source versions

| Direct source | SHA-256 |
|---|---|
| research_mixed_initial44_sharper_half_face_floor.md | eeb48098cf6a53eb7e9cee54ec1eb944f5607252e42550fbc69599f4a76c672a |
| research_mixed_initial44_lower_right_action_calibration.md | ef0079ed2c3148db13a24c23e715d9daab6e164b1aff0231de11041613e0106f |
| research_mixed_initial44_half_face_height_connections.md | 4d83ce42628d9dcd9d965be4f75a6538c4a150ec767b436c42847a177eb352f8 |
| research_mixed_four_conditional_unit_multiplier.md | 4d73d90557948056413ef0445cb7754569cbbc03e7ff3f35ecab0f3e9fe8f66f |
| research_mixed_initial44_far_right_physical_envelope.md | a676bfee21df1e78965bb6515a37e0aebd669b6fb4e4cecb2976a8c254cf778d |

All deductions above are hand algebra and analytic inequalities.
No mathematical numerical evaluation, saved-value arithmetic,
test, import, compilation or frozen-source change is used.
Independent full proof and direct-source review is required before
adoption.
