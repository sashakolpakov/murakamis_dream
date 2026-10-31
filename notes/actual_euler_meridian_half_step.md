# The actual Euler meridian half-step has a controlled norm and a nonzero endpoint

27 October 2026. The right Euler frame in the original all-strand cap
has an explicit adapter under M -> qM. Its operator and inverse have
at most polynomial norm in the specified flat relative metric. Its
canonical endpoint evaluation is EXACTLY 2/[N(1-q)], and its affine
cyclic transport retains the central factors 1+Z and 1-Z.

This is a sourced local calculation, not a new knot invariant or a
proof of selected geometric survival. It controls the Euler part of
the meridian frame change. It does not bound the fusion change in
the original physical metric or the full word/source contraction.

## 1. The actual adapter and all its coefficients

Use q=exp(pi*i/N), Q=q^2, N>=2, and the right coefficient algebra
of [the all-strand original source](all_strand_euler_cauchy_cap.md).
Put z=xf with z^N=0, x=-M/q, and

    u_N(z)=sum_(k=0)^(N-1) z^k/(Q;Q)_k.

Keep the same abstract coefficient-module frame when changing M.
The actual meridian step M -> qM sends x to qx and hence z to qz.
Define the two inverse, finite polynomial adapters

    B_N(z)=u_N(qz)u_N(z)^-1,
    A_N(z)=B_N(z)^-1=u_N(z)u_N(qz)^-1             (1)

in that nilpotent algebra. The actual word basis uses u_N^-1,
so the direction of the basis change can use A_N rather than B_N;
both bounds below are stated. This is not a substitution into a
classical momentum coordinate.

Their unique degree-<N representatives are

    A_N(z)=sum_(k=0)^(N-1) a_k z^k,
    a_k=(q;Q)_k/(Q;Q)_k,
    B_N(z)=sum_(k=0)^(N-1) b_k z^k,
    b_k=q^k(q^-1;Q)_k/(Q;Q)_k.                  (2)

One can prove (2) without an infinite-product specialization.
The nilpotent Euler equation u_N(Qz)=(1-z)u_N(z) gives

    (1-z)B_N(Qz)=(1-qz)B_N(z) modulo z^N.

Its constant coefficient is one; comparing every higher degree
below N gives exactly the b_k recurrence in (2). Taking the
inverse gives the analogous a_k recurrence. All its denominators
1-Q^k, 0<k<N, are actual nonzero root units.

## 2. The unreduced polynomial Ward equations retain the source

For their CANONICAL degree-<N representatives, before discarding
degree N, the exact polynomial identities are

    (1-z)B_N(Qz)-(1-qz)B_N(z)=-(2/N) z^N,
    (1-qz)A_N(Qz)-(1-z)A_N(z)=+(2/N) z^N.       (3)

All coefficients below degree N cancel by (2). For the first
top coefficient use the FULL root products

    product_(r=0)^(N-1)(1-q^-1 Q^r)=2,
    (Q;Q)_(N-1)=N,
    b_(N-1)=2q^(N-1)/[N(1-q^-3)].

Thus (q-Q^-1)b_(N-1)=2q^N/N=-2/N. The second top coefficient
is (1-q^-1)a_(N-1)=2/N. These prove (3), including composite
levels. The factor two comes from q^N=-1 and has not been
absorbed into a normalization.

Evaluate the FIRST identity at the polynomial argument z=1.
Its shifted term is multiplied by zero, so one obtains

    B_N(1)=2/[N(1-q)]
          =1/N+(i/N)cot(pi/(2N)).                (4)

At z=q^-1 the same identity gives

    B_N(q)=2/[N(1-q^-1)]=conjugate(B_N(1)).      (5)

In particular B_N(1) is nonzero at every level and tends to
2i/pi. Equation (4) is an exact evaluation of the specified
polynomial, not a claim that z=1 defines a character of z^N=0.
The source term in (3) is necessary for that evaluation.

## 3. The affine norm torsor has both central divisors

Keep the same polynomials but now place z in the cyclic algebra
z^N=Z, with Z a central parameter. Away from 1-Z=0 the first
identity in (3) becomes the exact AFFINE difference equation

    sigma(B_N)=L(z)B_N-2Z/[N(1-z)],
    sigma(z)=Qz,  L(z)=(1-qz)/(1-z).             (6)

The cyclic norm of its homogeneous multiplier is exactly

    product_(j=0)^(N-1)L(Q^j z)=(1+Z)/(1-Z).     (7)

