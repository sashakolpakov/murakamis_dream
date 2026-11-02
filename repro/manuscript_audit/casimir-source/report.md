# Audit of the local bounds and central shared coefficient

I read both complete papers at commit `acd7e7d5bff5641537f0b6dc71684711ac68dda0`: `papers/local-coefficients/main.tex` and `papers/source-asymptotics/main.tex`. I also read the finite Fourier identification and marked coefficient/filling statements that they import, and the hypotheses and conclusion of the oscillatory filling theorem to which the second paper exports its result. `sources.json` records exact hashes and proof locators; `snapshot/` contains those sources.

**Result:** I found no proved defect or unresolved implication in the two main arguments under their printed hypotheses. This is a mathematical reading, with limited supplementary calculations. It is not a formal verification of the analytic proofs, an audit of every proof in the imported papers, or a proof of a knot-volume result. In particular, a stationary positive radius vector is an explicit hypothesis of the shared-coefficient paper.

The present record concerns those two historical source files. The later consolidation into a single paper is checked separately by the root reviewer against the saved proof diffs and label migration. This audit does not substitute a hash comparison for that consolidation review.

## What the first paper establishes

Its object is the degree-$d$ polynomial numerator of the actual finite Casimir resolvent, with the homogeneous face variables kept independent. Here and below the degree is $d=N-1$. The main theorem is an exponential upper bound for each of its three path sectors, uniformly over the whole real spectral interval and every face phase. It permits fixed zero faces but requires $x+y>0$. The proof of the one-sided bounds does **not** assert coefficientwise domination by the complete polynomial.

The following steps withstand the checks I made.

1. **The exact polynomial and both parities.** The adjugate identity has the sign $(-1)^d$ dictated by $\sigma=-2-u$. The path factors are exactly the unvisited diagonal rows. The even cut has three crossing types; the odd cut has both paths visiting the middle row and paths skipping it. The latter contribute $u s_m^2xyD_bD_c$. This term vanishes at $u=0$, but its first $u$ derivative does not. It is retained before estimates or differentiation.
2. **The central comparison.** For the individual cofactors, spectral degree is at most $J=\lfloor (N-1)/2\rfloor$. Thus the discrete Fourier interpolation uses strictly fewer than $N$ differences of retained modes; it has no hidden Nyquist collision. Its $O(\log N)$ bound applies to these cofactors, not to the entire degree-$d$ numerator. At nodes after the forcing has stopped, positivity is proved for the continuant itself using $0\leq\gamma_r\leq1$; it is not inferred by taking absolute values of its signed recurrence. The central factorization then controls the odd skipping term as well.
3. **The signed transfer estimate.** The positive quantity $\rho_\delta(t)$ is the spectral radius of the limiting real two-by-two matrix. The proof uses the bound on powers of that matrix followed by fixed-length blocks. It does not substitute one eigenbranch for the spectral radius of a varying product. After an initial interval is removed, Cayley--Hamilton gives a uniform bound even at a repeated eigenvalue. The initial interval and the sine factors have integrable logarithmic costs. The order of choices $\eta$, block length, then $N$, is sufficient for an all-level upper estimate.
4. **Unused rows.** The upper Riemann estimate truncates logarithms from below. A sampled zero therefore strengthens the estimate instead of invalidating it. The two original unused products are bounded before the complete-prefix integral is cancelled. This avoids division by a vanishing spectral factor.
5. **The continuum maximum.** The calibrated action agrees with the triangle entropy including its additive constant. Its spectral derivative has the required sign. In the one-sided optimization, the post-change stationary branch has derivative sign $\operatorname{sign}((c-b)\sin^2(\pi\delta)-A)$, so it cannot furnish an interior spectral maximum. The exceptional $xy=0$, $b=0$, and symmetric final-endpoint cases are treated by their exact one-step/sole-start formulas and continuous values. The maximum is an upper-envelope statement; it is not represented as a lower bound for the oscillatory finite polynomial.
6. **Arbitrary phases and the last interval.** The identity $1+\beta_j\geq0$ proves coefficient positivity of interval tails only up to the stated spectral cap. The remaining cap is covered by polynomial exterior growth. Its transformed endpoint is $1+O(N^{-2})$, so degree $N-1$ costs a bounded factor. Complex coefficients and the order of the face-phase supremum are respected.

The final shared-radius application uses a fixed finite number of boxes and common radii for genuinely shared variables. The resulting sum of local rates is a Cauchy upper bound. The paper correctly leaves the strict global gap, a surviving leading term, and geometric volume identification to other arguments.

