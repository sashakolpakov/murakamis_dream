# The actual geometric target channel and its finite Casimir polynomial

Follow-up: the [actual primitive-word theorem](actual_matching_circle_rectangle_bound.md)
now proves c<=1 for EVERY circle in the certified complete class, including
half twists. The c>1 algebraic case classified below is therefore formal
and cannot be realized by that complete marked quotient. Equality c=1
remains a genuine parabolic target.

30 October 2026. The literal four-port
bend fixes the recoupled channel; it is not a freely chosen geometric
diagonal. In the certified right-angled geometry its complete trace is
`2-4/c^2`, where `c` is the actual crossing-circle rectangle ratio. In
particular, an entire already constructed class has a target outside
the real physical channel range at EVERY matching edge.

There is nevertheless an exact source polynomial that can be evaluated
at that trace. The fully normalized original Racah scalar is a degree-a
polynomial in the target Casimir, generically before specialization.
Consequently the completed target operator is that polynomial of the
original Casimir. This retains all its normal derivatives. Its scalar
evaluation below trace -2 is positive and has a direct variational limit.

This is not yet an asymptotic for that operator in the surrounding
coherent contraction. In particular a polynomial of degree proportional
to N cannot be replaced by its value at a classical symbol without an
additional argument. No global volume equality follows here.

## 1. The typed bend fixes the geometric target

Use the exact bend of the [marked four-port source](actual_matching_edge_marked_four_port_block.md):

    B(K)_(a,b,c,e)=sum_(u,v) K_(a,b;u,v) pV(u,e)pV(v,c).

Its four external objects occur in the order `(a,b,c,e)`. The target
tensor in that theorem couples the middle ports `(b,c)` and then applies
the ACTUAL pivotal last-to-first turn to the other pair. It is not a
different permutation of these objects.

Here is the corresponding based-holonomy calculation. For an original
physical head write

    Lminus(X,S)=[[1,0],[S(1-X)/X,-1/X]],
    G(X,S)=[[-1/X,(1-X)/(XS)],[-S(1-X)/X,-2+1/X]].

The original cup gives the inverse-head relation
`(X,S) -> (X^-1,-S)`. Its two Lminus matrices multiply to the identity,
and prefix transport makes its two based meridians inverses. Thus the
nested cups in `B(I)` have ordered based meridians

    (A_in, B_in, B_in^-1, A_in^-1).                    (1)

For example, the middle two local Lminus factors cancel; the remaining
prefix at the fourth head is the first Lminus, which gives precisely
the inverse of the first based meridian. This proves the nesting order,
including its basing, directly from the original cups.

The [actual critical character map](actual_augmented_plat_local_critical_character_map.md)
preserves both total F and total K. Therefore it preserves the ENTIRE
matrix `Lminus_2 Lminus_1`, not only the trace of the pair product.
Applying the coupon to the first two heads of (1) consequently leaves
the prefixes and based meridians at the last two heads unchanged.
The bent tensor has the ordered tuple

    (A_out, B_out, B_in^-1, A_in^-1),
    A_in^-1 B_in^-1 B_out A_out=P_in^-1 P_out=I.        (2)

The original target middle Casimir is consequently

    lambda_target=Tr(B_in^-1 B_out).                   (3)

The pivotal turn does not change (3): it is the actual cyclic basepath
change for the OTHER pair, already retained in the finite tensor formula.
It does not replace a meridian by its negative or insert a longitude.

At completeness normalize the incoming pair by simultaneous conjugacy:

    A=-[[1,1],[0,1]], B=-[[1,0],[-4,1]],
    P=BA, H=P+I, H^2=0,
    C=I+bH, B_out=C B C^-1.

Direct matrix multiplication gives

    Tr(B^-1 C B C^-1)=2+16b^2.                        (4)

All these traces use the original trace-minus-two lifts. No common
choice of framing flags changes (3) or (4).

## 2. Classification in the certified complete geometry

