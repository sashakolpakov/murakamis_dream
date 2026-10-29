# Complex peripheral paths retain the absolute regulator bound

28 October 2026. Complex meridian excursions do not by themselves
invalidate the representation-volume bound on a holomorphic action.
There is an exact endpoint correction, which vanishes when BOTH
meridian endpoints are unitary. Consequently a continuously lifted
path of genuine representations, starting at regulator zero, has the
desired geometric exponential upper bound even if it changes sheets
at complex ramification points or winds logarithms. A bare spectral
node is a different matter. This note proves that distinction; it
does not identify the conversion paths of an actual quantum recurrence.

## 1. Fixed peripheral marking and the exact complex-path identity

Use the actual preferred SL2 peripheral eigenvalues (M,ell) of
[the longitude/action calculation](quantum_longitude_and_regulator_action.md).
Let beta be its absolutely marked fundamental Bloch chain and
R=D(beta)=Vol(rho). The independently proved
[general peripheral representation-volume bound](general_peripheral_representation_volume_bound.md)
gives |R|<=V, where V is the hyperbolic manifold volume.

On any regular representation curve, the actual boundary identity is

    delta beta=-2 M wedge ell.

Write compatible continuously lifted logarithms as

    u=Log M=a+i theta, v=Log ell=b+i phi,
    y=Log Y=2u, Y=M^2.

Here phi is an unwrapped longitude argument, not an independently
reset principal argument. The Bloch--Wigner differential gives

    dR=2(b dtheta-a dphi).                        (1)

Define the holomorphic action increment along a path gamma by

    A_gamma=integral_gamma v dy=2integral_gamma v du.            (2)

Direct real and imaginary differentiation gives

    Im(v dy)=2(b dtheta+phi da)
            =dR+2d(a phi).

Thus the complete endpoint formula is

    Im A_gamma=R(end)-R(start)
                    +2[log|M| Arg(ell)]_(start)^(end).          (3)

Equivalently, for the M-step action S_gamma=integral v du,
Im S_gamma=(R(end)-R(start))/2+[log|M| Arg(ell)]_start^end.
No integral along the complex excursion remains in the correction.

These are the actual root-step constants. For h_Y=2pi i/N,

    (1/N)log|exp(A_gamma/h_Y)|=Im A_gamma/(2pi).                 (4)

The M-step convention h_M=pi i/N gives exactly the same number
using S_gamma. In particular the actual previously derived identity
dS_flat=2v du and Im S_flat=R+2Re(u)Im(v) is precisely (3),
with its absolute constant already fixed by the original Bloch chain.

If both endpoints have |M|=1 and the initial regulator is zero,

    Im A_gamma=R(end),
    (1/N)log|exp(A_gamma/h_Y)|<=V/(2pi).           (5)

This holds for an arbitrary finite complex path of the stated type,
not only a path staying on the meridian unit circle. Without the zero
anchor, the bound from two absolute regulator values is 2V, not V.
Without unit meridian endpoints the term in (3) must be retained.

## 2. Finite character covers and ramification

There is a useful descent statement. Let pi:C->B be a connected
finite cover of normalized peripheral curves on a regular algebraic
open set. On C suppose the actual, single-valued regulator satisfies
dR=pi^*eta, where eta is the differential (1) determined by M,ell.
Then R descends to B.

Proof. On the unramified open set, average R over the d points of
each fiber. The average Rbar is globally defined there, since
monodromy only permutes the summands, and dRbar=eta. Therefore
R-pi^*Rbar is locally constant on C. Removing finitely many points
from the connected normalization leaves it connected, so this
difference is one constant c. Its fiber average is zero, hence c=0.
Thus R=pi^*Rbar. This proof uses the absolute, single-valued R;
it is not a choice of unrelated local action constants.

For a map of irreducible algebraic character/peripheral curves,
remove the finitely many branch and nonproper points to obtain the
finite cover used here. Additional algebraic flag or shape choices
may be included in C. The result does not assert finiteness for a
positive-dimensional family mapping to one peripheral point.
Different disconnected character components over the same B can
still have different additive constants. A common independently
proved zero anchor fixes those constants if its limits are controlled.

At a point of B where M and ell are finite and nonzero, eta is smooth
and closed, so its descended primitive extends across the finite
excluded points. Its absolute volume bound extends by continuity.
In particular, ordinary ramification of the meridian projection on
the NORMALIZED curve creates no jump. In a local coordinate t,
M=M_0+O(t^e), ell=ell_0+O(t), and

    v dy=2 Log(ell(t)) M'(t)/M(t) dt

is holomorphic there. A path entering one meridian sheet and exiting
another through this point is a continuous path on the normalization;
its regulator and endpoint formula remain the same.

Consequently (5) also applies on a genuinely identified normalized
peripheral component with such a finite character/Bloch cover. A
particular character lift need not return to itself after a loop;
the regulator is nevertheless unchanged on the same peripheral fiber
within this connected cover.

