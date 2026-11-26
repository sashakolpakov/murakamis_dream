# The sign of the terminal height-transport fee

Research deduction, 6 November 2026. At an actual type-four incoming
leg, the allocated marginal of either complete terminal transform has
strictly positive imaginary part. Consequently the proved transport
from a negative reference height towards zero, or to a selected
positive height, leaves a positive fee relative to its original complex
affine plane. This identifies a term that an adjacent comparison must
pay. It is not a counterexample to a joint source bound.

## 1. Original terminal notation and marginal

Fix a mixed open word of length \(m\ge2\), with terminal type
\(3+\epsilon\), where \(\epsilon\in\{0,1\}\). Let
\(a_*=A+ic\) be its incoming nonprivate leg, of type four.
It is the preceding ordinary right leg when \(m\ge3\), and
the opposite endpoint's attached leg when \(m=2\).
The reduced-disk inclusion in
[local factor coverage, Section 1](research_mixed_open_local_factor_coverage.md)
and the original typed height bounds give
\[
                 .24<A<.36,\qquad -.108<c<-.001.
\tag{1}
\]
Write \((e_*,t_*,u_*)\) for the terminal endpoint root, in
private, attached, auxiliary order, and put \(v=\Re t_*\).
The [endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md)
give, for either terminal type,
\[
                .246<v<.391,
       \qquad -.108<\Im t_*<.021.
\tag{2}
\]
Here \(t_*\) is the attached transform-index coordinate, not
the private endpoint leg. For type three this identification also
follows from the off-shell elimination in
[the terminal critical curve, Section 2](research_mixed_terminal_three_critical_curve.md).

