# The Rivin optimizer is a whole algebraic function of the boundary phases

Research proof, 27 October 2026. The positive geometric edge curve
and its conjugate place have an étale two-parameter **phase-ratio
map**. Its inverse is the unique constrained Rivin optimizer.
Consequently the optimizer shapes, peripheral norms, constrained
Hessian and all higher derivatives of the boundary potential are
algebraic functions of two independent multiplicative boundary
phases. The potential itself is a marked logarithmic regulator
period, with an explicit primitive.

This strengthens the earlier algebraicity over an already selected
meridian: it constructs the algebraic inverse of the real boundary
phase optimization. It is a classical whole-function statement,
not a quantum-source selection or volume-conjecture theorem.

## 1. Assumptions and the retained marks

Let T be a one-cusped ideal triangulation with t tetrahedra and a
specified positive complete geometric shape point z^0, meaning
Im z_j^0>0. Use the open algebraic shape space with
`z_j(1-z_j)!=0` and the monomial edge/peripheral equations over Q,
including their original sign characters. No branching of all
tetrahedra at once is required for this local calculation.

We use the independently established marked gluing linear data:

* t-1 independent real integral edge rows span an isotropic space E;
* its symplectic reduction E^perp/E is the marked peripheral plane;
* a primitive meridian row adjoined to the edges has rank t and is
  isotropic;
* the peripheral convention is
  `Omega_red=-(1/2)du wedge dv`.

These are the explicit rank and marking inputs, not consequences
of concavity alone. They are proved for the actual knot gluing
complex in the preceding integral peripheral notes. The proof
below also works for any triangulation supplied with this data.

Let the original SL2 eigenvalues be calM,calL, with complete
characters calM_c,calL_c in {+1,-1}. Keep those characters on
their prescribed finite cover and set the centered logs

    u=2Log(calM/calM_c), v=2Log(calL/calL_c),
    m=exp(u), ell=exp(v).                         (1)

Thus u=v=0 at the complete place. Their signs are external
marked characters, not reset by squaring or centering. They
must be reinserted when an SL2 A-polynomial or a quantum
peripheral operator is used.

## 2. The constrained variational equation fixes moduli only after phases

For each tetrahedron take compatible logs

    x_j=Log z_j, y_j=Log z_j'', z_j''=1-z_j^(-1),
    alpha_j=Im x_j, gamma_j=Im y_j,
    beta_j=pi-alpha_j-gamma_j.

All three angles are positive. The angle domain has the usual
linear tetrahedral and edge equations. Its volume is

    V(theta)=sum_j[Lambda(alpha_j)+Lambda(beta_j)+Lambda(gamma_j)],
    Lambda'(theta)=-Log(2sin theta).

On each tetrahedral angle simplex the negative Hessian in
alpha,gamma is

    [[cot alpha+cot beta,cot beta],
     [cot beta,cot gamma+cot beta]].              (2)

Its determinant is one and its first diagonal entry is
`sin gamma/(sin alpha sin beta)>0`. Hence V is strictly concave
on every affine angle slice.

Write Omega=sum_j dx_j wedge dy_j. The sine rule gives exactly

    dV(delta theta)=Omega(Re(x,y),delta theta).  (3)

For example Re x=Log(sin beta/sin gamma) and
Re y=Log(sin alpha/sin beta), which verifies (3) by direct
differentiation. Edge-angle tangents form E^perp. Fix the TWO
real peripheral angles

    a=Im u, b=Im v.

Their common tangent space is E, since their two rows give a
basis of E^perp/E. Therefore an interior stationary point on
this affine fixed-(a,b) slice satisfies

    Re(x,y) in E^perp.                           (4)

Equation (4) is exactly the missing real part of the edge
gluing equations. Their imaginary parts were imposed by the
angle equations. Thus the stationary point solves full complex
edge gluing. Its real peripheral logs are outputs of the
optimization, not separately fixed constraints.

