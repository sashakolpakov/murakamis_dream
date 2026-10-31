# Odd half twists in the full Conway Newton source

29 October 2026. A literal half twist has an explicit triangular
transport matrix in the FULL Newton algebra. It yields a new uniform
Newton-coordinate bound for every auxiliary-color alias. At complete
colors, the already selected local coherent coefficient and a concave
global envelope prove the original-source asymptotic for arbitrary
fixed half-twist patterns in every retained robust Conway factor.

This note concerns exact transport and complete colors. The later
[supporting-plane theorem](actual_odd_conway_uniform_mixed_source_gap.md)
supplies the whole mixed-color gap for C(FG), with both children robust;
it excludes C(A). Neither result by itself supplies a long-filling
theorem. The changed source is not obtained by dropping phases from
the positive source.

## 1. Exact full-algebra half-twist transport

Use the original pair algebra H_N, actual turn T, crossing R, and
Newton basis Bhat_v of the [pure auxiliary-color theorem](actual_pure_conway_auxiliary_color_leaf.md).
Put D=N-1, q=exp(pi i/N), x=q^D=-q^-1, kappa=q^(D^2/2), with its
original unreset half-Cartan mark. For epsilon=+1 or -1 define

    T_epsilon(f)=T(R^epsilon T(f)).

Then, for EVERY 0<=v<=D, exactly in the full repeated-root algebra,

    T_epsilon(Bhat_v)
       =kappa^epsilon (-1)^v
          sum_(r=0)^v q^[epsilon v(r+1)]
                       [v choose r]_q Bhat_r,
    [v choose r]_q=s_v/[s_r s_(v-r)]>0.                 (1)

In particular the actual odd leaf is

    h_j^epsilon=T(R^epsilon L_j)=T_epsilon(h_j).        (2)

Proof. The literal continuant source identity gives
T_-(Bhat_v)=kappa^-1 f_v. One can also obtain it by comparing the
FULL two-band formula for every actual L_j with the pure-color
formula: the L_j form a basis, so this comparison proves the linear
identity on the entire algebra, not only its values at the nodes.
The independently proved finite continuant expansion is

    f_v=x^v sum_(r=0)^v (Q^-v;Q)_r Q^r P_r/F_r^3,
    P_r=q^(r^2) B_r, F_r=(Q;Q)_r, Q=q^2.

Insert s_r^2=(-1)^r q^[-r(r+1)]F_r^2 and
(Q^-v;Q)_r=(-1)^r Q^[-vr+r(r-1)/2]F_v/F_(v-r).
The coefficient of Bhat_r becomes
x^v q^[r^2-2vr] {v choose r}_Q
=(-1)^v q^[-v(r+1)] [v choose r]_q. This proves (1) for
epsilon=-1, including v>D/2 and every normal coordinate.

The actual inverse crossings are coefficient-conjugate polynomials
in the real Newton basis: their nodal values are reciprocal unit
phases and their first logarithmic derivatives are purely imaginary.
Uniqueness of Hermite interpolation proves the full polynomial
identity. The turn reverses this real basis, so it commutes with
coefficient conjugation. Conjugating the preceding formula proves
(1) for epsilon=+1. No Hermitian positivity is being asserted.

## 2. A uniform full-Newton bound for the actual color alias

Write the exact pure split h_j=C_j+A_j. Every A_j has support
v>=ceil(N/2), and each of its coefficients has modulus at most N/2.
More precisely its support is v>=N-h for a low complementary color
1<=h<=floor(N/2). The actual half-twist alias is T_epsilon(A_j).
Equation (1) gives the exact coefficientwise upper bound

    |[Bhat_r]T_epsilon(A_j)|
       <=(N/2) sum_(v=max(r,N-h))^D s_v/[s_r s_(v-r)].   (3)

Let J(t)=integral_0^t log(2sin(pi u))du. The endpoint-uniform
factorial estimate then gives, uniformly over ALL physical colors
and all Newton indices,

    |[Bhat_r]T_epsilon(A_j)|
       <=poly(N) exp[N k(r/N)],
    k(u)=-2J(u/2), 0<=u<=1.                           (4)

