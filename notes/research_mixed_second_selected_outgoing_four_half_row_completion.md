# Completed outgoing four-type half row at the second selection

Research theorem and finite-source assembly, 6 November 2026.

The outgoing own-four half row is now strictly below its original
main contour on the full containing height and target domain.
For first three flags \((\alpha,1,1)\), this reduces the second-selection
problem with position 1 unselected to the two central Fourier
alternatives. When both first positions are selected, sixteen
profiles remain. Neither statement supplies the still-missing central
sign or a whole-chain estimate.

## 1. Completed pointwise comparison

Use the original bare own-four phase
\[
 Q(s;a,b)=g(s+a)+g(s+b)-3g(s)-g(a)-g(b)+2\pi ias.
 \tag{1}
\]
The [analytic criterion](research_mixed_second_selected_outgoing_four_half_row.md)
and its [standalone checker](../experiments/check_mixed_second_selected_outgoing_four_half_row.py)
are frozen at SHA-256 hashes
f2d292d99ff3ebbc447d400de25104a1f315c3fb36b951badfac998e4d43fd4f
and
857c5c116bbfda43a413bca7d5618de053b943b089b31b4b20785c1df20220b6.
The single completed
[32-interval record](../repro/results/research-mixed-second-selected-outgoing-four-half-row.json)
has hash
6ae8312f07d9a4b968834f8311085fac2cb8287c7b55d89d35bac32f78c957d9.

All 32 whole-height tests passed at 160 bits. The smallest saved
rational lower endpoint is
\[
 \frac{1227125406282592374982731466121489441644043997127}
 {11692013098647223345629478661730264157247460343808}
 >.10495>\frac1{20}.
 \tag{2}
\]
The saved-data check verifies the exact interval partition, all six
current input hashes, each strict rational inequality, and the lower
bound obtained by subtracting the recorded height correction and
\(3/800\) real-target correction from the midpoint lower endpoint.
It performs no new primitive, source, or root evaluation.

Consequently, throughout
\[
 a=x+i/100,\quad b=y+ik,\quad x,y\in P=[.22,.45],
 \qquad h,k\in[-.102,-.001],
 \tag{3}
\]
the criterion's Proposition 1 gives
\[
 R_R(a,b):=\Re Q(1/2;a,b)
 <
 R_0(a,b)-\frac1{20},\qquad
 R_0(a,b):=\max_{1/8\le t\le1/2}\Re Q(t+ih;a,b).
 \tag{4}
\]
The admissible trial is \(3/10+ih\). The original asymmetric chirp,
the real-target minimization loss, and the whole-height Lipschitz
correction are included. Every allocation or affine term common to
both profiles may be added unchanged.

## 2. Position 1 unselected: two comparisons remain

Fix any mixed three/four word of length \(m\ge4\), with first three
flags \((\alpha,1,1)\). Retain the actual reference, original
normalization, and profiles of the
[second-selection finite reduction](research_mixed_second_selected_plateau_reduction.md).
Put
\[
 z_1=x_1+ic_1,\quad z_2=x_2+i/100,\quad z_3=x_3+ic_3,
 \qquad x_1,x_2,x_3\in P.
 \tag{5}
\]
Positions 1 and 3 are unselected. Both the index and outgoing
coordinate of factor 3 have own-four heights in
\((-.102,-.001)\), including \(m=4\), when its next external
leg is attached. Thus (4) applies without restricting any suffix.

The literal finite product and the complete selected-weight rates are
\[
 \begin{split}
 \mathcal B_{23,N}
 &=|C_{1,N}(X_1,X_2)C_{1,N}(X_2,X_3)d_N(X_2)X_2^{-N}|
             |d_N(X_1)|^{\alpha/2}|d_N(X_3)|^{1/2},\\
 W_2^{\mathrm{fac}}&=-\Re g(z_2)-2\pi/100,\qquad
 W_2^{\mathrm{force}}=0 .
 \end{split}
 \tag{6}
\]
Let \(\Lambda_{23}\) be the original two-boundary affine term,
with both original marginals, and define
\[
 D_2=\max_{\nu\in\{\mathrm{fac},\mathrm{force}\}}
 \left\{
 R_0^2+R_0^3-\frac\alpha2\Re g(z_1)-\frac12\Re g(z_3)
                  +W_2^\nu-\Lambda_{23}
 \right\}.
 \tag{7}
\]

