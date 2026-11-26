# An exact clean-cut reduction to bounded physical boundary families

Private research deduction, 10 November 2026. A coarse bound for the
literal finite endpoint polynomials, followed by the original occupation
inequality, gives an exact finite-family alternative. Large occupation
is paid. Otherwise clean plateau triples occur within a bounded distance
of both physical ends. Retaining their exact closing losses removes
the intervening arbitrary alphabet without an approximation fee.

The remaining boundary signs are stated as sufficient propositions,
not proved here. This is not a new whole-word asymptotic, a completion
of the first-period contours, or a finite-exception theorem.

## 1. Keep either original source chart

Fix a positive word \(n_j=3+\epsilon_j\), \(1\le j\le m\), and its
actual complete-color critical reference. All original logarithmic
lifts, types, markings and source priorities are retained. Write
\[
 X_j=e^{-2\pi iz_j},\qquad
 D_j=d_N(X_j)^{\epsilon_j}X_j^{-N\sigma_j},\qquad
 \sigma_j\in\{0,\epsilon_j\},\qquad k_4=\sum_j\epsilon_j.
 \tag{1}
\]
The two exact charts are
\[
\begin{split}
 \mathscr J^u_{\sigma,N}
 &=\mathcal U_{\epsilon_1,N}(w_L,X_1)
     \prod_{j=2}^{m}C_{\epsilon_j,N}(X_{j-1},X_j)
     \mathcal H_N(w_R,X_m^{-1})\prod_{j=1}^{m}D_j,\\
 \mathscr J^c_{\sigma,N}
 &=\mathcal U_{\epsilon_1,N}(w_L,X_1)
     \prod_{j=2}^{m-1}C_{\epsilon_j,N}(X_{j-1},X_j)
     \mathcal V_{\epsilon_m,N}(w_R,X_{m-1})
                                  \prod_{j=1}^{m-1}D_j.
\end{split}
 \tag{2}
\]
Their retained lengths \(h\) and original scalars are
\[
\begin{array}{c|c|c}
 &h&\text{scalar}\\ \hline
 u&m&\kappa_N^{m+k_4}N^{m+k_4}\\
 c&m-1&\kappa_N^{m+k_4}N^{m+k_4-1}.
\end{array}
 \tag{3}
\]
The second chart requires \(m\ge2\); a one-letter word remains in
the first. These are Corollary 3 of
[torus composition](research_mixed_conditional_torus_composition.md)
and Proposition 1 of
[terminal contraction](research_mixed_reversed_cap_assembly.md).
In the second chart the entire last finite coordinate, its diagonal
weight and its Fourier alternatives are already inside \(\mathcal V\).
It has no additional selection \(\sigma_m\).

Choose one chart and its original periodic hybrid graph. Missing
neighbors have cutoff one. Fix the collar width before the level.
No new height reset is performed. The actual reference domains and
the original attenuated heights lie in a fixed bounded set; choose
\(H\ge1\) containing all those heights in absolute value. Fix
\(W\ge2\) and allow \(|w_L|,|w_R|\le W\).
The coarse bounds below hold on this entire ordinary-color disk.
Favorable calibrated signs have only their separately stated color scope.

## 2. A coarse constant from all finite coefficients

Put \(\zeta=e^{-2\pi i/N}\), and write
\[
 P_j=(\zeta;\zeta)_j,\quad S_j=|P_j|,\quad
 p_j(X)=(\zeta X;\zeta)_j,\quad
 J(t)=\int_0^t\log(2\sin\pi v)\,dv,\quad
 b=\max_{0\le t\le1}|J(t)|.
 \tag{4}
\]
The maximum is finite, including the integrable logarithmic ends.
The endpoint-uniform sine-factorial estimate in equation (8) of
[the all-real column theorem](research_mixed_symmetric_closing_all_real_column_bounds.md)
gives
\[
 S_j+S_j^{-1}\le C N^A e^{Nb},\qquad 0\le j<N.
 \tag{5}
\]
No value of \(b\) is evaluated or needed. Its literal Newton formula
\[
 e_j(w)=S_j^{-2}\prod_{\nu<j}(c_\nu-w),\qquad
 c_\nu=2\cos((2\nu+1)\pi/N)
\]
therefore gives, for every indicated ordinary color,
\[
 |e_j(w)|\le C N^A\exp N\{2b+\log(2+W)\}.
 \tag{6}
\]
All indices, including revived complete-color zero rows, remain.
Only the nonzero factorials \(P_j\), \(j<N\), occur as denominators.

