# The constrained Hessian of the original sharp source

31 October 2026. **analytical research reduction.**
This derives an exact second-variation test on the original shared transport
fiber. The local obstruction below shows why an odd MAIN four-cycle does
not alone supply an unstable direction. It is not a globally realized
stable maximum, an absolute source bound, or a volume theorem.

## 1. The actual fixed-spectrum row Hessian

Use the [full-fiber activation](research_full_fiber_sharp_boundary_activation.md)
and [stationary classification](research_full_fiber_sharp_stationary_classification.md). Work at a
classified datum with finite common positive ordinary weights, on its
actual protected-coordinate face. All ordinary incidences are positive.
For the restricted non-CROSS maximum, retain the hypothesis that its value
is at least Phi_D and that some middle load is strictly greater than 1/2;
then the small two-sided variations used below remain admissible.

At a LEFT Green write q=(xi,mu,1-nu,nu-mu-xi), with actual common weights
(x,b,c,y). Put

    g(t,l,delta)=log Lambda_delta(t;exp(l),1)-log|alpha_delta(t)|,
    a(t)=partial_l log Lambda_delta(t;exp(l),1),
    V=int_mu^nu partial_l^2 log Lambda_delta(t;exp(l),1) dt.

The alpha and Lambda are exactly those of the full sharp functional;
both unused intervals are retained. At the actual minimizing tilt,
V>0 when both outer incidences are ordinary. Differentiation of that
Legendre minimum gives, at fixed delta,

    d^2 h_delta = -g_t(mu) dmu^2 + g_t(nu) dnu^2
          -[-a(mu)dmu+a(nu)dnu-dxi]^2/V.              (1)

There is no omitted scalar or spectral normalization in (1). The common
weighted linear face terms have zero Hessian. A strict straddling Green
has g_t(mu)>0 and g_t(nu)<0, so (1) is negative definite in the free local
row coordinates. Protected middle coordinates are omitted, not varied.
If one outer incidence is protected, specialize the exact monomer first:
there is no independent xi coordinate or tilt, and only the two diagonal
row terms remain. RIGHT is the literal row reflection.

At a complete CROSS port the same argument at delta=0 applies: its start
lies before 1/2 and its stop after 1/2, so the two row signs in (1) again
give negative definiteness. Equivalently, write its entropy as the maximum
of C(alpha)+C(beta) over the actual latent two-triangle split. On all free
triangle coordinates, f''(t)=-2pi/sin(2pi t)<=-2pi. The projection to the
four original loads has squared operator norm at most 2. Consequently

    d^2 h_CROSS(q)[v,v] <= -pi ||v||^2               (2)

for every original row-tangent v, with protected coordinates removed.
This follows either by differentiating the unique latent optimizer or
directly from strong concavity and the same linear projection. The
permitted protected monomial half contributes no independent coordinate;
the other half supplies the remaining strict concavity.

Thus the negative fixed-spectrum row Hessian K is positive definite
on the product of the free noncap row-coordinate spaces. This does not
say that the joint row/spectral Hessian is negative definite.

## 2. Exact original-target Schur complement

Let v collect the noncap row displacements in any fixed linear row-simplex
coordinates. Let s collect the spectral displacements of the strict
Green ports. Hold the complete CROSS spectra at zero and cap spectra at
1/2 for this test. At the stationary datum write the second variation as

    Q(v,s)=-v^T K v+2v^T B s+s^T D s,              (3)

where B is the actual mixed row/spectral derivative and D is diagonal
because spectra are local to the original coupons. No separate local
maximum or local-to-global minimax exchange is asserted.

If there are no residual caps, let T be the original ordinary-face
balance map in these row coordinates: feasible v satisfy Tv=0. Redundant
face equations are retained harmlessly. If residual caps are present,
let T_0 be the noncap face map and T_cap the actual cap row map. A cap
action is identically zero at its held spectrum. Its free row displacement
w can compensate precisely T_0 v in im(T_cap). Hence set

    T=P T_0,

where P is the orthogonal projection onto ker(T_cap^T). Then Tv=0 is
exactly the condition that some actual cap displacement w makes the
original face targets unchanged. All ordinary loads are positive, so
these infinitesimal row displacements are realized by sufficiently small
positive and negative displacements in the original fiber. This
elimination is linear second-variation bookkeeping, not a change of the
source or a new merged-face theorem.

Define

    W=D+B^T K^(-1)B,
    R=T K^(-1)B,
    C=T K^(-1)T^T.

The Moore--Penrose inverse C^dagger is needed only for redundant target
equations. Since range(C)=range(T), every column of R is in range(C).
Completing the square, or a constrained quadratic minimization, gives

    max_(Tv=0) Q(v,s)=s^T [W-R^T C^dagger R] s,     (4)
    v_*=K^(-1)B s-K^(-1)T^T C^dagger R s.          (5)

Thus a positive eigenvalue of

    S=W-R^T C^dagger R                             (6)

