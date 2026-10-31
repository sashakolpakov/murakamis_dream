# The original boundary source has exactly two flat face directions

30 October 2026. On the labeled original
right-angled matching graph, the finite boundary models detect every
homogeneous magnetic direction except two explicit face potentials.
Two neighboring original physical heads give a primitive slice for those
directions. This statement includes the closed source and the common
fixed-charge two-cut lattice; arbitrary routed extra factors are excluded.

Together with the separate local curvature estimates, the result gives a
uniformly invertible transverse Hessian for the actual nonzero ROOT source
product at the resonant boundary sample, in a shrinking folded-channel
window. It does NOT say that this sample is stationary, perform a Gaussian
contraction, or assign a coefficient in the original relative period.

## 1. The literal graph and its homogeneous lattice

Use the labeled certificate and original reference meridian of the
[common boundary chart](actual_original_network_resonant_boundary_chart.md).
Let Delta be its plane cubic graph, with R matching edges D and 2R
vertices. The [full original source](general_matching_graph_full_normal_source.md),
section 2, identifies this SAME graph with the actual W/pi contraction:
matching edges carry V_(2a_i), and all other edges carry V_d, d=N-1.
Cups, caps, reversals, and the cyclic order at every vertex are retained.
No new routing braid is inserted.

For an oriented typed edge of highest weight L_e center its head by
z_e=h_e-L_e/2. The actual degree equation at each vertex is exactly

    sum_out z_e-sum_in z_e=0.                            (1)

Changing an edge orientation replaces z_e by -z_e. A literal cup or cap
replaces h by L_e-h, which makes precisely this sign change in centered
variations. Thus degree-two bends can be contracted without changing the
integral HOMOGENEOUS lattice. Half-integral centered basepoints when L_e
is odd do not change that lattice: its variations remain integral.

For fixed channel labels, the retained half twist multiplies the original
circle term by its exact scalar omega_a^epsilon. The full-source identity
already includes the physical reversal in pi. Consequently half twists
do not add a magnetic constraint, remove a graph edge, or add a free
magnetic variable to (1). Their scalar phases remain in the source.

Write B for the oriented incidence matrix of Delta. Its homogeneous
lattice is

    V_Z=ker_Z B,  dim_C V=|E|-|V|+1=R+1.                (2)

The certificate makes Delta connected. Its white faces are the actual
projection regions, not freely identified copies of developed faces.
There are R+2 of them. Let P_f be one additive potential per white face,
modulo a common additive constant. Assign to an oriented edge the difference
of its left and right face potentials, with the sign chosen to agree with
(1). This gives an integral isomorphism

    Z^(white faces)/Z(1,...,1)  = V_Z.                   (3)

Here is an elementary proof of surjectivity, including primitivity.
Given an integral divergence-free edge assignment, integrate it along
paths in the dual graph from a fixed face. Around a dual face, the sum
is the original vertex divergence, hence zero. Every closed dual walk
on the sphere is a sum of these oriented face boundaries; cutting it
at repetitions and filling its simple components proves this directly.
The potential is therefore well defined and integral. Its only ambiguity
is the initial constant. Conversely differences have zero divergence
because the consecutive faces around a vertex telescope. This proves (3)
over the integers, not only by a dimension count.

At an ordered shaded triangle with white regions (f0,f1,f2), the physical
variations are, up to the fixed orientation,

    P_f0-P_f1, P_f1-P_f2,

and the auxiliary variation is their sum P_f0-P_f2. This is also the
differential of the actual prefix clocks X=-L_f0/L_f1, Y=-L_f1/L_f2.
For a literal dual white, its heads are (d-j,d-i), so the two physical
variations are reversed and negated and the auxiliary variation is
negated. No dual row is incorrectly identified with the physical row.

## 2. The exact finite-clock rank

