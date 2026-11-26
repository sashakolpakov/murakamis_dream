# A complete first-period contraction at a 34 boundary

Private research deduction, 10 November 2026. For an actual open word
beginning with \(34\), the first retained coordinate can be summed
over its entire period before an outer contour is chosen. The
already completed following-prefix source then replaces that entire
coordinate by a calibrated local boundary factor. This removes its
early taper, seam and far half from a specified larger restricted
polynomial, retaining a nonzero original leading coefficient.

The first remaining coordinate is still restricted to a fixed
neighborhood of its actual reference. No full-period estimate for
that coordinate, analogous claim for every initial pair, or
whole-word theorem is concluded.

## 1. Exact contraction and its original normalization

Fix a positive three/four word of length \(m\ge3\) with
\[
 \epsilon_1=0,\qquad\epsilon_2=1,\qquad n_j=3+\epsilon_j,
 \qquad k_4=\sum_{j=1}^{m}\epsilon_j,\qquad h=m-1 .
\tag{1}
\]
All references, lifts, markings and ordinary colors are those of
the original open source. Write \(X_j=e^{-2\pi iz_j}\), and retain
\[
 W_{\epsilon,N}(X)=\{d_N(X)(1+X^{-N})\}^{\epsilon}.
\tag{2}
\]
The exact complete first-period polynomial is
\[
\begin{split}
 f_{34,N}(w,Y)
   &=N\operatorname{CT}_X
          [U_{0,N}(w,X)C_{1,N}(X,Y)]\\
   &=\sum_{a=0}^{N-1}
          U_{0,N}(w,r^a)C_{1,N}(r^a,Y),\qquad
                         r=e^{-2\pi i/N}.
\end{split}
\tag{3}
\]
This is the full polynomial of
[the actual following-prefix theorem](research_mixed_three_four_following_complete_prefix.md).
The equality of the two lines is the exact band argument in
[literal conditional transfer](research_mixed_literal_transfer_norm_obstruction.md),
equations (3)--(4), with incoming flag zero. There is no first
diagonal weight or first selected alternative to remove. Every
ordinary row, triangular zero and off-grid output row remains in
(3). Its degrees in \(w,Y\) are less than \(N\).

Apply (3) to the exact terminal-contracted chart of
[reversed-cap assembly](research_mixed_reversed_cap_assembly.md),
equation (13). The whole original boundary polynomial becomes
\[
\begin{split}
 \mathcal Z_N
 ={}&\kappa_N^{m+k_4}N^{m+k_4-2}
    \operatorname{CT}_{X_2,\ldots,X_h}
       \left[
       f_{34,N}(w_L,X_2)
       \prod_{j=3}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)\right.\\
 &\left.\hspace{27mm}\cdot
       \mathcal V_{\epsilon_m,N}(w_R,X_h)
       \prod_{j=2}^{h}W_{\epsilon_j,N}(X_j)
       \right].
\end{split}
\tag{4}
\]
The conditional product is empty when \(h=2\).
In particular the complete second weight
\(d_N(X_2)(1+X_2^{-N})\) remains. The terminal transform
still contains every private terminal row and alternative.
The first contraction removes exactly one factor \(N\) from
the old outside scalar; \(f_{34,N}\) contains no extra
\(\kappa_N\), outgoing halfweight or final Gram factor.

Before terminal contraction the corresponding exact formula retains
\[
 f_{34,N}(w_L,X_2)
   \prod_{j=3}^{m}C_{\epsilon_j,N}(X_{j-1},X_j)
   \mathcal H_N(w_R,X_m^{-1})
   \prod_{j=2}^{m}W_{\epsilon_j,N}(X_j)
\tag{5}
\]
and outside scalar \(\kappa_N^{m+k_4}N^{m+k_4-1}\).
The inverse in the original terminal argument is unchanged.

For each fixed \(N\), these are identities of finite Laurent
polynomials under constant-term extraction. First perform that
extraction on independent circles; then deform the remaining entire
Laurent source. This order does not infer Fubini factorization of
a preassigned hybrid graph whose second height depended on the
first real coordinate. Formula (4) provides a different exact
source chart before such a graph is selected. It preserves both
parities and every original ordinary derivative or normal.

