# Completing the real right interval for the initial four/four pair

Private written assembly, 10 November 2026. The complete cap and
conditional estimates have compatible comparisons at the real half
face. Combining them closes the intervening interval from \(7/10\)
to \(7/8\). The existing far-right estimate and periodic endpoint
collar then cover the entire real interval \([7/10,1]\).

Every statement concerns the original full first pair, with both
first Fourier choices and the outgoing halfweight. Later coordinates
remain in their original unselected plateau ranges. No whole-word or
knot-volume conclusion is asserted here.

## 1. The exact pair and its original comparison

Fix an actual positive three/four word of length \(m\ge3\) beginning
with four and four. Retain the original reference
\[
 a_*=a_0+ic,\quad b_*=b_0+id,\qquad
 .246<a_0<.350,\quad -.078<c<-.020,\quad
 -.102\le d\le-.001 .
 \tag{1}
\]
The second target is \(b=z+id\), with \(z\in[11/50,9/20]\).
Write \(X=e^{-2\pi ix}\), \(Y=e^{-2\pi ib}\).
The literal function is
\[
 K_{\epsilon,N}(w;x,b)
 =U_{1,N}(w,X)\,C_{1,N}(X,Y)\,d_N(X)X^{-N\epsilon},
                       \qquad\epsilon=0,1,
 \tag{2}
\]
with the original cap, conditional polynomial and forced Fourier
polynomial. Its outgoing allocation is \(|d_N(Y)|^{1/2}\).
Use the original affine action \(\Lambda(z)\), and put
\[
 \kappa=1/2500000,\qquad \kappa_R=8\kappa/9,\qquad
 \delta_R=\kappa(9/20-a_0)^2,\qquad
                  \kappa/100<\delta_R<\kappa .
 \tag{3}
\]
These are the same constants as in the previous half-face bounds.

Let \(\mathcal A=\mathcal A(0)\) be the original real-half-face
cap profile envelope, as defined in
[complete cap transport](research_mixed_initial44_complete_real_cap_transport.md).
Let
\[
 L(b)=E_{1/2}(2/25;b),\qquad H(b)=E_{1/2}(1/2;b)
 \tag{4}
\]
be the two physical cut rates from
[the intermediate conditional source theorem](research_mixed_four_conditional_intermediate_real_source.md).
Write \(\Theta(x,b)\) for the original conditional critical action.
All these are calibrated continuous rates, not logarithms of
possibly zero finite values.

## 2. Each of the six rate combinations is paid

The two complete source theorems give on \(7/10\le x\le7/8\),
with any prescribed positive rate allowances,
\[
\begin{split}
 |U_{1,N}(w,X)d_N(X)X^{-N\epsilon}|
   &\le \operatorname{poly}(N)
                    e^{N\{\max(\mathcal A,9/10)+\tau_1\}},\\
 |C_{1,N}(X,Y)|
   &\le \operatorname{poly}(N)
                    e^{N\{\max(\Re\Theta(x,b),L(b),H(b))+\tau_2\}}.
\end{split}
 \tag{5}
\]
The exact outgoing Fourier estimate, retained in
[the far-right physical calibration](research_mixed_initial44_far_right_physical_envelope.md),
is
\[
 |d_N(Y)|^{1/2}\le \operatorname{poly}(N)
                           e^{N\{-\Re g(b)/2+\tau_3\}} .
 \tag{6}
\]
It uses the original primitive, for which \(\Re g(b)<0\) on
this outgoing domain. No Fourier factor is divided out.

First consider the entry \(\mathcal A\) in (5).
Corollary 2 of
[the half-face height theorem](research_mixed_initial44_half_face_height_connections.md)
proves
\[
 \mathcal A+
      \max\{\Re\Theta(1/2,b),L(b),H(b)\}
          -\tfrac12\Re g(b)\le\Lambda(z)-\delta_R.
 \tag{7}
\]
The [unit-circle multiplier theorem](research_mixed_four_conditional_unit_multiplier.md)
gives \(\Re\Theta(x,b)\le\Re\Theta(1/2,b)\).
Thus (7) pays all three combinations involving \(\mathcal A\).

For the constant \(9/10\), retain the different original
comparisons; there is no substitution \(\mathcal A=B_*\).
The [original critical calibration](research_mixed_initial44_lower_right_action_calibration.md)
and the height decrease in the half-face theorem give
\[
\begin{split}
 B_*+\Re\Theta(x,b)-\tfrac12\Re g(b)
 &\le\Lambda(z)
       -(\kappa+\kappa_R)(1/2-a_0)^2-\kappa_R(z-b_0)^2 .
\end{split}
 \tag{8}
\]
Here the incoming height is first increased from \(c\) to zero
at real part \(1/2\), then the real coordinate moves to \(x\).
The [sharper half-face floor](research_mixed_initial44_sharper_half_face_floor.md)
proves \(B_*>183/200\), so \(B_*-9/10>3/200\).
Also
\((\kappa+\kappa_R)(1/2-a_0)^2>\delta_R\).
Equation (8) therefore pays the constant cap entry against the
critical term with more than the gap \(\delta_R\).