In the common reference normalization, precisely two white faces contain
the marked ideal vertex p: call them u,v. Their prefixes have zero
lower-left entry. Every other white face has strictly positive normal
coefficient and a quadratic prefix diagonal. This follows from the
strict supporting inequalities of the labeled certificate. A right-angled
ideal vertex has exactly two incident white and two incident shaded faces.

The [white-normal polyhedron](actual_right_angled_selected_framing_obstruction.md),
sections 2--3, is a convex three-dimensional polyhedron C whose vertices
are these white faces and whose facets are the original shaded triangles.
Its boundary is a triangulated sphere. An edge of C corresponds to an
edge of Delta; u,v are joined by the original marked MAIN edge e0.

Define L on (3) from each literal numerator by the following head rows:

| Numerator type | Rows of L |
| --- | --- |
| 200, 002 | none |
| 220 | first physical variation |
| 022 | second physical variation |
| 202 | sum of the two physical variations |
| 222 | both physical variations |

Pull these rows back through the actual dual reversal when the numerator
is in pi. Row signs or invertible local changes of these rows do not
change their common kernel. All six types, including 202/202 pairs,
are allowed. No exclusion at rectangle parameter c=1 is made.

The equations L P=0 say exactly that every pair of QUADRATIC white-face
potentials belonging to one shaded triangle is equal. The induced graph
on all vertices of C other than u,v is connected. To prove this without
an external connectivity theorem, start with any path in the connected
1-skeleton. Remove occurrences of u by rerouting through its cyclic
vertex link. In the resulting graph, occurrences of v can be rerouted
through its link with u removed. This link is a cycle or a path and is
connected. The replacement never returns to u. Thus any two surviving
vertices remain joined.

Every surviving edge is in a shaded triangle and its endpoints are both
quadratic, so its equality is among the equations of L. Consequently all
quadratic-face potentials coincide. After subtracting that common value,

    ker L={P_u,P_v arbitrary; P_f=0 for f!=u,v},
    dim ker L=2,  rank L=R-1.                           (4)

This is a theorem about independent original source variables. It does
not extend the critical-scheme/representation inverse off criticality.

The two directions are precisely the LIMITING geometric framing tangents.
At r=N rho the quadratic prefix logarithms have common varying part
2 Log rho-Log s. Write the two constant prefixes as
e_u(1+z_u s), e_v(1+z_v s). The original marked primitive meridian makes
z_u-z_v=+1 or -1: in the reference convention these are I and -J or its
recorded reciprocal. After subtracting one quadratic face potential,
the two remaining variable parts are

    P_u=-2 Log rho+Log s+Log(1+z_u s),
    P_v=-2 Log rho+Log s+Log(1+z_v s).                   (4a)

The exact constant signs, face coefficients, and common 2 Log N are
retained additive constants and disappear only on differentiation.
The Jacobian of (4a) in (Log rho,s) has determinant

    2(z_u-z_v)/[(1+z_u s)(1+z_v s)] != 0.               (4b)

It and its inverse are uniformly bounded on the specified compact chart.
Thus these two complete-geometry tangent directions span (4). This is
not a stationarity claim for the actual finite auxiliary labels.

## 3. A neighboring physical-head slice is primitive

The marked main edge e0 separates u,v, so its homogeneous head is
P_u-P_v up to sign. Choose either shaded triangle adjacent to e0 and
let w be its third white vertex. It is different from u,v and hence
quadratic. Each shaded triangle has exactly one matching edge and two
main edges. Since e0 is main, exactly one of its other two edges is also
MAIN. Call that edge e1. It joins w to u or to v.

On ker L, the two actual head functionals at e0,e1 therefore have matrix,
up to the recorded row and column signs,

    [[1,-1],[1,0]]  or  [[1,-1],[0,1]].                 (5)

Their determinant is +1 or -1. Thus fixing these two actual physical
heads removes exactly the two flat directions, with a primitive,
diagram-independent integer minor. This chooses source integration
coordinates; it does NOT authorize a new single-port co-source, move an
observable through a braid, or claim that e1 is first in an existing
Morse slice.

