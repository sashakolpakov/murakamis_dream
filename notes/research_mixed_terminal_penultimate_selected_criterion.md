# A complete two-boundary criterion for the penultimate selection

Research deduction and fixed saved-data protocol, 6 November 2026.
Only the penultimate retained coordinate is selected here. Its outgoing
neighbor stays at its original height, so the completed two-selected
terminal theorem is not applied with one selection removed. Instead
the original two ordinary factors have a complete finite-source
reduction with both boundary marginals. The two remaining main
budgets can be bounded using the already saved vertices and a new
explicit clipped quadratic. This note asserts no new numerical sign.

## 1. Original source and exact reference

Keep the suffix and canonical family of the
[reference reconstruction](research_mixed_terminal_two_selected_reference_reconstruction.md):
\[
 (n_{m-3},n_{m-2},n_{m-1},n_m)
     =(3+\gamma,4,4,3+\epsilon),\qquad m\ge4.
 \tag{1}
\]
In the notation \((c,r,b,s,a)\), \(c,b,a\) are the three
retained coordinates, and \(r,s\) are ordinary indices. The
external coordinate \(c_*\) lies in \(K_{3+\gamma}\); the
original canonical reference has
\[
 r_*,b_*,s_*,a_*\in O_4,\qquad
 .24<\Re(r_*,b_*,s_*,a_*)<.36,\qquad
 -.102<\Im(r_*,b_*,s_*,a_*)<-.001.
 \tag{2}
\]
The [bank transfer](research_mixed_terminal_two_selected_reference_bank_transfer.md)
provides the same complete reference coverage as before. No new
reference equation or root is required. The original terminal family
is used to identify this reference, not to insert a selected terminal
source into the present product.

Put \(P=[.22,.45]\), \(H=1/100\), \(X_z=e^{-2\pi iz}\).
Select \(b\) at height \(H\). Keep \(c,a\) at their original
reference heights, with all three real targets independent in \(P\).
The literal allocated source is
\[
 \mathcal B_N=
 |C_{1,N}(X_c,X_b)C_{1,N}(X_b,X_a)d_N(X_b)X_b^{-N}|
                       |d_N(X_c)|^{\gamma/2}|d_N(X_a)|^{1/2}.
 \tag{3}
\]
There is one complete selected weight. Both outer halfweights are
unselected allocations, and the incoming one is absent when
\(\gamma=0\).

Retain the original primitive, chirps and logarithmic lifts, and set
\[
 \begin{split}
 Q(r;c,b)&=g(r+c)+g(r+b)-3g(r)-g(c)-g(b)+2\pi icr,\\
 F_{\rm pair}&=Q(r;c,b)+Q(s;b,a)-g(b)
                         -\frac\gamma2g(c)-\frac12g(a),\\
 M_*&=F_{\rm pair}(q_*),\\
 p_c&=g'(r_*+c_*)-(1+\gamma/2)g'(c_*)+2\pi ir_*,\\
 p_a&=g'(s_*+a_*)-\frac32g'(a_*),\\
 \Lambda(c,a)&=\Re\{M_*+p_c(c-c_*)+p_a(a-a_*)\}.
 \end{split}
 \tag{4}
\]
The original derivatives in \(r,b,s\) vanish. In particular,
\[
       g'(r_*+b_*)+g'(s_*+b_*)-3g'(b_*)+2\pi is_*=0.
 \tag{5}
\]
The two boundary derivatives in (4) are not discarded. They cancel
against the adjoining original phases only when the corresponding
larger source is assembled.

## 2. Complete ordinary profiles, including the changed orientation

For each ordinary factor retain the bare main maximum \(R_0\),
real cuts \(R_L,R_R\), and all four affine last-row carriers.
The [complete ordinary compiler](research_mixed_plateau_window_concave_profiles.md)
includes their physical tails, revived rows, horizontal aliases,
vertical sides and zero-mode joins. Equivalently one can take the
maximum \(R_1\) of the four last-row carriers before forming the
two-factor maximum. Thus (3) has 98 expanded profile/weight choices,
or 32 choices with each last-row envelope already maximized.

The following replacements are valid with every other term fixed.

| Factor and profile | Bound | Applicable original domain |
|---|---|---|
| Left: all six nonmain labels | below its main maximum by \(1/500\) | Incoming \(c_*\in K_3\cup K_4\), outgoing height \(H\), index height in (2) |
| Right: left real cut | below its main maximum by \(1/1000\) | Incoming height \(H\), outgoing and index heights in (2) |
| Right: real half row | below its main maximum by \(1/20\) | The same full independent target and height domain |

