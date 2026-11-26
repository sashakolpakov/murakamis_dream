# The spectral rate of every fixed positive three/four word

Research theorem, 7 November 2026. The complete cyclic source bounds
give an upper estimate uniform in the number of repetitions of a
fixed word. Consequently its original finite matrix has spectral
radius at the calibrated geometric exponential rate. This proof
uses local finite-source bounds and the pointwise cyclic occupation
inequality, not a uniformity assertion about fixed-word Gaussian
asymptotics. No new numerical calculation is needed.

## 1. Original matrices, action and repeated reference

Fix a nonempty word \(w=(n_1,\ldots,n_\ell)\) with
\(n_j\in\{3,4\}\), and let \(k\) be its number of fours. Put
\[
 W_N=A_{n_1,N}\cdots A_{n_\ell,N},\qquad A_{n,N}=J_NM_N^n.
 \tag{1}
\]
These are the original matrices, with no corner deletion, change
of diagonal weights or scalar renormalization. Let \(F_w\) be
their original cyclic critical action and \(M_w=\Re F_w\).
The action, logarithmic lift and unit scalar \(\kappa_N\) are
those of [the complete cyclic theorem](research_mixed_full_cyclic_period.md).

The actual critical reference for \(w^r\), for every integer
\(r\ge1\), is exactly the \(r\)-fold repetition of that for \(w\).
Indeed the repeated coordinates solve every original lifted local
critical equation. The
[cyclic injectivity and existence theorem](research_mixed_cyclic_critical_localization.md)
identifies this solution with the original reference of \(w^r\).
The absolute action constant also repeats, so
\[
                    F_{w^r}=rF_w,\qquad M_{w^r}=rM_w.
 \tag{2}
\]
This includes primitive periods one and two with their literal
repeated incidences. No independence of repeated target variables
is lost: only the reference is periodic.

## 2. A finite-source bound uniform in the repetition count

Fix the original periodic hybrid collar at \(\rho=1/1000\).
For the repeated word use all original selected Laurent terms
and their exact hybrid graphs. Their identity and normalization
are equations (2)--(3) of
[the original cyclic source](research_mixed_local_outer_contribution.md):
\[
 \operatorname{tr}(W_N^r)
 =\sum_{S\subseteq E_4(w^r)}
       \int_{[0,1]^{r\ell}}
       f_{S,N}(z_S(x))\det(I+iD\mathcal H_S(x))\,dx .
 \tag{3}
\]
There are exactly \(2^{rk}\) selections. The outside scalar is
\(\kappa_N^{r(\ell+k)}N^{r(\ell+k)}\). The graph is applied
to the entire original Laurent integrand, so (3) has no discarded
seam or joining currents.

Here is the required local uniformity statement. For every
\(\tau>0\), there are \(C_\tau\ge1\), \(b_\tau\ge0\), and
\(N_\tau\), independent of \(r\), such that each allocated finite
edge modulus is bounded by
\[
                 C_\tau N^{b_\tau}e^{N(e_j+\tau)}
                      \qquad(N\ge N_\tau).
 \tag{4}
\]
The constants may depend on the fixed word and collar; no
dependence on a repeated length is permitted in (4).
The rate \(e_j\) is exactly the seam-priority, raw-right or
coherent allocated envelope used in
[full-period occupation](research_mixed_full_period_occupation.md).

To specify the allocation without any analytic square-root choice,
write \(\epsilon_j=n_j-3\), \(X_j=e^{-2\pi iz_j}\), and
\(\sigma_j=\boldsymbol1_{\{j\in S\}}\). Define nonnegative
finite weights
\[
 D_{j,N}=|d_N(X_j)|^{\epsilon_j}
                       e^{-2\pi N\sigma_j\Im z_j},\qquad
 \mathfrak a_{j,N}
   =|C_{\epsilon_j,N}(X_{j-1},X_j)|
                            \sqrt{D_{j-1,N}D_{j,N}}.
 \tag{5}
\]
Their product restores every actual Fourier polynomial and selected
monomial once. Thus
\[
 |f_{S,N}(z)|=
       N^{r(\ell+k)}\prod_{j=1}^{r\ell}\mathfrak a_{j,N}(z).
 \tag{6}
\]
Zeros are allowed in (5); no inverse of a possibly zero finite
Fourier factor is introduced.