The slice W={head_e0=head_e1=0} in homogeneous variations has dimension
R-1, and L|_W is injective. Because the diagram is fixed, choose an
integral basis of W once. In that basis its smallest singular value is
a positive diagram-dependent constant, independent of N and the frame.
Alternatively fixing the two constant-face potentials directly is a
primitive complementary slice with the same conclusion.

An arbitrary second physical head need not work. If both its adjacent
white faces are quadratic, its restriction to ker L is zero. In general
the exact test is the rank of the two cut-head rows restricted to (4).
The corresponding kernel dimension after fixing the heads is 2 minus
that rank. No generic-cut transversality is silently assumed.

## 4. Closed, marked-open, and fixed-charge two-cut sources

For the original marked source, equality of the two exposed heads is the
permitted WHOLE-SOURCE consequence of integer degree conservation. It is
not a local replacement of the unrestricted mark by an invariant cap.
After that equality, restoring the exposed edge gives exactly (2), with
its actual marked scalar weight still attached. The marked-open chart
including the one free exposed head therefore has the same homogeneous
space V. Fixing that head imposes its one displayed linear functional.

For two cuts on DISTINCT original edges use the actual port orientations
of the [common charged chart](actual_matching_graph_common_band_ward_current.md):
the heads are (a,a+delta) and (l,l+delta). At a FIXED charge delta, subtract
one recorded affine particular solution. Variations then have equal
heads across each cut and restore exactly a cycle flow on Delta. Thus,
when a,l are included as coordinates, the homogeneous space is again V
and (4) applies unchanged. Fixing a,l gives the slice obtained by setting
their two cut-head functionals to zero, so (5) is the promised sufficient
condition for a full transverse slice.

The deleted graph is connected for two distinct edges of this certified
Delta. Indeed it is the dual of the triangulated sphere boundary of C.
If deleting at most two dual edges disconnected its triangles, the
boundary between a nonempty proper set of triangles and its complement
would be a nonempty edge cycle with at most two edges. A simplicial sphere
has no such cycle. This also proves that a single original edge is not a
bridge. If two cut positions lie on the SAME edge, or a routed source
uses a different graph, retain the component conditions of the common
charged-chart theorem instead; the preceding conclusion need not apply.

Varying delta itself adds an affine relative-boundary direction. It is not
a closed cycle flow and is NOT counted as a third flat framing variable
by (4). The neighboring-band quotient fixes delta to +1 or -1 after its
single analytic interpolation. The two physical support cycles still
differ; (3)--(5) do not identify them or erase an endpoint current.

## 5. Assembly of the finite transverse curvature bounds

This section uses the separately proved local estimates in
[the finite boundary curvature theorem](actual_q_hahn_boundary_model_curvature.md).
Retain the exact models of the
[correlated-band theorem](actual_correlated_boundary_band_ratio.md),
their scalar phases, the literal pi reversal, and every cup and mark.
The statement concerns the original uncontracted root product. It does
not include the nonlinear binomial co-source or replace its actual weight.

Use logarithmic face coordinates, so a physical clock is multiplied by
exp(P_f-P_g). Equivalently the finite head changes by
N(P_f-P_g)/(2pi i); the integral lattice in sections 1--4 is the same
after this fixed scalar normalization. At the real limiting boundary
clocks, the local 220/022 scalar curvature, 202 positive-total curvature,
and 222 two-variable curvature are bounded below by cN and above by CN
on their displayed rows of L. Their non-affine phases have already been
retained in the local source formulas; the positive reference Hessians
are taken in the corresponding real logarithmic clock coordinates.

Thus their sum is a real symmetric matrix H0_N with

    cN ||L P||^2 <= P^T H0_N P <= CN ||L P||^2          (6)