The [general matching-graph geometry](general_augmented_plat_matching_geometry.md)
puts the crossing-circle rectangle at `(1,E,-1,-E)`, with
`E=exp(2pi i x)`, `0<x<1/2`, and `c=cot(pi x)>0`. The actual primitive
collar, calibrated to the quantum half-twist sign in the
[channel-Hessian theorem](actual_augmented_plat_channel_hessian.md), is

    tau_epsilon=2ic/(1-epsilon ic),
    b-epsilon/2=1/tau_epsilon, epsilon in {0,+1,-1}.

Hence the apparent shear cancels in the physical pair transport:

    b=-i/(2c), lambda_target=2-4/c^2.                  (5)

This is independent of the retained half-twist sign; its primitive
auxiliary meridian still depends on that sign. The source target
eigenvalue is `zeta^(2g+1)+zeta^(-2g-1)`, whose real scaled limit is
`2cos(2pi xi_target)`. Thus (5) has the classification

    c>1: xi_target=asin(1/c)/pi in (0,1/2), up to partner;
    c=1: lambda_target=-2, the folded parabolic point;
    0<c<1: xi_target=1/2 +/- i arcosh(1/c)/pi.          (6)

The last case is a fixed nonzero imaginary channel displacement. Neither
the ordinary packet, which keeps the channel real and discrete, nor the
shrinking REAL-fold norm theorem is a continuation to it.

There is no general remedy by selecting another matching edge. The
[strict-quarter theorem](actual_conway_strict_leaf_quarter_bound.md),
together with the actual marked Conway geometry, proves `x_leaf>1/4`
for EVERY leaf of EVERY retained robust cylindrical Conway factor.
Those are its measured primitive rectangle parameters, as follows also
from the proved cusp shape `2i cot(pi x_leaf)`. Thus every matching edge
in that broad class has `c<1`. In `C(h^3)`, all three ratios are `c=1/2`,
so all three target traces are -14. This is an obstruction to a proposed
real-target-channel rescue, not to recoupling or to the conjecture.

## 3. The original scalar is a generic polynomial in the target Casimir

Put `d=N-1`, use generic `zeta`, `Q=zeta^2`, and symmetric quantum
integers `[n]=(zeta^n-zeta^-n)/(zeta-zeta^-1)`. Let `S_ag,G_ag,D_a`
be the ACTUAL seven-factorial sum and face factors of the
[positive matching-edge scalar](actual_matching_edge_racah_positive_scalar.md):

    G_ag=(-1)^d S_ag/[N],
    D_a=(-1)^a[N][a]!^2[d-a]!/[d+a+1]!,
    H_ag=D_a G_ag D_g.

Define `lambda_r=zeta^(2r+1)+zeta^(-2r-1)` and

    p_a(z)=sum_(k=0)^a (-1)^k/[k]!^2
       *product_(r=0)^(k-1)
          {[a-r][a+r+1]/([d-r][d+r+2])
                    *(z-lambda_r)/(zeta-zeta^-1)^2}.
                                                               (7)

For every generic label `0<=a,g<=d`, the exact identity is

    H_ag=p_a(lambda_g).                               (8)

In particular this is a degree-a polynomial in the ACTUAL target
Casimir, with `p_0=1` and `p_a(lambda_0)=1`. Its finite basic sum is

    4phi3(Q^-a,Q^(a+1),Q^-g,Q^(g+1);
                         Q,Q^-d,Q^(d+2);Q,Q).        (9)

There are no omitted powers of zeta in (7). Indeed each numerator
pair in (9) contributes
`-(zeta-zeta^-1)^2 zeta^(2r+1)[a-r][a+r+1]`, or its g version.
The four denominator factors and the summand's `Q^k` leave exactly
the sign `(-1)^k` in (7). Also
`[g-r][g+r+1]=(lambda_g-lambda_r)/(zeta-zeta^-1)^2`.

Here is an own finite proof from the source sum. By symmetry assume
`a<=g`. Apply the already proved [finite Sears identity](finite_balanced_sears_operator_proof.md)
to (9), with length a, retained parameter `Q^(g+1)`, and
`d_S=Q^-d,e_S=Q`. Its new numerator and denominator EXPONENTS are

    (-a,g+1,g-d,-d-a-1); (-d,g-a+1,g-d-a),