For its two physical combinations, equation (29) of the far-right
physical theorem gives the original bare plane \(B_0\) and
\[
\begin{split}
 B_0+\max\{L(b),H(b)\}-\tfrac12\Re g(b)
    &\le\Lambda(z)-\kappa(z-b_0)^2-2\delta_R,\\
 B_0&>233/250-\kappa>9/10.
\end{split}
 \tag{9}
\]
Thus these two combinations also retain more than \(\delta_R\).
Together (7)--(9) prove
\[
 \max\{\mathcal A,9/10\}
 +\max\{\Re\Theta(x,b),L(b),H(b)\}
 -\tfrac12\Re g(b)
 \le\Lambda(z)-\delta_R .
 \tag{10}
\]
This is an explicit comparison of all six alternatives. It neither
uses positivity of the signed conditional sum nor infers an
individual profile bound from the modulus of that sum.

**Theorem 1.** For every \(\tau>0\), both level parities and
\(\epsilon=0,1\), the full original pair satisfies
\[
 |d_N(Y)|^{1/2}|K_{\epsilon,N}(w;x,b)|
 \le C_\tau N^{A_\tau}
              e^{N\{\Lambda(z)-\delta_R+\tau\}},
               \qquad 7/10\le x\le7/8 .
 \tag{11}
\]
The bound is uniform for ordinary real colors \(w\in[-2,2]\).
It also holds on sufficiently small fixed ordinary-color disks
and for their fixed derivatives on smaller disks.

*Proof.* Multiply (5)--(6), use (10), and distribute the single
total allowance among \(\tau_1,\tau_2,\tau_3\). The complete cap
theorem supplies the color extension and derivatives; the other
factors are constant multipliers in that argument. All finite
indices, contour corrections and scalar factors are already
retained in those two source estimates. \(\square\)

## 3. The closed real interval through the periodic endpoint

**Corollary 2.** On the entire real interval \(7/10\le x\le1\),
\[
 |d_N(Y)|^{1/2}|K_{\epsilon,N}(w;x,b)|
 \le C N^A e^{N\{\Lambda(z)-\delta_R/2\}},
 \tag{12}
\]
with both first Fourier choices, both level parities, all real
ordinary colors, and fixed derivatives on a common sufficiently
small ordinary-color disk.

*Proof.* Use (11) with the fixed allowance \(\kappa/400\);
by (3) this leaves at least \(\delta_R/2\).
The [periodic endpoint collar](research_mixed_four_four_periodic_right_endpoint_collar.md)
has a fixed width \(r_0>0\) and rate
\(\Lambda(z)-1/4000\) on \([1-r_0,1]\), for this identical
finite pair and outgoing allocation.
Choose a fixed \(0<\rho<\min(r_0,1/8)\).
The [complete far-right pair theorem](research_mixed_initial44_near_endpoint_complete_pair.md)
then covers \([7/8,1-\rho]\) with rate
\[
 \Lambda(z)-\kappa(z-b_0)^2-2\delta_R-1/400+\tau.
\]
Take its allowance to be \(1/800\). This rate and the collar
rate are both at most \(\Lambda(z)-\delta_R/2\), because
\(\delta_R<\kappa<1/4000\).
The three closed intervals cover \([7/10,1]\).
Intersect their fixed color disks and take the largest of
their finitely many constants and polynomial powers.
This proves (12). The endpoint \(x=1\) uses the exact periodic
Laurent polynomial, not a factorial approximation at its
singular endpoint. \(\square\)

Multiplication by the original density \(N\,dx\) and integration
over any subinterval of \([7/10,1]\) costs only a polynomial
factor in (12). The orientation and the selected monomial
remain those of (2). This completes the previously missing real
first-coordinate path, but does not estimate other Fourier
selections or departures of later coordinates from their
original plateaux.

## Direct source versions

| Direct source | SHA-256 |
|---|---|
| research_mixed_initial44_complete_real_cap_transport.md | dd8d313e1e23240943421b6fbb340f28de769f46d2c0f98f3a4a749be20d4420 |
| research_mixed_four_conditional_intermediate_real_source.md | e5eff44816440f4675f6a216d09f614330ebe4f72a2bdcc2ddf20939b711710d |
| research_mixed_initial44_half_face_height_connections.md | 4d83ce42628d9dcd9d965be4f75a6538c4a150ec767b436c42847a177eb352f8 |
| research_mixed_four_conditional_unit_multiplier.md | 4d73d90557948056413ef0445cb7754569cbbc03e7ff3f35ecab0f3e9fe8f66f |
| research_mixed_initial44_lower_right_action_calibration.md | ef0079ed2c3148db13a24c23e715d9daab6e164b1aff0231de11041613e0106f |
| research_mixed_initial44_sharper_half_face_floor.md | eeb48098cf6a53eb7e9cee54ec1eb944f5607252e42550fbc69599f4a76c672a |
| research_mixed_initial44_far_right_physical_envelope.md | a676bfee21df1e78965bb6515a37e0aebd669b6fb4e4cecb2976a8c254cf778d |
| research_mixed_four_four_periodic_right_endpoint_collar.md | 91ed08bf7e2d04dabcd8e85bc3d3eac648bfdde9ae29a4d1bc7f6a137cbd39a4 |
| research_mixed_initial44_near_endpoint_complete_pair.md | 4a481d134c93b8bb11bed2406253cec046f6e04a95339b1b48a8594469bc7712 |

No mathematical numerical evaluation, saved-value arithmetic,
test, import, compilation or frozen-source edit is used.
Independent full proof and direct-source review is required
before adoption.
