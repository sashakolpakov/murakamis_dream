# A first boundary selection with an arbitrary unselected or interior-selected suffix

Research theorem, 6 November 2026.

The complete estimate for the first type-four cap followed by a
type-three block can now be joined to the rest of an open chain.
Its outgoing linear term cancels the incoming linear term of the
suffix. Consequently selecting the first retained Fourier coordinate
is exponentially suppressed on the entire plateau, even when the
chain is arbitrarily long. Additional selections sufficiently far
from the ends may be present.

This is a statement about specified integration regions of the exact
source. Contributions outside those regions and selections at the
other boundary positions remain untreated here.

## 1. Source, allowed selections, and contours

Fix a word \(n_j=3+\epsilon_j\), \(1\le j\le m\), with
\[
 m\ge3,\qquad \epsilon_1=1,\quad \epsilon_2=0,\qquad
 \epsilon_j\in\{0,1\}\quad(j\ge3).
 \tag{1}
\]
Put \(h=m-1\), \(k_4=\sum_j\epsilon_j\), and
\(P=[.22,.45]\). Let \(r_j=a_j+ic_j\), \(1\le j\le h\),
be the retained coordinates of the original open critical point.
The fixed reference action is denoted by \(\mathcal F_m(z_*)\);
write \(M_{\mathrm{open}}=\Re\mathcal F_m(z_*)\).

Use the literal terminal contraction and its finite kernels from
[the whole unselected plateau theorem](research_mixed_full_unselected_plateau.md).
For a set \(S\subseteq\{j\le h:\epsilon_j=1\}\), its exact
Fourier summand is
\[
 \begin{split}
 \mathscr J_{S,N}(\mathbf z;w_L,w_R)
 ={}&U_{1,N}(w_L,X_1)
       \prod_{j=2}^{h} C_{\epsilon_j,N}(X_{j-1},X_j)
       \mathcal V_{\epsilon_m,N}(w_R,X_h)\\
 &\qquad\cdot\prod_{j=1}^{h}
                d_N(X_j)^{\epsilon_j}X_j^{-N\mathbf 1_{j\in S}},
 \qquad X_j=e^{-2\pi iz_j}.
 \end{split}
 \tag{2}
\]
The terminal factor already contains its entire private sum and
its Fourier alternatives. No additional selection at position \(m\)
is made.

Let
\[
 I_m=\{j:6\le j\le m-5\},\qquad
 T\subseteq I_m\cap\{j:\epsilon_j=1\},\qquad S=\{1\}\cup T.
 \tag{3}
\]
When \(I_m\) is empty, \(T=\varnothing\).
The integration region for this summand is
\[
 \begin{split}
 z_1&=x_1+iH_1,\qquad H_1=7/625,\\
 z_j&=x_j+i\bigl((1-\mathbf 1_{j\in T})c_j
                        +\mathbf 1_{j\in T}H_{\mathrm{int}}\bigr),
                    \quad 2\le j\le h,\\
 H_{\mathrm{int}}&=7/500,\qquad \mathbf x\in P^h.
 \end{split}
 \tag{4}
\]
In particular \(z_2\) remains at its reference height: its type is
three, and it is not selected. All heights in (4) are constant,
so the plateau parametrization has Jacobian one.

For summands without the first selection, use the contours of
[the interior-selection theorem](research_mixed_interior_selected_plateau.md).
The positive height of the first selected coordinate in (4) is the
height proved by the new local estimate. No equality between
individual plateau integrals at different heights is assumed.
The exact Laurent-polynomial summands admit these contour choices
in the full torus formula; the unestimated complements are still
part of that formula.

## 2. Joining the two-factor estimate to the suffix

Let \(M_{12}\) and \(p\) be the original reference action and outgoing
marginal of
[the complete selected two-factor theorem](research_mixed_selected_four_three_full_product.md).
The first two factors of (2), together with the first diagonal and
selected weight, are exactly
\[
 \mathcal K_N
      =U_{1,N}(w_L,X_1)C_{0,N}(X_1,X_2)d_N(X_1)X_1^{-N}.
 \tag{5}
\]
For every prescribed positive tolerance \(\tau_{12}\), that theorem
gives
\[
 |\mathcal K_N|
 \le C N^A\exp N\left\{
      M_{12}+\Re p\,(x_2-a_2)-1/2000+\tau_{12}\right\}.
 \tag{6}
\]
It applies to every \(x_1,x_2\in P\). It includes the complete
first and second summation kernels and both Fourier upper-bound
alternatives.

The action of these first two factors, before eliminating their
private critical indices, is
\[
 \Psi(e,z_1)+Q_3(s;z_1,z_2)-g(z_1).
 \tag{7}
\]
Both indices are at their original critical values. The derivative
of the reduced action with respect to \(z_1\) vanishes, since all
factors incident to that coordinate are in (7). Its derivative in
\(z_2\) is \(p\). Thus the right side of (6) is its original
complex affine tangent, evaluated on (4), minus the stated gap.
There is no term for the imaginary displacement of \(z_1\).
The imaginary displacement of \(z_2\) is zero.

