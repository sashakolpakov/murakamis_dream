# The one-sided full-numerator remainder on actual spectral polydisks

31 October 2026. Internally reviewed spectral remainder theorem. This is an absolute bound
for the ORIGINAL shared polynomial numerator at the fixed root. It uses
the reviewed unique geometric maximizer and the actual odd/even positive
majorants. It is not a relative estimate against an oscillatory value,
a Gaussian cycle theorem, or a genuine-q normal estimate.

## 1. The positive reference source and its fixed entropy gap

Fix the original certified flat plat D, with R ports, unchanged ordinary
face targets d=N-1 and its two protected targets zero. Write

  Phi=Vol(Y_D)/(2pi),
  V_N(sigma)=chi_N(sigma)(sigma-Omega_N)^(-1),
  F_N=-V_N(-2)                              (N even),
  F_N=V_N(-2)-N^(-2)partial_sigma V_N(-2)    (N odd).

These are the actual covariant coupons in the [homogeneous source theorem](actual_homogeneous_casimir_face_source.md), with the [exact odd/even majorants](actual_fejer_odd_regularized_full_numerator.md).
The coefficient of H_(F_N) at every local degree-d exponent is positive,
and its logarithmic rate is uniformly the same continuous h(q), q=n/d,
at both parities. Let Z_F be their original whole shared coefficient.
Then log Z_F/N -> Phi.

The [unique-maximizer theorem](actual_fejer_unique_geometric_maximizer.md) gives a single q_geom in the compact
incidence polytope Q_D, with every middle load strictly less than1/2.
On the closed set

  B_D={q in Q_D: some q_(e,b)>=1/2 or q_(e,c)>=1/2}

the continuous full entropy has maximum at most Phi-gamma, gamma>0,
provided B_D is nonempty. Fix that gamma throughout. The empty case
has no feasible one-sided source summands and the conclusions below
hold with identically zero remainder.

The path endpoints i<=j determine the original middle exponents
b^i c^(d-j). At N=2m, CROSS means i<=m-1 and j>=m; LEFT means j<=m-1,
and RIGHT means i>=m. At N=2m+1, CROSS means i<=m and j>=m; LEFT means
j<=m-1, and RIGHT means i>=m+1. Thus any noncross term has a normalized
middle load strictly greater than1/2, in B_D, at BOTH parities.

Let Z_F,nc be the original coefficient obtained by retaining all path
assignments with at least one noncross port in the positive product
of H_(F_N). Positivity, the uniform local coefficient theorem and the
polynomial number of integer arrays imply

  Z_F,nc <= exp[N(Phi-gamma+o(1))].                     (1)

The o(1) is independent of any spectral parameter used below. It is an
all-level statement with the indicated parity-dependent F_N, not a
subsequence assertion. No fixed-label eventual-feasibility test is
needed: the upper bound uses the FULL local coefficients at the same
actual integer exponents and the compact set B_D.

## 2. Exact support-preserving local spectral comparisons

Put a_j=2+2cos((2j+1)pi/N), theta(r)=arcosh(1+r/2), r>=0.
Let P_N(u)=(-1)^d H_(V_N(-2-u)); its unused-row path products are
nonnegative polynomials in u and the four original face variables.
For a complex u and |u|<=r, the triangle inequality on EACH original
path gives its positive value at r as a coefficientwise majorant.
All physical missing steps and endpoint zeros stay literal.

At EVEN N every a_j is positive. The ratio of an unused-row product
at r to its value at0 is bounded by the product over ALL rows. Hence

  |P_N(u)|_coef <= C_N(r) H_(F_N),
  C_N(r)=prod_j(1+r/a_j)
        =cosh^2(N theta(r)/2) <= exp(N theta(r)).       (2)

At ODD N=2m+1 only a_m is zero. The exact positive decomposition is
H_(F_N)=P_N(0)+N^(-2)Q, Q=partial_u P_N(0). Write Q_skip for those
derivative paths that skip row m. Visiting paths have nonzero value
at0; skipping paths have precisely one factor u. Therefore

  |P_N(u)|_coef
    <= C_N(r)[P_N(0)+r Q_skip]
    <= C_N(r)max(1,N^2 r) H_(F_N),                    (3)
  C_N(r)=prod_(j!=m)(1+r/a_j)
    =[sinh(N theta(r)/2)/(N sinh(theta(r)/2))]^2
    <= exp((N-1)theta(r)),