with prefactor

    F1=(Q^-g,Q^(g-d-a);Q)_a/(Q,Q^(-d-a-1);Q)_a.

Apply the same finite identity again, retaining `Q^(g-d)` and taking
`d_S=Q^(g-a+1), e_S=Q^(g-d-a)`. This gives

    4phi3(Q^-a,Q^-a,Q^(g-d),Q^(d+g+2);
                          Q,Q^(g-a+1),Q^(g-a+1);Q,Q),
    F2=(Q^-a,Q^(g-a+1);Q)_a/
                          (Q^(g-d-a),Q^(d-a+1);Q)_a.

The intermediate denominator `Q^(g-d-a)` first vanishes AFTER length
a, including g=d. Multiplying and reversing the negative products gives

    F1 F2=(-1)^a[N][d-a]![g]!^2/
                          ([d+a+1]![g-a]!^2).         (10)

The right side is precisely the original `z=d+g` Racah summand,
multiplied by `(-1)^d D_a D_g/[N]`. Its successive summand ratio is

    -[d+g+k+2][d-g-k][a-k]^2 /
                              ([g-a+k+1]^2[k+1]^2),

which is also the final series ratio. It terminates at
`min(a,d-g)`, exactly the original range. This proves (8) by finite
products and the own finite transform, including all generic zeros.
Both sides of (9) are symmetric in a,g, which covers a>g.

## 4. Exact completed-operator identity, with every normal retained

Let Omega and Pi_g be the original generic two-head Casimir and its
generic projectors in the [completed target theorem](actual_matching_edge_completed_projector_block.md).
Its scalar is `F_ag=G_ag D_g`. Equation (8) gives the operator identity

    sum_(g=0)^d F_ag Pi_g = D_a^-1 p_a(Omega).          (11)

Indeed the projectors exhaust the actual generic tensor product and
Omega has eigenvalue lambda_g on their images. This is a GENERIC
identity, so it includes the true first normal and every fixed generic
jet. At a colliding pair its root Hermite data are exactly

    F_ag(q)=D_a(q)^-1 p_a(lambda_g(q))=R_N(a,g),
    H_ag^div(q)=D_a(q)^-1 p_a'(lambda_g(q)).            (12)

The prime in (12) is the spectral-variable derivative; generic-q
derivatives are still taken in (11). This distinction is essential.
In particular the old nilpotent term has not been removed: (12)
computes its actual coefficient rather than inferring that coefficient
from equality of the two root scalar values.

The full typed replacement is therefore exactly

    sum_g G_ag h_g T_(2g)=beta_N R B[D_a^-1 p_a(Omega)]. (13)

Here `beta_N`, the physical bend B and the pivotal turn R are the
unchanged maps of the completed target theorem. All original row
weights, half-twist phases and the exposed whole-source normal remain
outside (13) with their original conventions.

For the original range `0<=a<=floor(d/2)`, every denominator in (7)
and D_a is a root unit after its displayed common zero is canceled.
Thus the right side of (11) is holomorphic directly, without forming
individual singular projectors. Equation (11) is not an assertion that
Omega is Hermitian or that p_a(Omega) has polynomial operator norm.

## 5. Positive evaluation at the actual nonphysical geometric trace

At `q=exp(pi i/N)` put `theta=pi/N`,
`x_r=2cos((2r+1)theta)`, `s_k=product_(v=1)^k 2sin(v theta)`.
Converting the generic products in (7) at the root gives

    p_a(z)=sum_(k=0)^a s_k^-4
                 product_(r=0)^(k-1)(x_r-x_a)(x_r-z). (14)

For the original folded row range, `x_r>x_a` whenever r<a. Hence
EVERY term in (14) is positive at every real z<-2. This is a genuine
finite source-polynomial evaluation, not interpolation in a fabricated
complex integer color. At z=x_g it equals the previously proved
positive squared-trinomial Racah sum, but (14) remains defined away
from all those physical nodes.

Fix compact subsets `xi in (0,1/2]`, `c in (0,1)`, and let
`a/N->xi`, with actual geometric trace `z=2-4/c^2`. Write

    A=sin^2(pi xi), kappa=c^-2,
    f_(xi,c)(v)=integral_0^v
       log[(A-sin^2(pi s))(kappa-sin^2(pi s))/sin^4(pi s)] ds.
                                                               (15)

