# A finite Gaussian certificate for original signed-twist source endpoints

29 October 2026. Every FIXED signed crossing power has an explicit
original-source endpoint asymptotic. Its leading coefficient is a
finite algebraic function of N modulo8k. Nonvanishing can therefore be
checked by finite exact arithmetic rather than assumed from a spectral
curve. Powers3,4,5 all pass uniformly in N. Power4 supplies the next
source endpoint after the
[two-twist interaction](actual_newton_two_twist_interaction_packet.md).
This is an endpoint theorem, not a new whole-knot asymptotic or a claim
that arbitrary recurrences have no channel conversion.

## 1. The FULL original source, including its repeated nodes and signs

Let N>=2,d=N-1,q=exp(pi i/N),Q=q^2,kappa=q^(d^2/2), and r=R/kappa.
Use the actual fixed-root g-pivotal one-cut functional phi and put

    c_j=q^(2j+1)+q^(-2j-1), A_j=q^(2j+1)-q^(-2j-1),
    nu_j=(-1)^j q^[j(j+1)], j=0,...,d.

For EVERY integer k the exact full-normal source is

    phi(r^k)=(-1)^(d+1)/2 sum_(j=0)^d nu_j^k
                  [c_j-(k/2)(d-2j)A_j].                 (1)

This is derived from the actual spectral-JET functional, not an
eigenvalue-only trace. At each double node,

    phi(f)=(-1)^d sum_double[(4-c^2)f'(c)-cf(c)]
                         +odd_simple f(-2),
    r'(c_j)/r(c_j)=-(d-2j)/(2A_j).

Since 4-c_j^2=-A_j^2, inserting f=r^k gives (1). Indices j,d-j
give equal contributions; the odd simple node has c=-2,A=0 and is
counted correctly by the half-sum. In particular the factor(-1)^d
from the ORIGINAL pivot is retained. For the full crossing multiply
(1) and all asymptotics below by kappa^k.

The small powers are explicit exceptions to a nonzero N^(3/2) leading
term: phi(1)=0, phi(r)=(-q)^d, and phi(r^2)=N(-q)^d.
They are retained exact source identities, not discarded endpoints.

## 2. A finite, residue-class leading coefficient

Fix k>0, put epsilon=k mod2, and for integers m define

    s_m=(2m-epsilon)/(2k),
    a(s)=(1-2s)sin(2pi s), b(s)=cos(2pi s),
    G_k(N)=sum_(0<s_m<1) (-1)^m a(s_m)
                      exp[-i pi N(m-epsilon/2)^2/k].     (2)

Then the all-level original source satisfies

    phi(r^k)=C_(N,k) N^(3/2)G_k(N)+O_k(N),
    C_(N,k)=(-1)^(d+1) exp[-i pi epsilon/2-i pi k/(4N)]
                                 (-i sqrt(k)/2)e^(i pi/4). (3)

When k is odd the error improves to O_k(sqrt N). Negative powers
are exactly complex conjugates of positive powers because
r^sharp=r^(-1), the Newton basis and phi being real.

To prove (3), use the half-grid s_j=(j+1/2)/N. EXACTLY on that grid,

    nu_j^k=exp[-i pi epsilon/2-i pi k/(4N)]
                                  exp[i pi N(ks_j^2+epsilon s_j)].

It is important to use epsilon, not k, in the linear term: replacing
one by the other off the lattice changes its retained integer mark.
Equation (1) is therefore the stated scalar prefactor times

    sum_j [b(s_j)-(ikN/2)a(s_j)]
                              exp[i pi N(ks_j^2+epsilon s_j)].

The periodized amplitude is continuous at0 and1 because
k+epsilon is even and a,b have matching endpoint values. Twice
integrating its Fourier coefficients proves absolute convergence,
so exact half-grid Fourier selection gives

    sum_j A(s_j)e^[i pi N(ks_j^2+epsilon s_j)]
      =N sum_(m in Z)(-1)^m integral_0^1
                    A(s)e^[i pi N(ks^2+(epsilon-2m)s)] ds. (4)

For the finitely many interior stationary points complete the square.
The compact-cutoff Gaussian integral is

    e^(i pi/4) A(s_m) e^[-i pi N(m-epsilon/2)^2/k]/sqrt(kN)
                                                   +O_k(N^(-3/2)).

An elementary justification is Fourier inversion of the smooth cutoff
amplitude, the damped Gaussian integral, and
|exp(it)-1|<=|t| against its integrable second Fourier moment.
Away from those cutoffs two integrations by parts give summable
O_k(N^(-2)(1+|m|)^(-2)) when A=a. For A=b the first boundary
terms have matching endpoint phases and their difference is
O_k(N^(-1)(1+|m|)^(-2)); hence their total is still summable.

For odd k there is no endpoint resonance: the a sum in(4) equals its
displayed stationary contribution plus O(N^(-1/2)). The b sum itself
is O(sqrt N), with nonstationary remainder O(1). For even k the two
possible resonant endpoints have a=0. Write a(s)=s a_0(s) near0
and similarly near1; one integration using the derivative of
exp(i pi Nk s^2) bounds each endpoint integral by O_k(1/N).
Their contribution to(4) is O_k(1). The b sum is O_k(sqrt N).
Multiplying the a sum by N proves the error in(3). All endpoint
and half-grid currents have thus been included.

## 3. A finite NONVANISHING test, and three explicit uniform cases

Every coefficient in (2) is algebraic, and G_k(N) is periodic in
N modulo8k. Consequently, if its finitely many residue-class values
are all nonzero, their minimum modulus is positive and (3) proves

    c_k N^(3/2)<=|phi(R^k)|<=C_k N^(3/2)                 (5)

at every sufficiently large level, with no parity or coprimality
restriction. Failure of this leading test does not prove a zero
endpoint: lower-order terms may survive. For example k=1,2 have
G_k=0 and require their exact lower-order identities.

Here are own exact nonvanishing checks:

    G_3(N)=-(2sqrt3/3)exp(-i pi N/12),
    G_4(N)=-exp(-i pi N/4).

For k=5 put a_1=(4/5)sin(pi/5), a_2=(2/5)sin(3pi/5).
Pairing m with k+1-m gives

    G_5(N)=2exp(-i pi N/20)[-a_1+a_2exp(-2pi i N/5)],
    |G_5(N)|>=2(a_1-a_2)
       =(8/5)sin(pi/5)[1-cos(pi/5)]>0.                  (6)

These are uniform exact phase calculations, not fits at sampled levels.

## 4. A genuinely new endpoint for the next reduced turn word

Let the original finite Green coefficients be

    P_i=F_i^2 sum_(v=0)^i Q^v/F_v^2,
    P_0=1, P_i=(1-Q^i)^2P_(i-1)+Q^i.

The exact Newton source column obeys

    (r^3 1)_i=(-q)^i P_i,
    phi(r^4)=(-q)^d sum_(i=0)^d P_i.                    (7)

For a finite proof of the first equality, multiply the known r and
r^2 source kernels. The remaining convolution is
F_i sum_j nu_j/F_(i-j); its generating series satisfies the displayed
first-order P recurrence, with P_0=1. The second equality uses
nu_j[d choose j]_Q=1 in the literal last-row multiplication by r.

Combining k=4 in(3),(6) with(7) gives the explicit all-parity endpoint

    sum_(i=0)^d P_i
      =N^(3/2)exp[i pi(3-N)/4]+O(N).                    (8)

Thus the next repeated-two-twist source has a known nonzero polynomial
endpoint, rather than an unknown boundary value. Its interior is a
new higher-order Ward problem; (8) does not by itself prove the
necessary dominant projection or a coherent long-word estimate.

This is the reusable analytic input a purely algebraic A-curve test
would miss. A marked recurrence and its spectral cover must be
supplemented by the ACTUAL source endpoint and any reciprocal
inhomogeneous current. The finite certificate(2)--(5) supplies such
endpoints for a family of original twist powers. It is a root-value
source theorem; no q-normal derivative of a different generic source
germ is substituted.

## 5. The next actual reduced word has an explicit rank-three current

The previous endpoint is not merely a free parameter. Put C=T_1P_rev
and consider its actual source vector C T_(-3)1. Its coefficients are

    (C T_(-3)1)_i=kappa^(-2)(-q)^(i-d)K_i,
    K_i=sum_(j=0)^i nu_j [i choose j]_Q conjugate(P_(d-j)). (9)

The modular reduction identifies this with the fourth repeated
two-crossing/turn run, up to its already recorded unit scalar. Thus
it is a genuine next-depth original word, not an arbitrary clock coupon.
Its two scalar endpoints are known:

    K_0=conjugate(P_d),
    K_d=sum_j conjugate(P_j).                            (10)

They have the nonzero polynomial asymptotics of powers3 and4 above.

There is also an EXACT whole-index Ward equation, including its current.
Write G_i=K_i/F_i, G_i=0 for i<0, and Y=Q^i. Then for1<=i<=d,

    (1-Y)^3 G_i+B_iG_(i-1)+C_iG_(i-2)+D_iG_(i-3)
                                             =Q^2 delta_(i,1),
    B_i=-(1+Q+Q^2)+(4+3Q)Y-3Y^2,
    C_i=Q+Q^2+Q^3-(1+4Q)Y,
    D_i=Q^3(Q^(i-2)-1).                                (11)

In particular D_2=0 is a second exact source reset. To verify (11),
put B_j=conjugate(P_(d-j)); its original backward Green relation is
(1-Q^j)^2B_j=B_(j-1)-Q^j. The coefficient
a_j=nu_j B_j/F_j therefore satisfies

    (1-Q^j)^3a_j=-Q^j a_(j-1)-nu_j Q^j/F_(j-1).

Convolve with E(z)=sum z^k/F_k and use
sum nu_j z^j/F_j=(Qz;Q)_infinity, as a formal identity below degreeN.
The generating equation is

    (z;Q)_3G(z)+(Qz-3)(1-Qz)(1-Q^2z)G(Qz)
                    +3(1-Q^2z)G(Q^2z)-G(Q^3z)=Q^2z,

whose coefficients are exactly (11). All finite denominators are units.

For the monic variable M_i=F_i^3G_i=F_i^2K_i the classical spectral
polynomial is

    lambda^3+(-3+7Y-3Y^2)lambda^2
              +(3-5Y)(1-Y)^3lambda-(1-Y)^7.             (12)

At Y=1 this is lambda^2(lambda+1). The initial data obey
M_0=conjugate(P_d),
M_1=(1-3Q+Q^2)conjugate(P_d)+Q^2; the actual current is visible.
Equation (12) is a concrete new vector-recurrence test for any proposed
general spectral criterion. The known scalar endpoints (10) do NOT
by themselves determine its dominant projection across the cubic
cover. That requires a full vector boundary/current certificate; no
single-branch survival or sharp next-depth rate is asserted here.

Audit: [full original signed matrices, finite coefficients and Gaussian endpoints](../experiments/audit_actual_twist_endpoint_gaussian_certificate.py).

Independent proof review and primary replay passed, including the
fixed-root pivot sign, all original positive/negative matrices,
half-grid marks, endpoint resonances and explicit k4/k5 nonvanishing.
The k=0,1,2 exceptions and possible vanishing of a scalar leading
coefficient remain explicit. The
[endpoint-vector companion](actual_newton_run_endpoint_vectors.md)
resolves all Gaussian boundary modes even when that scalar cancels.