## 2. Actual reference and complete source near the new boundary

Let \(z_*=t_2^*\), \(a_*=t_1^*\), and \(c_*=s_3^*\) at the
actual reference of the word. The third leg \(c_*\) is in its
original \(O_3,O_4\) domain if that vertex is ordinary, or in
its \(A_3,A_4\) attached domain if it is the last vertex.
The original first two critical blocks therefore identify
\[
                         z_*=q_{34}(c_*).
\tag{6}
\]
This is the uniqueness identification in
[the all-word pre-Gram curve](research_mixed_arbitrary_prefix_pregram_curve.md)
and the following-prefix theorem. It does not substitute a
private endpoint for an ordinary input. The assumption \(m\ge3\)
is relevant: the isolated two-vertex ordinary pair has a different
last closure and is not used to establish (6).

Fix this actual base and its first height \(c_1=\Im a_*\).
Let \(P=[.22,.45]\). Retain the exact old first-plateau current
\[
 I_{P,N}(w,z)=
      N\int_P U_{0,N}(w,e^{-2\pi i(x+ic_1)})
                C_{1,N}(e^{-2\pi i(x+ic_1)},e^{-2\pi iz})\,dx .
\tag{7}
\]
There is a fixed complex neighborhood \(\mathcal U\) of
\((-2,z_*)\), and original holomorphic functions
\(\mathcal P_{34},\mathcal A_{34}\), with
\(\mathcal A_{34}\ne0\), such that
\[
\begin{split}
 f_{34,N}(w,e^{-2\pi iz})
   &=N^{-3/2}\mathcal A_{34}(w,z)
          e^{N\mathcal P_{34}(w,z)}
                       (1+O_{\rm hol}(N^{-1})),\\
 \left|e^{-N\mathcal P_{34}(w,z)}
       \bigl(f_{34,N}(w,e^{-2\pi iz})-I_{P,N}(w,z)\bigr)\right|
   &\le C N^A e^{-\delta N}
\end{split}
\tag{8}
\]
for some \(\delta>0\), on a smaller neighborhood.
The same normalized exponential estimate holds for every fixed
mixed derivative after another shrink.

Both statements are full-source conclusions. The second follows
from the exact seven-segment identity (9) and all nonplateau
bounds in Section 3 of the following-prefix theorem, with that
base held fixed. Its plateau is exactly (7), at the same \(c_1\).
All remaining real initial, left taper, right, vertical and fixed
complementary pieces are included in the difference in (8).
No mathematical numerical minimum of their gaps is required.

The original conditional action is
\[
 \mathcal P_{34}(w,z)
   =\operatorname{stat}_{a,s}
        [\mathcal T_0(a,w)+Q_1(s;a,z)]
\tag{9}
\]
on its already selected logarithmic sheet. At complete color it
is the original pre-Gram action, with the original additive
constant. In this case the last own type is four, so the extra
\(-(1-\epsilon_2)g(z)\) term in equation (17) of
[retained-prefix calibration](research_mixed_retained_prefix_unselected_plateau.md)
is zero. This calibration matters below.

## 3. The allocated prefix has a strict horizontal supporting plane

Set
\[
                    L_{34}(z)=\mathcal P_{34}(-2,z)-\tfrac12g(z).
\tag{10}
\]
The halfweight in (10) is precisely the remaining outgoing
type-four halfweight. Its Hessian sign can be checked on the
original variables, independently of a norm estimate for (3).

Write \(s=s_1\), \(a=t_1\), \(b=s_2\), and \(z=t_2\).
Before eliminating \(u,s,a,b\), the allocated phase is
\[
 \mathcal F_L(u,s,a,b,z)
 =E(s,u)+V_0(s,a)+G(a,b)+V_1(b,z)-\tfrac12g(z),
\tag{11}
\]
with the original primitives of retained-prefix calibration.
At its selected internal critical point it equals (10).
The logarithmic and constant identity follows from equations
(18)--(19) of that calibration, not from an exponentiated
stationary equation.

