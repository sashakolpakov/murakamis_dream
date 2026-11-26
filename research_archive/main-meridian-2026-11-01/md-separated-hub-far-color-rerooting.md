# Exposing each original circle in a separated-hub tree

Private derivation, 1 November 2026. No repository source is changed.

This report supplies the source adapter for the half-twist contour estimate. It uses the actual typed closing pairing to expose any one of the original auxiliary circles. It does not move an auxiliary circle by a tangle isotopy and does not change the marked main cut.

## 1. Statement and inputs

Fix a strict literal Conway source whose reduced tree has no adjacent bare hubs. A flagged hub has exactly one original flagged leaf; a bare hub has none. The construction, all its ordered maps, its \(m\) labeled original circles, and its retained half-twist pattern \(\epsilon_i\in\{0,\pm1\}\) are fixed. Let \(F_0\) be its original complete action.

Assume the proved source bounds and their fresh Gaussian conclusions:

- an ordinary or decorated outgoing \(L\)-module has its original spectral pressure \(\Omega_L=2G_0+c_L\) and a fresh Gaussian at that pressure;
- an outgoing bare-hub \(A\)-module with \(B\ge2\) incoming \(L\)-cones has original pressure \(\Omega_Q=\widehat\omega_B+\sum c_b\) and a fresh Gaussian there.

These are Sections 1 and 3 of the workspace note actual_main_meridian_source_bounds.md. In the second statement the Gaussian follows from the original clean low-coordinate profile and the strictly smaller spectral remainder, not merely from a norm estimate.

The resulting assertion is: for every fixed \(R<1/2\) and \(0<\delta<1\), there is \(\gamma>0\) such that
\[
 \sup_{\substack{|s|\le R,\ 1\le j_i\le N\\
                  \text{some }j_i\le(1-\delta)N}}
 |\mathcal F_{N,\mathbf j}^{\epsilon}(q^s)|
 \le \exp N(F_0-\gamma)
 \tag{1}
\]
for every sufficiently large \(N\), at both parities. The scalar is the actual reduced auxiliary-colored source, with the prescribed main cut and framing. The argument does not sum auxiliary filling colors.

The exact half-twist contour theorem is the private report md-half-twist-root-chirp-and-far-color-gap.md. The original geometry accounting is md-separated-unflagged-hubs-original-geometric-budget.md. All private reports are in the temporary directory; no extra geometric comparison is assumed here.

## 2. The available closing adjunction

In fixed canonical Newton coordinates, the pairing for either actual quotient is
\[
 \langle f,g\rangle=\sum_{n=0}^{N-1} f_n g_{N-1-n}.
 \tag{2}
\]
Every prescribed typed turn is
\[
 T_\gamma=\frac{\gamma_N(s)}{H_N(s)}
          \mathbf J\operatorname{diag}(W_n(s)),
 \qquad \mathbf J_{ij}=\mathbf1_{i+j=N-1}.
 \tag{3}
\]
Consequently
\[
 \langle T_{\gamma_1}f,g\rangle
 =\frac{\gamma_1}{\gamma_2}
       \langle f,T_{\gamma_2}g\rangle.
 \tag{4}
\]
Both sides are \(\gamma_1H_N^{-1}\sum W_nf_ng_n\). The scalar ratio records the two actual object types. Coherent carriers cancel in the composed pairing; the primitive top moment is the same for either orientation. This is an identity of the original full typed tensor contraction, including the first normal coordinates.

Changing the direction of a finite tree's recursive evaluation uses (4), associativity within compatible objects, and the exact consecutive-turn identities. It multiplies the scalar only by the recorded bounded phase \(\chi_{i,N}(s)\), which is a fixed product of powers of \(q^{s^2/2}\). The original root crossing and circle pivot stay in their coupons. There is no assertion of an isotopy or of a scalar factorization of an effective branch.

## 3. Three possible positions of the selected original leaf

Choose an original circle \(i\), and orient all subtree evaluations toward its incident hub. Each child subtree remains in the separated-bare-hub class. The same induction supplies its original intrinsic pressure and fresh Gaussian.

### A flagged leaf

If \(i\) is the marked leaf of a flagged hub, expose its original coupon \(p_i=R_s^{\epsilon_i}L_{j_i}\). Let \(Q_1,\ldots,Q_k\) be the other incident outgoing modules, each of type \(L\) or \(A\). The normalized closing scalar is
\[
 Z_{N,\mathbf j}^{\epsilon}(s)
 =\chi_{i,N}(s)\,
    \phi_\sigma\!\left(R_s^{\epsilon_i}L_{j_i} E_i\right),
 \qquad E_i=\prod_{a=1}^k Q_a,
 \tag{5}
\]
where the product defining \(E_i\) is retained as a raw polynomial. Each factor is canonical and has its fresh Gaussian at \(\Omega_{Q_a}\). Their product therefore has a fresh Gaussian at \(\sum_a\Omega_{Q_a}=F_0\), by the original flagged-root action identity.

