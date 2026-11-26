# The separate boundary tests and a quantitative cap-metric obstruction

Private written deduction, 10 November 2026. The exact clean-cut
reduction leaves a sum of two literal boundary log moduli. For a fixed
actual word, their target windows are disjoint. Their joint supremum
has an exact occupation-budget convolution. Setting the other window
to its actual baseline then shows that a nonpositive joint package
would require the corresponding one-sided signs, up to vanishing
finite-level errors. This statement concerns the post-cancellation
rates \(G_L,G_R\), not the older rates with artificial closing fees.

There is also a quantitative obstruction to a class of positive-norm
proofs of that package. At an actual type-four first-cap reference,
every Hermitian Cauchy estimate which is subexponentially comparable
to a positive diagonal metric loses a fixed exponential amount. A
calibrated metric would need exponential diagonal condition number
of rate at least \(1/6000\). This does not refute the coherent cap or
the proposed boundary signs, and does not exclude a genuinely coherent
matrix estimate with its conditioning explicitly controlled.

## 1. The literal post-cancellation problem

Fix one actual positive three/four word and one of the two exact charts
in equations (2)--(3) of
[the clean-cut finite-family reduction](research_mixed_exact_clean_cut_finite_boundary_reduction.md).
Use its complete-color reference, original lifts, original periodic
hybrid graph, fixed collar, and complete ordinary colors \((-2,-2)\).
Nothing below changes the reference when target coordinates are reset.
The retained length is \(h=m\) in the uncontracted chart and \(h=m-1\)
in the terminal-contracted chart. Their original scalar factors remain

\[
 \kappa_N^{m+k_4}N^{m+k_4},\qquad
 \kappa_N^{m+k_4}N^{m+k_4-1},
 \tag{1}
\]

respectively. No terminal selection is added after contraction.

Retain precisely the constants \(B,r\), interval \(I_0=[14,m-14]\),
occupation \(p_i\), and canonical searches of that reduction. Here

\[
 m\ge6r+27,\qquad
 p=16+3j,\quad q=m-15-3k,\quad 0\le j,k<r,
 \qquad F=[p+1,q-2].
 \tag{2}
\]

The first triple of occupation sum less than one, in each indicated
search order, determines its canonical label. Every preceding triple
has sum at least one. Both chosen triples are unselected in

\[
                         P=[.22,.45].
 \tag{3}
\]

Use the exact boundary moduli \(L_N(p),R_N(q)\), actions \(M_L,M_R\)
and complex marginals from equations (11)--(12) of the reduction:

\[
\begin{split}
 G_{L,N}(p)&=N^{-1}\log L_N(p)-M_L(p)
                  +\Re[P_{p,a}(z_{p-1}-r_{p-1})],\\
 G_{R,N}(q)&=N^{-1}\log R_N(q)-M_R(q)
                  +\Re[P_{q,b}(z_q-r_q)],\qquad \log0=-\infty.
\end{split}
 \tag{4}
\]

In particular \(R_N\) contains the original
\(\mathcal H_N(w_R,X_m^{-1})\) in the uncontracted chart and the
whole \(\mathcal V_{\epsilon_m,N}\) in the contracted chart. The
two halves of each cut diagonal weight remain allocated as in the
source. The proved upper comparison is

\[
 N^{-1}\log|\mathscr J_{\sigma,N}|-M_{\rm open}
 \le G_{L,N}(p)+G_{R,N}(q)-\kappa\sum_{i\in F}p_i
                         +\eta+O_{m,\eta}(\log N/N),
 \qquad \kappa=1/20000.
 \tag{5}
\]

We analyze the right side before its tolerance. We do not identify
it with the rate of the finite source on a remote configuration.

## 2. Exact occupation-budget convolution

For a left label \(j\), let \(\mathcal L_j\) consist of the original
target symbols on \([1,p]\) for which \(j\) is the first clean triple
in the left search. Similarly, \(\mathcal R_k\) uses \([q-1,h]\)
and the right search. Keep the types, reference and actual height rules
of this same word in these sets. Write

