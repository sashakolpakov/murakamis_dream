# Polynomial structural costs in the uniform physical Conway metric

22 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

The full physical pair algebra has a positive metric in which the
actual quarter-turn is unitary, multiplication has polynomial tensor
norm, and both original closing rows have polynomial dual cost.
Consequently the synthesis covariance of every fixed unfilled Conway
tree has polynomial condition number. This uses the uniform balanced
physical metric, rather than the normalized Newton coefficient metric
or the binomial head metric.

Recompiling the known convex quartic in this metric permits constant
structural budgets. Its leaf norms and its numerical
minimum change. This is not a bound on the surviving projection of
the actual leaf data or on its overlap with the original closing.

## 1. The full physical algebra and the chosen positive metric

Fix \(N\ge2\), \(d=N-1\), and
\[
 q=e^{\pi i/N},\qquad Q=q^2,\qquad x=q^d=-q^{-1}.
 \tag{1}
\]
Declare the recorded balanced physical basis \(w_0,\ldots,w_d\)
orthonormal. This is the **uniform** head metric:
\(\|w_a\|=1\), not \(\binom da^{-1/2}\).
Give \(V_N\otimes V_N\) its product metric and its endomorphisms
the unnormalized Hilbert--Schmidt inner product
\[
 \langle A,B\rangle_{\mathrm{ph}}=\operatorname{Tr}(A^*B).
 \tag{2}
\]
In particular the identity on the physical pair has norm \(N\).

The original balanced generators and the actual pair Casimir are
\[
 Ew_a=(Q^{-a}-1)w_{a-1},\quad
 Fw_a=(1-Q^{a+1})w_{a+1},\quad Kw_a=xQ^{-a}w_a,
\]
\[
 E_\Sigma=E_1K_2+E_2,\quad
 F_\Sigma=F_1+K_1^{-1}F_2,\quad
 \Omega=F_\Sigma E_\Sigma+qK_1K_2+q^{-1}K_1^{-1}K_2^{-1}.
 \tag{3}
\]
Missing extreme arrows are zero. The complete physical commutant
theorem identifies
\[
 \begin{gathered}
 \mathcal A_N=\mathbb C[\Omega]\simeq\mathbb C[z]/P_N(z),
 \qquad\mathcal A_N\subset\operatorname{End}(V_N\otimes V_N),\\
 P_N(z)=2T_N(z/2)+2 .
 \end{gathered}
 \tag{4}
\]
faithfully, and \(\dim_{\mathbb C}\mathcal A_N=N\).
Here \(T_N\) is the Chebyshev polynomial of the first kind.
All first derivatives at double Casimir roots remain independent
directions of this space, including at even and composite levels.
Restriction of (2) to \(\mathcal A_N\) is positive definite.
We do not replace (4) by its distinct-root value quotient.

All physical coefficients below are known before evaluating a closed
source. One can choose a concrete Hilbert--Schmidt orthonormal basis
\(F_1,\ldots,F_N\) of \(\mathcal A_N\) by Gram--Schmidt applied to
\(I,\Omega,\ldots,\Omega^d\), with positive normalizing square roots.
These powers are independent by the full minimal polynomial (4).
Their finite entries, Gram matrix, and resulting basis are algebraic
at each level. No source value or chosen leaf packet enters this choice.
No numerical conditioning of that basis construction is asserted.

## 2. Actual turns, products, and both original closures

The actual cup, ordinary cap, and unrestricted marked cap in the
recorded all-primal chart are
\[
 p_{ab}=Nx^{-b}\mathbf1_{a+b=d},\qquad
 \ell_{ab}=x^a\mathbf1_{a+b=d}/N,\qquad
 m_{ab}=x^b/N^2.
 \tag{5}
\]
Their fixed duality conventions and snakes are those of the source
directs. In particular \(mp=1\). The marked cap is not substituted
for the ordinary cap inside a turn.

Let \(\mathcal T\) be the genuine unscaled quarter-turn. On a whole
physical Hopf box \(B\in\mathcal A_N\), its exact formula is
\[
 (\mathcal TB)_{(a,b);(c,e)}
       =x^{a-e}B_{(d-a,c);(b,d-e)}.
 \tag{6}
\]
This formula uses the symmetry of actual Hopf boxes in the recorded
chart; no all-array identification of different oriented bends is
needed here. It is the original cup/cap contraction on
\(\mathcal A_N\), with their \(N\) and \(1/N\) factors canceled
exactly, not an additional crossing or a rescaling of the turn.
It preserves \(\mathcal A_N\) and obeys \(\mathcal T^2=I\).

