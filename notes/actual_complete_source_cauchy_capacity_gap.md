# When one shared positive Cauchy torus loses exponential accuracy

31 October 2026. The theorem concerns the full positive endpoint source on its shared face variables. It does not assert growth of the oscillatory invariant beyond volume.

## 1. The two different capacities

Fix an actual certified simple-white marked plat with $R$ ports and $R$
ordinary faces. Keep its adjacent protected faces exactly zero. Set
$h_f=\log L_f$ at ordinary faces and fix the common-scale gauge
$\sum_fh_f=0$. Write

$$
\begin{aligned}
F(h)&=\sum_e X_e(e^h)-\sum_f h_f,\\
J(h)&=\sum_e H_e(e^h)-\sum_f h_f,\\
X_e&=Q(x_e,b_e,y_e)+Q(x_e,c_e,y_e),\\
H_e&=\max\bigl(\{X_e\}\cup\{\log b_e:b_e>0\}
                            \cup\{\log c_e:c_e>0\}\bigr).
\end{aligned}\tag{1}
$$

The complete triangle theorem gives a unique minimizing gauge class $h^*$
for $F$, with

$$
F(h^*)=\Phi_D=\frac{\operatorname{Vol}(Y_D)}{2\pi}.\tag{2}
$$

In contrast, $H_e$ is the weighted rate of the **full** positive endpoint
polynomial, as proved in the [closed half-block theorem](actual_fejer_half_block_entropy.md),
Section 2. All variables in each expression are shared across the original
ports. Zero protected variables are removed from the supported corner sets.

**Theorem.** Both infima in (1) are attained on the scale quotient, and

$$
\min_hJ(h)=\Phi_D
\quad\Longleftrightarrow\quad
X_e(e^{h^*})\geq\log b_e,\ \log c_e
\text{ for every positive middle}.\tag{3}
$$

In particular, a strict failure of this nonstrict packing condition at
one port implies

$$
\min_hJ(h)>\Phi_D.\tag{4}
$$

This concerns nonstrict balance in (3). Equality at a local target does
not imply the strict condition used by the full filling theorem.

## 2. Coercivity from the actual triangle incidences

Let $a^*_{tf}$ be the normalized complete triangle angles. Each row has
sum $1/2$, every ordinary face has sum one, and every allowed ordinary
corner is positive. A row with just one ordinary corner has its fixed
value $1/2$. For a real ordinary-face vector $v$, define

$$
B_\triangle(v)=\frac12\sum_t\max_{f\in t\text{ ordinary}}v_f
                       -\sum_fv_f.\tag{5}
$$

Using the face balances of $a^*$, (5) is the sum of nonnegative row
differences between a maximum and a strictly positive weighted mean.
Equality forces $v$ to be constant on the allowed corners of every row.
The ordinary-face adjacency graph is connected: removing the two marked
vertices from a simple triangulated sphere leaves a connected graph.
Every remaining white edge occurs in an actual triangle row. Hence equality
forces all ordinary values to be equal.

On the unit sphere of the zero-sum gauge, $B_\triangle$ is continuous and
strictly positive. Thus, for some $\kappa>0$,

$$
B_\triangle(h)\geq\kappa\lVert h\rVert_2.\tag{6}
$$

The triangle Legendre identity, evaluated at a vertex with zero entropy,
gives $Q(e^{h_f}:f\in t)\geq\tfrac12\max_{f\in t}h_f$. Consequently
$F(h)\geq B_\triangle(h)$, and $J\geq F$ is also coercive. Both are
continuous, so both minima are attained. If the gauge has dimension zero,
the same attainment assertion is immediate, and the argument below does
not require (6).

Uniqueness of the minimizer of $F$ can also be seen directly. On each
supported row, the strictly concave triangle entropy has an interior
maximizer at finite positive weights. Its Legendre potential is strictly
convex in directions that are not constant on that row. Connectedness of
the ordinary-face graph therefore makes the sum strictly convex modulo
common scale. The actual complete angles give its critical point $h^*$.

## 3. Equality and strict loss

Since $J\geq F\geq\Phi_D$, the nonstrict condition in (3) makes
$J(h^*)=F(h^*)=\Phi_D$ and proves one direction.

