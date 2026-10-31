# The adjoint finite-jet connection on the original source cycle

30 October 2026. The exact tensor-source
transport has a corresponding identity for the original cotangent
period. Its adjoint acts on the cotangent density as well as on the
explicit source gauge. The resulting double-pole and finite-part terms
are retained. This does not make the finite head sum periodic or move
its cycle to the geometric critical point.

## 1. The actual period and the specified source connection

Use the [actual tensor-source connection](actual_tensor_source_finite_jet_connection.md).
After the original integral affine head equations, write the primitive
free lattice as h=h0+A x, x in C^k. Constant head factors remain their
original source constants. Fix the finite channel labels, or retain the
finite vector of label sectors when their characters differ. Every
outside tensor, turn and peripheral character is part of the specified
meromorphic source S(epsilon,x). At the original marked arc use its
ordinary generic pivotal closure and subsequent exposed-trace normal,
or an explicitly chosen covariant generic marked row. No generic
continuation of the bare root mark is supplied by this theorem.

Initially assume S is root-regular in epsilon on a common neighborhood
of the cycle, after retaining its actual meromorphic cancellations.
If a chosen representation has a finite Laurent pole of order M,
apply the statements to epsilon^M S through order J+M to recover
the original Laurent jet through order J. One must not use only
J translation terms before multiplying a source with such a pole.

Put P=pi i/Log(q0 exp(epsilon)), Delta=N-P, and P'=iN^2/pi.
For b in Z^k, let D_b=sum b_j partial_(x_j). The source theorem proves

    S(epsilon,x+Nb)=chi(b) G(x) exp(Delta D_b)[G(x)^-1 S], (1)

where chi(b) is the actual parity character and G is the explicit
P-independent rational cup/character gauge. Its construction omits
constant head factors; in particular it never inserts g(integer) for
an identically constant cup argument. Formula (1) is meromorphic and
its exponential is a FINITE differential operator modulo any fixed
epsilon^(J+1).

The original lattice density and normalized period are

    W(x)=product_(j=1)^k pi cot(pi x_j),
    I_Gamma[S]=(2pi i)^(-k) integral_Gamma W(x) S(x) dx,  (2)

with dx=dx1 wedge ... wedge dxk. Gamma is the original sum of compact
local tori, or a specified closed cycle on the same source chart. It
avoids the divisors of S, W, G and G^-1 on its surface on a common
epsilon germ, or the genuinely canceled meromorphic integrands are
used throughout. Its
interior may contain the original cotangent and source poles. The
[source-null extension theorem](actual_matching_edge_degree_cycle_boundary.md)
allows its explicitly proved zero ordered tori to be included as well.
Other polar strata are not implicitly added or removed.

## 2. Exact adjoint transport of every finite quantum jet

For every fixed J, on the original CLOSED cycle one has

    I_Gamma[S(epsilon,x+Nb)]
      =chi(b)(2pi i)^(-k) integral_Gamma
          G^-1 exp(-Delta D_b)(W G) S dx
                                            mod epsilon^(J+1). (3)

All derivatives in (3) act on the actual top-form density W G. This
is not a replacement of the original period by a period of S/G.
The final meromorphic integrand is used with every cancellation and
divisor retained, rather than evaluated factor by factor at G=0 or
G=infinity.

Proof: for meromorphic f,g with no pole on the cycle,

    integral_Gamma f D_b g dx=-integral_Gamma (D_b f) g dx.

Indeed D_b(fg) dx=d(fg contraction_b(dx)), whose integral on a closed
cycle is zero. This argument needs no pole-free interior. Apply it r
times to the r-th term of (1), with f=W G and g=G^-1 S. Since Delta
is independent of x and belongs to (epsilon), only r<=J occurs for
the root-regular source specified in section 1. For a Laurent source
use the cleared source and the enlarged order stated there.
This proves (3) without an infinite differential expansion or an
analytic translation of Gamma by the small complex number Delta.

For the literal translated cycle Gamma+Nb, a change of variables also
gives

    I_(Gamma+Nb)[S]=I_Gamma[S(epsilon,x+Nb)],              (4)

because the original W is N-periodic. This is an identity of the
specified continued source at that translated cycle. It does not say
the shifted head values are admissible original states or vanish
outside the physical basis. In particular the meromorphic continuation
need not vanish at out-of-basis shifted indices.

