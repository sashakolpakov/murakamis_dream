# The complete selected first-four/next-three finite product

Research theorem, 6 November 2026.

The selected product of the first type-four cap and its neighboring
type-three block now has a strict exponential gap on their whole
retained plateau. Both factors are complete finite kernels. The
original outgoing affine term, ordinary color, and complete selected
Fourier factor are retained. This is a two-factor source theorem;
it does not assert a bound for every sector of an open chain.

## 1. Literal source and theorem

Fix the original coupled critical reference of any mixed open word
of length \(m\ge3\) whose first two types are four and three.
All later types may be three or four. Use the original logarithmic
lifts and notation of
[the finite-source reduction](research_mixed_selected_four_three_finite_reduction.md):
\[
 \begin{gathered}
 H=7/625,\qquad z=y+iH,\qquad b=v+ih_b,\qquad
 y,v\in P=[11/50,9/20],\\
 M=\Re\{\Psi(e_*,z_*)+Q(s_*;z_*,b_*)-g(z_*)\},\\
 p=g'(s_*+b_*)-g'(b_*),\qquad
 \ell_b(v)=\Re p\,(v-\Re b_*).
 \end{gathered}
 \tag{1}
\]
All starred variables belong to the same actual reference.
In particular \(b\) is the outgoing own-three leg, not the next
external input to the ordinary block. At length three that next
external input may be attached; the necessary-reference covers
include it.

Put \(r=e^{-2\pi i/N}\), \(P_i=(r;r)_i\),
\(p_i(X)=(rX;r)_i\), \(X=e^{-2\pi iz}\), and
\(Y=e^{-2\pi ib}\). The exact source under consideration is
\[
 \begin{split}
 \mathcal K_N(w;X,Y)
   &=U_{1,N}(w,X)\,C_{0,N}(X,Y)\,d_N(X)X^{-N},\\
 U_{1,N}(w,X)
   &=\sum_{i=0}^{N-1}\frac{H_N(w,r^{-i})p_i(X)}{P_i^2},\\
 C_{0,N}(X,Y)
   &=\sum_{j=0}^{N-1}
          \frac{X^{-j}p_j(X)p_j(Y)}{P_j^2}.
 \end{split}
 \tag{2}
\]
Here \(H_N\) and \(d_N\) are the original endpoint and Fourier
objects. There is no extra outgoing halfweight at the type-three
coordinate. The two allocated halves at \(z\) have already been
recombined into the single complete factor in (2). The cap has one
ordinary color \(w\), whose complete value is \(-2\).

**Theorem 1.** For every \(\tau>0\) and every fixed nonnegative
ordinary-color derivative order \(k\), a sufficiently small fixed
color disk about \(-2\) and constants \(C_{\tau,k},D_{\tau,k},N_0\)
give, uniformly on \(P^2\), for every integer \(N\ge N_0\),
\[
 |\partial_w^k\mathcal K_N(w;X,Y)|
 \le C_{\tau,k}N^{D_{\tau,k}}
          \exp N\{M+\ell_b(v)-1/2000+\tau\}.
 \tag{3}
\]
Both level parities are included. In particular, choosing
\(\tau<1/4000\) gives the finite gap \(1/4000\) with a
polynomial prefactor. All indices in both sums (2), the cap's
complete inner endpoint coefficient, and the full selected
Fourier polynomial are present.

## 2. The last independent comparison is proved

For the profiles of the finite reduction, let
\[
 W_1(y)=-\Re g(y+iH)-2\pi H,\qquad W_0(y)=0.
 \tag{4}
\]
These are two upper-rate alternatives for the same complete
\(d_N(X)X^{-N}\), not an exact decomposition into different
finite sources.

The [left-cap/main-contour majorant](research_mixed_selected_cap_left_main_majorant.md)
bounds the profile \(A_L+B_0+W_\nu-M-\ell_b\), after maximizing
all three real targets, by an explicit scalar quantity
\(\mathcal J_\nu\) at the original reference. The outgoing trial
gradient vanishes only after retaining the original marginal in
(1). The private-action difference \(S(.27)-S(e_*)\), chirp,
negative index force, and both Fourier alternatives remain in
that quantity.