This distinction is essential. Fixing arbitrary independent
complex values m and ell overdetermines the one-dimensional
geometric edge curve. Conversely imposing nonlinear full
holonomy constraints in angle variables is not an affine
constraint to which strict concavity can simply be applied.
The correct independent real optimization parameters are a,b;
the multiplicative algebraic parameters constructed below are
their squared phases.

Any positive stationary point is the unique global maximizer
on that affine slice, and on its closure. For any other point
the segment from the positive stationary point is interior
until its possible final endpoint. Its second derivative is
strictly negative by (2) and its initial derivative is zero,
so its volume is strictly smaller, including by continuity
at a degenerate final endpoint.

## 3. Positive gluing gives the required complex transversality

Here is the short rank calculation, recorded to make all
algebraic inverses explicit. At a positive shape

    dy_j/dx_j=tau_j=1/(z_j-1), Im tau_j<0.

Let (A B) be the rank-t isotropic matrix of edges and the marked
meridian. The fixed-meridian logarithmic shape Jacobian is

    J=A+B diag(tau_j).                           (5)

If Ja=0, the shape tangent `(a,diag(tau)a)` lies in the
complexification of a real Lagrangian. Its symplectic pairing
with its conjugate is zero. But directly

    (i/2)Omega((a,tau a),conjugate(a,tau a))
                       =sum_j Im tau_j |a_j|^2<0

unless a=0. Hence det J!=0. The edge curve is smooth at the
positive point and is étale over the complex meridian m.
The conjugate place has the conjugate invertible Jacobian.

Write its peripheral slopes as

    tau_+=dv/du, tau_-=d(v_tilde)/d(u_tilde).

They are algebraic rational functions on the corresponding
shape curve: solve (5) for a unit meridian variation and apply
the longitude row. On the positive real pair tau_-=bar(tau_+),
and the reduced symplectic identity gives

    Im tau_+=-2sum_j Im tau_j |dx_j/du|^2>0.     (6)

Thus the two peripheral slopes are distinct. This is the
transversality which strict concavity by itself would not supply.

## 4. The doubled normalized curve is étale over the phase torus

Let X_+ be the chosen normalized positive edge-curve place and
X_- its conjugate place. Work on their product, retaining the
shape cover if the peripheral curve alone forgets shapes. Define

    P_mu=m_+/m_-, P_lambda=ell_+/ell_-,
    A=m_+m_-, B=ell_+ell_-.                     (7)

The map to the two-dimensional phase torus is algebraic over Q.
Its logarithmic Jacobian in the local coordinates u,u_tilde is

    [[1,-1],[tau_+,-tau_-]],
    determinant=tau_+-tau_-.                    (8)

It is invertible at the chosen complete pair by (6). Equivalently
one may use both sets of edge equations and the two ratio
equations (7); their full shape Jacobian is the product of the
two fixed-meridian Jacobians and (8), up to explicit nonzero
monomial coordinate factors.

It follows that the selected doubled shape germ is étale over
`(P_mu,P_lambda)=(1,1)`. Its shapes, norms A,B and slopes are
algebraic over Q(P_mu,P_lambda). A component defined only after
a number-field extension causes no loss of algebraicity over
Q: the entire defining gluing/ratio system is over Q, and its
selected unramified component is generically finite over the
phase torus.

For completeness, the algebraicity does not follow merely
from a unique real optimum. For the full polynomial system at
fixed phase values, invertibility of its Jacobian makes every
shape differential over the phase coefficient field zero.
A finitely generated characteristic-zero field of positive
transcendence degree has nonzero differentials (choose a
transcendence basis). Thus the selected shape field extension
is algebraic and finite.

This is a local étale statement with a selected place. It does
not assert that all branches form a finite étale cover over a
Zariski neighborhood of (1,1). Other places can ramify above
the same base value. The selected completed local factor, after
its finite residue-field mark, is the power-series ring in the
two phase parameters and is finite étale over the completed
base. Every specified nilpotent phase lift has a unique shape
lift at that mark. Globally the same function field is finite
over the phase field, but branch and deleted divisors must be
retained in any continuation.

