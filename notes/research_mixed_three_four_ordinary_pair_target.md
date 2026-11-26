# The actual ordinary three/four pair after exact terminal contraction

Research scope and source deduction, 7 November 2026. No numerical
evaluation is used. Frozen source notes and manuscripts are unchanged.

The completed two-independent-Fourier-boundary theorem for the pair
\((2,2)\) is a new observation of an already controlled ordinary
component. The next positive mixed component considered here is instead
the original internal pair \((3,4)\). Its whole ordinary source reduces
exactly to one retained circle, with no retained Fourier alternative.
This note fixes that source and distinguishes its established plateau
estimate from the still missing whole-circle estimate.

## 1. Correct the covered case before choosing another component

Put \(A_n=JM^n\), with the original crossing matrix and scalar
\(\kappa_N\). The [internal two-crossing chain theorem](research_internal_two_crossing_chain.md),
Proposition 1 and Section 3, already proves
\[
 A_2^2=\kappa_N^3M^{-1}A_{-3}(M^{-1})^T,
 \qquad
 A_aA_2^2A_b=\kappa_N^3A_{a-1}A_{-3}A_{b-1}.
 \tag{1}
\]
These are full-algebra identities, including every repeated-root
normal. The same source proves the nonzero ordinary two-boundary
packet and whole-period strip for every fixed same-sign two-crossing
run. The [marked chain reduction](research_repeated_two_crossing_chain_reduction.md)
retains the boundary shifts, rotations and disk framings. Thus a fixed
\((2,2)\) component with sufficiently long remaining neighbors is
already covered by the [ordinary finite-kernel assembly](research_finite_two_boundary_kernel_closure.md).
The new local Fourier kernel is not needed to establish that family.

The [ordinary observation adapter](research_mixed_two_adjacent_ordinary_observation_adapter.md)
also records why the new Fourier center cannot simply be used as the
ordinary complete center. Exact conversion uses two complete periods
with the original Newton adapters; even the ordinary-complete integrand
is not stationary at \((x_0,x_0)\).

The pair \((3,4)\) is different. Its two-boundary collar matrix is
\[
 SA_4^{\rm top}SA_3^{\rm top}S
       =\begin{pmatrix}-3&1\\11&-4\end{pmatrix},
 \qquad
 A_n^{\rm top}=\begin{pmatrix}1&n\\0&1\end{pmatrix},
 \quad S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
 \tag{2}
\]
Its two diagonal entries are not both congruent to the same
\(\pm1\pmod {11}\). The necessary and sufficient
[one-vertex collar criterion](research_rational_corridor_compression.md),
Proposition 1, therefore excludes that particular compression while
both arbitrary attachments and their boundary frames are retained.
This does not classify special closures or every possible reduction.

Unlike the smaller internal signed pair \((2,-2)\), whose original
complete-boundary positive chart has a corner obstruction in
[the square-corner theorem](research_square_corner_flat_geometry.md),
the positive \((3,4)\) pair has an established actual geometric germ.
The [mixed geometric boundary theorem](research_mixed_geometric_boundary_germ.md)
identifies its source action, primitive periods and absolute volume
throughout a neighborhood of both complete ordinary boundary colors.

## 2. One exact circle, with all ordinary data retained

Write
\[
 D=N-1,\quad r=e^{-2\pi i/N},\quad q=e^{\pi i/N},
 \quad P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j.
\]
The original all-color polynomials are those of
[exact conditional torus composition](research_mixed_conditional_torus_composition.md),
Corollary 3:
\[
 \begin{split}
 H_N(w,Y)&=\sum_{\ell=0}^{D}
       \frac{(-q)^{-\ell}e_\ell(w)}{P_\ell}(Y;r)_\ell,\\
 U_{\alpha,N}(w,X)&=\sum_{i=0}^{D}
       \frac{H_N(w,r^{-i})p_i(X)}{P_i^{1+\alpha}}.
 \end{split}
 \tag{3}
\]
Define the coherently contracted terminal-four polynomial by
[reversed-cap assembly](research_mixed_reversed_cap_assembly.md),
equation (9):
\[
 V_{1,N}(w,X)=\sum_{i=0}^{D}
       \frac{X^{-i}p_i(X)}{P_i^2}U_{1,N}(w,r^i).
 \tag{4}
\]
Its band in \(X\) is contained in \([-D,0]\); the band of
\(U_{0,N}\) is contained in \([0,D]\). The exact terminal
contraction has already included every terminal row, the own-four
diagonal weight, and its Fourier alternative in (4).