for real P, with a fixed finite number of local rows. Sign changes from
022 or the literal dual are included in L. In a fixed basis of the
primitive slice W of section 3, (6) gives

    c_D N I <= H0_N|_W <= C_D N I.                     (7)

Now retain the exact finite-r clocks at r=N rho. Their relative errors
from the finite nonzero limiting clocks are O(1/N). The uniform complex
logarithmic derivative bounds through order three in the local curvature
theorem make their Hessian correction O(1). The 200/002 zero-free Bessel
factors have O(1) Hessian on the common compact neighborhood; their
endpoint-product corrections have Hessian O(1/N). Linear head monomials
and all fixed channel scalars contribute zero Hessian.

Let S=sum_i(d-2a_i). The retained 202/222 partner products and auxiliary
root cups have Hessian O(S), since their factors are uniformly separated
from zero. Mixed-type cup/partner residuals are smaller after their
linear monomials are removed. These are estimates of the actual root
identities; no root reflection or partner collision is differentiated
as a generic-q identity. Physical cup/cap characters are linear.

The nonzero actual product and finite model satisfy a relative O(1/N)
estimate on a fixed source polydisc. Cauchy's formula gives an O(1/N)
Hessian error for their local logarithms. Consequently the actual root
source Hessian H_N at the boundary sample satisfies, on W,

    ||H_N-H0_N|| <= C_D(1+S).                          (8)

For S=o(N), (7),(8) imply invertibility and

    ||(H_N|_W)^-1|| <= C_D/N.                          (9)

This is a complex Hessian statement; positivity is asserted for the
reference matrix H0_N, not for an arbitrarily perturbed complex point.
All constants are uniform in the stated alpha/rho compacts and through
both maximal-fold parities. The shrinking s-window is an INTERNAL
channel window, not the external auxiliary-color h-window needed for
the eventual filling theorem. Genuine q normals are not estimated by
(8),(9).

## 6. What this does not yet prove

The complete geometric framing sample is not automatically stationary
for the finite labels a_i. Even at the folded limit the actual linear
source characters and retained Poisson sector must be checked against
the boundary action before invoking a stationary reduction. A Hessian
bound alone does not bound the gradient or the displacement of a nearby
critical point. The binomial base localization, transverse amplitude,
Jacobian, square-root branch and common descending cycle would all have
to be retained in a Gaussian theorem.

The exact critical-scheme inverse remains a statement on the critical
representation germ. No off-critical flat representations were used
to obtain (4) or (9). In particular a generic unframed perturbation of a
zero lower-left prefix is not assigned the same scale as a primitive
source-head perturbation.

Finally, selecting the primitive neighboring-head slice does not expose
those heads as two first slots without additional source algebra. The
original relative cotangent periods, their support/carry boundaries,
the global nonzero coefficient and the mixed-color/alias estimates
remain separate. No hyperbolic-volume equality follows here.

## 7. Focused audit and scope

The [focused audit](../experiments/audit_actual_original_boundary_transverse_rank.py)
and [results](../experiments/actual_original_boundary_transverse_rank_results.json)
pass 56 exact rank cases, 1136 ordered triangle/dual checks, 224 oriented
chain maps, 112 primitive neighboring slices, 336 fixed-charge affine
restorations, 56 deliberately nontransverse cut witnesses, and 56 cup/cap
subdivisions. Original finite tensors at both parities separately check
5732 degree entries, 42 retained half-twist sectors and 540 cup/cap entries.
Five exact prefix/frame identities include (4b). The actual cube and
octahedral combinatorics are distinguished from supplemental combinatorial
sphere regressions; the latter certify no additional geometric realization.
The local curvature theorem has its own source-matrix audit. No numerical
knot list replaces the class-wide proof.

The transverse-rank theorem does not identify a stationary point, first-slot routing, Gaussian contraction or relative-period coefficient.

The rank calculation does not establish a stationary sector, a descending cycle or a nonzero original period.