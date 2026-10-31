# Negative roots of the actual complete-channel source polynomial

30 October 2026. The finite polynomial inside EVERY physical
complete-channel q-Hahn column has only negative nonzero roots.
They are simple; its sole possible zero at the origin is the forced
support power. This is an all-level theorem for the ACTUAL finite
coefficients, not an inference from the stationary quadratic or a
sampled real-root plot. In particular the physical Fourier evaluation
of that polynomial never vanishes.

The proof uses an exact two-binomial recurrence and an elementary
sine coefficient multiplier. An independent sine-operator peeling
proof of the two-binomial step is retained in section5.

## 1. The exact source polynomial and its support

Put N>=2, d=N-1, theta=pi/N, q=exp(i theta), and

    s_r=product_(k=1)^r 2sin(k theta), s_0=1,
    beta(n,a)=s_n/[s_a s_(n-a)] for 0<=a<=n,
    beta(n,a)=0 outside that integer range.

For physical 0<=t<=d, 0<=u<=t and 0<=j<=t set v=t-u and

    P_(t,j,u)(z)=sum_a E_a z^a,
    E_a=beta(j,a) beta(u,a) beta(v,j-a)/beta(t,j).           (1)

Its nonzero support is exactly

    a0=max(0,j-v), a1=min(j,u), n=a1-a0.                   (2)

All coefficients in this interval are strictly positive. The actual
[complete augmented-plat compiler](actual_augmented_plat_phase_compiler.md)
uses the further restrictions j<=floor(d/2), t+j>=d and the exact
physical evaluation

    f_u(c_j)=(-1)^u q^[-(j+1)u] P_(t,j,u)(q^delta),
    delta=t+j-d>=0.                                       (3)

Equation (1) is precisely that finite compiler coefficient, with no
q-factorial normalizer omitted. The theorem holds even without those
further complete-image restrictions:

    P(z)=C z^a0 product_(h=1)^n(z+rho_h),
    C>0, rho_h>0, and all rho_h distinct.                  (4)

If n=0 this is a positive monomial, with no nonzero roots to list.

## 2. A two-binomial polynomial has simple negative nonzero roots

For u,v>=0 with t=u+v<N define

    Q_j^(u,v)(z)=sum_a beta(u,a) beta(v,j-a) z^a,
    0<=j<=t.                                             (5)

The symmetric quantum-binomial product is the finite identity

    B_k(w)=sum_a beta(k,a)w^a
          =product_(r=0)^(k-1)(1+q^(k-1-2r)w).            (6)

For an elementary proof, use
B_k(w)=(1+q^(k-1)w)B_(k-1)(q^-1 w). The two coefficient terms
combine to beta(k,a) by the sine addition identity; B_0=1 starts
the induction. No root-location assertion for B_k is made: its roots
usually lie on a unit-circle arc.

Let F(w,z)=B_u(zw)B_v(w)=sum_j Q_j(z)w^j. Its q-shifts obey

    (1+q^-u zw)(1+q^-v w)F(qw,z)
      =(1+q^u zw)(1+q^v w)F(q^-1 w,z).

Comparing the coefficient of w^j and dividing by 2i gives the EXACT
three-term recurrence

    sin(j theta) Q_j
      =[z sin((u-j+1)theta)+sin((v-j+1)theta)] Q_(j-1)
         +z sin((t-j+2)theta) Q_(j-2),                    (7)

with Q_0=1 and
Q_1=[sin(u theta)z+sin(v theta)]/sin theta.

First suppose j<=min(u,v). For 2<=j<=min(u,v), every sine coefficient
shown in (7) is strictly positive, since t<N. At any negative zero r
of Q_(j-1), the sign of Q_j(r) is opposite to that of Q_(j-2)(r).
Starting with Q_0,Q_1, a direct induction therefore gives j SIMPLE
negative roots of Q_j strictly interlacing those of Q_(j-1). For
completeness, adjacent roots of Q_(j-1) give j-2 alternating sign
intervals; its rightmost root has Q_j<0 while Q_j(0)>0; and its
leftmost root has sign opposite to the sign of Q_j at negative
infinity. These provide all j roots. The leading and constant
coefficients are positive by (5).

All other j are reduced to this case by the following EXACT identities:

    Q_j^(u,t-u)(z)/beta(t,j)
       =Q_u^(j,t-j)(z)/beta(t,u),                         (8)
    Q_j^(u,v)(z)=z^u Q_(t-j)^(u,v)(1/z),                 (9)
    Q_j^(u,v)(z)=z^j Q_j^(v,u)(1/z).                     (10)

Identity (8) follows coefficientwise by canceling six sine factorials;
(9),(10) follow from beta(k,a)=beta(k,k-a). Their Laurent expressions
are exactly polynomials because the same forced support zeros are
present on both sides.

Choose the smallest of j,t-j,u,v. If it is j, use (7). If it is t-j,
use (9). If it is u, use (8). If it is v, use (10) and then (8).
The new degree parameter is at most both new group sizes, so the
previous Sturm induction applies. Reversal replaces each nonzero
negative root by its reciprocal and multiplication by a positive
constant or a forced power of z does not change its sign or simplicity.
Thus (5) has exactly its forced zero of order a0, followed by n simple
negative roots, for EVERY 0<=j<=t<N.

## 3. The sine multiplier preserves negative roots

Let D=z d/dz and define the REAL coefficient operator

    S_r=sin[theta(D+r)],
    S_r A(z)=[e^(ir theta)A(e^(i theta)z)
                        -e^(-ir theta)A(e^(-i theta)z)]/(2i). (11)

