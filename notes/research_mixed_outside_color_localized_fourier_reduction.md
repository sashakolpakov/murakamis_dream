# Localized Fourier reconstruction and the missing outside-color energy

Research deduction, 6 November 2026. No numerical evaluation is used.

There is an exact positive-energy formulation of a sufficient real
outside-color estimate for the mixed open source. It uses an explicitly
localized reproducing kernel and a linearly oversampled angular grid.
The energy premise is not proved here and is not asserted to be weaker
than the original exponential gap. The physical integer-color grid at
the same quantum level has no room for the required localization.

## 1. The source and its missing estimate

For a fixed positive word \(\mathbf n\in\{3,4\}^m\), retain the
literal source
\[
 Z_{\mathbf n,N}(w_L,w_R)
   =v(w_L)^T A_{n_1}\cdots A_{n_m}v(w_R),\qquad A_n=JM^n,
 \quad Q_N(\boldsymbol\theta)
   =Z_{\mathbf n,N}(-2\cos\theta_L,-2\cos\theta_R).
 \tag{1}
\]
The ordinary degree in either color is at most \(N-1\), hence its
separate angular Fourier degrees are at most \(D=N-1\). This is an
identity for the whole finite polynomial, including the original normal
directions, not an identification with its plateau sector. See the
[exact contraction](research_mixed_wire_exact_contraction.md), Section 3,
and the [stability reduction](research_mixed_open_source_stability_reduction.md),
Section 2.

With \(M_*=\Re\mathcal W_{\mathbf n}(-2,-2)\), the missing real
estimate is, for a sufficiently small fixed \(\rho>0\),
\[
 \sup_{\|\mathbf x\|_{\mathbb T,\infty}\ge\rho}|Q_N(\mathbf x)|
       \le C N^A e^{N(M_*-\delta)},\qquad \delta>0.
 \tag{2}
\]
Here the torus distance to zero is used in each coordinate. A larger
absolute-partition or operator-norm rate cannot replace \(M_*\).
The [central-region theorem](research_mixed_central_region_boundary_colors.md)
already proves this kind of estimate for its specified polynomial
sector; its equation (13) isolates the remaining whole-source
complement. The homogeneous
[outside-boundary theorem](research_three_chain_outside_boundary_decay.md)
obtains (2) by carrying an endpoint deficit through every original
contour and complementary term, not by positivity of arbitrary word
coefficients.

## 2. An exact exponentially localized reproducer

Let \(P\) be any trigonometric polynomial of separate degree at most
\(D\) in \(r\) variables. Its coefficients may be arbitrary complex
numbers. For an integer \(k\ge0\), define
\[
 \mathscr D_\ell(t)=\sum_{n=-\ell}^{\ell}e^{int},\qquad
 K_{D,k}(t)=\mathscr D_{D+k}(t)\cos^{2k}(t/2).
 \tag{3}
\]
The binomial expansion is
\[
 \cos^{2k}(t/2)=\sum_{j=-k}^k c_j e^{ijt},\qquad
 c_j=4^{-k}\binom{2k}{k+j}\ge0,\qquad\sum_jc_j=1.
 \tag{4}
\]
Consequently \(\widehat K_{D,k}(n)=1\) for \(|n|\le D\),
and it vanishes for \(|n|>D+2k\). Positivity in (4) belongs to
this elementary auxiliary kernel; it is not an assumption about \(P\).

Choose an integer number of grid points \(L>2D+2k\), and put
\(\theta_j=2\pi j/L\). Exact character orthogonality gives
\[
 P(\mathbf x)=\frac1{L^r}
  \sum_{\mathbf j\in\{0,\ldots,L-1\}^r}
   P(\boldsymbol\theta_{\mathbf j})
       \prod_{a=1}^rK_{D,k}(x_a-\theta_{j_a}).
 \tag{5}
\]
Indeed, in one coordinate the frequency difference in this discrete
convolution has absolute value at most \(D+(D+2k)<L\).
Only the zero difference survives, and its multiplier is one.
Apply this argument separately in every coordinate.

