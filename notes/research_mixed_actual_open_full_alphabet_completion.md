# Finite-depth completion for the full alphabet of an actual open word

Private research deduction, 10 November 2026. This extends the optimized
middle completion in the original open-boundary comparison from an
unselected plateau corridor to **every original target symbol**. The
reference is the actual open three/four word throughout. No periodic
completion, new critical point, flat height reset, or change of boundary
functional is made.

The conclusion is a rate comparison with a controllable one-sided error.
It does not prove the remaining endpoint-source inequality. In particular
it is not a new open-word asymptotic or a finite-exception theorem.
The ordinary free colors in this comparison remain \((-2,-2)\).
The full alphabet below consists of the original retained-leg coordinates
and selections, not newly freed ordinary boundary colors.

## 1. Exact source inputs and the safe interval

Fix the permitted collar width once. Use the complete allocated upper
rates and original complex tangents of
[the open-boundary reduction](research_mixed_open_boundary_comparison_reduction.md),
equations (1)--(10). Relabel its retained, safe symbol interval as
\(I=\{1,\ldots,n\}\). An ordinary middle with at least one edge has
\(n\ge4\). If no such safe middle is chosen, retain the whole original
bounded-length boundary problem instead. A symbol is
\[
 q_i=(x_i,\sigma_i),\qquad 0\le x_i\le1,\qquad
 \sigma_i\in\{0,\epsilon_i\},\qquad \epsilon_i\in\{0,1\}.
 \tag{1}
\]
The original reference is \(r_i=a_i+ic_i\), and the baseline symbol is
\(q_i^0=(a_i,0)\). Every symbol outside \(I\) is baseline. The safe
interval has the eight-vertex reference halo stipulated in the
open-boundary reduction. Every truncation of a perturbation inside \(I\)
therefore has the same eligibility. None reaches a private endpoint.

Write
\[
 w_j=w_j(q_{j-2},q_{j-1},q_j,q_{j+1}),\qquad
 D(q)=-\sum_j w_j(q).
 \tag{2}
\]
Only finitely many summands are nonzero. These are exactly the original
four-symbol rates, with the zero-seam priority, complete raw right rows,
true coherent Fourier alternatives, and tangent planes retained.
In the indexing of the open-boundary reduction, \(D\) is its
\(D_{p,q}\), including all six closing edges.

Let \(P=[.22,.45]\), let \(y_i\) be the clamp of \(x_i\) to \(P\), and
put
\[
 p_i=\min\{1,\sigma_i+400(y_i-a_i)^2\},\qquad
 \kappa=\frac1{20000}.
 \tag{3}
\]
Outside \(I\), set \(p_i=0\). The actual safe reference has
\(.27<a_i<.39\). In particular,
\[
 p_i<1\ \Longrightarrow\
 \sigma_i=0,\quad x_i\in P,\quad p_i=400(x_i-a_i)^2.
 \tag{4}
\]
The [full-period occupation theorem](research_mixed_full_period_occupation.md),
including its safe-open-reference statement, gives
\[
 D(q)\ge\kappa\sum_{i\in I}p_i(q)
 \tag{5}
\]
for every allowed configuration, not just a minimizer. It also gives
(5) for every synthetic sub-block obtained by replacing the remaining
symbols by baseline values.

There is a finite uniform local bound \(K_\rho\) for \(|w_j|\).
Here one may use exactly the definition and boundedness proof in
[the full-alphabet potential](research_mixed_full_alphabet_boundary_potential.md),
Section 1: take the supremum over the original compact typed reference
windows, allowed selections and real quadruples. The coherent pieces
are bounded on their regular compact domains, collar profiles are
bounded, and the complete raw rates are compact maxima of continuous
integrated logarithms. The tangents are bounded on their original
charts. The same local data are eligible at the actual open reference
by [window inheritance](research_mixed_open_word_window_inheritance.md).
No periodic-reference identity is used here. No value of \(K_\rho\)
is evaluated.

Global continuity of \(w_j\) across priority interfaces is unnecessary.
All infima below are genuine infima; no attained optimizer is assumed.

## 2. A cut in a small-occupation block

