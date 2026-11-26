# Boundary comparison for the full open source

Research reduction, 5 November 2026. This note identifies a finite
boundary comparison for the original one-cap source. It retains the
actual open reference and the two surviving complex tangents. It also
explains why dropping the middle action loss can make that comparison
false already at quadratic order. No new global open-source estimate
is asserted. The comparisons below are at the complete ordinary colors
\((-2,-2)\); retaining the literal endpoint polynomials does not
assert a whole ordinary-color strip estimate.

## 1. Localizing the pointwise proof without a periodic reference

Fix the original critical point of a finite open word, put
\(r_j=t_j^*\), and let \(p_j=(\Re r_j,0)\) denote its baseline
symbol (real coordinate, selection). For a target symbol
\(q_j=(x_j,\sigma_j)\), use the same row-dependent periodic hybrid
height formula as in the cyclic proof. At an end of the path, the
missing neighbor has baseline cutoff one. The complete Laurent
integrand still admits this periodic graph by homotopy; its Jacobian
is bounded almost everywhere independently of \(N\), for the fixed
word and fixed collar width. Endpoint heights are not silently replaced
by cyclic heights.

For an ordinary edge \(j\), retain the original allocation
\[
 \Gamma_j(a,b)=\phi_j(r_{j-1},r_j)
       +P_{j,a}(a-r_{j-1})+P_{j,b}(b-r_j).                 \tag{1}
\]
Let \(\mathcal E_j(q)\) be the complete allocated upper rate:
the coherent phase with the true Fourier half-corrections where its
source theorem applies, the full absolute row rate on a right-incident
edge, and the original collar profile on a seam-incident edge. Collar
priority is the one in
[the completed cyclic assembly](research_mixed_full_cyclic_period.md).
Every selected frequency and factorial half occurs once. Define
\[
                    w_j(q)=\mathcal E_j(q)-\Re\Gamma_j(z_{j-1},z_j).
                                                               \tag{2}
\]
On an unchanged baseline edge this is zero. A changed rate or height
depends on the four symbols \(q_{j-2},\ldots,q_{j+1}\).

Call a finite interval of perturbed symbols *safe* when all original
reference windows touched by the cyclic proof's local replacements,
support inequalities and minimum-level derivatives lie in the interior
inheritance ranges of
[the open-window theorem](research_mixed_open_word_window_inheritance.md).
This is a fixed-width condition, not a length-dependent hypothesis.
The imported stages have the following reference requirements. The
entries count original reference vertices; the two external legs are
kept separately.

| Pointwise stage | Reference inputs | Sufficient maximum window |
|---|---|---|
| [Closed half](research_mixed_closed_half_period.md), including seam runs and early/plateau comparison | Independent typed reference rectangles; the five-window height bounds establish their actual-domain membership | Five vertices |
| [Raw exterior seam repair](research_mixed_seam_raw_exterior_repair.md) | The same closed-half run comparisons; the raw chord and bare-kernel comparison need only the admitted typed heights | Five vertices |
| [Upper-transition removal](research_mixed_nonlow_upper_transition_removal.md) | Independent typed height products; coherent and raw/coherent derivative domains, with the inherited typed geometry | Five vertices |
| [Minimum-level transport](research_mixed_nonlow_middle_transport.md) | The conditioned three-type boxes and the five-window 44/444 refinements; the physical star has radius two | Five vertices |
| Final early/plateau/right supporting-plane allocation | Three-window PR/RR and transition/right supports suffice for the newest independent-height route; the retained [right-run support atlas](research_mixed_right_run_supports.md), Theorem 1, also includes a six-vertex three-block support | Six vertices, conservatively |

An affected edge's own index is within two indices of a perturbed
symbol. A six-vertex reference window containing that index extends
at most five indices farther; its two external legs are at most one
additional vertex away. Thus every needed reference vertex and
external leg lies in the eight-vertex halo
\[
                         2+5+1=8.                       \tag{2a}
\]
For derivative stencils the corresponding bound is only
\(2+4+1=7\). Requiring the perturbation and its eight-vertex
halo to lie inside \([6,m-5]\) is therefore conservative.
In particular every complete window lies in the range of Corollary 2
of the open-window theorem, which explicitly transfers both five-
and six-vertex certificates with the original external legs.

