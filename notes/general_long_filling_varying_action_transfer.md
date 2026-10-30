# Long filling with the actual finite-level critical action

30 October 2026. Independently reviewed and frozen. The complete
core theorem retains a holomorphic action S_N in its exponential. Its
convergence to S does not justify replacing exp(N S_N) by exp(N S).
The long-filling argument can retain S_N throughout. This removes that
compatibility issue without assuming a new asymptotic expansion of S_N.
The full mixed-source gap remains a separate hypothesis.

## 1. Precise hypotheses and conclusion

Retain the original full-twist identity, endpoint and normal currents,
and normalization chi_N of the
[general filling transfer](general_original_source_long_filling_transfer.md).
Fix the diagram and its b filled ports. Suppose there are nonzero
scalars c_N with

    (1/N) log|c_N| -> F0,

and exact finite holomorphic packets C_N, separately even, on the SAME
fixed complex color neighborhood used in that theorem. Assume

    C_N(x)=c_N exp[N phi_N(x)] [a_N(x)+r_N(x)],       (1)
    phi_N(0)=0,  phi_N -> phi holomorphically,
    sup|r_N|=O(1/N).

Here phi_N and a_N are separately even and holomorphic. On a slightly
smaller fixed neighborhood assume |a_N| is bounded above and below by
positive constants, uniformly in N. Uniform bounds on still smaller
domains give bounds on their fixed derivatives by Cauchy's formula.
Assume

    phi''(0)=2pi i diag(tau_1,...,tau_b), Im tau_i>0. (2)

The full physical-color complement and the error between the original
mixed source and its retained unit phase times C_N obey the same
exponential gap as in the original transfer, now measured relative to
|c_N|. A gap measured relative to exp(N F0) also suffices after reducing
its positive exponent, because log|c_N|=N F0+o(N).

Then there is a diagram-dependent threshold T such that every FIXED
signed integer tuple p with all |p_i|>T has

    K_N(p)=chi_N eta_N kappa^(-sum p_i) c_N
               D_N(p) exp[N S_(p,N)] [1+O_p(1/N)],   (3)

where the actual finite-level critical point xi_N is the small solution
of

    partial_i phi_N(xi_N)+pi i (xi_N,i-1)/p_i=0,
    S_(p,N)=phi_N(xi_N)+(pi i/2)sum_i(xi_N,i-1)^2/p_i. (4)

For each such fixed p, |D_N(p)| is bounded above and bounded away from
zero for all large N. No convergence of a_N or of D_N is required.
The actions S_(p,N) converge to S_p defined by (4) with phi in place of
phi_N. Consequently

    lim_N (2pi/N) log|K_N(p)|=2pi(F0+Re S_p).        (5)

The normalization chi_N is the original known nonzero factor with
log|chi_N|=o(N), and eta_N and the displayed kappa factors are the
retained unit phases. No unknown value of the filled invariant is
used to choose a normalization. The diagram and p are fixed before
N tends to infinity, and neither equal signs nor comparable slopes
are required.

All source scalars use the same convention as the original transfer:
any common recorded exterior framing unit occurs once, either in c_N
or in the displayed outer factors, as in that source's exact identity.

## 2. Uniform local estimates

Holomorphic convergence on a fixed neighborhood implies uniform
convergence of all fixed derivatives on a smaller one. Separate
evenness makes every phi_N Hessian at zero diagonal. By (2), its
negative real quadratic part on real color directions is uniformly
positive for all large N. Taylor's formula therefore gives the same
Gaussian corridor upper bound as in the original transfer, with
constants independent of N:

    |C_N(x+i y)| <= C |c_N|
                 exp[N(-a0 |x|^2+B0 |y|^2)].         (6)

The holomorphic implicit-function construction is uniform as well.
Define the actual finite-level Fourier critical map and action by

    grad phi_N(xi_F,N(z))+2pi i z=0,
    Psi_N(z)=phi_N(xi_F,N(z))+2pi i xi_F,N(z).z.

They exist on one fixed polydisc and converge with fixed derivatives
to their limiting counterparts. Psi_N is separately even, Psi_N(0)=0,
and its quadratic coefficients converge to -i pi/tau_i.

Use the EXACT finite packet C_N in the finite color sum. The contour
argument in the original transfer uses its holomorphy, (6), and the
fixed-width complement gap; these estimates are uniform here. Applying
stationary phase directly to (1), including its holomorphic absolute
remainder, gives

    F_N(z)=c_N N^(b/2) exp[N Psi_N(z)]
                            [B_N(z)+O(1/N)],
    B_N(z)=(2pi)^(b/2) a_N(xi_F,N(z))
                       /sqrt(det[-phi_N''(xi_F,N(z))]). (7)

All errors and fixed derivatives are uniform on a smaller fixed domain.
The Gaussian square root is fixed by the translated original contour.
Neither the grid error nor exp[N(phi_N-phi)] is Fourier transformed as
an independent approximation. The action phi_N remains in (7).

