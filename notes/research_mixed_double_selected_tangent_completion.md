# Simultaneous selection at the first two positions

Research theorem, 6 November 2026.

When the first two crossing powers are four, their simultaneous
Fourier selection has a strict exponential gap on the full prescribed
central integration region. The third power may be three or four,
and every later power may independently be three or four. The proof
bounds all remaining profile functions on their entire real boxes.
It uses the same original stationary reference and the full original
finite factors.

This is a theorem about a specified part of the source integral.
The subsequent assembly adds these terms to the already controlled
partial sum. Regions outside the central integration region and the
whole knot invariant are not covered by this theorem.

## 1. The original phase and the profile defect

Fix a mixed positive word of length \(m\ge4\), with first powers
\((4,4,3+\beta)\), \(\beta\in\{0,1\}\). Use the actual reference
\[
 r=(e_*,a_*,u_*,z_*,v_*,b_*).
\]
Here \(e_*\) is the first private cap coordinate; \(a_*,z_*,b_*\)
are its first three retained coordinates; and \(u_*,v_*\) are the
ordinary indices in factors two and three. The next external index
parametrizes this reference through the original canonical family.

Keep the original bare cap phase \(\Psi\), ordinary phases \(Q_1,Q_\beta\),
and primitive \(g\), with their prescribed branches. Define
\[
 F=\Psi(e,a)+Q_1(u;a,z)+Q_\beta(v;z,b)
                         -g(a)-g(z)-\frac\beta2g(b),
 \qquad
 p_R=g'(v_*+b_*)-(1+\beta/2)g'(b_*).
\]
Its five internal derivatives vanish at \(r\). The sole remaining
boundary derivative is \(p_R\).

Set both selected heights to \(H=1/100\) and put \(P=[.22,.45]\).
The target real box has coordinates
\[
 e_R\in[.27,.49],\quad a_R,z_R,b_R\in P,\quad
 u_R\in[.125,.5],\quad
 v_R\in[\ell_\beta,.5],\qquad
 \ell_0=.15,\quad\ell_1=.125.
\]
The private and ordinary main contours retain their reference heights.
The cap-left profile instead fixes \(e=.27\); the outgoing half-row
profile fixes \(v=.5\). Both fixed cuts are real. The outgoing half
row is needed only when \(\beta=0\).

For each cap and outgoing choice, and
\(\nu_1,\nu_2\in\{0,1\}\), let
\[
 D_{\nu_1,\nu_2}
 =\Re\!\left\{
 F(w)+(1-\nu_1)g(w_a)+(1-\nu_2)g(w_z)
   +2\pi i(\nu_1w_a+\nu_2w_z)-F(r)-p_R(w_b-b_*)
 \right\}.
\]
The selected arguments have imaginary part \(H\); all other heights
are those just specified. A value \(\nu_i=1\) denotes the factorial
alternative, and zero denotes the forced alternative. These are the
upper-rate alternatives for the original finite weights, not new
independent quantum sources. There are sixteen remaining profiles
for \(\beta=0\), and eight for \(\beta=1\).

**Theorem 1.** On both complete canonical parameter domains \(K_3,K_4\),
every remaining profile and every target in its full box satisfy
\[
                         D_{\nu_1,\nu_2}<-\frac1{100}.
\]

## 2. A certified tangent bound on every boundary cell

The [concavity theorem](research_mixed_double_selected_concave_profile_budget.md)
applies on each entire target box, including its original small-index
intervals and the real fixed cuts. Its proof adds the bare cap Hessian
bound to the two bare ordinary bounds. The remaining terms have
nonnegative negative real Hessian. Thus at any real trial \(y\),
\[
 D(x)\le D(y)+\nabla D(y)\cdot(x-y).
\]
The maximum of the right side on a box is its explicit support
function. This eliminates every target variable without assuming that
the trial is stationary or that a numerical optimizer converged.

The [complete calculation](../repro/results/research-mixed-double-selected-tangent-boundary-attempt01.json.gz)
uses all 1,431 certified reference cells in the original boundary bank.
Together with 114 strict geometric exclusions, these give all eighteen
complete boundary partitions. For each required profile, the evaluator
uses a rational trial and encloses its original value and derivatives
with Arb at 192 bits. The four endpoint products for each gradient
interval give an exact rational upper bound for its support term.
All 17,728 resulting upper bounds are strictly negative.

