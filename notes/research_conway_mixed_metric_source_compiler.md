# A mixed physical and Newton metric for the original Conway source

24 November 2026. Written research proof.

Multiplication takes one uniform physical packet and one Newton packet
to a Newton packet with bilinear norm at most one. This follows from
the actual adjoint formulas, without comparing the condition numbers
of the two metrics. A fixed Conway tree can consequently retain one
Newton leaf, or two leaves meeting at its highest product, while all
other branches use the physical metric. The structural normalization
cost is constant except for a possible factor \(\sqrt N\) at the root.
The resulting compact reciprocal integral keeps the original closing.
No geometric lower bound is proved.

## 1. The two complete packet metrics

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and
\(x=q^d=-q^{-1}\). Use the actual physical pair algebra of [P]:
\[
 \mathcal A_N=\mathbb C[\Omega]\simeq\mathbb C[z]/P_N,\qquad
 P_N(z)=2T_N(z/2)+2,\qquad \dim\mathcal A_N=N .
 \tag{1}
\]
Here \(T_N\) is the Chebyshev polynomial. Every double-root first
normal and the odd simple-root value remain in (1). Give the original
balanced head basis \(w_0,\ldots,w_d\) its uniform orthonormal metric.
For \(f\in\mathcal A_N\), write
\[
 \iota(f)=f(\Omega),\qquad
 \|f\|_{\rm ph}=\|\iota(f)\|_{\rm HS},\qquad
 \|f\|_{\rm mat}=\|\iota(f)\|_{\rm op}.
 \tag{2}
\]
The Hilbert--Schmidt norm is unnormalized, so \(\|1\|_{\rm ph}=N\).

The other Hilbert norm makes the full Newton basis orthonormal:
\[
 c_j=q^{2j+1}+q^{-2j-1},\qquad
 S_r=\prod_{h=1}^r2\sin(\pi h/N),\quad S_0=1,\qquad
 b_r(z)=S_r^{-2}\prod_{j<r}(c_j-z),\quad 0\le r\le d .
 \tag{3}
\]
Write \(\|\cdot\|_{\rm Newt}\) for this norm and
\(f^\sharp(z)=\overline{f(\bar z)}\) for coefficient reflection.
All \(b_r\) have real coefficients. The original unscaled turn
\(\mathcal T\), multiplication \(M_f:g\mapsto fg\), and both original
closing rows obey [A,P]
\[
 \begin{gathered}
 \mathcal T b_r=b_{d-r},\qquad \mathcal T^2=I,\\
 \|\mathcal T f\|_{\rm Newt}=\|f\|_{\rm Newt},\qquad
 \|\mathcal T f\|_{\rm ph}=\|f\|_{\rm ph},\\
 M_f^{\dagger_{\rm Newt}}=\mathcal T M_{f^\sharp}\mathcal T,\\
 \lambda_0(f)=f(c_0),\qquad \lambda_d(f)=\phi(f),\qquad
 \|\lambda_0\|_{{\rm Newt},*}
   =\|\lambda_d\|_{{\rm Newt},*}=1,\qquad
 \lambda_0\mathcal T=\lambda_d .
 \end{gathered}
 \tag{4}
\]
The physical dual norms of these two rows are at most one.
The ordinary cups, cap, unrestricted mark, pivot and framing are
exactly those fixing (4); no new closure is introduced here.

## 2. A constant-one bridge, including matrix coefficients

Let \(\mathsf S\) exchange the two physical heads. In the balanced
metric the literal generators satisfy
\[
 E^*=-F,\qquad F^*=-E,\qquad K^*=K^{-1}.
 \tag{5}
\]
Using \(E_\Sigma=E_1K_2+E_2\),
\(F_\Sigma=F_1+K_1^{-1}F_2\), and the original
\(\Omega=F_\Sigma E_\Sigma+qK_1K_2+q^{-1}K_1^{-1}K_2^{-1}\),
this gives
\[
 E_\Sigma^*=-\mathsf S F_\Sigma\mathsf S,\quad
 F_\Sigma^*=-\mathsf S E_\Sigma\mathsf S,\quad
 \Omega^*=\mathsf S\Omega\mathsf S .
 \tag{6}
\]
Indeed adjoint reverses \(F_\Sigma E_\Sigma\), and the first two
identities restore that order after the exchange; the two Cartan
terms are exchanged by conjugating their scalars. Polynomial
functional calculus therefore proves
\[
 \iota(f)^*=\mathsf S\iota(f^\sharp)\mathsf S,\qquad
                  \|f^\sharp\|_{\rm mat}=\|f\|_{\rm mat}.
 \tag{7}
\]

