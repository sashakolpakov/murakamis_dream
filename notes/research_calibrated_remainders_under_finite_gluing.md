# Calibrated remainders under the original finite gluing

Research deduction, 7 November 2026. A global polynomial remainder
bound survives every fixed original Hermite gluing at polynomial
cost. Its calibration must then be compared with the action of the
composed source. This separates a reusable upper-bound mechanism
from the nonzero main contribution and from the action loss at an
actual short attachment. The three/four complementary contour gives
a concrete input to this mechanism. No numerical evaluation is used.

## 1. An unreduced-product version of the original trace bound

Use the original algebra
\[
 \mathcal A_N=\mathbb C[z]/(\chi_N(z)),\qquad
 \chi_N(z)=2T_N(z/2)+2,\qquad
 \phi_N(F)=(-1)^{N-1}N^2[z^{N-1}]
                              \operatorname{rem}_{\chi_N}F.
                                                               \tag{1}
\]
Let \(R\) be the original crossing and \(n\in\mathbb Z\) fixed.
The trace is the full Hermite functional: it retains the first
normal at every double root and the odd-level simple root.

**Lemma 1.** For every complex polynomial \(H\) of degree at most
\(L\), without requiring \(L<N\),
\[
 |\phi_N(R^nH)|
 \le N^2\left(\frac{L+1}{N}+\frac{|n|}{2}\right)
                                      \|H\|_{[-2,2]}.           \tag{2}
\]
The product is taken in the original algebra. On the right, \(H\)
is its displayed unreduced polynomial, not a pointwise replacement
by its canonical remainder.

*Proof.* The original normalized filling functional
\(\mathcal L_N^n=(-1)^{N-1}N^{-2}\phi_N(R^n\,\cdot)\)
has the exact midpoint expression in
[the uniform filling bound](actual_uniform_filling_supremum_bound.md),
equations (12)--(15). Put
\[
 \theta_j=(2j+1)\pi/N,\quad
 P(\theta)=H(2\cos\theta),\quad
 f_n(2\cos\theta)
  =q^{n(N-1)^2/4}e^{inN(\theta-\pi)^2/(4\pi)}.
                                                               \tag{3}
\]
The fixed exponential convention for \(q=e^{\pi i/N}\) is the
original one. The formula reads
\[
 \mathcal L_N^nH=-N^{-2}\sum_{j=0}^{N-1}
 \{\cos\theta_j f_jP_j+
      \sin\theta_j f_j'P_j+\sin\theta_j f_jP_j'\}.
                                                               \tag{4}
\]
It depends only on the original Hermite data, so holds for any
polynomial degree. In particular no canonical-remainder supremum
estimate is needed. We have
\[
 |f_j|=1,\qquad |f_j'|\le |n|N/2,\qquad
 \|P'\|_{\mathbb R}\le L\|P\|_{\mathbb R}
                         =L\|H\|_{[-2,2]}.
                                                               \tag{5}
\]
The last inequality is the complex trigonometric Bernstein inequality
proved by the finite Riesz formula in the same source. Summing (4)
gives (2). The midpoint formula includes both parity cases, including
the value at the odd simple root. \(\square\)

For \(L=N-1\), (2) is the established bound
\(N^2(1+|n|/2)\). Its explicit degree dependence is useful at a
joining vertex: a product of several canonical boundary polynomials
usually has degree larger than \(N-1\). One must not apply the
degree-\((N-1)\) estimate to that product without justification.

## 2. Finite networks and the exact calibration condition

Consider an actual finite source written in its original ordinary
boundary variables as
\[
 \mathfrak C_N(\{K_{e,N}\})=
 \left(\bigotimes_{v\in V_{\rm int}}\phi_N^{(z_v)}
                                  R_v^{\,n_v}\right)
                    \prod_e K_{e,N}(\mathbf z_{\partial e}).
                                                               \tag{6}
\]
This includes the usual circle-tree contraction after selected
components have been replaced by their exact boundary polynomials.
The graph, signed powers, factors and their boundary slots are fixed
before \(N\to\infty\). Each separate ordinary degree is \(O(N)\).
Original scalar normalizations remain outside (6) in their prescribed
locations; fixed powers of \(N\) and unit scalars cause no exponential
change.

Multiplication is performed before canonical reduction. At a vertex
\(v\), let \(L_v\) be the sum of the displayed degrees of the incident
factors in \(z_v\). Applying (2) successively gives
\[
 \|\mathfrak C_N(\{K_e\})\|_{\rm free\ real}
 \le
 \prod_{v\in V_{\rm int}}
 N^2\left(\frac{L_v+1}{N}+\frac{|n_v|}{2}\right)
                 \prod_e\|K_e\|_{\rm all\ real}.
                                                               \tag{7}
\]
Application in one variable does not increase the degrees in any
other variable. All boundary supremums in (7) are over their complete
real ordinary intervals. Full first normals at internal nodes are
already part of the proof; fixed derivatives at free boundaries
follow by Markov's inequality at polynomial cost.

