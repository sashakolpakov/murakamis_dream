# Actual quantum-A energy propagation with regulator weights

28 October 2026. A geometric regulator weight cancels the diagonal
growth of a smooth spectral branch, but does not by itself control the
actual source or channel mixing at each time step. This can be checked
EXPLICITLY for the actual affine figure-eight operator, on a regular
arc with distinct eigenvalues and no turning-point or resonance issue.

The calculation identifies a concrete missing estimate in the proposed
rigid-dynamics argument. It does not rule out a better exact Green
representation: the [pointed Newton--Green theorem](pointed_newton_green_barrier.md)
already provides one for this prototype. Nor does it replace the whole
source by a largest-eigenvalue prescription.

## 1. Keep the actual affine operator and source

Use C F_N=D(3-U-U^-1), U=Y^N, with the exact coefficients and
normalizations of the pointed Green note. On a regular part of the
root orbit U=1, its forward inhomogeneous recurrence is

    w_(j+1)=T_Q(Y_j) w_j+f_Q(Y_j),
    w_j=(F_N(Y_j),F_N(Q^-1Y_j))^t,
    T_Q=[-c0/c+, -c-/c+; 1,0],
    f_Q=(D/c+,0)^t, Y_(j+1)=Q Y_j.                  (1)

This is the original affine source, not an arbitrary homogeneous
initial vector. The equation is used away from zeros of c+ only.
Its global root singularities and complete-point normal pointing
remain exactly those in the actual operator/source theorem.

Put Q=exp(h), h=2pi i/N. The limiting homogeneous transfer is

    T0(Y)=[P(Y),-1;1,0],
    P(Y)=Y^2+Y^-2-Y-Y^-1-2.                         (2)

Its roots satisfy lambda+lambda^-1=P. On a regular spectral chart
with lambda!=+/-1 choose

    V(Y)=[lambda,lambda^-1;1,1],
    a(Y)=Y/(Y^2-1), dot P=Y dP/dY.

Differentiating the ACTUAL quantum coefficients, not just the
classical symbol, gives

    T_Q=T0+h T1+O(h^2),
    T1=[-aP,2a;0,0].                               (3)

The source tends to

    f0=((Y+1)^2/Y,0)^t.                             (4)

All these expansions are uniform on compact regular arcs. The roots
and V can be continued there with their original marks.

## 2. The exact first-order channel connection is nonzero

Write Lambda=diag(lambda,lambda^-1). Since

    dot lambda=dot P lambda^2/(lambda^2-1),

the transfer between successive CLASSICAL eigenframes is

    V(QY)^-1 T_Q(Y) V(Y)=Lambda+h B(Y)+O(h^2),
    B=V^-1 T1 V-V^-1 dot V Lambda.                  (5)

Direct rational multiplication gives

    B12=a/lambda+dot P/(lambda^2-1)^2,
    B21=a lambda+dot P lambda^4/(lambda^2-1)^2.      (6)

These include BOTH the subprincipal quantum coefficient and the
moving-frame derivative. Ignoring the latter is not a time-step
energy calculation. At the regular point

    Y=i, P=-4, lambda=-2-sqrt(3),

one obtains EXACTLY

    B12=i(sqrt(3)-1)/6,
    B21=-i(sqrt(3)+1)/6.                            (7)

Both are nonzero. The same point is an actual root-orbit sample for
every N divisible by four. This mixing is therefore actual quantum
transport, not a synthetic matrix counterexample.

## 3. What happens to the proposed step energy

Suppose a genuinely identified peripheral branch has its ABSOLUTELY
marked regulator R_i(theta), Y=exp(i theta). The
[general peripheral bound](general_peripheral_representation_volume_bound.md)
and the actual boundary differential give

    |R_i|<=Vol(X), dR_i/dtheta=log|lambda_i|.         (8)

