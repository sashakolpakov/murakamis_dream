# A strongly convex minimum for the complete Conway source

21 November 2026. This note concerns the original reduced Kashaev source
of a fixed literal Conway construction. Previous final notes and public
manuscripts remain unchanged.

After an explicit normalization of its local tensors, the source admits
an unweighted quartic minimum on a product of unit balls. Its real Hessian
lies between \(I\) and \(3I\), uniformly in the quantum level and the
number of vertices. The minimum has a unique interior point, and the
corresponding value satisfies
\[
 |K_N|^2\le Q_N\le\gamma|K_N|^2,\qquad
                         \gamma=\frac{197}{196}.        \tag{1}
\]
This includes zeros. An explicit degree-six polynomial gives an exact
lower-certificate maximum for the minimum. These statements concern the
original marked source; no reference coordinate or ordinary-color sum
is introduced. Their geometric volume rate remains to be proved.

## 1. The physical boundary data and its normalization

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), and
\[
 s_r=\prod_{j=1}^r2\sin(\pi j/N),\quad s_0=1,\qquad
 H_N=\mathbb C[z]/(2T_N(z/2)+2).
\]
Here \(T_N\) is the Chebyshev polynomial of the first kind. Use the
Euclidean Hermitian norm in the normalized Newton basis
\[
 b_r=\frac{\prod_{j=0}^{r-1}(q^{2j+1}+q^{-2j-1}-z)}{s_r^2},
 \qquad 0\le r\le d.                                    \tag{2}
\]
This is the full \(N\)-dimensional boundary algebra, including the first
derivatives at its double roots. Its physical operations are the product
\(M(f,g)=fg\), the turn \(Jb_r=b_{d-r}\), and the signed packets
\[
 R^{\pm1}=\kappa^{\pm1}\sum_{r=0}^d(-q)^{\pm r}b_r,
 \qquad \kappa=q^{d^2/2}.                               \tag{3}
\]
Fractional powers mean the displayed exponentials. These are the actual
complete packets. The formulas and original source conventions are in
the [Conway compiler](research_conway_full_boundary_quotient_gram.md)
and [Newton source theorem](actual_newton_turn_positive_gram.md).

Take a fixed literal expression built from prescribed leaves, products
and turns. Its ordered closure is assumed to give one knot, with the
original reduced marking and zero-framing convention. There are \(m\ge2\)
vertices, including the closing root, whose unique child is \(v_0\).
Put \(s=m-1\). Let \(f_v\in H_N\) be the true open packet of the proper
subtree at \(v\), and let the exact original closing row be \(\ell_N\).
Thus
\[
                              K_N=\ell_Nf_{v_0}.         \tag{4}
\]
The known framing phase and any recorded fixed power of \(N\) remain
in this row. Neither original closing row is replaced by a norm or
an ordinary cap.

For each local physical tensor \(T_v\), including leaves and the root,
choose the known budget
\[
 b_v=16\max(1,\|T_v\|_{\rm HS}),\qquad \sigma=\frac1{16}.
\]
The squared Hilbert--Schmidt norm is the sum of the squared absolute
values of all its coefficients. For a proper vertex \(v\), let \(B_v\)
be the product of the budgets in its proper subtree, and put
\[
                           B_{\rm tot}=\prod_vb_v.
\]
All these numbers are positive and algebraic at each level. Write
\(a_v=f_v/B_v\). The exact normalized recursion is
\[
 a_v=\Phi_v((a_c)_{c\text{ child of }v}),\qquad
 L=\ell_N/b_{\rm root},\qquad
                       k_N=K_N/B_{\rm tot}=La_{v_0}.    \tag{5}
\]
At a leaf, \(\Phi_v=f_v/b_v\) is a prescribed constant. At a turn,
\(\Phi_v=J/b_v\); at a product, \(\Phi_v=M/b_v\).
Every normalized leaf and every normalized linear or bilinear map has
norm at most \(\sigma\), as does \(L\). Induction gives
\(\|a_v\|\le\sigma\). This normalization retains all phases, markings,
and physical boundary directions. Its total scalar is kept explicitly
in (5).

