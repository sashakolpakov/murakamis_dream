# The actual six-crossing source: a proved triple reduction and the missing finite transform

28 October 2026. This note reduces the ORIGINAL six-crossing four-plat,
with every turn and framing factor retained, to a three-index finite sum.
The proof uses literal finite transfer elimination and the independently
proved terminating three-factor q-Chu identity. It does not assume a
colored-Jones formula.

The attractive Rogers/Newton expansion in Section 4 remains **unproved**.
It matches the direct finite tests and its classical characteristic is
exactly the independently derived longitude quartic. Neither fact proves
the finite transform. Accordingly this note supplies no verified actual
quantum color operator for 6_1 and no new volume estimate.

## 1. The marked plat and its source

Use the conventions of the [actual four-crossing proof](figure_eight_whole_source_identity.md):
Q is any primitive Nth root, d=N-1, x=-M/q, Q=q²,
Y=Qx²=M², and xvee=x^-1 Q^-1. The actual action order is

    sigma2, sigma1^-1, sigma1^-1, sigma1^-1, sigma2, sigma2.

The braid word, with rightmost action first, is sigma2² sigma1^-3
sigma2. Its rational-tangle slope is

    T² U³ T (0,1)^t=(9,4)^t,
    T=[[1,1],[0,1]], U=[[1,0],[1,1]].                 (1)

This is the 9/4 handedness, mirror to the 9/5 convention in the
[independent longitude calculation](six_one_classical_spectral_envelope_obstruction.md).
We keep this handedness throughout the source calculation; mirroring
replaces Q by Q^-1 in the final scalar.

Top colors/orientations are (x,xvee,xvee,x), (+,-,-,+). Cut the fourth
leg with the ORIGINAL left-trace coupon D0=g E00. As in the earlier
proof, the input is

    (a,d-a,d,0), with coefficient N² x^(a-2d).       (2)

The oriented writhe is 2. With A=alpha, B=2d-alpha, the full mixed
Cartan exponent minus the actual framing exponent is exactly dB:

    sum_crossings sign*alpha_i alpha_j/2
                 -2*(A²-2dA)/2 = dB.              (3)

Thus the retained common factor is xvee^d. The final colors are
(xvee,x,xvee,x), so BOTH caps are ev_L. No ordinary quantum dimension
is divided out and no turn is moved through a crossing.

## 2. Forced transfers give an actual four-index sum

The surviving transfer list is

    (0,k,ell,r,a,0),
    0<=a, k, a+k<=d, 0<=ell<=k,
    0<=r<=d-a-k+ell.                               (4)

Indeed the first transfer is zero because its second input is d. After
the three negative crossings the state is

    (d-k+ell-r, a+k-ell+r, d-a, 0).

If the fourth positive transfer is j<=a, the final second cap forces
the last transfer j-a. Hence j=a and the last transfer is zero. The
final state is

    (d-k+ell-r, k-ell+r, d, 0).

The two cap factors multiply to x^(2d-k+ell-r)/N². This exponent is
important; replacing it by x^d gives the wrong source.

Write G_m=(Q/Y;Q)_m and let brackets denote Gaussian binomials. Direct
multiplication of the literal mixed entries, (2), the two caps, and
(3), followed only by reflection of [d choose a], gives

    F_N(Y)=sum_(4) W(a,k,ell,r),

    W=Y^(d-2a-k+r)
      Q^[1+a+2k(a+k+1)-ell(a+2k)+ell²]
      [a+k choose k] [d-k+ell choose ell]
      [a+k-ell+r choose r]
      (Q/Y)_k (Y Q^(-a-k))_ell
      (Q^(k-ell+1)/Y)_r (Y Q^(-a-k+ell-r))_a.      (5)

Here and below all Pochhammers have base Q. The root relation used to
reduce integer exponents is d=-1 modulo N; no half-power root sign is
discarded. All binomial factorial indices lie between 0 and d.

## 3. A proved three-index source

The actual same period is

    F_N(Y)=sum_(m=0)^d sum_(b=0)^m sum_(r=0)^(d-b)
       Y^(m-b) Q^(b²) [m choose b] [d-b choose r]
       G_m (Q^(b+1)/Y)_r (Q^(-2b-m-r-1))_b.       (6)

Proof. In (5) put n=a+k, m=a+k-ell+r, b=n-ell. The new support is

    0<=m,n<=d, 0<=a<=b<=min(m,n).

Reflect [d-k+ell choose ell] and invert the two Y-positive
Pochhammers. The four original Pochhammers combine to

    G_m (Q^(b-a+1)/Y)_(n-b) (Q^(b+1)/Y)_(n-b),

