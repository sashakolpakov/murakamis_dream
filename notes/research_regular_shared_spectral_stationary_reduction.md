# What a regular original shared stationary point actually implies

Unpublished workspace research reduction, 31 October 2026. This audits the hypotheses
of the conditional signed-circle/group/fan theorem. No strong duality,
concavity in the two rows, or separate weighted local maximality is
assumed. The result is a first-order reduction on specified smooth
strata of the original shared incidence problem, at every fixed width.

## 1. The exact functional being differentiated

For a LEFT port write its original limiting degrees, in order (x,b,c,y),

    q=(xi,mu,1-nu,nu-mu-xi),
    0<=mu<=nu<=1/2, 0<=xi<=nu-mu.                 (1)

Let alpha_delta(t)=4[cos^2(pi delta)-sin^2(pi t)] and Lambda_delta(t;x,y)
be the positive root of the original cleared tail recurrence. Define

    B_delta(mu,nu)=int_0^mu log|alpha_delta| dt
                            +int_nu^(1/2) log|alpha_delta| dt,
    Phi_delta(mu,nu,l)=int_mu^nu log Lambda_delta(t;exp(l),1) dt,
    h_delta=B_delta+inf_l[Phi_delta-xi l].          (2)

This keeps BOTH unused intervals. The omitted-half scalar has zero
exponential upper modulus, but its actual two phases are not discarded
when reconstructing the source. Formula (2) is the sharp interval
Legendre functional, not the fractional comparison t C(alpha). The
fractional obstruction specifically prevents replacing (2)
by that latter concave perspective and borrowing its duality.

The [global closed-domain coefficient-majorant theorem](research_global_sharp_coefficient_limsup_majorant.md)
now proves a uniform coefficient LIMSUP upper bound for the original
full-interval functional at both parities, including all closed degree
boundaries, the final spectral cap and sampled zeros. The
[regular theorem](research_sharp_regular_coefficient_limsup_majorant.md)
identifies (2) and its CROSS split with that full-interval functional.
Thus the reduction applies to regular extrema of a proved compact
original-source upper problem. An every-level remote coefficient limit
or nonzero prefactor is NOT needed for this upper-bound route. No lower
asymptotic or equality of a signed central sum with its upper rate is
asserted. Uniform coefficient coverage does not imply regularity or
geometric realizability of a boundary maximizer.

On a strict ordinary chart,

    0<mu<nu<1/2, 0<xi<nu-mu, 0<delta<1/2,

and neither row equals t_c=1/2-delta. The minimizing tilt in (2) is
unique and finite. Indeed, put eta=cos^2(pi delta)/sin^2(pi t)>0.
Apart from a t-only constant,

    log Lambda(t;exp(l),1)
      =l/2+log[cosh(l/2)+sqrt(sinh^2(l/2)+eta)],
    partial_l^2 log Lambda
      =eta cosh(l/2)/[4(sinh^2(l/2)+eta)^(3/2)]>0. (3)

Its first derivative ranges from 0 to 1. Thus Phi_ll>0 and its first
derivative ranges from 0 to nu-mu, proving existence, uniqueness and
smoothness of the tilt. The moving alpha zero has an integrable log;
as long as neither endpoint meets it, B is smooth by its explicit
logarithmic antiderivative. No convexity in mu or nu follows from (3).

## 2. Linear-target stationarity, without strong duality

Use one original row supply1 and each original ordinary face target1;
protected incidences have target0 and are removed, not regularized.
For CROSS retain its two half-row allocations as separate local
variables. Fix a smooth branch stratum in which every remaining local
inequality is strict, apart from the explicitly forced protected zeros.

At a relative-interior constrained local extremum of sum_e h_e,
its differential annihilates the kernel of the LINEAR target map.
Elementary finite-dimensional row-space orthogonality therefore gives
face multipliers lambda_f, regardless of redundant target equations.
All these multipliers are finite real numbers on this smooth finite-
dimensional stratum, so L_f=exp(-lambda_f)>0 automatically. Then EACH
local Lagrangian

    h_e+sum_(f at e) q_(e,f) log L_f               (4)

is STATIONARY in all its free local variables, with the same L_f at
every occurrence of f. This is not an assertion that (4) is maximal
over its full local polytope. A finite positive multiplier vector also
does not imply that every local inequality is inactive; the preceding
relative-interior hypothesis is substantive.

At an ordinary LEFT port, xi stationarity and (3) give
l=log(x/y), where x,y,b,c now denote these common positive weights.
After this equality, (4) is exactly

    F=mu log b+(1-nu)log c+int_mu^nu log L_delta(t;x,y) dt,
    L_delta=Lambda_delta/|alpha_delta|.            (5)