The exact polynomials are
\[
\begin{split}
 \mathcal H_N(w,Y)
   &=\sum_{\ell<N}\frac{(-q)^{-\ell}e_\ell(w)}{P_\ell}
                                        (Y;\zeta)_\ell,\\
 \mathcal U_{\epsilon,N}(w,X)
   &=\sum_{i<N}\frac{\mathcal H_N(w,\zeta^{-i})p_i(X)}
                                        {P_i^{1+\epsilon}},\\
 C_{\epsilon,N}(X,Y)
   &=\sum_{j<N}\frac{X^{-j}p_j(X)p_j(Y)}{P_j^{2+\epsilon}},\\
 \mathcal V_{\epsilon,N}(w,X)
   &=\sum_{i<N}\frac{X^{-i}p_i(X)}{P_i^{1+\epsilon}}
                                  \mathcal U_{\epsilon,N}(w,\zeta^i),
 \qquad q=e^{\pi i/N},
\end{split}
 \tag{7}
\]
and
\[
 d_N(X)=\frac1N\sum_{a=0}^{N-1}\frac1{P_a}
                     \sum_{k=0}^{N-1}(X\zeta^{-a})^k.
 \tag{8}
\]
These are finite identities, not reciprocal-factorial approximations.
No peripheral multiplier is divided out at a zero.

Set \(R=e^{2\pi H}\), \(L=\log(1+R)\), \(T=\log R\),
and \(g=\log(2+W)\). On \(R^{-1}\le|X|,|Y|\le R\),
direct triangle bounds give polynomial prefactors and the rates
\[
\begin{array}{c|c}
\text{complete factor}&\text{upper rate}\\ \hline
 \mathcal H_N(w,Y)&B_H=3b+g+L\\
 \mathcal U_{\epsilon,N}(w,X)&B_U=5b+g+\log2+L\\
 C_{\epsilon,N}(X,Y)&B_C=3b+T+2L\\
 D_j&B_D=b+2T\\
 \mathcal V_{\epsilon,N}(w,X)&B_V=7b+g+2\log2+T+L .
\end{array}
 \tag{9}
\]
Indeed \(|p_j(X)|\le(1+R)^j\). At the physical argument
\(\zeta^{-i}\) in \(\mathcal U\), the product in \(\mathcal H\)
costs \(2^\ell\); at the physical argument in \(\mathcal V\),
the product in \(\mathcal U\) costs \(2^i\) as well.
Each inverse factorial costs at most \(b\). Formula (8) costs
\(b+T\), and the selected monomial costs at most another \(T\).
This proves all entries, uniformly for both type flags.

Thus (9) bounds the whole finite sources before any row or contour
decomposition. Both parities and the full Hermite data encoded in the
original matrices are retained. Fixed ordinary derivatives on smaller
color disks follow by Cauchy applied to (7), with the same rates.
No modulus halfweight is differentiated.

## 3. Initial safe cuts and a uniform calibrated coarse bound

For \(m\ge31\), take
\[
 p_0=16,\qquad q_0=m-15,\qquad
 I_0=[14,m-14],\qquad |I_0|=m-27.
 \tag{10}
\]
The interval with its eight-vertex halo is \([6,m-6]\), inside the
original safe range of
[open-window inheritance](research_mixed_open_word_window_inheritance.md).
These ordinary cuts work in either chart.
Retain the exact boundary allocation
\[
\begin{split}
 L_N(p)&=|\mathcal U_{\epsilon_1,N}|
       \prod_{j=2}^{p-1}|C_{\epsilon_j,N}|
       \prod_{j=1}^{p-2}|D_j|\,|D_{p-1}|^{1/2},\\
 R_N^u(q)&=|\mathcal H_N(w_R,X_m^{-1})|
       \prod_{j=q+1}^{m}|C_{\epsilon_j,N}|
       |D_q|^{1/2}\prod_{j=q+1}^{m}|D_j|,\\
 R_N^c(q)&=|\mathcal V_{\epsilon_m,N}|
       \prod_{j=q+1}^{m-1}|C_{\epsilon_j,N}|
       |D_q|^{1/2}\prod_{j=q+1}^{m-1}|D_j|.
\end{split}
 \tag{11}
\]
Each middle factor receives its complementary two halfweights.
These are nonnegative modulus identities, including at zeros.

