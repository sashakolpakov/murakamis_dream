# What a finite algebraic source criterion can certify

29 October 2026. This audits the proposed A-polynomial/gluing-ideal route.
It separates a finite certificate for the ACTUAL hyperbolic value from
the remaining estimate on the original quantum period. It supplies a
specific obstruction using the actual source's value/normal pair, not
a claim that knot A-polynomials never contain enough information.

## 1. A finite classical certificate is available

For a specified actual decorated triangulation/port diagram, the useful
algebraic object is its FULL marked gluing ideal on the regular locus,
saturated by every inverted shape/frame denominator. A peripheral
elimination polynomial alone is weaker. The following are checkable
finite data:

* The actual integer gluing/peripheral incidence and its topological
  fundamental-class marking, including all multiplicities.
* An algebraic complete solution with every positively ordered shape
  in the upper half-plane. Its sign inequalities can be certified by
  real-algebraic isolating intervals, rather than by a fitted shape.
* Full edge rank and the marked peripheral symplectic pairing. The
  [explicit ideal certificate](actual_pretzel_positive_ideal_angle_certificate.md)
  proves these for the actual current cellulation; the general
  [stationarity audit](source_angle_stationarity_critical_audit.md)
  makes the required rank conditions explicit.
* The nonzero marked gluing Jacobian. Positive polarization proves it
  directly after choosing independent edge and marked peripheral
  constraints: if (A B) has full row rank n and its n-dimensional
  row space is real Lagrangian in R^(2n), and
  tau_j=1/(z_j-1), then Im tau_j<0 and
  (A+B diag tau)v=0 would put (v,diag(tau)v) in its complexified
  Lagrangian kernel,
  contradicting sum Im(tau_j)|v_j|^2<0 unless v=0.
* An actual localized inverse between the selected source critical
  scheme and this decorated group/gluing scheme, retaining the
  original meridian, preferred longitude, flags and central signs.

These certify an etale geometric germ and identify the selected
regular critical representation there. They are stronger than finding
the same peripheral polynomial or matching a cusp derivative.

At a positive full gluing solution, the coisotropic identity gives
the volume derivative for EVERY affine angle tangent:

    dV=(1/2)sum_i(Re V_i dIm U_i-Re U_i dIm V_i).

At a complete point this vanishes on the whole edge-angle domain. At
a filled point, Re(a_i U_i+b_i V_i)=0 makes it vanish on the FULL
fixed-slope-angle domain. Strict concavity makes that positive point
the unique global maximum, including against boundary points. Thus
these data identify V_source with hyperbolic volume once the marked
source action is calibrated on the same branch.

The exponentiated filling equation is not enough: the actual primitive
period must be +/-2pi i, not zero or a higher multiple. The
[general geometric completion](general_source_regulator_hyperbolic_equality.md)
proves the needed degree-one statement from the bounded near-complete
framed representation and these small log periods. Its equivariant
construction avoids a universal ideal-triangulation existence premise.
When an angle presentation is used, its positive chart must be supplied
separately; a topological triangulation alone is not that certificate.

## 2. Why A or a localized quantum module does not specify the actual source

There is an exact example INSIDE the existing original-source theory.
Let F_N(Y) be the actual reduced meridian period and put

    f_N(Y)=(1-Y)F_N(Y).

This is the normalized actual function used in
[the whole Newton source transform](newton_actual_source_canonical_transform.md).
Both are meromorphic sections of gauge-equivalent q-difference modules
over the localized meridian field. If P=sum a_k(q,Y)T^k annihilates F,
Tg(Y)=g(QY), then

    P_f=(1-Y)P(1-Y)^(-1)

has coefficients a_k(q,Y)(1-Y)/(1-Q^kY) and annihilates f. Away from
Y=1 its classical symbol is EXACTLY the same as P's. Clearing and
saturating apparent meridian factors does not restore the source row.

Nevertheless at the complete physical point

    f_N(1)=0,
    -partial_Y f_N(1)=F_N(1)=K_N.                       (1)

For the actual figure-eight, the already proved exact K_N=sum_r|F_r|^2
is positive at every level. Thus the full nonzero geometric growth is
in the NORMAL coefficient in(1), while the value is identically zero.
This is not two different knot invariants with the same A-polynomial.
It proves the narrower necessary statement: the same localized
peripheral curve/module does not tell one which actual value or normal
functional computes the original invariant.

A criterion must therefore retain the integral pointed lattice and
its specified normal co-source, not just a meromorphic gauge class or
a saturated classical ideal. Regular-singular language on a punctured
meridian disk does not by itself restore this lost lattice datum.
The bounded-normal-factorial theorem gives estimates for prescribed
jets of explicit kernels; it does not choose which jet the source uses.

There is a second independent loss. The peripheral differential fixes
an action only up to a meridian-independent constant. Bloch lifts of
the same boundary wedge can differ by a closed Bloch class with
nonzero regulator. The
[Bloch-period audit](bloch_lift_and_boundary_torsor.md), sections3--4,
shows precisely why the actual fundamental-class lift and complete
volume anchor must accompany the A-curve. They are not recovered from
the peripheral equation's Jacobian or degree.

## 3. Exact algebraic support does not yet give the whole quantum estimate

The [actual coefficient normal-period theorem](actual_geometric_normal_period.md)
proves a nonzero local formal geometric normal block and a formally
unit gauge to the calibrated geometric line. It explicitly leaves the
two framing modes and their original relative pushforward unevaluated.
The algebraic local ring and nonsingular Hessian are therefore real
progress, but they do not prove that the original whole period retains
that block.

This is visible in an exact endpoint calculation, rather than a generic
appeal to Stokes phenomena. The
[sourced telescoping audit](sourced_telescoping_geometric_support_criterion.md),
section5, has for the actual relative interval

    J_v(S_eta f)=exp(-v)J_v(f)
       +exp(-v)[integral_1^(1+eta)-integral_0^eta]
                                      exp(vt/eta)f(t)dt.

Already f=1 excludes the naive homogeneous shift-covariant replacement.
The endpoint source must be transported or canceled exactly. A proof
of interior ideal equality cannot delete this term by saturation.

Similarly, the [saturated critical compactification](saturated_critical_regulator_compactification.md)
bounds all TRUE full critical limits, but explicitly does not put every
endpoint of the original relative cycle into that closure. Its exact
Pachner counterexample shows cleared equations can create false boundary
volume; full saturation removes that false component, not an arbitrary
physical boundary current.

The [algebraic-clock conversion example](algebraic_clock_conversion_counterexample.md)
also warns against replacing whole transport by selected principal
root actions: a polynomial offdiagonal perturbation changes the leading
exponential rate despite nonzero distinct roots and bounded eigenframes.
It is not a knot operator or a counterexample to a knot-specific theorem.
It rules out deriving the needed propagation solely from that generic
algebraic/spectral regularity.

Thus a DECORATED POINTED quantum module could in principle supply the
missing source theorem, but it must supply more than its regular local
ring: actual normal evaluation, relative boundary/shift covariance,
and a quantitative nonzero geometric pushforward. No impossibility
theorem for such a source-specific algebraic construction is asserted.

The [general original-source filling transfer](general_original_source_long_filling_transfer.md)
provides one concrete successful bridge from base data: an exact even
complex color packet, global complementary source gap, marked actual
representation and calibrated action imply full nonzero long-filling
asymptotics. Those analytic base estimates have been proved for the
current explicit source class, not for every ideal satisfying the
classical tests in section1. This distinction keeps the active broader
equality objective from being replaced by a principal-curve criterion.
