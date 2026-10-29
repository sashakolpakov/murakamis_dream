# An original-source zero-side patch across an isolated shape-one divisor

28 October 2026. A single transverse A=1 exit of a DIRECT full-Psi
factor is locally removable. The actual function is holomorphic on
the entire shrinking patch, including all its accumulating zeros.
After crossing to its zero side, its outgoing current is the exact
sum of TWO regular selected-strip currents. The whole norm factor
1-A^N, its logarithmic mark and every original side current are retained.

For a fixed finite patch this costs exp(o(N)). With a normal collar
chosen smaller than the background regularity scale, both outgoing
phase sectors are downhill. This does not bound the global number of
visits, sum an arbitrary set of simultaneous signed collisions, or
estimate the remaining original side currents by knot volume.

## 1. Precise local source hypotheses

Let u=Log A be a genuine complex normal coordinate to A=1 in the
INTEGRATION variables, with u=0 on the divisor. In the actual monomial
phase charts this is a fixed real integral linear combination of the
log coordinates; complete it by fixed linear coordinates y. The
coordinate change has N-independent condition number. A purely external
meridian specialization is not an available normal contour direction.

The argument A includes every ORIGINAL Q/q/color tag of that full-Psi
factor. If its classical signed monomial differs by an O(1/N) logarithmic
shift, keep that shift in u exactly. It moves the collision center by
O(1/N), which is inside the collar since alpha<1; the uniform estimates
are unchanged. In particular its N-th power need not be one for a
half-root tag. The exact factor 1-exp(Nu) below retains that character
and is not replaced by the untagged 1-A_classical^N.

This applies to an actual source chart before singular elimination:
use the [atomic-window whole-source resolution](atomic_window_total_source_resolution.md)
and keep its finite-window interval sources and original coupled caps.
The finite window is an entire polynomial in its argument; its exact
interval prefactor Log r/(r-1) has its removable value at r=1.
Near a lone atomic t=1, these sources therefore introduce no new
normal pole. Their N-dependent exponential monomials stay in G,
with interval variables and endpoints fixed by the local normal
translation. The remaining rational/head exclusions must still be
checked on the chart. This does not assume an eliminated current
with an apparent inverse norm is holomorphic term by term.

Suppose the original scalar differential form on this chart is

    omega_N=Psi_epsilon(u) exp(G(u,y)/h) a_N(u,y) du wedge dy,
    h=2pi i/N, epsilon=+1 or -1,                       (1)

where a_N and the FULL original relative co-source are holomorphic in
the normal tube being used. All other actual full-Psi factors, fixed
Gaussian/interval phases and N-dependent monomial factors are retained
in G and a_N. Their own shape and quantum-pole exclusions remain valid.
The unexpanded original ray currents and boundaries remain part of
the same relative chain. No bare reciprocal full function or unpaired
norm denominator is assumed holomorphic by definition.

For the quantitative estimates, assume the other regular factors obey
the slowly expanding window bounds with L=N^epsilon_0. In the fixed
normal coordinate these imply

    |partial_u G|<=C_0+C_1 epsilon_0 log N              (2)

when their logarithmic marks stay bounded. For downhill alone it is
enough to impose this bound on |Re partial_u G|: arbitrary retained
integer wall marks have purely imaginary normal derivative and do
not affect that bound. The rational/half-density amplitude is bounded
by a fixed power of N, or more generally by exp(o(N)), on this tube.

The tube is ISOLATING: no other dilogarithm shape-one divisor, source
pole, cap singularity or quantum pole is crossed. These are substantive
local hypotheses. In particular the lemma cannot be applied separately
to two current summands whose apparent norm poles only cancel in their
sum. One must first use their actual holomorphic aggregate.

Set delta=N^(-alpha), with 0<alpha<1. The patch below lies in
|Re u|<=delta, -3delta<=epsilon Im u<=delta. By isolation, all other
factors remain regular throughout this patch. N is sufficiently large
that Ndelta>=2pi and a fixed multiple of delta is small.

## 2. Uniform full-function bound on the ENTIRE collision collar