For completeness, (4) follows from the existing local sources,
before their fixed-word total tolerances are chosen:

* On an edge with no seam or raw-right endpoint, the completed
  conditional packets apply on the finite union of compact
  cap, plateau and right-transition products. The
  [full nonlow source assembly](research_mixed_full_nonlow_half_region.md),
  Section 1, specifies this union, including
  [the left/right interfaces](research_mixed_left_right_interface_source.md).
  Deep-low nonseam targets have height zero and lie in the compact
  square \([\rho,1/2]^2\); they use the
  [closed half-endpoint packet](research_mixed_half_endpoint_conditional_packet.md),
  Theorem 2. Their Fourier factors have the arbitrary-tolerance
  absolute bound in
  [Fourier continuation](research_mixed_fourier_weight_continuation.md),
  after equation (19).
* An edge meeting a seam uses the literal zero-uniform row bounds.
  The [height-resolved profiles](research_mixed_height_resolved_seam_sources.md),
  Theorem 1 and Section 3, cover both orientations, every other
  real angle, and the full allowed height/selection bands.
  The [closed-half proof](research_mixed_closed_half_period.md),
  equation (10), supplies the single SS-edge rate. These are
  uniform at zero and at numerator zeros, rather than extensions
  of compact-away-from-zero packets.
* Every remaining right-incident edge uses its complete absolute
  row envelope. The local source scope and the original Fourier
  halfweights are precisely those retained in
  [raw exterior repair](research_mixed_seam_raw_exterior_repair.md),
  Section 4, and
  [nonlow middle transport](research_mixed_nonlow_middle_transport.md),
  Section 5. The underlying uniform finite estimates are equations
  (2), (7)--(8) of
  [right-half source reduction](research_mixed_right_half_source_reduction.md):
  the zero-safe product upper bound, the reciprocal-factorial
  logarithmic error and the actual right-half Fourier bound.
  They cover all physical rows and both parities uniformly on
  these compact physical bands, including their endpoint zeros.

Only finitely many local type, selection and source-domain labels
occur. The reference heights in a repetition are the same fixed
heights, while each hybrid target depends on a fixed number of
neighboring coordinates through the original bounded cutoffs.
The displayed local source theorems are uniform on their complete
closed products. Choose their individual tolerances small enough
that each allocated block spends at most \(\tau\), and take the
maximum of their constants, polynomial exponents and level
thresholds. This proves (4) simultaneously on every edge of every
repetition. The finite alternative count per block is absorbed
into \(C_\tau\).

In particular, one does **not** apply a fixed-word bound with a
total tolerance and then assume its constants uniform in \(r\).
Here the tolerance is fixed per physical edge, so the total loss
allowed for a repetition is \(r\ell\tau\).

The pointwise full-period occupation theorem gives, before any
finite-source tolerance,
\[
             \sum_{j=1}^{r\ell}e_j
              \le rM_w-\frac1{20000}\sum_jp_j
              \le rM_w .
 \tag{7}
\]
This is the original envelope on every real configuration and
selection, not a statement inferred from a cyclic integral.
Its local comparisons and degree-two incidence counts are valid
at every length.

The [exact graph bound](research_mixed_split_cutoff_hybrid_contour.md),
equation (6), gives
\[
               |\det(I+iD\mathcal H_S)|\le60^{r\ell}.
 \tag{8}
\]
The parameter cube has volume one. Equations (3)--(8), summed
over the \(2^{rk}\) selections, therefore prove the explicit
all-repetition bound
\[
 \boxed{\quad
 |\operatorname{tr}(W_N^r)|
 \le\left[
    2^k60^\ell C_\tau^\ell
    N^{\,\ell+k+b_\tau\ell}
    e^{N(M_w+\tau\ell)}
                         \right]^r
       \quad(r\ge1,\ N\ge N_\tau).\quad}
 \tag{9}
\]
There is no partition-count constant growing faster than
exponentially in \(r\): the local estimates are already uniform
on the whole cube, and (8) bounds the graph directly.
All normalizations, both parity classes and every original
selection remain in (9).

## 3. The spectral-radius limit

