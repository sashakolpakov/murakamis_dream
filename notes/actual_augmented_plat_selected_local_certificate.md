# A finite certificate for the selected geometric principal phase

**Subsequent scope result (30 October):** the
[right-angled obstruction and localization](actual_right_angled_selected_framing_obstruction.md)
proves that no common all-central selected frame exists for the actual
certified right-angled plat cut. Generic geometric strip flags have exactly
two strict physical-support failures, at arbitrary bridge width. The local
conditional statements below remain valid; their simultaneous realization
in that right-angled class cannot supply the general proof.

30 October 2026. For any fixed augmented plat, of arbitrary width, this
note gives explicit tests which identify the geometric stationary
branch with the source-selected LOCAL q-Hahn principal action. It also
expresses the endpoint sheet test as a condition on the two common
framing flags. No intersection with the original finite summation
cycle is inferred.

The certificate has not been shown to exist for every positive
geometric augmented plat. Its point is to replace an unspecified
local branch-identification assumption by finite tests on the actual
marked representation, with all input/output signs retained.

## 1. Data and the selected-critical certificate

Fix the actual augmented-plat Morse word, retained half twists, and
primitive peripheral marks. Supply:

1. An actual marked positive complete gluing certificate, as in
   [the geometric certificate theorem](general_marked_positive_gluing_certificate.md).
   It gives the geometric representation, not an unrelated component
   of the character equations.
2. ONE rank-one projector Pi satisfying all the regular-chart,
   central-support and cup/cap tests of
   [the physical framing criterion](actual_augmented_plat_physical_framing_criterion.md).
   These include the original affine degree equations with the
   canonical wire logarithms and the actual low/high adapters.
3. The actual magnetic multiplier at each ordinary column factor.
   At an input it is Y_geo=S_1/S_2; at an output it is
   Y_geo=S_2/S_1. The momenta S are reconstructed from the original
   prefix matrices, not chosen separately to make a test pass.
4. The selected-root test in section 2 at every input and output,
   and the original logarithmic/Poisson characters of the full marked
   phase. The latter are retained as part of the certificate, rather
   than erased after exponentiation.

These conditions imply the following LOCAL conclusion. The actual
geometric critical germ is a germ of the source-selected principal
phase. Modulo its two framing directions its magnetic Hessian is
nondegenerate. Its fully marked critical action phi has

    d(2pi i phi)=1/2 sum V_i dU_i,
    2pi Re phi(0)=Vol(Y_D),
    phi_(chi_i chi_j)(0)=pi i tau_i delta_(ij),          (1)

with U_i=-2pi i chi_i and the original primitive cusp shapes tau_i.
Its ordinary q-Hahn column amplitude factors are nonzero.

The conclusion concerns the actual marked phase and its ordinary
column factors. It is NOT a full-source amplitude theorem, a bound
for generic normal currents, a continuation of the finite discrete
channel, or a claim that the original cycle contributes at this germ.

## 2. The local sheet test is algebraic on the marked cover

Use the actual low coordinates tau,nu of each column, after applying
the high adapter when required. Put

    xi=1/2, zeta=exp[pi i(tau-2nu)], c=-cos(pi tau),
    W=1+2c zeta, V=1+2c zeta+zeta^2.                   (2)

Here W is a scalar, not a prefix matrix. In the central domain
Re c>0, Re zeta>0. Both W/zeta and V/zeta have positive real part;
hence W and V avoid the nonpositive real axis. In particular the
principal square root of W has strictly positive real part.

The [joint original-kernel theorem](actual_q_hahn_joint_complex_amplitude.md),
section 7, gives the source-selected multiplier

    Y_sel=(zeta+i sqrt(W))^2/V.                         (3)

For the actual geometric multiplier define

    r_geo=[V Y_geo-zeta^2+W]/(2i zeta).                 (4)

The actual Casimir characteristic equation says r_geo^2=W. Therefore

    Y_geo=Y_sel  if and only if  Re r_geo>0.             (5)

