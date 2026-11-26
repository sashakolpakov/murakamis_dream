# Componentwise refinement of saved Neumann bounds

Research lemma, 6 November 2026. Saved interval matrices permit a
componentwise improvement of an existing derivative enclosure by exact
rational matrix arithmetic. A separate segment-containment test permits
the same argument for root localization. No provider is changed and no
reference, phase, parameter or interval calculation is performed here.

## 1. A finite positive-matrix bound

Let a complex vector \(x\) satisfy
\[
                 x=Ex-d,
 \qquad |E_{ij}|\le C_{ij},\quad |d_i|\le r_i,
 \qquad C_{ij},r_i\ge0.
 \tag{1}
\]
The absolute value of a vector is componentwise. Suppose
\(\eta=\max_i\sum_jC_{ij}<1\), and put
\(b=\|r\|_\infty/(1-\eta)\). The ordinary Neumann bound
gives \(|x|\le b\mathbf1\). For any fixed integer \(m\ge0\),
\[
 |x|\le v^{(m)}
 :=\sum_{k=0}^{m-1}C^kr+C^m\mathbf1\,b
 \le\sum_{k=0}^{m-1}C^kr+
       \frac{\eta^m\|r\|_\infty}{1-\eta}\mathbf1.
 \tag{2}
\]
Indeed (1) gives \(|x|\le r+C|x|\). Iterate this inequality
\(m\) times and insert the initial uniform bound in the remainder.
The first bound in (2) is computed by
\[
 v^{(0)}=b\mathbf1,
 \qquad v^{(m+1)}=r+Cv^{(m)}.
 \tag{3}
\]
Since \(r+Cb\mathbf1\le b\mathbf1\), this sequence decreases
componentwise. Thus predetermined orders four and eight cannot worsen
the bound; they require no convergence test or adaptive series search.

There is a useful variant when an independent valid bound
\(|x|\le w^{(0)}\) has already been certified. The finite iteration
\[
       w^{(m+1)}=\min\{w^{(m)},\ r+Cw^{(m)}\}
 \tag{4}
\]
is also valid and decreasing componentwise. Its proof uses only (1)
and induction, so it does not require a new \(\eta<1\) test.
Taking a componentwise minimum of independent valid upper bounds never
discards a possible solution.

All entries in (2)--(4) may be rational. A saved complex rectangle
\([l_x,h_x]+i[l_y,h_y]\) has squared-modulus upper bound
\(M=\max(l_x^2,h_x^2)+\max(l_y^2,h_y^2)\). A nonnegative
rational \(t\) with \(t^2\ge M\) certifies a modulus bound;
this square inequality is an exact witness. One must not replace it
with an inward rounded square root. These constructions require no
evaluation of the original analytic matrix entries.

## 2. Derivatives of the canonical prefix

Use the [original-reference provider](research_mixed_second_selected_external_reference_evaluation.md)
with its exact rational trial column \(T\), preconditioner \(P\),
and certified actual-root Jacobian enclosure \(H\). For each actual
parameter \(c\), set
\[
 x=q_*'(c)-T,\qquad E=I-PH(q_*;c),
 \qquad d=P\{H(q_*;c)T+f_c(q_*;c)\}.
 \tag{5}
\]
The original implicit equation \(Hq_*'+f_c=0\) implies (1)
exactly. Saved enclosures of `I_minus_PH` and
`preconditioned_response_residual` therefore supply \(C,r\).
The saved original uniform derivative-error bound supplies
\(w^{(0)}\) for (4), or may be minimized with (2).

The resulting derivative rectangle for coordinate \(j\) is centered
at the same exact \(T_j\), with both real and imaginary radii at
most \(w_j^{(m)}\). It is a rectangular enclosure of the certified
modulus error, not a new reference or an assertion of nonempty parameter
intersection. No derivative of an interval-clipping operation is taken.

For the [boundary response](research_mixed_second_selected_external_response.md),
the saved coefficients \(L_a,L_u,R_v,R_b\) still enclose
\[
 p_L'=L_a a'+L_u u',\qquad
 p_R'=R_v v'+R_b b'.
 \tag{6}
\]
They may be reused with the refined derivative rectangles to bound
\(|p_L'a'|+|p_R'b'|\). This requires only new interval arithmetic
on the saved coefficients; it needs no new cotangent, root, primitive
or reference evaluation. The new bound must be recorded separately
with its source associations and exact witnesses. No improvement in
an actual boundary cell is asserted by this lemma.

## 3. Root localization requires the connecting segment

Let \(q_{\rm aff}(c)=q_0+T(c-c_0)\) be the original affine
predictor, and let \(\mathcal A\) be the Cartesian product on
which a saved interval matrix \(\mathcal H\) encloses the
**whole analytic Jacobian**. Suppose, for every actual \(c\) in
the cell,
\[
 q_*(c)\in\mathcal A,
 \qquad q_{\rm aff}(c)\in\mathcal A,
 \qquad [q_{\rm aff}(c),q_*(c)]\subset\mathcal A,
 \tag{7}
\]
and the saved Jacobian enclosure also covers all these external
parameters. The segment inclusion follows from the first two inclusions
when \(\mathcal A\) is convex. A sufficient directly checkable
condition is containment of the **entire saved raw affine box** in
the saved actual-root box; regularity must hold throughout that box.
Containment of the root alone, or overlap of the two boxes, is insufficient.

Put \(y=q_*(c)-q_{\rm aff}(c)\). Integrating the original gradient
along the segment gives
\[
 \bar H y=-f(q_{\rm aff}(c);c),\qquad
 \bar H=\int_0^1 f_q(q_{\rm aff}+ty;c)\,dt\in\mathcal H.
 \tag{8}
\]
Since each complex rectangle of \(\mathcal H\) is convex, the
saved enclosure of \(I-P\mathcal H\) also contains
\(I-P\bar H\). The saved componentwise Taylor data give
\[
 |f_i(q_{\rm aff}(c);c)|\le R_i
 :=|r_{0,i}|_++|L_{0,i}|_+d+\tfrac12\rho_i d^2,
 \quad L_0=H_0T+f_{c,0},\quad d\ge|c-c_0|.
 \tag{9}
\]
Here \(|\cdot|_+\) denotes a certified modulus upper bound,
and \(\rho_i\) is the already saved whole-affine Taylor bound.
With rational \(P^+_{ij}\ge|P_{ij}|\), set \(r=P^+R\).
Then \(y=(I-P\bar H)y-Pf(q_{\rm aff};c)\) has exactly the
form (1). If (2) is used, take its componentwise minimum with the
original certified Euclidean localization radius \(\varepsilon\).
Alternatively initialize (4) with \(\varepsilon\mathbf1\).
Either construction gives valid component radii no larger than
\(\varepsilon\), which enlarge the same raw affine coordinates to
give a new root enclosure. Formula (2) alone need not improve the
original localization radius.

If (7) is not established, the derivative refinement in Section 2
remains valid, but this localization refinement is unavailable from
that saved matrix. One must retain the original localization estimate
or separately enclose the Jacobian on the full connecting segments.
In particular, necessary pointwise root clipping cannot be silently
applied to an affine predictor that is not itself a root.