For an integer cut \(k\), let \(q^{\le k}\) retain \(q_i\) at \(i\le k\)
and set every other symbol to baseline. Define \(q^{>k}\) similarly.
The only stencils which cross this cut are those of
\[
                         j=k,\ k+1,\ k+2.
 \tag{6}
\]
Their union is the six-symbol block \(\{k-2,\ldots,k+3\}\).

Suppose every symbol in this block has \(p_i<1\). Then it is an
unselected plateau block by (4), including after either truncation.
All its relevant target heights are the original reference heights.
The clean coherent rate is the original phase, so on these stencils
\[
 -w_j=e_j(x_{j-1},x_j),\qquad
 e_j(s,t)=-\Re\{\phi_j(s+ic_{j-1},t+ic_j)
                         -\Gamma_j(s+ic_{j-1},t+ic_j)\}.
 \tag{7}
\]
The original pair function and its gradient vanish at its reference
pair. The uniform plateau Hessian bound used in
[plateau boundary forgetting](research_mixed_plateau_boundary_forgetting.md),
equation (3), implies
\[
                         |\partial_1\partial_2 e_j|\le20
 \tag{8}
\]
on the whole real segments involved. This use of the plateau source
is confined to the six symbols at the cut. Symbols elsewhere may be
selected, in a seam, or in the full right half.

All terms at \(j=k,k+2\) cancel in the cut difference, since their
actual phase pairs stay on one side. Consequently the exact identity is
\[
\begin{split}
 D(q)-D(q^{\le k})-D(q^{>k})
   ={}&e_{k+1}(x_k,x_{k+1})-e_{k+1}(x_k,a_{k+1})\\
     &-e_{k+1}(a_k,x_{k+1})=:\mathcal R_k(q).
\end{split}
 \tag{9}
\]
The missing baseline term is zero. Integrating the mixed derivative
over the real rectangle and using (3)--(4) gives
\[
 |\mathcal R_k(q)|
 \le20|x_k-a_k|\,|x_{k+1}-a_{k+1}|
 \le\frac{p_k+p_{k+1}}{40}.
 \tag{10}
\]
This is an identity and estimate for the original rates. It does not
split an exact finite polynomial into independently bounded factors.

It is useful to reserve some occupation loss. Fix \(0\le\theta<1\)
and define
\[
 D_\theta(q)=D(q)-\theta\kappa\sum_i p_i(q),\qquad
 \kappa_\theta=(1-\theta)\kappa>0.
 \tag{11}
\]
Then \(D_\theta\ge\kappa_\theta\sum p_i\). Since the occupation is
additive under the two truncations, (9)--(10) hold for \(D_\theta\)
with exactly the same remainder.

## 3. Uniform two-sided finite-depth approximation

Prescribe the first and last three physical symbols:
\[
 v_L=(q_1,q_2,q_3),\qquad
 v_R=(q_{n-2},q_{n-1},q_n).
 \tag{12}
\]
If these triples overlap, their common entries must agree; such short
intervals will be retained without truncation. All other symbols range
over the full alphabet (1). Put
\[
 V_\theta(v_L,v_R)=\inf D_\theta(q).
 \tag{13}
\]
Set
\[
 C_0=12K_\rho+1,\qquad B_\theta=\frac{C_0}{\kappa_\theta}.
 \tag{14}
\]
Indeed, the competitor which retains only the two prescribed triples
changes at most six edge stencils per triple. Its value of
\(D_\theta\) is at most \(12K_\rho<C_0\), because the subtracted
occupation is nonnegative. Thus
\[
                         0\le V_\theta<C_0.
 \tag{15}
\]

Choose an integer \(m>B_\theta\), and let
\[
                         d=3+6m.
 \tag{16}
\]
For \(n>2d+6\), define \(V_\theta^{[d]}\) by the same infimum as
(13), with all symbols \(d<i\le n-d\) pinned to their actual baseline.
For \(n\le2d+6\), define \(V_\theta^{[d]}=V_\theta\); this retains
the entire bounded-length problem and handles every small integer
length and overlapping boundary triple.

**Theorem 1.** Uniformly in the original word length, the prescribed
terminal triples, all selections and all real target symbols,
\[
 \boxed{\quad
 0\le V_\theta^{[d]}-V_\theta
       \le\varepsilon_{\theta,m}:=\frac{B_\theta}{20m}.
 \quad}
 \tag{17}
\]
The constants use the original local source bounds and actual-reference
occupation theorem only. In particular \(\varepsilon_{\theta,m}\to0\)
as \(m\to\infty\), with no reference-period extension.