### An ordinary leaf incident to a flagged hub

Now \(h_i=T_{\gamma_1}(p_i)\) is ordinary at its hub. That hub has a different marked original coupon \(p_v\), and its remaining branches are \(Q_a\) of type \(L\) or \(A\). Before the closing adjunction the scalar is the pairing of \(T_{\gamma_1}p_i\) with \(p_v\prod_aQ_a\). Transfer the closing turn by (4). The remaining canonical polynomial is
\[
 E_i=T_{\gamma_2}\!\left(p_v\prod_aQ_a\right).
 \tag{6}
\]
This is exactly a decorated \(L\)-module, so it has a fresh Gaussian at
\[
 \Omega_{E_i}=2G_0+\sum_a\Omega_{Q_a}.
 \tag{7}
\]
This rate is the original \(F_0\): using \(v\) as the earlier flagged root gives the same sum, with the selected ordinary leaf contributing its intrinsic pressure \(2G_0\). The scalar again has the form (5), with its actual phase ratio included in \(\chi_{i,N}\).

### An ordinary leaf incident to a bare hub

The selected leaf \(h_i=T_{\gamma_1}p_i\) occupies one incidence of the bare hub. Every other child branch is type \(L\), because adjacent bare hubs are forbidden. There are \(B=d_v-1\ge2\) such branches. Transferring the selected leaf's turn gives
\[
 E_i=T_{\gamma_2}\!\left(\prod_{a=1}^B L_a\right).
 \tag{8}
\]
This is exactly the whole bare-hub output. It has a fresh Gaussian at
\[
 \Omega_{E_i}=\widehat\omega_B+\sum_ac_a.
 \tag{9}
\]
The closure with the selected existing ordinary leaf is precisely its defining intrinsic probe, so (9) equals the original \(F_0\). That leaf was already in the source; it has not been added as a new crossing circle. Equation (5) again holds with the prescribed typed adjunction scalar.

These alternatives exhaust every original leaf when a hub exists. In the strict two-leaf case, exposing either original coupon leaves the other decorated leaf, with Gaussian budget \(2G_0=F_0\), and the same closing adjunction supplies (5).

## 4. Apply the actual root contour and retain the main cut

For each fixed \(i\), the polynomial \(E_i\) in (5), (6), or (8) is independent of \(j_i\). Its Gaussian constants and error are uniform over the other original physical colors. It is either one canonical outgoing polynomial or a product of a fixed number of canonical outgoing polynomials. Its degree is therefore \(O(N)\), though the half-twist contour estimate needs only its polynomial analyticity and Gaussian bound.

In every case its bound has the form
\[
 |E_i(-2\cos(t+iv))|
 \le N^{K_i}
   \exp N\{F_0-c_i t^2+C_i v^2+o(1)\},
 \quad |t|\le\pi,\quad |v|\le y_i,
 \tag{10}
\]
with \(c_i>0\). The actual half-twist contour theorem applied to (5) gives a strict loss \(\gamma_i>0\) whenever \(j_i\le(1-\delta)N\). It covers both signs \(\epsilon_i=\pm1\) and the pure case \(\epsilon_i=0\), and also the constant opposite-color relation with its known monodromy scalar.

The original reduced cut is
\[
 \mathcal F_{N,\mathbf j}^{\epsilon}(q^s)
 =H_N(s)\,Z_{N,\mathbf j}^{\epsilon}(s).
 \tag{11}
\]
There is still only one such boundary factor. It and every \(\chi_{i,N}\) are bounded on the fixed disk and do not change the strict rate. The finite number of original leaves permits \(\gamma\) in (1) to be chosen smaller than every \(\gamma_i\), while absorbing all uniform \(o(1)\) errors and polynomial factors. This proves (1).

Under the original strict marked geometry, \(2\pi F_0=\operatorname{Vol}(Y^\epsilon)\). This identifies the action appearing in (1); it is not a comparison with a newly assembled probe link.

## 5. Limits of the result

The estimate is for the auxiliary-colored source before the filling transform, and its reference rate is the augmented complete action. It does not prove the filled knot's lower volume rate or the convergence of the normalized regular main-meridian profile. The radius is fixed below \(1/2\), as required by the chosen unwrapped crossing-root contour. Adjacent bare hubs remain outside this source induction.