This identity uses the squared meridian Y and the actual longitude
eigenvalue. It is not asserted for an unidentified factor of an
arbitrary annihilator. Let

    G_N(theta)=diag(exp[-N R_i(theta)/(2pi)]),
    u_j=G_N(theta_j) V(Y_j)^-1 w_j.

Then the EXACT step and source are

    u_(j+1)=A_(N,j) u_j+g_(N,j),
    A_(N,j)=G_N(theta_(j+1)) V(Y_(j+1))^-1
                     T_Q(Y_j)V(Y_j) G_N(theta_j)^-1,
    g_(N,j)=G_N(theta_(j+1)) V(Y_(j+1))^-1 f_Q(Y_j). (9)

The ordinary energy identity is therefore

    ||u_(j+1)||^2=||A_(N,j)u_j||^2
          +2 Re <A_(N,j)u_j,g_(N,j)>+||g_(N,j)||^2. (10)

The source and its cross term have NOT been dropped. Equation (8)
makes the diagonal factors of A have modulus 1+O(1/N). But for i!=k,
(5) gives

    (A_(N,j))_(ik)
      =[h B_ik+O(h^2)]
          exp{N[R_k(theta_j)-R_i(theta_(j+1))]/(2pi)}. (11)

A nonzero O(1/N) connection can thus have EXPONENTIALLY large weighted
norm when the branch regulators differ. It is not absorbed by
|R_i|<=Vol or by a polynomial number of time steps.

For the actual geometric/conjugate figure-eight branches the complete
regulator limits are +Vol and -Vol. They remain separated on a small
regular punctured arc near completeness. The coefficients (6) are
analytic on its connected hyperbolic spectral interval and are not
identically zero by (7); their isolated zeros cannot fill that arc.
Thus there are regular points with a fixed regulator gap and a
nonzero dangerous entry in (11). The natural instantaneous weighted
transfer is not uniformly contractive even in this solved prototype.

The source is also genuinely present in both channels. At Y=i,
f0=(2,0)^t, and V^-1 f0 is a nonzero multiple of (1,-1)^t.
Its weighted norm cannot be declared polynomial solely because the
UNWEIGHTED affine source is bounded. A common constant shift of all
R_i changes source weights and the final evaluation together; it does
not remove the relative exponential factors in (11).

## 4. What a successful dynamical estimate must add

Equations (9)--(11) are a source-exact time-step formulation. To get
a sharp cumulative upper bound from regulator weights one still
needs an actual estimate on mixing and source response, for example
an exact triangular source flag or an exponentially accurate branch
connection with its Stokes and boundary matrices controlled. A fixed
finite-order adiabatic diagonalization only replaces 1/N in (11) by
a power of 1/N; that still does not beat a fixed regulator gap.

Using the exact fundamental solution as the weight would trivially
remove the dynamics, but would already encode the unproved Green
response. It is not an independently derived estimate. Conversely,
this calculation is not a lower bound for the complete invariant:
the actual selected solution can and does exhibit cancellations
between the terms in (10).

Eigenvalue collisions require block transport rather than (5), and
the complete root resonance needs its original source/normal Schur
data. Neither issue explains away (11), which occurs on an entirely
regular arc. The known figure-eight pointed Newton factorization
supplies extra exact source structure and its endpoint evaluation
metric; the actual five-crossing recurrence already needs a different
two-channel treatment. No broad knot class has yet been shown to
have the additional structure needed for a sharp regulator bound.

The subsequent [pointed metric theorem](actual_pointed_metric_transport_and_crossing_obstruction.md)
adds a quantitative limitation: even after retaining the actual input
and output costs, a well-conditioned full-space positive metric may
be forced to pay the larger spectral envelope. Its exact analytic
example requires exponential metric conditioning to recover the true
coherent rate. This is a general cocycle obstruction, not a further
claim about the actual figure-eight operator above.

[Audit](../experiments/audit_actual_regulator_weighted_a_transfer.py):
the actual quantum coefficient expansion, both exact connection
entries, the nonzero radical values, the original affine source,
and finite root-orbit convergence of the mixing formula.