The original terminal action \(P_\epsilon\), before the incoming
halfweight, is equation (3) of
[the terminal tail theorem](research_mixed_terminal_transform_tails.md).
Its dependence on the external variable, before critical elimination,
is exactly
\(g(a+t)-g(a)+2\pi iat\). Critical stationarity therefore gives
\[
 \begin{split}
 P_\epsilon'(a_*)&=g'(a_*+t_*)-g'(a_*)+2\pi it_*,\\
 \Pi_\epsilon&=P_\epsilon-g/2,\qquad
 p=\Pi_\epsilon'(a_*)
   =g'(a_*+t_*)-\frac32g'(a_*)+2\pi it_*.
 \end{split}
\tag{3}
\]
The incoming allocation is determined by its type four, independently
of the terminal own type \(\epsilon\). The primitive retains its
original lift \(g'(w)=\operatorname{Log}(1-e^{-2\pi iw})\).
In particular \(.486<\Re(a_*+t_*)<.751\), so the displayed
sum remains in the original regular strip.

## 2. A strict positive marginal

**Proposition 1.** At every reference just specified,
\[
                           \Im p>\frac{7\pi}{100}.
\tag{4}
\]

*Proof.* For \(0<x<1\) and real \(h\), set
\(\mathcal A(x,h)=\arg(1-e^{2\pi h-2\pi ix})\), on the
original lift. The radius-angle bounds proved in
[the alias argument lemma, Section 2](research_mixed_horizontal_alias_transport.md)
are
\[
 \pi\min(1-2x,0)\le\mathcal A(x,h)
                 \le\pi\max(1-2x,0).
\tag{5}
\]
For \(0<A<1/2\), the argument is strictly increasing in the
positive radius: its radius derivative is
\(\sin(2\pi A)/(1-2r\cos(2\pi A)+r^2)>0\).
Since \(c<0\), its radius is below one. Evaluation at radius
one gives
\[
              0<\mathcal A(A,c)<\pi(1/2-A).
\tag{6}
\]
Equation (3) now reads
\[
 \Im p=\mathcal A(A+v,c+\Im t_*)
              -\frac32\mathcal A(A,c)+2\pi v.
\tag{7}
\]
If \(A+v\ge1/2\), equations (5)--(6) imply
\[
 \Im p>\pi\{1-2(A+v)-\tfrac32(1/2-A)+2v\}
          =\pi(1/4-A/2)>7\pi/100.
\tag{8}
\]
This includes equality \(A+v=1/2\), where the first argument
is zero. If \(A+v<1/2\), that first argument is positive,
and (1)--(2), (6) give instead
\[
 \Im p>\pi(2v-3/4+3A/2)
       >\pi(.492-.750+.360)=51\pi/500>7\pi/100.
\tag{9}
\]
These two cases exhaust the original reference domain. \(\square\)

## 3. What the proved finite-source transport does and does not pay

Let \(y\in P=[.22,.45]\), \(d=y-A\), and
\(\kappa=1/2500000\). The horizontal reference plane is
\[
 B_\epsilon(a_*;y)=\Re\Pi_\epsilon(a_*)
                   +\Re p\,d-\kappa d^2.
\tag{10}
\]
The [selected type-three terminal theorem](research_mixed_terminal_three_selected_height_completion.md),
and Theorem 1 and Corollary 2 of
[the common terminal extension](research_mixed_terminal_four_selected_height_completion.md),
bound the whole literal \(V_\epsilon\), with its prescribed
incoming halfweight, by a polynomial times
\(\exp N(B_\epsilon+\tau)\). The unselected range is
\(c\le k\le0\); the selected range is \(0\le k\le.014\).
They retain both Fourier branches, every internal row and current,
both parities, and fixed ordinary-color derivatives. The complete
type-four base source used there is discharged by Corollary 3 of
[the whole unselected plateau theorem](research_mixed_full_unselected_plateau.md).

At the target \(a_k=y+ik\), the original complex affine plane,
with the same real quadratic loss, is
\[
 \Gamma_\epsilon(a_k)
  =\Re\{\Pi_\epsilon(a_*)+p(a_k-a_*)\}-\kappa d^2
  =B_\epsilon(a_*;y)-(k-c)\Im p.
\tag{11}
\]
Thus the existing upper theorem retains the fee
\[
 B_\epsilon-\Gamma_\epsilon=(k-c)\Im p
      >\frac{7\pi}{100}(k-c)>0\qquad(k>c).
\tag{12}
\]
In particular its zero rate allowance *relative to the horizontal
plane* is not a nonpositive allowance relative to the original
complex affine plane.

For \(m\ge3\), let \(\phi\) denote the preceding ordinary
allocated phase. Original stationarity gives \(\phi_b=-p\)
at the incoming terminal leg. Its complex affine term contributes
\(+ (k-c)\Im p\) when that leg's height increases. Summing
that ordinary affine comparison with (10) leaves precisely (12);
the matching negative term would have been present in (11).
At the reference real coordinates all horizontal displacement losses
vanish, so these two upper planes alone exceed the original total
reference value as soon as \(k>c\).

This is an inadequacy of that combination of upper bounds, not a
positive defect for the actual joint finite source. A neighboring
strict loss can pay (12), or a calibrated joint horizontal comparison
can avoid introducing it. The completed
[first-collar theorem, Sections 2--3](research_mixed_first_collar_full_terminal_completion.md)
uses the latter structure and is unaffected. When \(m=2\), the
preceding incidence is the first cap rather than an ordinary factor;
its opposite marginal has the same tangent bookkeeping.

For comparison, a type-three incoming leg has no halfweight and has
\(p=P_\epsilon'(a_*)\). The original angle calculation in
[common terminal height transport, Section 2](research_mixed_terminal_height_transport.md)
gives \(0<\Im p<\pi\). Its supplied horizontal allowance is
\(A_c(k)=0\) when \(c\le0\), and
\(A_c(k)=\pi(c-k)\) when \(c\ge0\). Consequently its
fee relative to the complex affine plane is likewise
\[
 A_c(k)+(k-c)\Im p=
 \begin{cases}
 (k-c)\Im p,&c\le0,\\
 (c-k)(\pi-\Im p),&c\ge0,
 \end{cases}
\tag{13}
\]
strictly positive at a nontrivial attenuation. That comparison keeps
its original real target interval \([.267,.433]\). Neither sign
statement enlarges a target domain or supplies the remaining joint,
selected, taper or full-period open-source estimates.
