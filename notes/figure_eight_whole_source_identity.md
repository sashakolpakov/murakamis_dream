# An exact whole-source identity for the figure-eight knot

Research note, 27 October 2026. This proves at every level, and as a
whole meridian Laurent polynomial, that the actual reduced figure-eight
ADO period is the earlier quantum-A calibration. The proof changes to
a four-strand plat with the actual oriented turns and a literal cut
matrix entry, eliminates its forced transfers, and applies one finite
q-binomial identity. It uses no colored-Jones formula or asymptotic.

The figure-eight is a prototype for source elimination at arbitrary
bridges. This result does not narrow the main target to this knot and
does not prove the original volume conjecture for a broad knot class.

## 1. The identity and the marked four-plat

Let N>=2, q=exp(pi*i/N), Q=q^2, x=-M/q, and Y=M^2=Qx^2. Write

    (z;Q)_k=product_(r=0)^(k-1)(1-zQ^r).

The original reduced knot period satisfies

    F_(4_1),N(Y)
      =sum_(n=0)^(N-1) (-1)^n Q^(-n(n+1)/2)
                            (YQ;Q)_n(Q/Y;Q)_n
      =sum_(n=0)^(N-1) product_(r=1)^n
                               (Y+Y^(-1)-Q^r-Q^(-r)). (1.1)

All factors and coefficients in (1.1) are finite. In particular the
identity includes Y=1 and all of its normal derivatives as whole
germs; it is not an equality modulo Y^N-1 or an unspecified scalar.

Use the four-plat with word

    beta=sigma_2^2 sigma_1^(-1) sigma_2,           (1.2)

where the rightmost crossing acts first. Thus its actual action order
is sigma_2, sigma_1^(-1), sigma_2, sigma_2. Its top cup colors are

    [V(x), V(xvee), V(xvee), V(x)],
    xvee=x^(-1)Q^(-1).                            (1.3)

This plat has rational slope 5/2. Here is an explicit marking check.
The initial adjacent-cap tangle has slope zero. The lifts of the
two adjacent crossing arcs to its torus double cover are primitive
curves intersecting once. Choose the cap lift (0,1) and the
complementary lift (1,0). In that marked basis, sigma_2 acts by
T=[1 1;0 1], while sigma_1^(-1) acts by U=[1 0;1 1]. The latter
fixes the initial cap slope, as it should. Directly,

    T^2 U T (0,1)^t=(5,2)^t.                     (1.4)

These matrices obey the braid relation with sigma_1 represented
by U^(-1). They also give the continued-fraction description
[2,1,1]=[2,2]. Joining the two rational tangles is the usual
two-bridge 5/2 figure-eight diagram. Thus the identification uses
the marked rational-tangle slope and its elementary terminal-1
tangle isotopy, rather than numerical knot recognition.

Assign orientations [+, -, -, +] at the top. The crossing signs
in oriented knot order are +,+,-,-, so the resulting framing
writhe is zero. No additional twist correction is required.

## 2. Exact mixed-color crossings

Use the balanced basis w_a=v_a/(Q;Q)_a on every color. Let a,b be
the input indices and x_1,x_2 their respective highest-weight
parameters. After removing only the common full Cartan scalar,
the positive crossing sends (a,b) to (b+k,a-k) and has coefficient

    r_+(a,b,k;x_1,x_2)
      =(-1)^k x_1^(-b-2k) x_2^(-a+k)
         Q^(ab+(a-b)k-k(k+1)/2)
         {b+k choose k}_Q (Qx_1^2 Q^(-a);Q)_k.   (2.1)

The negative crossing sends (a,b) to (b-k,a+k) and has coefficient

    r_-(a,b,k;x_1,x_2)
      =x_1^b x_2^(a-k) Q^(-ab)
         {a+k choose k}_Q (Qx_2^2 Q^(-b);Q)_k.   (2.2)

The support bounds are the actual unwrapped finite bounds:
0<=k<=min(a,N-1-b) positively and
0<=k<=min(b,N-1-a) negatively.

For a direct derivation, in the unbalanced basis the Cartan
diagonal at indices c,d is x_1^(-d)x_2^(-c)Q^(cd).
The positive nilpotent factor is the literal E_(x_1)^k tensor F^k
with coefficient q^(k(k-1)/2)(q-q^(-1))^k/[k]_q!.
Its E product contributes (-x_1^(-1))^k and the ordinary
Gaussian binomial {a choose k}_Q after cancellation. Evaluate
the diagonal at c=a-k,d=b+k. The factorial basis change multiplies
by (Q;Q)_(b+k)(Q;Q)_(a-k)/[(Q;Q)_a(Q;Q)_b], changing this
binomial to {b+k choose k}_Q and giving (2.1).