Here and below a zero coefficient causes no difficulty. Indeed the
largest possible exponent in (3), after relaxing its lower bound
to v/N>=max(u,1/2), is

    max_(w>=max(u,1/2)) [J(w)-J(u)-J(w-u)].

Its derivative in w is log[sin(pi w)/sin(pi(w-u))]. The maximum
is at w=(1+u)/2. Reflection J(1-a)=-J(a), followed by duplication
J(2a)=2J(a)-2J(1/2-a), reduces its value to -2J(u/2).
The argument includes u=0,1 by continuity; the exact factorial
errors are O(log N) uniformly there.

The maximum of k is at u=1/3 and equals v_3/pi, where v_3 is the
regular ideal tetrahedron volume. On u>=1/2 it is strictly decreasing,
since k'(u)=-log(2sin(pi u/2))<0. In particular
k(1/2)=-2J(1/4). This is a coordinate bound for the original normal
source, so it may be propagated through the positive Newton product
and the actual index-reversing turn. It is not a bound in a nodal
quotient or an unspecified operator norm.

There is a useful exact small-color estimate as well. Set v=N-t.
Root factorial reflection gives

    [N-t choose r]_q=[t+r-1 choose t-1]_q
                      <=binomial(t+r-1,t-1)
                      <=binomial(N-1,t-1).             (5)

The middle inequality follows from the nonnegative coefficients of
the ordinary Gaussian polynomial at a unit root. Thus for
1<=h<=floor(N/2), every alias coefficient is at most

    (Nh/2) binomial(N-1,h-1).                          (6)

In a corridor h<=delta N, delta<1/2, this costs at most
poly(N) exp[N H(delta)], where
H(delta)=-delta log delta-(1-delta)log(1-delta)->0.
For h=1 each transport coefficient actually has modulus one:
[D choose r]_q=1. Thus an alias can occupy ALL Newton coordinates,
including their normals; it is no longer square-zero under products.

A sharper color-dependent envelope is obtained by keeping chi=h/N
in (3): it is

    k_chi(u)=J(u+chi)-J(u)-J(chi),  u<=1-2chi,
    k_chi(u)=-2J(u/2),               u>=1-2chi.         (7)

These expressions agree at the joining point. This is an upper
envelope, not an assertion that the signed alias attains it.

## 3. Complete odd coefficients: the exact selected source

At j=N there is no alias. The old finite original-source transform
gives, with M=floor(D/2),

    h_N^-=exp(-i pi D/4)
                sum_(r=0)^M a_(N,r) W_(N,r) Bhat_r,
    a_(N,r)=N^2 s_(2r)/s_r^4.                         (8)

For reference W is fixed by the literal finite sums, not chosen as
a formal recurrence solution:

    A_r=sum_(v=r)^M Q^(-vr) F_(2v)/(F_v^3 F_(v-r)),
    D_r=Q^(-r^2)F_(2r)/F_r^3,
    W_(N,r)=kappa^-1 exp(i pi D/4)
                           (A_r/D_r)/[(-1)^r q^(r(r+1))].

The [selected high-index theorem](actual_pretzel_coherent_inner_gauss_elimination.md)
proves, uniformly on compact subintervals 1/4<u<1/2,

    W_(N,r)=sqrt(sin(pi u))exp(i pi u/2)[1+O(N^-1)],
    u=r/N.                                            (9)

The [actual quarter-transition theorem](actual_complete_circle_boundary_packet.md)
extends this same nonzero selected expression to a fixed neighborhood
of u=1/4. Its exponentially accurate source transport includes the
initial second channel and all coupling errors. Distinct recurrence
roots alone would not justify this extension.

At ALL indices the [two-branch source bound](actual_pretzel_all_index_backward_envelope.md)
gives |W_(N,r)|<=poly(N)exp[N E(pi r/N)], where

    E(pi u)=g(1/4)-g(u),  0<=u<=1/4;
    E(pi u)=0,           1/4<=u<=1/2;
    g(u)=J(2u)-4J(u).                                 (10)