**Proposition 1.** For every \(N\ge2\), all complex ordinary
colors, and every positive circle radius,
\[
 \boxed{\quad
 Z_{34,N}(w_L,w_R):=v(w_L)^TA_3A_4v(w_R)
 =\kappa_N^3N^2\oint
       U_{0,N}(w_L,X)V_{1,N}(w_R,X)\frac{dX}{2\pi iX}.
 \quad}
 \tag{5}
\]
Equivalently,
\[
 Z_{34,N}=\kappa_N^3N
       \sum_{j=0}^{N-1}U_{0,N}(w_L,r^j)V_{1,N}(w_R,r^j).
 \tag{6}
\]
Both identities hold after arbitrary fixed ordinary-color derivatives.

*Proof.* Specialize equation (13) of reversed-cap assembly to
\(m=2\), \(\epsilon_1=0\), \(\epsilon_2=1\). Its external
scalar is \(\kappa_N^{m+k_4}N^{m+k_4-1}=\kappa_N^3N^2\),
and its conditional product is empty. Its sole retained diagonal
exponent is zero. This gives (5) without an additional
\(d_N\) or \(1+X^{-N}\). The product in (5) has band
\([-D,D]\), whose only multiple of \(N\) is zero. Its root
average is therefore its constant coefficient, giving (6).
The factors are literal finite polynomials in each ordinary color;
all differentiations and contractions are exact. \(\square\)

In particular, this source has no retained selected sector to pay.
Aliases and physical tails inside either factor still belong to that
factor's full estimate. The constant term does not authorize taking
absolute values inside the coherent terminal sum (4).

## 3. The actual ordinary critical point and the proved part of its circle

At \(w_L=w_R=-2\), let
\(r_*=a_*+ic_*=t_1^*\) be the attached leg of the left type-three
endpoint in the actual length-two open reference. The
[open critical localization theorem](research_mixed_open_word_critical_localization.md),
Section 3, obtains this reference from the two endpoint maps using
one another's attached outputs. It is not the cyclic alternating
reference \(x_0\) used by the free Fourier kernel.
The [endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md)
give
\[
 .278<a_*<.391,\qquad -.072<c_*<.021.
 \tag{7}
\]
The private legs and endpoint auxiliary coordinates remain those of
the same coupled solution. In particular the terminal-four input is
this attached type-three leg, not an independent ordinary type-four
point or a periodic reference.