The first row is the
[full-input ordinary-label completion](research_mixed_terminal_ordinary_label_completion.md).
Both typed \(c\)-height ranges lie inside its containing interval
\([-223/2000,17/250]\). The other rows are respectively the
[outgoing-four left-cut theorem](research_mixed_second_selected_outgoing_four_left_cut.md)
and [completed outgoing-four half-row theorem](research_mixed_second_selected_outgoing_four_half_row_completion.md).
They have the required orientation: the selected coordinate is
incoming, and the outgoing coordinate is unselected and negative.
No theorem with selected outgoing height is substituted for them.

The only remaining nonmain profile is the right last-row envelope.
It is paid jointly with the left main profile, not by declaring
pointwise right-main domination. The proof of
[the outgoing-last-row theorem](research_mixed_second_selected_outgoing_last_rows.md),
equations (6)--(25), applies with
\((z_1,z_2,z_3)=(c,b,a)\) and \((\alpha,\beta)=(\gamma,1)\).
Here is the external-domain justification for that application.

At the original negative height of \(b_*\), the individual
unselected main and last-row supporting-plane bounds follow from
[the full ordinary source assembly](research_mixed_three_row_source_assembly.md),
Sections 1--2. Their complete typed products include the coupled
left map \((r_*,b_*)=B_1(c_*,s_*)\) and the right map
\((s_*,a_*)=B_1(b_*,t_*)\), with \(t_*\) the original attached
terminal leg. The typed input roles and strong output bounds are
those in the reconstruction and canonical source-domain proofs.
The individual row estimates were proved before taking the modulus
of their sum. They therefore provide the unselected main/last-row
baseline, with both boundary planes (4), also on this complete
canonical \(K\) family.

Moving the shared \(b\)-height from \(h_b=\Im b_*<0\) to \(H\),
it is outgoing in the left factor. Its left-profile derivative is
exactly the difference of the two original logarithm arguments in
equation (10) of the cited proof; the incoming \(c\)-chirp is
independent of the moved height. Hence that derivative bound has no
restriction on \(\Im c_*\) beyond the original source domain.
The right last-row envelope changes by exactly \(2\pi h_b\).
The rest of that proof uses only \(h_b<0\), \(H=.01\), and the
full real targets \(P\). Its elementary forced-weight bound also
holds on all of \(P\). Consequently each right last-row carrier,
with either complete selected-weight alternative, has joint defect
strictly below \(-1/400\) relative to (4).

This also pays the original double-last-row choices: first replace
their left carrier by the left main maximum using the first row of
the table, then apply the joint right-last-row bound. No carrier,
physical row or alias side has been omitted.

## 3. The exact main/main criterion

Let \(\mu=1\) denote the factorial alternative and \(\mu=0\)
the forced one. Set \(\Delta=H-\Im b_*>0\),
\(\bar b=b_*+i\Delta\), and
\[
 \begin{split}
 B(z;\Delta)&=g(z+i\Delta)-g(z)-i\Delta g'(z),\\
 L(z;\Delta)&=g'(z+i\Delta)-g'(z),\\
 T_\mu&=\Re\{B(r_*+b_*;\Delta)+B(s_*+b_*;\Delta)
                                      -3B(b_*;\Delta)\}
                  +(1-\mu)\Re g(\bar b)-2\pi\mu H,\\
 A_r&=\Re L(r_*+b_*;\Delta),\\
 A_{b,\mu}&=\Re\{L(r_*+b_*;\Delta)+L(s_*+b_*;\Delta)
                                     -3L(b_*;\Delta)\}
                         +(1-\mu)\Re g'(\bar b),\\
 u&=\Re L(s_*+b_*;\Delta)-2\pi\Delta<0.
 \end{split}
 \tag{6}
\]
Original stationarity (5) cancels the linear height response. The
lifted reference has forces \((0,A_r,A_{b,\mu},u,0)\) in the
order \((c,r,b,s,a)\). Unlike the two-selected problem, there
is no compensating positive \(a\)-lift force at \(s\).

Both main indices can be restricted to \([.22,.5]\). For \(r\)
use the [full-input barrier](research_mixed_terminal_full_input_index_barrier.md).
For \(s\) use Proposition 3, \(\beta=1\), of
[the original horizontal-concavity theorem](research_mixed_second_selected_horizontal_concavity.md),
which imports the cap-independent index lemma of the
[next-four endpoint proof](research_mixed_first_four_next_four_endpoint_budget.md).
Its incoming height is \(H\), and its outgoing and index heights
are exactly (2). The incoming \(c\) does not occur in that
derivative. Bare ordinary concavity on the original index intervals
extends both positive lower-face derivatives to those intervals.