No reference root, parameter subdivision, or derivative of the
reference family was recomputed. Thirty-two numerical proposals carried
an unsuccessful optimizer flag. Their rational trial points still
belonged to the original boxes, and the same interval tangent bound
proved their inequalities. The optimizer flags have no role in the
acceptance criterion.

The calculation retains the original cap action and outgoing
marginal in every reference subtraction. Its
[evaluation specification](research_mixed_double_selected_tangent_evaluation.md)
describes the branches and all recorded arithmetic. The complete result
has SHA-256
7558c95df3e34d43f8f3e2177ac3768617a50d63864b9a98c329c65639dce61e.

The [saved-data check](../repro/results/research-mixed-double-selected-tangent-boundary-saved-audit.json)
verifies all 88 input bindings, the complete boundary partitions and
reference associations, and all 106,368 exact support contributions.
It also checks every reference enclosure against the real and height
domains needed by the cap and ordinary Hessian theorems, including
the private height interval \([-.051,-.019]\). These individual
coordinate bounds extend to the canonical domains by the harmonic
maximum and minimum principles. No joint interior correlation is
inferred from independent extrema.

## 3. Extension to the entire external parameter domain

The [one-boundary extension](research_mixed_double_selected_boundary_extension.md)
proves
\[
 \Delta D\ge-2B_R,\qquad B_R=|p_R'b_*'|.
\]
There is no incoming response term after the original first cap has
been restored. The saved reference records already enclose \(B_R\).
Its whole-boundary maximum and the phase's whole-boundary maximum
are taken separately.

The following conservative rational bounds follow from the complete
record. Here \(D\le-\gamma\) on the entire boundary and \(B_R\le B\).

| Third flag | Domain | \(\gamma\) | \(B\) | \(\gamma-R^2B/2\) |
| --- | --- | ---: | ---: | ---: |
| \(0\) | \(K_3\) | .02342 | 1.637 | .0177813535 |
| \(0\) | \(K_4\) | .03628 | 2.044 | .0326008 |
| \(1\) | \(K_3\) | .03415 | 1.364 | .029451702 |
| \(1\) | \(K_4\) | .04078 | 1.672 | .0377704 |

The radius factors are \(R_3^2/2=.0034445\) and \(R_4^2/2=.0018\).
The clipped-disk maximum principle gives
\[
                         D\le-\gamma+\frac{R^2B}{2}
\]
throughout each domain. All four corrected gaps exceed \(1/100\),
proving Theorem 1. The same target is held fixed while applying the
maximum principle; no numerical optimum or scalar majorant is
differentiated.

## 4. The complete local finite product

Write \(X_1=e^{-2\pi ia}\), \(X_2=e^{-2\pi iz}\),
\(X_3=e^{-2\pi ib}\), and retain the original finite kernels and
Fourier weight. The literal allocated modulus is
\[
 \mathcal B_{123,N}=
 \left|U_{1,N}(w_L,X_1)C_{1,N}(X_1,X_2)C_{\beta,N}(X_2,X_3)
             d_N(X_1)X_1^{-N}d_N(X_2)X_2^{-N}\right|
             |d_N(X_3)|^{\beta/2}.
\]
The last factor is only an allocation of a modulus. It introduces
no holomorphic square root and no division at a zero.

**Corollary 2.** For every positive tolerance \(\tau\), at both level
parities and all sufficiently large levels,
\[
 \mathcal B_{123,N}\le C_\tau N^{A_\tau}
   \exp N\left\{\Re F(r)+\Re[p_R(b-b_*)]-\frac3{1000}+\tau\right\}.
\]
The same conclusion holds on a sufficiently small fixed ordinary-color
disk, with fixed derivatives on smaller disks.

Indeed the [last-row theorem](research_mixed_double_selected_last_rows.md)
already supplies the gap \(3/1000\) for its eight omitted profiles.
Theorem 1 pays every other profile by the larger gap \(1/100\).
Insert both into the complete finite-current reduction, retaining all
rows, aliases, joins, and both selected weights. Its original color
estimates spend one arbitrarily small total tolerance. Cauchy's formula
applies to the original integer-weighted holomorphic product; the
outgoing modulus allocation is not differentiated.

Choosing the tolerance strictly below \(3/2000\) and absorbing the
polynomial prefactor gives the finite-source rate gap \(3/2000\).
The outgoing derivative and halfweight remain available for exact
assembly with the suffix, including the terminal join at \(m=4\).
