# Which derivatives the current direct-power route actually requires

The [whole-source local packet](general_full_spectral_numerator_geometric_packet.md) now assembles these results for the actual full numerator. The original global spectral filling period remains open.

31 October 2026. Internally reviewed.

Conclusion: the current route to the original root sequence does NOT
require a genuine-q normal estimate. It does require the full spectral
Hermite/Jordan data at the fixed root. Those are different derivatives.

For each individual N, fix q_N=exp(pi i/N), d=N-1, and the literal
original pair Casimir Omega_N. In
notes/actual_direct_long_power_source.md, section3, the exact identity is

    R_N^n=q_N^(n d^2/4) exp[n K(Omega_N)/(2hbar)],
    hbar=2pi i/N, K(sigma)=arccosh(-sigma/2)^2.

At each double Casimir node its value AND derivative with respect to
sigma equal those of the actual original R_N^n. At the odd simple node
only its value is required. Full Hermite uniqueness in the root Casimir
quotient therefore proves the matrix equality, including negative powers
and the original square-root scalar. No semisimple quotient is taken.
An earlier generic argument used to establish these finite identities
would not by itself introduce a uniform off-root asymptotic requirement.

The source map in notes/actual_homogeneous_casimir_face_source.md,
sections1--4, applies to these exact polynomials at the SAME fixed root.
It retains the original physical endpoints, Cartan factors, changing
strand positions, and unrestricted marked cap. The other caps and
integer total-degree conservation force the marked complementary pair
only AFTER the whole contraction. Its literal mark satisfies mp=1.
The cup/cap constants and mark character are assembled explicitly in
(7a,b); the inverse Fourier measure and original degree constraint give
the exact coefficient (9), with no extra N factor and no root limit.
In particular the ordinary quantum dimension is never divided out in
this direct marked evaluation.

The passage from that raw marked contraction to the original enhanced
Kashaev normalization is the existing fixed-root crossing/pivot/dual
comparison and retained framing character. The complete-color comparison
in notes/actual_complete_augmented_source_normalization.md uses root
cut scalarity, exact basis covariance and mp=1. It is local in the
crossing word and applies when a box contains the actual power R_N^n.
The enhanced reduced normalization differs by a recorded unit phase.
If one instead asks for the full one-cut modified ADO normalization,
its additional exact factor is i^(N+3)/N at the complete pointing;
that is not an uncomputed q-normal correction and has zero exponential
rate. No such extra modified factor is silently attached to Kashaev's
unknot-one evaluation.

The exact spectral Cauchy and total-derivative periods are therefore
alternative formulas for the SAME root marked scalar for every N.
Their V_N(sigma) and partial_sigma V_N contain the independent
nilpotent and semisimple data. Differentiating a value-only complete
interpolation would be invalid, but that issue is spectral, not a
requirement to deform q away from q_N. The current cofactor proofs
address precisely this fixed-root spectral issue.

The generic trace identity F_D(t)=D_N(t) z_D(t), with
z_D(0)=F_D'(0)/D_N'(0), is a valid ALTERNATIVE presentation of the
marked scalar in the matching-graph notes. Using that presentation
for asymptotics would require its specified moving-q lift and normal.
The direct marked/Casimir route does not use this quotient and need
not inherit its analytic hypotheses. Similarly, extending the result
to a generic-q or moving meridian invariant is a separate problem.

Although q_N varies with the integer level N, the desired theorem is
a limit of exact fixed-root identities indexed by N. It needs uniform
N estimates for those identities, not a derivative with respect to q.
The shared coefficient packet is now proved by the linked whole-source
theorem. The subsequent localized period theorem also supplies the nonzero
unit-charge contribution with its original normalization. The outstanding
gate is control of its exact global spectral/charge remainder. A genuine-q
normal should not be listed as another necessary gate for this route.

Audited sources: actual_direct_long_power_source §§1--3;
actual_homogeneous_casimir_face_source §§1--4;
actual_original_marked_face_coefficient §§2--4;
actual_complete_augmented_source_normalization §§1--3;
actual_spectral_total_derivative_source;
actual_coherent_filling_gaussian_chirp §1;
general_augmented_plat_long_twist_target equation(3a).
This is an analytical dependency audit, not a new numerical test.

Root independently checked the cited fixed-root Gaussian, Hermite data, original coefficient normalization and reduced/modified distinction.

The [localized original period](general_localized_unit_charge_filling_period.md)
now proves the nonzero unit-charge contribution and dominance in the
finite local charge sector. The remaining gate is its exact global
remainder, including the full integrals of remote charges. It does not
require a generic-q continuation.