**Lemma 1 (compact perturbations of the actual open reference).**
Suppose \(q_j=p_j\) outside a safe interval. The complete mixed
upper rate satisfies
\[
                              \sum_j w_j(q)\le0.          \tag{3}
\]
Only finitely many summands are nonzero. The original pointwise
strict losses, when used, are losses for this same reference.

*Proof.* This uses the pointwise proof, not its cyclic integral
conclusion. Clamp original right angles at \(.5\) with permanent
raw labels, raise nonseam deep lows, perform the collar repair, remove
upper transitions, and apply the minimum-level and early/plateau/right
comparisons, exactly as in the completed cyclic argument. Every moving
real coordinate and every erased selection belongs to the perturbed
interval. Outside coordinates are unselected baseline plateau values,
so they are never selected for any of these moves. Their heights can
change only at an adjacent incidence; all affected rates and reference
windows are safe by hypothesis. Thus every local source, derivative
and charge inequality has its original hypotheses.

The actual open equations give
\(P_{j,b}+P_{j+1,a}=0\) at every changed coordinate. Summing
all affected edges therefore cancels their complex tangent changes.
No change reaches either endpoint action. The regional charge argument
has only finite runs surrounded by baseline plateau positions; no
closing edge or periodic extension of the reference is introduced.
At the final all-plateau configuration, the original pair concavity
gives the required nonpositive residual. Retaining a nonempty early,
seam or raw-right set gives precisely the corresponding local charge
loss from the same proof. These are the steps establishing (3).
\(\square\)

In particular, on an unselected plateau perturbation all heights are
the reference heights, and the proved pair Hessian bound gives
\[
                   -\sum_j w_j(q)\ge\frac15
                         \sum_j(x_j-\Re r_j)^2.           \tag{4}
\]
Each perturbed coordinate has its two ordinary incidences. This is
the real variational bound, not a finite-kernel monotonicity claim.

## 2. Exact six-edge closure and the original endpoint factors

Choose ordinary middle edges \(p,\ldots,q\), retaining physical
symbols \(q_{p-2},\ldots,q_{q+1}\). Replace every other symbol
by its baseline value, and call this synthetic configuration
\(\widetilde q\). Assume its retained interval is safe. Then every
middle edge has its original four symbols and hence its original
height and rate. The only other possibly nonzero defects are
\[
 A_p=\sum_{j=p-3}^{p-1}w_j(\widetilde q),\qquad
 E_q=\sum_{j=q+1}^{q+3}w_j(\widetilde q).                  \tag{5}
\]
The left function uses the three retained symbols
\((q_{p-2},q_{p-1},q_p)\); the right one uses
\((q_{q-1},q_q,q_{q+1})\). No auxiliary edge is added to a
finite source. Lemma 1 gives
\[
 \sum_{j=p}^{q}w_j(q)\le-A_p-E_q,
 \qquad
 D_{p,q}(q):=-\sum_{j=p-3}^{q+3}w_j(\widetilde q)\ge0.    \tag{6}
\]
In fact the first expression equals \(-A_p-E_q-D_{p,q}\).
The nonnegative term \(D_{p,q}\) will matter below.

Retain the exact boundary moduli from equations (10)--(11) of the
open-window theorem:
\[
\begin{split}
 L_N&=|U_{\epsilon_1,N}|\prod_{j=2}^{p-1}|C_{\epsilon_j,N}|
       \prod_{j=1}^{p-2}|D_j|\ |D_{p-1}|^{1/2},\\
 R_N&=|H_N|\prod_{j=q+1}^{m}|C_{\epsilon_j,N}|
       |D_q|^{1/2}\prod_{j=q+1}^{m}|D_j|,\\
 D_j&=d_N(X_j)^{\epsilon_j}X_j^{-N\sigma_j}.
\end{split}                                                    \tag{7}
\]
The full original modulus is \(L_NR_N\) times the allocated
middle product. These are equalities of nonnegative moduli; there
is no division by a Fourier factor which may vanish.