The identity int_0^(1/2)log|alpha_delta|=0 is used only here, after
retaining the actual outside products. The free row equations are

    L_delta(mu)=b, L_delta(nu)=c.                 (6)

Since delta_e is independent of every shared target constraint,
its first derivative at an interior spectral extremum is zero.
This derivative is taken at FIXED (mu,nu,xi) in (2), before applying
the tilt/envelope cancellation. At a solution of (6) it equals the
partial_delta of (5). It is not differentiation along an already
imposed equation c=b+(x+y)/sin^2(pi delta).

## 3. Classification of strict LEFT/RIGHT critical rows

Write A=x+y, P=xy, z=sin^2(pi delta), D=A^2-4Pz. The proved L_delta
is increasing before t_c and decreasing after t_c, from infinity down
to L_end=(A+sqrt D)/(2z). For a pre-pole stationary row q>0 use

    E_q=A+2qz+2sqrt(z)*sqrt(qA+P+q^2z),
    Q_q'=-log(E_q/sqrt D).

For a strict post-pole stationary row q>L_end use

    H_q=2qz-A+2sqrt(z)*sqrt(q^2z-qA+P),
    J_q'=-log(H_q/sqrt D).                        (7)

These are the absolutely normalized primitives of the original
cofactor. Both derivatives follow from the retained outside integrals;
no maximum property of the chosen row is used to differentiate its
stationary branch.

There are three possibilities for mu<nu:

* Pre/pre: (6) gives b<c. The weighted stationary action is
  Q_b-Q_c+log c, so its spectral derivative is log(E_c/E_b)>0.
* Post/post: (6) gives b>c>L_end. The action is J_b-J_c+log c,
  and its spectral derivative is log(H_c/H_b)<0.
* Pre/post: the action is Q_b-J_c+log c. Spectral stationarity
  is H_c=E_b. The two numbers are larger roots with the SAME product
  D, and their half-sums are A+2bz and 2cz-A. Strict monotonicity
  of that larger root gives exactly

      (c-b)z=A, R0=-E_b/H_c=-1.                 (8)

Thus a strict interior free-spectral LEFT critical point MUST be the
calibrated straddling branch. At this point the second row derivatives
of (5) are -partial_t log L(mu)<0 and partial_t log L(nu)<0;
the endpoint dependence is separable. The strict start/stop maxima
at FIXED delta therefore follow from (6)--(8), rather than being
assumed from the shared maximum. This checks the endpoint hypothesis
of the regular switching-window theorem on compact subcharts.

It does NOT make (5) a local maximum in delta: after following both
stationary rows with fixed weights, this branch has a spectral minimum.
Indeed sign(log(H_c/E_b))=sign((c-b)z-A) by the same larger-root
comparison, and c>b at (8); as delta increases this changes from
negative to positive.
That row-following variation generally changes the original shared
face loads and is not an admissible variation of the constrained
problem. It cannot exclude a shared maximum. RIGHT is the exact
original row reversal, exchanging b and c and the overloaded end.

## 4. CROSS and the exact protected exceptions

A regular CROSS allocation has two actual half-cofactor rows, ending
at 1/2, and their retained outer split. Its split stationarity gives
the same shared tilt; each free starting row solves L_delta(mu)=q.
Without assuming either start to be a weighted maximum, its branch is
Q_q if pre-pole and J_q if post-pole. Every one of
QQ,QJ,JQ,JJ therefore has strictly NEGATIVE free spectral derivative
when all displayed weights are positive, by (7). A regular CROSS
port cannot have 0<delta<1/2 at a free spectral critical point.
Its remaining regular possibility is the complete boundary delta=0;
delta=1/2 and terminal/pole rows remain separate boundary strata.

Protected cases are specialized in the literal source BEFORE a tilt:

* A protected LEFT overloaded c makes the whole finite sector zero.
* If x=0 or y=0, the tail is its exact one-monomer product. Its
  outer degree is forced, so no finite log(x/y) tilt is used. Equations
  (5)--(8) still follow for the FREE rows by that monomer action,
  with P=0. These are the one-outer-line fan cases.
* If b=0 with x,y>0, the start is exactly mu=0. Its sole-start
  primitive is Q_0, with E_0=A+2sqrt(zP). A pre-pole free stop c>0
  has log(E_c/E_0)>0. A post-pole free stop is critical precisely
  when H_c=E_0, giving c=A/z. This is the middle-line case.
* If b=0 and one outer is also protected, then P=0 and E_0=A=sqrt D.
  A strict pre-pole stop has E_c>A, and a strict post-pole stop has
  H_c>A. Its spectral derivative is positive in either case.
  Consequently there is NO free 0<delta<1/2 Green critical point
  with this double zero and nu<1/2. Equality forces the terminal
  nu=1/2, which is not covered by the regular argument.

