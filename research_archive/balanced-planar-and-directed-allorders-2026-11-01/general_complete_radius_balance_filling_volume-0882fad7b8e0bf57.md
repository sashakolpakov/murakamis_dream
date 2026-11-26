# Full original long-filling volume under the actual complete-radius balance test

The subsequent [planar decoration theorem](actual_balanced_terminal_fan_volume.md) constructs balanced diagrams from every simple triangulated sphere with a chosen dual matching. It includes the full general Morse source and independently long fillings. The theorem below retains its own original scope.

conditional-class theorem, 31 October 2026. The condition below is imposed on the one actual complete marked circle packing. Its realization at arbitrary bridge width is not asserted. The proof controls the full original numerator and period for diagrams satisfying this condition, rather than only an all-CROSS contribution.

## 1. The finite geometric condition

Fix an original certified marked flat plat $D$, with its simple labeled white sphere and actual complete positive ordinary face curvatures. Retain the original two marked curvatures exactly zero. At each port write its actual ordered quartet as $(x,b,c,y)$, with $A=x+y>0$, and put

$$
X_e=Q_b(0)+Q_c(0).
$$

The normalization of $Q$ is the original determinant, beta and half-forced-product normalization, as proved in the [cofactor action theorem](actual_cross_cofactor_marked_action.md). Assume the following strict balance condition at every port:

$$
X_e>\log b\quad\text{whenever }b>0,\qquad
X_e>\log c\quad\text{whenever }c>0.\tag{1}
$$

No logarithm of a protected zero is required. This is a finite test on one shared complete packing, invariant under its common positive scale. It does not optimize a separate radius vector for each port.

For every positive middle $t$ and $A>0$,

$$
Q_t(0)>\frac12\log t.\tag{2}
$$

Indeed, the actual zero-spectral start action has a strict interior maximum, larger than its terminal-start value $\tfrac12\log t$. This continues to either single-outer-zero case by its exact first-order formula. The only monomial case is $t=0$ and $xy=0$; (2) is not applied there.

## 2. Every sector containing a one-sided port has a global spectral gap

The [exact path partition](actual_cross_cofactor_factorization.md) is disjoint at both parities. For $N=2m$, LEFT has $j\leq m-1$, CROSS has $i\leq m-1$ and $j\geq m$, and RIGHT has $i\geq m$. For $N=2m+1$, LEFT has $j\leq m-1$, CROSS has $i\leq m\leq j$, and RIGHT has $i\geq m+1$. The odd central zero-step path belongs to CROSS exactly once.

At a fixed port, the [global weighted LEFT theorem](actual_global_left_weighted_spectral_envelope.md) bounds the actual absolute value, at arbitrary face phases and every real spectral value, by the rate

$$
L_e=\max\left\{\log c,Q_b(0)+\frac12\log c\right\},\qquad c>0.\tag{3}
$$

If $c=0$, the finite LEFT polynomial vanishes identically because its $c$ exponent is at least $\lfloor N/2\rfloor>0$. Similarly, the RIGHT rate is

$$
R_e=\max\left\{\log b,Q_c(0)+\frac12\log b\right\},\qquad b>0,\tag{4}
$$

and the RIGHT polynomial vanishes exactly when $b=0$. Equations (1)–(2) give $L_e<X_e$ and $R_e<X_e$ whenever the corresponding sector survives. This also resolves the protected monomial exception: if one triangle has $t=0$ and $xy=0$, the sector overloading that zero middle is absent, while the opposite surviving sector uses (2) for its positive middle. If both middles vanish, both one-sided sectors vanish exactly.

The [global CROSS coefficient comparison](actual_cross_cofactor_factorization.md), Section 8, bounds its value on the same face torus by rate $X_e$, with only a polynomial or logarithmic prefactor. Thus the whole local full numerator is bounded by rate $X_e$, and any chosen LEFT or RIGHT factor supplies a fixed strict loss. Since $D$ is fixed, the minimum of its finitely many surviving one-sided gaps is positive. If none survives, the remainder is identically zero and the subsequent conclusion is immediate.

Take any original path sector with at least one one-sided port and CROSS, LEFT or RIGHT assigned elsewhere. The value bounds are uniform over the original common face Cauchy torus. The same marked target extraction therefore gives, for some $\gamma>0$ and all sufficiently large $N$,

$$
|Z_{\mathrm{sector}}(\sigma_1,\ldots,\sigma_R)|
\leq e^{N(\Phi_D-\gamma)},\tag{5}
$$