For any fixed finite complex matrix \(T\),
\[
       \rho(T)=
          \limsup_{r\longrightarrow\infty}
                            |\operatorname{tr}(T^r)|^{1/r}.
 \tag{10}
\]
Indeed, if \(\lambda\) runs over its distinct eigenvalues with
algebraic multiplicities \(m_\lambda\), then near zero
\[
 \sum_{r=0}^{\infty}\operatorname{tr}(T^r)z^r
                  =\sum_\lambda\frac{m_\lambda}{1-\lambda z}.
 \tag{11}
\]
Every nonzero eigenvalue of maximal modulus gives a genuine pole
at \(z=1/\lambda\); a different eigenvalue has no pole there
and \(m_\lambda>0\). The convergence radius is therefore
\(1/\rho(T)\), and the power-series root test proves (10).
If \(\rho(T)=0\), the matrix is nilpotent and (10) holds
directly. Jordan blocks do not alter the traces in (11).

**Theorem 1.** Every fixed nonempty positive three/four word satisfies
\[
          \boxed{\displaystyle
          \lim_{N\longrightarrow\infty}
               \frac1N\log\rho(W_N)=M_w.}
 \tag{12}
\]
Both level parities are included.

*Proof.* First fix \(\tau>0\). For each fixed
\(N\ge N_\tau\), apply (10) to (9), obtaining
\[
 \rho(W_N)\le
  2^k60^\ell C_\tau^\ell
       N^{\,\ell+k+b_\tau\ell}e^{N(M_w+\tau\ell)}.
 \tag{13}
\]
Only after taking this repetition limit do we let \(N\) tend
to infinity. Its upper exponential rate is at most
\(M_w+\tau\ell\). Since \(\tau\) is arbitrary, this gives
the upper bound \(M_w\).

For the lower bound use only the already completed fixed-word
cyclic asymptotic, at repetition one:
\[
 \operatorname{tr}(W_N)
   =\kappa_N^{\ell+k}A_w e^{NF_w}(1+O_w(N^{-1})),
                      \qquad A_w\ne0.
 \tag{14}
\]
Since \(W_N\) has dimension \(N\),
\(|\operatorname{tr}(W_N)|\le N\rho(W_N)\). Equation (14)
therefore gives the opposite lower exponential bound. This proves
(12) without interchanging an unproved pair of uniform limits.
\(\square\)

For \(w=(3,4)\), (9) becomes
\[
 |\operatorname{tr}((A_{3,N}A_{4,N})^r)|
 \le[7200C_\tau^2N^{3+2b_\tau}e^{N(M+2\tau)}]^r,
 \tag{15}
\]
and its spectral rate is the same calibrated \(M\) as in the
[complete paired kernel](research_mixed_contracted_pair_full_kernel.md).

## 4. A word-specific adapted positive inner product

**Corollary 2.** Fix \(w\) and \(\varepsilon>0\).
For every sufficiently large \(N\), set
\(a_N=e^{N(M_w+\varepsilon)}\). There is a positive definite
Hermitian matrix \(H_N\ge I\) for which
\[
 W_N^*H_NW_N=a_N^2(H_N-I),\qquad
                         \|W_N\|_{H_N}<a_N.
 \tag{16}
\]

*Proof.* By (12), \(\rho(W_N)<a_N\) for all sufficiently
large \(N\). At each such fixed level the series
\[
 H_N=\sum_{j=0}^{\infty}
             a_N^{-2j}(W_N^*)^jW_N^j
 \tag{17}
\]
converges in matrix norm. For example the finite Jordan form
bounds its powers by a fixed polynomial in \(j\) times any
exponential strictly between \(\rho(W_N)\) and \(a_N\).
Every summand is positive semidefinite and the zeroth is \(I\).
Shifting the series proves (16); its strict norm inequality
follows from positive definiteness of \(I\) in finite dimension.
\(\square\)

This is an inner product adapted to the one complete word \(W_N\).
It is not a common metric for \(A_3,A_4\), does not make them
positive or self-adjoint, and is not multiplication by a scalar
Fourier weight. It is consistent with the earlier
[relative-operator obstructions](research_mixed_three_four_operator_obstruction.md).
No bound on the condition number of \(H_N\), on actual cap norms,
or on a closing overlap follows from (17). In particular the
spectral conclusion does not control a specified boundary matrix
coefficient or establish an open-source, knot-volume or cofinite
filling theorem.
