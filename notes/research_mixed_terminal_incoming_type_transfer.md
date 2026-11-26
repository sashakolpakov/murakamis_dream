# A common terminal comparison for both incoming types

Research deduction, 6 November 2026. The incoming type changes the
boundary allocation and its original marginal, but none of the three
main scalar costs or the two direct-cut scalar costs. The two canonical
families agree wherever their input disks overlap. Consequently the
completed type-four-disk certificates also give a complete local
estimate for incoming type three on \(K_3\cap D_4\). They do not
cover all of \(K_3\). No reference, primitive, optimizer, source or
certificate is evaluated in this deduction.

## 1. One canonical family, two boundary allocations

The preceding ordinary vertex has own flag one, the terminal flag is
\(\epsilon\in\{0,1\}\), and the incoming flag is
\(\beta\in\{0,1\}\). Use the disks and actual domains of
[the source-domain theorem](research_mixed_terminal_canonical_source_domain.md):
\[
 \begin{split}
 D_3&=\{|b-(.35-.01i)|\le.09\},&
 D_4&=\{|b-(.30-.052i)|\le.064\},\\
 K_3&=\{|b-(.35-.01i)|\le.083\}
       \cap\{-.072\le\Im b\le.068,\ \Re b-3\Im b\le.608\},\\
 K_4&=\{|b-(.30-.052i)|\le.060\}
       \cap\{-.108\le\Im b\le-.001\}.
 \end{split}
\tag{1}
\]
Let \(q_{\beta,\epsilon}(b)=(e,\xi,t,a,s)\) be the original
canonical zero on \(D_{3+\beta}\). Its five unscaled logarithmic
equations are those of
[the suffix construction, equation (2)](research_mixed_terminal_horizontal_envelope_diagnostic.md).
They contain \(\epsilon\) but no \(\beta\). The latter flag
only specifies the disk of the fixed external argument.

Both constructions put their zero in the same convex chamber
\[
 E\times U\times Q^3,\qquad
 E=[.33,.47]+i[-.09,.08],\quad
 U=[.21,.25]+i[.01,.10],\quad
 Q=[.23,.45]+i[-.12,.12],
\tag{2}
\]
where the original negative real Hessian is greater than
\((6\pi/49)I\). Therefore
\[
 q_{0,\epsilon}(b)=q_{1,\epsilon}(b)
                   \qquad(b\in D_3\cap D_4).
\tag{3}
\]
This follows from uniqueness of the original zero-lift equations,
not from uniqueness of an exponentiated equation. The holomorphic
branches consequently glue on the interiors of the two disks and
retain their original continuous boundary values. Their separate
affine enclosures may have different centers and errors while
enclosing the same branch on the overlap.

Put \(P=[.22,.45]\), \(H=.01\), and retain
\[
 Q_1(s;b,a)=g(s+b)+g(s+a)-3g(s)-g(b)-g(a)+2\pi ibs.
\tag{4}
\]
For a canonical reference \(r_*=(b_*,s_*,a_*,t_*,v_*)\), where
\(v_*=\xi_*\) or \(e_*\), write \(P_*=P_\epsilon(a_*)\).
The correct action and incoming marginal for each flag are
\[
 \begin{split}
 M_\beta&=Q_1(s_*;b_*,a_*)+P_*-g(a_*)-\frac{\beta}{2}g(b_*),\\
 p_\beta&=g'(s_*+b_*)-(1+\beta/2)g'(b_*)+2\pi is_*.
 \end{split}
\tag{5}
\]
The exact finite allocation is
\[
 \left|C_{1,N}(X_b,X_a)\mathcal V_{\epsilon,N}(w,X_a)
                   d_N(X_a)X_a^{-N}\right|\,|d_N(X_b)|^{\beta/2}.
\tag{6}
\]
For incoming type three the final factor in (6) is one. There is
no incoming halfweight to retain, estimate or match elsewhere.
The selected weight at \(a\), the ordinary own-four denominator,
all terminal diagonals, and both original chirps stay unchanged.

