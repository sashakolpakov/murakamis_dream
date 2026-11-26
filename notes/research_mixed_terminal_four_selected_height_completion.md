# Selected and attenuated type-four input heights of complete terminal sources

Research deduction, 5 November 2026. This extends the selected-input
argument to the complete type-four terminal polynomial and records
unselected negative-height attenuation for both terminal types.
The stronger alias reserve has been extracted from the completed
replay; the entire unselected terminal theorem is proved in
[mixed plateau completion](research_mixed_full_unselected_plateau.md),
Corollary 3. No source evaluation or root calculation is performed here.

## 1. Exact quantity and reference plane

Let \(a_*=A+ic\) be an actual type-four input of a type-four terminal
block in a fixed word of length \(m\ge2\). Thus
\(-.108<c\le-.001\). Put
\[
 \Pi=P_1-g/2,\quad p=\Pi'(a_*),\quad
 B(a_*;y)=\Re\Pi(a_*)+\Re p\,(y-A)-\kappa(y-A)^2,
 \quad \kappa=1/2500000.
 \tag{1}
\]
Take \(y\in P=[.22,.45]\), \(a_h=y+ih\), \(0\le h\le7/500\).
The actual selected halfweight is
\(e^{-\pi Nh}|d_N(e^{-2\pi ia_h})|^{1/2}\), with rate
\(q_1(h)=\max\{-\Re g(a_h)/2-\pi h,0\}\).
At the reference height put \(q_0(c)=-\Re g(y+ic)/2\).
Horizontal convexity of \(\Re g\) gives
\(B_0(a_*;y)+q_0(c)\le B(a_*;y)\), where \(B_0\)
is the same supporting plane formed with the bare action \(P_1\).
Thus each baseline bare current comparison supplies its allocated
comparison before incoming-height transport.

**Completed alias reserve.** All twelve penalized alias endpoint families
in the completed terminal-four source certificate have bare deficit
less than \(-1/10\) relative to their fixed-reference bare plane, at
every actual reference and every admitted real target. The
[exact saved-bound extraction](research_mixed_terminal_four_alias_reserve.md)
passed with [record](../repro/results/research-mixed-terminal-four-alias-reserve.json)
SHA256 `6ff887ab81798ea4e237dfaf39cbd99f17cfecda367bc4e551f92ea61da351d0`.
It checks all 22,932 alias jobs: 21,936 saved source bounds and 996
jobs containing only proved geometric exclusions. A wholly excluded
job has no required actual reference; it is not assigned a numerical
source bound. No phase was reevaluated.

**Theorem 1.** For every \(\tau>0\),
fixed small ordinary-color disks and polynomial factors give
\[
 |\mathcal V_{1,N}(w,e^{-2\pi ia_h})|\,
 e^{-\pi Nh}|d_N(e^{-2\pi ia_h})|^{1/2}
       \le C_\tau N^{A_\tau}e^{N(B(a_*;y)+\tau)}
 \tag{2}
\]
for all sufficiently large integer levels of either parity. Every
fixed ordinary-color derivative has the same rate on a smaller disk.

All internal private Fourier alternatives and Newton indices remain
inside the literal source
\[
 \mathcal V_{1,N}(w,X)
 =\sum_{i,j<N}\frac{X^{-i}p_i(X)}{P_i^2}
                  \frac{p_j(r^i)\mathcal H_N(w,r^{-j})}{P_j^2}.
 \tag{3}
\]
The exact wall \(i+j<N\) is retained. The selected factor in (2)
belongs only to the incoming retained coordinate.

## 2. Central reduced currents at the selected height

Use the exact reduced interpolation and its phase from
[the complete reduced-current proof](research_mixed_terminal_four_reduced_currents.md):
\[
 \Phi_1(a;e,t)
 =S(e)+g(a+t)+g(e+t)-3g(t)-g(e)-g(a)
                      -i\pi(e-e^2)/2+2\pi iat.
 \tag{4}
\]
The transform rectangle is \([.15,.5]+i[-.12,.12]\);
the private rectangle is \([.27,.49]+i[-.055,.04]\).
The complete endpoint coefficient inside \(S(e)\) is kept coherent.

