# The next boundary selection: the second retained coordinate

Research deduction, 6 November 2026. No numerical calculation, root
proposal, source evaluation, or new cover is used here.

The complete selected first-coordinate comparisons leave a different
local problem when the second coordinate is selected. With the first
coordinate unselected, the two ordinary factors incident to the second
coordinate form the smallest block containing both selected incidences.
With both coordinates selected, the corresponding left block contains
the cap and two ordinary factors. This note gives their exact finite
products and a finite-current reduction. The signs of the resulting
joint comparisons are not asserted.

## 1. Actual references and the scope of the older selected theorem

Fix an actual mixed open word of length \(m\ge4\), put
\(h=m-1\), and assume its second type is four. Write
\[
 \epsilon_1=\alpha,\qquad \epsilon_2=1,\qquad
 \epsilon_3=\beta,\qquad \alpha,\beta\in\{0,1\},\qquad
 r_j=a_j+ic_j.
 \tag{1}
\]
Here \(r_j=t_j\) are retained coordinates. The ordinary index
at vertex \(j\) is \(s_j^*\). Both vertices 2 and 3 are
ordinary, including at \(m=4\); no private terminal leg is
treated as an ordinary index.

Put \(P=[.22,.45]\). Select position 2 at a fixed
\(0<H_2\le.014\). If position 1 is unselected, put
\(z_1=x_1+ic_1\); if it is selected, then \(\alpha=1\)
and put \(z_1=x_1+iH_1\), where \(H_1=1/100\).
In either case \(z_2=x_2+iH_2\), \(z_3=x_3+ic_3\),
and \((x_1,x_2,x_3)\in P^3\). Positions beyond 3 may be
unselected, with additional selections in the safe interior set
\(I_m=\{6,\ldots,m-5\}\) as in the
[interior-selection theorem](research_mixed_interior_selected_plateau.md).

The completed [selected ordinary theorem](research_mixed_selected_plateau_support.md)
requires both retained references of each factor to lie in
\[
 R_3=[.30,.39]+i[-.03,.02],\qquad
 R_4=[.27,.33]+i[-.057,-.02].
 \tag{2}
\]
It is an independent-reference theorem, so an actual open pair in
these rectangles is eligible without periodic identification. The
[open-window inheritance theorem](research_mixed_open_word_window_inheritance.md)
does not, however, place the second type-four vertex in \(R_4\).
Its general actual bound is the reduced disk and ordinary rectangle
\[
 r_2,s_2^*\in
 \{|z-(.30-.052i)|\le.060\}
       \cap\bigl((.24,.36)+i(-.102,-.001)\bigr).
 \tag{3}
\]
The attached reference \(r_1\) also has its wider endpoint
rectangle. For \(\alpha=1\), the coupled endpoint theorem
improves its height to \((-.078,-.020)\), but not to the
height interval in (2). For \(\beta=0\) and \(m\ge5\),
the type-three window does place \(r_3\) in \(R_3\);
this supplies only one of the two references of factor 3.
These are failures of an available implication between proved
domains, not counterexamples at actual words.

There is a useful precise restricted consequence: if an actual
reference happens to satisfy \(r_j\in R_{3+\epsilon_j}\)
for \(j=1,2,3\), and position 1 is unselected, the existing
selected theorem at \(H_2=7/500\) already bounds each of
factors 2 and 3 with loss \(1/200\). Their product therefore
has loss \(1/100\) against its two boundary tangents. The
unselected cap and suffix then join by their completed bounds.
No new certificate is required for that stated reference subclass.
The current universal open-reference ranges do not prove membership
in this subclass for any unrestricted first-type pattern in (1).

## 2. The smallest affected ordinary product when position 1 is unselected

Use the literal kernels and Fourier polynomial of the
[exact torus composition](research_mixed_conditional_torus_composition.md),
and write \(X_j=e^{-2\pi iz_j}\). The allocated modulus is
\[
 \mathcal B_{23,N}=
 |C_{1,N}(X_1,X_2)C_{\beta,N}(X_2,X_3)d_N(X_2)X_2^{-N}|
 |d_N(X_1)|^{\alpha/2}|d_N(X_3)|^{\beta/2}.
 \tag{4}
\]
The two halfweights at coordinate 2 have become its one full
selected weight. The remaining halves at coordinates 1 and 3
belong to the cap and the following factor, respectively. All
halfweights here are nonnegative roots of moduli.