## 2. An unweighted quartic objective

Use one trial packet \(x_v\in H_N\) at each proper vertex and put
\[
 \mathcal D_N=\prod_{v\ne\mathrm{root}}\{x_v:\|x_v\|\le1\},
 \qquad
 \mathcal R_v(x)=\Phi_v((x_c)_c)-x_v.
\]
Let \(G(x)=(\mathcal R_v(x))_v\). Define
\[
 E_N(x)=|Lx_{v_0}|^2+\|G(x)\|^2,\qquad
 \boxed{\quad Q_N=\gamma B_{\rm tot}^2
                   \min_{x\in\mathcal D_N}E_N(x).\quad} \tag{6}
\]
There are \(2Ns\) real variables and the degree is at most four,
independently of \(N\) and \(s\). This is the ordinary sum of squared
local recursion errors, together with the original closing term. There
are no depth weights or penalties depending on the quantum level.
The feasible set is nonempty and compact, and all coefficients and
ball radii are algebraic at each level.

All differential statements use the real inner product
\(\langle u,v\rangle_{\mathbb R}=\operatorname{Re}\sum_vu_v^*v_v\).
The gradient includes every real and imaginary Newton coefficient.

## 3. Uniform convexity

**Lemma.** On \(\mathcal D_N\), the real Hessian satisfies
\[
                              I\le D^2E_N\le3I.         \tag{7}
\]

**Proof.** The derivative of the full residual map is
\(DG=-I+A(x)\). A block of \(A\) from child \(c\) to parent \(v\)
is \(D_c\Phi_v\), with norm at most \(\sigma\). This uses the unit-ball
bound on the other input of a product. Each row has at most two child
blocks, and each child occurs in at most one parent row. Therefore
\[
 \|A(x)\xi\|^2\le2\sigma^2\sum_v\|\xi_v\|^2,\qquad
                         \|A(x)\|\le\sqrt2\sigma\le\frac18.
\]
Consequently
\[
                  \frac78\|\xi\|\le\|DG(x)\xi\|
                                       \le\frac98\|\xi\|.       \tag{8}
\]

Only product vertices contribute a second derivative to \(G\).
At such a vertex, the residual-curvature term in the half-Hessian of
\(\|G\|^2\) is
\[
                2\operatorname{Re}
                    \langle\mathcal R_v,\Phi_v(\xi_L,\xi_R)\rangle.
\]
Since \(\|\mathcal R_v\|\le1+\sigma\), its absolute value is at most
\[
 2\sigma(1+\sigma)\|\xi_L\|\|\xi_R\|
 \le\sigma(1+\sigma)(\|\xi_L\|^2+\|\xi_R\|^2).
\]
Sibling pairs belonging to different parents are disjoint. Thus the
total has absolute value at most
\(\sigma(1+\sigma)\|\xi\|^2=17\|\xi\|^2/256\), and hence at most
\(\|\xi\|^2/8\). The closing term adds at most
\(\sigma^2\|\xi\|^2\) to the half-Hessian, and adds no negative term.
Using (8), this proves the more explicit bounds
\[
 \frac{41}{32}\|\xi\|^2
 \le D^2E_N(x)[\xi,\xi]
 \le\frac{357}{128}\|\xi\|^2.
\]
They imply (7). \(\square\)

It follows that \(E_N\) has a unique minimizer on its feasible set.
The Hessian assertion concerns this product of balls; convexity on the
whole real coordinate space is not asserted.

## 4. Comparison with the original source