*Proof.* Only the long case requires proof. Choose a configuration
whose value is within an arbitrarily small positive amount of (13).
By taking that amount small enough, its value is below \(C_0\).
Equation (11) gives
\[
                            \sum_i p_i<B_\theta.
 \tag{18}
\]
Divide \(\{4,\ldots,d\}\) into \(m\) consecutive disjoint blocks
of six symbols. One has total occupation at most \(B_\theta/m<1\).
Cut after its third symbol, at \(k_L\). Thus
\(6\le k_L\le d-3\), and its full six-symbol cut block obeys (4).
Do the same in \(\{n-d+1,\ldots,n-3\}\), obtaining a cut \(k_R\)
with \(n-d+3\le k_R\le n-6\). Both retained terminal triples are
outside the removed middle.

Let \(q^L,q^M,q^R\) retain respectively the symbols at
\(i\le k_L\), \(k_L<i\le k_R\), and \(i>k_R\), and be baseline
elsewhere. Both cuts are well separated since \(n>2d+6\). Applying
(9) at the two cuts gives
\[
 D_\theta(q)=D_\theta(q^L)+D_\theta(q^M)+D_\theta(q^R)
                      +\mathcal R_{k_L}+\mathcal R_{k_R}.
 \tag{19}
\]
Every synthetic support is inside the same safe interval. Hence
\(D_\theta(q^M)\ge0\) by the original occupation theorem. This
nonnegativity is the reason the middle may be removed; individual
edge defects are not assumed nonnegative.

Let \(\widehat q\) retain \(q^L,q^R\) and be baseline in between.
No four-symbol stencil meets both retained supports, so
\[
 D_\theta(\widehat q)=D_\theta(q^L)+D_\theta(q^R).
 \tag{20}
\]
This configuration is admissible for \(V_\theta^{[d]}\). The two
chosen blocks and (10) now imply
\[
 D_\theta(\widehat q)-D_\theta(q)
 \le|\mathcal R_{k_L}|+|\mathcal R_{k_R}|
 \le\frac{B_\theta}{20m}.
 \tag{21}
\]
Let the initial error in (13) decrease to zero. The reverse inequality
in (17) follows from restricting an infimum. No minimizer, interface
continuity, or numerical value of any infimum was used. \(\square\)

In the long case, the pinned middle separates the two remaining
finite problems exactly:
\[
 V_\theta^{[d]}(v_L,v_R)
           =L_{\theta,d}(v_L)+R_{\theta,n,d}(v_R).
 \tag{22}
\]
Each function is an infimum over a finite boundary buffer of depth
\(d\), with the original fixed reference and all allowed symbols.
The intervening baseline stencils contribute zero. No independence
of overlapping symbols is asserted in the short case.

## 4. Consequence for the literal open endpoint comparison

Retain precisely the boundary rates \(\mathcal B_L,\mathcal B_R\)
of equations (7)--(9) of the open-boundary reduction: the complete
ordinary endpoint polynomials, all reciprocal-factorial halves,
the two surviving complex tangents, and the original closing
constants remain in them. Its source inequality and (11), (17) give
\[
\boxed{\begin{split}
 \text{original upper rate}-M_{\rm open}
 \le{}&\mathcal B_L+\mathcal B_R
          -V_\theta^{[d]}(v_L,v_R)
          -\theta\kappa\sum_i p_i
          +\varepsilon_{\theta,m}.
\end{split}}
 \tag{23}
\]
This holds for the complete alphabet, including selected type-four
alternatives, seam symbols and raw right rows. Unlike a purely
optimized middle bound, it can retain a positive fraction of the
occupation loss at every original physical symbol.
As in its source reduction, this is the comparison at complete ordinary
colors. It does not enlarge the ordinary-color domains of the literal
endpoint estimates.