The index map on the right of (6) permutes the entire four-index
array, and \(|x^{a-e}|=1\). Summing the absolute squares of all entries
therefore proves
\[
 \boxed{\quad
 \|\mathcal TB\|_{\mathrm{ph}}=\|B\|_{\mathrm{ph}},\qquad
 \|\mathcal T\|_{\mathrm{op}}=1,\qquad
 \|\mathcal T\|_{\mathrm{HS}(\mathcal A_N)}=\sqrt N .
 \quad}
 \tag{7}
\]
The last norm is the coefficient-tensor norm of this linear map
on the \(N\)-dimensional positive space, not a norm of one box.

Product is ordinary physical composition
\(M(A,B)=AB\). The elementary matrix inequality
\[
 \|AB\|_{\mathrm{ph}}
       \le \|A\|_{\mathrm{ph}}\|B\|_{\mathrm{op}}
       \le \|A\|_{\mathrm{ph}}\|B\|_{\mathrm{ph}}
 \tag{8}
\]
gives its bilinear norm at most one. In the orthonormal basis above,
\[
 \|M\|_{\mathrm{HS}}^2
     =\sum_{i,j=1}^N\|F_iF_j\|_{\mathrm{ph}}^2\le N^2.
 \tag{9}
\]
Thus its tensor operator norm is also at most \(N\). This sharper
restriction bound is sufficient; the full ambient pair-matrix
composition tensor has Hilbert--Schmidt norm \(N^3\).

Retain the original two normalized closing rows
\[
 \lambda_d(B)=\phi(B)
       =\frac1N\operatorname{Tr}[(I\otimes g)B],
 \quad g=K^{1-N}=(-1)^dK,
 \qquad
 \lambda_0(B)=mBp .
 \tag{10}
\]
The exact sewing identity, including the unrestricted mark, is
\[
                    \lambda_0=\phi\circ\mathcal T
                         \quad\hbox{on }\mathcal A_N .
 \tag{11}
\]
It retains every Hermite channel. For example, on \(f(\Omega)\),
these are the full Frobenius functional and \(f(q+q^{-1})\).

Since \(g\) is diagonal unitary, the ambient functional \(\phi\)
has Hilbert--Schmidt dual norm
\(\|I\otimes g\|_{\mathrm{HS}}/N=1\). Restriction and (7)--(11)
give \(\|\lambda_d\|_*,\|\lambda_0\|_*\le1\).
Conversely \(\lambda_0(I)=1\) and \(\phi(\mathcal TI)=1\);
both \(I\) and \(\mathcal TI\) have physical norm \(N\). Hence
\[
 \boxed{\qquad
        N^{-1}\le\|\lambda_0\|_*=\|\lambda_d\|_*\le1 .
 \qquad}
 \tag{12}
\]
The equality of the two norms follows from the unitary involution.
Off this physical algebra the marked functional \(B\mapsto mBp\)
has ambient dual norm \(\sqrt N\), since
\(\|p\|=N^{3/2}\) and \(\|m\|_*=N^{-1}\).
The stronger bound in (12) uses the exact restricted identity (11).
No ordinary cap has replaced the original mark on arbitrary arrays.

## 3. Polynomial covariance for every unfilled Conway tree

Let \(E\) be a fixed finite expression whose leaves are independent
copies of the entire space \(\mathcal A_N\), with binary products
and genuine turns. If there are \(l\) leaf occurrences and \(p\)
products, then \(p=l-1\). The actual synthesis map is
\[
 B_E:\mathcal A_N^{\otimes l}\longrightarrow\mathcal A_N,
 \quad
 B_{\mathrm{leaf}}=I,\quad
 B_{\mathcal TE}=\mathcal TB_E,\quad
 B_{EF}=M(B_E\otimes B_F).
 \tag{13}
\]
All tensor products use the physical Hilbert metrics. The map depends
on the unfilled expression, not on the eventual filling leaf values.