\[
 S_L=\sum_{i\in I_0\cap[1,p]}p_i,\qquad
 S_R=\sum_{i\in I_0\cap[q-1,h]}p_i.
 \tag{6}
\]

These include only the occupation originally counted in \(I_0\);
there is no new penalty on physical symbols outside that interval.
For \(0\le s\le B\), set

\[
 \ell_{j,N}(s)=\sup_{\mathcal L_j,\ S_L\le s}G_{L,N}(p),
 \qquad
 r_{k,N}(s)=\sup_{\mathcal R_k,\ S_R\le s}G_{R,N}(q).
 \tag{7}
\]

An empty supremum is \(-\infty\). All suprema are bounded above by
a finite constant by the literal finite coefficient bounds in Section 2
of the reduction; the value \(-\infty\) is allowed. No maximum or
continuity across priority interfaces is needed.

**Proposition 1.** Let \(\Omega_{jk}\) be the actual canonical
low-occupation piece with labels \(j,k\). Then, at every level \(N\),

\[
\begin{split}
 \sup_{\Omega_{jk}}
       \left(G_{L,N}(p)+G_{R,N}(q)-\kappa\sum_{i\in F}p_i\right)
 &=\sup_{\substack{b_L\in\mathcal L_j,\ b_R\in\mathcal R_k\\
                         S_L+S_R\le B}}
                  \bigl(G_{L,N}(p)+G_{R,N}(q)\bigr)\\
 &=\sup_{0\le s\le B}
                         \bigl(\ell_{j,N}(s)+r_{k,N}(B-s)\bigr).
\end{split}
 \tag{8}
\]

*Proof.* The length condition gives \(q\ge p+2\). Consequently the
left and right target windows are disjoint, even when \(F\) is empty.
Their union and \(F\) partition the retained target indices. On \(I_0\)
this gives the exact identity

\[
                         S=S_L+S_R+\sum_{i\in F}p_i.
 \tag{9}
\]

The original hybrid height at coordinate \(i\) depends only on its
own symbol and its two neighboring real symbols; see equation (4) of
[the split-cutoff graph](research_mixed_split_cutoff_hybrid_contour.md)
and Section 1 of
[the actual open-boundary reduction](research_mixed_open_boundary_comparison_reduction.md).
The left product ends at coordinate \(p-1\), so all of its heights,
weights and its tangent in (4) are determined by \([1,p]\). The right
product begins at coordinate \(q\), and is determined by \([q-1,h]\).
Missing physical neighbors retain cutoff one. Thus varying the free
symbols does not change either term in (4). In particular the proof
does not replace an arbitrary moving-height boundary by a plateau one.

The canonical tests before and at \(j\) use only \([1,p]\); those
before and at \(k\) use only \([q-1,h]\). Given the two boundary
states in the first supremum on the right of (8), set every symbol
in \(F\) to its actual unselected baseline. This preserves both
canonical labels and all boundary heights, gives \(S\le B\), and
makes the free penalty zero. Conversely every point of \(\Omega_{jk}\)
has \(S_L+S_R\le B\) and a nonnegative free penalty. This proves
the first equality. The second is the elementary allocation of the
budget between two disjoint sets, using supremizing sequences if
necessary. The reference halos may overlap, but they are fixed data;
they introduce no extra target compatibility condition. All constructions
remain in the same actual word and reference pair. \(\square\)

This is an optimization identity for the completed upper comparison
(5). It is not a factorization of the original integral, a replacement
of its graph Jacobian, or a sharp assertion about the remaining actual
middle factors. In particular no additional cancellation is available
between \(G_L\) and \(G_R\): they are already logarithms of moduli.

## 3. Neutralizing the opposite boundary

Let \(g^0_{L,N}\) be (4) for the baseline left window at the first
cut \(p_0=16\), and \(g^0_{R,N}\) its right counterpart at

\[
                              q_0=m-15.
 \tag{10}
\]

Both canonical labels are zero at baseline. The complete local factor
packets in Lemma 1 of
[the original local Gaussian theorem](research_mixed_open_local_gaussian.md)
and equation (10) of
[the terminal-contracted plateau theorem](research_mixed_full_unselected_plateau.md)
give