For the negative crossing first interchange the colors. The
inverse diagonal contributes x_2^a x_1^b Q^(-ab), and the inverse
nilpotent factor acts by E_(x_2)^k on index b. Its signs and
extra q-powers cancel, leaving x_2^(-k){b choose k}_Q and its
displayed Pochhammer. The same literal basis change gives (2.2).

The full Cartan scalars have not been discarded from the plat.
Put A=alpha and B=2(N-1)-alpha, so q^A=x and q^B=xvee with the
actual unrolled dual lift. The four common scalars multiply to

    q^((B^2-AB+AB+AB)/2)
       =q^((N-1)B)=xvee^(N-1).                 (2.3)

We retain (2.3) in every contraction below. Its cancellation is
part of the source identity.

## 3. A literal cut source, with the correct pivotal side

The turns are those already proved for the actual quantum group:

    coev_L(x)=sum_a N x^(-a)
                        w_(N-1-a) tensor w_a^vee,
    coev_R(x)=sum_a N x^(-a)g_(N-1-a)^(-1)
                        w_a^vee tensor w_(N-1-a),
    ev_L(x)(w_a^vee tensor w_b)
                        =x^a/N delta_(a+b,N-1),
    g_b=x^(1-N)Q^(-b).                          (3.1)

Cut the fourth top leg, which is the primal leg of coev_R, and
take its index-zero matrix entry. In a fully closed drawing the
correct coupon is

    D_0=g E_00.                                 (3.2)

This is a left pivotal trace: coev_R followed by ev_L closes an
endomorphism C as Tr(g^(-1)C). Therefore

    Tr(g^(-1) D_0 C)=Tr(E_00 C)=C_00.            (3.3)

The side matters: substituting g^(-1)E_00 in (3.2) would give a
wrong scalar. This coupon is kept at its specified position; it
is not moved unchanged through crossings.

Equation (3.3) is the actual reduced cut evaluation. At generic
meridian the cut knot endomorphism is scalar, and its index-zero
entry is precisely the original reduced ADO scalar. The equality
extends to exceptional meridians by its Laurent-polynomial germ.
The [original pointing](kashaev_ado_pointing.md) identifies its
value at M=1 with the prescribed Kashaev invariant. No division
by the zero ordinary quantum dimension has occurred.

The source (3.2) fixes the fourth input index to zero and hence
the third to N-1. The first cup leaves inputs

    (a,N-1-a,N-1,0), 0<=a<N.                    (3.4)

Its coefficient, including both cups and the coupon, is
N^2 x^(a-2N+2). At the end both output pairs have colors
V(xvee) tensor V(x) and are closed by ev_L(x).

## 4. Forced transfer elimination and its whole scalar

Write k_1,...,k_4 for the transfers in action order. In (3.4)
the first positive crossing has second index N-1, so k_1=0.
The second crossing is negative and permits

    k_2=k, 0<=k<=N-1-a.

After it the state is (N-1-k,a+k,N-1-a,0). At the third positive
crossing its transfer j obeys j<=a. The final cap on the third
and fourth legs forces the fourth transfer to be j-a. Its
nonnegativity therefore gives

    k_3=a, k_4=0.                               (4.1)

The final state is (N-1-k,k,N-1,0), so the first cap matches
automatically. Thus the exact surviving support is a,k>=0,
a+k<N. This is a support elimination in the actual finite
indices; no stationary-phase or cyclic reduction is involved.

The two caps contribute x^(2N-2-k)/N^2. Together with the cups
and coupon, their entire boundary factor is x^(a-k). Multiplying
the four coefficients (2.1)--(2.2) and the full Cartan scalar
(2.3) now gives the surviving route weight

    W_(a,k)=Y^(k-a) {a+k choose k}_Q
                       (Q/Y;Q)_k (YQ^(-a-k);Q)_a. (4.2)

Here are the monomial cancellations, to make its normalization
reviewable. The four crossing monomials in order are

    xvee^(a-2N+2) Q^(a+1),
    x^(N-1) xvee^(a-k) Q^a,
    (-1)^a x^(1-N-a) xvee^(-k)
                              Q^(a(a-1)/2-k),
    xvee^(-k) x^(1-N) Q^(-k).

