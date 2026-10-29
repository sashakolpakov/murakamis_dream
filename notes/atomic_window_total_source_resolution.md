# Exact total-source resolution of every compact atomic Cauchy-pole cluster

28 October 2026. All artificial atomic Cauchy poles in the full-Psi
scalar period can be removed simultaneously by an exact WHOLE-SOURCE
identity. This includes compact clusters with dependent atomic
characters; no independence or transversality is needed. The resulting
source uses the same full literature Psi functions and Gaussian,
with one fixed interval variable per atom. Its normal critical
scheme is the actual nine-atom scheme, with independent nondegenerate
normal blocks. Atomic interval endpoints have no finite regular
stationary points.

This is a source identity, not a declaration that separately localized
bare/cut terms vanish. All original cups, ordinary caps, full marked
cap and external scalar lines remain unchanged. It removes the
meromorphic-intersection mechanism before asymptotics. It does not
prove a global geometric coefficient or control zero ends and
dilogarithmic degenerations by itself.

The [audit](../experiments/audit_atomic_window_total_source_resolution.py)
and [results](../experiments/atomic_window_total_source_resolution_results.json)
check nine original whole-word source identities at independent moment
parameters, with genuinely present high tails and no intermediate head
projection. They also check the normal determinant, finite endpoint
exclusion, and exact interval kernels. The key tail support scope has
been independently checked by the other two proof agents.

## 1. The source annihilates every nonempty atomic high-tail product

Start with the ORIGINAL convergent full-Psi flow chamber, after or
before its valid head-Hardy forest contraction. Write s_j=A_j/t_j for
its atomic Cauchy ratios. The continuous coefficient-independent
support theorem in
[the flow-cycle proof](actual_full_psi_scalar_flow_cycle.md)
states that EVERY feasible whole-source atomic order satisfies

    0<=h_j<=d=N-1.                                (1)

Let L_N denote the COMPLETE original head/source pairing, at fixed
moment variables t and Gaussian tuple xi. Evaluate the exact finite
cup/cap polynomials first; the full marked row is restricted by total
degree as previously proved. No Ward identity is reapplied per sector.
For any subset S of atoms,

    K(s)=1/(1-s)=K_N(s)+s^N K(s),
    K_N(s)=sum_(h=0)^(N-1)s^h.                     (2)

Expand (2) in the original common chamber |s_j|<1. Every term with a
nonempty tail subset has at least one order h_j>=N and therefore NO
feasible whole-source route by (1). Its L_N pairing is zero, pointwise
in all t and xi and independently of the coefficients at the other
atoms. Consequently

    L_N[ product_j K(s_j) ]
      =L_N[ product_j K_N(s_j) ].                  (3)

One may replace any selected subset instead of all atoms. In the
common chamber the right side is a finite Laurent polynomial in the
moment variables. Equation (3) identifies the complete head pushforward
with that polynomial; it is stronger than equality after a special
full-Psi or Gaussian integration.

The statement does NOT remove arbitrary head-reset tails or Laurent
coupons. A microfactor that heals an out-of-range index can invalidate
(1). No such new operator or arbitrary head-angle cutoff is inserted
here. The proof applies to the original strict whole word and its
authorized original source.

## 2. Pole clusters disappear in a genuine holomorphic representative

Each K_N is a polynomial. At s=1,

    K_N(1)=N,

so the numerator 1-s^N cancels the Cauchy denominator exactly. Replacing
the participating atoms of ANY compact cluster by (3) makes the entire
source holomorphic across that cluster. Multiplying these polynomials
does not require independent characters: coincident poles, undirected
circuits and all higher intersections are covered at once. Other true
singularities of the full functions or coordinate boundary are a
separate issue.

This gives a precise regrouping of the TOTAL source represented by
P_bare+W_cut in
[the exact pushforward](actual_full_psi_cut_wall_pushforward.md).
The regrouping is performed by the algebraic tail annihilator (1),
not by defining W_cut to be a difference. Separate cluster cutoffs
can destroy the Fourier support argument and create side prisms;
their individual period values are not asserted to cancel. The whole
current has the explicit pole-free representative (3).

After the valid head-Hardy forest contraction, the head kernel is a
finite Laurent polynomial. Its complete
head Cauchy integral is independent of ALL finite nonzero head radii.
The head radii can be chosen fixed, independently of t, and there are
no atomic-pole residues when changing them. Positive factorial monomials,
Gaussian coefficients and all original cap factors remain explicit.

## 3. Keep full Psi and resolve the window by one interval

On the principal logarithmic chart put

    B(s)=Log s/(s-1), B(1)=1,
    K_N(s)=N B(s) integral_0^1 exp(Nu Log s)du.      (4)

The right side is exactly (s^N-1)/(s-1). Near ANY compact cluster
s_j=1, choose Log_j 1=0 for each atom. Then every B(s_j) is holomorphic
and nonzero. All dependent-cluster source densities are regular.
The interval endpoints, original factors N and every logarithmic mark
are retained. At other logarithmic sheets of s=1, do not separate a
compensating pole and zero; use the polynomial or its selected local
chart instead.

