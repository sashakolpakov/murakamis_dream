# A certified right-half core support comparison

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This note compares the original low-row source envelope, and its exact
row-one endpoint profile, with the geometric supporting plane. Both
expressions in the actual Fourier-weight bound are retained. High rows
paired with an angle below \(13/100\), and the full exterior estimate,
remain separate.

## 1. Original source and reference

Use the original \(C_{\epsilon,N}\), \(d_N\), and half-weight allocation of
[the two-right theorem](research_mixed_two_right_source_bound.md). Put
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \quad J(u)=\Re g(u),\quad
 I_h(u,y)=\int_0^u\log|1-e^{2\pi h-2\pi i(y+t)}|\,dt .
 \tag{1}
\]
One target angle equals \(1/2\), at height zero. The other is \(y+ih\).
Let \(\beta\) be its type-four indicator, and \(c=1\) when it is the
first argument of \(C_\epsilon\), otherwise \(c=0\). Its selected-wrap
indicator is \(\sigma\). The complete row envelope is
\[
 E(u,y;h)=I_0(u,1/2)+I_h(u,y)-(2+\epsilon)J(u)-2\pi chu
 +\frac\beta2\{\max(\nu_h(y),2\pi h_+)-2\pi\sigma h\},
 \qquad \nu_h(y)=-\Re g(y+ih).
 \tag{2}
\]
The six distinct source profiles are
\[
 (\epsilon,\beta,c)\in
 \{(0,0,0),(1,1,0),(0,0,1),(0,1,1),(1,0,1),(1,1,1)\}.
 \tag{3}
\]
The first two have their first target angle fixed at \(1/2\); the last
four have their second target angle fixed there. The other right-half
Fourier weight has zero exponential rate; its selected wrap has modulus
one. These are actual moduli, with no holomorphic half-weight chosen.

For the reference take every three-vertex word and both external types
in the rectangles
\[
 R_3=[.30,.39]+i[-.03,.02],\qquad
 R_4=[.27,.33]+i[-.057,-.02].
 \tag{4}
\]
The global holomorphic window branch is established in
[the critical-height theorem, Section 2, Lemma 2](research_mixed_cyclic_critical_height_bounds.md).
Set \(a=t_0,s=s_1,b=t_1\), \(\eta=\epsilon_0,\epsilon=\epsilon_1\),
retaining the original logarithmic lifts. The critical action and its
supporting plane are
\[
 \begin{split}
 \Phi(a,b)&=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias
             -(1+\eta/2)g(a)-(1+\epsilon/2)g(b),\\
 \Gamma_{x,y}(a,b)&=\Phi+\Phi_a(x-a)+\Phi_b(y-b).
 \end{split}
 \tag{5}
\]
Here \(s\) is eliminated by the actual zero-lift stationary equation.
The [slope theorem](research_mixed_geometric_support_slopes.md) gives
\(-1/5<\Re\Phi_a,\Re\Phi_b<1/4\) on every reference product.

## 2. Height profiles cover either proposed taper

Let \(\chi_0\) be quadratic from zero to one on \([0,.25]\), equal one
on \([.25,.4]\), and quadratic from one to zero on \([.4,.5]\).
Let \(\chi_1\) use \([0,.22],[.22,.45],[.45,.5]\) instead.
Both vanish on \([.5,1]\), and \(\chi_0\le\chi_1\).

For type three allow the larger independent height interval \([-.03,.02]\).
For type four allow
\[
 \begin{cases}
 -.057\chi_1(y)\le h\le-.02\chi_0(y),&\sigma=0,\\
 .014\chi_0(y)\le h\le .014\chi_1(y),&\sigma=1.
 \end{cases}
 \tag{6}
\]
Partition the other-angle core into
\[
 [.13,.20],\quad [.20,.22],\quad [.22,.25],\quad
 [.25,.40],\quad [.40,.50].
 \tag{7}
\]
On each interval \(Y\), enclose (6) by the exact minimum and maximum
over \(Y\), and use both resulting height endpoints. These rational
rectangles contain both taper graphs; no height endpoint is omitted.
For the small-angle reduction also use the degenerate interval
\(Y=\{.13\}\), with heights
\([-.057\chi_1(.13),0]\) or \([0,.014\chi_1(.13)]\), respectively.

There are 75 fixed-height profiles: six type-three profiles and 69
type-four profiles. Repeated endpoint heights within a nondegenerate
interval are removed.

## 3. Certified source supports

For each profile \(Y,h\), define the continuous convex function
\[
 S_h(\kappa)=\max\left\{
 \max_{\substack{u\in[1/5,1/2]\\y\in Y}}(E(u,y;h)-\kappa y),\
 \max_{y\in Y}(E(1,y;h)-\kappa y)\right\}.
 \tag{8}
\]
The second term is the literal periodic-entropy endpoint:
\[
 E(1,y;h)=2\pi(h_+-ch)
 +\frac\beta2\{\max(\nu_h(y),2\pi h_+)-2\pi\sigma h\}.
 \tag{9}
\]
Put \(H=|h|\), \(G_H(v)=\Re g(v-iH)\), \(q\in\{0,\beta\}\),
\(d_h=2\pi(h_+-ch)\),
\(b_h=\pi h_+(\beta-q/2)-\beta\pi\sigma h\), and
\(k_h=\kappa+q\pi h_+\). The two exact alternatives in the first
term of (8) are
\[
 F_q(u,y)=J(1/2+u)+G_H(u+y)-(1+q/2)G_H(y)
            -(2+\epsilon)J(u)+d_hu+b_h-k_hy.
 \tag{10}
\]
Their maximum is \(E-\kappa y\). The endpoint alternatives are
\(-qG_H(y)/2+d_h+b_h-k_hy\). Thus positive selected heights keep both
the wrap normalization and Fourier forcing.