On this localized product, the exact decomposition into the four
pair phases \(V(r,c),V(r,b),V(s,b),V(s,a)\) and the node terms
allows the [symmetric pair reserve](research_mixed_terminal_symmetric_pair_costs.md).
It gives simultaneous retained costs
\[
             2g_{h_r},\qquad(\mu+1)g_H,\qquad2g_{h_s}
 \tag{7}
\]
at \(r,b,s\). All pairs have real coordinates in \([.22,.5]\)
and height moduli at most \(.12\). The remaining positive boundary
costs may be discarded because their lifted-reference forces are
zero. Every connecting segment uses the original reference center.

Let \(G_r,G_{b,\mu},G_s\) be the exact Bregman conjugates of
(7), with their respective reference centers. Their targets are
\([.22,.5],I_\mu,[.22,.5]\), where
\(I_1=P\), \(I_0=[.4,.45]\). The simultaneous complete-weight
branch theorem justifies the forced domain; its \(b\)-gain remains
signed. Define
\[
              \mathfrak P_\mu=T_\mu+G_r(A_r)
                                   +G_{b,\mu}(A_{b,\mu})+G_s(u).
 \tag{8}
\]
Integrating the simultaneous costs bounds the main/main defect by
(8), without assuming independent actual force extrema.

**Theorem 1.** For any uniform containing bounds
\(\mathfrak P_\mu\le P_\mu^+\) on this reference family and
any \(\eta>0\), the complete original product (3) satisfies
\[
 \mathcal B_N\le C_\eta N^{A_\eta}
 \exp N\left\{\Lambda(c,a)
        +\max\{-1/400,P_0^+,P_1^+\}+\eta\right\}.
 \tag{9}
\]
It retains both parities, both original boundary marginals, all
independent plateau targets and every original finite-contour term.

Indeed Section 2 reduces the complete profile maximum to the two
main/main defects and the paid joint last-row bound. Section 3
bounds the former by (8). Apply the complete finite-source envelope
with one total tolerance. This proves (9); it proves no sign for
\(P_0^+,P_1^+\).

## 4. Root-free bounds for the sole unopposed index force

Write the projected \(s\)-center interval as \([s_-,s_+]\).
Impose the exact saved guard \(|h_s|<.061\) throughout the family.
The [cubic curvature theorem](research_mixed_terminal_cubic_cost_and_response_bounds.md)
then gives
\[
          (2g_{h_s})''(x)\ge19(1/2-x),\qquad .18\le x\le.5.
 \tag{10}
\]
Put
\[
         m=19(1/2-s_+)>0,\qquad D=s_+-.22>0.
 \tag{11}
\]
For \(A\ge0\), define the explicit convex function
\[
 Q(A)=\max_{0\le d\le D}\{Ad-md^2/2\}
 =\begin{cases}
       A^2/(2m),&0\le A\le mD,\\
       AD-mD^2/2,&A\ge mD.
   \end{cases}
 \tag{12}
\]
Extend it by \(Q(A)=0\) for \(A\le0\). This extension is
convex and nondecreasing.

**Lemma 2.** At every actual reference, \(G_s(-A)\le Q(A)\)
for \(A\ge0\).

*Proof.* For targets to the right of the reference center the
negative linear force and nonnegative Bregman cost give value at
most zero. To the left, the segment curvature is at least
\(19(1/2-s_+)\), since every point is at most its actual center
and hence at most \(s_+\). Its remainder is at least
\(md^2/2\), while \(0\le d\le s_*^R-.22\le D\).
Maximizing gives (12). The original center is an admissible target,
so zero remains legitimate for this ordinary-index gain. \(\square\)

There is a stronger bound retaining the cubic part of the same
curvature. Define the exact convex, nondecreasing function
\[
 F(A)=\max_{0\le d\le D}
       \{Ad-md^2/2-19d^3/6\}.
 \tag{13}
\]
It equals zero for \(A\le0\). For \(A>0\), put
\[
 d_{\rm hi}(A)=\min\{D,A/m\},\qquad
 d_{\rm lo}(A)=\min\{D,A/(m+19d_{\rm hi}(A)/2)\},\qquad
 R(A)=Q(A)-\frac{19}{6}d_{\rm lo}(A)^3,
 \tag{14}
\]
and set \(R(A)=0\) for \(A\le0\).

**Lemma 3.** At every actual reference and \(A\ge0\),
\[
                   G_s(-A)\le F(A)\le R(A)\le Q(A).
 \tag{15}
\]

