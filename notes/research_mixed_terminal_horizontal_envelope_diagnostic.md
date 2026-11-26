# A coupled test of the selected-terminal horizontal envelope

Research deduction and bounded diagnostic specification, 6 November 2026.
The existing complete terminal theorem supplies a horizontal upper
plane at every selected incoming height. This note derives its exact
joint comparison with the preceding own-four ordinary factor. A simple
original-marginal test can prove that this particular upper envelope
is too large, without evaluating a dilogarithm or optimizing a target.
No outcome of the prescribed diagnostic is asserted here.

## 1. Canonical two-vertex suffix references

Let \(\epsilon\in\{0,1\}\) be the terminal own flag and
\(\beta\in\{0,1\}\) the type of the external incoming leg
\(b\). The intervening ordinary vertex has flag one. In the
original right-end notation, the unknowns are
\[
 q=(e,\xi,t,a,s).
 \tag{1}
\]
Here \(e\) is the terminal private leg, \(\xi\) its ordinary
endpoint coordinate, \(t\) its attached transform index, and
\((s,a)\) the preceding ordinary vertex's two legs. Exact reversal
of the full original critical action gives the same five-variable
system as a left prefix with flags \((\epsilon,1)\), fixed next
external leg \(b\). This uses no identification of finite contour
sectors under reversal.

Write \(j(z)=\Log(2\sin\pi z)\) on the original strip. The
five original, unscaled gradient components are
\[
\begin{split}
 f_e={}&-j(e-\xi)+j(e+t)-\epsilon j(e)
             +i\pi[\xi-t+\epsilon(e-1/2)],\\
 f_\xi={}&2\Log\cos\pi\xi+\Log\sin\pi(e-\xi)
                         -3\Log\sin\pi\xi+i\pi e,\\
 f_t={}&j(e+t)+j(t+a)-(2+\epsilon)j(t)
                         +i\pi[a-e+\epsilon(t-1/2)],\\
 f_a={}&j(a+s)+j(t+a)-3j(a)+i\pi[t-s+a-1/2],\\
 f_s={}&j(a+s)+j(s+b)-3j(s)+i\pi[b-a+s-1/2].
\end{split}
 \tag{2}
\]
For example these differentiate
\[
\begin{split}
 F={}&B(e,\xi)+J(e+t)-\epsilon[J(e)+J(t)]
      +J(a+s)-J(a)-J(s)\\
 &+J(t+a)-2J(t)-2J(a)+J(s+b)-2J(s)-2J(b)\\
 &+i\pi\{e\xi-et+ta-as+sb
  +\tfrac\epsilon2(e^2+t^2-e-t)+\tfrac12(a^2+s^2-a-s)\},\\
 B(e,\xi)&=-2J(1/2-\xi)-3J(\xi)-J(e-\xi).
\end{split}
 \tag{3}
\]
The function (3) is the corresponding principal restriction of the
[original length-three action](research_mixed_open_word_hessian.md),
up to a function of the fixed coordinates. On
\[
 \mathcal D=E\times U\times Q^3,\qquad
 E=[.33,.47]+i[-.09,.08],\quad
 U=[.21,.25]+i[.01,.10],\quad Q=[.23,.45]+i[-.12,.12],
 \tag{4}
\]
its negative real Hessian is greater than \(\mu I_5\), where
\(\mu=6\pi/49\). All logarithms in (2) are on their original
branches throughout a neighborhood of this convex product.

For every \(b\in D_{3+\beta}\), a canonical zero exists before
any numerical proposal: update the disjoint groups
\((e,t,\xi)=\operatorname{endpoint}_\epsilon(a)\) and
\((a,s)=\operatorname{ordinary}_1(t,b)\). The completed
[endpoint](research_mixed_open_word_critical_localization.md) and
[ordinary](research_mixed_cyclic_critical_localization.md) maps make
this a continuous self-map of their original typed disk product.
Brouwer gives a zero and strict accretivity gives uniqueness in (4).
The same argument as the
[prefix residual theorem](research_mixed_prefix_residual_localization.md)
therefore proves
\[
              \|q_0-q_*(b)\|_2\le\|f(q_0;b)\|_2/\mu
                  \qquad(q_0\in\mathcal D).
 \tag{5}
\]
The canonical zero is holomorphic near the closed input disk. The
endpoint image rectangles and full-bidisk ordinary image bounds apply
to it. In particular \(a,s\) have own-four heights in
\((-.102,-.001)\) and real parts in \((.24,.36)\).
This is a canonical suffix, not a claimed realization by a finite
remaining word.

## 2. Exact use of the existing complete terminal bound