\[
                    g^0_{L,N},g^0_{R,N}=O_m(\log N/N).
 \tag{11}
\]

Indeed every factor in each baseline product has its original nonzero
local symbol and calibrated phase. Its modulus is a nonzero fixed
coefficient times a power of \(N\) times the exponential of its
baseline action, with relative error \(O(N^{-1})\). The marginal
in (4) vanishes there. Equation (11) applies in either exact chart,
without imposing a relative packet on any remote target.

Put

\[
\begin{split}
 L_N^*&=\max_{j<r}\ell_{j,N}(B),\qquad
 R_N^*=\max_{k<r}r_{k,N}(B),\\
 E_N^*&=\max_{j,k<r}\sup_{\Omega_{jk}}
       \left(G_{L,N}+G_{R,N}-\kappa\sum_{i\in F}p_i\right).
\end{split}
 \tag{12}
\]

**Corollary 2.** For the fixed actual word and either chart,

\[
 \max\{L_N^*+g^0_{R,N},\ R_N^*+g^0_{L,N}\}
                   \le E_N^*\le L_N^*+R_N^*.
 \tag{13}
\]

Consequently

\[
 \limsup_{N\to\infty}E_N^*\le0
 \quad\Longleftrightarrow\quad
 \limsup_{N\to\infty}L_N^*\le0
 \ \hbox{and}\ 
 \limsup_{N\to\infty}R_N^*\le0.
 \tag{14}
\]

*Proof.* Pair any admissible left state of occupation at most \(B\)
with the entire opposite side and free middle at baseline. Its right
canonical label is zero, and its left label is unchanged. This is
one of the pieces in (12), with no free occupation. The mirrored
construction applies to each right state. These two constructions
give the lower bound in (13); the upper bound follows directly from
(8). Equation (11) proves (14). \(\square\)

Thus the proposed nonpositive joint package, uniformly over all its
canonical pieces, cannot repair a strictly positive one-sided \(G\)
by an unspecified opposite-end surplus. The same test preserves any
strict deficit required whenever that one boundary window is selected
or nonplateau. This is only a necessary test for the proposed pointwise
package; a separately sharper middle comparison or cancellation in a
whole restricted integral could avoid that package altogether.

The conclusion must not be substituted into the earlier quantities
\(\mathcal B_L=G_L-A_p\), \(\mathcal B_R=G_R-E_q\). Their artificial
closing fees are absent from (4), and their separate nonpositivity has
the known quadratic obstruction in Section 3 of the open-boundary
reduction. Nor have the actual left and right reference parameters
been enlarged to independent auxiliary disks.

## 4. Dense positive metrics still need exponential conditioning

Let \(K_4\) be the original compact union of the two type-four attached
endpoint images, with the separately certified one-vertex point included,
as in the complete-cap theorem. At \(z\in K_4\), retain the literal
complete-color finite sum

\[
 U_N=U_{1,N}(-2,X)=\sum_{i=0}^{N-1}A_i,
 \qquad A_i=\frac{H_N(-2,\zeta^{-i})p_i(X)}{P_i^2},
 \qquad X=e^{-2\pi iz}.
 \tag{15}
\]

Here \(\zeta=e^{-2\pi i/N}\), \(P_i=(\zeta;\zeta)_i\) and

\[
 p_i(X)=(\zeta X;\zeta)_i,
 \qquad a_i=\overline{H_N(-2,\zeta^{-i})/P_i},
 \qquad b_i=p_i(X)/P_i,
 \qquad U_N=a^\dagger b.
 \tag{16}
\]

Every finite row remains, at both parities. In particular the possible
zeros of a complete-color coefficient have not been removed. All
denominators \(P_i\), \(i<N\), are nonzero.

For any positive definite Hermitian matrix \(H\), define its Cauchy cost
and its best diagonal condition number by

