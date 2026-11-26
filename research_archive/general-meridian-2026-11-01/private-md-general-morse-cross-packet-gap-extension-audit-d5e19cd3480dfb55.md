# Independent audit: CROSS H1 and global H2 on a certified general Morse source

31 October 2026. Full dependency review by the coherent-source reviewer.
This audit separates the all-CROSS estimates from the old full-numerator
restoration. The latter is not an input to either conclusion below.

## Precise source and geometric hypotheses

Use `notes/research_matched_sphere_morse_source.md` to realize the fixed
matched spherical cellulation as an actual original Morse source. For
this analytic extension assume the chosen white triangulation is SIMPLE
and has the existing labeled nondegenerate positive certificate. Mark
an original MAIN edge uv. There are R ports, R+2 faces, R ordinary
variables, and exactly their original degree d=N−1 targets. The diagram
and its finite Morse presentation are fixed before N tends to infinity.
No prescribed bridge width or constant intermediate headcount is assumed.

The finite source-realization theorem allows more general multigraphs.
The present analytic statement does not silently extend to all of them.
Simplicity is used below both for the allowed protected zero patterns
and for connectivity of the ordinary phase graph. A separate theorem
constructing this certificate for a selected simple diagonal choice may
of course discharge the geometric hypothesis.

Write C_N for the sign-adjusted actual all-CROSS coefficient and
C_N^raw=(-1)^(dR)C_N. Let sigma_e=−2cos(2pi delta_e).

## 1. Exact local factor inputs have no Morse-width dependence

The original cofactor factorization, ordinary/protected middle relative
packets, and interpolant rigidity operate on one ordered quartet
(x,b,c,y), retaining all its starting rows and the actual even/odd
central factor. The finite local polynomial in the new source is
literally the same H_V, by the new compiler; no local identity is being
transported through a projected sector.

Because uv is MAIN and the white triangulation is simple, a matching
edge cannot have both protected endpoints. Thus x+y>0 at every port.
Each local triangle has only the already covered zero patterns. A
triangle with one positive variable is the retained exact monomial,
not a nonexistent local saddle. On the fixed compact of nonzero
complete radii all local constants can be chosen uniformly over the
finitely many ports. Both parity grids and terminal row shifts remain
exactly those in the local proofs.

The independently proved local theorem is therefore, on one fixed
complex face and spectral neighborhood,

    P_cross,e=N² Bcal_e,N(1+O(exp(−kappa N))).           (A1)

Here Bcal keeps the exact maximal-fold anchor, forced product, beta,
parity offset and half-index. It has a holomorphic logarithm with the
same limiting triangle action Q_b+Q_c. This is the result of
`actual_cross_cofactor_interpolant_rigidity.md`, using the local
`actual_positive_face_exponential_fold_interpolation.md`, not an
interpolation of unproved off-node data.

## 2. The global angular and Hessian arguments use only the sphere

The cofactor global angular theorem is also local. When two supported
face phases in a triangle are separated it gives a strict exponential
loss uniformly over the entire real spectral interval and a fixed
thin complex strip. The actual terminal cofactors satisfy this with
their omitted-node corrections. Every other cofactor has its global
polynomial endpoint majorant; the finite central products introduce
only polynomial losses. No off-node PSD or coefficientwise strict
comparison is assumed.

Deleting u and v from a simple triangulated sphere leaves a connected
graph. The elementary proof used in the rank/coefficient notes reroutes
a path around u along its cyclic link, then around v along its link
with u removed. Each surviving edge lies in an actual triangle with
two ordinary vertices. Consequently a nonconstant ordinary phase has
a separated supported pair in some triangle. After fixing one ordinary
phase, the source Cauchy integrand has a strict angular complement
gap. Its only zero phase is the common rotation; the edge differences
are primitive +1,−1 rows, so no angular alias is introduced.

Exactly the same incidence argument and the actual positive determinant
pair-trace bounds give a positive definite face Hessian on the R−1
dimensional scale quotient. The finite coefficient proof in
`actual_positive_face_coefficient_saddle.md`, sections 2–4, uses the
positive complete radii, the actual angle-force equation at each
ordinary circle, and this connected phase graph. Its proof does not
use a sweep, a flat gap forest, or a uniform count of physical heads.
Its complete exponential anchor is Phi=Vol(Y)/(2pi) from the labeled
two-ball geometry.