## The local complex asymptotic in the second paper

The positive stationary radii are assumed in equation `sa:stationarity`; the text does not derive them merely from the existence of a spherical triangulation. All local complex neighborhoods are taken with a fixed zero pattern and compact positive nonzero entries.

For a positive middle variable, the starting-row saddle is strictly interior. On its retained interval the dominant root is a unit and the other-root ratio is bounded strictly below one. The analytic Riccati construction includes its shift of domains and a separate rectangle for the residual. Its exponentially small residual feeds into a geometric difference recurrence for the actual initial-value solution. This supplies the coefficient $a_N$, rather than assuming a nonzero saddle amplitude.

The two products in the starting-row formula have analytic logarithms on the intervals where Euler--Maclaurin is used: the prefix ends before its possible spectral zero, and the tail begins away from the initial sine zero. The displayed remainder bound follows from the periodic Bernoulli remainder and Cauchy derivative estimates on a fixed smaller strip. Taking the truncation length proportional to $N$, with a sufficiently small proportionality constant, gives an exponential remainder. The actual terminal row and endpoint half-terms remain in the finite phase. The external formula checked here was [DLMF 2.10.1](https://dlmf.nist.gov/2.10.E1); that formula supplies the summation remainder, not the source-specific zero exclusion or contour argument.

The omitted starting rows have a fixed real action loss. For a small complex spectral perturbation, the comparison with $a_j+|u|$ only costs $e^{N\omega(|u|)+O(\log N)}$; near-zero diagonal rows are separated before this bound is used. Homogeneous face degree controls a small logarithmic face perturbation. Those costs can be chosen smaller than the starting-row loss.

The cotangent contour has its vertical sides on half-grid lines, where the cotangent has modulus at most one. On fixed horizontal lines its error from the limiting constants is exponentially small. At the real reference the horizontal phase cost is quadratic in the height. Choosing the height before the complex parameter neighborhood therefore gives a genuine contributing integral and a relative Gaussian estimate. This is the substantive discrete-to-integral step; positivity of a real saddle alone would not replace it.

When the middle variable is zero, the proof does not reuse the interior saddle. Its normalized two-mode system begins with ratio $-1$, but the eigenvalues are distinct and $1-r$ stays nonzero. Removing the $O(N^{-1})$ off-diagonal coupling leaves $O(N^{-2})$ errors and bounded partial products; the accumulated error is $O(N^{-1})$. The negative mode decays over a terminal interval of positive macroscopic length. The initial eigenbasis coefficients are explicitly $1/g(0)$ and $-1/g(0)$. If one outer variable also vanishes, the exact monomer product is used instead. Thus the protected case is not lost at an endpoint of the interior argument.

The terminal ratio gives the stated even and odd central units. The odd unit contains the skipped-row contribution. Both are nonzero near the complete point. Consequently the local logarithm is taken from the actual polynomial on a fixed zero-free neighborhood. It is not obtained by differentiating an approximate interpolation at physical nodes.

## The two global complement estimates

I checked these separately, since either one would be a serious missing step if only the local Hessian had been established.

### Face phases away from the common phase

The determinant contraction inequality is valid without commutativity: the normalized positive matrices sum to the identity, and the trace defect is the sum of pair traces weighted by squared phase differences. With positive middle entry, disjoint interior Cholesky vectors give order-$N$ pair traces. For zero middle entry, the exact binary coefficient formula supplies a log-radius variance of order $N$, which equals the needed pair trace. A monomial triangle is explicitly exempt.

The cofactor argument treats both groups of physical nodes. Near-fold nodes inherit the triangle phase loss. At far nodes with $xy>0$, independent dimer replacements give an exponential advantage over the monomer product. With $xy=0$ and positive middle entry, either the unused-prefix factors give a loss or a short start lies below a later positive start by an exponential factor. For cofactors of degree $J-k$, the absent top nodes are supplied by multiplication with the missing fixed number of factors. Removing those factors costs a polynomial, as shown by a small interval next to a maximum. A fixed thin spectral strip is then obtained from polynomial growth, not from a claim about complex positivity.

Deleting the two marked vertices from the spherical triangulation leaves its ordinary graph connected. The triangle differences contain a spanning tree of that graph and span the primitive sum-zero integer lattice. This is enough both for a unique common-phase class and for the measure factor one after quotienting by common phase. Each term of the exact central factorization contains a terminal cofactor from each triangle. The global loss therefore applies to every term at the same shared radii, not to a chosen favorable term.

### Spectral variables away from the complete point

For every nonmonomial triangle, the local real cofactor rate has a strict loss away from zero: the action decreases, and the constant endpoint branch is strictly below the complete entropy. The local fixed-block proof permits a sufficiently small complex face perturbation chosen **after** the block length. On the nearby face-phase region this gives the spectral loss. On its complement the preceding global angular loss applies. Both regions use the original common radius vector and the same Cauchy target factor.

The final fixed complex spectral strip follows from the product Poisson inequality for the actual Laurent polynomial. Its separate degree is at most $N-1$, so the cost is $2\pi(N-1)\sum_e |y_e|$. The Poisson mass of the separated real region tends uniformly to one as the strip shrinks. This upgrades the real shared-coefficient gap to the stated complex-strip gap without requiring local factor estimates throughout that strip.

## The finite Gaussian, normal derivatives, and parity

I independently differentiated the entropy loads and obtained all nine entries of the stated three-variable graph Hessian. The common ordinary graph makes the grounded sum positive definite. The finite saddle is built from the exact local logarithms, with the exact target $d/N$, and its implicit-function argument uses this limiting Hessian. The primitive torus measure is $(2\pi)^{-(R-1)}d\vartheta$. Thus the Gaussian denominator is $(2\pi N)^{(R-1)/2}\sqrt{\det H_N}$, as stated.

The action $A_N$ retains all finite normalization terms; convergence to $A_0$ is never used to replace $e^{NA_N}$ by $e^{NA_0}$ in a relative formula. Separate evenness eliminates the mixed face/spectral derivatives at zero. Differentiating the calibrated action gives the printed diagonal $-2\kappa_e$, including protected monomial triangles, whose individual contribution is zero.

The proof treats the two parity factorizations explicitly. The maximal-fold anchor is at zero for odd $N$ and $1/(2N)$ for even $N$; the finite phase retains this difference. The interpolation grids, sine denominators and transfer estimates use only integer $N$ and indices below $N$, not primality. Fixed derivative assertions follow on smaller complex neighborhoods by Cauchy's formula. They are not claims of uniform control for derivative order growing with $N$.

## Imported hypotheses and the exact scope of the export

The finite Fourier proposition uses the same $q=e^{\pi i/N}$, the same residue block, evaluation matrix and diagonal gauge. With the convention $\mathsf C=-T$, its displayed conjugacy is exactly the one used here. Its Cayley--Hamilton argument proves the full annihilator, including nilpotent parts. The homogeneous adapter keeps the factor $N^{-1}$ and the canonical integer shift. The diagram theorem extracts the ordinary targets $d$, with both marked faces set to zero and its cups, caps and mark accounted for. The central path selection is then an algebraic contribution to that full shared polynomial; it need not itself be a separate polynomial functional of the physical Casimir.

The oscillatory theorem requires separate spectral degree at most $N-1$, an entire even periodic source, a fixed holomorphic local packet with nonzero limiting amplitude, separately even real finite actions, a negative diagonal limiting spectral Hessian, and the shared complex-strip gap. The present theorem supplies each of these for its raw central coefficient. Substituting its amplitude and exponent into the oscillatory formula gives the stated $N^{R+1/2}\sqrt{2\pi}$ factor. Its two level-parity signs multiply to one. The independently signed twists remain fixed before $N$ tends to infinity.

This checks the interface to that imported theorem, not the entire proof of its infinite-charge estimate. Nor do these two papers prove existence of the stationary radii, control of the noncentral part of the invariant, a topological realization of an arbitrary analytic datum, or an action-volume equality. Those are ordinary retained assumptions or separate written arguments, not defects in the conditional central theorem.

## Supplementary checks and merger instructions

`local-exact-check.json` reproduces the supplied exact polynomial checks at $N=3,4,5,6$. `source-exact-check.json` reproduces the exact determinant, protected binary, pivot and parity-anchor checks at $N=3,\ldots,8$. These check bounded finite identities only.

`counterchecks.py` independently checks the generic entropy Hessian symbolically, samples the continuum envelope for six weight choices including protected zeros, and computes first $u$-derivatives of the actual finite cofactor recurrence before converting them to the second spectral derivative. The latter diagnostic includes both parities and a protected constant triangle. Numerical quadrature and convergence samples are explicitly excluded as proofs of uniformity, zero exclusion, complement gaps or a volume theorem.

For the merger, preserve the proof distinctions listed above. In particular, do not shorten the global angular proof to Hessian positivity, omit the protected initial-mode argument, replace the one-sided value bound by coefficientwise domination, or absorb finite $A_N$ into its limit. No theorem restriction or corrective proof patch is recommended by this audit.