The [new certificate construction](research_mixed_selected_cap_left_main_scalar_certificate.md)
and its
[complete record](../repro/results/research-mixed-cap-left-main-budget-attempt01.json)
prove
\[
 \mathcal J_\nu<-1/2000,\qquad \nu=0,1.
 \tag{5}
\]
The cover uses the same rational endpoint parameter, original
necessary-reference filters, and centered original primitive as
the completed half-row comparison. Its initial auxiliary domain
is \([.217,.234]+i[.027,.045]\). Every actual reference in
(1) is contained in the retained necessary-reference set; there
is no assertion that every auxiliary point is realized by a word.

The single 160-bit attempt completed after 3,715 visits. Its
1,858 terminal leaves consist of 762 accepted and 1,096 necessarily
excluded leaves, with no unresolved cell and maximal depth 15.
Their binary addresses are prefix-free with exact dyadic mass one,
and \(3715=2\cdot1858-1\). The saved-data check
checked all 1,524 exact rational acceptance endpoints strictly
below \(-1/2000\), all 30 current input bindings, and the
complete partition. The largest upper endpoints are approximately
\[
 \begin{array}{c|r}
 \text{factorial}&-0.004265822359713091\\
 \text{forced}&-0.0005065713373775167 .
 \end{array}
 \tag{6}
\]
Only the saved rational endpoints determine acceptance. The
record's SHA256 is
c1f8b432d812992f27a004601b37461df0cb3ec8969129b92032ee0a56aacf1b.
The check reevaluated no reference map, primitive, root, finite
quantum sum, or earlier cover.

Consequently, uniformly on \(P^2\),
\[
 A_L(y)+B_0(y,v)+W_\nu(y)
             <M+\ell_b(v)-1/2000,\qquad \nu=0,1.
 \tag{7}
\]
This is the independent comparison left open by the half-row
completion.

## 3. Assembly of all finite currents and rows

The [half-row completion](research_mixed_selected_four_three_half_row_completion.md),
equation (11), already bounds the entire literal product by
\[
 |\partial_w^k\mathcal K_N|
 \le C_{\tau,k}N^{D_{\tau,k}}
 \exp N\{M+\ell_b(v)+\max(-1/2000,D_L(y,v))+\tau\},
 \tag{8}
\]
where
\[
 D_L(y,v)=
 \max_{\nu=0,1}\{A_L(y)+B_0(y,v)+W_\nu(y)-M-\ell_b(v)\}.
 \tag{9}
\]
Equation (7) makes the maximum in (8) equal to \(-1/2000\).
This proves (3).

For clarity, the previous reductions cover the full finite source
in the following way.

| Ordinary profile | Completed joint control |
|---|---|
| Main \(B_0\) | The central theorem controls \(A_0\); (7) controls \(A_L\); the right cap cut and both cap aliases are pointwise below \(A_0\). |
| Left real row \(B_L\) | The pointwise bound \(B_L<B_0-1/125\) reduces every cap pair to the preceding row. |
| Half row \(B_R\) | The completed half-row theorem controls all five cap profiles with gap \(1/2000\). |
| Last row \(B_1\) | The last-row theorem controls all five cap profiles with the larger gap \(3/100\). |

The original contour reduction includes both zero-mode joins and
all alias pieces. Its real-row reductions include every physical
row, wrapped product, endpoint limit, and half-grid sliver.
The cap endpoint ceilings at the positive incoming height retain
the reflected factor \(e^{2\pi H i}\); they are already below
the cap main profile and are not discarded by a negative-height
argument. Thus the table leaves no unestimated profile in (2).

The finite interpolation, factorial bounds, contour prefactors,
color perturbation and half-grid shifts consume one arbitrarily
small total \(\tau\). The complete cap packet is uniform on a
fixed ordinary-color neighborhood, so Cauchy's formula gives the
fixed derivatives in (3). The parity conventions and exact finite
normalization are inherited unchanged from (2) and the finite
reduction.

The theorem concerns the first selected type-four coordinate with
its neighboring type-three block at the stated height and plateau
targets. It supplies a complete local factor estimate with its
outgoing affine term. It does not integrate or estimate an arbitrary
remaining suffix, settle every selected or nonplateau open-source
sector, include length two, or establish noncancellation of the
whole knot invariant. The five independent comparisons in the
next-type-four finite reduction also remain separate. No global
volume or finite-exception theorem is asserted.