**Theorem 1.** For every two complete packets,
\[
 \boxed{\quad
 \|M_f\|_{{\rm Newt}\to{\rm Newt}}\le\|f\|_{\rm mat},
 \qquad
 \|fg\|_{\rm Newt}\le\|f\|_{\rm ph}\|g\|_{\rm Newt}.
 \quad}
 \tag{8}
\]
Commutativity permits exchange of the two inputs.

*Proof.* The same finite linear map
\(B=(\mathcal T M_{f^\sharp}\mathcal T)M_f\) is positive in the
Newton metric, by (4). Its spectral radius is thus
\(\|M_f\|_{\rm Newt}^2\). Compute its radius instead using its
operator norm in the physical packet metric. Actual composition of
pair matrices gives
\(\|M_h\|_{{\rm ph}\to{\rm ph}}\le\|h\|_{\rm mat}\).
The physical unitarity of the genuine turn and (7) imply
\[
 \|M_f\|_{\rm Newt}^2
  =\operatorname{rad}(B)
  \le\|B\|_{{\rm ph}\to{\rm ph}}
  \le\|f^\sharp\|_{\rm mat}\|f\|_{\rm mat}
  =\|f\|_{\rm mat}^2.
 \tag{9}
\]
Finally \(\|f\|_{\rm mat}\le\|f\|_{\rm ph}\) proves (8).
No change-of-frame bound between the metrics was used. \(\square\)

There is also a full matrix amplification. Let
\(\mathbf f=(f_{ij})\in M_{a,b}(\mathcal A_N)\), let
\(\mathbf M_{\mathbf f}\) act on \(b\) Newton packets by
\((g_j)_j\mapsto(\sum_j f_{ij}g_j)_i\), and put
\(\mathbf F=(\iota(f_{ij}))\), acting on \(b\) physical pairs. Then
\[
 \boxed{\qquad
 \|\mathbf M_{\mathbf f}\|_{{\rm Newt}^b\to{\rm Newt}^a}
                              \le\|\mathbf F\|_{\rm op}.
 \qquad}
 \tag{10}
\]
For completeness, set \(\mathbf f^\ddagger=(f_{ji}^\sharp)\) and
\(\mathcal T_b=I_b\otimes\mathcal T\). Equation (4) gives
\(\mathbf M_{\mathbf f}^\dagger
 =\mathcal T_b\mathbf M_{\mathbf f^\ddagger}\mathcal T_a\).
The coefficient block matrix \((\iota(f_{ji}^\sharp))\) is
\((I_b\otimes\mathsf S)\mathbf F^*(I_a\otimes\mathsf S)\).
Physical left multiplication by a block matrix has norm at most
that block matrix's operator norm on the direct sum of pair spaces.
The outer packet turns also have physical norm one. Applying (9) to
\(\mathbf M_{\mathbf f}^\dagger\mathbf M_{\mathbf f}\) proves (10),
also for rectangular sizes. The bound is independent of \(a,b\).
It is not a claim that the Hilbert tensor flattening of the bilinear
map in (8) has norm one.

Taking \(g=1\) in the first inequality of (8) gives the useful
same-packet comparison
\[
                    \|f\|_{\rm Newt}\le\|f\|_{\rm mat}
                                           \le\|f\|_{\rm ph}.
 \tag{11}
\]

## 3. One Newton path through an arbitrary literal tree

Fix a literal tree with \(L\) prescribed leaf occurrences, \(s\)
proper vertices, products and genuine turns. Its original scalar is
\(K_N=\eta_N\lambda(A_{\rm top})\), where
\(\lambda\in\{\lambda_0,\lambda_d\}\) and \(\eta_N\) is its recorded
known external factor. Every prescribed leaf is its entire actual
packet \(A_\ell\), not its distinct-root values.