Use the definitions of the
[terminal concave envelope](research_mixed_terminal_concave_profile_envelope.md),
Section 5. Put \(a_*=A+ic\),
\(\Pi_\epsilon=P_\epsilon-g/2\),
\(p_T=\Pi_\epsilon'(a_*)\), and \(\kappa=1/2500000\).
The completed
[type-three](research_mixed_terminal_three_selected_height_completion.md)
and [type-four](research_mixed_terminal_four_selected_height_completion.md)
selected-height theorems give the whole-terminal half-allocated rate
\[
 B_T(y)=\Re\Pi_\epsilon(a_*)+\Re p_T(y-A)-\kappa(y-A)^2
                    \qquad(0\le H\le.014).
 \tag{6}
\]
The type-three baseline uses the original endpoint graph over the
whole input disk. The completed type-four baseline has the narrower
[coupled oriented input scope](research_mixed_terminal_four_coupled_source_continuation.md).
The canonical suffix satisfies this scope as well: \(a,s\) lie in
the reduced own-four disk of radius \(.060\), and the
[oriented ordinary image bound](research_mixed_terminal_four_oriented_source_continuation.md)
gives \(\Re a>.259\) when \(\epsilon=1\). In the original
adjacent-block inverse condition, the reconstructed opposite leg and
next external coordinate are exactly \(s\) and \(b\), by (2).
The former is in that reduced own-four disk; each proposed \(b\)
is the center of its required reduced typed disk. Thus no necessary
length-at-least-three inverse exclusion can discard this reference.
No length-two fixed-point claim is needed. The source bounds therefore
apply independently of finite-word realization, with their original
own-four heights retained.
No new unselected reference plane is substituted at height \(H\).

For the literal product
\(C_1(b,a)V_\epsilon(a)d_N(X_a)X_a^{-N}|d_N(X_b)|^{\beta/2}\),
split the complete selected modulus equally. The remaining ordinary
halfweight has rates \(-\Re g(a)/2-\pi H\) and zero.
For an ordinary label \(\rho\) and \(\nu\in\{0,1\}\),
the resulting joint defect envelope is exactly
\[
\begin{split}
 D_{\rho,\nu}={}&B_T(y)+\Re Q_1^\rho(s;b,a)
 -\tfrac\beta2\Re g(b)-\tfrac\nu2\Re g(a)-\pi\nu H\\
 &-\Re\{M_*+p_*(b-b_*)\},\qquad a=y+iH,
\end{split}
 \tag{7}
\]
with the original \(M_*\), \(p_*\) from that envelope's (16).
Each profile (7) is horizontally concave. At the two proposed external
centers \(\Im b_*<0\), so the four affine ordinary last-row
carriers have maximum at \(1_{11}\). Thus only
\(\rho\in\{0,L,R,1_{11}\}\) need be tested: eight profiles
including both halfweight alternatives. This is a complete upper
envelope for the product, not an equality of rates with the source.

**Proposition 1.** The main factorial profile at the legal trial
\(b=b_*\), \(s=s_*\), \(y=A\) satisfies
\[
 D_{0,1}(b_*,s_*,A+iH)
 \ge L(H):=(H-c)\Im p_T-\pi H.
 \tag{8}
\]
Consequently \(L(H)>0\) rules out a negative comparison by (7)
at that reference and height. It does not rule out a comparison by
the exact terminal phases or by the original finite source.

*Proof.* Set \(\psi(a)=Q_1(s_*;b_*,a)-g(a)/2\). The exact
shared-leg equation is \(\psi'(a_*)=-p_T\). At this trial (7)
reduces to
\(\Re[\psi(A+iH)-\psi(a_*)]-\pi H\).
The [ordinary concavity theorem](research_mixed_second_selected_horizontal_concavity.md)
and \(\Re g''(a)>0\) imply
\(\partial_k^2\Re\psi(A+ik)>0\) along the whole segment
\(c\le k\le H\). Its initial height derivative is
\(-\Im\psi'(a_*)=\Im p_T\). Integration gives (8).
The incoming affine term and the real terminal quadratic vanish at
this particular trial, rather than being discarded elsewhere.
\(\square\)

The function \(L(H)\) is affine in \(H\). Hence
\[
 \min\{L(0),L(7/500)\}>0
 \quad\Longrightarrow\quad L(H)>0\quad(0\le H\le7/500).
 \tag{9}
\]
This is a single interval test, not a search for a favorable height.

## 3. One prescribed four-case diagnostic

The [new driver](../experiments/diagnose_mixed_terminal_horizontal_envelope.py)
uses exactly \((\beta,\epsilon)\in\{0,1\}^2\), with
\[
 b_0=7/20-i/100,\qquad b_1=3/10-13i/250.
 \tag{10}
\]
There is one original-log proposal per case, at 80 decimal digits,
at most 30 Newton steps, requested residual \(10^{-55}\), and
60-digit rational saved centers. The fixed initial endpoint triples
\((e,\xi,t)\) are respectively
\((.407+.009i,.230+.063i,.335-.025i)\) and
\((.348-.035i,.225+.036i,.298-.064i)\); both ordinary legs start
at \(.30-.052i\). No alternate seed, input, precision, or retry is
permitted. At 256 bits certify radius \(10^{-30}\) by (5), using
the exact sum of squared rational residual endpoints and an outward
lower bound for \(6\pi/49\). Check every proposed localization
square in (4), as well as the typed endpoint/ordinary image domains,
the reduced typed disks, and \(\Re a>.259\) for \(\epsilon=1\).
Every reconstructed Arb coordinate interval must contain its saved
exact localization square; no rounded interval is silently narrowed.

After localization, evaluate only the original logarithmic marginal
\[
       p_T=g'(a_*+t_*)-\tfrac32g'(a_*)+2\pi it_*.
 \tag{11}
\]
Save outward component enclosures and exact endpoint combinations
for \(L(0),L(1/100),L(7/500)\). Report all four cases regardless
of sign. A failure of any proposal, domain, or residual test is
recorded as inconclusive, with no downstream marginal evaluation.

This diagnostic performs no dilogarithm evaluation, target optimization,
full 378-profile pass, finite quantum-source evaluation, subdivision,
or automatic fallback. A positive result concerns the upper-envelope
obstruction in (8)--(9) only. A nonpositive lower bound is inconclusive
for that obstruction; it is not a negative upper bound for (7).