For \(\epsilon\in\{0,1\}\), define the bare ordinary phase
\[
 Q_\epsilon(s;a,b)=g(s+a)+g(s+b)-(2+\epsilon)g(s)
                          -g(a)-g(b)+2\pi ias.
 \tag{5}
\]
Thus the notation \(Q_1\) is the earlier bare \(Q_4\).
Before eliminating the two ordinary indices, the allocated phase is
\[
 F_{23}=Q_1(s_2;z_1,z_2)+Q_\beta(s_3;z_2,z_3)
       -\frac\alpha2g(z_1)-g(z_2)-\frac\beta2g(z_3).
 \tag{6}
\]
At the actual reference this equals \(\phi_2+\phi_3\),
with exactly the original constants. The two index derivatives
and the internal derivative in \(z_2\) vanish. Put
\[
 M_{23}=\Re F_{23,*},\qquad
 p_L=\partial_{z_1}F_{23,*},\qquad
 p_R=\partial_{z_3}F_{23,*},\qquad
 \Lambda_{23}=M_{23}+\Re\{p_L(z_1-r_1)+p_R(z_3-r_3)\}.
 \tag{7}
\]
These are fixed original complex tangents. In the present targets
both boundary heights are unchanged, so only their real displacement
terms survive. The two complete Fourier alternatives are
\[
 \Re F_{23}-2\pi H_2,
       \qquad \Re F_{23}+\Re g(z_2).
 \tag{8}
\]
Their maximum retains the full polynomial in (4).

Here is an explicit all-current sufficient comparison. For an
ordinary factor of own flag \(\epsilon\), with actual index
height \(h_s\), let \(\ell_0=3/20\),
\(\ell_1=1/8\), and set
\[
 \begin{split}
 R_0(a,b)&=\max_{\ell_\epsilon\le v\le1/2}
                          \Re Q_\epsilon(v+ih_s;a,b),\\
 R_L(a,b)&=\Re Q_\epsilon(\ell_\epsilon;a,b),\qquad
 R_R(a,b)=\Re Q_\epsilon(1/2;a,b),\\
 R_1(a,b)&=2\pi(-\Im a)_++2\pi(\Im b)_+.
 \end{split}
 \tag{9}
\]
The last line is the full periodic last-row rate, not the evaluation
of the central logarithmic branch at index one. Use superscripts
\(2,3\) to distinguish the actual indices and types in (9).
Put
\[
 W_2^{\rm fac}=-\Re g(z_2)-2\pi H_2,
 \qquad W_2^{\rm force}=0,
 \tag{10}
\]
and define the explicit defect
\[
 \mathfrak D_{23}=
 \max_{i,j\in\{0,L,R,1\}}\ \max_{\nu\in\{\rm fac,\rm force\}}
 \left\{R_i^2(z_1,z_2)+R_j^3(z_2,z_3)
 -\frac\alpha2\Re g(z_1)-\frac\beta2\Re g(z_3)
 +W_2^\nu-\Lambda_{23}\right\}.
 \tag{11}
\]

**Proposition 1.** On the actual families (1) and the indicated
targets, for every \(\tau>0\),
\[
 \mathcal B_{23,N}\le C_\tau N^{A_\tau}
          \exp N\{\Lambda_{23}+\mathfrak D_{23}+\tau\}.
 \tag{12}
\]
Both parities and the full two finite sums are retained.

*Proof.* The pointwise fixed-contour inequalities in the
[asymmetric contour proof](research_mixed_horizontal_asymmetric_contour.md),
the [half-index extension](research_mixed_half_index_contour.md),
and the [own-four smaller-cut proof](research_mixed_four_left_cut_extension.md)
are valid on the outer height box \([-.12,.12]^2\).
Cancel their index-independent allocations on both sides. Their
horizontal aliases lie below the same-real-coordinate original
index line; their vertical aliases lie below the real-cut values;
vertical convexity bounds the zero-mode joins by those cuts and
the original line. These pointwise assertions do not require a
new supporting-plane inequality at the changed target heights.