\[
\begin{split}
 \mathfrak C_H(a,b)&=(a^\dagger Ha)^{1/2}
                              (b^\dagger H^{-1}b)^{1/2},\\
 \chi(H)&=\inf_{D>0\ {\rm diagonal}}
       \frac{\lambda_{\max}(D^{-1/2}HD^{-1/2})}
            {\lambda_{\min}(D^{-1/2}HD^{-1/2})}.
\end{split}
 \tag{17}
\]

The metric and the diagonal comparison may depend on the level and
the actual reference, with no uniform entry bound assumed.

**Lemma 3.** With \(T=\sum_i|a_i b_i|\),

\[
                      \mathfrak C_H(a,b)\ge\frac{T}{\sqrt{\chi(H)}}.
 \tag{18}
\]

*Proof.* For a positive diagonal \(D\), put
\(\lambda=\lambda_{\min}(D^{-1/2}HD^{-1/2})\) and define
\(\Lambda\) similarly. Then \(\lambda D\preceq H\preceq\Lambda D\),
and inversion gives \(H^{-1}\succeq\Lambda^{-1}D^{-1}\). Hence

\[
 \mathfrak C_H(a,b)
 \ge\sqrt{\lambda/\Lambda}
             (a^\dagger Da)^{1/2}(b^\dagger D^{-1}b)^{1/2}
 \ge\sqrt{\lambda/\Lambda}\sum_i|a_i b_i|.
 \tag{19}
\]

Take diagonal matrices approaching the infimum in (17). No minimizer
is required. The second inequality is ordinary Cauchy applied to
nonnegative component moduli, and remains valid at zeros. \(\square\)

Write \(M_1(z)=\Re\mathcal T_1(z,-2)\) for the original cap action.
The complete-cap packet is
\[
 U_N=N^{-3/2}\mathcal B_1(z,-2)e^{N\mathcal T_1(z,-2)}
                                  (1+O(N^{-1})),\qquad
 \mathcal B_1(z,-2)\ne0 .
\]
It is uniform on \(K_4\), so \(U_N\ne0\) there for all sufficiently
large levels. The source-specific input below is stronger than a loose
row ceiling.
[The actual private-row obstruction](research_mixed_cap_private_row_triangle_obstruction.md),
equations (9)--(10), proves uniformly on \(K_4\)

\[
 T\ge cN^{-2}e^{N(M_1(z)+1/12000)},\qquad
 \frac{T}{|U_N|}\ge c' N^{-1/2}e^{N/12000}.
 \tag{20}
\]

Its one large summand is an original physical row near the real part
of the actual private saddle. The
[actual endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md)
place the saddle height strictly below \(-19/1000\); the proved
vertical curvature gives the strict increase to that real row.
The [complete cap packet](research_mixed_complete_first_cap_packet.md)
supplies the nonzero denominator and its original action \(M_1\).
No upper envelope is being treated as a lower bound in (20).

**Theorem 4.** Every metric in (17) satisfies