Conversely, suppose $\min J=\Phi_D$ and let $h_0$ attain that minimum.
Then $F(h_0)\leq J(h_0)=\Phi_D$, so uniqueness forces $h_0=h^*$.
Every term $H_e-X_e$ is nonnegative. Their sum can vanish at $h^*$ only
if every positive middle logarithm is at most $X_e$. This proves (3),
and (4) follows immediately. No local optimizers have been chosen
independently and no minimax interchange is used.

## 4. Even level-dependent positive radii cannot remove this loss

For even $N$, let $d=N-1$ and let $P_{e,N}$ be the original full positive
Fejer endpoint polynomial. Define its exact positive Cauchy bound

$$
\operatorname{Cap}_N=
\inf_{L_f>0}
\frac{\left.\prod_eP_{e,N}\right|_{L_u=L_v=0}}
     {\prod_{f\text{ ordinary}}L_f^d}.\tag{7}
$$

The infimum permits arbitrary $N$-dependent radii. The uniform closed
coefficient entropy theorem gives, uniformly on every compact set of
ordinary logarithmic weights,

$$
G_N(h):=\frac1N\log
\frac{\prod_eP_{e,N}(e^h)}{\prod_f e^{dh_f}}
\longrightarrow J(h).\tag{8}
$$

This follows by finite positive Laplace summation: every local coefficient
has its uniform closed entropy, the number of monomials is polynomial
in $N$, and the supported rational grids approximate the compact simplex.
The difference between $d/N$ and one is uniform on compact logarithmic
sets. The exact weighted maximum is $H_e$, with its original normalization.

There is no escaping-minimizer loophole in (8). Each allowed pure-face
monomial has degree $d$ and logarithmic coefficient $o(N)$ uniformly
over the finitely many vertices. Its coefficient entropy is zero. Keeping
one such monomial at each port gives

$$
G_N(h)\geq\frac dN B_{\mathrm{port}}(h)-\varepsilon_N,
\qquad\varepsilon_N\longrightarrow0,\tag{9}
$$

where $B_{\mathrm{port}}(h)=\sum_e\max_{f\in e\text{ ordinary}}h_f-\sum_fh_f$.
The two triangle rows at each port show
$B_{\mathrm{port}}\geq B_\triangle$. Thus (6) and (9), together with the bounded
value $G_N(h^*)$, put all finite-level minimizers in one fixed compact set
for sufficiently large $N$. At each fixed level coercivity also gives
attainment. Compact uniform convergence now proves

$$
\lim_{\substack{N\to\infty\\N\text{ even}}}
\frac1N\log\operatorname{Cap}_N=\min_hJ(h).\tag{10}
$$

Let $Z_N$ denote the actual original marked coefficient of this same
positive product. The [complete endpoint theorem](general_fejer_endpoint_source_volume.md)
gives $N^{-1}\log Z_N\to\Phi_D$. Combining with (10) yields

$$
\lim_{\substack{N\to\infty\\N\text{ even}}}
\frac1N\log\frac{\operatorname{Cap}_N}{Z_N}
=\min J-\Phi_D.\tag{11}
$$

At a strictly unbalanced complete packing this is a positive exponential
loss in the best undivided positive Cauchy bound. It is not a claim of
excess growth in the coefficient, which still has the actual volume rate.
The statement is already decisive along even levels; no odd regularization
is needed for this obstruction.

## 5. Consequence for the general strategy

One cannot repair a strict packing imbalance merely by optimizing a single
positive torus for the full endpoint product, even with radii depending on
the level. The proved [anchored shared-radius theorem](general_anchored_shared_radius_filling_volume.md)
avoids this particular loss by separating genuine source sectors first.
It is not contradicted by (4) or (11). The [finite actual-sector cover theorem](general_actual_sector_cover_filling_volume.md)
retains those common face constraints while permitting finer decompositions.
A [certified original source](actual_shared_radius_certificate_separation.md)
shows that the anchored test itself is not universal, although a finer cover succeeds.

The argument uses finite convex geometry, the original uniform local coefficient theorem and its actual endpoint volume calibration; it does not use a numerical optimizer as a proof.