Write \(d_{\mathbb T}(t,0)\in[0,\pi]\) for circular distance.
Since \(\tan u\ge u\) on \([0,\pi/2)\), integration gives
\(\log\cos u\le-u^2/2\). Thus
\[
 |K_{D,k}(t)|\le(2D+2k+1)
       \exp\{-k\,d_{\mathbb T}(t,0)^2/4\}.
 \tag{6}
\]
The endpoint where the cosine vanishes follows by continuity. For
\(k=0\), (6) is the ordinary Dirichlet bound without a decay factor.

## 3. The resulting positive-energy criterion

Fix \(0<\rho<\pi\), and define the actual sampled energies
\[
 \begin{split}
 E_{\rm all}&=L^{-r}\sum_{\mathbf j}
                         |P(\boldsymbol\theta_{\mathbf j})|^2,\\
 E_{\rm out}(\rho/2)&=L^{-r}
    \sum_{\|\boldsymbol\theta_{\mathbf j}\|_{\mathbb T,\infty}
                  \ge\rho/2}|P(\boldsymbol\theta_{\mathbf j})|^2.
 \end{split}
 \tag{7}
\]
Both are nonnegative observations of the original polynomial.
Since \(L>2D\), the first is also its exact continuous Fourier
energy, \(E_{\rm all}=\sum_{\mathbf n}|\widehat P(\mathbf n)|^2\).
The second retains its prescribed exterior window and all interference
already present in each source value.

**Lemma.** Under the grid condition in Section 2,
\[
 \boxed{\quad
 \sup_{\|\mathbf x\|_{\mathbb T,\infty}\ge\rho}|P(\mathbf x)|
 \le (2D+2k+1)^r
     \left(\sqrt{E_{\rm out}(\rho/2)}
           +e^{-k\rho^2/16}\sqrt{E_{\rm all}}\right).
 \quad}
 \tag{8}
\]
*Proof.* Split (5) into the exterior grid window and its complement.
Cauchy--Schwarz with normalized counting measure bounds the first
part by \((2D+2k+1)^r\sqrt{E_{\rm out}}\). For the other part,
some coordinate of \(\mathbf x\) has distance at least \(\rho\)
from zero, while every grid coordinate in that part has distance less
than \(\rho/2\). The circular triangle inequality gives separation
at least \(\rho/2\) in that coordinate. Equation (6), followed by
the same Cauchy--Schwarz inequality, bounds that part by the second
term of (8). No coefficient sign or source phase is removed.
\(\square\)

In particular suppose \(D\le dN\), and, at the chosen grid,
\[
 E_{{\rm all},N}\le C N^A e^{2NB},\qquad
 E_{{\rm out},N}(\rho/2)\le C N^A e^{2N(M_*-\delta)}.
 \tag{9}
\]
Choose a fixed \(c>0\) such that
\(c\rho^2/16>B-M_*+\delta\), set \(k=\lceil cN\rceil\),
and choose \(L>2D+2k\) with \(L=O(N)\). Equation (8) proves
(2), with a changed polynomial prefactor. Thus a calibrated positive
**exterior** energy bound is a sufficient finite-dimensional target.
A bound for the total energy alone does not supply it. Conversely,
a pointwise gap on the larger exterior region immediately bounds its
sampled energy. This is a reformulation with an angular collar, not a
claim that (9) is an easier or already established exponential estimate.

For the literal open word, the samples in (7) are exactly the values
of the matrix product in (1). If \(V_{j,a}=v_a(-2\cos\theta_j)\)
and \(T=A_{n_1}\cdots A_{n_m}\), their array is \(VT V^T\).
Thus \(E_{\rm out}\) is an explicit positive quadratic observation
of this unchanged product. Replacing \(T\) by an absolute-entry
majorant, a reflected word or its top singular vector changes that
observation and does not prove (9).

