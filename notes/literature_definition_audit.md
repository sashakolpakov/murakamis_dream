# Literature definition, independent audit, and equivalence question

Current scope, 25 October 2026:

The target is Kashaev's original invariant. The AK definitions audited
below are comparison objects. The subsequent
[direct crossing audit](kashaev_crossing_and_period_lattice.md) and
[ADO pointing calculation](kashaev_ado_pointing.md) now specify the
original enhanced state and its literature all-level annihilator ideal,
with independent matrix, pairing and normalization proofs. No AJ or
all-level holonomicity theorem is assumed merely from accepting that
ideal's definition.

* Use a quantum object defined in the existing literature, with its prescribed
  state, operator conventions, normalization and parameter regime.
* Do not assume the correctness of the published proofs. Reconstruct and check
  the identities and analytic arguments actually needed.
* Preserve the earlier custom constructions as comparison candidates. They
  become results about the chosen literature object only after an equivalence
  has been established; a common classical A-curve or volume rate is insufficient.
* Retain peripheral variables and allowed boundary factors before specializing
  to the complete ideal point. A numerical multiplier in a specialized 2–3
  comparison is not by itself an obstruction to the appropriately normalized
  move identity.

## 1. An existing definition to audit

Andersen–Malusa, *A Geometric Quantisation view on the AJ-conjecture for the
Teichmueller TQFT*, arXiv:1711.11522v3 (30 April 2024), Section 5,
Definition 5, printed page 21:

https://arxiv.org/pdf/1711.11522v3

The object is the specified Andersen–Kashaev state J^(b,N)_(M,K), and its
annihilating left ideal in the q-difference algebra. The paper singles out a
primitive operator of minimal shift degree when the relevant ideal is nonzero.
The state and its quantum operators are described in Sections 2.1–2.3 and 5.
This is not an instruction to choose a convenient solution of a naively
ordered classical A-polynomial.

For general knots the same source treats existence/nontriviality and the
classical-symbol identification as conjectural. Those are proof obligations
here, not consequences of accepting the definition. The purported statements
for 4_1 and 5_2 likewise remain to be independently checked.

The source and original PDF for the underlying construction are Andersen–Kashaev,
*A TQFT from quantum Teichmueller theory*:
https://arxiv.org/abs/1109.6295 . Fix a source version before transferring formulas.

## 2. Necessary checks

1. Write the exact published state integral, quantum dilogarithm, Gaussian,
   Haar/spectral measure, contour and peripheral multiplication/shift operators.
2. Verify the local functional equations and quantum commutators directly.
3. Verify noncommutative elimination using explicit certificates.
4. Check the passage from integrand equations to state equations: contour
   changes, residues, endpoint terms and parameter domains must be accounted for.
5. Establish nonzero state, minimality and the classical limit with all
   removable or nonremovable factors recorded.
6. For volume, establish the appropriate asymptotic for that exact normalized
   state. Existing claims about contour deformation, saddle selection and
   uniform error estimates are not assumed.

The earlier computations in `quantum_a_volume.md` do not discharge these checks
for the literature state.

## 3. How to test equivalence with the custom candidate

Match variables first: in the classical symbol the literature Q corresponds
to m^2, so its q-commutation parameter must be compared with the square of the
parameter for a shift acting on m itself. Include orientations, Fourier or
Gaussian conjugations and peripheral/framing changes explicitly.

Then compare operators at generic q and generic peripheral variables, allowing
the units or boundary factors permitted in the stated construction. For a
second-order equation with coefficients a_0(X),a_1(X),a_2(X), EX=qXE,

    I(X)=a_0(qX)a_2(X)/(a_1(qX)a_1(X))

is invariant under multiplying the equation by a scalar function and under
a scalar gauge f(X)=g(X)u(X). It is consequently a useful test for the simplest
possible equivalence, including right multiplication by scalar units. It does
not test equivalence by a general matrix gauge or change of polarization.

Finally relate the states themselves. An operator equivalence alone does not
identify a selected integration cycle, a particular solution, or an
exponentially significant normalization.