Then the actual finite polynomial satisfies

    N^-1 log p_a(2-4/c^2) -> max_(0<=v<=xi) f_(xi,c)(v).
                                                               (16)

If the parameters on the right are taken at their actual values
`xi=a/N`, the logarithmic error is O(log N), uniformly on the stated
compacts. This includes the folded limit. More explicitly, its k-th
term has EXACT logarithm

    sum_(v=a-k+1)^(a+k) log sin(v theta)
       -4 sum_(v=1)^k log sin(v theta)
       +sum_(r=0)^(k-1) log[kappa-sin^2((r+1/2)theta)].

The first line follows from
`x_r-x_a=4 sin((a-r)theta)sin((a+r+1)theta)`; all powers of two
cancel. The last summand is smooth uniformly because kappa>1.
The elementary endpoint harmonic bound for log sin gives an O(log N)
error for its Riemann sums, even when a+k approaches N-1 or a-k=0.
Finally `sin(pi(xi-s))sin(pi(xi+s))=A-sin^2(pi s)` identifies the
integral with (15). Thus `log term_k=N f(k/N)+O(log N)`, including
either endpoint.
The polynomial has at most N positive terms; the upper bound is their
maximum times N, and a nearest integer to its interior maximum gives
the reverse bound with the same logarithmic loss.

The maximizing point is unique. Set t=sin^2(pi v). The derivative
exponential is `(A-t)(kappa-t)/t^2`, strictly decreasing from infinity
to zero as t runs from 0 to A. Consequently

    sin^2(pi v_*)=A kappa/(A+kappa).                  (17)

At the folded row `xi=1/2`, this becomes

    v_*=atan(1/c)/pi=x,                              (18)

the ACTUAL measured crossing-circle rectangle parameter. Thus the
positive finite polynomial selects the correct local rectangle in
this precise scalar variational sense.

For z in a fixed compact subset of (-infinity,-2), all fixed generic-q
and spectral derivatives of the scalar in (14) cost only a polynomial
relative to p_a(z). This follows from (7), not from differentiating a
root-only formula: each root term is positive; the nonzero quantum
integer factors have total logarithmic derivative
`O(N^2(1+log N))`, and `z-x_r` is uniformly separated from zero.
On a disk of that reciprocal radius every summand remains in a fixed
narrow sector. Cauchy gives the fixed-jet bound. This controls scalar
evaluation at that trace, not the norm of the operator in (11).

## 6. The remaining analytic question is narrower, but still real

Equations (3)--(6) answer which target channel the actual geometry
requires. Equations (7)--(14) provide its exact finite source polynomial
without a complex-color interpolation. The full root Hermite data and
generic normal are retained, and (16)--(18) give a positive scalar
action whose critical parameter is the actual rectangle.

The original contracted operator is nevertheless `p_a(Omega)` with
`a` proportional to N. A sharp analysis must show how that polynomial
acts on the actual surrounding selected boundary state, including
the pivotal reshuffle and shared magnetic variables. Its scalar value
at lambda_target is not already such an operator theorem, nor a
noncancellation estimate for the full marked source. This is the
remaining step exposed here; taking the independent full operator
maximum would again pay the previously computed 10v3 boundary cost.

Audit: [typed target, original polynomial, normal and scalar-rate checks](../experiments/audit_actual_matching_edge_geometric_target_polynomial.py).
It passes exact symbolic nested-cup/prefix/primitive-collar identities,
4,485 generic original seven-factorial comparisons, eleven original
Casimir polynomial matrices (6,453 entries), 529 four-jet comparisons
before specialization and 251 actual divided-normal comparisons with
the spectral derivative. Twelve positive scalar evaluations at 80
digits check the stated variational normalization and selected mode.
These checks supplement the displayed finite and asymptotic proofs;
none tests or asserts a surrounding coherent operator asymptotic.

The strict-quarter obstruction concerns the measured primitive rectangles. No scalar-to-operator asymptotic follows.