\[
 \frac{\mathfrak C_H(a,b)}{|U_N|}
       \ge\frac{c'N^{-1/2}e^{N/12000}}{\sqrt{\chi(H)}}.
 \tag{21}
\]

If a sequence of these actual cap estimates is calibrated at its
coherent rate, in the precise sense

\[
       \limsup_{N\to\infty}
          \{N^{-1}\log\mathfrak C_{H_N}(a,b)-M_1(z)\}\le0,
 \tag{22}
\]

then necessarily

\[
                 \liminf_{N\to\infty}N^{-1}\log\chi(H_N)
                                      \ge1/6000.
 \tag{23}
\]

In particular a family with \(\log\chi(H_N)=o(N)\) cannot supply
the calibrated estimate. All conclusions are uniform in the original
image whenever the proposed bounds are uniform there.

*Proof.* Combine (18) and (20). Taking logarithms of the first
inequality in (20) and using (22) gives (23). This proof includes
arbitrary polynomial prefactors and both level parities. \(\square\)

At the baseline canonical cuts, all free occupation is zero and both
literal coherent boundary rates are \(O_m(\log N/N)\). Replacing only
\(|U_N|\) by the cost (17) changes the left boundary rate by exactly

\[
                  N^{-1}\log(\mathfrak C_H/|U_N|).
 \tag{24}
\]

Every other baseline factor has its original nonzero local packet.
Thus a subexponentially diagonally conditioned metric creates a positive
liminf of at least \(1/12000\) in this upper boundary comparison,
even if the other boundary and every other factor are kept coherent.
Neither moving the safe cuts nor reserving the unchanged free
occupation pays it. This is an actual-source obstruction to the stated
norm replacement, not a counterexample to the desired signs of the
literal \(G\)'s.

## 5. Scope of the obstruction and what remains

An unrestricted dense positive metric can encode the cancellation.
For any fixed vectors with \(a^\dagger b\ne0\), there exists a positive
definite \(H\) for which \(\mathfrak C_H=|a^\dagger b|\). To see
this, multiply \(b\) by a unit scalar so \(a^\dagger b>0\), choose
the first unit basis vector along \(a\), and prescribe \(Ha=b\).
The first diagonal entry is positive; choosing the complementary
diagonal block strictly larger than its Schur-complement requirement
makes this prescription positive definite. Equality then holds in
Cauchy. The phase change does not alter either cost in (17).
This observation supplies no uniform, independently calibrated metric:
for the actual cap, Theorem 4 imposes (23) on any such choice.

The word-adapted positive metric in Section 4 of
[the positive-word spectral theorem](research_mixed_word_spectral_radius.md)
has no proved conditioning or cap-norm bound and therefore does not
contradict this result. The earlier
[literal transfer-norm obstruction](research_mixed_literal_transfer_norm_obstruction.md)
concerns unrestricted nodal phase classes; (21)--(24) instead use
the actual geometric cap at its original reference.

The new conclusions are the exact optimization (8), the necessary
one-sided tests (13)--(14), and the conditioning cost (23). No remote
coherent boundary sign is proved. A successful route can retain the
coherent cap and estimate its complementary finite currents, prove a
phase-sensitive positive metric with all conditioning and boundary
costs included, or use an exact integrated contraction that bypasses
the pointwise package. Such a contraction must retain its original
finite periods and boundary functional; its cancellation does not by
itself imply (5)'s pointwise boundary signs. The bounded short-word
cases, color-angle losses, original marking and any knot or
finite-exception conclusion remain unchanged.

## Direct source bindings

| Source | SHA-256 |
|---|---|
| research_mixed_exact_clean_cut_finite_boundary_reduction.md | 3141323e88186592367c57463413ac0a32ee7fcba5abd671f6e02147dcf612e6 |
| research_mixed_split_cutoff_hybrid_contour.md | 6318c11366520ff2080b47028ce3ef8196d0835df2a21d0d7d5a504a80b1cc67 |
| research_mixed_open_boundary_comparison_reduction.md | 5d3f875a6c1a7e0c2c9840c16674dc8ad5921bf0f2312202cb26f278c86c72ce |
| research_mixed_open_local_gaussian.md | f3717d752fea9ea640c66b80ae805becde75bbd3dc3811493622bd124e01de89 |
| research_mixed_full_unselected_plateau.md | abd5dcddc9ed5057b6658bd8b7b60922540fd664c0c5c794135b19c1678c62a6 |
| research_mixed_cap_private_row_triangle_obstruction.md | de0b4b7f4903324ef8d904d784d6c3520a5cf4f06d9efa1c86dc3523023c6a60 |
| research_mixed_complete_first_cap_packet.md | 245e3c90a322ad094466c082bdf79f4234c68bb6a4ee98af356d650907ee5f1b |
| research_mixed_open_word_endpoint_rectangles.md | ac5603badc00d42e98d17a1c5948cae011a6abd991d5249fa61d4224a829ad07 |
| research_mixed_word_spectral_radius.md | 4cd7c2e600f4d84168375ac2360616da052a0739fe25efd697ceae3a6b10f294 |
| research_mixed_literal_transfer_norm_obstruction.md | e9ce5a518439ed23b94c70eb548470ecbf9abfa5bd7c880f6828ed594a3fe0a3 |

No mathematical numerical evaluation, saved-value arithmetic, import,
test, compilation, or edit to a frozen source or manuscript is used.