## 4. Peripheral factors and the factor-eight observation

The local angle-factorial test evaluated two specialized amplitudes, 1/27 and
1/216 at N=6. Its ratio 8 establishes only failure of strict equality of those
bare amplitudes.

A factor such as (1+M^a) is a unit near M=1 and specializes to 2. Products of
such factors can produce 8. This illustrates why the numerical observation
cannot decide the correct move law; it does not identify its missing factor.

For each move, the calculation should retain its boundary variables and
determine whether the multiplier is an allowed unit, a change of boundary
trivialization, a projective scalar, a quantum-dilogarithmic factor, or a genuine
anomaly. Its behavior under composition of moves must then be checked.

Factors vanishing at the ideal point require separate limit analysis. Generic
localization permits division by them, while the analytic germ at M=1 may
not. That distinction is already visible in right factors involving Q-1 in
the literature operator comparison.

## 5. Current proof status

The literature definitions are starting data. No equivalence between
the custom cone-normalized states and the literature state is established.
No failure of topological invariance modulo allowed boundary factors has been
proved by the factor-eight test. Neither publication nor matching numerical
volume asymptotics is being used as a substitute for an audited proof.

An initial exact algebraic check is reproducible with
`python3 experiments/compare_literature_quantum_a.py`. It compares the custom
figure-eight operator with the explicit candidate q P'_q obtained from equation
(13) of arXiv v3. Their scalar-gauge invariants differ for generic q, although
their classical invariants agree. Thus a mere scalar normalization in the
same peripheral coordinates cannot identify these two operators. This does
not exclude a more general intertwiner or change of polarization, and it does
not assume that the candidate is the minimal annihilator of the literature
state.

The same calculation finds a discrepancy among the formulas **as printed in
arXiv v3**: right-multiplying q P'_q by Q-1 agrees with equation (5) in the
constant and quadratic shift coefficients, but its linear shift coefficient
has an additional factor qQ-1. Inserting that factor into the printed equation
(5) makes the asserted right-factor identity exact. This was checked against
the original v3 TeX source, not inferred from PDF text extraction. The
classical prefactor stated in Theorem 17 also needs reconciliation with the
explicit specialization in the proof of Theorem 19. These may be typographical
errors; they do not by themselves disprove the underlying construction. The
journal version and any corrections must be checked before attributing the
discrepancies to the final published article.

## 6. Subsequent independent proofs and exact comparisons

The full derivations are in `literature_state_volume.md` and
`custom_literature_equivalence.md`.

1. The Faddeev defining integral gives a uniform *complex* O(b^2) logarithmic
   remainder on every smaller strip |Im z|<=pi-delta, for all Re z. The proof
   explicitly handles the upper indentation and normalization constant.
2. On a contour through the regular ideal saddle, the exact literature
   figure-eight state satisfies

       J_b(0)=3^(-1/4) exp(-Vol(4_1)/(2 pi b^2))(1+o(1)).

   The contour has a fixed strip gap; the manuscript's compact-fold pole
   accumulation is not being passed through.
3. The v3 Ore certificate for equation (13) is exactly correct. It was expanded
   in the noncommutative four-generator algebra, separately from the printed
   equation (5) discrepancy above. The integrand equations were recovered from
   the defining integral, and the finite contour shifts justified near the
   semiclassical parameter. A local uniform saddle expansion and the nonsquare
   classical discriminant rule out a rational first-order annihilator. Thus
   the explicit second-order operator is minimal for this level-one state on
   its specified analytic branch. No general-level-N theorem is inferred.
4. The same remainder estimate and a negative definite real Hessian prove a
   volume law for the published FAMED state integral (4.5), given positive
   complete shapes and the finite face, edge and peripheral matrix certificates.
   This does not prove a quantum annihilator exists for every member of that
   class, nor verify blanket knot-family or census membership claims.
5. Our compact Psi_q is an exact factor of Phi_b after its second, dual compact
   product is included. Functional equations and the left-end normalization
   independently prove this equality in the convergent complex-b regime.
