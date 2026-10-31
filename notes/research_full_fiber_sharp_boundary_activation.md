# Boundary reduction for a global full sharp-source maximum

31 October 2026. **Internally reviewed research theorem.** Root and a
separate reader completed full analytical reviews. This is a variational statement for the original sharp
interval functional on the ENTIRE original flow fiber, with independently
free spectra. It does not prove a finite-source asymptotic, a phase
selection theorem or an inequality by complete volume.

## 1. Original fiber and explicit hypotheses

Fix an original simple-white certified plat. Its white sphere is a simple
triangulation, the protected faces u,v are adjacent along the marked MAIN
edge, and a port pairs two shaded triangles across a MATCHING edge.
Keep every original incidence, including the protected zeros.

Let P be the FULL nonnegative transport fiber: each port supplies1,
each ordinary face demands1, and each protected face demands0.
No LEFT/CROSS/RIGHT label inequalities are imposed on P. A local vector
q=(X,B,C,Y) with sum1 is written

    mu=B, nu=1-C, xi=X, zeta=Y=nu-mu-xi.

The actual complete geometric flow qG belongs to P. It has positive
load on EVERY ordinary incidence, zero on protected incidences, and
both middle loads strictly less than1/2. Its two literal triangle
allocations are positive on every ordinary triangle corner. Each port
has at least one ordinary outer incidence: the two protected faces are
joined by a MAIN edge, not by its outer MATCHING edge. Therefore

    qG_x+qG_y>0 at every port.                         (1)

For 0<=delta<=1/2 define h_delta on the FULL interval by the original
[sharp functional](research_global_sharp_coefficient_limsup_majorant.md)

    h_delta(q)=int_0^mu log|alpha_delta|
                +int_nu^1 log|alpha_delta|
                +inf_(x>0){int_mu^nu log Lambda_delta(t;x,1)dt
                              -xi log x},             (2)
    alpha_delta=4[cos^2(pi delta)-sin^2(pi t)].

Here Lambda=beta rho, with beta(t)=4 sin^2(pi t) and rho the exact
[positive eta-word root](research_positive_eta_word_transfer.md),
eta=cos^2(pi delta)/sin^2(pi t). Endpoint values are the continuous ones. In particular h_(1/2)=0 for
ALL q. At delta=0, h_0 is the [continuous full-kernel
endpoint entropy](actual_fejer_full_kernel_entropy_identity_reduction.md). On CROSS (B,C<=1/2),

    h_0(q)=max_(a+b=q) [Ctri(a)+Ctri(b)],              (3)

where the two original triangle rows have supply1/2 and their indicated
middle loads B,C. This is the exact latent split of the original port,
not independently reassigned angles. The all-CROSS geometric allocation
has [total endpoint entropy Phi_D>0](actual_fejer_unique_geometric_maximizer.md).

Consider a GLOBAL maximum of sum_e h_(delta_e)(q_e), with q in P and
independent real delta_e in[0,1/2]. Alternatively maximize over the
closed non-CROSS union, but assume the maximum being studied has value
at least Phi_D and at least one STRICT non-CROSS middle load greater
than1/2. Such a port
keeps the geometric segment below in that union for all sufficiently
small perturbations. No analogous claim is made for a seam-only
non-CROSS boundary maximum.

The statements use the sharp continuum functional directly. Where
it is used as an upper functional for the actual source, this theorem
does not supply a new coefficient-identification or cap-uniform N limit.

## 2. Fixed-load spectral exclusions

First, a positive-length port at strict 0<delta<1/2 cannot have an
endpoint at either simple alpha pole. Write the poles as p=1/2-delta
and p'=1/2+delta. Moving an endpoint pole into the active interval
increases the two outside integrals by
|s|log(1/|s|)+O(|s|). If both endpoints are poles, necessarily
mu=p,nu=p'; decreasing delta moves both inside and gives twice this
gain. All other outside-integral changes are O(|s|).
The tilted tail changes only O(|s|), uniformly in the tilt: with
eta=cos^2(pi delta)/sin^2(pi t),

    0<=partial_(log eta)log rho_eta(x)<=1/2,