Let \(b_L,b_R\) be any uniform exponential upper rates for the
literal expressions (7), with polynomial prefactors and one total
arbitrarily small rate tolerance. They must retain all rows of
\(U,H\) and all selected alternatives. Let \(M_L,M_R\) be
the unselected baseline phase values of the literal boundary products,
not the values of a possibly loose upper ceiling. Their nonzero local
source packets identify these values exactly and give
\[
 M_{\mathrm{open}}
 =M_L+\sum_{j=p}^{q}\Re\phi_j(r_{j-1},r_j)+M_R.           \tag{8}
\]
Define the two calibrated boundary rates
\[
\begin{split}
 \mathcal B_L&=b_L-M_L+\Re\{P_{p,a}(z_{p-1}-r_{p-1})\}-A_p,\\
 \mathcal B_R&=b_R-M_R+\Re\{P_{q,b}(z_q-r_q)\}-E_q.
\end{split}                                                    \tag{9}
\]
The tangent-sum identity for the actual open reference now proves
the explicit sufficient bound
\[
 \boxed{\quad
  \text{original upper rate}-M_{\mathrm{open}}
       \le\mathcal B_L+\mathcal B_R-D_{p,q}.\quad}        \tag{10}
\]
Both tangents survive in (9). Endpoint phases remain order-\(N\)
quantities inside \(b_L,b_R\).

The boundary rates in (9) have fixed width. For example one can take
\(p=16,q=m-15\) when the middle is nonempty; its retained interval
with the conservative halo above is safe. Each boundary function then
uses at most seventeen physical target symbols. The reference prefix
or suffix is the actual finite endpoint block, with one external
nonprivate leg held fixed. To identify this family, fix that external
leg in its typed disk. The already proved endpoint update at the
ordinary boundary and the ordinary two-leg updates at all other
vertices map the product of \(E,U\) and the original typed disks
into itself. Brouwer supplies a fixed point. The endpoint positive
pair form and the ordinary pair forms from the open Hessian proof
give the same uniform accretivity; at the fixed external leg its
pair contributes its active principal submatrix. Thus the solution
is unique on the product chart and is holomorphic in the external
leg. Restricting the actual open solution identifies it with this
one-ended branch. The reflected argument treats the suffix. This
uses neither a periodic completion nor a new root search.

Consequently the reference parameters belong to finitely many
fixed-length type families and one external typed disk. A word
too short for these cuts remains one finite boundary block; this
does not assert its global comparison has already been proved.
When the two boundary symbol sets overlap, their common symbols remain
the same physical variables in (10). No independence is asserted.

Formula (10), or its version with optimized middle loss, is a concrete
boundary-source target. It is not fulfilled merely by bounding the
two endpoint moduli by unspecified exponential constants.

## 3. Why separately discarding the middle loss is too strong

The proposed simplification \(\mathcal B_L\le0\) can fail even
on an unselected plateau, without any seam, raw row or selected alias.
This is an obstruction to that sufficient comparison, not to the
original open asymptotic.

Keep every physical symbol at its reference except
\(x_{p-3}=\Re r_{p-3}+\delta\) and
\(x_{p-2}=\Re r_{p-2}+\eta\). All target heights are their
unselected reference heights. Near this point the original boundary
finite factors have their established coherent source packets.
Use their exact phase rate for \(b_L\). The two common edges in
the physical and synthetic prefixes cancel, leaving exactly
\[
\begin{split}
 \mathcal B_L={}&w_{p-3}(r_{p-4},r_{p-3}+\delta)
    +w_{p-2}(r_{p-3}+\delta,r_{p-2}+\eta)\\
 &-w_{p-2}(r_{p-3},r_{p-2}+\eta),
\end{split}                                                    \tag{11}
\]
where real increments are understood and the reference heights
are unchanged. Any larger valid source ceiling is no better for
the desired nonpositivity.