The incoming marginal in (4) is the same as in
[selected physical and complex transport](research_mixed_terminal_selected_height_rows.md).
The stronger argument in Section 3 of
[selected terminal-three completion](research_mixed_terminal_three_selected_height_completion.md)
therefore gives zero additional allocated cost whenever \(\Re t\ge.18\).
It depends only on \(a,t\), not on the private coordinate or own type.
On the entire transform rectangle its residual cost is bounded by
\[
 \gamma_c(y,\Re t)
   =\pi(-c)[3/4-3y/2-2\Re t]_+<.041.
 \tag{5}
\]

For the zero-mode left strip, the actual type-four endpoint ranges give
\[
 -.108<h_t<-.020,\qquad -.051<h_e<-.019.
 \tag{6}
\]
Take \(.15\le v=\Re t\le.18\), transform height between zero and
\(h_t\), and private height between zero and \(h_e\).
Then
\[
                         \Re\Phi_{1,t}(a_h;e,t)>0.
 \tag{7}
\]
Indeed set \(r=e^{2\pi\Im t}\), \(s=e^{2\pi\Im e}\),
\(R=e^{-2\pi h}\). The larger bounds
\(1/2<r\le1\), \(s>7/10\), \(R>10/11\) hold even if the
private height is lowered to \(-.055\).
The incoming and private shifted real parts lie respectively in
\([.37,.63]\) and \([.42,.67]\). Thus
\[
 \begin{split}
 e^{2\Re\Phi_{1,t}}
 &=\frac{|R-r e^{-2\pi i(y+v)}|^2
          |1-rs e^{-2\pi i(v+\Re e)}|^2}
         {|1-r e^{-2\pi iv}|^6}\\
 &>
 \frac{\{100/121+1/4+20/33\}(561/400)}{(6/5)^3}>1.
 \end{split}
 \tag{8}
\]
We used
\(\cos2\pi(y+v)<-2/3\),
\(\cos2\pi(v+\Re e)<-2/5\),
and \(\cos2\pi v>2/5\).
The exponential and trigonometric endpoint bounds follow from the
same elementary Taylor inequalities used in the terminal-three
argument. The last comparison is an exact rational inequality.

Consequently the zero-mode horizontal points with \(v<.18\), and
their private joins, may be compared pointwise to \(v=.18\).
At that coordinate use zero-cost incoming-height transport, then the
original fixed-reference horizontal plane or private flattened face.
The actual transform root has \(\Re t_*>.246\). Even the weaker
joint reduced Hessian floor \(\pi/100\) gives a strict horizontal
index loss there:
\[
                  \frac{\pi}{200}(.246-.18)^2>1/20000.
 \tag{9}
\]
This is a phase comparison, not a deformation through a moving saddle.

At the transform joins \(v=.15,.5\), use separate height convexity at
the new incoming target. The endpoint at actual transform height is
covered above. At transform height zero, the dependence on \(a\) has
exactly the real-transform rate \(R(t;k)\) from the selected-row
proposition, plus an incoming-independent private expression.
Its continuum inequality therefore bounds every such point by its
allocated baseline value. The completed flattened and corner tests
apply there. Double joins are reduced by two separate convexity steps.
The incoming halfweight is constant in both index coordinates.

For alias endpoint families, (5) and the completed reserve leave more
than .059 below the allocated plane. The original two-index residue
reduction then controls all vertical aliases using these penalized
endpoints and the zero-mode boundary endpoints just handled.
The same reduced Hessian gives separate height convexity throughout
the required regular rectangles at \(a_h\). No diagonal-height
convexity or raw independent cut-face estimate is assumed.
Thus every central current has upper rate at most \(B\), with a
strict reserve on the nonhorizontal pieces.