Suppose A has degree n and only negative roots, with positive leading
coefficient, and 0<r, r+n<N. Then S_r A has n SIMPLE negative roots.
Here is a direct proof. Write A(z)=C product(z+rho_h), rho_h>0.
For x>0 follow the continuous argument

    arg[e^(ir theta)A(-e^(i theta)x)].

Each factor rho_h-x e^(i theta) has strictly decreasing argument,
with derivative -rho_h sin(theta)/|rho_h-x e^(i theta)|^2. The total
argument decreases from r theta to (r+n)theta-n pi. It crosses exactly
0,-pi,...,-(n-1)pi, once each. Those crossings are exactly the n negative
roots of (11); the factors being measured never vanish on x>0.
Its leading and constant coefficients are positive. Repeated roots
of the input do not spoil the strict argument monotonicity.

A forced power z^a is retained: S_r[z^a A]=z^a S_(r+a)A. Thus the
same assertion applies if 0<r+a and r+a+n<N.

The elementary root reflection s_a s_(d-a)=N gives

    beta(j,a)=s_j/N product_(r=1)^(d-j) 2sin[(a+r)theta],
                         0<=a<=j.                       (12)

Consequently multiplication of the a-th coefficient by beta(j,a),
on a polynomial of degree at most j, is the exact operator

    M_j=(s_j/N) 2^(d-j) product_(r=1)^(d-j) S_r.           (13)

Every factor in (13) satisfies r+degree<=d<N. On a polynomial with
its forced zero at the origin the shifted inequality in section3
is the same one. It therefore preserves that zero and all remaining
negative roots. Applying M_j to Q_j and dividing by the positive
beta(t,j) gives precisely (1). Equations (5)--(13) prove (4).
The empty product j=d causes no exception: then j=t=d and n=0.

## 4. The actual Fourier value and its logarithmic branch

In the complete-image chamber, 0<=delta<=j<=floor(d/2). Thus
q^delta has argument between 0 and pi/2, strictly below pi/2 at
finite N. It lies away from every zero in (4), so the ACTUAL
canonical column (3) is nonzero, including all magnetic endpoints.

More generally P(z)/P(1) has a canonical holomorphic logarithm on
C minus the nonpositive real axis, fixed to be zero at z=1. Its exact
factorization is

    Log[P(z)/P(1)]=a0 Log z
             +sum_h Log[(z+rho_h)/(1+rho_h)].              (14)

For real |phi|<pi this also gives the elementary bound

    cos(phi/2)^n <= |P(e^(i phi))|/P(1) <= 1.              (15)

This follows from
|e^(i phi)+rho|^2=(1+rho)^2-4rho sin^2(phi/2).
The loss in (15) can be exponential in N. It is not a subexponential
whole-source bound, a Gaussian amplitude estimate, or a proof of
noncancellation after summing different physical magnetic variables.
The zero-free logarithm is the rigorous input for a separate local
complex asymptotic argument.

## 5. Independent sine-operator peeling proof of section2

There is a second own proof that does not use the recurrence or the
intersection duality. Begin with the finite Laurent polynomial

    A_initial(z)=z^j B_v(1/z)=z^(j-v) B_v(z).

Apply the coefficient multiplier beta(u,a). By (12) with j replaced
by u, it is proportional to product_(r=1)^(d-u) S_r. The same product
is zero on every unwanted Laurent power: for a<0 the factor r=-a
occurs, and for a>u the factor r=N-a occurs. This uses v<=d-u and
j<=u+v<=d. On the wanted powers it equals beta(u,a) exactly, so its
output is the polynomial (5).

The factors commute. If j>u, apply first r=N-j,...,d-u in increasing
order. The identity

    S_(N-k) B_k=sin(k theta) B_(k-1)

removes each forced high power, with the fixed prefactor z^(j-v)
accounted for in the shift. If j<v, next apply r=v-j,...,1 in
decreasing order. The identity

    S_0 B_k=sin(k theta) z B_(k-1)

removes each forced negative Laurent power. All extracted constants
are positive. The remaining polynomial is a positive multiple of
z^a0 B_n(z), with a0,n as in (2).

The unused factors have r from max(0,v-j)+1 to d-max(u,j).
After extracting z^a0 their parameters are s=r+a0. They satisfy
0<s and s+n<N, and their number is

    n+(d-t) >= n.                                       (16)

Use at least n of these factors to strip B_n. More generally,

    S_s[B_k(z) A(z)]=B_(k-1)(z) T_(s,k)A(z),
    T_(s,k)A=Im{e^(is theta)(1+q^k z)A(qz)}               (17)

for real z; equivalently take the two conjugate polynomial terms
as in (11). If A has m negative roots, positive leading coefficient,
and k+m=n, the argument at z=-x decreases strictly from s theta to
(s+k+m)theta-(m+1)pi. Here 0<k<N and 0<s+n<N. It therefore crosses
exactly m+1 multiples of pi, giving T_(s,k)A exactly m+1 SIMPLE
negative roots and positive leading/constant coefficients.

Starting with A=1, each step reduces k by one and increases m by one.
After n steps no B factor remains and all roots are negative. The
remaining d-t ordinary S_s factors preserve them by section3. This
independently proves the complete support and root assertion for Q.
It also explains why a reciprocal sine factorial by itself need not
be a multiplier: the proof uses the whole paired coefficient structure.

Audit: [exact recurrence, dualities, finite source coefficients and root counts](../experiments/audit_actual_q_hahn_negative_root_source_polynomial.py).

Numerical root counts remain regression checks, not the all-level proof.