For a CROSS half with protected middle, use Q_0. Its derivative is
negative if both outers are positive; it is zero only if the half is
a genuine one-positive-weight monomial. In the actual simple-white
plat an outer MATCHING pair cannot be the two protected MAIN faces.
There are only two protected faces, and the four port labels are
distinct. Thus BOTH CROSS halves cannot be monomial simultaneously:
if one outer is protected, both would additionally need both middles
protected. At least one half has strict loss. Hence the preceding
CROSS exclusion survives every allowed protected pattern, provided
its other local rows/splits are regular. No finite cross endpoint
with a forbidden zero outer unit is silently inserted.

At delta=0 a centralizer eigenratio tending to1 does NOT imply C=I:
the outer product is parabolic and the collar's removable divided
difference retains a nonzero limit. No kernel or identity assertion
is made from that ratio. The existing endpoint entropy/chain theory
is the relevant separate input there.

## 4a. A one-sided nonterminal maximum cannot have delta=0

There is a stronger statement for MAXIMA, without any local weighted
maximum assertion. Fix any 0<=mu<nu<1/2 and any allowed closed outer
degree 0<=xi<=nu-mu. Put z=sin^2(pi delta) and restrict
0<z<cos^2(pi nu), so the entire fixed interval remains pre-pole.
At any positive outer weights, q=L_delta(t) is the positive solution
of sin^2(pi t)=(1-z)q^2/(q^2+Aq+P). Differentiating gives

    partial_z log L_delta(t)
      =(q^2+Aq+P)/[(1-z)(Aq+2P)]
      >=1/[2(1-z)].                              (8a)

The inequality is exactly 2q^2+Aq>=0. It is UNIFORM in the outer
tilt, not a claim restricted to the minimizing tilt. Integrating
first in z and then in t yields

    int_mu^nu log L_delta(t;exp(l),1)dt
      >=int_mu^nu log L_0(t;exp(l),1)dt
                       -(nu-mu)/2 log(1-z).

Since the total half-alpha integral is zero, (2) is the infimum of
these integrals minus xi l. Taking that infimum preserves the same
uniform additive gain:

    h_delta(mu,nu,xi)
      >=h_0(mu,nu,xi)-(nu-mu)/2 log(1-z)>h_0.      (8b)

At mu=0 the logarithmic endpoint is integrable and (8a) is used on
(0,nu] before taking its integral limit. At xi=0 or nu-mu the same
tilt-uniform inequality applies to the limiting infimum. Alternatively
the literal one-outer monomer has L=A sin^2(pi t)/(cos^2(pi t)-z),
whose logarithmic z derivative is 1/(cos^2(pi t)-z)>0. Thus neither
protected starts nor a closed outer-degree endpoint invalidate (8b).

Changing only this port's delta leaves EVERY original face degree
and target fixed. Consequently a maximum of the stated sharp shared
functional cannot have a positive-length, nonterminal LEFT/RIGHT
port at delta=0. Diagonal length0 and terminal nu=1/2 are deliberately
excluded. For a fully regular maximum away from delta=1/2, every
one-sided port is therefore a strict positive-spectral straddler,
whereas every regular CROSS port is complete. Mixed endpoint Green
ports are needed for general stationary data, but not for this
regular MAXIMUM reduction.

## 5. Original face angles and the integer overload

At any stationary local branch just classified, the ordinary weight
derivatives of its stationary action are its original degrees q.
This is the ordinary envelope rule at a stationary branch, not a
strong-duality assertion. The physical triangle derivative
gives alpha_(t,f)=theta_(t,f)/(2pi), with each triangle load sum1/2.
The signed continuation retains the original output character:

    CROSS: q=alpha_input+alpha_output,
    LEFT:  q=alpha_input-alpha_output+e_c,
    RIGHT: q=-alpha_input+alpha_output+e_b.         (9)

The signs and integer terms come from the actual local primitive,
including Log c (respectively Log b), and its prescribed continued
root. They are not the fractional t alpha loads of an envelope.
At a protected line its alpha corner is exactly zero, by the literal
line limit, so its zero target remains unchanged.

Summing (9) at each original ordinary face yields exactly

    sum_(t incident f) sigma_t theta_(t,f)
                             =2pi(1-o_f),         (10)

where o_f is the INTEGER number of incident LEFT/RIGHT overloaded
middles. Every strict one-sided overload has q_f>1/2, so the target1
allows at most one, while a protected target0 allows none. Thus
o_f in {0,1} on this regular stratum. Equation (10) is an automatic
consequence of the original targets and first-order equations, with
no independent maximization or source factorization.

## 6. Dependency audit: what is proved, what still is not

