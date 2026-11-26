# The second selection after an initial type-three block

Research deduction, 6 November 2026.

The completed first-type-three central and half-row comparisons give
the entire second-selection finite product for prefixes of types
\(343\) and \(344\). It joins the unselected first cap and every
mixed suffix with the original affine tangents and diagonal allocation.
The restricted plateau sum retains its original nonzero geometric
coefficient. No first-type-four reference or numerical response bound
is transferred. This is not an estimate for the entire open source.

## 1. The original finite product and its completed comparisons

Fix a positive mixed three/four word of length \(m\ge4\), with
first three flags \((\epsilon_1,\epsilon_2,\epsilon_3)=(0,1,\beta)\),
\(\beta\in\{0,1\}\). Let \(r_j=a_j+ic_j\) be its original
retained critical coordinates, put \(P=[.22,.45]\), and set
\[
 z_1=x_1+ic_1,\qquad z_2=x_2+i/100,\qquad z_3=x_3+ic_3,
 \qquad (x_1,x_2,x_3)\in P^3,\qquad X_j=e^{-2\pi iz_j}.
 \tag{1}
\]
Positions 1 and 3 are unselected. The reference indices
\(u_*=s_2^*\), \(v_*=s_3^*\) are ordinary, also at \(m=4\).
The next external coordinate \(c=s_4^*\) is attached at length
four and ordinary at greater lengths. In both cases the
[first-type-three reference theorem](research_mixed_second_selected_first_three_extension.md)
places it in \(K_3\cup K_4\) and identifies the actual prefix
with the corresponding canonical reference.

Use the original bare phase
\[
 Q_\epsilon(s;a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)
                              -g(a)-g(b)+2\pi ias
 \tag{2}
\]
and its allocated two-factor phase
\[
 \begin{split}
 F_0&=Q_1(u;z_1,z_2)+Q_\beta(v;z_2,z_3)
                                      -g(z_2)-\tfrac\beta2g(z_3),\\
 M_{23}&=\Re F_{0,*},\qquad
 p_L=g'(r_1+u_*)-g'(r_1)+2\pi iu_*,\\
 p_R&=g'(v_*+r_3)-(1+\beta/2)g'(r_3),\\
 \Lambda_{23}&=M_{23}
       +\Re\{p_L(z_1-r_1)+p_R(z_3-r_3)\}.
 \end{split}
 \tag{3}
\]
All starred quantities belong to one original reference, with its
original logarithmic lifts and additive phase constant. There is no
incoming \(-g(z_1)/2\). The internal derivatives with respect to
\(u,z_2,v\) vanish at this reference; both boundary marginals in
(3) are retained.

The literal product is
\[
 \mathcal B_{23,N}=
 |C_{1,N}(X_1,X_2)C_{\beta,N}(X_2,X_3)
                            d_N(X_2)X_2^{-N}|
                                  |d_N(X_3)|^{\beta/2}.
 \tag{4}
\]
There is no incoming modulus halfweight. If \(\beta=0\), the
last factor is identically one, including at zeros of \(d_N\).

The [completed central comparison](research_mixed_second_selected_first_three_central_completion.md)
gives a raw main/main gap greater than \(1/100\) for \(\beta=0\)
and greater than \(1/200\) for \(\beta=1\). These estimates
bound both original Fourier alternatives, with all real targets
free and the two tangents (3) unchanged.

For \(\beta=0\), the
[completed first-type-three half-row comparison](research_mixed_second_selected_first_three_half_row_completion.md)
gives a raw gap greater than \(1/20\) for both main/right-half-row
defects in equation (6) of the
[four-profile reduction](research_mixed_second_selected_four_profile_reduction.md).
It is uniform on the original \(\alpha=0,\beta=0\) canonical
family over \(K_3\cup K_4\), with all real targets free. Its
reference bank and response bounds belong to this first-type-three
family, not to the previously completed first-type-four family.
Define
\[
                     \delta_0=\delta_1=\frac1{400}.
 \tag{5}
\]

**Theorem 1.** For \(\beta=0,1\), every \(\tau>0\) admits
constants such that
\[
 \mathcal B_{23,N}\le C_\tau N^{A_\tau}
                 \exp N\{\Lambda_{23}-\delta_\beta+\tau\}
 \tag{6}
\]
uniformly on (1), at all sufficiently large integer levels of both
parities. Every finite row, alias and contour join is retained.