Suppose exact polynomial subsources \(A_{e,N},E_{e,N}\), each with
separate degrees \(O(N)\) in its boundary variables, satisfy
\[
 K_{e,N}=A_{e,N}+E_{e,N},\quad
 \|A_{e,N}\|\le C_eN^{b_e}e^{NM_e},\quad
 \|E_{e,N}\|\le C_eN^{b_e}e^{N(M_e-\delta_e)},
                     \qquad\delta_e>0.                        \tag{8}
\]
The words “exact polynomial” matter: a local Gaussian approximation
is not substituted into (6) away from its source domain.
The degree requirement applies to both replacement polynomials,
not just their sum \(K_{e,N}\): an artificial high-degree cancellation
would not inherit the polynomial gluing cost in (7).
Multilinearity and (7) prove
\[
 |\mathfrak C_N(\{K_e\})-\mathfrak C_N(\{A_e\})|
 \le C N^B
       e^{N\{\sum_eM_e-\min_e\delta_e\}}.                       \tag{9}
\]
Every nonempty error subset is retained. There are finitely many of
them for the fixed source, so their count changes only the prefactor.
The same argument gives the larger sum of the individual
\(\delta_e\)'s for a prescribed subset of errors.

**Corollary 2.** Suppose separately that the prescribed retained
contraction has a proved nonzero asymptotic with real action
\(M_{\rm obs}\). Define its actual calibration deficit by
\[
                    \Delta=\sum_e M_e-M_{\rm obs}.             \tag{10}
\]
If \(\Delta<\min_e\delta_e\), then the full source has the same
leading asymptotic. Its error gap is at least
\(\min_e\delta_e-\Delta\), with polynomial prefactors retained.

This is an upper-bound and comparison theorem. It supplies no lower
bound for the retained contraction and no assertion that \(\Delta\)
is nonpositive. In particular norms of separate factors are not
identified with their signed matrix coefficient. The proved
exponential coherence loss in
[coefficient transport](research_complete_boundary_coefficient_transport.md),
Section 7, is compatible with (10): the deficit must be measured
at the intended geometric action, rather than assumed to have
zero exponential rate.

## 3. The actual three/four remainder is a transferable polynomial

Let \(I_{+,N}(w_L,w_R)\) be exactly the complete complementary
observation in
[the all-real-color theorem](research_mixed_three_four_complementary_real_colors.md),
equation (20):
\[
 I_{+,N}=\kappa_N^3N^2\int_{\Gamma_+}
 U_{0,N}(w_L,e^{-2\pi ia})V_{1,N}(w_R,e^{-2\pi ia})\,da.
                                                               \tag{11}
\]
The contour is fixed at the complete-color reference. Its finite
integrand is polynomial of degree at most \(N-1\) in each ordinary
variable; integration therefore gives a polynomial of those same
degrees. No off-grid spectral representative is being substituted.
Its established bound is
\[
 |I_{+,N}(-2\cos\theta_L,-2\cos\theta_R)|
 \le CN^B\exp N\left\{M_{34}-\frac1{600}
          -\frac{D(\theta_L)+D(\theta_R)}{2400}\right\},
 \quad D(\theta)=1-\cos\theta .
                                                               \tag{12}
\]
Here \(M_{34}\) is the certified original ordinary-pair action,
not an action assigned to an interior pair in a longer word.

For any actual boundary polynomials \(F_N,G_N\) of degrees at
most \(d_FN,d_GN\), with real bounds
\[
 \|F_N\|\le C_FN^{b_F}e^{NA},\qquad
 \|G_N\|\le C_GN^{b_G}e^{NB},
                                                               \tag{13}
\]
and fixed signed powers \(n_L,n_R\), the original two-sided
observation of this remainder consequently satisfies
\[
 \left|(\phi_N^{(w_L)}R^{n_L}\otimes
         \phi_N^{(w_R)}R^{n_R})
              [F_N(w_L)I_{+,N}(w_L,w_R)G_N(w_R)]\right|
 \le C'N^{B'}e^{N(A+B+M_{34}-1/600)}.                           \tag{14}
\]
Here \(F_N,G_N\) occupy the prescribed Frobenius boundary slots:
any required turns or fixed boundary adapters are retained in those
actual polynomials before (13) is applied. Formula (14) is not an
assertion that unadapted matrix entries compose by pointwise
multiplication, nor a bound transporting a supremum through a turn.
This statement retains the actual full trace and both ordinary
normal adapters, for both parities. It holds for arbitrary fixed
signed powers, with no near-invariance or positivity hypothesis.
Its explicit sufficient action comparison is
\[
                 M_{\rm composed}>A+B+M_{34}-1/600.            \tag{15}
\]
If only one boundary is glued, the same bound retains the other
angular loss in (12). Sharper known bounds for \(F_N,G_N\) can
be used before taking their supremums.