The second crossing's remaining factors are
{a+k choose k}_Q (Q/Y;Q)_k, and the third's are
{N-1 choose a}_Q (YQ^(-a-k);Q)_a. Use

    {N-1 choose a}_Q=(-1)^a Q^(-a(a+1)/2),
    xvee=x^(-1)Q^(-1), Y=Qx^2.

The crossing monomials, x^(a-k) boundary factor and
xvee^(N-1) full Cartan scalar simplify to
Y^(k-a)(-1)^a Q^(a(a+1)/2), which the reflected binomial
cancels exactly. This proves (4.2). All N factors, signs,
half-root characters and peripheral monomials have been included.

## 5. One finite binomial identity finishes the comparison

Set n=a+k and sum (4.2) first over k. Its n-th diagonal is

    S_n=sum_(k=0)^n Y^(2k-n){n choose k}_Q
                    (Q/Y;Q)_k(YQ^(-n);Q)_(n-k). (5.1)

Invert the last n-k Pochhammer factors as whole polynomials:

    (YQ^(-n);Q)_(n-k)
      =(-Y)^(n-k) Q^(-(n(n+1)-k(k+1))/2)
                               (Q^(k+1)/Y;Q)_(n-k).

Multiplication by (Q/Y;Q)_k gives (Q/Y;Q)_n. Consequently

    S_n=(-1)^n Q^(-n(n+1)/2)(Q/Y;Q)_n
          *sum_(k=0)^n {n choose k}_Q
                         (-1)^k Q^(k(k-1)/2)(YQ)^k
       =(-1)^n Q^(-n(n+1)/2)(Q/Y;Q)_n(YQ;Q)_n. (5.2)

The last equality is the finite q-binomial theorem, proved
inductively by inserting the final factor of (z;Q)_n. The
Gaussian denominators are nonzero because n<N. This is an
identity of whole Laurent polynomials, including Y=1.

Finally -Q^(-r)(1-YQ^r)(1-Q^r/Y)
=Y+Y^(-1)-Q^r-Q^(-r), so summing (5.2) over 0<=n<N proves
both equalities of (1.1).

## 6. Consequence for the actual quantum-A calibration

The previously proved calibration operator and finite telescoping
certificate in [the normal-period note](peripheral_normal_period.md)
now apply to the actual figure-eight state at every N. In particular
its full inhomogeneous source, including 3-U-U^(-1), U=Y^N, is
an actual identity rather than a calibration supported by finitely
many cut checks. Its homogenized operator and normal source lattice
are likewise actual all-level objects. This statement retains the
whole peripheral functions and says nothing about deleting their
vanishing factors at completeness.

At Y=1 the identity gives the positive period

    <4_1>_N=sum_(n=0)^(N-1)
                       product_(r=1)^n 4 sin^2(pi*r/N). (6.1)

Thus the independently elementary positive-period volume argument
applies to the original invariant in this case. The exact bridge
elimination and finite binomial collapse, rather than a Jones
comparison, are the mechanism here. Extending that source transport
and its regulator norm beyond this prototype remains the main task.

### The selected leading coefficient is the algebraic torsion coefficient

Here is a direct quantitative version, including its normalization.
Put

    f(x)=log(4 sin^2(pi x)), Phi(x)=integral_0^x f(t)dt,
    t_(N,k)=product_(r=1)^k 4 sin^2(pi r/N).

Monotonicity of f on each side of 1/2, treating its integrable
endpoint logarithms separately, gives uniformly for 0<=k<N

    log t_(N,k)=N Phi(k/N)+O(log N).             (6.2)

For example the omitted first-cell integral and the endpoint values
are O(log N), since sin(pi/N) is bounded above and below by fixed
multiples of 1/N. Upper and lower rectangle sums bound the error
on each monotone interval. Hence positivity makes the exponential
rate the maximum of Phi, with at most another log N error from
summing N terms.

The unique global maximum is at x_*=5/6: f changes sign at 1/6
and 5/6, Phi(0)=Phi(1)=0, and

    Phi''(5/6)=-2pi sqrt(3).                    (6.3)

To recover the coefficient, remove the endpoint singularity by
writing log(2sin(pi x))=log(2pi x)+g(x), where
g(x)=log(sin(pi x)/(pi x)) is smooth at zero. Stirling's formula
for k! and Euler--Maclaurin for g give, uniformly for k/N in a
fixed neighborhood of 5/6,

    t_(N,k)=2N sin(pi k/N) exp(N Phi(k/N))
                                      *[1+O(1/N)]. (6.4)

In more detail the logarithm is
N Phi(x)+log(2N sin(pi x))+pi cot(pi x)/(6N)+O(N^(-3)).
Thus no unmarked multiplicative constant is introduced by the
endpoint regularization.