This is an equality test for the selected root, not just a test that
both values solve the characteristic polynomial. The source theorem
fixes the square root by its actual center phase and finite-source
continuation.

All expressions in (2)--(5) are algebraic after retaining the marked
square root of T=exp(2pi i tau). Its argument is pi Re tau in
(pi/2,pi), which fixes the square-root sign; zeta=T^(1/2)/U with
U=exp(2pi i nu). Thus for an algebraic marked representation and
projector the endpoint root test is a finite real-algebraic test.
The logarithmic characters of the action remain additional marked
data, not a consequence of squaring (4).

## 3. Exact flag formulas, including the output sign and high adapter

Normalize one actual incoming pair to

    A=-[[1,1],[0,1]], B=-[[1,0],[-4,1]],
    P=B A, H=P+I.

Write Pi=v ell, ell(v)=1. In these disk coordinates let w be the
kernel flag of ell and let z be the image flag W_prefix v. This use
of the actual prefix is essential. Normalize the local rank-one
matrix W_prefix Pi by its trace; it has image z and kernel w.

In affine coordinates a representative of the local common frame is

    g=[[1,-w],[1,-z]].

Direct substitution into the ORIGINAL head and prefix formulas gives

    U_phys=(z-w)/(z-w+1),
    T_phys=(z-w)/(4wz+3w+z+1),
    S_1/S_2=-w/(z+1).                                  (6)

The source internal root in a low column is obtained from the actual
inverse, at J=-1,

    Z=-U[y(T-U)+(1-U)]/[-y(T-U)+T(1-U)].                (7)

For the input use y=S_1/S_2; for the output use its RECIPROCAL.
Equations (6),(7) give

    Z_in,low=(2w+1)/(2w-1),
    Z_out,low=(2z+1)/(2z+3).                            (8)

For the high adapter one must first replace

    T_low=T_phys^(-1), U_low=U_phys/T_phys.

Keeping the same actual input/output momentum convention in (7)
then gives

    Z_in,high=-(2z+1)/(2z+3),
    Z_out,high=-(2w+1)/(2w-1).                          (9)

These are rational identities, not deductions from a root-only
symmetry. They retain the output sign of a kernel and the actual
high-degree translation.

## 4. The endpoint selected sheets are oriented disk sides

For any strict central triple, its two local framing flags z,w are
on the SAME open side of the real disk circle, by section 5 of the
physical framing criterion. The two roots of the local characteristic
give the two opposite choices of that side.

One can see the latter directly from (6). Fix U_phys,T_phys and put
d=U_phys/(1-U_phys)=z-w. The equation for w is quadratic; its roots
have sum -(d+1). Consequently its two flag pairs are related by

    (z,w) -> (-w-1,-z-1).                              (10)

They therefore lie on opposite sides of the real circle. There is
no collision or boundary crossing in the central domain. For example
T+1-U cannot vanish there: arg T is in (pi,2pi), arg(1+T) is strictly
between arg T and 2pi, while the strict physical U argument lies
between 0 and arg T. The other regular root denominators are excluded
by the regular-chart assumptions. The simple characteristic and the
connected central domain preserve the two sheet labels.

At a strict physical real point, the actual selected internal root
Z is in the upper half of the unit disk, as proved by the original
q-Hahn selection theorem. Equation (8) then gives w below the real
circle for an input, and z above it for an output. Equation (9)
gives the SAME respective side choices in the high adapter. Together
with the same-side necessity, continuation through the central domain
therefore proves the equivalent tests

    selected input  <=> Im z<0 and Im w<0,
    selected output <=> Im z>0 and Im w>0,              (11)

where each line uses that factor's OWN actual disk normalization.
The inequalities in (11), rather than an upper-half-disk assertion
for Z at arbitrary complex parameters, are what continue globally.
They agree with (5); either supplies the same endpoint sheet test.

## 5. A global strip-intersection question remains

For one actual complete coupon its transport is C=I+bH. The primitive
mark fixes b-epsilon/2=1/tau_cusp, so Im b<0 for the positive geometric
orientation. In the incoming disk coordinate set

    eta(s)=1/(2s+1).