6. The two figure-eight companion systems are inequivalent even under rational
   two-by-two gauges in the same peripheral coordinates. The proof uses finite
   pole propagation and formal degrees at zero and infinity; a scalar invariant
   alone would not suffice. Changes of polarization and nonrational transforms
   remain separate questions.

The exact generic-q factors are retained throughout. In particular the minimal
operator's classical specialization contains (Q^2-1) times the geometric
quadratic; those factors cannot be canceled at Q=1 without a limit analysis.
The bare factor-eight observation about the different positive factorial model
continues to have only the limited interpretation in Section 4 above.

There is a further scalar-normalization discrepancy to reconcile in the
displayed change of variables preceding equation (4.5) of the FAMED preprint:
the stated Jacobian is p_1 but the displayed fiber prefactor is p_1 rather
than 1/p_1. The broad volume proof explicitly fixes the printed integral;
the difference is a recorded nonzero constant, not an assumed exact equality
of differently normalized states.
This discrepancy was also checked in the original v2 TeX source, lines
3277–3292. The N=1 dilogarithm convention was separately checked from the
finite-product definition (122) of Andersen–Kashaev, arXiv:1409.1208.

## 7. General existence and the explicit twist families

`general_annihilator_and_volume.md` now proves a nonzero annihilator exists
for the rescaled geometric FAMED integrals in the Andersen–Malusà b-shift
algebra. Exact finite products give a common denominator with linear degree
growth. A dimension count eliminates the internal multiplication variables.
If the resulting operator vanishes when the internal shifts are set to 1,
exponential moments extract its first nonzero Taylor coefficient. A finite
restriction-of-scalars argument returns to the prescribed peripheral field.
The operator of least degree then exists by skew-polynomial division.

The same exact state has a locally uniform, nonzero geometric saddle
asymptotic. Consequently the classical symbol contains the geometric
peripheral component with explicitly recorded PSL/SL lift, inverse and
factor-of-two conventions. No claim that all other classical components have
been removed is made.

There are two finite-b conventions that must not be identified: the natural
Andersen–Malusà algebra uses q_b=exp(2pi i b^2) and a spectral shift -i b;
FAMED Section 4.4 uses q_F=exp(4pi i hbar) and scaled shift +4pi i hbar.
The existence theorem here is for the former action on the rescaled published
integral. It does not establish the latter's conditional AJ hypothesis.
Moreover the source's displayed WKB substitution for its positive shift
gives exp(-H_l) from its stated potential derivative, so its inverse-longitude
convention requires reconciliation before use.

For 4_1 the exact conversion of the two literature state normalizations is

    J_F(hbar,2pi sqrt(hbar)t)
       = zeta_b/(2pi sqrt(hbar)) exp(pi(b+b^(-1))t) J_AM,b(t).

This boundary factor changes the classical longitude root's sign. It is
retained at generic peripheral value, and only then evaluated at t=0. The
factor is exponentially significant at a fixed scaled boundary value.

`twist_family_audit.md` reconstructs the two explicit infinite face families,
their face Gaussian, the edge/face matrix identity, and positive complete
geometric angle maxima by formulas valid for every fixed twist parameter.
It includes a multiplier/horosphere proof that an interior angle maximum
produces a complete metric. The exact finite checks rebuild edge incidences
and the matrices from the face pairings for p=0,...,8 in both parities.
They support the all-p formulas; they are not used as a substitute for them.

A further generic-boundary discrepancy was found in arXiv:1903.09480v5:
the even-family theorem prints x(x-y_U-y_W), while the derivation at TeX
lines 8791–8802 gives x(y_U-y_W-x). The direct face-matrix substitution agrees
with the latter. Both expressions agree at x=0. The exact state fixed for
this audit is the later FAMED integral, and the final journal version of the
older twist paper has not been checked for the discrepancy.

The subsequent `twist_topology_and_peripherals.md` reconstructs the
knot-diagram identification and independently identifies the peripheral
curves by constant-size normal-curve certificates. Its meridian separates
the marked-edge germs before drilling; its primitive longitude is an
integral boundary in the complement, and its angular branch correction is
zero. Exact diagnostics and optional Regina recognition check eighteen
examples against those uniform formulas.