The terms outside this neighborhood are exponentially smaller by
(6.2). On a smooth cutoff within it, the discrete sum equals N
times its Laplace integral with relative error O(1/N). One direct
bound is the composite trapezoid estimate
|N^(-1)sum h(k/N)-integral h|<=C N^(-2)integral|h''|.
For h=chi(x)sin(pi x)exp(N[Phi(x)-Phi(x_*)]), the integral of
|h''| is O(N^(1/2)), whereas integral h is of order N^(-1/2).
The ordinary Gaussian integral, with its odd cubic correction
integrating to zero, also has relative error O(1/N). Therefore

    <4_1>_N=3^(-1/4) N^(3/2) exp(N Phi(5/6))
          *[1+11pi/(36sqrt(3)N)+O(N^(-2))].    (6.5)

To justify the displayed correction, use the fourth-order version
of the same cutoff trapezoid bound. Its error is at most
C N^(-4) integral|h^(4)|; the integral is O(N^(3/2)), giving
relative error O(N^(-2)). Put A=-Phi''(x_*), B=Phi'''(x_*),
C=Phi''''(x_*), a(x)=2sin(pi x), b(x)=pi cot(pi x)/6. The
first relative Laplace correction is

    b_*+a''_*/(2A a_*)+a'_* B/(2A^2 a_*)
                    +C/(8A^2)+5B^2/(24A^3)
       =11pi/(36sqrt(3)).

Here A=2pi sqrt(3), B=-8pi^2, C=-16pi^3sqrt(3), a_*=1,
a'_*= -pi sqrt(3) and a''_*= -pi^2. Taylor expansion with the
Gaussian moments gives an O(N^(-2)) remainder uniformly on
the cutoff, while (6.2) controls its exponentially small complement.

Let Lambda(theta)=-integral_0^theta log|2sin t|dt. Then
Phi(5/6)=2 Lambda(pi/6)/pi. Duplication of sin gives
2 Lambda(pi/6)=3 Lambda(pi/3). The
[exact actual Bloch specialization](figure_eight_bloch_specialization.md)
now evaluates the marked crossing fundamental class directly as
2D(exp(pi*i/3)), using the exact Riley field and normalized
configuration-chain identities. Thus no separate triangulation
recognition is needed for this calibration. Consequently

    Phi(5/6)=Vol(S^3 minus 4_1)/(2pi).           (6.6)

This proves the original volume limit and its leading coefficient
for the actual invariant in this prototype. It is the standard
figure-eight value, now obtained from the independently normalized
bridge source rather than a presumed equivalence of states.

It also tests the intrinsic coefficient computed earlier. With
f_4(t)=t^2-t+1, S_4=-1 and the positive place t=exp(pi*i/3),
the squared density multiplier is 1/[S_4 f'_4(t)]. Its modulus
is 1/sqrt(3), whose square root is exactly 3^(-1/4) in (6.5).
Thus the algebraic principal density and the selected leading
coefficient agree in absolute value here. The positive exact sum
fixes its real positive phase. This does not infer the analogous
selected coefficient for a general knot from the local density
identity alone.

With the lower Riley place t_R=(1-i sqrt(3))/2, put
rho_4=-1/(2t_R-1)=-i/sqrt(3). The selected first correction can
also be written (11/36)rho_4 h_N, h_N=pi*i/N. Thus the first
quantum coefficient is an algebraic number times the specified
quantum parameter, with its embedding retained.

## 7. Verification

The [independent audit](../experiments/audit_figure_eight_whole_source.py)
starts with the original mixed E matrices and Cartan diagonal,
then applies the literal factorial basis change. It checks 2,340
mixed crossing entries against (2.1)--(2.2), 33 full finite path
contractions at levels 2 through 12 and three meridians per level,
18 comparisons to the original three-braid cut, and seven generic-Q
symbolic diagonal identities. It also checks the rational slope,
the oriented writhe and the full unrolled Cartan exponent.

These computations validate the displayed formulas; the proofs
of the all-N statements are Sections 2--5. The computation does
not assume the desired calibration when contracting the plat.

[Results](../experiments/figure_eight_whole_source_results.json).

[Selected-coefficient audit](../experiments/audit_figure_eight_selected_asymptotic.py)
checks the exact Hessian/correction constants and their density
normalization, with numerical diagnostics of the actual positive
period distinguished from the proof above.
[Selected-coefficient results](../experiments/figure_eight_selected_asymptotic_results.json).

Reproduce with:

    python3 experiments/audit_figure_eight_whole_source.py