Put \(K_j=-\Re\phi_j''\) at its actual reference pair and
\[
 A=(K_{p-3})_{22}+(K_{p-2})_{11}>0,
 \qquad B=(K_{p-2})_{12}.
\]
Since every defect and its gradient vanish at the reference, (11)
has Taylor expansion
\[
 \mathcal B_L=-\frac A2\delta^2-B\delta\eta
                  +O((|\delta|+|\eta|)^3).              \tag{12}
\]
Whenever \(B\ne0\), choosing \(\delta=-B\eta/A\) gives
\[
 \mathcal B_L=\frac{B^2}{2A}\eta^2+O(|\eta|^3)>0
                    \quad\text{for small nonzero }\eta.\tag{13}
\]
Thus this obstruction applies at any actual open reference with the
stated nonzero real mixed derivative; it does not assume such a
derivative from numerical samples.

For scale, the exact homogeneous-three conditional phase at
\(s=a=b=1/3\) has
\[
 K=\begin{pmatrix}
 5\pi/(2\sqrt3)&-\pi/\sqrt3\\
 -\pi/\sqrt3&5\pi/(2\sqrt3)
 \end{pmatrix},
 \qquad \frac{B^2}{2A}=\frac{\pi}{10\sqrt3}>0.           \tag{14}
\]
This follows by its elementary conditional Schur complement. It is
an exact ordinary-phase example in the certified local domains,
not an identification of an open endpoint reference with a cyclic
one. No new open-word counterexample is inferred from (14).

The positive amount in (13) is the gain from allowing the preceding
coordinate to relax. The original middle loss in (10) has not
disappeared. On a plateau it is controlled by (4) and more precisely
by the real Dirichlet energy of that chain. Its optimization retains
the coupling which the separate bound \(\mathcal B_L\le0\)
throws away.

## 4. The next comparison

The remaining target is therefore the literal boundary source rate
**together with** the calibrated middle completion in (10). Suppose
the retained corridor, including both terminal triples, is unselected
and lies in \(P=[.22,.45]\). Fix its two terminal triples
\(v_L,v_R\) in (5) and define
\[
 V_{p,q}(v_L,v_R)=
    \min_{\text{intervening unselected plateau symbols}}
                          D_{p,q}.                       \tag{15}
\]
All constants in the six closing edges are retained in this minimum.
After the prescribed terminal triples are fixed, its variable part
is an ordinary nearest-neighbor Dirichlet chain with two fixed real
endpoints. Overlapping prescribed triples must agree; a short chain
is retained directly. Since \(D_{p,q}\ge V_{p,q}\), formula
(10) remains valid with \(D_{p,q}\) replaced by \(V_{p,q}\).

The existing strong-convexity/finite-propagation proof in
[plateau boundary forgetting](research_mixed_plateau_boundary_forgetting.md)
uses only local Hessian bounds and interior stationarity; on a safe
open-reference interval these hypotheses hold verbatim. It gives
a fixed-depth approximation to that optimized completion, with the
stated error, while retaining the actual open reference. It does not
apply to selected or nonplateau corridor states.

More explicitly, pin the deep middle to its actual reference and
let \(V^{[d]}\) be the resulting minimum, with the same closing
constants. For a long enough corridor it splits into two finite
boundary windows, and the proved estimate is
\[
 0\le V^{[d]}-V_{p,q}\le\varepsilon_d,\qquad
 \text{upper rate}-M_{\mathrm{open}}
 \le \mathcal B_L+\mathcal B_R-V^{[d]}+\varepsilon_d.     \tag{16}
\]
For example the existing depth \(d=315\) gives
\(\varepsilon_d<1/4000\) on these plateau domains. Thus (16)
is a finite boundary-source inequality with a stated one-sided error,
independent of the intervening word length. It is not a difference
of unverified numerical lower optima. No sign of its right side has
been certified here.

A complete global proof must either extend the finite message
comparison to those other states, or first transport them into the
plateau while charging the exact boundary changes. The periodic
incoming potential cannot be imported merely because the interior
reference lies in the same rectangles. The new local packets justify
the central contribution and the local expansion (11); they do not
establish the global sign of (10), the whole ordinary-boundary strip,
the marked volume identity, or arbitrary short-filling stability.