The coarse total-energy hypothesis in (9) does have an elementary
bound for every fixed word. Put \(p=\sum_v n_v\). In the exact
crossing formula of the positive-cycle theorem and the
[original Newton formula](research_all_color_path_normal_bound.md),
equation (1), write
\(S_j=\prod_{r=1}^j2\sin(\pi r/N)\). For \(j\le N/2\),
\[
 S_j\ge (4/N)^j j!\ge (4j/(eN))^j\ge e^{-N/4}.
\]
The last inequality minimizes \(x\log(4x/(eN))\) at \(x=N/4\);
\(j=0\) is immediate. For \(j>N/2\), reflection gives
\(S_j=N/S_{N-1-j}\ge N2^{-N/2}>e^{-N/2}\).
Thus \(S_j\ge e^{-N/2}\) throughout. The exact crossing entries
obey \(|M_{jk}|\le 2^N e^N\), while each real-color Newton
polynomial obeys \(|e_j(w)|\le4^N e^N\), \(-2\le w\le2\).
The Euclidean matrix/vector norms therefore give
\[
 \sup_{\mathbf x}|Q_N(\mathbf x)|
 \le N^{p+1}e^{NB},\qquad
 B=2(1+\log4)+p(1+\log2).
 \tag{10}
\]
Here reversal has norm one, and all \(p\) crossing factors remain.
Consequently \(E_{{\rm all},N}\le N^{2p+2}e^{2NB}\).
This crude bound suffices to choose a finite oversampling constant
in (9). It has no geometric calibration and gives no exterior loss.
The second inequality in (9) is still the unproved literal-source
premise.

## 4. Why the physical integer-color lattice does not supply (9)

The level-\(N\) integer-color angular spacing is \(\pi/N\),
giving at most a \(2N\)-point full-circle lattice (up to the fixed
shift or reflection used by a convention). For the available degree
\(D=N-1\), setting \(L=2N\) in (5) requires
\[
          2N>2(N-1)+2k,\qquad\text{hence }k<1.
 \tag{11}
\]
There is no positive integer \(k\) satisfying this condition, much
less \(k\) proportional to \(N\). For this reproducer the failure
is actual aliasing, not just an unused sufficient condition. At
\(k\ge1\), its coefficient at \(n=N+1\) is positive: the
\(j=k\) term of (4) contributes because
\(|N+1-k|\le N-1+k\). On the unshifted \(2N\)-point grid,
the admissible even polynomial \(P(t)=\cos((N-1)t)\) therefore
produces a nonzero reconstructed coefficient at \(N+1\), through
the alias from its frequency \(-(N-1)\). The true polynomial has
no such coefficient. A fixed grid shift multiplies this alias by
a unit scalar and does not remove it.

The proved [ordinary-color bound](ordinary_color_plancherel_bound_audit.md),
Sections 3--4, concerns the original reduced colors \(1\le j<N\)
of one fixed one-component closed knot at the same quantum root.
It gives an exact energy decomposition
\(E_N^{\rm knot}=|K_N|^2+R_N\) with polynomial \(R_N\).
That energy is not (7) for an arbitrary two-boundary open word.
Nor does the theorem bound the new noninteger colors required by
\(L>2D+2\lceil cN\rceil\) at the same level \(N\).
Changing the level to make a denser lattice physical also changes
the crossing matrices and the polynomial, so it is not an application
of (5) to the original source.

Degree and a local geometric packet cannot fill this gap. The explicit
all-level polynomial construction in
[Fourier lower bounds, Section 9](research_fourier_lower_bounds_and_almost_invariance.md)
has degree below \(N\), a nonzero holomorphic packet with strictly
negative local angular curvature, and a small Newton coefficient norm,
yet a remote real value has a strictly larger exponential rate.
It can even use cyclotomic coefficients. It is not a counterexample
for a fixed tangle; it proves that those analytic/algebraic hypotheses
alone allow exponential remote spikes.

Finally, positive transfer and almost-invariance do not presently
supply the missing exterior energy. The exact homogeneous conjugacy
becomes \(H M^{n_1-3}\cdots H M^{n_m-3}\) for mixed words, where
\(H=M^*M\); the inserted \(M\)'s are not positive or unitary
([positive-cycle theorem](research_positive_three_crossing_cycle.md),
equation (6)). The full crossing has nontrivial unit-circle Jordan
blocks, and geometric quasimodes can have exponentially small original
cap observations
([original observation theorem](research_original_almost_invariance_and_observation.md)).
The established weighted interior transfer norm is an upper estimate
on its specified domain and retains an unestimated boundary conversion
cost ([weighted transfer](research_mixed_nonlow_weighted_transfer.md),
Section 4). None proves (9) at the calibrated \(M_*\).

The Fourier idea therefore has a precise positive observable and an
exact localization mechanism. What remains is new information about
that literal exterior source energy, or complete contour estimates
that prove (2) directly. No mixed whole-source gap, short-filling
stability theorem or finite-exception conclusion follows from this
note alone.