Thus (3)--(4) give a full-Psi/continuous-Gaussian period with a fixed
interval per atom and the original fixed cap intervals if desired.
It has no atomic Cauchy poles and no finite matrix source. Its number
of integration variables depends on the word, not on N.

For absolute convergence use the principal-log estimate already proved
for cap intervals:

    |B(s)|<=C(1+|log|s||)exp(-max(0,log|s|)).

On any fixed compact u-path in 0<=Re u<=1, this bounds the interval
density in (4) by

    C N(1+|log|s||)exp(d max(0,log|s|)+C_path N).   (5)

Choose arbitrary fixed head radii. The explicit Gaussian coefficients
of A_j have logarithmic moduli at most C(1+sum|xi|). On a radial
moment piece t_j=-r_j, (5) is therefore bounded by a polynomial in
1+sum|xi|+sum|log r_j| times

    N^B exp(CN(1+sum|xi|)) product_radial r_j^(-d).

The exact full-Psi ray measure has modulus
sqrt(1+r_j)r_j^(N-1)dr_j/(2*pi). Its power cancels r_j^(-d)
because d=N-1. The remaining logarithms are integrable at zero;
the continuous Gaussian dominates exp(CN sum|xi|). Fixed outer
circles are compact. This proves joint absolute convergence of the
new interval source directly, with fixed head radii. No divergent
high-tail integral is evaluated in this new chamber: tail cancellation
was proved first in the original common chamber.

The source logarithm seams are explicit relative interval derivatives.
For L->L+2*pi*i the difference of the two densities N L e^(NuL)/(e^L-1)
is

    d_u{[e^(Nu(L+2*pi*i))-e^(NuL)]/(e^L-1)}.

Its primitive vanishes at u=0 and u=1. Thus angular seams do not create
an omitted source period. Full-Psi moment-circle endpoints and their
paired radial ends still match by the original full-function monodromy.
All these matches can also be checked by integrating the interval
first, which recovers the single-valued polynomial K_N.

## 4. The joint interior critical scheme is the actual geometric scheme

Write T_j=Log t_j and U_j=2*pi*i*u_j. On a chosen local sheet the
window logarithm is

    L_j=Log A_j-T_j-2*pi*i*n_j, n_j in Z.

On a recorded full-Psi leading-phase cell, including its exact integer
monodromy expansion, the extended phase contains

    W_ext=sum_j [epsilon_j Li_2(e^T_j)+U_j L_j
                                      +2*pi*i*m_j T_j]
                   +original Gaussian, reflected and cap phase. (6)

Each m_j is its retained integer ray/monodromy mark. The full-function
symbol is applied only where its stated uniform phase is valid;
dilogarithmic divisors such as t=1 require separate treatment.

At an interior joint critical point,

    T_j=Log A_j-2*pi*i*n_j,
    U_j=2*pi*i*m_j-epsilon_j Log(1-A_j).            (7)

The normal Hessian in (T_j,U_j) is

    [ epsilon_j A_j/(1-A_j)   -1 ]
    [          -1             0 ],

with determinant -1. It is independent of ALL incidence ranks and
circuits. The normal blocks are independent over the external head,
Gaussian and cap variables. Thus every regular compact Cauchy cluster
is resolved by nondegenerate normal pairs, not an unresolved
meromorphic intersection.

Eliminating (T,U) in (6) yields exactly the actual nine-atom action
with its original integer logarithmic marks. The extra constants
from n_j are real phase constants. Its full critical equations are
the original Hurwitz/cap representation equations, and its critical
regulator satisfies
[the proved sharp representation-volume bound](regular_critical_values_and_representation_volume_bound.md).
The factor B(1)=1 and determinant -1 give a nonzero LOCAL normal
density. They do not determine the original global normal/thimble
cycle coefficient.
For a positive oriented shape epsilon_j Im A_j>0 on its ordinary
half-plane branch, with m_j=0, (7) gives
0<Re u_j<1/2. Thus its normal interval point lies strictly inside
the actual allowed vertical strip; an endpoint-fixed compact
complex interval path can pass through it while preserving (5).
This is an allowed source-path statement, not a noncancellation proof.

The product source cycle is maximal totally real on a regular phase
chart: order its coordinates (T,Gaussian,U,cap,head Z), and the real
parameters by their moment/Gaussian/interval paths and head angles.
The complex Jacobian is block triangular with nonzero path derivatives
and iI on the head angles. Thus interior stationarity of the complex
phase is full holomorphic stationarity here. This is not merely a
stationary real-part envelope.

## 5. Atomic interval endpoints cannot be finite regular stationary points

At u_j=e in {0,1}, the derivative in U_j is omitted, but T_j is still
a free regular moment coordinate. Stationarity in all the remaining
complex directions forces

    -epsilon_j Log(1-e^T_j)-2*pi*i*e+2*pi*i*m_j=0.

Exponentiating gives 1-e^T_j=1, so t_j=0. There is NO finite nonzero
regular endpoint stationary point. The same applies to simultaneous
atomic endpoints. A constrained boundary maximum without the other
stationarity equations is not covered.