Let \(M_L(p),M_R(q)\) be the original allocated baseline actions
and \(P_{p,a},P_{q,b}\) the surviving original complex marginals. Set
\[
\begin{split}
 G_{L,N}(p)&=N^{-1}\log L_N(p)-M_L(p)
                +\Re[P_{p,a}(z_{p-1}-r_{p-1})],\\
 G_{R,N}(q)&=N^{-1}\log R_N(q)-M_R(q)
                +\Re[P_{q,b}(z_q-r_q)],\qquad \log0=-\infty.
\end{split}
 \tag{12}
\]
For the synthetic baseline closure of \(I_0\), keep its exact
six-edge quantities \(A_{p_0},E_{q_0},D_{I_0}\).
The [uncontracted reduction](research_mixed_open_boundary_comparison_reduction.md)
and Section 3 of
[contracted collars](research_mixed_contracted_boundary_collar_completion.md)
give
\[
 N^{-1}\log|\mathscr J_{\sigma,N}|-M_{\rm open}
 \le G_{L,N}(p_0)+G_{R,N}(q_0)-A_{p_0}-E_{q_0}
                    -D_{I_0}+\eta+O_{m,\eta}(\log N/N).
 \tag{13}
\]
Here \(\eta>0\) is one total finite-source tolerance.
The middle rates retain their original seam priority and all selections.

Take the uniform local bound \(K_\rho\) for \(|w_j|\) from
Section 1 of
[full-alphabet completion](research_mixed_actual_open_full_alphabet_completion.md).
Also choose a uniform bound \(B_{\rm ref}\) for
\[
 |M_L(p_0)|+|M_R(q_0)|
 +(1+2H)(|P_{p_0,a}|+|P_{q_0,b}|).
 \tag{14}
\]
This bound is finite: the initial prefixes and suffixes have fixed
length. Section 2 of the boundary reduction identifies their reference
families with the original one-ended solutions and one external typed
leg. The original compact regular charts bound their finitely many
phase values and marginals. Take the larger bound for the two distinct
terminal charts. This does not bound a growing whole-word action by
a constant, or replace the actual reference by a periodic one.

At (10), the two products (11) have at most thirty conditional
factors and thirty full diagonal weights, counting their halfweights.
Consequently
\[
 \boxed{\quad
 C=B_U+\max(B_H,B_V)+30(B_C+B_D)+B_{\rm ref}+6K_\rho+1
 \quad}
 \tag{15}
\]
is a uniform eventual upper bound for
\(G_{L,N}(p_0)+G_{R,N}(q_0)-A_{p_0}-E_{q_0}\).
The unit absorbs the fixed polynomial prefactors for sufficiently
large \(N\), uniformly in word length because these initial products
have bounded length. This proves existence of \(C\) from literal
finite coefficients. No favorable sign or small value is assumed.

## 4. Large occupation or two bounded clean cuts

For \(i\in I_0\), write
\[
 p_i=\min\{1,\sigma_i+
     400(\operatorname{clamp}_{[.22,.45]}x_i-a_i)^2\},
 \qquad \kappa=1/20000,\qquad S=\sum_{i\in I_0}p_i.
 \tag{16}
\]
Crucially these are only the safe interior indices \(I_0\).
Equations (3)--(4) of full-alphabet completion give their actual
reference range \(.27<a_i<.39\). Thus \(p_i<1\) forces an
unselected symbol with \(x_i\in P=[.22,.45]\): outside \(P\)
the distance of the clamped coordinate from \(a_i\) exceeds \(1/20\).
No such implication is asserted for a physical near-end reference.
The reference is kept fixed at complete colors, even when ordinary
colors vary in (2). Its occupation theorem gives \(D_{I_0}\ge\kappa S\).

Fix \(\delta>0\), set \(B\) as below, and choose an integer \(r>B\):
\[
 B=\frac{C+2\delta}{\kappa},\qquad r>B.
 \tag{17}
\]
These constants are fixed before the word length and the level.
For \(m\ge6r+27\), form the disjoint candidate triples
\[
\begin{split}
 T_L(j)&=\{14+3j,15+3j,16+3j\},\\
 T_R(k)&=\{m-16-3k,m-15-3k,m-14-3k\},
                  \qquad 0\le j,k<r.
\end{split}
 \tag{18}
\]
The left and right collections are disjoint and contained in \(I_0\).