Use the original local factor actions
\[
 L(z)=\mathcal T_0(z,-2),\qquad
 \Pi(z)=\mathcal P_1(z),\qquad
 \Phi(z)=L(z)+\Pi(z),\qquad M=\Re\Phi(r_*).
 \tag{8}
\]
There is no Fourier halfweight subtraction in (8). The
[whole unselected plateau theorem](research_mixed_full_unselected_plateau.md),
Sections 2--5, proves the exact original action matching
\(\Phi'(r_*)=0\) and \(\Phi(r_*)=\mathcal F_2(z_*)\).
It also proves, for \(P=[.22,.45]\), \(d=x-a_*\),
and \(\kappa_*=1/2500000\), the complete-factor upper rates
\[
 \begin{split}
 N^{-1}\log|U_{0,N}(w_L,e^{-2\pi i(x+ic_*)})|
 &\le\Re L(r_*)+\Re L'(r_*)d-\kappa_*d^2+\tau
       +O(\log N/N),\\
 N^{-1}\log|V_{1,N}(w_R,e^{-2\pi i(x+ic_*)})|
 &\le\Re\Pi(r_*)+\Re\Pi'(r_*)d-\kappa_*d^2+\tau
       +O(\log N/N).
 \end{split}
 \tag{9}
\]
For every prescribed tolerance the bounds hold on sufficiently small
fixed ordinary-color neighborhoods, with fixed jets and both parities.
All terminal-four comparison conditions in the older conditional
completion note are discharged on this actual-reference family by
Section 1 of the whole plateau theorem.

The first line of (9) alone extends through \(x=.5\), by
[complete upper-target cap support](research_mixed_cap_upper_target_completion.md).
That extension does not enlarge the second line. In particular the
two whole-factor support theorems together currently give (9) on
\(P\), at the fixed actual height \(c_*\).

The local symbols are \(N^{-1}b_Ue^{NL}\) and
\(N^{-2}b_Ve^{N\Pi}\), both nonzero. Their one-dimensional
Gaussian, with \(H=-\Phi''(r_*)\) on the original accretive
branch, gives the already established plateau contribution
\[
 Z^P_{34,N}(-2,-2)
 =\kappa_N^3N^{-3/2}
      \frac{\sqrt{2\pi}\,b_U(r_*)b_V(r_*)}{\sqrt H}
       e^{N\Phi(r_*)}(1+O(N^{-1})).
 \tag{10}
\]
The scalar count is \(N^2N^{-1}N^{-2}N^{-1/2}=N^{-3/2}\).
The inherited orientation is increasing \(\Re z\); it follows by
reversing the clockwise parametrization \(X=e^{-2\pi iz}\) of
the positive circle. The boundary germ identifies the real action
in (10) with the original partial-filling volume divided by \(2\pi\)
and retains the original purely imaginary source constant.

## 4. A proved seam collar and the concrete remaining contraction

There is also a complete discarded collar for this exact length-two
source. The [two-vertex first-collar theorem](research_mixed_two_vertex_first_collar.md),
Theorem 2 with \((\alpha,\beta)=(0,1)\), gives a fixed
\(\rho>0\) such that
\[
 |U_{0,N}(w_L,e^{-2\pi ix})V_{1,N}(w_R,e^{-2\pi ix})|
 \le C N^A e^{N(M-1/20)},\qquad 0\le x\le\rho.
 \tag{11}
\]
Its reference is precisely the actual two-endpoint reference above.
The proof compares the zero-safe seam ceiling \(3211/1500\)
with \(M>9/4-147\pi/20000\), leaving more than \(7/100\)
before its fixed collar costs. Both ordinary-color neighborhoods,
all fixed jets, and both level parities are retained.

Equation (11) is on the real seam, not on the line of height
\(c_*\). It can be used together with (9) on the original
one-coordinate periodic hybrid graph, which has height zero on
the first collar and height \(c_*\) on \(P\). Alternatively,
any explicit connecting deformation must retain its other pieces.
The Laurent-polynomial identity (5) makes such complete graph
deformations legal; it does not bound their transition pieces.

The [complete terminal profile envelope](research_mixed_terminal_concave_profile_envelope.md)
supplies 25 regular profiles and two physical-complement profiles on
the larger height tube \([.22,.45]+i[-.12,.12]\). Its regular
profiles are jointly horizontally concave and vertically convex.
This proves a finite-source representation on that tube, but the
calibrated terminal plane (9) is proved only at the actual height.
In particular the envelope supplies neither a moving-height sign
outside \(P\) nor a whole-period phase for \(V_1\).

For (5), the unresolved retained region is the complement of
the paid plateau and seam collar on a complete one-variable contour,
with all transitions and connectors retained. There are
no ordinary middle factors, no retained Fourier selection, and no
length-dependent pinning fee in this particular problem. Nevertheless
neither separate plateau plane in (9) bounds that complement.
One must estimate the coupled product \(U_0V_1\), or a coherent
replacement of its complete complementary contour, at the original
action (8).

The existing [prepared-cap theorem](research_mixed_prepared_cap_coherent_contour_completion.md)
instead estimates \(v(w)^TA_3A_4h(y)\) near \((w,y)=(-2,x_0)\).
It is not (5), and its reference action cannot be substituted for
\(\Phi(r_*)\). Likewise the new free Fourier \((2,2)\) packet
does not alter this ordinary observation.

Completing this one-circle comparison would establish the whole
local ordinary packet. To insert it as a component in the original
long-filling theorem, the other analytic requirement remains the
strict calibrated decay over the whole real outside-color torus.
The [open-source stability reduction](research_mixed_open_source_stability_reduction.md)
then supplies its quadratic complex strip, while the geometric
premise is already discharged by the boundary-germ theorem cited
above. No whole-circle, outside-color, or new knot-family conclusion
is asserted in this note.