Integrating \(DG=-I+A\) along a segment in the convex set
\(\mathcal D_N\) gives
\[
              \|G(x)-G(y)\|\ge\frac78\|x-y\|.           \tag{9}
\]
Indeed the difference is \(-(x-y)\) plus a vector of norm at most
\(\|x-y\|/8\). The true normalized field \(a=(a_v)_v\) is feasible,
with \(G(a)=0\). Since \(\|L\|\le1/16\), (9) implies
\[
 |k_N-Lx_{v_0}|
       \le\frac1{16}\|x-a\|\le\frac1{14}\|G(x)\|.       \tag{10}
\]
Cauchy--Schwarz applied to the two terms on the right gives
\[
 |k_N|^2\le\left(1+\frac1{196}\right)
                         (|Lx_{v_0}|^2+\|G(x)\|^2).
\]
At the true field, \(E_N(a)=|k_N|^2\). Taking minima therefore proves
\[
 \frac{|K_N|^2}{\gamma}
          \le B_{\rm tot}^2\min E_N\le|K_N|^2,          \tag{11}
\]
and hence (1). No step assumes \(K_N\ne0\) or divides by it. A zero
minimum forces every residual and the closing term to vanish, so
\(Q_N=0\) precisely when \(K_N=0\).

## 5. An explicit local contracting iteration

The gradient uses only local residuals and their actual adjoints:
\[
 g_v=-2\mathcal R_v
       +2(D_v\Phi_u)^*\mathcal R_u
       +\mathbf1_{v=v_0}\,2L^*Lx_v.                    \tag{12}
\]
The middle term is present only if the parent \(u\) is proper. Define
\[
                         T(x)=x-\frac12\nabla E_N(x).   \tag{13}
\]
No projection is necessary. At a nontop vertex,
\(T_v=\Phi_v-(D_v\Phi_u)^*\mathcal R_u\), so
\(\|T_v\|\le\sigma+\sigma(1+\sigma)=33/256\).
At the top, \(T_{v_0}=\Phi_{v_0}-L^*Lx_{v_0}\), with norm at most
\(\sigma+\sigma^2=17/256\). Thus
\[
                    T(\mathcal D_N)\subset
                                      \frac{33}{256}\mathcal D_N. \tag{14}
\]
The Hessian averaged between two feasible points is self-adjoint with
eigenvalues in \([1,3]\), so \(I-H/2\) has norm at most \(1/2\).
Consequently \(T\) is a contraction on the complete set \(\mathcal D_N\).
Its iterates converge: successive displacements are bounded by a
geometric series. The limit is a fixed point \(x_*\), and contraction
makes it unique. Equation (13) gives \(\nabla E_N(x_*)=0\).
Strong convexity then identifies \(x_*\) as the unique minimum.
It is strictly interior by (14), and
\[
                         \|T^j(x)-x_*\|\le2^{-j}\|x-x_*\|.       \tag{15}
\]
Starting at zero gives the bound \(\|x_*\|\le\sqrt{s}\), independent
of \(N\) for a fixed expression. The iteration needs no dense global
Hessian. Uniform conditioning does not by itself give relative precision
when \(\min E_N\) is exponentially small. No numerical iteration has
been run here.

## 6. An exact polynomial lower certificate

For any feasible field, define
\[
                    D_N(x)=E_N(x)-\frac12\|\nabla E_N(x)\|^2.
                                                               \tag{16}
\]
This is a real polynomial of degree at most six. The lower Hessian
bound gives
\[
                            D_N(x)\le\min E_N\le E_N(x).        \tag{17}
\]
Indeed, for feasible \(y\),
\[
 E_N(y)\ge E_N(x)+\langle\nabla E_N(x),y-x\rangle_{\mathbb R}
                                            +\tfrac12\|y-x\|^2.
\]
The minimum of this quadratic over the whole real coordinate space is
\(D_N(x)\), by completing the square. This argument uses convexity
only on the feasible balls. At \(x_*\) the gradient is zero, so
\[
                     \min_{\mathcal D_N}E_N
                           =\max_{\mathcal D_N}D_N.             \tag{18}
\]
The polynomial \(D_N\) need not be concave.