Global exact state transformations and the extension to every alternating
knot remain unfinished. The active goal is not marked complete on the basis
of the state-integral criterion or the twist-family theorem for specified
literature realizations.

## 8. Independent positive local move and a fiber-normalization equivalence

`faddeev_pentagon_audit.md` derives the Faddeev Fourier formula from both
shift equations, fixes its constant using Fourier inversion and a Fresnel
asymptotic, and obtains the generic scalar Ramanujan integral from two shift
identities and its residue at zero. Pole cancellation in the contour shifts
is explicit. These give the bounded operator pentagon by an integrable
spectral regularization.

For the charged operators defined in AK (18), the resulting exact identity is

    T_12(a_4,c_4)T_13(a_2,c_2)T_23(a_0,c_0)
       =exp(pi i c_b^2 P/3)T_23(a_1,c_1)T_12(a_3,c_3),
    P=2(c_0+a_2+c_4)-1/2,

under the full positive charge relations recorded in that note. It holds
with all face boundary variables unspecialized. The charged proof is a
contour translation of the scalar uncharged kernel identity; it does not
treat the separately unbounded exponential charge factors as bounded.
The phase and all boundary-linear terms are also checked symbolically.

The same note identifies the exact factor J_coarea=J_printed/p_1^2 for
the FAMED fiber Jacobian convention. It is a nonzero constant normalization,
so these two states have the same annihilator and volume rate. This does
not silently replace the printed state: its factor is recorded throughout.

The local identity can be contracted with a convergent exterior kernel or
Schwartz boundary states. An explicit invertible face matrix also makes
the full positive tensor contraction absolutely convergent; this supplies
the gluing justification for embedded replacements of the audited operator
pentagon pattern when both full face matrices are invertible.
General gluing, movement outside the positive
chamber, the level/framing convention, and the exact polarized fiber-state
covariance still need their own checks. No generic multiplier for the
different positive factorial comparison model is inferred from it.

## 9. Exact peripheral phase and state recovery

`peripheral_phase_and_state.md` upgrades the magnitude relationship to the
complex identity

    Z_AK(X,alpha)=sigma_X exp(pi i N/12+i K_X(alpha)/hbar)
         integral_(R+i mu) (J_printed(hbar,x)/p_1^2)
                                   exp(lambda x/(4pi hbar)) dx,
    sigma_X=sign(det(script-A)p_1).

It derives K_X from the charged kernel and defining inversion identity,
including the imaginary lift in the boundary coordinate. Choosing the
published AK level ell=-4K_X/pi removes exactly that angle phase. The
fiber state is then uniquely recovered by analytic continuation and
Fourier–Laplace injectivity with the proved exponential tail bounds.

On balanced angles K_X is affine apart from the universal term
-lambda mu/(8pi). Compatible positive moves cancel this quadratic term;
the remaining scalar transform law is eta exp(i(d_0+d_1 lambda)/hbar).
A zero-slope certificate identifies the same state up to its recorded
scalar. A nonzero slope requires an explicit meridian translation and
its contour check. The slope is not silently set to zero.

The generic mixed-sign phase identity is symbolic. Eighteen twist angle
spaces were checked in their entirety, and pointwise quantum checks using
the independently derived real-b remainder agree within 9e-15. The raw
phase varies even at fixed peripheral angles in all eighteen examples.
Actual move sequences, other vertex-order patterns, and the all-alternating
geometric extension remain unfinished.

## 10. A calibrated connecting move for the figure-eight state

`tetrahedral_symmetry_and_figure_eight.md` derives all three adjacent vertex
transposition identities from the audited Fourier formula. The published
Gaussian triangle kernels supply an exact S_3 action: their cyclic product
has cube scalar exp(3pi i/12-pi i/4)=1. Gaussian regularization justifies
their cancellation in the proper contractions used here.

The note reconstructs the actual 3–2 bipyramid in the p=0 even twist
triangulation. Its canonical signs are all negative, so the adjoint
pentagon is required. It transports the full positive angle space and
the preferred peripheral rows, which reverse both meridian and longitude.
The affine phase certificate has slope zero and constant 11pi/12.

