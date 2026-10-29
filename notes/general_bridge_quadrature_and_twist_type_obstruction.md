# What the selected five-crossing proof does and does not generalize

28 October 2026. This is an independent audit of the proposed extension
from the original selected 5_2 period to many bridges or long twist regions.
The result below is an exact obstruction inside the ORIGINAL repeated
crossing, rather than an arbitrary oscillatory example. It identifies why
one useful quadrature theorem cannot simply be iterated after aggregating
long twists. It is not an obstruction to the volume conjecture.

## 1. The genuinely reusable input

The [five-crossing proof](five_two_selected_volume_proof.md) combines four
different facts:

* an exact finite whole-source transform;
* a lattice-to-integral comparison with every endpoint retained;
* global bounds for the selected contour and every quadrature correction;
* the geometric action and a nonzero Gaussian coefficient.

Only the second item currently has a local criterion that can be read
directly from a general finite kernel. Section 5 of
[the inner quadrature theorem](source_preserving_inner_quadrature.md)
gives that criterion for a reflected factorial convolution with a quadratic
Gaussian. The finite-height version is more general, but produces additional
source contours instead of bounding them automatically.

The arbitrary-plat reduction and positive gluing arguments supply classical
equations and rigidity at arbitrary bridge number. They do not supply the
exponential bounds for the finite quantum endpoint sources. Thus neither
positive ideal shapes nor an acyclic classical bridge complex currently
checks all four items for an infinite hyperbolic knot class.

## 2. An exact sector of an actual long twist

Use the original equal-color crossing and its actual Borel fusion from
[the whole-word theorem](actual_crossing_euler_completion_and_weight_source.md).
Its relative coefficient, after retaining the common Cartan scalar kappa
externally, is

    a_R/kappa = sum_(a+k<N)
       (-1)^k Q^(k(k-1)/2) x^(-a-2k) f^a e_k/F_a.

The ideal (f) is two-sided. Hence the image of a literal p-fold crossing in
the exact quotient by (f), for any integer p, is

    sum_k d_k^p e_k,
    d_k=(-1)^k Q^(k(k-1)/2) x^(-2k).

Equivalently these are the actual degree-zero diagonal entries of
C^(-1) R^p C/kappa^p. This is an exact matrix sector, not a semiclassical
replacement of the full crossing. At the complete color x=-q^(-1), Q=q^2,

    d_k=(-1)^k Q^(k(k+1)/2).

Let n=N-1. A normalized entire interpolation of these literal lattice
values is

    B_(p,N)(z)=exp[pi i p z(z-n)/N].                         (1)

Indeed its exponent differs from the displayed d_k^p exponent by
-2pi i p k, so (1) agrees at EVERY integer k. All ordinary linear lattice
gauges have the form

    B_(p,N,ell)(z)=exp(2pi i ell z) B_(p,N)(z), ell in Z.     (2)

The quotient calculation does not permit replacing the original knot's
whole cut by this sector alone. Its role here is to test a proposed
universal local quadrature rule on an actual component of that kernel.

## 3. No linear lattice gauge removes the long-twist type

For a=0,n and real t,

    |B_(p,N,ell)(a+it)|
       =exp[-pi {p(2a-n)/N+2ell} t].                       (3)

The largest absolute vertical exponent over the two endpoints and two
directions is therefore exactly

    pi [ |p|(N-1)/N + 2|ell| ].                            (4)

In particular ell=0 is optimal, and its minimal type approaches pi|p|.
This is a minimization over all the linear integer lattice gauges, not a
failure to find a suitable gauge.

More decisively, the actual endpoint numerator in finite Abel--Plana is
explicit. The identities B(n-z)=B(z) and exp(2pi i ell n)=1 give

    B_ell(it)-B_ell(-it)-B_ell(n+it)+B_ell(n-it)
       =4 exp(-pi i p t^2/N)
          sinh(pi p n t/N) cosh(2pi ell t).                 (5)

There is no hidden cancellation between the two endpoints. Dividing by
exp(2pi t)-1, its absolute size at infinity is asymptotic, up to a fixed
positive constant, to

    exp{ pi [|p|(N-1)/N+2|ell|-2] t }.                     (6)

Consequently, whenever |p|(N-1)/N>2, no gauge (2) gives the absolutely
convergent endpoint integral used in the reusable infinite-height
quadrature theorem. For every fixed |p|>=3 this fails at every sufficiently
large level. At equality the absolute integral still diverges; no claim
about a conditionally regularized formula at that threshold is needed.

This exact test includes both crossing signs and every level parity.
The common Cartan scalar has no head-index dependence and changes none
of (3)--(6). A zero-framing scalar external to a larger braid likewise
does not change the endpoint vertical type.

## 4. What a long-twist theorem would have to do differently

The subsequent [finite-mode quadrature theorem](finite_mode_source_quadrature_and_long_twists.md)
now resolves this particular type obstruction constructively: retain an
explicit O(|p|)-sized Fourier packet and an endpoint remainder which is
O_p(1) at every level. Its far tail is exponentially small at height
proportional to N. The modes and near endpoint correction remain present.

The finite-height residue formula remains exact for (1), so this is not
a prohibition on that method. It forces one to keep and control the extra
contours. At height t=N h their endpoint growth after the Abel--Plana
denominator has rate

    pi [ |p|(1-1/N)-2 ] h.

Thus a bound that keeps h fixed while aggregating an arbitrarily long
twist has a linearly growing adverse rate already in this actual sector.
A valid large-twist argument may instead retain the individual crossings,
use heights of order 1/|p|, or prove a different exact recoupling together
with all its transformed endpoint sources. The present theorem does not
decide which of those succeeds.

Nor does the existence of a positive geometric triangulation bound these
quantum endpoint terms. Any use of volume monotonicity must first identify
the endpoints with specified original lower-complexity periods; an
unidentified face of a factorial sum is not automatically the invariant
of a drilled or smoothed link.

The next genuinely structural theorem is therefore an endpoint transport
and bound for a whole bridge move: express every finite-source boundary
correction as a specified lower-complexity pointed period, with a proven
rate below the geometric main period, uniformly over a diagram class.
That is a concrete target suggested by the 5_2 error bound by the ORIGINAL
figure-eight invariant. It has not yet been established for arbitrary
plats, arbitrary alternating diagrams, or a nontrivial infinite family
with unbounded bridge number.

## 5. Coverage, not proof input

The primary abstract of Jun Murakami's
[double-twist preprint](https://arxiv.org/abs/2501.00225)
(v3 dated 2 May 2025) states a volume-conjecture result for double twist
knots. The primary abstract of van der Veen's
[Whitehead-chain paper](https://arxiv.org/abs/math/0611181)
states an infinite family of links. The latter is not a theorem about
arbitrary many-bridge knots in S^3. The published
[twist triangulation theorem](https://ems.press/journals/qt/articles/12209830)
concerns the Teichmueller-TQFT volume conjecture; its abstract does not
identify that state with the original Kashaev scalar. These are coverage
checks only. No proof technique or theorem from those papers is used in
(1)--(6).

The strongest established original-knot output of the present selected
finite-source mechanism remains its independently proved figure-eight
and five-crossing prototypes. A broad-class theorem is a further task,
not a consequence of continuity of the classical geometric point.

[Exact original-matrix and vertical-type audit](../experiments/audit_twist_vertical_type_obstruction.py).