Use the ordinary allocated phases \(\phi_j\) and the terminal
allocated phase \(\Pi\) from the unselected plateau theorem.
The original action and stationary equations imply
\[
 \begin{split}
 \mathcal F_m(z_*)&=\mathcal F_{12,*}
               +\sum_{j=3}^{h}\phi_j(r_{j-1},r_j)+\Pi(r_h),\\
 p+\partial_1\phi_3(r_2,r_3)&=0\quad (h\ge3),\\
 p+\Pi'(r_2)&=0\quad(h=2).
 \end{split}
 \tag{8}
\]
Here \(\Re\mathcal F_{12,*}=M_{12}\); the first line includes
the same allocation and additive logarithmic constants as (7).
All other internal derivatives cancel in the usual adjacent pairs.
At \(h=2\), the ordinary suffix product is empty and the terminal
factor is directly adjacent to (5).

Because \(\epsilon_2=0\), no diagonal halfweight is left on the
boundary between (5) and the suffix. Every later diagonal weight
is allocated once between its two incidences, exactly as in the
unselected and interior-selected proofs.

If \(T=\varnothing\), all suffix factors have the complete horizontal
upper planes from those theorems. Their nonpositive quadratic
remainders may be discarded. If \(T\ne\varnothing\), put
\[
 E(T)=\{j\in\{3,\ldots,h\}:j-1\in T\ \text{or}\ j\in T\}.
 \tag{9}
\]
Every \(j\in E(T)\) is at least six. Therefore none of these
factors belongs to (5). The open-window inheritance theorem and
the selected ordinary-factor theorem used in the interior-selection
proof apply unchanged to them, with their full complex affine
tangents and a gap \(1/200\) per incident factor. All other suffix
factors have unselected arguments and use their horizontal planes.
The terminal argument is always unselected.

By (8) and the remaining stationary equations, the sum of these
affine tangents and the tangent in (6) has real part
\(M_{\mathrm{open}}\) at every point of (4).
This includes cancellation of the imaginary displacement terms at
the interior selected coordinates.

## 3. Exponential suppression and preservation of the leading term

**Theorem 1.** For every fixed word satisfying (1), every set (3),
and every \(\tau>0\), there are polynomial prefactors and sufficiently
small fixed ordinary-color disks such that, uniformly on (4),
\[
 |\mathscr J_{\{1\}\cup T,N}|
 \le C_{\tau,m}N^{A_{\tau,m}}
 \exp N\left\{
 M_{\mathrm{open}}-\frac1{2000}-\frac{|E(T)|}{200}+\tau
 \right\}.
 \tag{10}
\]
The assertion holds at all sufficiently large integer levels of
both parities. Fixed ordinary-color derivatives satisfy the same
exponential bound on smaller disks.

*Proof.* Multiply (6) by the complete suffix estimates just described.
Use (8) to add the reference values and cancel the affine terms.
The exact integer diagonal powers in (2) are recovered by multiplying
the allocated moduli; no derivative of a halfweight modulus is used.
For the fixed word choose all local rate tolerances to sum to at most
\(\tau\). Only the two endpoint factors depend on the ordinary colors;
their estimates hold on fixed neighborhoods with these tolerances.
Cauchy's formula on smaller color disks supplies the fixed derivatives.
Every factor theorem includes both parities. \(\square\)

In particular, taking \(\tau<1/4000\) gives a gap \(1/4000\)
even for \(T=\varnothing\). The number of admissible sets \(T\)
is finite for the fixed word. Multiplication by the exact original
scalar \(\kappa_N^{m+k_4}N^{m+k_4-1}\), of polynomial modulus,
and integration over \(P^h\) preserve this exponential gap.

Let \(\mathcal Z_N^{\mathrm{first+int}}\) be the sum of these
plateau contributions and the interior-selection contributions with
the first coordinate unselected. Then
\[
 \mathcal Z_N^{\mathrm{first+int}}(-2,-2)
 =\kappa_N^{m+k_4}N^{-3/2}A_m
        e^{N\mathcal F_m(z_*)}(1+O(N^{-1})),
                  \qquad A_m\ne0 .
 \tag{11}
\]
The action, coefficient, orientation and power of \(N\) are those
of the whole unselected plateau theorem. Equation (10) and the
interior-selection theorem make all additional terms exponentially
smaller, so they cannot cancel that coefficient.

This settles the first selected position for the prefixes in (1),
including simultaneous interior selections and arbitrarily long
suffixes of the two permitted types. It does not settle selections
at positions \(2,\ldots,5\) or at the last four retained positions,
prefixes whose second type is four, length two, or the regions outside
\(P^h\). In particular (11) is not yet an asymptotic for the entire
knot invariant or a stability theorem for arbitrary short fillings.