and partial_delta log eta is bounded on every strict delta compact.
Taking a common infimum preserves that Lipschitz estimate, also for
closed outer loads. Thus an arbitrarily small feasible spectral change
increases (2). This excludes positive-length pole endpoints without
assuming face stationarity or concavity in the row variables.

Second, at delta=0 a positive-length nonterminal one-sided interval
cannot maximize in its free spectrum. For a lower interval nu<1/2,
put z=sin^2(pi delta) and L_z=Lambda_z/alpha_z, with z small enough
that alpha stays positive on the interval. Directly from the positive
root,

    -partial_z log Lambda_z <=1/[2(1-z)],
    partial_z log L_z >=1/[2(1-z)].

The first inequality follows by bounding its square-root denominator
below by 4xy(1-z); it remains valid at a monomial tilt. Hence,
uniformly in every outer tilt and after the same infimum,

    h_delta(q)-h_0(q)>=-(nu-mu)log(1-z)/2>0.          (4)

Reflection proves the upper one-sided case. Thus every positive-length
delta=0 port at a maximum lies in CROSS, allowing its seams for now.

Finally classify a positive-length delta=1/2 port at fixed loads.
The sharp entropy dominates its monomer action because J*>=0.
If 0<mu<nu<1, choose a positive k=cos(pi delta) smaller than the
minimum of sin(pi t) on that fixed interval. The entire active
interval is then after the small lower pole and before its reflection,
and its actual monomer action is

    int_mu^nu -log[1-k^2/sin^2(pi t)]dt>0.           (5)

Thus every interval with both endpoints strictly inside(0,1) is excluded
at the cap, uniformly over its closed outer split. Write I_k(0,a)
for the initial monomer integral of log[sin^2/|k^2-sin^2|].
If mu=0 and 1/2<nu<1, the exact total and reflection identities give

    I_k(0,nu)=-I_k(0,1-nu)>0                       (6)

for sufficiently small k, because the latter initial interval has
negative monomer action by its regular positive suffix formula.
Exact reflection treats nu=1 and 0<mu<1/2.

For mu=0,0<nu<1/2 and BOTH outer loads positive, the [protected-middle
cap lemma](research_protected_middle_spectral_cap_exclusion.md) gives, at small positive k=cos(pi delta),

    h_delta>=2 min(xi,nu-xi)log(1+k)
                        -(2/pi)k^2 cot(pi nu)>0.     (7)

The half-terminal extension has no baseline cost, and a full interval
[0,1] has the same positive chord bound for strict outer loads. Exact
reflection covers the protected output. Consequently a cap maximum
with positive length can only have a monomial outer split and be

    [0,nu], 0<nu<=1/2; its reflected interval;
    or the whole interval[0,1].                     (8)

Every other fixed-load cap candidate has an available positive value
at another spectrum, while the cap value is zero. This classification
does not yet eliminate the zeros at (8).

## 3. One geometric segment, with source spectra retained or retuned

Use the EXACT full-fiber segment

    q(eps)=(1-eps)q+eps qG.                          (9)

It preserves every ordinary target, protected zero and row supply.
It activates every zero ORDINARY incidence. It is not required to
preserve an old LEFT/CROSS/RIGHT label at a boundary: the full source
fiber has no such imposed labels. If a strict non-CROSS port was
specified, its strict inequality persists for small eps.