Use the exact quantum shift, with its original logarithmic lift,

    Psi_epsilon(u+epsilon h_0)
                   =Psi_epsilon(u)/(1-exp u),
    h_0=2pi i/N.                                     (3)

Choose a FIXED integer m=O(Ndelta) large enough that every u in
the patch has

    delta<=epsilon Im(u+epsilon m h_0)<=Cdelta.

Iteration gives the literal function identity

    Psi_epsilon(u)
       =Psi_epsilon(u+epsilon m h_0)
                    product_(j=0)^(m-1)(1-exp(u+epsilon j h_0)). (4)

The shifted factor is holomorphic and nonzero in its selected strip.
Every product factor is entire; its size is at most Cdelta on the
patch. Equation (4) proves that Psi itself is holomorphic there and
retains the simple zeros u=-epsilon j h_0; no pole or residue is
created by crossing them. The argument uses the actual full function,
not the norm-one cyclic atom.

At the shifted point the shrinking-strip estimate applies. The local
dilogarithm expansion Li_2(exp w)=pi^2/6+O(w(1+|Log w|)) gives

    sup_patch |Psi_epsilon(u)|
       <=exp[C Ndelta(1+|log delta|)+O(log N)]
       =exp(o(N)).                                   (5)

The constant pi^2/6 contributes unit modulus in the prescribed h_0
phase. This upper bound is uniform through every zero; no lower
bound for Psi or its logarithm across those zeros is claimed.

The variation of the other leading phase across this normal patch
is O(delta log N) by (2). Thus relative to the same tangential base
phase at u=0, the entire local integrand changes its exponential
scale only by exp(O(Ndelta log N)+o(N)). Fixed-dimensional translations
and their sweeps have at most polynomial mass cost.

## 3. Exact outgoing selected-strip sectors

Translate the normal variable by

    H_t(u,y)=(u-2i epsilon delta t,y), 0<=t<=1.         (6)

For incoming |u|<=delta the output u'=u-2i epsilon delta satisfies

    -3delta<=epsilon Im u'<=-delta.