If a geometric deformation from one cycle to the other crosses source
divisors, their tubes and residues remain in that deformation. Equations
(3),(4) compute the translated period; they do not identify the two
cycles in the complement of those divisors.

## 3. The first normal and the original exposed trace normalization

Write S=S0+epsilon S1+O(epsilon^2). Formula (3) yields

    I_(Gamma+Nb)[S0]=chi(b) I_Gamma[S0],
    I_(Gamma+Nb)[S1]-chi(b) I_Gamma[S1]
      =chi(b) P' (2pi i)^(-k) integral_Gamma
                         G^-1 D_b(W G) S0 dx.            (5)

The sign is positive: Delta'=-P' and the adjoint exponential is
exp(-Delta D_b). The correction includes derivatives of BOTH W and G.
Writing it as W D_b Log(WG) is permissible only as a meromorphic
identity; the un-divided density in (5) specifies its actual periods.

For the original ordinary exposed-head closure, retain

    nu_N=2N(-1)^N/(q0-q0^-1),
    P'/nu_N=(-1)^(N+1) N sin(pi/N)/pi.                    (6)

When the original root closure I_Gamma[S0] is zero, its translated
root closure is also zero by (5), so division of the first-normal
identity by nu_N gives the exact corresponding marked-period
difference. Its correction density has the nonzero order-one scalar
in (6), rather than an arbitrarily assigned boundary coefficient.
It is not yet a nonzero global geometric contribution.

For a primitive direction with several nonzero b_j, D_b differentiates
the corresponding original cotangent factors. A chosen degree h need
not be a primitive free variable. For h=A0 x_j+B0 at fixed other
coordinates, the weight is (pi/A0)cot(pi(h-B0)/A0) dh. The finite-part
rules of the boundary theorem apply with that weight. Neither (3) nor
(5) replaces it by pi cot(pi h) dh.

## 4. A literal cup exhibits a nonzero double-pole correction

For one varying cup argument, its source gauge is

    g(x)=Y/(1-Y), Y=exp(2pi i x),
    pi cot(pi x)=-pi i(1+2g(x)).

Let w=pi cot(pi x). The correction density in (5) is

    g^-1 (w g)'=w'+w * 2pi i/(1-Y).                     (7)

At an integer n, with y=x-n, this equals

    -2/y^2+pi i/y+O(1).

Consequently its residue against a root source regular there is

    pi i S0(n)-2 S0'(n).                               (8)

Both copies of the derivative matter: one comes from the original
cotangent and one from the actual cup gauge.

For the ordered fixed-L cup with L=d=N-1, the exact fixed-root
reflection gives p_d(0,x)=exp(pi i d x/N). On a physical n in [0,d],
the difference of its translated and parity-weighted original
first-normal cotangent periods is therefore exactly

    (-1)^d N(N-2) exp(pi i d n/N).                       (9)

This is the ordered channel-cup normalization of the source theorem.
For the physical cup, multiply by its original root scalar
N q0^(-d^2); its generic scalar derivative cancels from the difference
because the corresponding root difference is zero. The translated
cup can have a generic pole at n+N. Its cotangent period is the actual
Laurent finite part, not its value at that pole. Thus (9) is a concrete
counterexample to silently declaring these continued periods periodic.

## 5. Scope of the cycle identity

The source connection, the original primitive lattice and the original
weight together determine every finite-order correction in (3). The
isolated wall residues and source-null ordered periods are already
given by the boundary theorem. Their combination supplies exact
finite-head transport with its boundary terms retained.

What remains separate is a deformation of the FULL original period
through all its source divisors to a contributing geometric cycle,
including its noncompact ends and the coherent outside contraction.
No equality of the positive envelope with volume, no periodic extension
of the physical basis, and no nonzero saddle coefficient follows from
this adjoint identity.

Focused verification: [adjoint and original cup audit](../experiments/audit_actual_tensor_source_translated_cycle_normals.py)
and [saved results](../experiments/actual_tensor_source_translated_cycle_normals_results.json).
The audit checks 60 exact meromorphic adjoint residues through derivative
order three, the actual cotangent double-pole coefficient, and 12 genuine
translated first-normal cup finite parts obtained independently from
the original moving-Gamma Laurent coefficients. The latter agree with
(9) to relative error below 5.3e-38 at 100 digits. These are checks of
the retained local periods, not evidence for a global saddle coefficient.

The result retains all source and gauge divisors and makes no contributing-cycle assertion.

No wrapped physical state or geometric contribution is inferred from the translated normal identities.