The [right-core concavity theorem](research_mixed_right_half_concavity.md)
makes each \(F_q\) concave in \((u,y)\), and each endpoint alternative
concave in \(y\). At any rational trial point \(p\), the entire
rectangle \(D\) therefore satisfies
\[
 \sup_D F_q\le F_q(p)+
 \max_{v_u\in\partial D_u}F_{q,u}(p)(v_u-p_u)+
 \max_{v_y\in\partial D_y}F_{q,y}(p)(v_y-p_y).
 \tag{11}
\]
The one-dimensional analogue bounds the endpoint. Original dilogarithms
and logarithmic derivatives are evaluated outward. A floating optimizer
only proposes the rational trial point; neither convergence nor
stationarity is an acceptance premise. A degenerate angle interval
has zero angular remainder.

The source record supplies strict rational upper values for all 750
pairs of profiles and \(\kappa_j=-1/5+j/20\), \(j=0,\ldots,9\).
Each value bounds both Fourier alternatives and the raw endpoint.
Convex upper chords cover intervening slopes without extrapolation.

For fixed \(u,y\) in the core, (2) is convex in height by the same
concavity theorem, including the maximum with the Fourier forcing.
Equation (9) is also convex in height: \(-\Re g(y+ih)\) has positive
height curvature for \(0<y<1/2\), while the other nonlinear term is
\(h_+\). Hence the fixed-height comparisons cover the whole height
rectangles of Section 2.

## 4. Geometric comparison

**Theorem 1.** For every profile, reference product, and corresponding
orientation,
\[
 E(u,y;h)\le\Re\Gamma_{1/2,y+ih}-1/500
 \quad\hbox{or}\quad
 E(u,y;h)\le\Re\Gamma_{y+ih,1/2}-1/500,
 \qquad u\in[1/5,1/2]\cup\{1\}.
 \tag{12}
\]
The same bound holds throughout the permitted height interval.

On each reference boundary cell, enclose the relevant real slope
\(\kappa\), intersecting with the already proved \([-1/5,1/4]\) if
necessary. Take grid endpoints containing that whole range. If their
upper chord is \(A\kappa+B\), the comparison becomes exactly
\[
 B<\Re\Gamma_{1/2,-A+ih}-1/500
 \quad\hbox{or}\quad
 B<\Re\Gamma_{-A+ih,1/2}-1/500.
 \tag{13}
\]
The midpoint action is evaluated on a separately certified six-variable
Newton enclosure at the exact parameter midpoint, never solely on the
floating proposal. Its parameter derivative uses the full six-variable
affine response and conditional Schur formula of
[the two-right theorem, Section 3](research_mixed_two_right_source_bound.md).
The five-term Neumann expansion keeps its weighted remainder; the
two maximum norms maximize outward upper endpoints. The resulting
mean-value bound controls each whole rational parameter cell, including
all imaginary tangent terms in (5).

All eight words, four external type pairs, and sixteen edge products
are included: 512 reference boundary products. The author accepts
5,546 cells after 6,272 visits. Every acceptance has gap greater than
\(1/500\); exact prefix-free dyadic coverage is checked. The input
slope cells are re-evaluated rather than trusting cached summaries.

The actual optimized defect is separately subharmonic in the two
external complex reference variables: it is a supremum of real parts
of holomorphic supporting-plane differences plus fixed source costs,
over a compact source set. Joint continuity gives local boundedness.
Successive maximum principles extend the boundary comparison to the
whole products. They apply to the actual defect, not an extrapolated
chord or a slope-restricted subdomain. This proves (12).

## 5. Finite-source consequences and limits

The saved right-half reduction moves \(u<1/5\), \(y\ge.13\), to
\(u=1/5\) without increasing the source defect, also absorbing any
extra right-angle maximum. For \(y<.13\) and \(u\le1/2\), its
small-angle argument moves to \(y=.13\) at the original height.
This is why the degenerate profiles are retained.

Thus (12), the uniform original-product entropy estimate, and the
actual Fourier-weight bound give a \(1/1000\) exponential loss for
the full low-row part of the finite source at right angle \(1/2\),
relative to its original complex supporting plane. Both parities,
all rows in this stated low-row part, and both Fourier alternatives
are kept. Only the arbitrarily small Fourier tolerance and polynomial
prefactors consume the strict support margin.

The raw \(u=1\) comparison is available for a separate high-row
reduction on \(y\in[.13,.5]\). By itself it disposes of no high-row
interval. In particular high rows with \(y<.13\), right endpoint
\(1\) comparisons, and the other exterior regions remain separate.
This note gives no full mixed-word lower bound or new knot volume theorem.

## 6. Reproduction

    python3 experiments/certify_mixed_right_core_support_grid.py --precision 256
    python3 experiments/certify_mixed_right_core_support_reference.py --precision 256

The first record includes every rational trial point and strict source
upper value. The second includes every accepted reference address and
exact coverage check. Both bind the current proof, scripts, and
dependencies. Decimal summaries are informational only.