The exact FULL-turn identity is

    Psi_epsilon(u')
       =(1-exp(Nu')) Psi_epsilon(u'+epsilon 2pi i).    (7)

The shifted factor now lies in its original selected strip with
margin at least delta. Hence the outgoing differential form is
exactly the sum

    omega_out,0 = Psi_epsilon(u'+epsilon 2pi i)
                     exp(G(u',y)/h_0) a_N(u',y) du' wedge dy,
    omega_out,1 = -exp(Nu') omega_out,0.               (8)

Their leading actions are

    W_0=epsilon Li_2(exp u')+G(u',y),
    W_1=W_0+2pi i u'.                                (9)

The dilogarithm and logarithm in W_0 are on the shifted selected
strip, not reset to an unrelated principal value. The factor
1-exp(Nu') has NOT been divided out or replaced by a number.
It records the entire outgoing zero lattice and the original
integer norm/ray mark. There are exactly two currents here,
independent of N, with coefficients +1,-1.

## 4. Genuine downhill transport on nested collars

The singular leading action is epsilon Li_2(exp u). Along a vertical
normal translation its derivative satisfies, on any continued local
sheet away from u=0,

    d/ds Im W(u-i epsilon s,y)
       =-epsilon Re(partial_u W)
       =log|1-exp u|-epsilon Re(partial_u G).          (10)

This real derivative is independent of the logarithm branch. It is
locally integrable through u=0 itself. Since |u|<=Cdelta on the patch,
(2) gives

    d/ds Im W <=-(alpha-C_1 epsilon_0)log N+C.          (11)

Choose

    C_1 epsilon_0<alpha<1.                            (12)

For large N this is uniformly negative. Thus the normal patch is
genuinely downhill, not merely of subexponential amplitude cost.
The background exponent epsilon_0 may first be chosen small enough
to permit (12). If the SAME exponent is used for both collars and
the arbitrary background bound is only O(log N), strict downhill
does not follow automatically; the upper bound (5) still does.

For incoming points in the selected side, continue its classical
action along (6) without silently changing sheets. On Re u'<0 it
agrees with W_0 at the outgoing point and W_1 has smaller imaginary
part. On Re u'>0 it agrees with W_1 and W_0 has smaller imaginary
part. This is the usual local Li_2 monodromy difference 2pi i u';
both continuations agree at u'=0. The statement holds for either
epsilon by conjugate reflection. Therefore

    max(Im W_0,Im W_1) <= Im W_in-c delta log N         (13)

on a complete translation of length 2delta, under (12), for some
fixed c>0. Retained integer logarithmic marks only add a constant
2pi m Re u along each vertical path, so the same downhill conclusion
holds with those marks included. The two-sector split does not
introduce an uncontrolled leading action.

## 5. The original chain identity, INCLUDING side currents

Let Gamma be any fixed finite-dimensional original chain portion in
the isolating tube, with its original source and logarithmic marks.
Let S=H_*([0,1] times Gamma) and S_side=H_*([0,1] times partial Gamma),
with the product orientation. Since

    partial S=Gamma_out-Gamma-S_side,

holomorphy of the FULL differential form in (1) proves exactly

    integral_Gamma omega_N
       =integral_(Gamma_out,0) omega_out,0
         +integral_(Gamma_out,1) omega_out,1
         -integral_(S_side) omega_N.                 (14)

No additional residue is produced at u=0 or at the lower neighboring
cyclotomic zeros. The original radial/logarithmic boundaries are
carried by the same homotopy or left outside its support; they are
not deleted by (14). If the chart has to be split along a logarithmic
seam, the two original seam currents are matched using the exact
identity (7), rather than assuming the classical Li_2 branch is
single valued. The whole norm factor in (7) is retained.

The side current in (14) is compulsory. It vanishes for a closed
chain piece, cancels on a common face of two pieces using the SAME
homotopy, or remains as an explicit original relative boundary term.
Normal side faces with |Re u|=delta already lie outside the shape-one
divisor and are regular. Boundaries from other coordinates remain
their original exit currents; this theorem does not estimate them
by knot volume. All finite patch sweeps have exp(o(N)) local cost
relative to the retained tangential phase, by (5), (2) and their
bounded translation Jacobians.

This removes the isolated shape-one divisor as a local analytic
barrier and returns its outgoing contribution to REGULAR full-Psi
charts with explicit integer sectors. It does not prove a global
bound on the number of patches, revisits or accumulated branching.

## 6. Several independent divisors, and the limitation

For a fixed number p of INDEPENDENT normal coordinates u_j, direct
factors product_j Psi_(epsilon_j)(u_j), an isolating polydisc and
background satisfying the corresponding bounds, the translations
in (6) commute. Their exact outgoing factor is

    product_j (1-exp(Nu_j'))
              product_j Psi_(epsilon_j)(u_j'+epsilon_j 2pi i).

Thus a fixed simultaneous patch has 2^p regular outgoing sectors,
with every integer mark retained, and the same exp(o(N)) bound.
Under nested collars satisfying (12) in each direction, the actions
are downhill coordinate by coordinate. Product-chain side currents
are retained by the same Stokes formula. This is a fixed finite
independent-normal statement, not a cancellation theorem.

Dependent signed normals can prevent a common zero-side translation;
oppositely cooriented copies of the same divisor are the simplest
example. Balanced collisions, simultaneous source poles, nontransverse
normal maps, and arbitrary collision circuits are excluded. No
automatic cancellation or sharp whole-knot estimate is inferred there.

## 7. Reproduction and scope of the checks

    python3 experiments/audit_actual_isolated_shape_one_patch.py

The exact finite-product checks are made at Re u<0 so their logs are
on the original convergent anchored branches; no floating branch
unwrapping is assumed. They compare both signs of (4),(7), retaining
the norm factor, through N=256 and both level parities. Separate
phase calculations test both outgoing sectors with adverse polynomial
background derivatives. Fresh result: **PASS**, 36 exact normal-chart
transitions and 48 signed two-sector downhill checks.
[Saved results](../experiments/actual_isolated_shape_one_patch_results.json).

The theorem and its uniform estimates follow from the analytic proof
above. The checks do not establish a global patch-count bound, a
simultaneous dependent-collision theorem or a geometric lower bound.