The original CAP interval endpoints are different: they give central
physical meridians and value zero under the separately proved regular
endpoint theorem. Moment outer endpoints are matched parts of one
full-Psi relative cycle, not independent new boundaries. Log seams
are matched by the relative derivative above. True zero ends,
phase singularities and escape in later contour deformations still
need their recorded estimates or further source analysis.

## 6. The actual interval variables have a radial Legendre/flow interpretation

The new variables also make the proposed flow/Rivin structure explicit
on a stated positive chamber. Use the unshifted marks m_j=0 and set

    T_j=sigma_j+i*vartheta_j, U_j=2*pi*i*u_j,
    V=rho+i*theta,
    Log A_j=a_j.V+i*pi*nu_j.

V contains the head and the transformed Gaussian logarithms. The
original cap variables are likewise purely imaginary multiples of
their real interval parameters in this calculation. All remaining
quadratic coefficients are real. Consequently the WHOLE imaginary
action has the form

    Im W_ext=sum_j [epsilon_j Im Li_2(exp T_j)
                                  -2*pi*u_j*sigma_j]
                      +rho dot F(theta,u,cap),       (8)

where F is the original affine head/Gaussian flow expression. More
explicitly its atomic part is 2*pi*sum_j a_j u_j; the original real
quadratic, reflected, sign and cap terms supply the remaining affine
terms. Thus minimizing over the unrestricted rho gives a finite value
exactly when F=0. These are linear equations, not additional guessed
geometric constraints. Equivalently they follow by differentiating
the imaginary action in the head/Gaussian radial variables.
This is an identity for the LEADING phase W_ext. Exact q half-steps
and d=N-1 rather than N remain in the recorded finite-N amplitude;
it is not an equality for the full finite-N logarithm of the density.
The unrestricted radial minimization is in the complexified coordinate
space. The original real Gaussian path has
eta_s=sqrt(pi)(1+i*s)xi_s, so its real and imaginary parts are linked;
it does not already supply that independent radial polarization.

For one atom assume epsilon*vartheta in (0,pi). Put

    alpha=epsilon*vartheta, beta=2*pi*u,
    gamma=pi-alpha-beta.

If alpha,beta,gamma are all positive, the radial expression

    f(sigma)=epsilon Im Li_2(exp(sigma+i*vartheta))-beta*sigma

has derivative -epsilon Arg(1-t)-beta and strictly positive second
derivative epsilon Im(t)/|1-t|^2. Its derivative tends to -beta at
minus infinity and gamma at plus infinity. There is a unique global
minimum, at

    exp(sigma)=sin(beta)/sin(gamma).

At this minimum -epsilon Arg(1-t)=beta, so EXACTLY

    min_sigma f=epsilon D(t)
               =Lambda(alpha)+Lambda(beta)+Lambda(gamma). (9)

Combining (8)--(9) on F=0 gives the sum of the positive tetrahedral
volumes, OFF criticality in the remaining angular variables. The
actual interval coordinate u is therefore beta/(2*pi). The imaginary
parts of the other normal equations impose the affine angle matching
vartheta_j=a_j.theta+pi*nu_j-2*pi*n_j. On any fixed marked chamber,
these and F=0 are the actual linear angle/flow constraints; positivity
cuts out a convex domain. The usual strict tetrahedral concavity
holds on the quotient by directions leaving every angle unchanged.

This is an identity for the newly constructed ORIGINAL source, not
a newly defined positive model. Its scope is essential: the original
signed nine-atom atlas is not known to place its geometric point in
one simultaneous positive chamber, and such a choice cannot be
assumed from geometricity alone. The previously found indefinite
actual-phase Hessian precludes repairing that issue by arbitrary
real Gaussian changes. Transport to a positive chart and control of
the ORIGINAL interval cycle still require proof. Equations (8)--(9)
explain which flow and volume optimization that transport must carry;
they do not supply its missing geometric coefficient.

## 7. What has and has not been canceled

The compact artificial Cauchy-pole clusters of the total source are
removable, including arbitrary dependent circuits. The local L1-pole
growth countermodel cannot be applied to the regrouped holomorphic
kernel as though its uncanceled denominator were still present.

This does not prove that every localized compact nonstationary piece
has a sharp exponential bound: artificial cutoffs have side currents,
and the new fixed-interval phase has its genuine critical/endpoint
geometry. It supplies that geometry explicitly. In particular the
normal interval period at fixed A is EXACTLY the original finite
v_(epsilon,N)(A); its global normal-cycle coefficient cannot be read
off from the local Hessian. The known coefficient-one atom region in
[the full Euler-region theorem](full_euler_atom_dilog_and_endpoint_regions.md)
is an anchor, not an assertion about every positive shape.

What remains includes source-compatible analysis of the zero ends and
dilogarithmic degenerations, and a nonzero selected geometric lower
bound. The exact pole-free representative and normal resolution
remove a specific obstruction to those steps; they do not constitute
the broad volume conjecture by themselves.