uniformly on the entire real spectral cube $[-2,2]^R$, at both parities. Here $\sum_eX_e$ minus the original ordinary log-radius targets is exactly $\Phi_D=\operatorname{Vol}(Y_D)/(2\pi)$, by the calibrated complete source. The protected variables stay zero throughout. No infimum of a sum of local maxima or independent-radius capacity equality is used.

There are only $3^R-1$ such sectors. Their sum is exactly the full shared numerator minus its all-CROSS part. Thus (5) also holds for that remainder, after reducing $\gamma$. It is a polynomial of spectral degree at most $d$ in each variable. Multivariate cosine Bernstein extends (5) to a sufficiently thin fixed complex $\delta$ strip, at cost $\exp[2\pi d\sum_i|\operatorname{Im}\delta_i|]$. Reducing the strip height and $\gamma$ gives the same strict gap there.

## 3. Entire original Fourier remainder and the full invariant

Apply the [whole-domain three-integration-by-parts lemma](actual_global_diagonal_spectral_sector_gap.md), Section 4, to the remainder polynomial. The original sine factors vanish at both endpoints, first derivatives match, and the second-derivative endpoint current is retained. Source derivatives use the fixed strip; Gaussian derivatives are taken only on the real cube. Summing all nonzero original charges with their actual weights and parity gives

$$
|I_{\mathrm{full}}-I_{\mathrm{cross}}|
\leq C_D\prod_i(1+|n_i|)^3e^{N(\Phi_D-\gamma')},\tag{6}
$$

for a fixed $\gamma'>0$. No infinite sharp-cube charge series is split. All framing and component scalars remain the original ones.

The [entire all-CROSS period theorem](general_all_cross_long_filling_volume.md) supplies a nonzero relative filling asymptotic for every fixed independently signed sufficiently long integer vector $n_i=\epsilon_i-2p_i$. Its unit critical rate tends to $\Phi_D$ as $\min_i|n_i|$ tends to infinity, with loss $O_D(\sum_i n_i^{-2})$. Choose a diagram-dependent threshold so this loss is less than $\gamma'/2$ and all existing geometric and analytic filling thresholds hold. Then (6) is exponentially smaller than the complete all-CROSS asymptotic. Thus

$$
\frac{I_{\mathrm{full}}}{I_{\mathrm{cross}}}
=1+O_{\mathbf n}(e^{-c_{\mathbf n}N}),\tag{7}
$$

and

$$
\lim_{N\to\infty}\frac{2\pi}{N}\log|I_{\mathrm{full}}|
=\operatorname{Vol}(\text{the actual smooth filled exterior}).\tag{8}
$$

The same conclusion holds after multiplying by the separately recorded original normalization characters and nonzero polynomial-level factors. For the prescribed parity yielding a knot, this is the corresponding full original knot invariant, not a chosen spectral contribution. It does not assert that a given $2k$-plat has minimal bridge number $k$.

The quantifiers are: for each fixed certified $D$ satisfying (1), there exists $T(D)$ such that every independently signed fixed filling vector with all $|p_i|\geq T(D)$, in the prescribed parity convention, has (7)–(8) as $N\to\infty$. No bound on ratios $|p_i|/|p_j|$ is needed. There is no joint growing-twist/level estimate or uniform threshold over different diagrams or widths.

## 4. An algebraic certificate and its coverage limit

The [source-normalized triangle entropy lemma](actual_triangle_entropy_algebraic_balance.md) gives a finite algebraic sufficient test for (1): at every port require

$$
(A+b)(A+c)\geq\max(b^2,c^2),\qquad A=x+y>0.\tag{9}
$$

Indeed, $Q_t(0)\geq\tfrac12\log(A+t)$, strictly whenever at least two triangle weights are positive. If either middle is positive, its triangle has that strictness, so even equality in (9) implies strict balance. If both middles vanish, the condition is vacuous and both one-sided sectors vanish. The simpler $|b-c|\leq A$ implies (9) and is also sufficient. All tests use the same actual complete marked packing.

Realization of this condition for arbitrary $k$ is not proved here. Neither a condition on free local weights nor a comparability criterion alone establishes such a family of actual labeled diagrams. Nothing here asserts that every certified simple-white plat satisfies (1). When it fails, the weighted local full maximum can exceed the cross value at these particular radii, and the general shared forest and phase problem remains. No obstruction to the volume conjecture or to a weaker optimized certificate follows from that failure.

## Validation and scope

The proof uses only the linked source theorems and the explicit balance hypothesis. Its conditional full-invariant conclusion does not establish arbitrary-width coverage or a universal balance condition.