## 5. The algebraic inverse is the entire positive optimizer on its phase fiber

For real phases near the complete point take

    P_mu=exp(2ia), P_lambda=exp(2ib),
    Log P_mu=2ia, Log P_lambda=2ib.              (9)

The product-curve real involution `(z,w)->(bar w,bar z)` covers
`(P_mu,P_lambda)->(1/bar P_mu,1/bar P_lambda)`. It fixes the
chosen conjugate pair. Uniqueness of the local inverse in (8)
therefore forces w=bar z on the real phase torus. Positivity of
z persists in a sufficiently small neighborhood. These shapes
satisfy the full edge gluing and the fixed boundary phases, so
Section 2 makes their angles the unique GLOBAL volume maximizer
of that whole positive affine angle fiber.

Thus the constrained optimum is not merely obtained by a flow
limit: its shapes are the values of the selected whole algebraic
inverse (7). The angles themselves are logarithmic phases of
these shapes and need not be algebraic numbers or functions.

There is also a global real statement on the fixed affine
angle/log-marking. Take all positive solutions of the full edge
equations in that marked angle domain. Each is stationary on
its fixed-(a,b) fiber by (3)--(4). Strict concavity therefore
makes the map to the UNWRAPPED angle pair (a,b) injective.
Equations (5)--(8) make it a local real diffeomorphism at every
such point. Consequently it is a diffeomorphism onto its open
image, with one classical sheet there (absolute degree one).
The image is not asserted to be all feasible phase pairs or
convex. Different log-lift fibers can have the same periodic
(P_mu,P_lambda), so this global assertion is not made over
the unmarked phase torus. It does not assign a degree to the
quantum compact source cycle or its critical projection.

The complex peripheral values are recovered algebraically on
this cover. They lie on the marked A-curve, rather than being
two independent full holonomy parameters. Complete m=ell=1,
or the original calM_c,calL_c=+1 or -1, gives the recorded
algebraic complete shape field.

## 6. The multiplicative Legendre graph and its full Hessian are algebraic

Let V_boundary(a,b) be this maximal volume and put

    Phi(a,b)=-2 V_boundary(a,b).

The reduced form and (3) give

    dV_boundary=(1/2)(Re v da-Re u db),
    u=Phi_b+ia, v=-Phi_a+ib.                    (10)

On the doubled real slice the norm coordinates in (7) therefore
satisfy the whole multiplicative identities

    exp(2Phi_b)=A, exp(-2Phi_a)=B.               (11)

A and B are algebraic functions of P_mu,P_lambda. Hence the
exponentiated Legendre graph is algebraic over the phase torus,
while its first derivatives are marked logarithms of algebraic
functions.

There is an explicit algebraic Hessian. Write Delta=tau_+-tau_-.
Then

    Hess_(a,b) Phi
       =(2i/Delta)[[tau_+tau_-,-(tau_++tau_-)/2],
                    [-(tau_++tau_-)/2,1]],
    det Hess Phi=1.                             (12)

On the real slice, tau_+=p+iq with q>0, this is

    (1/q)[[p^2+q^2,-p],[-p,1]],

which is positive definite. Formula (12) follows by solving
`dLog P_mu=du-du_tilde` and
`dLog P_lambda=tau_+du-tau_-du_tilde`, then applying (10).
Its determinant is one directly, without a period estimate.
All derivatives of Phi of order at least two are algebraic
on this cover: the phase derivatives are the algebraic vector
fields `2iP_mu partial_(P_mu)` and
`2iP_lambda partial_(P_lambda)`, extended uniquely to the finite
characteristic-zero function field.

The same statement holds for the full constrained angle
fluctuation matrix. For example

    cot(alpha_j)=i(z_j+w_j)/(z_j-w_j),