## 3. The literal physical complement

Use exactly the source partition of
[whole terminal-four completion](research_mixed_terminal_four_full_completion.md),
with its comparisons now supplied by the completed actual-reference
certificate. The following operations preserve all internal rows:

1. Remove the entire coherent end-index sectors first. Section 2 of
   selected terminal-three completion is an own-type-independent
   lemma: at an actual type-four input \(P_\epsilon(a_*)>1.17\),
   the bare horizontal plane exceeds .99, and the selected halfweight
   costs at most .048 relative to its negative-height value.
   The original all-height end-index majorant is below .868.
   Both whole end tails therefore have allocated gap \(7/100\)
   after a small total tolerance.

2. For \(\delta<t=i/N<.15\), retain each whole
   \(\mathcal H_N\), then split only its private index as in
   [the left-strip proof](research_mixed_terminal_four_left_strip.md).
   Its central-private derivative
   \(\partial_t\Re\Phi_1>\log(13/10)\) holds for every
   \(a\in P+i[-.12,.12]\) and every admitted complex private
   height. Transport to real \(t=.15\) first. At the anchor,
   the selected-row inequality is independent of the private
   coordinate and its residue penalty. The original flattened,
   corner and zero-transform-height private-alias comparisons apply.
   Its two real-private corner estimates likewise admit the entire
   incoming height rectangle; they transport to the same real
   anchors. The Newton sum inside \(\mathcal H_N\) is never split.

3. For \(.15\le t<.5\), the central private interval is controlled
   by Section 2. In both private complements use
   [the private-tail theorem](research_mixed_terminal_four_private_tails.md).
   Its derivative in the real private index is independent of \(a\).
   Transport that index to \(.27\) or \(.49\) before applying
   index-height convexity. The resulting transform main, join and
   alias anchors are precisely those bounded in Section 2.
   The endpoint polynomial remains whole throughout.

4. For \(t\ge.5\), the
   [right-triangle bound](research_mixed_terminal_four_right_triangle.md)
   is a positive majorant of the original triple summands.
   Apply the finite selected-row inequality to the exact external
   factor \(X^{-i}p_i(X)\) of each summand; all other factors,
   including ordinary-color derivatives, are independent of \(a\).
   Its allocated baseline gap is supplied by the completed raw
   half-transform comparison. Restriction to the disjoint remaining
   transform range is legitimate for this positive majorant.

Choose physical splitting indices first and put the residue cuts
halfway between them, exactly as in the original completion. The
even-level row \(i=N/2\) belongs only to the right triangle.
All \(O(1/N)\) changes at \(.15,.5,.27,.49\) lie in regular
anchor neighborhoods and are absorbed in one tolerance.
No whole coherent end row is later restricted in either inner index.

This exhausts (3). The old exact interpolants and zero-safe physical
bounds hold uniformly on small fixed ordinary-color disks.
Choose all rate tolerances to sum to less than \(\tau\), then sum
the polynomial prefactors. This proves (2).
Cauchy's formula supplies the stated derivatives, with both parities
and revived finite rows retained.

## 4. Unselected attenuation for both terminal types

Let the terminal own type be \(3+\epsilon\), \(\epsilon=0,1\),
and let its actual incoming type again be four. Set
\[
 \Pi_\epsilon=P_\epsilon-g/2,\qquad
 p_\epsilon=\Pi_\epsilon'(a_*),\qquad
 B_\epsilon(a_*;y)=\Re\Pi_\epsilon(a_*)
       +\Re p_\epsilon(y-A)-\kappa(y-A)^2.
 \tag{10}
\]
For \(c\le k\le0\), put \(a_k=y+ik\). Its unselected
Fourier halfweight has upper rate
\(q_0(k)=-\Re g(a_k)/2\): on this rectangle
\(\Re g(a_k)<0\), so this is the larger of the two actual
Fourier alternatives, including the limiting real height.