Every present actual index height belongs to
\([-.108,.068]\). The outer target heights have absolute value
at most \(.108\), including both signs for an unselected
type-three argument. The left real tails increase to their cuts.
The [right-tail endpoint theorem](research_mixed_right_tail_endpoint_bound.md)
reduces each remaining real tail to its half row and its full last
row, yielding precisely (9). The regular strips, original
factorial interpolation, coefficient \(+N\), and both parities
are unchanged. Thus the entire bare kernel is bounded by the
maximum of its four profiles with any prescribed rate tolerance.

An unselected type-four boundary argument has negative height,
so its halfweight has rate \(-\Re g/2\). At the selected
coordinate the full weight has the two rates (10). Multiply the
two bare kernel bounds and those Fourier bounds, spending a single
total tolerance. This gives (12). No moving conditional saddle
or selected-height full packet is presumed. \(\square\)

For example, the two last-row entries here are
\(R_1^2=2\pi(-c_1)_++2\pi H_2\) and
\(R_1^3=2\pi(c_3)_+\). The positive \(2\pi H_2\)
cannot be removed by reusing the earlier first-selected last-row
theorem, whose outgoing second coordinate remained negative.

A uniform strict negative bound for (11) would settle this
position-2 selection with position 1 unselected. The cap tangent
is \(-p_L\); the next suffix tangent is \(-p_R\), or at
\(m=4\) the terminal tangent is \(-p_R\). These exact
stationary identities close (12) without a constant boundary fee.
Interior selections meet only factors of index at least six, so
their already proved losses and complex tangent cancellation remain
disjoint from this local product.

## 3. Both first coordinates selected

Now \(\alpha=1\). The smallest initial product that closes
both selected incidences on its left is
\[
 \mathcal B_{123,N}=
 |U_{1,N}(w,X_1)C_{1,N}(X_1,X_2)C_{\beta,N}(X_2,X_3)
      d_N(X_1)X_1^{-N}d_N(X_2)X_2^{-N}|
 |d_N(X_3)|^{\beta/2}.
 \tag{13}
\]
With the original cap phase \(\Psi(e,z_1)\), its unoptimized
allocated phase is
\[
 F_{123}=\Psi(e,z_1)+Q_1(s_2;z_1,z_2)
       +Q_\beta(s_3;z_2,z_3)
                -g(z_1)-g(z_2)-\frac\beta2g(z_3).
 \tag{14}
\]
At the actual reference its value is \(L+\phi_2+\phi_3\).
All private-index derivatives and both \(z_1,z_2\) derivatives
vanish. Its sole boundary marginal is
\(p_R=\partial_{z_3}F_{123,*}\). Hence put
\[
 \Lambda_{123}=\Re F_{123,*}+\Re\{p_R(z_3-r_3)\}.
 \tag{15}
\]

Let \(A_0,A_L\) be the cap main-line and real left-cut profiles
at \(z_1=x_1+iH_1\), with unchanged actual private height,
as in the
[next-four finite reduction](research_mixed_selected_four_four_finite_reduction.md),
equation (6). Its cap-only full five-profile estimate holds at
this unchanged \(H_1=1/100\). The pointwise cap-alias and right-cut
comparisons remove \(A_-,A_+,A_R\) in favor of \(A_0\),
independently of the following targets. Both literal endpoint
ceilings are already paid by that same cap main profile.
Thus only \(A_0,A_L\) remain. Define \(W_1^\nu\) as in
(10), with coordinate and height 1. The exact sufficient defect is
\[
 \mathfrak D_{123}=
 \max_{a\in\{0,L\},\ i,j\in\{0,L,R,1\}}
 \ \max_{\nu_1,\nu_2\in\{\rm fac,\rm force\}}
 \left\{A_a+R_i^2+R_j^3-\frac\beta2\Re g(z_3)
          +W_1^{\nu_1}+W_2^{\nu_2}-\Lambda_{123}\right\}.
 \tag{16}
\]
All profiles in a term share the same three outer targets and the
same actual reference. Each index maximum remains independent only
because the literal finite kernels have independent sum indices.