and similarly for the other two shape orders. Thus (2), its
restriction to any fixed rational basis of the affine constraint
kernel, its inverse covariance and its determinant are rational
functions of the doubled shapes. Their determinants are units
on the positive chart. Its positive real Gaussian square root
is therefore an algebraic marked half-density on a finite cover.
This variational Hessian is not thereby the actual quantum
state's separately normalized Gaussian amplitude.

## 7. The potential is an explicit marked regulator period

On the doubled logarithmic cover retain u,v,u_tilde,v_tilde and
the sums and differences

    Log A=u+u_tilde, Log B=v+v_tilde,
    Log P_mu=u-u_tilde, Log P_lambda=v-v_tilde.

Equation (10) becomes the exact closed logarithmic one-form

    dPhi=[Log A dLog P_lambda-Log B dLog P_mu]/(4i).        (13)

Its derivative is
`[du wedge dv-du_tilde wedge dv_tilde]/(2i)=0`, since each
pair is pulled back from a curve. All differentiated log
coordinates are algebraic logarithmic differentials on the
whole doubled-phase cover.

Let R_+,R_- be the existing marked Heisenberg regulator periods
on the two shape factors, with

    dR_+=-(u dv-v du)/4,
    dR_-=-(u_tilde dv_tilde-v_tilde du_tilde)/4.

An exact primitive is

    Phi=(R_--R_+)/i
            +(u_tilde v-u v_tilde)/(4i)+C.      (14)

Differentiate (14): its cross term is the differential of the
displayed bilinear expression, and the remaining terms give
exactly (13). The bilinear term cannot be omitted away from
completeness.

The constant is fixed by the original fundamental-class marks,
not fitted to a desired volume. With conjugate marks at the
complete place, `R_-=bar R_+`, centered logs are zero, and the
already proved Bloch fundamental-class evaluation is
`Im R_+=Vol`. Both (14) and the definition of Phi then give
`Phi=-2Vol`, so C=0 with these marks. Other sign/log sheets
carry their recorded period characters and the corresponding
constant; they are not identified with this sheet.

Thus the optimizer is a whole algebraic shape/norm function,
and its volume potential is a whole logarithmic regulator
period on that cover. Its algebraic Hessian and every fixed
jet are evaluations of these functions. The statement does
not require treating a formal Taylor expansion as the primary
object.

## 8. A fixed two-step unipotent connection carries the whole potential

The logarithmic primitive has a fixed algebraic period object before
any quantum jet or level is chosen. Write

    A_log=Log A, B_log=Log B,
    P_log=Log P_mu, Q_log=Log P_lambda, Z=4i Phi.

Form the five-dimensional Heisenberg period matrix

    Pi=[[1,A_log,-B_log,Z],
        [0,1,0,Q_log],
        [0,0,1,P_log],
        [0,0,0,1]].

Its equation is exactly

    Pi^(-1)dPi=Omega,
    Omega=[[0,dlog A,-dlog B,0],
           [0,0,0,dlog P_lambda],
           [0,0,0,dlog P_mu],
           [0,0,0,0]].                         (14a)

The top-right entry vanishes precisely by (13). Every nonzero
entry of Omega is an algebraic logarithmic differential on the
fixed doubled curve. Its only possible curvature entry is

    dlog A wedge dlog P_lambda-dlog B wedge dlog P_mu
            =2(du wedge dv-du_tilde wedge dv_tilde)=0.

Thus (14a) is a flat algebraic connection on that whole cover.
The group law has a four-dimensional additive quotient and a
one-dimensional center; commutators are central and third nested
commutators vanish. In the displayed representation every product
of three connection matrices is already zero. Along a marked
path, transport is therefore EXACTLY the sum of the identity,
single integrals of Omega, and double ordered integrals of Omega.
No asymptotic expansion or infinite transport iteration is needed.

The marked value of Z at the complete point is -8i Vol, by (14).
It is the central fundamental-class period; zero initial logarithms
alone would leave this central constant free. The connection is
algebraic, while its horizontal period matrix generally is not.
In particular exponentiating the central period is a specified
analytic period evaluation, not an algebraic character from the
additive center to the multiplicative group.