*Proof.* The four-profile reduction is already proved for both
first flags. Its three pointwise comparisons remove the non-main
profiles of factor 2 on a containing incoming-height interval
\((-.078,.021)\); the actual attached type-three interval
\((-.072,.021)\) is contained in it. For either outgoing type,
the left cut of factor 3 is dominated by its main profile. The
joint outgoing last-row comparison retains the separate gap
\(1/400\), also for first flag zero.

For \(\beta=0\), the four remaining defects comprise two central
alternatives with gap greater than \(1/100\) and two right-half-row
alternatives with gap greater than \(1/20\). Inserting these in
the finite reduction's rate
\(\Lambda_{23}+\max(-1/400,D_4)\) gives (5)--(6).
For \(\beta=1\), the
[outgoing-four half-row theorem](research_mixed_second_selected_outgoing_four_half_row_completion.md)
dominates that half row by the right main profile with loss \(1/20\).
It has no first-flag premise. Its equation (8) leaves only the two
central defects, each below \(-1/200\), and the separate
\(-1/400\) last-row term. Thus \(\delta_1=1/400\).
The original finite-current estimate combines the finitely many
profiles with one total rate tolerance. Both Fourier alternatives
bound their original additive polynomial estimate; neither is
deleted or replaced by a minimum. This proves (6). \(\square\)

For any \(0<\tau<\delta_\beta/2\), the polynomial prefactor
can be absorbed into the strict remaining tolerance for large
enough \(N\), giving a finite-source rate loss
\(\delta_\beta/2=1/800\).

## 2. Joining the first cap and arbitrary suffix

Put \(h=m-1\), \(k_4=\sum_{j=1}^m\epsilon_j\), and
\(I_m=\{j:6\le j\le m-5\}\). This set is empty for
\(m\le10\). For a type-compatible \(T\subseteq I_m\), let
\(S=\{2\}\cup T\) and use
\[
 \Im z_2=1/100,\qquad \Im z_j=7/500\ (j\in T),\qquad
 \Im z_j=c_j\ (j\notin S),\qquad \mathbf x\in P^h.
 \tag{7}
\]
Each exact selected summand has its own permitted contour in the
full torus identity. These plateau heights are constant and their
parameter Jacobian is one. No equality between differently deformed
plateau pieces is assumed.

The exact retained integrand is
\[
 \begin{split}
 \mathscr J_{S,N}={}&U_{0,N}(w_L,X_1)
       \prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
       \mathcal V_{\epsilon_m,N}(w_R,X_h)\\
 &\quad\cdot\prod_{j=1}^{h}
             d_N(X_j)^{\epsilon_j}X_j^{-N\mathbf1_{j\in S}}.
 \end{split}
 \tag{8}
\]
The whole terminal transform contains its private source and its
own Fourier alternatives. The exact external scalar remains
\(\kappa_N^{m+k_4}N^{m+k_4-1}\), with \(|\kappa_N|=1\).

Let \(L_0=\mathcal T_0(\cdot,-2)\), let \(\phi_j\) be the
original allocated ordinary phases, and put
\(\Pi=\mathcal P_{\epsilon_m}-\epsilon_hg/2\), as in the
[whole unselected plateau theorem](research_mixed_full_unselected_plateau.md).
The exact original phase decomposition at the critical point is
\[
 \mathcal F_m(z_*)=L_0(r_1)+F_{0,*}
          +\sum_{j=4}^{h}\phi_j(r_{j-1},r_j)+\Pi(r_h).
 \tag{9}
\]
The sum is empty when \(m=4\).

