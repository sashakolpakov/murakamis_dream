# A penultimate four followed by an unselected three

Research deduction, 6 November 2026.

The existing outgoing-three prefix theorems settle this configuration
at length four. For longer words, the current source comparisons reduce
it to four defects on a different canonical family. The unchanged
own-four reference bank does not supply those references or signs.
No numerical evaluation or new certificate is used here.

## 1. Original source and reference

Fix an actual word of length \(m\ge4\) with suffix
\[
 (n_{m-3},n_{m-2},n_{m-1},n_m)
       =(3+\gamma,4,3,3+\epsilon),\qquad \gamma,\epsilon\in\{0,1\}.
 \tag{1}
\]
Let \(c_*,b_*,a_*\) be its last three retained references, and
\(r_*,s_*\) the indices of its last two ordinary factors. Only
\(b\) is selected:
\[
 c=x_c+i\Im c_*,\quad b=x_b+iH,\quad a=x_a+i\Im a_*,\quad
 H=1/100,\quad x_c,x_b,x_a\in P=[.22,.45].
 \tag{2}
\]
The indices retain their original heights. The actual domains are
\(c_*\in K_{3+\gamma}\), \(r_*,b_*\in O_4\), and
\(s_*,a_*\in O_3\), where the
[typed input sets](research_mixed_typed_last_row_envelopes.md)
include attached \(c_*\) at \(m=4\), and the ordinary image bounds give
\[
 \begin{array}{c|cc}
 &\Re z&\Im z\\\hline
 O_4&(.24,.36)&(-.102,-.001)\\
 O_3&(.267,.433)&(-.065,.068).
 \end{array}
 \tag{3}
\]
Their reduced disks remain necessary reference constraints; independent
targets in (2) are not clipped to them.

Use the original phase
\[
 Q_\delta(v;x,y)=g(v+x)+g(v+y)-(2+\delta)g(v)
                  -g(x)-g(y)+2\pi ixv.
 \tag{4}
\]
The exact affected source and its allocated action are
\[
 \begin{split}
 {\cal B}_N&=
 |C_{1,N}(X_c,X_b)C_{0,N}(X_b,X_a)d_N(X_b)X_b^{-N}|
                                      |d_N(X_c)|^{\gamma/2},\\
 F&=Q_1(r;c,b)+Q_0(s;b,a)-g(b)-\gamma g(c)/2.
 \end{split}
 \tag{5}
\]
There is no outgoing halfweight at the type-three coordinate \(a\).
Original stationarity gives \(F_r=F_b=F_s=0\) at the reference.
Keep both original complex marginals:
\[
 \begin{split}
 M&=\Re F_*,\qquad
 p_c=g'(r_*+c_*)-(1+\gamma/2)g'(c_*)+2\pi ir_*,\\
 p_a&=g'(s_*+a_*)-g'(a_*),\qquad
 \Lambda=M+\Re\{p_c(c-c_*)+p_a(a-a_*)\}.
 \end{split}
 \tag{6}
\]
They cancel with the preceding source and unselected terminal source
when the pair is joined to the word.

## 2. A full-input reduction to four defects

Let \(L_0\) be the main maximum of \(Q_1(r;c,b)\) on
\([1/8,1/2]+i\Im r_*\). For the right factor set
\[
 R_0=\max_{.15\le x\le.5}\Re Q_0(x+i\Im s_*;b,a),\qquad
 R_R=\Re Q_0(1/2;b,a),
 \tag{7}
\]
and put \(W_1=-\Re g(b)-2\pi H\), \(W_0=0\), retaining
both complete-weight alternatives.

Three existing pointwise comparisons apply on this entire actual class:

* [Full-input ordinary-label completion](research_mixed_terminal_ordinary_label_completion.md)
  puts every left nonmain label below \(L_0-1/500\). Its incoming
  height interval \([-.1115,.068]\) contains both \(K_3,K_4\);
  its outgoing and index heights are exactly those in (2)--(3).
* [The own-three left-row theorem](research_mixed_selected_three_left_rows.md)
  puts the right cut at \(.15\) below \(R_0-1/125\).
  Its \(H\le7/625\) and two own-three height hypotheses hold.
* [Outgoing last-row transport](research_mixed_second_selected_outgoing_last_rows.md)
  puts the joint left-main/right-periodic-last-row profiles below
  \(\Lambda-1/400\), for both alternatives. Its initial inequality
  adds two individually allocated unselected ordinary-profile planes
  from [source assembly](research_mixed_three_row_source_assembly.md).
  Their internal tangents cancel by \(F_b=0\). The subsequent height
  derivative is \(\Im g'(b)-\Im g'(r+b)\), independent of \(c\),
  and \(\Im b_*<0\). Thus the original proof and loss do not require
  the incoming reference to be attached.