For a non-diagonal strict-spectrum port, keep delta fixed. The
[ordinary-zero barrier table](research_sharp_spectral_ordinary_zero_barrier.md) and exact reflection give nonnegative
eps log(1/eps) coefficients, strictly positive if an ordinary zero
incidence is activated. Upper rows equal1/2 are regular units at a
strict spectrum; there is no half-label inequality in this full fiber.
At the full two-terminal interval mu=0,nu=1, write mu=eps B and
1-nu=eps C. With strict base outer loads use xi=xi0+eps dot_xi,
0<xi0<1; the two-end calculation gives B+C. At the x-zero corner
instead use xi=eps X, and its coefficient is 2(B+C+X).
Outer reflection is identical.
These exhaust the positive-length full-row zero patterns. All other
changes are O(eps).

For a delta=0 CROSS port choose an attaining split in (3), and mix
its two triangle rows with the actual geometric triangle rows. Their
sum is EXACTLY the local vector in (9). The optimized h_0 at that
vector is at least the entropy of this mixed split. Each triangle has
a nonnegative closed-corner singular coefficient, strictly positive
at every activated zero ordinary corner. Thus an ordinary zero in
the port gives a positive gain. At a seam nu=1/2 the output triangle
is the pure-middle vertex, and its contribution is

    2 dot_nu eps log(1/eps)+O(eps), dot_nu>0.         (10)

The input triangle has no negative singular contribution. The
mu=1/2 seam is reflected and gives -2 dot_mu>0. This uses an actual
latent complete split inside the FULL endpoint polynomial. It makes
no infeasible fixed-pattern retagging or terminal KKT assertion.

For a diagonal mu=nu=a, retune its spectrum. At a in(0,1), (1)
opens a positive interval; placing a simple pole inside it gives
W eps log(1/eps)+O(eps), or 2W at a=1/2, uniformly in the outer split.
At a=0 or1 use cos(pi delta_eps)=eps^2; its cost is at worst
O(eps^2). These are the [free-spectral retuning estimates](research_free_spectral_diagonal_retuning.md).

For a cap port from (8), the [cap-corner lemma](research_spectral_cap_corner_activation.md) gives the needed
ordinary-zero gain. At [0,nu0] with nu0<1/2 and x load zero, choose
cos^2(pi delta_eps)=eps K. Its singular coefficient is B+X, where
B=dot_mu and X=dot_xi. It is positive if either zero incidence is
ordinary. At a flat half-terminal monomial interval [0,1/2], the base value
is zero for EVERY spectrum. Retune its base to delta=0 and use the
actual latent CROSS split above. Its output triangle is the pure-middle
vertex, so (10) gives a strictly positive gain because qG_c<1/2.
This remains true when the input middle and the zero outer incidence
are both protected. Thus the half-terminal monomial is excluded at
every initial spectrum, not only at the cap. Exact reflection excludes
the upper half-terminal monomial as well.

At the flat full terminal interval, retune to a fixed strict delta and
use the corresponding corner table. A full [0,1] monomial interval
has three zero incidences, at least one ordinary, so its gain is strict.
If both zeros of a half-interval cap corner are protected, keep the
cap value zero. That port has no ordinary zero to activate. Reflected
and outer-exchanged cases use the same exact source symmetries.

All spectra are independent, so these choices can be made simultaneously
without altering (9). There are only finitely many ports. Every listed
singular coefficient is nonnegative; every strict gain dominates all
O(eps) terms. Thus global maximality implies:

* every non-diagonal port has positive load on every ordinary incidence;
* no interior diagonal remains;
* no positive-length delta=0 port lies on a CROSS seam;
* no half-terminal monomial remains at any spectrum;
* every remaining positive-length cap port has its two zero incidences
  both protected, and is a monomial corner [0,nu] with 0<nu<1/2,
  or its exact reflection.

This conclusion is for a global free-spectrum maximum. No such
simultaneous retuning is inferred at a local fixed-spectrum maximum.

## 4. Endpoint diagonals form an impossible closed component

Only diagonals at a=0 or1 can now remain. Let D be their ports and F
their occupied middle faces. Such a row sends its entire supply1 to
one ordinary face. Protected demand0 excludes a protected occupied face,
and demand1 makes the map D->F injective. Therefore |D|=|F|.

