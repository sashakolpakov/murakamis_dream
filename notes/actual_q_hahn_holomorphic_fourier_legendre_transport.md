# The selected Fourier action has a nonsingular holomorphic Legendre chart

30 October 2026. The actual selected
ordinary q-Hahn action admits a local holomorphic Legendre change at
EVERY point of the full strict physical tube. Restoring the exact
coefficient phase recovers the original magnetic coordinate and action.
This is a theorem about the selected classical action. It does not
continue a finite coefficient index away from its integer lattice or
prove a source integration-cycle statement.

## 1. The actual source fixes the additive phase

Fix a real channel parameter 0<xi<=1/2. Use the selected holomorphic
action Phi_xi(tau,nu) of the
[full physical packet](actual_q_hahn_full_physical_complex_packet.md), on

    P={1/2<Re tau<1, 0<Re nu<Re tau}.

The actual finite channel remains an integer j, with j/N tending to
xi. No complex finite-channel interpretation is made here. Put

    y=2pi i(nu-tau/2), w=exp(y),
    C=cos(pi xi), s=sin(pi xi), c=-cos(pi tau).

The image O of P in (tau,y) coordinates is convex. On a real radial
slice, tau and y are real, and the source polynomial P_(t,j)(w) is
positive when its actual complete support t+j>=d is imposed.

The finite source identity, including its scalar, is

    fhat_j(N nu)=q^[(d-2j)N nu] c_(t,j) P_(t,j)(exp y),
    c_(t,j)=q^[j(t+j-d)]/(Q;Q)_j,
    q=exp(pi i/N), Q=q^2, d=N-1.                    (1)

Use the original product logarithm

    (Q;Q)_j=(-i)^j q^[j(j+1)/2] s_j,
    s_j=product_(r=1)^j 2sin(pi r/N).

At nu=t/(2N)-iy/(2pi), with real y, the exact argument supplied by
the prefactors of (1) is

    pi[d(t-j)+j^2]/(2N),                            (2)

independent of y. This is a marked product logarithm, not a principal
argument chosen anew after reducing (2) modulo 2pi. Dividing its
logarithm by N yields the absolute phase

    C_0(tau,xi)=i pi(tau-xi+xi^2)/2.                (3)

Consequently define on O

    F_xi(tau,y)=J(xi)+(xi-1/2)y
         +Phi_xi(tau,tau/2-iy/(2pi))-C_0(tau,xi).   (4)

On the real complete radial slice this is precisely the REAL
positive-polynomial action in the
[coefficient variational theorem](actual_q_hahn_fourier_coefficient_variational.md).
The constant and linear terms in (4) are fixed by (1), not by an
arbitrary integration constant. Formula (4) also defines its
holomorphic continuation in tau and y. Throughout this note xi is
a fixed real parameter.

## 2. The Legendre derivative has no critical point on O

Write

    B=w^2+2cw+C^2, V=w^2+2cw+1.

The selected square root of B is continued from its positive value
on the real radial slice. The full packet proves B and V nonzero:
they are w^2 times its two nonzero characteristic factors. Since O
is convex, the selected square root is globally defined there.
The selected source multiplier has the exact expression

    Y=exp(Phi_nu)=(s+i sqrt(B))^2/V.                (5)

This retains the continued root. It does not assert that sqrt(B)
is pointwise principal outside the real slice. Differentiating (4),(5)
on that slice and continuing the identity gives

    F_y=xi-1/2+Phi_nu/(2pi i),
    F_yy=s w(w+c)/(pi sqrt(B) V).                  (6)

The only possible new zero in the second line is w+c=0. It is
AUTOMATICALLY excluded by the strict physical domain. Indeed put

    T=exp(2pi i tau), U=exp(2pi i nu).

Then w+c=0 is equivalent to U=(1+T)/2. The principal argument of T
is theta=2pi(Re tau-1), strictly between -pi and 0. The argument
of the positive sum 1+T lies strictly between theta and 0, for
every |T|>0. But an allowed physical U has its argument lift in
(0,2pi Re tau); its principal argument is either in (0,pi] or
in (-pi,theta). It cannot equal that of (1+T)/2.

Because s>0, w!=0, B!=0 and V!=0, equation (6) proves

    F_yy never vanishes on O.                      (7)

This includes the endpoint xi=1/2. The real radial curvature is
positive, but the proof of (7) uses the full complex physical
domain, not positivity of a complex Hessian.

## 3. Local action transport with its exact phase