**Corollary 2.** Uniformly for \(y\in P\) and \(c\le k\le0\),
\[
 |\mathcal V_{\epsilon,N}(w,e^{-2\pi ia_k})|
       |d_N(e^{-2\pi ia_k})|^{1/2}
 \le C_\tau N^{A_\tau}e^{N(B_\epsilon(a_*;y)+\tau)}.
 \tag{11}
\]
Both level parities and every fixed ordinary-color derivative are
included on smaller fixed color disks.

*Proof.* The proof uses the same exact source partitions as Theorem 1
and the [terminal-three selected theorem](research_mixed_terminal_three_selected_height_completion.md).
Here are all changes needed on the negative incoming path.

For every physical transform rate with \(t\ge.15\), equation (10)
of the [selected-row proof](research_mixed_terminal_selected_height_rows.md)
gives
\[
 \frac{d}{dk}\{R(t;k)+q_0(k)\}\le-\pi/100.
 \tag{12}
\]
The same zero-safe finite product argument therefore transports each
incoming-dependent physical factor from \(c\) to \(k\) with no
positive rate allowance. It applies termwise to positive majorants
and to the whole inner coefficient of each fixed outer row, but does
not infer transport of a cancelling outer sum from its total value.

For a complex transform coordinate with \(\Re t\ge.18\),
the negative-path argument already proved in Section 3 of that
terminal-three theorem gives allocated derivative strictly below zero.
For \(.15\le\Re t<.18\) on the zero-mode main and joining
heights, the same transform push remains valid: its incoming radial
factor is now \(R=e^{-2\pi k}\ge1\), which only strengthens
the numerator lower bounds used there and in (8). Thus the actual
horizontal and all flattened zero-mode anchors have the same bounds.
Separate index-height convexity at the moved incoming coordinate
again controls every join. All complex alias endpoints incur at most
the same \(\gamma_c\) in (5), since shortening the negative path
cannot exceed its integral bound to zero. The completed gap \(1/10\)
for each terminal type pays this cost.

The coherent end-index estimates and, for own type three, the positive
low/high/near-half Newton estimates remain uniform at \(a_k\).
Their halfweight cost satisfies
\[
 q_0(k)-q_0(c)
 \le q_0(0)-q_0(c)
 \le \tfrac12\pi(-c)(1/2-y)<.048.
 \tag{13}
\]
Hence the improved bare plane \(>.99\) leaves exactly the same
strict reserves as before. The real low-transform strip first moves
to \(t=.15\), using the old derivative bounds valid for every
incoming height in \([-.12,.12]\); apply (12) only at that
real-transform anchor. The private or Newton exterior derivatives
are incoming-independent. The right physical positive majorants use
(12) termwise. No other part of either source partition changes.

The original exact interpolants, half-grid slivers, whole coherent
inner sums and zero-safe physical products are therefore retained.
Choose the shared tolerance and fixed color disk as before.
This proves (11), including its ordinary derivatives. \(\square\)

## 5. What the bounds retain for subsequent assembly

The original complex affine plane at the moved incoming height is
\(B(a_*;y)-\Im p\,(h-c)\). Consequently (2) still retains the fee
\[
                            (h-c)\Im p
 \tag{14}
\]
relative to that plane. A neighboring factor must supply the matching
imaginary tangent or an appropriate loss. No cancellation is assumed
inside this one-factor theorem. Corollary 2 similarly retains
\((k-c)\Im p_\epsilon\) relative to its original complex affine
plane. Neither conclusion pays that adjacent-incidence term by itself.

The conclusions are upper bounds for the entire terminal factor with
a selected or attenuated type-four incoming coordinate. They do not
give a nonzero selected Gaussian, handle other selected coordinates automatically, or prove
the remaining nonplateau and full open-word comparisons.