with sign (-1)^a. The binomials become
[n choose b][m choose b][b choose a]. The whole scalar is

    (-1)^a Y^(d+m-2b)
      Q^[1+n+b+2b²+a(a-3)/2-a(2b+m)].              (7)

For fixed m,b,a, sum n=b+l. Set K=d-b,
A=Q^(b-a+1)/Y and B=Q^(b+1)/Y. The n-dependent part is

    Q^b sum_(l=0)^K (Q^-K)_l(A)_l(B)_l Q^l/F_l
      =Q^b sum_(r=0)^K [K choose r] B^(K-r)A^r(B)_r. (8)

This is the symmetric form of the terminating three-factor identity
proved in [the five-crossing finite transform, Section 1](five_two_cyclotomic_transform_proof.md).
It applies at every primitive root because K<N and every denominator
F_l is nonzero. Now B^(K-r)A^r=B^K Q^(-ar). Combining B^K with
(7) gives the factor Y^(m-b)Q^(b²), leaving the a-sum

    sum_(a=0)^b [b choose a] (-1)^a
       Q^[a(a-1)/2-a(2b+m+r+1)]
        =(Q^(-2b-m-r-1))_b.                       (9)

The finite q-binomial theorem proves (9). This gives (6). All operations
are identities of whole Laurent polynomials in Y, so fixed-root meridian
jets and the original modified-dimension germ, if attached, are retained.
No conclusion about moving-q normal jets is drawn from differentiation
of this root identity.

## 4. The exact finite identity still required for the simple recurrence

Put

    T_n(Y)=product_(j=1)^n(Y+Y^-1-Q^j-Q^-j),
    J_n(t)=sum_(j=0)^n t^(j(j+1)) [n choose j]_t.

The candidate remaining identity is

    (6) ?= sum_(n=0)^d J_n(Q^-1) T_n(Y).            (10)

Equivalently J_n(Q^-1)=sum_j [n choose j]_Q Q^(-j(n+1)).
The direct source tests agree, but (8)--(9) do not prove (10).
No existing note supplies the additional extra-sigma1^-1 transform.

There is a useful exact algebraic target if (10) is proved. The Rogers
polynomials satisfy generically

    J_0=1, J_1=1+t²,
    J_n=(1+t-t^n+t^(2n))J_(n-1)
                      -t(1-t^(n-1))J_(n-2).      (11)

This recurrence has a separate elementary formal generating-series proof
in [the multichannel note](actual_multichannel_newton_green_transport.md).
For the MIRRORED candidate c_n=J_n(Q), its forward operator in
u=Q^n, Ec_n=c_(n+1), Eu=QuE, is

    E²-[1+Q-Q²u+Q⁴u²]E+Q(1-Qu).                  (12)

It is monic and has stable classical order. It is an exact operator on
the stated Rogers sequence, but is NOT asserted here to be an actual
6_1 coefficient operator. If (10) is proved for all primitive roots and
whole Y, ordinary-color pointing at infinitely many levels and Laurent
polynomial rigidity promote these coefficients to the generic actual
ordinary-color Newton sequence. This avoids assuming an off-root lift.

At Q=1 the coefficient characteristic is

    1-(2-u+u²)V+(1-u)V²=0, V=E^-1.

Under the independently proved classical Newton map

    u=(YL+1)/(Y+L), V=Y+Y^-1-u-u^-1,

its numerator is EXACTLY the normalized quartic (3) of
the independent 9/5 longitude calculation, multiplied by Y^4;
the denominator is Y²(Y+L)²(YL+1)². This is checked symbolically.
The unmirrored version of (12) gives L reversed. This match is a useful
consistency check and does not substitute for (10).

Even after (10), a polynomial color-shift operator and its full
inhomogeneous source must be obtained by the quantum Newton transform
with denominators and unilateral endpoints retained. Generic
noncommutative fraction-field conjugacy alone does not certify the
classical leading coefficient of a particular cleared color operator.

## 5. Reproduction and precise output

Run

```sh
python3 experiments/audit_six_one_actual_source_recurrence_port.py
```

The audit constructs the literal six original mixed crossings and every
source factor independently of (5), checks the route identity (5), the
finite intermediate (7), and (6). It labels (10) as unproved and tests it
separately. It also verifies the generic Rogers recurrence and the exact
classical quartic transform. The uniform proofs of (5)--(9) are the
finite calculations above; the tests are diagnostics rather than an
all-N proof of (10).

The usable new result is the actual three-index source (6). The specific
remaining source identity is (10). A general classical-order theorem,
a verified actual 6_1 quantum color operator, phase-aware product
asymptotics, and a broad selected geometric coefficient are still open.