**Theorem 1 (exact alternative).** If \(m\ge6r+27\), every original
configuration has one of the following descriptions.

* If \(S>B\), its complete source has upper rate at most
  \(M_{\rm open}-2\delta+\eta+O_{m,\eta}(\log N/N)\).
* If \(S\le B\), there are \(j,k<r\) for which both triple sums
  in (18) are less than one. Put
  \[
   p=16+3j,\qquad q=m-15-3k,\qquad F=[p+1,q-2].
   \tag{19}
  \]
  All six protected symbols are unselected in \(P\), all free
  symbols in \(F\) remain arbitrary, and
  \[
  \boxed{\quad
  N^{-1}\log|\mathscr J_{\sigma,N}|-M_{\rm open}
     \le G_{L,N}(p)+G_{R,N}(q)-\kappa\sum_{i\in F}p_i
                         +\eta+O_{m,\eta}(\log N/N).
  \quad}
  \tag{20}
  \]
  There is no positive completion or pinning error.

*Proof.* The first assertion follows from (13), (15)--(17).
If every left triple sum were at least one, disjointness would give
\(S\ge r>B\). The same contradiction works on the right. Every
symbol in either chosen triple has occupation less than one.
The new interval \([p-2,q+1]\) is contained in \(I_0\), so its
original reference halo is safe. The length assumption gives
\(q\ge p+2\); its free interval may be empty.

Apply Lemma 1 of
[exact clean closing](research_mixed_clean_closing_edges_completion.md).
It retains the four clean losses on \(p-2,p-1,q+1,q+2\) and gives
\[
 D_{p,q}\ge-A_p-E_q+\kappa\sum_{i\in F}p_i.
 \tag{21}
\]
Insert this into the same exact six-edge source reduction at the
new cuts. This is equation (10) of
[completed-state propagation](research_mixed_completed_boundary_state_propagation.md),
and proves (20). All earlier physical departures remain inside the
longer literal boundary products (11). They are neither erased nor
reset. Their original neighboring height cutoffs are retained.
Membership of the protected triples in \(P\) is not a new packet
theorem for an arbitrary physical prefix. \(\square\)

For a disjoint integral partition, choose the first triple whose
sum is less than one in each listed order. First separate \(S>B\)
from \(S\le B\), then partition the latter by this pair of indices.
The rules depend only on real symbols and selections, not the colors
or \(N\). There are at most \(r^2\) low-occupation pieces in a fixed
chart. This partitions an already parametrized integral; it is not
another contour deformation and creates no new boundary current.

## 5. The finite family actually left

For (19), the left target window needed by (11)--(12), including
the neighboring height cutoff, is \([1,p]\). The right one is
\([q-1,h]\). Their sizes obey
\[
 p\le3r+13,\qquad h-q+2\le3r+14.
 \tag{22}
\]
Retaining the original eight-vertex reference halo gives prefixes
and suffixes of length at most \(3r+22\), each with its external
typed leg. One can equivalently index these families by the literal
indicated windows and their original one-ended equations.
There are finitely many bounded type strings, allowed selections
and cut-pair labels. Targets and external reference legs are still
continuous parameters.

Keep the actual pairs of reference data realized by the words.
Enlarging them to an independent product of external typed disks is
a stronger comparison and is allowed only if proved. The clean-cut
label describes the protected triples, not every preceding physical
symbol: all earlier selections, seams and raw right states remain.

The entire short-word family is
\[
                         1\le m\le6r+26.
 \tag{23}
\]
Keep each such whole original finite source and every type-compatible
selection. For \(m\ge2\) either complete chart may be chosen once;
for \(m=1\) use the uncontracted chart. Shared physical variables
are never replaced by independent boundary copies. This list contains
every word too short for the two searches or the original safety halo.

A precise sufficient remaining package is the following joint boundary
estimate, on each canonical long-word piece of Section 4:
\[
 G_{L,N}(p)+G_{R,N}(q)
       \le-\Delta_\partial(b_L,b_R)+\eta+O(\log N/N).
 \tag{24}
\]
This is a proposition to prove for the literal full product (11).
Its deficit is not supplied by the present reduction.
Separate nonpositivity of the two \(G\)'s is not required.
A convenient strong version has
\(\Delta_\partial\ge\delta_\partial>0\) whenever either physical
boundary window contains a selected or nonplateau symbol, and uses
the established unselected plateau planes otherwise. A weaker joint
bound is sufficient if it pays the desired region after the original
occupation in (20) is retained.