**Proposition 2.** For every \(\tau>0\) and every fixed ordinary
color derivative order \(k\), the modulus in (13), with
\(\partial_w^k\) applied to its holomorphic integer-weighted
product, satisfies
\[
 \mathcal B_{123,N}^{(k)}\le C_{\tau,k}N^{A_{\tau,k}}
          \exp N\{\Lambda_{123}+\mathfrak D_{123}+\tau\}.
 \tag{17}
\]
This holds on a small fixed ordinary-color disk at both parities.

Indeed multiply the cap bound just stated by the two four-profile
ordinary bounds from Proposition 1 and the two independent complete
selected Fourier bounds. The outgoing halfweight is added once.
Only the cap depends on the ordinary color, so its original disk
and Cauchy bounds give the derivative statement after allocating
the one total tolerance. This proves (17).

A uniform negative sign for (16) is the precise missing comparison.
The completed first-selected two-factor theorem is not this
assertion: it requires the second target height to remain \(c_2\).
Here changing it to \(H_2\) changes that theorem's outgoing
halfweight, original imaginary tangent contribution, and all its
ordinary profiles. In (14)--(17) these changes stay inside the
three-factor joint problem. At \(m=4\), its outgoing halfweight
and tangent meet the contracted terminal factor directly; no fourth
ordinary vertex is required.

## 4. Two already available analytic simplifications

First, the cotangent comparison in the
[four-corner lemma](research_mixed_selected_four_left_row_corners.md)
also applies to the own-four index of factor 2 in the present
orientation. Its hypotheses use only
\(\Re s_2^*\in[.24,.36]\),
\(|\Im s_2^*|,|\Im z_j|\le.102\), and the plateau real
interval. These hold here: the attached first-three height has
absolute value at most \(.072\), the attached first-four height
at most \(.078\), and either selected height is at most \(.014\).
Consequently
\[
 \Delta(x_1,x_2)=\Re\{Q_1(s_2^*;z_1,z_2)
                              -Q_1(1/8;z_1,z_2)\}
 \tag{18}
\]
is separately concave, even when the selected argument is the
outgoing one. Its minimum is attained among the four corners of
\(P^2\). Writing \(s_2^*=u+iv\),
\(k_1=\Im z_1\), \(k_2=H_2\), and \(a_0=1/8\),
those exact corner values are
\[
 \begin{split}
 K&=-3\Re g(s_2^*)+3\Re g(a_0)-2\pi k_1(u-a_0),\\
 I_\xi&=\Re\{g(s_2^*+\xi+ik_1)-g(a_0+\xi+ik_1)\}
                                      -2\pi\xi v,\\
 O_\eta&=\Re\{g(s_2^*+\eta+ik_2)-g(a_0+\eta+ik_2)\},\\
 D_{\xi\eta}&=K+I_\xi+O_\eta,
       \qquad \xi,\eta\in\{.22,.45\}.
 \end{split}
 \tag{19}
\]
Thus four reference-only signs would remove \(R_L^2\) from
(11) or (16). This is a proved reduction, not a sign claim.
The earlier corner record used \(k_1=.01,k_2=c_2\);
it does not certify the changed heights in (19).

Second, there is an existing complete estimate for a different
part of the exact boundary sector. The
[three-row source assembly](research_mixed_three_row_source_assembly.md),
Section 3, joins the calibrated second-four collar theorem to the
enlarged-contour height transport. It permits either first selection
and the physical second selected path, and gives a prefix loss
\(4/125\), with one total source tolerance, when the first
real coordinate lies in its fixed collar and
\(x_2\in[.24,.363]\). Its ordinary row excesses have been
discharged. The subsequent complete unselected terminal bound can
be attached at an unchanged final height with the exact halfweight
and tangent allocation. Safe interior selections may likewise be
inserted only on disjoint eligible factors. This uses the existing
collar hypotheses; it does not turn that first real collar into
the plateau \(x_1\in P\) or enlarge the second real interval.

These reductions preserve arbitrary word length and the original
source, but prove neither uniform sign (11)/(16) nor a global
open-chain asymptotic. Regions outside the stated contours, the
other boundary selections, ordinary-color strips, and stability
under arbitrary short partial fillings remain separate from the
cofinite filling-volume objective.