Here the incoming cancellation can be checked directly. Write
\(j(w)=J'(w)=\operatorname{Log}(2\sin\pi w)\), and let \(e_*\)
be the original private first-cap coordinate. The
[original cap phase](research_mixed_complete_first_cap_packet.md),
equations (4)--(5), gives
\[
 \begin{split}
 L_0'(r_1)&=j(e_*+r_1)-j(r_1)-i\pi e_*,\\
 p_L&=j(r_1+u_*)-j(r_1)+i\pi u_*,\\
 L_0'(r_1)+p_L
   &=j(e_*+r_1)+j(r_1+u_*)-2j(r_1)
                                      +i\pi(u_*-e_*)=0.
 \end{split}
 \tag{10}
\]
The last expression is exactly the original first-type-three
attached stationary equation. No first-type-four own term appears.

At the right cut the remaining matching identities are
\[
 p_R+\partial_1\phi_4(r_3,r_4)=0\quad(h\ge4),\qquad
 p_R+\Pi'(r_3)=0\quad(h=3).
 \tag{11}
\]
The completed cap bound for \(U_0\) carries no halfweight, just
as (4) has none at coordinate 1. At coordinate 3, the other
incidence contributes \(|d_N(X_3)|^{\beta/2}\), either from the
next ordinary factor or from the complete terminal factor when
\(m=4\). Thus (4) restores the integer power
\(|d_N(X_3)|^\beta\). In the latter case
\(\Pi(z_3)=\mathcal P_{\epsilon_4}(z_3)-\beta g(z_3)/2\).
Every other retained weight is likewise allocated once between
its two incidences. No Fourier factor is divided out, even at a zero.

For the additional selections define
\[
 E(T)=\{j\in\{4,\ldots,h\}:j-1\in T\text{ or }j\in T\}.
 \tag{12}
\]
These factor indices are at least six and are disjoint from factors
2 and 3. The
[interior-selection theorem](research_mixed_interior_selected_plateau.md)
applies to their actual inherited ordinary reference pairs and gives
loss \(1/200\) per incident factor, counting a factor only once.
All other factors use their completed unselected planes. In
particular the cap and terminal real targets still range over all
of \(P\), rather than being fixed to their critical values.

**Theorem 2.** Every fixed word above and every \(\tau>0\) satisfy
\[
 |\mathscr J_{\{2\}\cup T,N}|
 \le C_{m,\tau}N^{A_{m,\tau}}
 \exp N\left\{M_{\rm open}-\delta_\beta
                     -\frac{|E(T)|}{200}+\tau\right\},
 \qquad M_{\rm open}=\Re\mathcal F_m(z_*).
 \tag{13}
\]
The assertion holds at both parities, on sufficiently small fixed
ordinary-color disks and for every fixed ordinary-color derivative
on smaller disks, with its own polynomial prefactor.

*Proof.* Multiply (6) by the complete first-cap, suffix and
terminal bounds, with the allocation above. Equations (9)--(11)
cancel both original boundary tangents. The other original
stationary equations cancel every remaining affine term, including
the imaginary displacements at selected interior positions.
Unused quadratic remainders are nonpositive. For a fixed word,
choose the total source and color tolerances below \(\tau\).
Only the two endpoint factors depend on the ordinary colors, and
their completed bounds hold on fixed disks. Apply Cauchy's formula
to the original holomorphic integer-weighted source on smaller
disks; no modulus halfweight is differentiated. This proves (13)
and the jet assertion. \(\square\)

## 3. The original coefficient in the restricted plateau sum

Allow all type-compatible \(S\subseteq\{2\}\cup I_m\), including
the empty set. Use (7) when \(2\in S\) and the existing
interior-selection contours otherwise. Let
\(\mathcal Z_N^{\rm second+int}\) denote the sum of these plateau
integrals multiplied by the original external scalar.

Choose \(\tau<\delta_\beta/2\) in (13). The nonempty selections
not containing 2 already have the interior theorem's strict gap
\(1/200\). For each fixed word there are only finitely many
selected sets, and the external scalar has polynomial modulus.
Consequently the completed unselected asymptotic gives
\[
 \mathcal Z_N^{\rm second+int}(-2,-2)
   =\kappa_N^{m+k_4}N^{-3/2}A_m
                e^{N\mathcal F_m(z_*)}(1+O(N^{-1})),
 \qquad A_m\ne0.
 \tag{14}
\]
This conclusion holds for both \(343\) and \(344\). Its action,
phase, orientation, power and coefficient are the original ones.
On sufficiently small
fixed color disks the same local packet and ordinary jets survive:
shrink the disks so the moving original critical action varies by
less than the strict comparison gap, then apply Cauchy's formula
to the exponentially small difference.

The rate loss is independent of the word length; constants, color
disks and the sufficiently-large-level threshold may depend on
the fixed word. Position 1 has type three, so its absence from the
selection set is automatic in the original retained Fourier
expansion. This does not address other boundary selections,
regions outside the plateau, whole-source outside-color estimates
or arbitrary short partial fillings. Equation (14) concerns the
specified partial integral, not the entire original invariant.