Let lambda=F_y. By (7), (tau,y)->(tau,lambda) is locally
biholomorphic at EVERY point of O. In each such chart define

    L_xi(tau,lambda)=F_xi(tau,y)-lambda y.           (8)

These are local Legendre charts on the marked action graph. No
global injectivity of the projection to (tau,lambda) is asserted.
They satisfy

    L_lambda=-y, L_lambdalambda=-1/F_yy,
    lambda=xi-1/2+Phi_nu/(2pi i),
    L_tau=Phi_tau+pi i(lambda-xi).                  (9)

On real complete radial parameters and 0<lambda<xi, this L is the
actual coefficient rate already proved. At other complex lambda
it is an analytic ACTION chart, not yet an asymptotic formula for
individual finite Fourier coefficients.

For an arbitrary physical nu in the same local chart, consider

    H(tau,nu;lambda)=L_xi(tau,lambda)
          +2pi i(lambda+1/2-xi)(nu-tau/2).         (10)

Stationarity in lambda gives

    y=2pi i(nu-tau/2).                             (11)

Substitution of (4),(8) then yields the exact critical-value identity

    H_crit=J(xi)+Phi_xi(tau,nu)-C_0(tau,xi).        (12)

The original prefactor contributes -J(xi)+C_0(tau,xi), by (1),
and therefore restores precisely Phi. In particular no discarded
quadratic phase has to be guessed from a Hessian or a volume value.
Differentiation of (12) also preserves the original magnetic
momentum and the tau momentum; the latter includes the explicit
shift in (9).

## 4. Actual affine cycle coordinates and retained characters

At a vertex of the exact shared-cycle compiler, let

    u_v=epsilon_v x_c+B_v,
    b_v=max(0,T_i-d), t_i=min(T_i,2d-T_i),
    delta_v=(B_v-b_v)/N-t_i/(2N), X_c=x_c/N.

The normalized magnetic coordinate is

    nu_v=epsilon_v X_c+(B_v-b_v)/N.

The exact finite coefficient phase contains the linear term
2pi i(lambda_v+1/2-xi_i)(delta_v+epsilon_v X_c),
up to the explicitly retained finite d/N correction. Thus its
classical lambda equation is (11), with

    y_v=2pi i(delta_v+epsilon_v X_c).

It recovers the ORIGINAL coordinate nu_v, with either actual degree
adapter and the original white-map reversal. It does not force the
new y_v to be real. This is the precise action-level distinction from
the [all-radial obstruction](actual_positive_fourier_radial_geometric_obstruction.md).

For a closed physical cycle, the exact coefficient constraint is

    sum_v epsilon_v(lambda_v+1/2-xi_i)
          +(1/2)sum_b epsilon_b
       =n_c+(b_c+E_c/2)/N.                         (13)

The original marked charge b_c, finite pivotal shift E_c/2 and the
integer Fourier winding n_c remain specified. In a leading stationary
action the multiplier includes the term -2pi i n_c X_c. It must
remain in a critical-value calculation. Likewise a factor (-1)^a
has its original product logarithm; replacing it by another logarithm
differing by 2pi i a is invisible on integer colors but changes a
continued action character. The local identity (12) does not authorize
either omission.

## 5. The remaining quantum statement is separate

This theorem gives an everywhere nonsingular LOCAL selected-action
change for ordinary physical factors. It explains how restoring the
exact phase permits nonradial magnetic critical coordinates; it does
not construct their finite coefficient asymptotics, select a contributing
global period, bound a complementary contraction, or prove that complex
critical contributions survive. Completed partner normals and the
exceptional four-port block retain their previous scope.

In particular, the finite positive coefficient theorem still concerns
actual integer indices and real complete parameters with interior
slopes. Holomorphic action transport alone cannot replace the missing
analytic statement about those coefficients or the full source cycle.

Focused audit: [source prefactor and Legendre derivative identities](../experiments/audit_actual_q_hahn_holomorphic_fourier_legendre_transport.py).

Primary-agent full analytical review: PASS. The reader recomputed the
finite product phase and absolute constant, both derivative shifts,
critical-value restoration, exclusion of the caustic on the full tube,
and exact winding and finite charge terms. Both actual degree adapters
and the white-map reversal retain their original scope.

Independent full analytical review and fresh audit: PASS. A second
reader checked the same source-normalized action identities and the
continued square-root convention, and reproduced the five exact audit
identities. Neither review infers complex finite coefficient indices,
global injectivity from the local argument, or a contributing source
cycle.