It follows directly from product(1-Q^j z)=1-Z and q^N=-1.
This specifies the local homogeneous norm curve and its retained
affine source. At Z=0 the homogeneous cyclic norm is one and
the affine term vanishes; the marked degree-<N section has
B_N(0)=1. At the norm divisor Z=1, (3), rather than two
separately undefined quotients in (6), gives the regular endpoint
value (4). Deleting either 1+Z or the source 2Z/N changes this
comparison.

This is the actual Euler adapter's local norm/source extension.
It is not identified with the knot's geometric A-curve. Replacing
z^N=0 by Z here defines a specified polynomial cyclic extension
of this adapter; it does not assert a full moving-q or full-word
holonomy extension.

## 4. Uniform coefficient and operator bounds

Write t=pi/N. For k>=1, the exact phases and positive magnitudes
in (2) are

    a_k=exp(-ikt/2) alpha_k,
    b_k=-exp(-ikt/2) beta_k,
    alpha_k=product_(r=1)^k sin((r-1/2)t)/sin(rt),
    beta_k=alpha_k sin(t/2)/sin((k-1/2)t).       (8)

There are all-level bounds

    alpha_k <= 2/sqrt(min(k+1,N-k)),
    beta_k <= pi/[min(k,N-k)]^(3/2).            (9)

Here is an elementary proof. For k<=N/2 write

    alpha_k=w_k product_(r=1)^k
                      sinc((r-1/2)t)/sinc(rt),
    w_k=product_(r=1)^k (r-1/2)/r.

The function log(sinc v) decreases on (0,pi/2]. The logarithm
of the displayed product sums its decreases over disjoint half
intervals, so is between zero and log(pi/2). Induction gives

    1/sqrt(4k+1) <= w_k <= 1/sqrt(k+1).

For the other half use the exact reflection identity

    alpha_(N-1-l)=1/[N alpha_l sin((l+1/2)t)],

which follows by splitting the full odd-root product. The
inequality sin v>=2v/pi for v<=pi/2 gives the first bound in
(9). Finally sin(t/2)<=pi/(2N) and

    sin((k-1/2)t)>=2 min(k-1/2,N-k+1/2)/N

give the second bound. These estimates include both tails.
Summation yields, with deliberately generous explicit constants,

    sum_(k=0)^(N-1)|a_k| <= 8 sqrt(N),
    sum_(k=0)^(N-1)|b_k| <= 1+6pi.              (10)

For example sum_(m>=1)m^(-3/2)<=3 suffices for the second.
Consequently for EVERY contraction Z_0 with Z_0^N=0,

    ||B_N(Z_0)|| <= 1+6pi,
    ||B_N(Z_0)^-1||=||A_N(Z_0)|| <= 8 sqrt(N). (11)

The flat right-regular basis f^a e_j makes R_f a truncated
unit-coefficient shift, so ||xR_f||<=1 on |M|=1. Thus (11)
applies to the actual relative right-Euler adapter in that
SPECIFIED metric. A physical fusion basis can be ill conditioned;
(11) is not a bound in every metric and is not a bound for the
whole knot operator.

## 5. The omitted endpoint carry stays nonzero

In the nilpotent algebra (1) implies

    B_N(qz)B_N(z)=1-z modulo z^N.

As an ordinary polynomial its exact form is

    B_N(qz)B_N(z)-(1-z)=z^N R_N(z),
    degree R_N<=N-2.                              (12)

Using (4)-(5), its endpoint carry is exactly

    R_N(1)=4/[N^2 |1-q|^2]
          =1/[N^2 sin^2(pi/(2N))] -> 4/pi^2.      (13)

Thus the high-degree carry does NOT vanish at the source endpoint.
Replacing the canonical finite adapter there by the ordinary
square-root relation B(qz)B(z)=1-z would change the period, even
though that relation holds in the nilpotent algebra. Evaluating
before the prescribed reduction is not an algebra homomorphism.
In particular A_N(1) and B_N(1) need not be reciprocal.

## 6. Critical-path meaning and checks

This result supplies an actual meridian source adapter with a
proved subexponential condition bound, a nonzero exact endpoint
and a specified affine norm torsor. It retains precisely the
central norm and highest-degree terms that a premature evaluation
would erase. It is not a proof that the knot-dependent endpoint
sum S_N has any lower bound or nonzero geometric image. Fusion,
word transport, the peripheral line and all source sectors must
still be compared to the marked geometric A-period. The original
volume conjecture remains unproved.

[The audit](../experiments/audit_actual_euler_meridian_half_step.py)
and [saved results](../experiments/actual_euler_meridian_half_step_results.json)
pass 23 exact finite-field levels N=2,...,24. They check the
actual Euler quotients, inverses, both UNREDUCED source equations,
exact endpoints, nonzero polynomial carry and both cyclic norm
factors. Nine complex diagnostics through N=4096 check the
separately proved coefficient bounds.