This realizes the proposed whole geometric torsor explicitly.
It does not make an arbitrary quantum A-module unipotent or
construct the selected quantum-source map into this torsor.

## 9. Direct A-polynomial formulation and the essential normalization

Let calA(m,ell) be a polynomial equation for the marked squared
peripheral curve. If the chosen A-polynomial uses SL2 variables,
retain the finite sign cover (1) instead. Equation (10) implies

    calA(exp(Phi_b+ia),exp(-Phi_a+ib))=0,
    calA(exp(Phi_b-ia),exp(-Phi_a-ib))=0.         (15)

On the whole algebraic phase cover, a necessary elimination
presentation is

    calA(m,ell)=0,
    calA(m/P_mu,ell/P_lambda)=0,
    A=m^2/P_mu, B=ell^2/P_lambda.               (16)

The selected normalized places are essential. At
P_mu=P_lambda=1 the raw first two equations in (16) coincide
and contain the entire diagonal peripheral curve. They are
not an étale zero-dimensional fiber by themselves. The
opposite geometric and conjugate places on the normalization
are distinct even where their plane images collide. Their
product has the nonzero determinant (8). If needed, retain
the finite shape cover of that normalization as well.

Thus an A-polynomial formulation can encode the optimizer
without a knot-by-knot calculation, but it must keep the
chosen normalized A-place/torsor and its fundamental period.
An unmarked plane equation and positivity at one point do
not discard the diagonal or other peripheral components.

## 10. Coverage and the quantum boundary

Classical angle-volume optimization and volume potentials on
peripheral curves are established subjects. The coverage already
recorded in the repo includes Rivin and
[Futer--Gueritaud](https://arxiv.org/abs/1004.0440), and the
coverage-only search includes Guilloux--Marche,
[Volume function and Mahler measure of exact polynomials](https://arxiv.org/abs/1804.01395),
and Johansson--Samuelsson Kalm,
[arxiv:1412.1585](https://arxiv.org/abs/1412.1585).
No proof from those papers is used here. The refinement proved
in this note is the explicit phase-doubled algebraic inverse,
its normalization requirements, and the marked primitive (14).
No new Ronkin, Harnack or dimer identification is asserted.

The theorem assumes a positive geometric ideal triangulation
and the stated integral gluing/peripheral rank data. It does
not infer right-angled geometric Menasco cells from alternatingness.
Those combinatorial diagrams need their own geometric hypotheses.
The classical proof makes no knot-family restriction once its
explicit geometric input is supplied.

The whole quantum A-state and its selected cycle are additional
objects. The doubled-phase cover may supply a fixed algebraic
coefficient space for a proposed comparison, but it does not
construct that comparison, prove a bounded quantum comparison
space, or establish a nonzero selected geometric contribution.
Its regulator period is not made algebraic by algebraicity of
the optimizer. No volume conjecture follows without that
remaining source/period theorem.

## 11. Focused exact audit

[audit_doubled_phase_rivin_optimizer.py](../experiments/audit_doubled_phase_rivin_optimizer.py)
and its
[results](../experiments/doubled_phase_rivin_optimizer_results.json)
verify the phase Jacobian, algebraic Hessian and determinant one,
the real positive Hessian, rational tetrahedral covariance,
the marked regulator primitive and its closedness, and the
exact H5 Maurer--Cartan matrix. All triple connection-matrix
products vanish, and its sole curvature coefficient is exactly
the stated difference of the two curve symplectic forms.

An exact algebraic node chart also checks the whole phase inverse,
norm-gradient/Hessian identities and the unnormalized A-equation's
diagonal fiber. It is a convention stress test, not an additional
knot case or a replacement for the general proof.

The independent
[doubled-phase and source audit](doubled_phase_and_critical_source_independent_audit.md)
checks the real branch, global fixed-affine-fiber maximizer,
unwrapped positive projection, sign characters, period constants,
normalization requirements and the H5 transport. All focused
symbolic checks passed. No quantum normal-family or selected
source conclusion is inferred from them.