excludes the alleged sharp maximum. A genuine maximum necessarily has
S<=0. Conversely S<=0 only passes this particular second-order test;
it does not establish a local maximum or a global maximum. The matrix
R^T C^dagger R is the exact nonnegative cost of repairing the row-optimal
spectral displacement to the original face targets.

The diagonal entries of W at a strict Green are positive. In fact the
local row-optimal response at held common weights is K_e^(-1)B_e.
For A=x+y, P=xy, z=sin^2(pi delta), D_0=A^2-4Pz and
C_0=A+2bz, the absolutely normalized stationary action has derivative
log(T_c/E_b), where

    E_b=C_0+sqrt(C_0^2-D_0),
    T_c=2cz-A+sqrt((2cz-A)^2-D_0).

These are the larger-root branch factors, distinct from the target map
T above. At (c-b)z=A, its second derivative is

    W_e=2(c-b) pi sin(2pi delta)/sqrt(C_0^2-D_0)>0. (7)

This is precisely the local weighted spectral minimum. It is
W, not S. The shared repair term in (6) cannot be discarded just because
the original incidence graph has an odd signed four-cycle. That cycle
is a phase statement; (4) is an unsigned constrained quadratic test.

## 3. An exact forced-edge mode with negative combined curvature

Take the actual protected-outer monomer specialization y=0 and

    (mu,nu,delta)=(1/6,1/3,1/4),
    (x,b,c)=(1,1,3),
    q=(1/6,1/6,2/3,0).                            (8)

The original row equations give b=L_delta(mu)=1 and
c=L_delta(nu)=3; the spectral equation is (c-b)sin^2(pi delta)=x.
Thus this is exact local Green stationary data with its original loads.
For reference, if u=tan(pi mu), v=tan(pi nu), r=tan(pi delta), the
retained monomer integrals give

    partial_delta h=2[atanh_abs(vr)-atanh_abs(ur)],
    atanh_abs(t)=(1/2)log|(1+t)/(1-t)|.

The original monomer Hessian in (mu,nu,delta) at (8) is

    [[-4pi sqrt(3), 0,            -4pi],
     [0,            -4pi/sqrt(3),-4pi],
     [-4pi,         -4pi,        -4pi sqrt(3)]].  (9)

Its fixed-degree spectral entry is strictly negative. Optimizing that
spectral displacement, equivalently differentiating the [sharp spectral action](actual_protected_outer_spectral_energy.md)
D_f(mu,nu-mu), gives the row Schur complement

    (4pi/sqrt(3)) [[-2,1],[1,0]].                 (10)

Its positive eigenvalue is a local fact. The forced ordinary MAIN edge
of this protected port is (x,c). The exact elementary circulation through
its neighboring port changes only the x and c loads of each of those two
ports, with opposite changes at the neighbor. In the Green row this fixes
mu and varies nu. Therefore (10) gives ZERO for the largest possible
Green second variation along this edge circulation. Following the optimal
spectral response cannot make it positive.

If the neighboring port is strict CROSS, its original row displacement
has two nonzero entries of opposite size s. Formula (2) gives at most
-2pi s^2. Hence the entire two-port circulation, even after the Green
spectrum is optimized, has strictly negative second variation for s!=0.
Allowing the CROSS spectrum to move from zero cannot repair this sign:
its mixed degree/spectral derivative is zero by evenness, and its pure
spectral second derivative is negative. The latter follows directly
from the outside-alpha and positive-root integrals; at least one genuine
half has a positive ordinary middle or two positive outers, so it is not
the zero derivative monomial exception.

This is an obstruction to the inference

    odd forced MAIN four-cycle => positive feasible second variation.

It uses the literal MAIN-supported circulation and original row loads,
not an arbitrary port-local variation. It does NOT exhibit a complete
diagram whose full stationary data realize (8) with that neighbor and
all other face targets, nor a stable full-source maximum. Other graph
directions may still yield a positive eigenvalue of (6).

## 4. What would settle this route

A general instability proof must control the original repair matrix in
(6), for example by producing some s with

    s^T R^T C^dagger R s < s^T W s.

Neither the positive local entries (7), the common-weight dominance, nor
the qualitative odd MAIN cycle presently proves that inequality. The
published relative phase bounds and the local cap obstruction are
independent of this exact Hessian reduction. No coefficient asymptotic,
signed-source cancellation, or absolute Phi_D comparison is deduced here.

Inputs: the published [full-fiber stationary classification](research_full_fiber_sharp_stationary_classification.md);
the exact [LEFT weighted spectral envelope](actual_global_left_weighted_spectral_envelope.md)
(its normalized branch derivative); the [protected-outer sharp spectral
action](actual_protected_outer_spectral_energy.md); and the already recorded
[local D_f nonconcavity](research_joint_entropy_triangle_decomposition.md). The new statements are the original-target
Schur complement and the precise failure of the elementary forced-edge
instability inference. No numerical test is needed for these identities.