**Theorem 1.** For every \(\tau>0\), the entire finite product (6)
satisfies
\[
 \mathcal B_{23,N}
 \le C_\tau N^{A_\tau}
       \exp N\{\Lambda_{23}+\max(-1/400,D_2)+\tau\}.
 \tag{8}
\]
Both level parities, all physical rows, and every original contour
contribution are retained.

*Proof.* The
[four-profile assembly](research_mixed_second_selected_four_profile_reduction.md),
Theorem 1, has already reduced all thirty-two initial profiles to
right main and right half-row, each with the two selected-weight
alternatives, together with the separately paid right-last-row
bound \(-1/400\). In each remaining half-row term, (4) replaces
\(R_R^3\) by \(R_0^3-1/20\); every other term is common.
The maximum is therefore bounded by (7), and the same finite-current
estimate gives (8). \(\square\)

This replacement does not subtract \(1/20\) from the main/main
terms themselves. Their two uniform signs remain open. The new
comparison has own-four scope; it removes no own-three half-row
comparison when the third flag is zero.

## 3. Both first positions selected: sixteen profiles remain

Now let the first three flags be \((1,1,1)\), and use
\(H_1=H_2=1/100\), with position 3 unselected. The exact product is
\[
 \mathcal B_{123,N}
 =|U_{1,N}(w,X_1)C_{1,N}(X_1,X_2)C_{1,N}(X_2,X_3)
      d_N(X_1)X_1^{-N}d_N(X_2)X_2^{-N}|
                         |d_N(X_3)|^{1/2}.
 \tag{9}
\]
Keep the original \(\Lambda_{123}\), including its unchanged
outgoing marginal. For \(i=1,2\), set
\(W_i^{\mathrm{fac}}=-\Re g(z_i)-2\pi H_i\) and
\(W_i^{\mathrm{force}}=0\). With the original cap profiles
\(A_0,A_L\), define
\[
 D_{16}=
 \max_{\substack{a\in\{0,L\},\ j\in\{0,1\}\\
                 \nu_1,\nu_2\in\{\mathrm{fac},\mathrm{force}\}}}
 \left\{
 A_a+R_0^2+R_j^3-\frac12\Re g(z_3)
       +W_1^{\nu_1}+W_2^{\nu_2}-\Lambda_{123}
 \right\}.
 \tag{10}
\]

**Theorem 2.** For every \(\tau>0\) and every fixed ordinary-color
derivative order \(k\),
\[
 \mathcal B_{123,N}^{(k)}
 \le C_{\tau,k}N^{A_{\tau,k}}
                  e^{N(\Lambda_{123}+D_{16}+\tau)}.
 \tag{11}
\]
Here the derivative acts on the holomorphic integer-weighted
product inside (9), before taking its modulus; the outgoing
modulus halfweight is then added once. The assertion holds on the
small fixed original color disk and at both level parities.

*Proof.* Theorem 2 of the four-profile assembly leaves 24 profiles:
two cap choices, right choices \(0,R,1\), and four pairs of Fourier
alternatives. Its pointwise left-factor reductions remain valid
because the incoming height \(H_1=.01\) lies in their containing
domains. Equation (4), independent of the first cap and factor 2,
removes right choice \(R\). This leaves
\(2\cdot2\cdot2\cdot2=16\) profiles, exactly (10).
Proposition 2 of the original finite reduction supplies the
complete finite-source, color, and derivative bound. \(\square\)

Right profile 1 remains in (10). Its earlier joint loss used the
first coordinate at its unselected reference height and is not
available here. In particular no unselected supporting plane is
substituted for \(\Lambda_{123}\). All sixteen signs remain open.

The new result is a pointwise elimination of a literal ordinary
half-row profile, followed by exact finite-product reductions.
It supplies no central sign, nonzero coefficient, whole-chain
bound, or finite-exception theorem.