The horizontal aliases, joins and physical rows are included by the
[complete two-factor reduction](research_mixed_second_selected_plateau_reduction.md).
Its contour comparisons use outer heights of modulus at most \(.12\),
not the first endpoint equations. They therefore apply here too.
Define, for each fixed \((\gamma,\epsilon)\),
\[
 D_{j,\mu}=\sup_{\substack{\text{actual references of (1)}\\
                         (x_c,x_b,x_a)\in P^3}}
 \{L_0+R_j-\gamma\Re g(c)/2+W_\mu-\Lambda\},
 \quad j\in\{0,R\},\quad\mu\in\{0,1\}.
 \tag{8}
\]
**Proposition.** For every fixed word (1) and aggregate tolerance
\(\eta>0\), the entire finite product satisfies
\[
 {\cal B}_N\le C_\eta N^{A_\eta}
 \exp N\{\Lambda+
       \max(-1/400,D_{0,0},D_{0,1},D_{R,0},D_{R,1})+\eta\}.
 \tag{9}
\]
Both parities and every finite row are retained.

Indeed replace the left labels by their main maximum, the right left
cut by its main maximum, and pay the right periodic carriers by the
third comparison. The four remaining terms are (8). These are
individual profile inequalities before summation. A common upper
\(-\delta\) for (8) would yield raw loss \(\min(\delta,1/400)\)
and half that loss after tolerance. No such sign is proved here.

## 3. Exact family mismatch and the remaining scope

The [own-four penultimate criterion](research_mixed_terminal_penultimate_selected_criterion.md)
and [bank transfer](research_mixed_terminal_two_selected_reference_bank_transfer.md)
use suffix \((3+\gamma,4,4,3+\epsilon)\), identified with prefix
flags \((\epsilon,1,1)\) by
\[
 (e,\xi,t,a,s,b,r;c)
          =(e^o,\xi^o,a^o,u^o,z^o,v^o,b^o;c^o).
 \tag{10}
\]
For (1) the same original action permutation instead has flags
\((\epsilon,0,1)\). Its middle rows are
\[
 \begin{split}
 f_a^{(0)}&=j(a+s)+j(t+a)-2j(a)+i\pi(t-s),\\
 f_s^{(0)}&=j(a+s)+j(s+b)-2j(s)+i\pi(b-a),\qquad j=J'.
 \end{split}
 \tag{11}
\]
The other five rows have the bank transfer's same formal expressions.
By [the original action](research_mixed_open_word_hessian.md),
\[
 f_a^{(1)}-f_a^{(0)}=-g'(a),\qquad
 f_s^{(1)}-f_s^{(0)}=-g'(s).
 \tag{12}
\]
Neither difference vanishes: \(g'(z)=\operatorname{Log}(1-e^{-2\pi iz})=0\)
would imply \(e^{-2\pi iz}=0\). Thus an unchanged type-four root
cannot solve the required system.

The required family has the original disjoint updates
\[
 (e,t,\xi)=\operatorname{endpoint}_\epsilon(a),\quad
 (a,s)=\operatorname{ordinary}_0(t,b),\quad
 (b,r)=\operatorname{ordinary}_1(s,c).
 \tag{13}
\]
The full typed-disk maps, Brouwer and original principal Hessian give
its existence, uniqueness and holomorphic dependence, as in
[the prefix construction](research_mixed_prefix_residual_localization.md).
Every actual suffix (1) is included. This supplies no numerical box
or scalar sign. The older outgoing-three prefix banks instead have
flags \((\alpha,1,0)\). Their selected \(z^o\) also maps to the
new ordinary index \(s\), not selected retained \(b=v^o\); a
reference reversal does not transpose their finite selected source.

At \(m=4\), however, \(b\) is literally position two of the original
prefix \((3+\gamma,4,3)\). The
[first-four](research_mixed_second_selected_plateau_completion.md) and
[first-three](research_mixed_second_selected_first_three_plateau_completion.md)
completions directly give raw loss \(1/400\), with precisely (5)--(6).
For unrestricted \(m\ge5\), the four defects (8) remain.
The own-four completion additionally uses right-half-row domination
with negative own-four outgoing height and a simultaneous \(2g_{\Im s_*}\)
cost containing the absent own-four node term. Its saved height guard
and force certificates concern the different family (10).
The [directional main](research_mixed_second_selected_directional_budget.md)
and [real-half-row](research_mixed_second_selected_half_row_budget.md)
formulas for an own-three right factor remain available, but their old
certified signs do not cover (13). This limitation is not an actual-source
counterexample.