The first identity is exact because g'(u)=2log cot(pi u).
Consequently the full coefficient envelope for a complete odd leaf
is the CONCAVE function

    g_tilde(u)=g(max(u,1/4)), 0<=u<=1/2.               (11)

It is constant below 1/4 and agrees with g above it; its derivatives
join at zero. The positive-half-twist formulas are the coefficient
conjugates of (8)--(9), with the same envelope. This is a coherent
coefficient theorem; termwise absolute values in its original inner
factorial sum would give a different bound.

## 4. Arbitrary fixed half-twist patterns at complete colors

Fix any retained cylindrical robust factor and independently choose
epsilon_l in {0,+1,-1} at each of its individual leaves. Replace its
actual h_N leaf by T(R^epsilon_l L_N), leaving every product, turn,
mark and external normalization unchanged. Let Z_N^epsilon be this
literal raw closed source and Z_N^0 its pure counterpart.

Let x_(l,*) be the unique complete positive maximizing leaf labels.
The [strict-quarter theorem](actual_conway_strict_leaf_quarter_bound.md)
gives x_(l,*)>1/4 for every leaf of every such factor. Then

    Z_N^epsilon
      =exp[(i pi D/4)sum_l epsilon_l]
         a_E(0) N^(3/2) exp[N phi_E(0)]
         product_(epsilon_l!=0)
            [sqrt(sin(pi x_(l,*))) exp(-i epsilon_l pi x_(l,*)/2)]
         *[1+O(N^-1)].                                (12)

Here a_E(0)>0 and phi_E(0) are the original pure-source normalization
and action from the finite Conway packet. The displayed leading
coefficient is nonzero. Both parities, every normal direction and
every fixed mixture of half-twist signs are included.

Proof of the global source claim. Replace g by g_tilde only at the
odd-marked leaves in the complete variational action. Each retained
product action m is concave, and the support polytope is convex.
The resulting majorant action is therefore concave. By the strict
quarter theorem it agrees with the pure action on a neighborhood
of its strict complete maximizer. That point is still stationary
with negative definite Hessian in the free wire coordinates, hence
is its unique GLOBAL maximizer. A second maximum would give a
constant segment through that strictly concave neighborhood.

The complement of any fixed small central window therefore has a
strict exponential gap for the majorant. Equations (8),(10), the
uniform factorial estimates and the polynomial state count bound
the whole original complex sum there, before any cancellation.
On the central window every odd coefficient has (9), with its
original common phase in (8). The resulting smooth nonzero multiplier
of the positive summand is exactly the product in (12), evaluated
at the critical point. The already proved lattice Laplace argument,
or its real-parameter version with this smooth complex amplitude,
proves (12). There is no assumption of positivity of the odd source.

Thus its exponential rate is the same complete geometric action
2pi phi_E(0) as the pure factor. Identifying this with the half-twist
partner's actual volume also uses its literal shaded-face gluing;
volume invariance is not a substitute for the quantum proof above.

## 5. What is still needed for odd-coupon long fillings

The mixed half-twist CORE has its [proved uniform envelope g_tilde](actual_pretzel_global_core_spectral_gap.md),
including colors outside a fixed corridor, by the actual selected
mixed-source recurrence. Its high-index physical-color packet is
also known. Equations (3)--(7) bound the changed alias in the correct
FULL Newton coordinates. The subsequent
[supporting-plane theorem](actual_odd_conway_uniform_mixed_source_gap.md)
proves its exponential gap after arbitrary C(FG) composition, with
both children robust. The minimal C(A) remains outside that estimate.

In particular the alias is not confined to output indices above
one half and products containing two aliases no longer vanish.
The pure source's square-zero seed argument cannot be reused.
The separately proved [complex packet](actual_odd_conway_complex_color_packet.md)
and [actual marked deformation](actual_odd_conway_marked_peripheral_deformation.md)
now complete the required interfaces for the
[long-filled knot and link theorem](actual_odd_conway_long_filling_volume.md).

Audit: [full physical transport, alias bounds and complete-source calibration](../experiments/audit_actual_odd_conway_newton_transport.py).

The finite transport and alias checks are diagnostics for the exact formulas. They do not establish the asymptotic estimates by sampling.