**Theorem.** There is an explicit linear right inverse \(S_E\), using
only (13), the physical identity box, and turns, with
\[
 B_ES_E=I,\qquad \|B_E\|_{\mathrm{op}}\le N^p,\qquad
                          \|S_E\|_{\mathrm{op}}\le N^p .
 \tag{14}
\]
Consequently, for \(C_E=B_EB_E^*\),
\[
 \boxed{\qquad
  N^{-2p}I\le C_E\le N^{2p}I,\qquad
                  \operatorname{cond}_2(C_E)\le N^{4p}.
 \qquad}
 \tag{15}
\]
For either original normalized row in (10), its squared dual cost
in the synthesis quotient norm is
\[
 a_\lambda(E)=\lambda C_E\lambda^*,\qquad
              N^{-2p-2}\le a_\lambda(E)\le N^{2p}.
 \tag{16}
\]
These bounds are uniform over the filling assignments at the leaves.

**Proof.** Equations (7) and (9) give
\(\|B_E\|\le N^p\) by induction. Define
\[
 S_{\mathrm{leaf}}=I,\qquad
 S_{\mathcal TE}=S_E\mathcal T,\qquad
 S_{EF}=(S_E\otimes S_F)\iota,\quad
                         \iota(y)=y\otimes I .
 \tag{17}
\]
The last \(I\) is the known physical identity box, not an identity
depending on an unknown tangle value. Since \(M(y,I)=y\) and
\(\mathcal T^2=I\), induction gives \(B_ES_E=I\).
Also \(\|\iota\|=\|I\|_{\mathrm{ph}}=N\), proving the right-inverse
bound in (14).

For any \(y\), the identity \(B_ES_E=I\) gives
\[
 \|y\|^2
   =|\langle B_E^*y,S_Ey\rangle|
   \le N^p\|B_E^*y\|\|y\|.
 \]
Thus \(\|B_E^*y\|\ge N^{-p}\|y\|\). Together with the upper bound
in (14), this proves (15). Applying (15) to the Riesz vector of
\(\lambda\) and using (12) proves (16). \(\square\)

For example the least-norm expanded lift is
\(B_E^*C_E^{-1}y\), and its squared norm is \(y^*C_E^{-1}y\).
This follows directly by splitting any other lift into that vector
and a vector in \(\ker B_E\). The latter is orthogonal to
\(\operatorname{ran}B_E^*\). Equation (15) therefore makes this
quotient norm polynomially equivalent to the fixed physical norm.
It does not identify a prescribed leaf tensor with its least-norm
lift.

The exponent \(p\) is fixed by the template. No bound independent
of a growing tree size, and no filling-dependent cancellation
estimate, is being deduced from (15).

Every leaf in (13)--(17) is still an independent copy of the full
algebra. The right inverse is allowed to insert the identity into
those slots. It need not respect a prescribed short filling at a
leaf. Thus (15) does not give a lower singular-value bound for a
partially specialized boundary channel after some incoming packets
have been fixed. Such a channel can have a kernel or poor conditioning.
For the filling application, keep all crossing blocks as variable
leaf slots when constructing \(B_E\), and only then insert their
actual fixed or free filling packets as the input tensor \(v\).
Their surviving projection and closing angle remain separate data.

## 4. The convex quartic with constant structural budgets

Take an actual literal source expression with prescribed full leaf
boxes \(A_v\in\mathcal A_N\). The root is one of (10), multiplied,
if necessary, by its recorded known scalar \(\eta_N\).
All framing phases and any specified cut or peripheral normalization
remain in this scalar; it is not chosen from the value of the source.

Choose the following known budgets:
\[
 \begin{array}{c|c}
 \text{vertex}&b_v\\ \hline
 \text{prescribed leaf }A_v&16\max(1,\|A_v\|_{\mathrm{ph}})\\
 \text{product}&16\\
 \text{genuine turn}&16\\
 \text{root }\eta_N\lambda&16\max(1,|\eta_N|)
 \end{array}
 \qquad B_{\mathrm{ph}}=\prod_v b_v .
 \tag{18}
\]
In particular an identity leaf has budget \(16N\).
Every normalized leaf has norm at most \(\sigma=1/16\);
every normalized linear map and closing row has operator norm
at most \(\sigma\); and every normalized product has bilinear
norm at most \(\sigma\), by (7), (8), and (12).

This last norm is the supremum over two separately unit inputs.
It is not the norm of the linear map on the Hilbert tensor product
or the coefficient Hilbert--Schmidt norm. In particular (9) only
bounds the normalized product's coefficient norm by \(N/16\).
The convexity and source proof below uses the bilinear bound,
not a level-independent coefficient norm. One may instead use
the larger polynomial budgets \(16N\) and \(16\sqrt N\) for
products and turns if a separate argument requires small
coefficient norms. That gives another valid recompilation,
not the same numerical minimum.