Direct substitution gives eta(C s)=eta(s)-2b. The incoming condition
in (11) becomes Im eta>0; the outgoing condition, in the disk frame
C^(-1), becomes Im(eta+2b)<0. Thus, CONDITIONAL ON the strict central
inequalities, both input and output are selected exactly when

    0<Im eta(w)<-2 Im b,
    0<Im eta(W_prefix v)<-2 Im b.                       (12)

This is the actual oriented region between the two developed disk
circles. Positivity of the primitive cusp orientation gives its
positive height. It does not prove that all such regions meet.

Let Omega_f denote this region in the one global flag sphere, using
the actual input disk normalization at coupon f. Formula (12) gives
the necessary separated global conditions

    w in intersection_f Omega_f,
    v in intersection_f W_f^(-1) Omega_f.               (13)

Once the coupled central tests also hold, (13) is sufficient for
ALL endpoint local sheet tests. This is a finite geometric version
of the certificate. It identifies the precise role of the actual
prefix pullbacks; independent local flags do not establish (13).

No general identification of these intersections with exteriors of
polyhedral face disks is asserted here. Such an identification would
need the actual based words and both disk copies, as well as the
coupled central inequalities. The common-product feasibility lemma
in the preceding framing note concerns support only; it does not
by itself supply these selected input/output sheets.

## 6. Proof of the certificate and precise persistence

The sheet test identifies each actual geometric magnetic multiplier
with the selected local multiplier. The regular inverse (7) then
identifies its internal root with the source-selected root, including
the high adapter. The original full coupon phase, its factorial
measure, external phases and marked cap characters are retained.
Fixing the stipulated logarithmic/Poisson characters gives the
actual marked principal phase, rather than merely its exponentiated
equations.

The [critical-scheme inverse](actual_augmented_plat_critical_scheme.md)
now identifies this germ with the actual marked geometric
representation germ modulo the diagonal scale. The positive
multi-cusp gluing rigidity theorem makes its only magnetic null
directions the two framing directions. A transverse framing slice
therefore has nondegenerate magnetic Hessian. The same theorem's
classical action corollary, using the primitive collar differential
and the absolute endpoint regulator, gives exactly (1). No new
period normalization is introduced by the test.

The joint column theorem gives, for actual integer channels with
real xi_N=j/N near 1/2, the nonzero ordinary amplitude

    fhat=N^(-1/2) B_(xi_N)(tau,nu)
                    exp[N Phi_(xi_N)(tau,nu)](1+O(1/N)).

A fixed finite product of such ordinary factors has the product
estimate on a compact common domain. This supplies nonzero ordinary
column amplitude germs at the certified branch; it supplies neither
generic normal-factor estimates nor a full-source saddle coefficient.

All strict central inequalities and (5) persist under small marked
peripheral deformation. The unramified geometric germ and transverse
critical slice then continue the certified CLASSICAL selected branch.
The selected coefficient functions also continue holomorphically in
xi near 1/2. This applies to sufficiently long geometric fillings,
with their original primitive marks. It does not continue the finite
discrete index j to a complex value or justify a channel contour.

The remaining global tasks are substantive: produce the certificate
for a broad geometric class, control all required normal currents,
and prove that the original finite cycle has the required contribution
and global exponential bound. This note resolves none of those tasks
merely by having a stationary point with the correct volume.

Audit: [exact original-head, adapter and strip identities](../experiments/audit_actual_augmented_plat_selected_local_certificate.py).

Independent analytical reviews: PASS. Two readers checked the finite
certificate, original low/high input/output conventions, connected-domain
sheet continuation, the actual primitive-collar strip and prefix
pullbacks, and the distinction between classical continuation and a
finite-channel or full-source asymptotic. A fresh independent audit
replay passed all four root identities, the exact strip translation,
and 2,000 selector comparisons on 1,000 central frames. The reviews
establish no general existence of the certificate or contributing cycle.