In the contracted chart, when every boundary-window symbol is
unselected in \(P\), equation (5) of
[the full plateau theorem](research_mixed_full_unselected_plateau.md)
already gives these neutral planes on its stated color neighborhoods.
Either a free symbol is selected or nonplateau, contributing occupation
one, or the whole retained configuration is the original unselected
plateau, which has its separate nonzero Gaussian theorem.
Thus (24) on the missing bounded boundary states would settle the
long-word complement in this chart. The uncontracted chart requires
its own terminal source propositions; a contracted terminal plane
cannot be inserted before the exact terminal sum.

Together with the whole short-word comparisons (23), this is an exact
sufficient finite-family reduction. Large occupation is paid by
Theorem 1. For a fixed word, choose the aggregate tolerance below the
available strict reserve and then take the level sufficiently large.
The scalar (3), finite
selection count and bounded graph Jacobian only change polynomial
factors. Every word and contour is fixed before \(N\to\infty\);
no uniform level threshold for unbounded word lengths is asserted.

## 6. Ordinary colors and the limits of the conclusion

The coarse constant and partition are uniform on the entire fixed color
disk. A favorable sign (24) is not created by that bound. A conclusion
near complete colors requires the favorable boundary package on its
own fixed ordinary neighborhoods. Whole real boundary decay for kernel
composition requires its positive angular losses on the full real color
square, or the corresponding strict gaps away from complete colors
together with the original local packet. Neither follows from \(C\).

Each restricted integral is still a polynomial of separate ordinary
degree at most \(N-1\): its graph and partition are color independent.
Bounds on complex neighborhoods give fixed jets on smaller ones by
Cauchy with the original normalization. No modulus halfweight is
differentiated. The two exact charts represent the same whole
polynomial, but their sector partitions must not be added as though
they were disjoint.

This reduction has no fixed approximation error and does not require
a word-uniform local packet radius. It proves no missing boundary sign
and chooses no new endpoint contour. Four first-pair estimates alone
do not cover all bounded physical strips in (22). Arbitrary short
signs or powers, branching selected components, original knot
identification and per-template finite exceptions remain outside.

## Frozen direct source bindings

| Source | SHA-256 |
|---|---|
| research_mixed_conditional_torus_composition.md | 8a25a25a95bf11767c4f305317a6fab9a9c17724ae0e24a36014b5fd8ec4f693 |
| research_mixed_reversed_cap_assembly.md | 79d44dfbcfe8c598783f27a49dea5bc716cc62e0a2c4762a238f3b2afffd244c |
| research_mixed_symmetric_closing_all_real_column_bounds.md | 02a134c219a5da365316de633e9edc407fbcc3de512d0474888bf8722b1f1059 |
| research_mixed_open_boundary_comparison_reduction.md | 5d3f875a6c1a7e0c2c9840c16674dc8ad5921bf0f2312202cb26f278c86c72ce |
| research_mixed_actual_open_full_alphabet_completion.md | d41f2c57b0ee397a24f299f5ffbfb132a1fb78ed1c47423543c56c975da0b782 |
| research_mixed_clean_closing_edges_completion.md | cc5b75d521fe648ab5aa0974e162de02b14fb814fc628635a1126349df5dfca9 |
| research_mixed_completed_boundary_state_propagation.md | cc7b2fc0db168d00e2b75b54ec3ff51496f178e819e4e5c8d5c6b53af563cb48 |
| research_mixed_contracted_boundary_collar_completion.md | c51b656e3f49e00d33e98df508941316a8db0df80a1a38ecd63312adde2786c6 |
| research_mixed_open_word_window_inheritance.md | b00b282d3258a42a4e5b6fe1af41b92d8a2c26cc31709b043a133dc27bbdf0ea |
| research_mixed_full_unselected_plateau.md | abd5dcddc9ed5057b6658bd8b7b60922540fd664c0c5c794135b19c1678c62a6 |

The complete proof and directly used source implications were read.
No mathematical numerical evaluation, saved-value arithmetic, test,
import, compilation, or edit to a frozen source or manuscript was used.