## 3. Loops, logarithmic marks, and different kinds of collision

A closed path on the normalized lifted curve based at |M|=1 has
zero imaginary action, even if u or v acquire integer 2pi i shifts.
More generally a meridian loop ending on a different longitude sheet
is NOT a closed path on that curve; its imaginary action is the
regulator difference and still satisfies (5) from a zero anchor.
Repeating such continuations cannot accumulate arbitrary positive
growth, because their regulator increments telescope.

Changing the initial longitude lift by 2pi i n changes A_gamma by
2pi i n(y_end-y_start). Its imaginary part is
2pi n log|Y_end/Y_start|, which vanishes for unit meridian endpoints.
A longitude sign adds i pi(y_end-y_start) and likewise changes only
the real action there. A fixed integral framing ell->M^w ell adds
w(u_end^2-u_start^2), also real at unit meridian endpoints. These
explicit phase changes must be retained in an exact quantum formula,
but they create no exponential norm in (5).

At a nonunit basepoint even a closed representation loop can have
nonzero imaginary action on the logarithmic cover: if the longitude
log winds by 2pi i n, (3) gives 4pi n log|M_base|. Thus a statement
about all loops without the unit-endpoint qualification would be false.

A node of a plane A-polynomial is not the same as ramification of its
normalization. Its two branches can correspond to two DIFFERENT
points of the normalization; they cannot be exchanged by declaring
their identical (M,ell) values to be one point. They can also belong
to different character components or represent different limiting
characters. The normalization and the actual Bloch lift matter.
A true common representation, or matching regulator limits, would
make a passage regulator-continuous; equality of peripheral
eigenvalues alone does not prove that condition.

For a piecewise lifted path whose branches are spliced at nodes,
choose matching longitude logs at each splice and write
J_j=R_after-R_before. Applying (3) on each genuine piece gives

    Im A_total=R_final-R_initial-sum_j J_j
                    +2[log|M| Arg(ell)]_initial^final.          (6)

Thus an unsupported node switch carries exactly the missing regulator
jump. If the logs themselves are reset at a nonunit node, its extra
2log|M| times the argument jump must be included as well. Neither
operation can be omitted by treating a spectral discriminant zero
as a smooth character ramification point.

## 4. The Gaussian conversion has precisely such a node mismatch

For [the independently proved analytic two-channel model](analytic_two_channel_conversion_counterexample.md),
the eigenvalues are alpha(x)=exp(a(x-1/2)) and
beta(x)=exp(-a(x-1/2)+i theta). Give both branches their calibrated
natural primitives at x=0:

    sigma_1(x)=a(x^2-x)/2,
    sigma_2(x)=-a(x^2-x)/2+i theta x.

Both complete marked actions have real part zero. Their logarithmic
eigenvalues coincide at the complex point

    x_*=1/2+i theta/(2a).

However their calibrated primitives do not agree there:

    sigma_2(x_*)-sigma_1(x_*)
       =a/4-theta^2/(4a)+i theta/2
       =Gamma+i theta/2.                         (7)

Following beta from 0 to x_* and then alpha to 1 has exactly this
total action. It is precisely the exponent computed by the exact
Gaussian conversion sum, including its phase.

To compare constants with (2), set Y=exp(2pi i x), M=exp(pi i x)
and A_i=2pi i sigma_i. At x_* the peripheral logs and hence the
boundary term 2log|M| Arg(ell) agree on the two branches. Their
artificial regulator lifts therefore differ by 2pi Gamma. The local
spectral curve is the reducible nodal union
(L-alpha(x))(L-beta(x))=0; its normalization keeps those branches
separate. The conversion is not a continuation through a common
smooth normalized point with one calibrated regulator. This explains
exactly why the general analytic counterexample does not contradict
the genuine geometric path bound.

## 5. Consequence for the actual upper-bound attack

Representation geometry supplies a sharp bound for complex action
paths with a genuine calibrated lift, unit meridian endpoints, and a
zero regulator anchor. Finite covers, ordinary meridian ramification,
and logarithmic winding do not defeat it. This is stronger than
bounding only real meridian arcs.

The unresolved quantum statement is specific: show that every
exponentially relevant sourced conversion is represented by such a
lifted path, or bound its additional node/connection jump by the
corresponding calibrated action difference. The original annihilator's
actual character components, its full source and its subprincipal
couplings must enter that proof. No assertion that a generic analytic
recurrence has this property is made here. Lower noncancellation
remains separate.

[Audit](../experiments/audit_complex_peripheral_action.py) checks the
differential constants, the Gaussian collision mismatch, and complex
Bloch-chart integrals with unit endpoints, nonunit endpoints, and
logarithm-winding loops. These integrals test the identity, not the
existence of a knot representation for an arbitrary one-shape chart.