Choose any leaf \(\ell_*\). Give every vertex on its path to the
root the Newton metric and every off-path vertex the physical metric.
At a product on the path, exactly one child has the Newton metric.
Equation (8) bounds that bilinear map by one. Off-path products
have physical bilinear norm at most one by matrix composition.
Turns have norm one in either metric, and the root row has dual
norm one. These assertions hold on all packet inputs, not only on
the prescribed forward field.

For each proper vertex and the scalar root choose the known budgets
\[
 b_v=
 \begin{cases}
 16\max(1,\|A_\ell\|_{\rm Newt}),&v=\ell=\ell_*,\\
 16\max(1,\|A_\ell\|_{\rm ph}),&v=\ell\ne\ell_*,\\
 16,&v\text{ is a product or turn},
 \end{cases}
 \qquad b_{\rm root}=16\max(1,|\eta_N|).
 \tag{12}
\]
Thus every normalized map, leaf and closing has its respective
bilinear, linear or vector norm at most \(1/16\). There is no
exponential Newton multiplication budget. Relative to the physical
budgets of [P], only one leaf factor changes:
\[
 {B_{\rm one}\over B_{\rm ph}}
  ={\max(1,\|A_{\ell_*}\|_{\rm Newt})
                         \over\max(1,\|A_{\ell_*}\|_{\rm ph})}
  \le1,\qquad B_{\rm one}=\prod_v b_v .
 \tag{13}
\]
This is a comparison of known normalization products, not of the
numerical minima or integrals in different packet metrics.

## 4. Two Newton paths and one terminal quotient metric

Suppose \(L\ge2\). Let \(v_*\) be the highest binary product; above
it there are only genuine turns before the scalar closing. Choose
one leaf in each child subtree of \(v_*\). Use the one-path assignment
inside each child subtree, making both packets entering \(v_*\)
Newton packets. All remaining vertices below it are physical.

At \(v_*\) use the already constructed multiplication quotient of [Q].
In fixed Newton coordinates let
\[
 M:\mathcal H_{\rm Newt}\otimes_2\mathcal H_{\rm Newt}
       \longrightarrow\mathcal A_N,\qquad
 C=MM^\dagger,\qquad \|y\|_{\rm quot}^2=y^\dagger C^{-1}y .
 \tag{14}
\]
Multiplication is surjective since \(M(y\otimes1)=y\); hence
\(C>0\), with every boundary coordinate retained. The map
\(C^{-1/2}M\) is a coisometry, so the product into this quotient
metric has bilinear norm at most one.
Transport the quotient metric through each turn above \(v_*\):
define \(\|\mathcal T y\|_{\rm next}=\|y\|_{\rm previous}\).
Every such turn has norm one by definition, with its literal
unscaled matrix retained.