Combining (11) and (17) gives, at every feasible trial field,
\[
 \boxed{\quad
 B_{\rm tot}^2\max(0,D_N(x))\le|K_N|^2
                         \le\gamma B_{\rm tot}^2E_N(x).
 \quad}                                                        \tag{19}
\]
This lower certificate includes every real and imaginary boundary
coordinate, including the physical normal directions.

For example, suppose feasible fields \(x_N\) satisfy
\[
 \|\nabla E_N(x_N)\|^2\le2(1-\eta_N)E_N(x_N),\qquad
 0<\eta_N\le1,\qquad \log\eta_N=o(N).                    \tag{20}
\]
Then \(D_N(x_N)\ge\eta_NE_N(x_N)\). If also
\(\frac\pi N\log(B_{\rm tot}^2E_N(x_N))\to V>0\), (19)
proves
\[
                         \frac{2\pi}N\log|K_N|\longrightarrow V.
\]
Thus a single controlled geometric trial field would suffice for a
volume lower bound. Neither moment stationarity nor angle stationarity
alone establishes (20), which uses the full real gradient. No geometric
trial field with the required estimates is supplied here.

## 7. Scope and an optional exact reduction

All coefficients come from the complete original source. For a fixed
literal construction, \(\log B_{\rm tot}=O(N)\); the sine-factor
bounds, crossing norms and closing normalization are recorded in
Section 7 of the
[earlier quartic note](research_anchored_conway_positive_variational_period.md).
Two exact presentations have logarithmic \(Q_N\) values differing by
at most \(\log\gamma\) whenever \(K_N\ne0\), and both values vanish
at every zero. Fixed short proper subtrees may be contracted with their
full open boundary packets before applying this construction.

There is an optional variable-projection reduction. Retain one child
variable for each binary product and eliminate every other variable.
Sibling pairs are disjoint, so if \(n_\times\) is the number of product
vertices this retains exactly \(n_\times\) packets. Every residual is
jointly affine in the eliminated variables when the retained ones are
fixed. Their inner minimization is therefore a strictly convex quadratic
problem on a product of balls. Its interaction graph consists of linear
corridors: every eliminated vertex has at most one eliminated child and
one parent. Its minimizer exists uniquely. Partial minimization preserves
strong convexity in the retained variables: interpolate the two inner
minimizers, then apply the original strong-convexity inequality and drop
the nonnegative squared displacement of the inner variables. This gives
an exact reduction to \(2Nn_\times\) outer real variables. The reduced
objective need not be polynomial.

Finally, the fixed comparison factor in (1) makes the exponential rate
of \(Q_N\) equivalent to that of the original source. Convexity has
provided a unique finite minimum, a uniformly contracting iteration,
and a lower witness at one trial field. Its asymptotic comparison with
hyperbolic volume remains necessary, including after the fixed short
partial assignments in the finite-exception program.

## Complete direct sources

The following complete matching texts were read. The first records the
earlier quartic formulation and source growth bounds; the others give
the actual full boundary operations and markings. The normalization,
convexity, source comparison, iteration and certificates are proved above.

| Source | SHA-256 |
|---|---|
| [Earlier complete-source quartic](research_anchored_conway_positive_variational_period.md) | e83c35d16c79faa13ac6556db78b9b57da2a2371d3fc04c4673ecd74e1d336f7 |
| [Complete Conway compiler](research_conway_full_boundary_quotient_gram.md) | debe56dbad8151b90d44d0fccbf0dcf33dafb780370e01c8acdadbd2939dc077 |
| [Actual Newton turn and source](actual_newton_turn_positive_gram.md) | d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3 |

Only written mathematics and text operations were used. No mathematical
program, test, build, numerical iteration, git operation or public-document
edit was performed.