Equation (15) is not established for arbitrary short contexts.
Nor does (14) control the other source errors in those contexts.
The input of the new three/four proof is specifically the ordinary
endpoint coefficient \(H_N(w,r^{-j})\), whose coherent seam ceiling
is known. Replacing an ordinary endpoint by a neighboring short
component changes that coefficient. Applying its old ceiling to
the new component would omit precisely the context rates \(A,B\)
and the composed-action comparison in (15).

## 4. Why the finite typed-window route remains the appropriate local version

For positive words in three and four there is already a more local
calibration than the sum in (10). The
[boundary-comparison reduction](research_mixed_open_boundary_comparison_reduction.md),
equations (7)--(10), retains the literal prefix and suffix, their
actual reference actions, the two uncanceled complex tangents and
the nonnegative middle defect. Internal tangent terms cancel by
the original open critical equations.

The [finite-window theorem](research_mixed_open_finite_boundary_windows.md)
defines \(F_N\) to be the normalized logarithmic source-rate excess
after subtracting the actual reference action and retaining the two
boundary tangent terms and middle defect. Its
\(\mathcal T_{L,N}^{R,d}\) and \(\mathcal T_{R,N}^{R,d}\) are
suprema over the actual bounded left and right source windows,
including their relative pinning costs. It then bounds this excess by
\[
 \sup F_N\le
 \max\{-\eta,\ \mathcal T_{L,N}^{R,d}+
                         \mathcal T_{R,N}^{R,d}\}.              \tag{16}
\]
Its occupation constant is \(1/20000\), its relative pinning can
use \(d=352\), and \(R=(B+1)(2d+7)\) depends on one finite
boundary budget rather than the word length. All chosen source
windows keep the original ordinary factors, selections, Fourier
halfweights and prescribed boundary states.

Thus a word-length-independent finite family of calibrated source
inequalities is already a rigorous sufficient reduction for this
alphabet. Its unknown inequalities are signs and strict
complementary losses for the actual functions in (16), uniformly
in their admissible reference data and in \(N\). The scalar
\(M_{34}>27/10\) proves one specified two-ended problem; it does
not establish those functions at arbitrary boundary states.
Bounded-length words outside the pinning construction also retain
their complete source problems. A finite list of possible type words
does not mean a finite list of numerical levels suffices.

## 5. Marked path normal forms and the remaining alphabet

The exact [definite corridor normal form](research_definite_rational_corridor_normal_form.md)
has already reduced every fixed rational two-boundary corridor
with nonzero lower-left matrix entry to uniform-sign powers of
magnitudes at least two, apart from its integral/unit cases.
For its displayed negative form the full source identity is
\[
 \mathcal Q_N(W)=\kappa_N^\ell M_N^r
       [J_NM_N^{-b_1}J_N\cdots J_NM_N^{-b_k}J_N]M_N^s,
 \quad b_j\ge2,\quad
 \ell=(e(W)-r-s+\sum_j b_j)/3\in\mathbb Z.                      \tag{17}
\]
The topological equality separately carries its specified proper
half-turn on the attached tangle. The end powers shift the original
remaining parameters by fixed integers. The positive version uses
the mirror of the whole equality; an ordinary continued-fraction
sign convention is not substituted for the physical crossing
and turn convention.

The [degree-two reductions](research_degree_two_short_reductions.md)
and their marked counterparts remove \(0,\pm1\) with their actual
scalars, neighbor shifts and rotations. The zero case merges
parameters and must retain its generally infinite fibers.
Normalizing maximal corridors in a branching tree leaves the
branching pieces in place.

Even if every path with all magnitudes at least eight is available,
(17) leaves arbitrary strings of the finite short alphabet
\(\{2,3,4,5,6,7\}\), together with their long interfaces.
Their lengths are not bounded by finiteness of the alphabet.
The existing finite-kernel closure theorem permits a proved finite
collection of whole-boundary kernels separated by sufficiently long
powers; its threshold depends on the common analytic domains and
need not equal eight. It does not eliminate adjacent arbitrary
short strings.

A general solution may establish the analogue of (16) for a larger
alphabet, or an invariant packet class with the actual short gluing
and (15) uniformly controlled. Neither follows from the integral
chain's positive definiteness. Other branch degrees, degenerate
zero-merger cores and their parameter fibers remain distinct
requirements for the all-but-finitely-many target. In particular,
an unresolved reduced core cannot be discarded as a finite exception
when the original padding construction supplies infinitely many
assignments representing it.