## 2. The exact role of the incoming curvature

For any terminal profile \(T_\sigma(a;y)\), define
\[
 \begin{split}
 D_{\beta,\nu,\sigma}={}&\Re Q_1(s;b,a)+T_\sigma(a;y)
       -\nu\Re g(a)-\frac{\beta}{2}\Re g(b)-2\pi\nu H\\
 &-\Re\{M_\beta+p_\beta(b-b_*)\},
 \qquad \nu\in\{0,1\}.
 \end{split}
\tag{7}
\]
Here \(\nu=1\) is factorial and \(\nu=0\) is forced. Both
retain the full independent targets \(b_R,a_R\in P\), with
\(\Im b=\Im b_*\), \(\Im a=H\). At a fixed reference the
identity between allocations is
\[
 D_{\beta,\nu,\sigma}
 =D_{0,\nu,\sigma}
 -\frac{\beta}{2}\Re\{g(b)-g(b_*)-g'(b_*)(b-b_*)\}.
\tag{8}
\]
The subtracted remainder is nonnegative on this horizontal segment.
Thus a bound for \(D_{1,\nu,\sigma}\) alone cannot be reversed
to bound \(D_{0,\nu,\sigma}\). The transfer below uses the actual
scalar majorants and their unused incoming curvature.

At the trial with \(b=b_*\), \(s=s_*\), and
\(\bar a=\Re a_*+iH\), the incoming derivative is exactly zero
after (5) is subtracted. Apply the symmetric pair inequality to
\(V(s,b)\) and \(V(s,a)\), where
\(V(z,w)=g(z+w)-g(z)-g(w)\). It gives
\[
 -\Re Q_1''+\frac{\beta}{2}\operatorname{diag}(g_{h_b}'',0,0)
 \succeq
 \operatorname{diag}\left(
        \frac{1+\beta}{2}g_{h_b}'',\,2g_{h_s}'',\,
                                      \frac12g_H''\right)
\tag{9}
\]
in the order \((b,s,a)\). The chirp has zero real horizontal
Hessian. This holds for the full target product after
\(s_R\ge.22\), whenever the individual height moduli are at
most .12. The first entry remains nonnegative for both flags.
Discarding only this zero-force cost leaves identical bounds in
the other variables.

This proves a reusable rule: any comparison obtained by integrating
(9) from this trial, adding terminal curvature and retaining the
original \(p_\beta\), has the same scalar right side for both
incoming allocations at the same reference. No lost incoming
curvature is silently assigned to another coordinate.

## 3. Three common scalar criteria

All formulas in this section use the same actual canonical reference.
Put \(a_*=A+ic\), \(\Delta=H-c\), and
\[
 B(z)=g(z+i\Delta)-g(z)-i\Delta g'(z),\qquad
 L(z)=g'(z+i\Delta)-g'(z).
\tag{10}
\]
The original shared-leg equation is
\[
 g'(s_*+a_*)+g'(t_*+a_*)-3g'(a_*)+2\pi it_*=0.
\tag{11}
\]
Define the main value and forces by
\[
 \begin{split}
 T_\nu&=\Re\{B(s_*+a_*)+B(t_*+a_*)-3B(a_*)\}
                          +(1-\nu)\Re g(\bar a)-2\pi\nu H,\\
 A_s&=\Re L(s_*+a_*),\qquad
 A_t=\Re L(t_*+a_*)-2\pi\Delta,\\
 A_{a,\nu}&=\Re\{L(s_*+a_*)+L(t_*+a_*)-3L(a_*)
                                      +(1-\nu)g'(\bar a)\}.
 \end{split}
\tag{12}
\]
There is no incoming flag in (10)--(12). The full lifted gradient
is \((0,A_s,A_{a,\nu},A_t,0)\).

Let \(\mathcal G_K(d;x_*,I)\) denote the signed clipped cubic
upper bound in
[the cubic-cost theorem](research_mixed_terminal_cubic_cost_and_response_bounds.md).
The canonical image and optimizer bounds give
\(s_R\in[.22,.5]\), \(t_R\in[.22,.4]\), and
\(|h_s|,|h_t|\le.108\). The original private domains are retained.
By [the symmetric-cost theorem](research_mixed_terminal_symmetric_pair_costs.md),
the main sufficient bound for either \(\beta\) is
\[
 \begin{split}
 \sup D_{\beta,\nu,\mathrm{main}}\le \mathfrak M_{\epsilon,\nu}
 :=T_\nu
 &+\mathcal G_{88/5}(A_s;\Re s_*,[.22,.5])\\
 &+\mathcal G_{49(\nu+1)/5}(A_{a,\nu};A,P)\\
 &+\mathcal G_{22(3+\epsilon)/5}(A_t;\Re t_*,[.22,.4]).
 \end{split}
\tag{13}
\]
It keeps both branches on full \(P\); the separately proved
forced-domain restriction is optional.

For a real transform cut \(\tau=.15\) or \(.5\), including the
entropy incoming dependence at \(\tau=.5\), retain a bare source
bound
\[
 T_\tau(a_*;y)-\Re P_*\le U_\tau
                      \quad\text{for every original private target }y.
\tag{14}
\]
The [direct-cut identity](research_mixed_terminal_real_transform_cut_budget.md)
eliminates these private targets exactly. With
\[
 \begin{split}
 D_\tau(z)&=g'(\tau+z)-g'(t_*+z)+2\pi i(\tau-t_*),\\
 C_\tau&=-\int_c^H\Im D_\tau(A+iy)\,dy,\qquad
 d_\tau=\Re D_\tau(\bar a),\\
 \kappa_{\tau,\nu}&=\nu+\tfrac12+\sigma_\tau,\qquad
 \sigma_{.15}=3/5,\quad \sigma_{.5}=5/3,
 \end{split}
\tag{15}
\]
the common bound is
\[
 \begin{split}
 \sup D_{\beta,\nu,\tau}\le \mathfrak C_{\tau,\nu}
 :=U_\tau+T_\nu+C_\tau
 &+\mathcal G_{88/5}(A_s;\Re s_*,[.22,.5])\\
 &+\mathcal G_{49\kappa_{\tau,\nu}/5}
                         (A_{a,\nu}+d_\tau;A,P).
 \end{split}
\tag{16}
\]
Its simultaneous curvature is
\(\operatorname{diag}((1+\beta)g_{h_b}''/2,
2g_{h_s}'',\kappa_{\tau,\nu}g_H'')\). The cut has height zero;
no main-height restriction on its transform variable is used.
The cancellations in the value and force of the direct-cut theorem
remain literal, including the off-stationary \(F_a\) term if an
evaluation point is not the original reference.

For the remaining reserve comparisons put
\[
 \begin{split}
 p_T&=\tfrac32g'(a_*)-g'(s_*+a_*),\\
 J_1&=\Delta\Im p_T+\Re\{B(s_*+a_*)-\tfrac32B(a_*)\}-\pi H,\\
 J_0&=J_1+\tfrac12\Re g(\bar a)+\pi H,\\
 G_s&=A_s,\qquad
 G_{a,1}=\Re\{L(s_*+a_*)-\tfrac32L(a_*)\},\\
 G_{a,0}&=G_{a,1}+\tfrac12\Re g'(\bar a).
 \end{split}
\tag{17}
\]
The same proof of (9) gives the improved joined-plane upper
\[
 \mathfrak E_\nu
 =J_\nu+\mathcal G_{88/5}(G_s;\Re s_*,[.22,.5])
       +\mathcal G_{49(1+\nu)/10}(G_{a,\nu};A,P).
\tag{18}
\]
If a terminal profile plus its selected halfweight is below the
original allocated plane by \(\rho_\sigma\), its full defect is
at most \(\mathfrak E_\nu-\rho_\sigma\). Source-cell refinements
may retain \(U_\sigma\), the reference restrictions and the plane
bound in the same original cell. Independent target intervals
remain unchanged.

Equations (13), (16), and (18) are three forms of a single
incoming-type rule. Their signed gain domains, original branches
and shared-parameter correlations are unchanged. The private-left
force-contraction theorem has the same property once its
separate barrier and force guards hold: its only altered force is
\(A_t+d_L\), and no incoming term enters those guards. Existing
whole-\(D_4\) guards are not thereby proved on whole \(D_3\).

## 4. What is already uniform on the type-three input domain

For \(b_*\in K_3\), the ordinary own-four images have
\[
 \Re a_*,\Re s_*\in(.24,.36),\qquad
 -.102<\Im a_*,\Im s_*<-.001.
\tag{19}
\]
The terminal endpoint rectangles, terminal-main barriers and
private intervals depend on \(\epsilon\), not \(\beta\).
The full-input ordinary barrier covers
\(-.12\le\Im b_*\le.08\); hence it covers all of \(K_3\).
The symmetric pair theorem allows \(|\Im b_*|\le.12\).
Thus every domain and curvature hypothesis used in
(13), (16), and (18) holds on both actual typed families.

The [ordinary-label completion](research_mixed_terminal_ordinary_label_completion.md)
already treats the full height interval \([-.1115,.068]\).
Together with the original finite seven-label envelope it removes
all six nonmain ordinary labels on \(K_3\), with loss at least
\(1/500\). Positive incoming heights use all four affine
last-row carriers; no negative-height specialization is needed.

Source eligibility is also available. Terminal type three uses
its original full ordinary-type-four endpoint input domain.
For terminal type four, the
[canonical source theorem](research_mixed_terminal_canonical_source_domain.md)
proves eligibility on \(K_3\): \(a,s\in P_4\), the oriented
bound is \(\Re a>.259\), and the original inverse equations
recover \(s\) and the same \(b\in P_3\).
The source filter permits its external inverse in \(P_3\cup P_4\).
It does not require that external inverse to have type four.

The completed [real-face extraction](research_mixed_terminal_uniform_face_reserves.md)
and [alias extraction](research_mixed_terminal_uniform_alias_reserves.md)
include both \(\beta=0\) images. Their cell bounds already give
(14) and the relevant raw reserves on source-feasible references.
The constant-profile height inequality also applies: it uses the
negative height of the shared own-four coordinate \(a_*\), not
the sign of the external type-three height.

What remains on \(K_3\) is quantitative: uniform negativity of
the main scalar bound, and sufficient joined-plane or direct
bounds for the other terminal labels. The original affine
reference and refined error enclosures are already present for
both \((\beta,\epsilon)=(0,0),(0,1)\). They do not supply the
height-integral cotangent bounds or negative scalar totals of the
completed \(\beta=1\) calculation outside its parameter domain.
No new critical equation, source partition, incoming-height
barrier, or incoming allocation is required.

More explicitly, fix \(\epsilon\) and let \(\mathcal F\) be the
nine real-face/entropy source families. Use any valid same-reference
uppers \(U_f\), allocated alias reserves \(\rho_k\), and constant
reserve \(\rho_C\). For each \(f\), start with
\(B_{f,\nu}=\mathfrak E_\nu+U_f\). If its transform coordinate
is fixed at \(\tau=.15\) or \(.5\), also permit the direct
upper \(\mathfrak C_{\tau,\nu}\) with that family's own \(U_f\).
This includes all six fixed-transform real faces, with either
private cut or private main state, and the entropy family at
\(\tau=.5\). Take the minimum of the available valid uppers.
For the type-four private-left/main-transform face one may further
include \(\mathfrak M_{\epsilon,\nu}+U_f\), but only after the
private-left symmetric-transfer barrier and force guards have
been proved on the reference set under consideration.

Thus a single sufficient remaining test is
\[
 \sup_{b_*\in K_3\setminus D_4}\ 
 \max_{\epsilon,\nu}\left\{
   \mathfrak M_{\epsilon,\nu},\
   \max_{0\le k<12}(\mathfrak E_\nu-\rho_k),\
   \mathfrak E_\nu-\rho_C,\
   \max_{f\in\mathcal F}B_{f,\nu}
 \right\}<0 .
\tag{20}
\]
Each displayed quantity is evaluated on the same canonical family
and same source cell when a cell bound is used. The only geometric
parameter is the complex input \(b_*\); all target variables have
already been bounded on their full independent intervals. Equation
(20) is an explicit sufficient scalar criterion, not a sign claim,
and its maximum is not asserted subharmonic. It is also permissible
to prove it on all \(K_3\), reusing the overlap as a check rather
than deleting it from a new cover.

## 5. A completed overlap consequence

**Corollary.** For incoming type three, preceding ordinary own
flag one, either terminal type, and
\[
                         b_*\in K_3\cap D_4,
\tag{21}
\]
the literal kernel (6), with \(\beta=0\), has the same raw gap
\(1/2600\) and finite gap \(1/5200\) as the
[completed type-four-disk comparison](research_mixed_terminal_uniform_kernel_completion.md).
It uses \(M_0,p_0\) from (5), and independent targets
\(b_R,a_R\in P\), \(\Im b=\Im b_*\), \(\Im a=.01\).

*Proof.* By (3), the canonical reference on (21) is the same
one enclosed by every completed whole-\(D_4\) analytic bound.
Equations (13), (16), and (18) show that those saved scalar
majorants, including their shared-force and same-source-cell
refinements, are unchanged when the boundary allocation is zero.
The direct private-left proof also discards only the zero-force
incoming cost. Its reference guards and its bare source bound
are unchanged on (21).

For completeness, the original image extractions can be reused
here for a source reason, not merely because the phases agree.
The \(D_4\) affine image rectangle still contains \(a_*(b_*)\);
every original closed cell intersecting that rectangle was retained.
Each source job is a theorem on the original endpoint input and
its stated inverse-feasible subset, and is independent of the
incoming halfweight. For (21), the separate \(K_3\) source
theorem just verified supplies those hypotheses. In particular
its inverse external leg lies in the allowed union \(P_3\cup P_4\).
The cell upper, entropy upper, constant plane, and all alias
penalties therefore remain valid. No source statement on an
arbitrary point of the rectangle or on all of \(D_4\) is used.

All 108 terminal/Fourier branches across both terminal types
thus retain the completed gap. The seven-label ordinary reduction
on \(K_3\) adds its nonmain losses and restores all 378 entries
per type. Real-cut endpoints pay the vertical alias sides.
The original physical complement and both parities are unchanged.
The finite envelopes give \(1/5200\) after the same tolerances.
The [real-color lift](research_mixed_terminal_profile_real_color_lift.md)
uses only these same profile bounds and is independent of the
incoming flag, so the bound holds also over the full real
terminal-color period, and for fixed ordinary-color jets.
\(\square\)

The overlap is a proper restriction. For example \(b_*=2/5\)
belongs to \(K_3\), while
\(|2/5-(.30-.052i)|^2=.012704>.064^2\).
This example is only a geometric domain comparison, not an
assertion that the point is realized by a finite word.
The corollary covers actual suffixes of length at least three
with flags \((0,1,\epsilon)\) whenever their incoming reference
lies in (21). It does not establish a complete new word family,
the full \(K_3\) estimate, nonplateau sectors, simultaneous
incoming selection, a nonzero whole-source amplitude, or
stability under arbitrary short fillings.