Every face in F is saturated by its diagonal row. By section3 every
ordinary incidence of a non-diagonal row is positive. Thus no
non-diagonal row can even be incident to F: N(F)=D in the full supported
bipartite incidence graph B. Evaluate the same demands with qG.
The faces F require |F|=|D|, and only D can supply them. All supplies
of D are therefore used inside F. Because qG is strictly positive on
every ordinary incidence, no D row has an arc to an ordinary face
outside F. Hence D union F is a union of connected components of B.

The original graph B is connected. Delete u,v from the simple white
triangulated sphere: the remaining white graph is connected. The [elementary connectivity argument](actual_original_boundary_transverse_rank.md)
reroutes a path through the cyclic link of u, and
then through the link of v with u deleted, which is a connected path
or cycle. Every remaining white edge belongs to an original port
quartet, so it induces a two-step path through that port in B.
Every port has an ordinary incidence. These facts connect all vertices
of B without creating any new source adjacency.

Consequently nonempty D would mean all ports are diagonal. Their
total sharp entropy is zero. This contradicts the feasible geometric
value Phi_D>0 for an unrestricted full-fiber maximum. In the strict
non-CROSS variant, the comparison must instead assume the studied
maximum has positive value (as is automatic for any candidate at or
above Phi_D). The all-geometric point need not lie in that restricted
set, so its value is not silently used as a feasible NC lower bound.

Thus D is empty under these stated value hypotheses. No actual identity
smoothing or cover is needed for this tight-cut argument.

## 5. What the reduction proves, and what remains

An unrestricted global full sharp maximum on this original certified
fiber has no diagonal and has positive load on every ordinary incidence.
Positive-length strict-spectrum ports have no endpoint at a pole;
delta=0 ports are strict CROSS. The only cap ports left by this
argument are monomial intervals [0,nu], 0<nu<1/2, and their exact
reflections, whose parent middle and one outer incidence are both the
original protected faces. Half-terminal monomials at any spectrum have
been excluded by their cost-free retuning to delta=0.

Those two zero incidences form the actual marked MAIN edge uv in one
shaded triangle. The edge has two incident triangles, and they belong
to distinct ports since ports pair across MATCHING edges. Thus at most
two such positive-length cap ports remain, adjacent to the mark.
This count does not identify their geometry, phase, or contribution.

The same boundary reduction holds for a competing maximum of value
at least Phi_D over the closed non-CROSS union if at least one STRICT
non-CROSS port is present. A seam-only constrained maximum requires its
own documented argument; it is not covered by a feasible qG segment here.

Ordinary positivity is not an all-boundary theorem. Protected zero
faces remain, the possible marked cap corners remain, and the full
spectral/filling phase still has to be controlled. No finite positive
ordinary multipliers, terminal geometric interpretation at a cap,
new developing representation, bound by Phi_D, or quantum period
conclusion is asserted at those residual cap configurations.

All arguments here concern the sharp continuum functional. They
use the exact original row/face constraints, both unused products,
the normalized eta word and the separately proved endpoint entropy.
They do not replace a signed polynomial by a new positive model or
interchange a shrinking spectral scale with N. Any later use for the
original finite source must retain its exact scalar zeros and the
independently proved coefficient upper/identification statements.

## Review scope

Root and a separate internal reader checked the full analytical argument:
the fixed-load spectral exclusions, original full-fiber geometric segment,
latent endpoint triangle split, simultaneous cap and diagonal retuning,
all directional singular gains, connected supported-graph tight cut,
and the restricted non-CROSS value and strict-margin hypotheses. Both
readers separately checked the half-terminal monomial refinement. These
are internal proof reviews, not external peer review. No numerical
asymptotic audit, finite-source lower bound, or volume inequality is
claimed. The possible ordinary-multiplier consequence is deliberately
left to a separate addendum.