An explicit orientation-preserving automorphism of the resulting
two-tetrahedron triangulation also reverses both peripheral curves and
has zero phase difference. Transform uniqueness proves its selected state
is even. Thus, for the stated face orders and printed normalizations,

    J_3(hbar,x)=-exp[-pi i/12+11pi i/(12hbar)]J_2(hbar,x).

The corresponding minimal order-two operator is exactly the same; its
reflection multiplier is only -q^(-6)Q^(-6), and no nonmonomial peripheral
factor has been removed. The exact face, angle, phase, automorphism and
operator checks are reproducible. Independent two-dimensional versus
one-dimensional integration agrees within 1.2e-12 in four checked cases.
General connecting sequences and the all-alternating extension remain open.

The further argument in Section 6.1 of `peripheral_phase_and_state.md`
removes the affine phase slope for any certified positive path with
compatible complete geometric endpoints. At lambda=0 the full saddle has
x(y*)=0, so hbar times the logarithmic longitude derivative of its normalized
transform tends to zero. Comparing the exact affine transform laws forces
d_1=0. Consequently selected-state annihilator ideals and volume limits are
invariant along these certified proper positive paths; no meridian
translation is discarded by convention. Path existence beyond the audited
components and the all-alternating geometric certificates are still required.

## 11. An independent edge theorem and a certified non-twist example

`face_edge_stokes_identity.md` proves the edge rows A_ed=B_ed G for any
globally branched oriented face pairing with invertible script-A. The proof
constructs a face assignment from arbitrary edge values and cancels an
oriented face sum. It also proves rank B_ed=N-1 for one-cusped triangulations.
This sharpens the earlier finite-certificate treatment; it neither assumes
nor proves that the preferred-longitude row follows automatically.