For each proper vertex \(v\), divide its true physical packet by
the product of the budgets in the subtree rooted at \(v\), including
the budget at \(v\) itself. Denote the
result by \(a_v\). The normalized maps \(\Phi_v\) are the actual
leaf, product, or turn divided by its own budget. Their exact
recursion and the normalized original root row \(L\) give
\[
       a_v=\Phi_v((a_c)_c),\qquad
                    La_{\mathrm{top}}=K_N/B_{\mathrm{ph}} .
 \tag{19}
\]
The true field has each packet norm at most \(\sigma\).
All derivatives below use the real part of the direct-sum physical
inner product. On the product \(\mathcal D\) of physical unit balls put
\(\mathcal R_v(z)=\Phi_v((z_c)_c)-z_v\), \(G=(\mathcal R_v)_v\), and
\[
 E_{\mathrm{ph}}(z)=
       \sum_{v\ {\rm proper}}
       \|\Phi_v((z_c)_c)-z_v\|_{\mathrm{ph}}^2
                          +|Lz_{\mathrm{top}}|^2 .
 \tag{20}
\]
There are \(2Ns\) real variables for \(s\) proper vertices,
and the degree is at most four.

The dimension-free normalized source proof applies in these new
orthonormal coordinates using the bounds just stated.
Explicitly \(DG=-I+A\), with each child
appearing in one parent row and at most two children per row, so
\(\|A\|\le\sqrt2\sigma\le1/8\).
The half-Hessian residual curvature is bounded by
\(\sigma(1+\sigma)\sum_v\|h_v\|^2\), using disjoint sibling pairs.
The scalar closing adds a positive term of norm at most \(\sigma^2\).
These are the same bounds as in the normalized convex theorem and give
\[
 I\le D_{\mathbb R}^2E_{\mathrm{ph}}\le3I,\qquad
 \left\|z_v-\tfrac12(\nabla E_{\mathrm{ph}})_v\right\|
                                            \le33/256 .
 \tag{21}
\]
Thus the half-gradient map is a contraction with factor \(1/2\),
the unique minimum is interior, and the Hessian bounds are uniform
in the level and the number of vertices.
Indeed the half-step at a nontop packet is
\(\Phi_v-(D_v\Phi_{\mathrm{parent}})^*\mathcal R_{\mathrm{parent}}\),
of norm at most \(\sigma+\sigma(1+\sigma)=33/256\);
at the top it is \(\Phi_v-L^*Lz_v\), of norm at most
\(\sigma+\sigma^2=17/256\).

For completeness, segment integration gives
\(\|G(z)-G(a)\|\ge(7/8)\|z-a\|\).
Since \(\|L\|\le1/16\),
\[
 |K_N/B_{\mathrm{ph}}-Lz_{\mathrm{top}}|
                           \le\|G(z)\|/14 .
 \]
One Cauchy--Schwarz inequality and the true competitor (19) prove
\[
 \boxed{\qquad
 B_{\mathrm{ph}}^2\min_{\mathcal D}E_{\mathrm{ph}}
     \le |K_N|^2
     \le\frac{197}{196}B_{\mathrm{ph}}^2
                                      \min_{\mathcal D}E_{\mathrm{ph}} .
 \qquad}
 \tag{22}
\]
This includes zeros and uses the original scalar closing.
At any feasible trial,
\[
 D_{\mathrm{ph}}(z)=E_{\mathrm{ph}}(z)
                     -\tfrac12\|\nabla E_{\mathrm{ph}}(z)\|^2
                         \le\min E_{\mathrm{ph}},
 \tag{23}
\]
by completing the square in the strong-convexity inequality.
Hence the original lower witness remains available with the new
budget:
\[
 B_{\mathrm{ph}}^2\max(0,D_{\mathrm{ph}}(z))
       \le |K_N|^2
       \le(197/196)B_{\mathrm{ph}}^2E_{\mathrm{ph}}(z).
 \tag{24}
\]
The polynomial degree assertion here concerns the objective.
No degree-four semidefinite exactness theorem under the
constant bilinear-norm budgets is inferred.

For a fixed template, all nonleaf factors in (18) are constant,
apart from the explicitly retained scalar \(\eta_N\).
Thus structural gluing contributes no level-dependent budget.
This does not estimate
the leaf packets by their nodal eigenvalues.
For a coarse finite growth check, (3) gives
\(\|\Omega\|_{\mathrm{op}}\le18\).
For the full Newton polynomials
\[
 c_j=q^{2j+1}+q^{-2j-1},\quad
 s_r=\prod_{j=1}^r2\sin(\pi j/N),\quad s_0=1,\quad
 b_r(z)=s_r^{-2}\prod_{j<r}(c_j-z),
 \]