If there are \(h\) turns above \(v_*\), put
\(\lambda'=\lambda\mathcal T^h\). This is either \(\lambda_0\)
or \(\lambda_d\). The exact original rows give [A,Q]
\[
 \|\lambda_0M\|_{\otimes_2,*}=1,\qquad
 \|\lambda_dM\|_{\otimes_2,*}=\sqrt N .
 \tag{15}
\]
Indeed \(\lambda_0(ab)=a_0b_0\), while
\(\lambda_d(ab)=a^{\mathsf T}Jb\) with \(J\) the reversal
matrix. Their flattened rows have respectively one and \(N\)
unit entries. Consequently the final transported quotient has
root dual cost
\[
 \gamma_N=
 \begin{cases}1,&\lambda'=\lambda_0,\\
 \sqrt N,&\lambda'=\lambda_d.
 \end{cases}
 \tag{16}
\]
Use Newton leaf budgets at the two selected leaves, physical budgets
at all others, budget \(16\) at every product and turn, and
\[
                    b_{\rm root}=16\max(1,|\eta_N|\gamma_N).
 \tag{17}
\]
This gives a second full-dimensional compiler with every normalized
local norm at most \(1/16\). Its budget product satisfies
\[
 {B_{\rm two}\over B_{\rm ph}}
 ={\max(1,|\eta_N|\gamma_N)\over\max(1,|\eta_N|)}
   \prod_{\ell\ {\rm selected}}
       {\max(1,\|A_\ell\|_{\rm Newt})
                              \over\max(1,\|A_\ell\|_{\rm ph})}.
 \tag{18}
\]
The quotient and its transport depend only on the original operations,
not on the selected leaf values or the unknown scalar.
No comparison of its condition number with the physical metric is used.

The direct scalar upper bound is slightly sharper than the flattened
root budget: both bilinear rows \(\lambda_0(ab)\) and
\(\lambda_d(ab)\) have norm one on separately unit Newton inputs.
Inducting below \(v_*\) therefore gives
\[
 |K_N|\le|\eta_N|
   \prod_{\ell\ {\rm selected}}\|A_\ell\|_{\rm Newt}
   \prod_{\ell\ {\rm other}}\|A_\ell\|_{\rm ph}.
 \tag{19}
\]
There is no factor \(\sqrt N\) in (19). That factor in (16) is the
linear dual norm required for the full quotient packet compiler.

## 5. The same original scalar in a compact reciprocal integral

Apply [C] to either assignment above, with its actual packet metrics
and budget product \(B_{\rm mix}\). Multiply all \(s\) proper budgets
and the root budget by \(N\):
\[
 \widehat B_{\rm mix}=N^{s+1}B_{\rm mix},\qquad
                         \sigma_N=(16N)^{-1}.
 \tag{20}
\]
In orthonormal coordinates for these metrics the residual map still
has own-output coefficient \(-I\), polynomial triangular inverse,
and real Jacobian one. Its energy, including the original scalar
row, has degree at most four. Keep one child per binary product and
solve the other packet equations exactly. Write \(F_{\rm mix}(u)\)
for the remaining residuals and scalar row. Then, with
\(n=N(L-1)\) and the product \(\mathcal U_N\) of retained unit balls,
\[
 \mathcal J_{\rm mix}={n!\over\pi^n}
        \int_{\mathcal U_N}\|F_{\rm mix}(u)\|^{-2(n+1)}du .
 \tag{21}
\]
The measure is rebuilt in the stated orthonormal coordinates.
For a fixed tree, [C] proves uniformly over its normalized leaf choices
\[
 \boxed{\qquad
 |K_N|^2={\widehat B_{\rm mix}^{\,2}\over\mathcal J_{\rm mix}}
                   \bigl(1+O_{\mathscr T}(N^{-1})\bigr)
 \qquad(K_N\ne0).
 \qquad}
 \tag{22}
\]
At a source zero the integral is infinite and its reciprocal is zero.
The one-point convention covers \(L=1\). All phases and full Hermite
directions survive these metric choices and forward substitutions.

The actual single signed crossing has, with \(\kappa=q^{d^2/2}\), [A]
\[
 R^{\pm1}=\kappa^{\pm1}\sum_{r=0}^d(-q)^{\pm r}b_r,\qquad
                      \|R^{\pm1}\|_{\rm Newt}=\sqrt N .
 \tag{23}
\]
Thus one or two such selected leaves have this explicit polynomial
leaf budget. An arbitrary fixed \(R^p\) must retain its actual Newton
norm; no polynomial bound for all powers is asserted.

The gain is a source-exact choice of packet metrics with smaller
known leaf factors and no large Newton structural multiplication
budget. Equations (21)--(22) define new normalized integrals, not a
free change in the value of an earlier integral. The original cap
and the new budgets must both remain. The dimension and denominator
power grow with \(N\) when \(L>1\). A geometric upper estimate on
\(\mathcal J_{\rm mix}/\widehat B_{\rm mix}^{\,2}\), or an original
closing lower certificate, is still required. There is no new
volume-conjecture case or finite-exception theorem.

## Complete inputs and coverage

The complete matching texts below fix the two source metrics, the
existing quotient construction, and the compact integral comparison.
The mixed inequality and its path assignments are proved above.

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| A | [Newton turn, adjoints and original rows](actual_newton_turn_positive_gram.md) | 434 | d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3 |
| P | [Uniform physical source compiler](research_conway_uniform_physical_quartic.md) | 477 | 39895b430535f565d30133b46ef57f67589207bc83f40597ffe96e2ce79bbda8 |
| Q | [Full multiplication quotient and closing costs](research_conway_full_boundary_quotient_gram.md) | 463 | debe56dbad8151b90d44d0fccbf0dcf33dafb780370e01c8acdadbd2939dc077 |
| C | [Compact reciprocal source comparison](research_conway_compact_reciprocal_source.md) | 321 | 94f261ac94d20b676cf02c3fb39514ebcb7e2a7c42e114bc5bb0ecb413a7e2b4 |