## 3. Charges, noncancellation and the leading coefficient

For each nonzero charge vector m put

    T_(m,N)(z)=Psi_N(z)-2pi i sum_i(p_i z_i^2+m_i z_i).

The proof excluding zero charges is an exact identity of the original
normal-current kernel and any even packet; it is unchanged. The finite
color endpoints and large-charge tails use (6) and its fixed derivatives,
so their exponential estimates are uniform in N too. When estimating
one charge coordinate, spectator chirps stay on their original real
grids or real contours, as in the original transfer. Thus there is no
cost growing exponentially with another fixed slope.

For the remaining local charges set e_i=1/p_i and t_i=m_i/p_i. Solve
uniformly in N

    z_i=-t_i/2+e_i partial_i Psi_N(z)/(4pi i).

Separate evenness and completing the square give

    T_(m,N)(z_(m,N))=(pi i/2)sum_i t_i^2/e_i
                                      +Bhat_N(t^2,e).

At the limit (t,e)=(0,0),

    partial_(t_i^2) Re Bhat = -pi Im(tau_i)/(4|tau_i|^2)<0.

Uniform derivative convergence preserves a fixed negative upper bound
on one common neighborhood for every sufficiently large N. Integrating
in the squared real t coordinates therefore gives the same strict
action ordering between |m_i|=1 and every other local charge. All finite
nonlocal charges and endpoint connectors obey the same uniform estimates
as the original transfer. Shrink the inverse-slope polydisc once so the
minimal-charge action is closer to zero than the global source gaps.

At the minimal charge, xi_N and the second saddle are related exactly by

    z_(N,i)*=(xi_N,i-1)/(2p_i).

The exponent is exactly S_(p,N) in (4), not its limiting value. Uniform
implicit convergence gives xi_N -> xi and S_(p,N) -> S_p. Write
partial_i phi_N(x)=x_i g_(i,N)(x). The stationarity equation gives

    xi_N,i=e_i pi i/[g_(i,N)(xi_N)+pi i e_i].

The denominators are uniformly nonzero near zero. Hence for fixed
nonzero e_i all xi_N,i are nonzero; moreover |xi_N,i|<1/2 after shrinking
the common polydisc. In particular z_(N,i)* is nonzero and small.

The two Gaussian integrations give the precise coefficient

    D_N(p)=2^b (2pi)^b a_N(xi_N) product_i sinh(2pi i z_(N,i)*)
       /[sqrt(det[-phi_N''(xi_N)])
                    sqrt(det[-T_(1,N)''(z_N*)])].    (8)

Both determinants stay nonzero, with the branches of the original
translated contours. For each fixed p the sinh factors have nonzero
limits, and a_N is uniformly bounded away from zero. Formula (8) is
therefore bounded above and away from zero. The 2^b minimal signed
charges have identical action and coefficient: evenness applies at each
N, while m_i sinh(2pi i z_i) and the actual parity character are unchanged
by simultaneous sign reversal. They add exactly as before. This proves
(3). Taking logarithms of absolute values divided by N proves (5).

## 4. Application to the established complete core

For the [actual core packet](actual_complete_core_complex_packet.md), set

    c_N=F_N(0),
    phi_N(chi)=S_N(chi)-S_N(0),
    a_N(chi)=sqrt(det K_N(0)/det K_N(chi)).

These satisfy (1)--(2) on a fixed smaller neighborhood. In fact the
separate channel reflection makes S_N and det K_N separately even:
flipping chi_i flips the corresponding critical delta_i, and conjugates
the Hessian by that coordinate reflection. Its determinant is unchanged.
The square root is the branch equal to one at zero. Thus a_N converges
to a nonzero unit and its bounds required above hold. The complete-source
theorem gives log|c_N|/N -> Vol(Y_D)/(2pi). The packet cusp parameter in
(2) is pi i/(C_i-pi i epsilon_i), half the primitive geometric cusp
parameter; the original filling kernel already retains that convention.

The [actual marked regulator](actual_complete_core_geometric_deformation.md)
identifies F0+phi with the geometric action, with its recorded boundary
correction and primitive peripheral logs. Under the STILL REQUIRED
whole mixed-source complement and corridor-error gaps, the general
geometric filling completion therefore identifies (5) with the actual
filled hyperbolic volume for every independently long fixed signed p.

This note closes the finite-action compatibility issue only. It neither
proves those mixed-source gaps nor extends the complete-core theorem to
filled knots by itself. No additional finite Taylor expansion of S_N,
nor an exchange of a level limit with the filling transform, is used.

Independent analytical review checked the exact saddle conversion,
both Gaussian powers and the coefficient (8), uniform complex and charge
estimates, finite-level evenness, noncancellation, and the actual core
normalization and cusp factor. No new finite computation is claimed:
this is a uniform extension of the stated conditional transfer proof,
not a numerical test of its missing source hypotheses.