one has
\[
 \|b_r(\Omega)\|_{\mathrm{ph}}\le N20^r/s_r^2
                        \le20^d/N,\qquad 0\le r\le d.
 \]
Indeed \(s_rs_{d-r}=N\) and \(s_{d-r}\le2^{d-r}\).
The exact signed packets
\(R^{\pm1}=\kappa^{\pm1}\sum_r(-q)^{\pm r}b_r\),
where \(\kappa=e^{\pi i d^2/(2N)}\),
therefore obey \(\|R^{\pm1}\|_{\mathrm{ph}}\le20^d\).
Fixed products and turns of these packets have at most
exponential growth, by (7)--(8). Thus a fixed literal construction
from signed crossing packets and identities, products, and turns
still has \(\log B_{\mathrm{ph}}=O(N)\).
This is a coarse upper bound, not a selected geometric rate.

## 5. What has and has not changed

The earlier fixed Newton coefficient metric makes the turn unitary
and the two closing rows unit vectors, but its multiplication and
unfilled synthesis covariance can have exponential cost.
The present theorem changes the positive metric to the inherited
uniform physical Hilbert--Schmidt metric. It proves polynomial
structural costs in that metric, rather than contradicting those
Newton-metric lower bounds.

In particular \(B_{\mathrm{ph}}\), the normalized trial coordinates,
and the raw minimum (20) are new. They are not asserted to agree
with their counterparts in the earlier quartic. Both constructions
retain the same original source and have their stated constant-factor
comparisons to it. No uniformly conditioned change to Newton
coordinates is needed to evaluate (20) from full physical matrices.

If a full physical matrix approximation to a true box is supplied,
orthogonal projection onto \(\mathcal A_N\) cannot increase its
Hilbert--Schmidt error. This retains all \(N\) physical Hermite
coordinates. It does not turn a one-coherent-input estimate into a
whole-matrix estimate.

For actual leaf tensors \(v=\bigotimes_jA_j\), there remains the
projection onto \((\ker B_E)^\perp\) and then the angle with the
prescribed closing row. Neither (15) nor (16) bounds these quantities
below. In particular a polynomially conditioned synthesis covariance
does not make an arbitrary signed closed period a positive norm.

The physical metric here also differs from the binomial metric used
in the small-activity full-norm Euler packet estimates. No estimate
is transferred between those metrics without its actual cost.
There is no new original-source lower bound, geometric trial field,
or arbitrary-short-filling volume theorem in this note.

## Complete proof sources and coverage

The following entire matching sources were read. Their actual
finite identities are used above; all new norm, covariance and
recompilation estimates are proved inline.

| Source | SHA-256 |
|---|---|
| [Full physical pair commutant and original trace](actual_pair_casimir_commutant_and_rotated_trace.md) | 00ab946b3eddb61256bdbd8ec487789a15991a80e1a28b4eee53bbb4a00f7666 |
| [Actual Newton turn, signed packets and both closures](actual_newton_turn_positive_gram.md) | d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3 |
| [Full-circle sewing and the literal marked closure](general_augmented_graph_source_extension.md) | 74487abaae10416cc967b21f442bc05502cc634acd03cd43a38deeaafa5ef86a |
| [Dimension-free normalized convex source](research_convex_normalized_conway_source.md) | 6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c |

For coverage, the entire boundary-quotient note at
debe56dbad8151b90d44d0fccbf0dcf33dafb780370e01c8acdadbd2939dc077
and the entire balanced bridge-source note at
6f4d4847218954dc0eff16b2269ada870f36afbaaddd7e1708e8f9e05b5d896f
were read at matching versions. The former already constructs the
synthesis quotient metric in Newton coordinates; the latter already
proves polynomial physical cup/cap norms. The addition here is the
uniform-physical restricted multiplication bound, the explicit
polynomial right inverse and all-tree covariance comparison, and the
resulting source-exact quartic with constant structural budgets.
No general novelty is claimed for Hilbert--Schmidt inequalities,
least-norm lifts, or strongly convex residual formulations.

Only written mathematics and text/hash operations were used.
No mathematical program, numerical test, build, git operation,
or earlier-final edit was performed.