The folded-layer construction in the appendix of Guéritaud--Futer,
[arXiv:math/0406242](https://arxiv.org/abs/math/0406242), gives explicit
face permutations from an R/L word. Its combinatorics have been reconstructed
in `experiments/layered_two_bridge.py`. The general geometricity proof in that
paper has not been adopted as an unaudited hypothesis.

For the particular word RLRL, `six_three_and_two_bridge_audit.md` supplies
an independent rational Rouché certificate, polynomial gluing identities,
rational logarithmic-argument bounds, and a preferred-longitude cellular
boundary certificate. These prove positive complete geometric and peripheral
data for the specified 6_3 state and put it under our analytic volume and
annihilator theorems. Optional combinatorial isomorphism checks calibrate
the standard knot marking; they are kept separate from the exact geometric
and preferred-longitude calculations. No claim that all canonical two-bridge
triangulations are proper is used: exhaustive branching searches find
singular face matrices for every compatible ordering of several such
triangulations, beginning with 6_2.

## 12. Evaluating singular face contractions before extracting the state

`singular_faces_and_six_two.md` evaluates the same charged kernels using
independent Fourier integration. It assumes rank D=N and a surjective
kernel-to-frequency matrix C; neither assumption is replaced by a presumed
TQFT existence theorem. The resulting normalization is a product of three
explicit Jacobians, and the residual integral is absolutely convergent.
The Stokes identity extends to its allowed shape subspace. Complete
horosphere decorations then identify the geometric critical point and give
a volume theorem for the full reduced tensor under the displayed hypotheses.

For 6_2 a separate exact certificate produces a three-variable selected
meridian fiber, the complete positive algebraic shapes and logarithmic
branches, the preferred-longitude cellular relation, and its entire
angle-dependent tensor-to-fiber phase. Its existence and volume law follow
without inverting the singular face matrix. The boundary factorization is
the type used in AK v2 Conjecture 1(1); it is not the undefined specialization
of the proper FAMED formula. Minimal annihilator existence uses the same
Andersen--Malusà convention as before. The full intrinsic AK conjecture,
including arbitrary triangulation identifications and H-triangulation
limits, has not been proved by this calculation.

## 13. The Fourier rank conditions are automatic for branched knot exteriors

`automatic_face_regularity.md` identifies the exact local linear obstruction
with a cellular ideal edge cocycle. It then proves that the obstruction
vanishes from H^1(M,boundary M)=0 for a knot exterior, using the cohomology
sequence and the boundary meridian generator. This proves rank D=N and
surjectivity of C uniformly, independently of the convergence assertion in
AK's Theorem 7. The completed independent full-tensor volume theorem now
applies to every globally branched complete positive geometric ideal
triangulation of a knot exterior in S^3. The general selected boundary state
and triangulation identifications remain separate obligations.

## 14. Preferred-longitude cochains and the meridian shear

Two further primary sources were located and read in this continuation:

* Kambampati, [arXiv:2610.04103v1](https://arxiv.org/abs/2610.04103v1),
  submitted 2 October 2026, supplies a cochain construction for the preferred
  longitude, including singular face matrices.
* Wong, [arXiv:2512.23198v1](https://arxiv.org/abs/2512.23198v1),
  submitted 29 December 2025, defines generalized FAMED and additional
  longitude--meridian conditions. Its analytic theorems are not premises
  of the new positive-geometry argument.

`preferred_longitude_cochains.md` reconstructs the first source's local face
potentials, derives its auxiliary potentials from endpoint sums, and proves
closure and peripheral period matching on the dual spine. The independent
local audit checks 60 potential/arc identities. A separate integer endpoint
formula, checked in all 1152 ordered arc-pair cases, proves the peripheral
symplectic normalization with the full factor two. The resulting rank and
preferred-longitude relations are proved using these cancellations and
knot-exterior cohomology, rather than adopted from the source's theorem.

`general_boundary_state_and_framing.md` then proves the selected-state volume
law whenever the longitude increases the B rank. It permits a rational
meridian shear, records its exact Gaussian correction and all scalar phases,
and proves volume preservation by a positive-Phi saddle argument. Its exact
operator action is Q -> q^beta Q E^(2beta), E -> E, with no specialization.
The additional zero-shear expectation in Wong's Definition 1.5 is not used.
The other affine-plane case, flat tetrahedra, arbitrary triangulation
identifications and H-triangulation limits remain outside that theorem.

## 15. Inverse Fourier recovery when longitude moves the shape plane

`fourier_boundary_state.md` now treats that other boundary rank, using
the same charged tensor and the same AK level definition. Its Fourier
and Gaussian operators are those in the A=R specialization of Section 6
of Andersen--Kashaev,
[arXiv:1409.1208v1](https://arxiv.org/abs/1409.1208v1). The particular
inverse transform, measure and angle-dependent quadratic level are
specified and independently derived. No new tetrahedral function or
unselected recurrence solution is substituted.

The inverse Fourier integral is absolutely convergent when the longitude
moves the shape plane. Its extra critical equation is the meridian
equation; its real Hessian is negative definite at the complete geometric
point. The full small-peripheral factorization includes an explicit real
level polynomial. In the ordinary-fiber case it recovers the preceding
fiber/Gaussian state exactly. Thus the combined volume theorem and the
independent annihilator argument apply to every globally branched complete
positive geometric ideal knot triangulation. Neither extra condition (2)
nor the zero-shear expectation in Wong's Definition 1.5 is needed for this
tensor-derived realization. Literal equality to a different printed
complex-state formula still requires matching its specified normalization.

An exact six-tetrahedron 5_2 certificate realizes the additional rank case.
Its algebraic shapes, logarithmic branches, preferred-longitude cellular
relation and Fourier constants are independent checks. Optional Regina
calibration verifies the three legal combinatorial 2--3 moves and the
initial marked meridian; this does not assume a quantum state identity
along them. General global triangulation identification, flat tetrahedra,
all-alternating geometric realizations and H-triangulation limits remain
open. This does not claim the full intrinsic AK conjecture.

## 16. Structural period torsors instead of additional knot cases

The current comparison is `structural_literature_delta.md`. It explicitly
marks standard local definitions, independent reconstructions and the
missing global assertion. In particular the cyclic dilogarithm and its
6j interpretation are existing constructions; renaming them is not a
new proof of the conjecture.

`heisenberg_period_torsor.md` derives the cyclic norm equation and its
determinant root as a finite Heisenberg torsor. It evaluates every
finite face contraction by character orthogonality, including composite
levels at which the support is not a free module. Its coisotropic
quotient constructs a boundary torsor on each nondegenerate gluing chart.

`pointed_steinberg_recoupling.md` identifies the local Faddeev difference
module with the pointed Steinberg vacuum at rational b^2. It derives
two generic quantum left-ideal identities, an explicit q-factorial
kernel and its determinant unit, and proves the basis-free pentagon
by coassociativity. No local integral identity is needed for that
algebraic coherence theorem. Published matrix conventions and their
global periods still have to be matched.

`rational_quantum_dilogarithm_torsor.md` independently reconstructs
the existing exact local rational-parameter formula, retaining its
Heisenberg period and branches. Finally `bloch_lift_and_boundary_torsor.md`
proves the rational boundary wedge identity and records the Bloch
period whose regulator is the volume exactly. The target is a
global pointed period carrying that lift and its regulator comparison.
Neither Hilbert 90 for an unpointed module nor fixed-level rigidity
alone supplies the remaining comparison across quantum levels.

The later `pointed_period_descent.md` proves the explicit Racah closure
and its signed shared-face normalization. `affine_frame_period_transport.md`
and `projective_frame_period_torsor.md` give full projective-frame
covariance of those local tensors on a compatible root cover, using
explicit norm-one intertwiners and a determinant rigidity argument
anchored at the identity frame. Their exact audits retain the scalar
before normalization; the inversion diagnostic gives 1084/925. The unit
vacuum is generally transported to a nonconstant vector, so local
pointed recoupling does not by itself select the global literature period.

The comparison also now includes Baseilhac--Benedetti's existing
[matrix dilogarithms](https://arxiv.org/abs/math/0306283) and
[analytic character-cover families](https://arxiv.org/abs/1212.4261v3),
Theorem 1.1 and Section 4.4. The latter already describes the classical
period as a parallel Chern--Simons section. Their global theorems have
not been adopted as premises; their published normalizations, weights
and selected periods must be compared explicitly to ours.

`equivariant_roots_and_phase_descent.md` now constructs the root
multipliers around the knot from the peripheral root characters,
normalizes triangle transports multiplicatively and treats the
remaining scalar pentagon/equivariance discrepancy in relative group
cohomology. The residual phase is evaluated on the relative fundamental
class; it is not removed by field Hilbert 90.

`boundary_regulator_period.md` independently derives the classical
boundary connection and invariant norm, including the centering term
for affine logarithmic edge constraints. It has the ordered-coordinate
form of Baseilhac--Benedetti Section 4.4, equations (56)--(57), while
recording that their longitude/meridian order is reversed from ours;
exchanging that order dualizes the line. It also retains a possible
flat unitary phase twist. Its exact regulator norm does not
prove the remaining quantum comparison for the selected literature state.

## 17. The rational state as an exact relative period

`rational_period_pushforward.md` gives the exact change of variables
from the prescribed rational Gaussian--Faddeev class, with the source
contour, Jacobian, quantum half phases and Q^n factors retained. It
proves multidimensional cubical folding and a unimodular Koszul
reduction, and derives the local gluing residue and its Hessian.
Garoufalidis--Kashaev [1411.6062](https://arxiv.org/abs/1411.6062),
Section 2.1, is the one-dimensional methodological comparison;
its global theorem is not used in higher dimensions.

The source-pole criterion requires positive factors and polar
coorientation; independent argument regulators can be used only with
the corresponding holomorphic period germ. The Faddeev-pair diagnostic
has H=-1 and a nonzero period, so open gluing solutions alone need not
retain the selected period at a special parameter. Its generic moving
gluing residue has a regular value at the removed polar divisor,
verified independently using the defining Phi integrals. The cycle
and that specialization data remain part of the comparison object.