## 3. H1: the original all-CROSS Cauchy torus supplies the local packet

Use the same fixed common-scale gauge and define

    Psi_N(z,delta)=N^−1 sum_e Log Bcal_e,N(delta_e;L(z))
                   −(d/N)sum_ordinary Log L_f(z).

All finite anchors remain in this phase. The new finite source theorem
gives exactly this target and its measure: removing the simultaneous
phase costs the factor1 and leaves (2pi)^−(R−1)dtheta. There is no
additional grid, mark, turn, or N factor.

Uniform local convergence with derivatives and the positive complete
Hessian give the same holomorphic finite saddle z_N(delta), its action
A_N, and face Hessian H_N. Deform the original Laurent coefficient
torus in its annulus; the local side faces are in the angular gap.
Equation (A1) and the original complex Gaussian estimate therefore give

    C_N^raw(delta)=(-1)^(dR) N^(2R) exp(N A_N(delta))
      /[(2pi N)^((R−1)/2) sqrt(det H_N(delta))]
       *[1+O(N^−1)].                                  (H1)

This is exactly sections 1–3 of
`general_full_spectral_numerator_geometric_packet.md`. Its section 4,
which restores the FULL numerator by a previous noncross estimate,
is expressly NOT used. The error is relative on one fixed complex
polydisk; all fixed derivatives are controlled on smaller polydisks.
The actual source saddle coefficient is nonzero.

Reality and separate evenness of the exact interpolation imply the
same properties of A_N. Its limit is the original critical face action
A_0, with A_0(0)=Phi. Since each port has at least one nonmonomial
triangle, the local constant C_e=pi(T_b+T_c)/(x+y)>0. Thus
A_0''(0)=−2diag(C_e), and shrinking the fixed neighborhood makes
Re A_N'' uniformly negative definite for large N. No half twist is
included here twice: this untwisted numerator action is A_0; the
retained half twists are added only by the original n=epsilon−2p
Gaussian decomposition.

## 4. H2: the whole real spectral complement is unchanged

`actual_global_cross_spectral_gap.md`, sections 1–3, bounds a single
cofactor's all-start sum using the signed normalized transfer and the
uniform logarithmic prefix upper. Its exact upper action is

    max{Q_b(delta), (1/2)log b},

with the second branch absent when b=0. It decreases strictly away
from delta0 unless that triangle is the literal monomial b=xy=0.
At least one triangle at each actual port is nonmonomial: if both
outers are positive then xy>0; if one is protected, the other
protected face can remove at most one of the two distinct middles.
Thus every separated spectral coordinate gives a fixed local loss.
The exact central even/odd sums keep both triangles in each term and
cost only bounded-degree or polynomial factors.

Outside the common ordinary phase neighborhood, section 2 of this
audit gives the global angular gap uniformly in ALL real spectra.
Inside that neighborhood, the local slow-transfer proof supplies its
fixed complex-face extension, so one separated spectral port gives
a strict loss while every other port stays below its endpoint rate
plus an arbitrarily small prescribed error. There are finitely many
ports; shrink the error and common strip so their total is smaller
than the loss. All targets are still shared and the common phase
cancels by total degree.

Consequently, for every eta>0 there are tau,gamma>0 such that

    |C_N^raw(delta)| <= exp[N(Phi−gamma)]              (H2)

for all large N, max|Re delta_e|>=eta in the centered real cube and
|Im delta_e|<=tau. Every fixed derivative has the same strict rate
on a smaller strip. This is exactly the original shared coefficient
sewing in section 4 of the global CROSS theorem. It is not a product
of independently optimized local norms or a coefficientwise strict
estimate for the full numerator.

## 5. Conclusion and explicitly excluded dependency

FULL independent dependency PASS for H1 and H2 on the new certified
simple-white general Morse source. No dependency used here requires
a fixed flat-plat width: all constants depend on the fixed finite
graph, its complete radii and its zero patterns. The variable number
of heads has already disappeared through the exact source compiler.

The whole all-CROSS Fourier theorem is consequently available from
these two inputs and the independently audited general-Morse action.
For the FULL original invariant, the new global NC gap must separately
restore the numerator and its exterior spectral estimate. No old
Fejér identity smoothing, pure-middle forest, or flat-plat full-packet
restoration is included in this audit. No new numerical test is
required for this proof-level dependency extension.