For the real Hermitian part of its negative Hessian, use the
notation of
[the original open Hessian proof](research_mixed_open_word_hessian.md):
\[
\begin{split}
 B(s,u)&=-2J(1/2-u)-3J(u)-J(s-u),\\
 V(x,y)&=J(x+y)-J(x)-J(y),\\
 W(s,a)&=J(s+a)-J(a).
\end{split}
\]
Up to an imaginary polynomial with real coefficients, the exact
decomposition of (11) is
\[
 B(s,u)+W(s,a)+V(a,b)+V(b,z)-J(b)-\tfrac12J(z).
\tag{12}
\]
On the original convex product \(u\in U,\ s\in E,\ a,b,z\in Q\),
the cited proof gives
\[
 -\Re B''\succ(6\pi/49)I,\qquad
 -\Re W''\succeq(\pi/8)\,da^2,\qquad
 -\Re V''\succ(\pi/8)I .
\]
The last two own terms in (12) have nonnegative negative-real
Hessians, since \(\Re\cot\pi b,\Re\cot\pi z>0\).
Every coordinate is covered. Consequently
\[
                  -\Re\mathcal F_L''\succ\mu I_5,
                         \qquad \mu=6\pi/49 .
\tag{13}
\]
All these rectangles are those of the actual original phase.

For completeness, this positivity survives the complex stationary
elimination. Put \(H=-\mathcal F_L''\), partition it into the
four eliminated coordinates and \(z\), and write
\[
 S=H_{zz}-H_{zv}H_{vv}^{-1}H_{vz},\qquad
                  \xi=(-H_{vv}^{-1}H_{vz},1)^T .
\]
Then \(H\xi=(0,S)^T\), so
\[
                \Re S=\xi^*(\Re H)\xi>\mu\|\xi\|^2\ge\mu.
\tag{14}
\]
The internal block is invertible by (13). The original local
implicit branch stays in the same product after a fixed shrink
of \(\mathcal U\). Thus \(-\Re L_{34}''>\mu\) there.