with C_N(0)=1. These statements retain the independent spectral
semisimple data in Q, not only the complete values at the root nodes.

Equations (2)--(3) apply SEPARATELY to every specified endpoint-support
class CROSS, LEFT or RIGHT. The comparison does not change i or j,
nor any local face exponent. At odd levels all noncross paths skip m;
there (3) may be sharpened to C_N(r)N^2r times the corresponding F_N
piece, but the displayed common max suffices. Visited-central derivative
paths belong to the cross support; they are never relabeled noncross.

## 3. The original shared numerator and its absolute remainder

Let S_N(sigma_1,...,sigma_R) be the entire ORIGINAL shared coefficient
of the product of H_(V_N(sigma_e)), with its original mark, cup/cap
normalization and target degrees. Let S_N,cross be the same coefficient
with every port restricted to the CROSS path class above. This is a
literal finite path partition of the polynomial numerator. It does
not replace a physical coupon by a freely interpolated off-node model.

Set Delta_N=S_N-S_N,cross. Expanding this difference retains exactly
the assignments having at least one noncross port. The common sign
(-1)^(dR) has modulus one. Apply (2)--(3) before taking the ONE original
shared target coefficient. For |sigma_e+2|<=r_e this proves the finite
inequality

  |Delta_N(sigma)| <= Z_F,nc prod_e M_N(r_e),          (4)

where M_N(r)=cosh^2(N theta(r)/2) for even N, and
M_N(r)=C_N(r)max(1,N^2r) for odd N. No extra N^R, independent face
norm, changed protected degree, or discarded Fourier alias occurs.

For fixed bounded radii, the odd additional factors cost only O(log N)
per port. Combining (1) and (4) gives uniformly on the full polydisk

  |Delta_N(sigma)|
    <= exp{N[Phi-gamma+sum_e theta(r_e)+o(1)]}.        (5)

In particular for a common fixed radius r the exponent is
Phi-gamma+R theta(r)+o(1). Since theta(r)->0, choose ANY sufficiently
small fixed r with R theta(r)<gamma/4. For all sufficiently large N,
the whole remainder on that polydisk is bounded by

  exp[N(Phi-gamma/2)].                              (6)

The radius can be made arbitrarily smaller. It depends on the fixed
diagram's gap, and no uniformity in growing diagrams or bridge width
is asserted. For ANY shrinking radii r_(e,N)->0, (4) instead gives

  limsup N^(-1)log sup_(|sigma_e+2|<=r_(e,N))|Delta_N|
       <= Phi-gamma.                               (7)

This remains true for polynomially or exponentially small radii; the
odd factor max(1,N^2r) causes no adverse small-radius cost.

These are ABSOLUTE errors relative to the geometric exponential scale.
They are not relative errors divided by S_N or S_N,cross, which may
vanish on a complex spectral locus. A nonzero relative cross packet
still requires an independent asymptotic theorem.

## 4. Spectral derivatives and the retained contour limitation

On the exact Cauchy polydisk r_e=N^(-2), theta(r_e)<=1/N and
M_N(r_e)<=e at both parities. Consequently for every multiindex alpha,

  |partial_sigma^alpha Delta_N(-2,...,-2)|
     <= e^R alpha! N^(2|alpha|) Z_F,nc.               (8)

For fixed alpha this has rate at most Phi-gamma. Fixed smaller
polydisks inside (6) also retain its exponential bound under fixed
spectral derivatives, by ordinary Cauchy margins. These are derivatives
of the original numerator's spectral variables, not genuine-q normals.

The actual direct-power period still contains the Gaussian factors,
the full chi_N denominators, and contours enclosing ALL physical poles.
The estimates above isolate its numerator on a specified small spectral
polydisk only. They do not justify discarding a growing Gaussian arc,
choosing a nonzero charge, moving the original cycle into that polydisk,
or asserting a contribution to the filled-knot invariant. Those
phase-sensitive operations remain separate.

Root and an independent internal reviewer checked the complete written
consequence, including the support-preserving path comparisons, both
parities, fixed and shrinking radii, and spectral derivatives. This uses
the linked exact identities and entropy proofs; it does not infer
asymptotic cancellation control from finite numerical experiments.