For the smooth stratum described here, first-order shared stationarity
automatically supplies common finite positive weights, all row and
tilt equations, the straddling signed
primitive and R0=-1 at every positive-spectral one-sided port, complete
spectral parameters at every regular CROSS port, the literal allowed
single-line adapters, and the integer face-angle equations (10).

Global uniform coefficient-majorant coverage is now proved separately
on the entire closed domain; neither that upper theorem nor an unnecessary
remote coefficient LIMIT is a remaining hypothesis here. The following
issues remain:

1. Relative-interior regularity: finite positive ordinary multipliers
   do not remove ordinary zero incidences, diagonal/terminal rows,
   spectral endpoints, or active structural flow facets. The separate
   [pole-endpoint exclusion](research_sharp_interval_pole_endpoint_exclusion.md)
   removes positive-length endpoint/pole contacts from genuine maxima,
   without asserting that every other boundary is regular.
2. The shared Z/2 face-character solution. The actual incidence signs
   must still satisfy epsilon_(e,f)=gamma_f+kappa_e on the original
   allowed incidence graph. The real target equations (10) do not
   impose these mod2 cycle conditions.
3. A proof that inconsistent-phase cancellation beats Phi. Its positive
   envelope may exceed Phi, so a relative exponential loss is not
   by itself the desired absolute comparison.

Once the shared sign cocycle in2 is supplied on the stated regular
real branches, the signed developing-disk/group dictionary
uses (10) and the literal original marks to construct the comparison
representation. Its original cup/cap/prefix and raw-line checks are
still REQUIRED, but are supplied by that lemma rather than by an
unproved new contributing-mode assertion. The new
direct-fan theorem then supplies canonical volume and a uniform fixed
peripheral-word gap on its stated regular branch list. Neither theorem
needs local weighted strong duality. If some remaining ports instead
lie at noncross delta=0, their correct endpoint tangent adapters must
also be retained; one must not replace their collars by identity.

Here is the explicit mixed endpoint adapter. At a tangent delta=0
Green port the frozen original reflection calculation gives

    C=I+i r(P+I),
    r=(eta_c T_c-eta_b T_b)/(2(x+y)) real,

including its one-line and two-line formulas. Normalize the common
tangent point to infinity and its two outer white planes to Re w=0,1.
Their original raw product is P=-[[1,2],[0,1]]. Therefore C acts by
w->w-2ir, preserving BOTH outer planes. The proved simultaneous head
conjugations then carry the middle plane and all three ordered
contacts. This establishes the same within-copy shaded pairing as
the positive-spectral half-turn, with no inference from eigenratio1.
Its entire peripheral image is parabolic and preserves the common
horosphere. The old tangent signed local fan identity and new
intersecting fan identity may therefore be summed in ONE developed
family and the SAME original two-ball fundamental chain. At least one
positive-spectral strict Green port still gives the fixed trace-zero
meridian and uniform gap. If all spectral coordinates are0, use the
existing endpoint noncross-mass gap, not a new trace-zero claim.

The retained omitted-half modes give U0=+/-pi i at (8), not zero.
Their corresponding central eigenvalue choices +/-i give the SAME
order-two PSL collar. Reversing its selected eigenline also leaves
that PSL collar unchanged. The compact-peripheral canonical volume
is independent of which fixed endpoint is used, by the proved
horosphere-to-axis contraction. Thus the real comparison does not
require selecting a complex contributing mode or proving a nonzero
intersection with the original Fourier cycle. Those questions belong
to a lower-bound/contribution theorem, not this conditional upper
bound. No retained finite scalar or original framing is being deleted;
their convention is distinguished from a claimed contributing saddle.

No arbitrary KKT datum is asserted to be a limit of these coherent
regular solutions. This first-order classification removes a genuine
local-maximality assumption but does not close the remaining global
phase and compact-boundary problems.


## Dependencies and verification scope

The original finite rows and retained scalars are in the
[four-state source identity](research_original_one_sided_four_state_transfer.md).
The weighted primitives and their derivative constants are in the
[LEFT envelope proof](actual_global_left_weighted_spectral_envelope.md).
The [fractional obstruction](research_fractional_one_sided_geometry_obstruction.md)
is why no perspective concavity or local strong-duality claim is imported.
The remaining [face-sign criterion](research_spectral_face_sign_cocycle.md),
[regular group sewing](research_regular_signed_spectral_group_sewing.md), and
[direct-fan fundamental chain](research_critical_circle_fan_fundamental_chain.md)
retain the original source and canonical volume conventions. The tangent
endpoint matrix is the literal formula in
[marked signed development](actual_fejer_marked_signed_development.md).

The global coefficient-majorant theorem supplies only its stated upper bound. These reductions do not supply a lower coefficient limit, an incompatible-phase comparison with complete volume, or regularity and geometric control of every compact-boundary maximum.