Choose a nondegenerate closed interval
\[
                  J_2=[\Re z_*-\rho_2,\Re z_*+\rho_2]
                         \Subset P
\tag{15}
\]
so that the horizontal segment \(J_2+i\Im z_*\) lies in that
neighborhood. Integrating the Hessian inequality gives
\[
 \Re L_{34}(y+i\Im z_*)
 \le \Re L_{34}(z_*)+\Re L_{34}'(z_*)(y-\Re z_*)
                       -\frac{\mu}{2}(y-\Re z_*)^2 .
\tag{16}
\]
At the actual reference,
\[
 L_{34}'(z_*)=g'(s_2^*+z_*)-\tfrac32g'(z_*),\qquad
            L_{34}'(z_*)+\partial_1\phi_3(z_*,t_3^*)=0 .
\tag{17}
\]
If the terminal-contracted chart has \(h=2\), replace the second
term by \(\Pi'(z_*)\). These are the original complex marginal
equations, including the own-four weight. No new mark or
endpoint action has been inserted.

The whole packet (8), the original unselected Fourier upper
bound, and continuity in the ordinary color now give, for every
\(\eta>0\), on a sufficiently small fixed \(w\)-disk,
\[
\begin{split}
 |f_{34,N}(w,e^{-2\pi iz})|\,
       |d_N(e^{-2\pi iz})|^{1/2}
 \le C_\eta N^{A_\eta}\exp N\{&
   \Re L_{34}(z_*)+\Re L_{34}'(z_*)(y-\Re z_*)\\
 &-\tfrac{\mu}{2}(y-\Re z_*)^2+\eta\},
 \quad z=y+i\Im z_*,\ y\in J_2.
\end{split}
\tag{18}
\]
The halfweight is only a modulus allocation. No square root of the
finite polynomial or division by a possibly zero factor is used.

## 4. An actually enlarged restricted polynomial with the old coefficient

Let \(\mathcal Z_N^P\) be exactly the whole unselected plateau
polynomial of
[the full plateau theorem](research_mixed_full_unselected_plateau.md),
with scalar \(\kappa_N^{m+k_4}N^{m+k_4-1}\) and retained
indices \(1,\ldots,h\). Define, for the remaining coordinates,
\[
 R_N(\mathbf z;w_R)
    =\prod_{j=3}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
       \mathcal V_{\epsilon_m,N}(w_R,X_h)
       \prod_{j=2}^{h}d_N(X_j)^{\epsilon_j}.
\tag{19}
\]
All coordinates in (19) are unselected and at their actual
reference heights. Put
\[
\begin{split}
 \mathcal Z_N^{P,34}
 =\mathcal Z_N^P
   +\kappa_N^{m+k_4}N^{m+k_4-2}
       \int_{J_2\times P^{h-2}}
          [f_{34,N}(w_L,X_2)-I_{P,N}(w_L,z_2)]
                         R_N(\mathbf z;w_R)\,d\mathbf x .
\end{split}
\tag{20}
\]
For \(h=2\), the last product interval is empty and its measure
is one. All domains and heights in (20) are fixed at the complete
reference while the ordinary colors vary.

Equation (20) is an exact restricted sum of the original source,
not a change of its coefficient. To see the region explicitly,
split the old plateau at \(x_2\in J_2\) and its complement.
On \(J_2\), its first integral is \(I_{P,N}/N\).
Formula (20) replaces it by \(f_{34,N}/N\), which is the entire
first-period integral. Use the exact seven-segment first cycle
from the following-prefix theorem: its plateau part is (7) and
its other oriented segments are precisely the added terms.
Outside \(J_2\), the old plateau remains. No first-period segment
or selected conditional row is lost. This is a partition in the
new exact chart, not an identification with a restricted segment
of the old coupled-height taper.

**Theorem 1.** On sufficiently small fixed ordinary-color disks,
\[
 \mathcal Z_N^{P,34}(w_L,w_R)
   =\kappa_N^{m+k_4}N^{-3/2}
       A_m(w_L,w_R)e^{N\mathcal W_m(w_L,w_R)}
                              (1+O_{\rm hol}(N^{-1})),
\tag{21}
\]
with exactly the action, nonzero coefficient and branches of
\(\mathcal Z_N^P\). All fixed normalized mixed ordinary derivatives
satisfy the corresponding remainder bounds.

*Proof.* Split the second integrand in (20) by allocating one
half of \(d_N(X_2)\) to its left factor. Equation (8) bounds
that complete difference by the same allocated phase as (18),
with the additional negative constant \(-\delta\).
The other half at \(X_2\), the remaining ordinary halves and the
terminal half are the original complete planes. At \(h=2\) the
other half belongs directly to \(\mathcal V\).
Their complex linear terms cancel by (17) and original stationarity;
their constants sum to \(M_{\rm open}\). The negative quadratic
terms can be discarded. With one total tolerance smaller than
\(\delta/4\), the integral added in (20), including its scalar,
therefore has a fixed gap from \(M_{\rm open}\).
Shrink the ordinary disks so that the real part of the original
\(\mathcal W_m\) differs from \(M_{\rm open}\) by less than
another fixed fraction of that gap. It is then exponentially
small relative to the nonzero original \(N^{-3/2}\) packet.

The full plateau theorem supplies that packet for
\(\mathcal Z_N^P\). Adding the exponentially small exact
difference proves (21), with the same \(A_m\), not just some
nonzero new symbol. All component integrals are holomorphic
on their fixed parameter neighborhoods. Nested Cauchy estimates
give the normalized derivative conclusion. Each ordinary-color
degree remains at most \(N-1\), since all contractions and
integration domains are independent of those colors.
Both parity normalizations remain those in (3)--(4).
\(\square\)

This proves preservation of the actual coefficient after adding
a whole first-coordinate period on a nonempty second-coordinate
interval. It is stronger than a statement about the local phase
in (16), but is still a restricted polynomial.

## 5. The complete contracted prefix can feed the arbitrary middle

Suppose now that safe cuts \(p,\ldots,q\) are available beyond
the first two vertices. Retain the protected unselected \(P\)
triples and arbitrary free alphabet \(F=[p+1,q-2]\) of
[clean-closing completion](research_mixed_clean_closing_edges_completion.md).
Take \(x_2\in J_2\), unselected at its actual height, and every
remaining left-prefix coordinate \(3,\ldots,p-1\) unselected
independently in \(P\), at its original height.

The literal new left modulus is
\[
 L_N^{34}
  =|f_{34,N}(w_L,X_2)|
      \prod_{j=3}^{p-1}|C_{\epsilon_j,N}|
      \prod_{j=2}^{p-2}|d_N(X_j)|^{\epsilon_j}
                      |d_N(X_{p-1})|^{\epsilon_{p-1}/2}.
\tag{22}
\]
Its baseline action replaces \(L+\phi_2\) by their original
stationary value \(L_{34}\). Apply (18), then the complete
unselected ordinary planes. Equation (17) cancels the first
joining marginal; all subsequent internal marginals cancel.
The calibrated left quantity, with the same cut tangent as
before, consequently satisfies
\[
 G_{L,N}^{34}
 \le-\frac{\mu}{2}(x_2-\Re z_*)^2
       -\kappa_*\sum_{j=3}^{p-1}(x_j-a_j)^2
                  +\eta+O_m(\log N/N),
             \qquad \kappa_*=1/2500000 .
\tag{23}
\]
Additional ordinary quadratic losses have merely been discarded.

Combine (23) with any compatible right state of
[completed boundary-state propagation](research_mixed_completed_boundary_state_propagation.md).
In the contracted chart choose one of RPc, RS3c, RS4c, RSSc,
RSPc; in the uncontracted chart choose R0u or RAu.
All its original source domains and window placement remain in
force. With its \(\Delta_R,K_R\), the exact new integrand obeys
\[
 |\mathscr J^{34}_{\sigma,N}|
 \le C_{\eta,m}N^{A_{\eta,m}}
   e^{N\{M_{\rm open}+\eta-\Delta_R-K_R
                    -\kappa\sum_{i\in F}p_i\}},
                 \qquad \kappa=1/20000 .
\tag{24}
\]
The outside scalar is the one in (4) or (5), respectively.
The clean closing edges and their charges are untouched: they
are ordinary edges far from the contracted prefix, on the same
actual reference. All free states remain in the original middle.

In the contracted chart, the regions in (24) with an active
selected suffix or a selected/nonplateau free state have common
finite gap \(1/40000\). They may be added to (20), using their
disjoint original selection and target regions. The neutral
all-plateau part on \(J_2\) is already in (20) and is not added
again. The enlarged restricted polynomial still has (21).
This conclusion retains all rows of \(f_{34,N}\), every free
middle symbol, all original second and subsequent weights,
and the ordinary disks and jets. It does not compare sums from
the two different terminal charts as disjoint regions.

## 6. Reversal, and the extra transform at the same-chart right end

There is a precise distinction between the mirrored theorem and
a same-chart right contraction. Whole matrix transposition sends a
word ending in \(43\) to one beginning in \(34\), exchanges the
ordinary colors and sends \(t_j\) to \(s_{m+1-j}\).
The original critical action and marks are preserved, as proved
in reversed-cap assembly. Applying Theorem 1 after this exact
reversal gives its right-end counterpart in the opposite retained
\(s\)-leg chart, with the same original nonzero coefficient.

In the original \(t\)-leg chart, the exact complete suffix
contraction for an ending \(43\) is instead
\[
 \mathcal B_{1,0,N}(w,X)
   =N\operatorname{CT}_Y
       [C_{1,N}(X,Y)W_{1,N}(Y)\mathcal V_{0,N}(w,Y)]
   =\mathsf L_1 f_{34,N}(w,\cdot)(X),
\tag{25}
\]
where
\[
 (\mathsf L_1 f)(X)=
       \sum_{j=0}^{N-1}
          \frac{X^{-j}p_j(X)}{P_j^2}f(r^j).
\tag{26}
\]
These are equations (5)--(9) of
[exact coherent suffix reversal](research_mixed_coherent_suffix_reversal.md),
with \(\mathsf S_1\mathsf L_0=\mathsf L_1\mathsf T_{01}\).
The result has band \([-N+1,0]\), not the nonnegative band of
\(f_{34,N}\). Its original outside scalar removes two terminal
factors \(N\), exactly as in that source's equation (10).

The already proved local packet (8) does not bound (26):
the latter uses all \(N\) physical values and their chirped
factorial weights, followed by their signed sum. In particular
one cannot replace it by \(f_{34,N}(w,X)\), reverse the arguments
of \(C_1\), or infer a calibrated plane from the degree bound.
A complete source estimate for (26) would be an additional theorem.
This obstruction to importing a local estimate is not a claim
that the actual suffix violates the desired bound.

## 7. What remains at the first retained coordinate

In (4), \(X_1\) is genuinely gone. The next coordinate \(X_2\)
is own type four and retains both alternatives of its complete
weight. This deduction treats its unselected local interval
\(J_2+i\Im t_2^*\); its remote real targets, selected alternative
and possible height attenuation are not disposed of by (8).
An early or seam state at that remaining coordinate therefore
still needs a calibrated comparison for the full product
\(f_{34,N}\), its weight and its next incidence.

For initial pairs \(33,43,44\), formula (3) has the corresponding
literal transfer, including the first complete four-weight when
needed. The present whole-source following theorem does not
cover those new retained-leg messages merely because the exact
finite transfer exists. Nor does the pure-three Fourier message
theorem identify its transformed bound with a retained-leg
pointwise bound.

The original fixed-height contour atlas already permits alternative
cycles, but its complete patch comparisons are still required.
We have not used that conditional construction to assert a global
new contour. The proved result is the concrete full-first-period
replacement (20), its unchanged nonzero packet, and its source-valid
attachment (24). No new whole open-word, knot, arbitrary short-filling
or finite-exception conclusion is inferred.

## Source bindings

| File | SHA-256 |
|---|---|
| research_mixed_literal_transfer_norm_obstruction.md | e9ce5a518439ed23b94c70eb548470ecbf9abfa5bd7c880f6828ed594a3fe0a3 |
| research_mixed_reversed_cap_assembly.md | 79d44dfbcfe8c598783f27a49dea5bc716cc62e0a2c4762a238f3b2afffd244c |
| research_mixed_three_four_following_complete_prefix.md | 87719e2611321df26470e87b614a83859b3e09f56a75af29a54a22fa71ac91de |
| research_mixed_arbitrary_prefix_pregram_curve.md | fb574ec2c0b8f7efe020af4ae3888554fc85040ef444f0c57e7bb8286c14c86c |
| research_mixed_retained_prefix_unselected_plateau.md | 4f8be2ee4fd0aceda28ad4d96bb4b57d864765438183563c34db070823d6d72b |
| research_mixed_open_word_hessian.md | 21556711a3ac410ce7d3e4dda0d3a6395cd7ee2a69993d82f5f8325c6e7dad23 |
| research_mixed_full_unselected_plateau.md | abd5dcddc9ed5057b6658bd8b7b60922540fd664c0c5c794135b19c1678c62a6 |
| research_mixed_clean_closing_edges_completion.md | cc5b75d521fe648ab5aa0974e162de02b14fb814fc628635a1126349df5dfca9 |
| research_mixed_completed_boundary_state_propagation.md | cc7b2fc0db168d00e2b75b54ec3ff51496f178e819e4e5c8d5c6b53af563cb48 |
| research_mixed_coherent_suffix_reversal.md | 53b9ac8daea4069dde59bcbe90cb991f803ef0127417c2a11081107a2b7c5843 |

All direct source proofs and the existing contraction/contour
alternatives were read. No new mathematical numerical evaluation,
saved-value arithmetic, import, compilation, test, or edit to a
frozen note was used.