For each fixed target error, (16)--(17) fix the buffer depth before
the word length or the level enters. The endpoint source profiles
already use at most seventeen physical target symbols on each side.
Adding the two finite buffers and the unchanged finite reference halo
therefore leaves only finitely many fixed-length type families.
Their reference data are the actual endpoint-prefix or suffix
solutions with one typed external leg, as proved in the
open-boundary reduction. They are not arbitrary periodic substitutes.
Short words remain whole finite boundary families. Their continuous
typed parameters, complete endpoint rows and every allowed selection
still have to be controlled.

Thus the additional comparison to seek is the sign of the finite
boundary expression in (23), with the retained occupation term and
the explicit error. A strict remote margin larger than that error
passes to the original whole rate. For a fixed word its finite-source
tolerance is then chosen once below the remaining margin, with all
local tolerances summed before use. No positive fixed tolerance is
spent in a neighborhood of the zero-loss critical point; the original
local coherent source and Hessian analysis govern that neighborhood.

There is no proof here that the finite boundary expression has the
needed sign. In particular Theorem 1 is not a reason to impose
\(\mathcal B_L\le0\) or \(\mathcal B_R\le0\) separately: the actual
quadratic relaxation obstruction in Section 3 of the open-boundary
reduction persists. The two retained completion functions are the
coupled comparison which that simplification discards.

## 5. Scope for short partial fillings

The new implication is a full-alphabet, actual-open-reference
finite-depth reduction. The old exponential plateau theorem gives a
sharper error on its smaller alphabet; the periodic full-alphabet
potential has a different reference and boundary-transform scope.
Neither is replaced or silently imported here.

Return accretivity and regular wire ordering alone cannot establish
the sign left in (23). The
[bare power-three obstruction](research_bare_kernel_power_three_obstruction.md)
already exhibits actual finite positive-three paths on which the
full bare edge and its shortened counterpart exceed the proposed
geometric edge rate. The
[convex-height atlas](research_mixed_convex_height_contour_atlas.md),
Section 4, separately shows that resetting the actual type-four
critical heights to zero increases a full unselected source density.
These statements rule out two stronger shortcuts, not the desired
whole contracted open-source theorem.

The proved ordinary two-boundary
[343 kernel](research_mixed_symmetric_343_full_boundary_kernel.md)
pays its complete complement by original-source comparisons. It
does not identify the finitely many functions in (22)--(23) with that
single kernel, or prove their inequalities for all type families.
The finite-depth reduction does, however, remove an unbounded middle
length from the remaining source comparison without dropping any of
its symbols. All original coefficients, markings, half-turns and
parameter-assignment fibers stay unchanged. Branching selected
components, pendant ports at the opposite complete color, arbitrary
short signs or powers, and a knot-invariant identification require
their own original-source and topological statements.

## Source bindings

The complete direct proof inputs were read without evaluation:

| File | SHA-256 |
|---|---|
| research_mixed_open_boundary_comparison_reduction.md | 5d3f875a6c1a7e0c2c9840c16674dc8ad5921bf0f2312202cb26f278c86c72ce |
| research_mixed_full_period_occupation.md | 70cd6262e5737c70ed178cbf88ca69cb6f7d7eb659a493a21673bdd5b2830fec |
| research_mixed_plateau_boundary_forgetting.md | 6f3294e9beaaa20c1048dff534cca91d0036150ead2f6609df56a31a22f495c9 |
| research_mixed_full_alphabet_boundary_potential.md | 682912f50d54d63dc9a42a5759574f552a42c7c3efeab1dd62078a2135b19668 |
| research_mixed_open_word_window_inheritance.md | b00b282d3258a42a4e5b6fe1af41b92d8a2c26cc31709b043a133dc27bbdf0ea |

The final scope comparisons use the following frozen notes:

| File | SHA-256 |
|---|---|
| research_bare_kernel_power_three_obstruction.md | 9feabd083c6ec0d864680b3fd49203508e54517abec974472f3065a15110fbaa |
| research_mixed_convex_height_contour_atlas.md | ca3c6d88c2461ce05f8bb239e2740baab7f418260945af1ede6d7cad379f1972 |
| research_mixed_symmetric_343_full_boundary_kernel.md | cb4003e168dafc77a7f464eac05ba3a7ae805b63eee4d38f2b9c27904ebc9bf3 |

No new source cover, mathematical numerical evaluation, optimization
run, or alteration of a frozen manuscript is used.
