# Exact peripheral phase, state recovery, and move covariance

Research note, 25 October 2026. Definitions are the charged operators in
Andersen–Kashaev [arXiv:1109.6295v2](https://arxiv.org/pdf/1109.6295v2),
equation (18), its real level in equation (4), and the state integral (4.5)
of Ben Aribi–Wong [arXiv:2410.10776v2](https://arxiv.org/pdf/2410.10776v2).
This note reconstructs the *complex* identities, including the phases that
their magnitude formulas do not specify. It does not infer a state equality
from equality of absolute values.

The positive local kernel and its proper contractions are independently
proved in `faddeev_pentagon_audit.md`. The complete geometric saddle and
annihilator statements remain those of the previous notes. The new results
here are an exact tensor-to-fiber formula, uniqueness of the fiber state
from that normalized tensor function, and an affine phase criterion for
transporting it under the audited positive moves.

## 1. Data and conventions

Write b>0 for the quantum parameter, Q=b+b^(-1), h=Q^(-2), c_b=iQ/2.
The letter Q here is not the peripheral multiplication operator; that
operator will be denoted mathsf-Q in Section 6.

For tetrahedron j let its physical angles a_j,b_j,c_j be in radians and
sum to pi. Its sign is epsilon_j. Put

    d=pi 1-a, C=diag(epsilon)c,
    delta_j=(epsilon_j+1)/2, N_+=sum_j delta_j,
    H=Q_f-diag(delta)/2, G=-2H.

The face matrix script-A is invertible and gives the kinematical Gaussian
Q_f. For the chosen longitude use the certified matrices A,B with

    B^(-1)A=G, p=2B^(-1)e_N, c_0=B^(-1)nu-G pi 1.

On the balanced angle space its exact linear identity is

    W:=2Q_f d-C=c_0+(lambda/2)p,                          (1.1)

where lambda is the angular holonomy of the chosen longitude. This follows
from the actual edge/longitude angle equations, with their branch constants.
It is also checked on the entire affine angle spaces in the accompanying
script, rather than only at one complete structure.

Fix the rational lift gamma in

    x=p^T y-i pi gamma, mu=p^T d-pi gamma.                 (1.2)

The fiber contour then has Im x=mu. When mu is called a meridian holonomy,
the corresponding normal-curve/peripheral certificate is required. For the
twist families it is supplied by `twist_topology_and_peripherals.md`; gamma=0,
mu=a_U-a_V, reversing the source's meridian orientation in the even case.
For other data (1.2) alone defines a spectral coordinate, not a topological
identification of a meridian.

Choose p_1!=0 by relabeling. Let J_print be the literal printed integral,
including its factor p_1/det(script-A), and put

    J_or=J_print/p_1^2,
    sigma_X=sign(det(script-A) p_1).                       (1.3)

Thus J_or uses the oriented coarea fiber form. The sign sigma_X converts
it to the positive Lebesgue disintegration of the full integral. It cannot
be inferred from a formula for its modulus.

## 2. Charged kernel versus the phase-free dynamical convention

For a positive tetrahedron, set its AK charges to a/(2pi),c/(2pi). The
Fourier identity proved in the pentagon note gives its charged kernel as
the phase-free dynamical factor times

    u(a,c;b)=exp[-pi i/12+i k(a,c)/h],
    k(a,c)=a c/(4pi)+(a-c)/12-pi/24.                      (2.1)

Indeed its Fourier factor is exp(-pi i/12)psi_(c/(2pi),b_angle/(2pi)).
Insert the defining psi and use a+b_angle+c=pi. The remaining x-dependent
factor is exactly

    exp(Q c s)/Phi_b(s-iQ(pi-a)/(2pi)).

For a negative tetrahedron take the adjoint and change spectral variable
t=epsilon s. Its phase is u^(-1), and its remaining dynamical factor is
exactly the negative factor in the FAMED definition. No sign Jacobian
appears for Lebesgue integration on the real line.

Let Z_AK be the contraction of the specified charged kernels and Z_D the
FAMED convention with its phase-free dynamical factors. Then exactly

    Z_AK=U_X Z_D,
    U_X=exp[-pi i sum(epsilon)/12
                       +i sum_j epsilon_j k(a_j,c_j)/h]. (2.2)

This uses the existing charged-operator definition. In the original v2
Theorem 4, formula (5) contains an alpha_3 even though the immediately
following indexing only defines alpha_0,alpha_1,alpha_2. We avoid resolving
that printed indexing by guesswork: equation (18) and its Fourier kernel
fix (2.1) unambiguously. Its scalar agrees algebraically with the displayed
varphi_T when alpha_0=a/pi, alpha_2=c/pi. No claim about the final journal
version is made from this version-specific observation.

## 3. The exact tensor-to-fiber identity

The phase-free contraction has the absolutely convergent spectral form

    Z_D=1/|det(script-A)| integral_R^N
          exp(2pi i t^T Q_f t)
          product_j exp(Q epsilon_j c_j t_j)
          Phi_b(epsilon_j(t_j-iQd_j/(2pi)))^(-epsilon_j) dt.

Set u=-t+iQd/(2pi), y=2pi u/Q, with left-to-right Lebesgue contour
orientations. The inversion identity Phi(z)Phi(-z)=zeta exp(pi i z^2),
where zeta=exp[pi i(Q^2-2)/12], gives

    Z_D=zeta^(-N_+) exp[i Theta_X/(2pi h)]
          (Q/(2pi))^N/|det(script-A)|
          integral_(Y_alpha) exp[(i y^T H y+W^T y)/(2pi h)]
                                      product_j Phi_b(Q y_j/(2pi)) dy,
    Theta_X=C^T d-d^T Q_f d.                              (3.1)

This is an affine substitution, not a deformation across a pole. In
particular the constant terms have h, not sqrt(h), in their denominator.
It follows by expanding 2pi i(-u+iQd/(2pi))^T Q_f(-u+iQd/(2pi))
and Q C^T(-u+iQd/(2pi)). The mixed-sign generic expansion is checked
symbolically in the script.

Disintegrate y into x and its fiber, using (1.1)–(1.3). The imaginary lift
in (1.2) contributes exp(i gamma lambda/(4h)). Combining (2.2), (3.1),
and the coarea Jacobian gives the exact result

    Z_AK(X,alpha;b)
      =sigma_X exp[pi i N/12+i K_X(alpha)/h]
          integral_(R+i mu) J_or(h,x)
                              exp(lambda x/(4pi h)) dx,   (3.2)

where

    K_X(alpha)=sum_j epsilon_j k(a_j,c_j)-pi N_+/12
                    +Theta_X/(2pi)+gamma lambda/4.        (3.3)

The b-independent constant pi N/12 results from combining the inversion
constant and the charged normalization; it is not an unspecified projective
scalar. All entries of K_X are explicit real angle polynomials. For real
angles,b, the multiplier in (3.2) has modulus one, but it matters in state
recovery and quantum-operator comparison.

The level in the *existing* AK definition acts by

    F_b(X,ell)=exp(pi i ell/(4h))Z_AK(X).

Consequently the explicit b-independent allowed choice ell=-4K_X(alpha)/pi gives

    sigma_X exp(-pi i N/12)F_b(X,-4K_X(alpha)/pi)
        =integral J_or(h,x)exp(lambda x/(4pi h))dx.         (3.4)

This identifies the fixed fiber integral with a particular realization of
the published leveled tensor state. It is a choice of level, not yet a
claim that this level choice is preserved by every triangulation change.

## 4. Existence, contour independence, and uniqueness of the fiber state

These points can be proved directly for positive proper FAMED data.
The dynamical factors in Section 3 decrease exponentially at both real
ends. Thus the original spectral integrand is bounded in modulus by
C exp(-c sum_j |t_j|), with c>0. On compact subsets of the positive angle
space the bound is uniform. Under the substitution in Section 3 this
is a corresponding bound for the weighted full y integrand.

Its Phi poles have imaginary coordinate at least pi in the y variable:
the first pole is 2pi c_b/Q=i pi. Hence the product numerator is holomorphic
throughout the box 0<Im y_j<pi. On a fiber the extra longitude factor is
constant in the internal variables. The preceding exponential bound
therefore proves absolute convergence of J_or and local holomorphy in x.
The real map (y_1,...,y_N)->(x,y_2,...,y_N) is invertible, so the same bound
also gives exponential decrease of J_or(x)exp(lambda x/(4pi h)) on the
horizontal x contour.

Positive angle structures form a convex open subset of an affine space.
Two choices with the same mu can be joined inside it. Their fiber
contours have the same x and remain in the pole-free box. Along a compact
part of this segment the tail estimate stays uniform, including when
lambda varies: its factor is constant along each fiber. Cauchy's theorem
with vanishing side faces therefore identifies the fiber integrals.

The image of the positive angle space in (mu,lambda) has an open interior.
One way to certify this is to parameterize its affine equations by a and
lambda: B invertible determines the z'' angles uniquely from
A a+B angle(z'')=nu+lambda e_N, and the other angles follow by their
tetrahedron sums. All remaining edge equations must be included or their
redundancy certified. With p!=0, mu=p^T(pi 1-a)-pi gamma and lambda have
independent differentials. The twist script checks rank two directly.

Thus J_or is holomorphic on the horizontal band of meridian values supplied
by positive angles. For fixed mu and an interval I of compatible longitude
values, its transform

    L_X(lambda)=integral_(R+i mu) J_or(h,x)
                                      exp(lambda x/(4pi h))dx

is holomorphic on the vertical strip Re lambda in I. Uniform exponential
bounds on smaller strips justify differentiation. Varying the horizontal
contour inside the compatible positive chamber does not change L_X.

**Uniqueness.** Values of L_X on any real open subinterval of I determine
J_or on its band. For two proposed states with the stated weighted decay,
the identity theorem first gives equality on the vertical strip. On
lambda=lambda_0+i tau the transform, after the explicit constant from
Im x=mu is removed, is the ordinary Fourier transform of
J_or(s+i mu)exp(lambda_0 s/(4pi h)). This is in L1. Fourier injectivity gives
equality on that horizontal line, then holomorphy gives equality on the
common band. In contrast, equality of the magnitudes of L_X supplies none
of this uniqueness.

## 5. The balanced phase is affine up to one universal term

Eliminating C from (3.3) by (1.1), and using a_j+b_j+c_j=pi, gives

    K_X(alpha)=L_X^angle(alpha)-lambda mu/(8pi)
                                            +gamma lambda/8,
    L_X^angle(alpha)=-pi N/24
        +sum_j epsilon_j(c_j-b_j)/12-c_0^T(pi 1-a)/(4pi).  (5.1)

The superscript distinguishes the affine angle expression from the
Fourier–Laplace transform L_X above. Equation (5.1) is an exact identity on
the balanced angle space. Its only quadratic dependence is the universal
meridian–longitude term. It is especially useful when comparing moves
that preserve the same peripheral coordinates.

For both twist families the script verifies (1.1) and (5.1) on their entire
affine angle spaces for p=0,...,8. It checks the tangent Hessian, gradient
and constant, so agreement at a single special angle is not the evidence.
The proof of (5.1) is the displayed elimination for arbitrary N. The raw
phase K_X varies even at fixed mu,lambda in every tested twist example;
discarding it on account of its unit modulus would lose actual information.

## 6. Exact covariance under a certified positive move

Suppose X,Y are proper positive FAMED realizations related by the audited
operator-pentagon pattern or its adjoint, with compatible peripheral curves,
coordinates and overlapping positive contour chambers. Write its tensor law
as

    Z_AK(X,alpha)=exp(i rho(alpha)/h)Z_AK(Y,alpha'),

where rho=-pi P/12 for the original pentagon and +pi P/12 for its adjoint.
The map of angles is affine. The two scalar transforms obey exactly

    L_X(lambda)=eta exp(i D(alpha)/h)L_Y(lambda),
    eta=(sigma_Y/sigma_X)exp[pi i(N_Y-N_X)/12],
    D=K_Y(alpha')-K_X(alpha)+rho(alpha).                   (6.1)

Because mu and lambda agree, the quadratic terms in (5.1) cancel. D is
affine in the remaining angle variables. The transforms depend only on
lambda. Where they are nonzero, varying angles at fixed lambda in (6.1)
forces the continuous real function D to be constant on each such fiber.
Hence, on the connected positive move chamber,

    D=d_0+d_1 lambda.                                    (6.2)

This is an affine linear-algebra statement, not an assumption that a
quantum normalization vanishes. Nonzero transforms are guaranteed near
the semiclassical regime when the previous positive geometric state theorem
applies: the state is nonzero, so its transform cannot be identically zero
by Section 4. Holomorphic continuation removes isolated transform zeros.
For rational face/peripheral data, d_0 is in pi Q and d_1 is rational.
Two generic angle evaluations, or coefficient comparison, determine them.

If d_1=0, uniqueness immediately gives the exact state identity

    J_or,X(h,x)=eta exp(i d_0/h)J_or,Y(h,x).                (6.3)

Thus this finite phase certificate proves equality of the annihilator and
of the volume rate for the *same selected state*, with every scalar retained.
For the printed normalizations one must also multiply by p_(1,X)^2/p_(1,Y)^2.

If d_1 is nonzero, (6.1) remains the exact transform relation; it must not
be replaced by (6.3). Put a=4pi i d_1. When the relevant fiber band contains
the required contour translation, inverse transformation gives

    J_or,X(h,x)=eta exp(i d_0/h)J_or,Y(h,x-a).              (6.4)

Without that strip/continuation check, (6.4) is not asserted. If it holds,
an annihilator in the natural b-shift algebra transports by a coefficient substitution.
Since mathsf-Q=exp[-(1+b^2)x],

    A_X(mathsf-Q,E)=A_Y(exp[(1+b^2)a]mathsf-Q,E),
    exp[(1+b^2)a]=exp(4pi i d_1)q^(2d_1), q=exp(2pi i b^2).

The formula is in the finite root extension when required; descent to the
prescribed coefficient field uses restriction of scalars as in the earlier
annihilator note, and need not preserve the minimal order over that field.
This retains the finite power of q and the root of unity in the meridian
lift. The complete value cannot be substituted before this comparison.

### 6.1 Geometric endpoints force the affine slope to vanish

There is a stronger conclusion when both endpoints have the positive
complete geometric certificates of the volume theorem, with the boundary
origins fixed by p^T y*=i pi gamma. Under the hypotheses of Section 6,

    d_1=0.                                               (6.5)

Here is a proof that does not assume state invariance. The normalized
transform L_X is the full N-variable integral from (3.1), with its
angle phase removed. At lambda=0 its leading potential is F_0, whose
*full* gradient vanishes at the positive complete y*. This follows directly
from the certified edge/longitude matrix identity and the complete
logarithmic equations, just as in the earlier fiber saddle calculation.

The same exact quantum remainder applies. With s=b^2, its b-dependent
potential at a nearby longitude parameter is

    F_s(y,lambda)=i y^T H y+c_0^T y
        +(lambda/2)(p^T y-i pi gamma)
        -i/(1+s)^2 sum_j Li_2(-exp((1+s)y_j)).

On the full real horizontal plane the real Hessian is
-diag(Im sigmoid((1+s)y_j)), strictly negative for the positive strip.
The full Hessian is invertible, so its critical point y_s tends to y*.
Concavity gives the same quadratic-near/linear-far coercivity bound as
in the fiber proof, now in N real directions. The exact remainder is
uniformly bounded and tends to zero on a smaller strip. The nonzero
Gaussian and the strict tail gap therefore prove L_X(h,0)!=0 for all
sufficiently small b.

Insert the linear moment x(y)=p^T y-i pi gamma. The same saddle argument
applies: the additional polynomial factor is integrable against the
coercive tails, and the ratio of the two Gaussian expansions tends to
x(y*)=0. Differentiation under the convergent integral consequently gives

    lim_(b->0+) h L_X'(0)/L_X(0)
       =lim (1/(4pi)) integral x(y)I_b(y)dy / integral I_b(y)dy
       =0.                                               (6.6)

All constant measure factors cancel in this ratio. The same result holds
for Y. Differentiate the exact relation (6.1)–(6.2):

    h [L_X'(0)/L_X(0)-L_Y'(0)/L_Y(0)]=i d_1.

Taking the limit proves (6.5), since d_1 is independent of b. This proves
that the translation alternative in (6.4) cannot occur for these compatible
geometric endpoints with their complete origins fixed. It was necessary
to retain that alternative before this argument, rather than cancel it
at the ideal point by convention.

The argument also applies to a finite certified path of proper positive
moves. Compose its exact tensor laws first. The endpoint K polynomials
cancel their common quadratic peripheral term, while the sum of local
pentagon phases is affine in the path's angle variables. The transform
uniqueness argument again gives d_0+d_1 lambda. Its identity, initially on
the path's nonempty open longitude interval, extends analytically to zero:
the intersection of the endpoint admissible longitude projections is an
interval containing zero and that initial interval. The contour-independent
local transform charts of Section 4 patch along this interval. Apply (6.6) only at
the endpoints. Intermediate triangulations need their proper positive
kernel contractions and the specified move/peripheral certificates; they
need not have complete geometric saddle certificates for this step.

**Consequence.** Within every such certified positive-path component of
geometric endpoint realizations, the selected coarea states differ only
by the recorded boundary-independent scalar eta exp(i d_0/h). Their
annihilator ideals, primitive minimal operators and volume limits agree
after the fixed peripheral coordinates are identified. The printed states
also retain their explicit p_1^2 ratio. This is a statement for certified
paths, not an assertion that an arbitrary topological Pachner path stays
positive or proper.

## 7. Scope and reproducible checks

Equations (3.2)–(3.4) supply the exact relationship between the specified
literature fiber integral and its leveled charged tensor realization.
Section 4 proves state recovery, and Section 6 reduces covariance for the
audited moves to an explicit affine phase and, if needed, a contour shift.
These improve the previous magnitude-only relationship.
Section 6.1 rules out the nonzero slope for compatible positive complete
geometric endpoints by a full-integral saddle moment. Thus only the scalar
phase remains for any connecting path satisfying the stated certificates.
The subsequent `tetrahedral_symmetry_and_figure_eight.md` applies this
criterion to the actual figure-eight 3–2 move. It audits the ordering
kernels, proves d_1=0 and d_0=11pi/12 on the entire angle space, and
records the simultaneous meridian/longitude reversal. A verified
automorphism then makes the two-tetrahedron state even, giving an exact
scalar equivalence at the same boundary value and the same minimal operator.

**Corollary for the volume theorem.** Under the positive complete geometric
and finite matrix certificates in `literature_state_volume.md`, the selected
inverse-transform state of the leveled tensor realization (3.4) is exactly
J_print/p_1^2. Its primitive minimal annihilator exists in the prescribed
Andersen–Malusà b-shift algebra, its classical symbol contains the certified
geometric peripheral component, and

    lim_(b->0+) -2pi h log|J_or(h,0)|=Vol(M).

This follows from the exact state identity here, the annihilator proof in
`general_annihilator_and_volume.md`, and the independently proved saddle
theorem. The nonzero constant p_1^2 contributes zero to the limit. Thus
the state in that theorem is an exact specified leveled AK realization,
not a solution selected only for its convenient asymptotic. The uniform
twist certificates give this corollary for every fixed parameter in the
two stated twist families and their recorded mirror convention.

What is still needed for a single intrinsic knot state across arbitrary
realizations is a certified connecting sequence, its compatible peripheral
lifts, the constants for the exactly normalized framed state, and any
continuation outside the positive chamber. The slope is already zero for
the certified geometric endpoints of Section 6.1. A path through
the required geometric triangulations is not supplied just by the existence
of a topological Pachner sequence. The all-alternating extension also still
needs its geometric and finite matrix certificates. None of these remaining
claims is inferred from the affine form (6.2).

Run `python3 experiments/audit_peripheral_phase.py`. It checks the generic
mixed-sign Gaussian identity, eighteen complete affine twist angle spaces,
their peripheral rank, and four pointwise quantum identities using the
independently derived real-b defining-integral remainder. The maximum
pointwise relative error was below 9e-15. The symbolic identities and
contour bounds above, rather than those finite samples, carry the proofs.