*Proof.* At distance \(y\) to the left of the reference center,
(10) bounds the curvature below by \(m+19y\). Integrating
this affine lower bound yields the remainder
\(md^2/2+19d^3/6\), proving the first inequality. For
\(A>0\), let \(d_*\) maximize (13). If \(d_*<D\),
the strictly decreasing derivative of its objective vanishes:
\(A=d_*(m+19d_*/2)\). This gives
\(d_*\le\min(D,A/m)=d_{\rm hi}\) and then
\(d_*\ge A/(m+19d_{\rm hi}/2)\ge d_{\rm lo}\).
If \(d_*=D\), its nonnegative left derivative gives
\(A\ge mD+19D^2/2\), so \(d_{\rm hi}=d_{\rm lo}=D\).
Thus in both cases
\[
 F(A)=Ad_*-md_*^2/2-19d_*^3/6
                  \le Q(A)-19d_{\rm lo}(A)^3/6.
\]
The case \(A=0\) is immediate. The final inequality is the
nonnegativity of the subtracted term. \(\square\)

All of \(Q,d_{\rm hi},d_{\rm lo},R\) are explicit rational formulas on rational
data. Convexity is required of the exact function \(F\), not
of its displayed rational upper \(R\). No claim that \(R\)
is convex is made.

## 5. Fixed reuse of the saved vertices, without new analytic data

The sole proposed recombination uses the complete record
repro/results/research-mixed-terminal-two-selected-lift-budgets.json.gz,
SHA256
`55d8252d1a34bb6ad514cdc77c43376c7b4cbc42fd76617b9b21ef1868c8024d`,
and its successful
[saved audit](../repro/results/research-mixed-terminal-two-selected-lift-budgets-saved-audit.json),
SHA256
`126b39c133170b668ab4e5ffe955a7064dd892521830a7c5b9c8e947226944be`.
The original harmonic projection, case associations, coordinates,
slabs, means, primitive endpoints and all input hashes remain fixed.
The exact \(s\)-height guard in Section 4 must pass before using
the coefficient 19; no domain clipping or fallback coefficient is
authorized by this protocol.

For each of the same 96 vertices retain the recorded \(r,b\)
gain certificates and their upper endpoints. The exact actual
quantity \(A=-u\) has formula
\[
                          A=\kappa(1+I_{sb}).
 \tag{16}
\]
Replace only the old linear shared debit \(\mathcal D\) by
\(R(A)\). Thus the stronger proposed saved-vertex upper is exactly
\[
             U^{\rm pen}_\mu(v)
                   =U^{\rm two}_\mu(v)-\mathcal D(v)
                                      +R(\kappa(1+I_{sb})).
 \tag{17}
\]
The signed forced trial and \(b\)-gain retain their common
\(q_e\). The vertical trial, \(r\)-force and \(b\)-force are
unchanged. The factor \(1+I_{sb}\) need not be artificially
clipped; the convex zero extension of \(F\), and \(R=0\)
there, handle any enclosing
vertex that does not itself satisfy the strict actual force sign.
The actual scalar comparison is used only at \(A=-u>0\);
no source gain at a nonactual negative \(A\) is being asserted.
Replacing \(R\) by \(Q\) gives a weaker valid vertex upper
and may be retained as a separate recorded comparison.

Before rational evaluation, use the exact \(F\) in the place of
\(R\) in (17). This expression is separately convex in
\((\kappa,I_b,I_{rb},I_{sb})\), and additionally \(q_e\) for
the forced alternative. This follows from the exact force-convex
conjugates, the affine forced trial, the nonnegative quadratic
vertical upper, and the convex function \(F\) of a separately
affine argument. Successive endpoint bounds therefore justify the
same 16 factorial and 32 forced vertices per terminal type. Only
their saved certified \(r,b\) gain upper values and the rational
upper \(R\) for \(F\) are substituted. Neither convexity of
a rounded saved gain nor convexity of \(R\) is assumed.

A standalone checker may verify those 96 rational replacements,
all four maxima, the exact guards and every inherited association.
It must retain every outcome and before/after binding, without
generating another gain, root, analytic value, source value or
parameter subdivision. This fixed recombination is unrun here.
Until its two maxima for each terminal type are strictly negative,
(9) remains a criterion rather than a new finite-source gap.

If those signs are established, adjoining the original unselected
terminal source cancels \(p_a\), and the preceding factor or cap
cancels \(p_c\), with the integer weights restored exactly once.
That would treat the penultimate-only plateau sectors. Neither
this conditional implication nor the present criterion supplies
their currently unproved signs or a whole-source theorem.
