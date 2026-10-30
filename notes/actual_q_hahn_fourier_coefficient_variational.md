# Exact coefficient duality for the original complete-channel polynomial

30 October 2026. The positive coefficients
of the actual magnetic polynomial are log-concave. Consequently a
positive-radius evaluation recovers each coefficient within a factor
at most j+1. The selected ordinary source action then gives a uniform
coefficient rate, with an explicit optimal radius, throughout the
interior coefficient-slope domain.

This theorem keeps the source's physical total and integer channel.
It neither deletes the Fourier phases when coefficients are sewn nor
proves cancellation control for the original graph contraction.

## 1. The original polynomial and its positive coefficients

Put d=N-1, q=exp(pi i/N), Q=q^2, and retain the ACTUAL complete range

    0<=j<=floor(d/2), d-j<=t<=d.

The proved magnetic factorization is

    fhat(u)=q^(du) Q^(-ju) G_t(Q^u),
    G_t(q^t z)=c_t P_(N,t,j)(z),
    c_t=q^[j(t+j-d)]/(Q;Q)_j,
    P(z)=B_h(z) A_n(z)=sum_(k=0)^j p_k z^k,
    h=d-t, n=t+j-d, h+n=j.                         (1)

Here B_h has the positive coefficients beta(h,k)=s_h/(s_k s_(h-k)),
where s_r=product_(a=1)^r 2sin(pi a/N). The actual residual A_n has
positive leading coefficient and n negative real roots. These are
properties of the original coproduct polynomial, proved in
[the magnetic corridor theorem](actual_q_hahn_magnetic_complex_corridor.md),
not a replacement of its values by an interpolating polynomial.
In particular p_k>0 for every 0<=k<=j.

The source condition t+j>=d is essential here. Although its ordinary
analytic continuation has a larger domain, positivity of this
factorization is not asserted for arbitrary nonphysical t or for
limiting tau+xi<1.

## 2. Log-concavity and an exact polynomial-loss duality

The coefficient sequence p_0,...,p_j is log-concave:

    p_k^2>=p_(k-1)p_(k+1), 1<=k<j.                 (2)

An elementary proof is enough. The consecutive ratio of B_h is

    beta(h,k)/beta(h,k-1)
                     =sin((h-k+1)pi/N)/sin(k pi/N).

Its decrease follows by cross multiplication: the difference of the
two adjacent numerators is sin(pi/N)sin((h+1)pi/N)>0. The h=0
sequence consists of one coefficient and is included.

Now let a_k be any nonnegative log-concave sequence with interval
support, extended by zero elsewhere. Multiplication of its polynomial
by z+rho, rho>0, gives b_k=rho a_k+a_(k-1), and

    b_k^2-b_(k-1)b_(k+1)
      =rho^2(a_k^2-a_(k-1)a_(k+1))
       +rho(a_k a_(k-1)-a_(k-2)a_(k+1))
       +(a_(k-1)^2-a_(k-2)a_k)>=0.                 (3)

The middle term is nonnegative by the decreasing consecutive ratios;
zero endpoints cause no problem. Factoring A_n into its positive
linear factors and iterating (3) proves (2).

For EVERY k=0,...,j the exact finite statement is

    p_k <= inf_(w>0) P(w) w^(-k) <= (j+1)p_k.       (4)

The first inequality holds because p_k w^k is one positive summand.
For an interior k choose

    p_(k-1)/p_k <= w <= p_k/p_(k+1).

This interval is nonempty by (2). At such a tilt, the kth term is
a mode of the entire sequence p_l w^l, again by decreasing ratios.
Its sum is at most j+1 times that term, proving the upper inequality.
For k=0 and k=j, take w to zero and infinity respectively; the
infimum equals the endpoint coefficient. For j=0 all statements
are identities.

Thus (4) is a two-sided estimate for actual coefficients, with no
unknown exponentially small cancellation or probability prefactor.
It is not an asymptotic Gaussian coefficient formula.

## 3. The correct radial free energy and its explicit derivative

Set tau=t/N, xi=j/N and w=exp(y), y real. Because the polynomial
coordinate in (1) is z=Q^u/q^t, the corresponding magnetic variable is

    nu=u/N=tau/2-i y/(2pi).                         (5)

The reciprocal determinant coordinate is 1/w, not w. Taking absolute
values in the EXACT source normalization (1) gives

    log P(exp y)=log s_j-(d-2j)y/2+log|fhat(N nu)|. (6)

Use the actual selected action Phi_xi from
[the full physical packet](actual_q_hahn_full_physical_complex_packet.md).
For complete physical indices with tau in a fixed compact subinterval
of (1/2,1), xi bounded away from zero, and y in a fixed finite interval,

    N^(-1)log P(exp y)=F(tau,xi;y)+O(log N/N),
    F=J(xi)-(1/2-xi)y
                    +Re Phi_xi(tau,tau/2-i y/(2pi)).             (7)

The scaled parameters in (7) are their ACTUAL values at level N.
The possible complete boundary displacement tau+xi=1-1/N is retained;
its limiting parameters satisfy tau+xi>=1. The packet and the
factorial estimate are uniform for these indices. The derivative
in y of the error in (7) is O(1/N) on smaller compact intervals.
The log s_j term is independent of y and has not been dropped.

There is an explicit derivative requiring no new saddle selection.
Put

    c=-cos(pi tau)>0, C=cos(pi xi), s=sin(pi xi)>0,
    B=w^2+2cw+C^2.

On (5) the selected multiplier is

    Y=exp(Phi_nu)=(s+i sqrt(B))^2/(1+2cw+w^2),
    Arg Y=2 arctan(sqrt(B)/s) in (0,pi).             (8)

It has modulus one, and the square root is positive real. This is
the already calibrated ordinary branch on this central vertical line.
Differentiating (7), with its MINUS sign in (5), yields

    F_y=xi-1/2+pi^(-1) arctan(sqrt(B)/s),
    F_yy=s w(w+c)/[pi sqrt(B)(1+2cw+w^2)]>0.         (9)

As y tends to minus or plus infinity, F_y tends respectively to
0 and xi, including the folded endpoint C=0. Every interior slope
0<lambda<xi therefore has a unique finite optimal tilt. It is
explicitly

    a=pi(1/2-xi+lambda),
    w_*=sqrt(c^2-C^2+s^2 tan(a)^2)-c>0,
    y_*=log w_*.                                   (10)

The quantity s tan(a) is strictly greater than C for lambda>0,
which proves positivity of this root. Formula (10) also gives uniform
finite tilt bounds on compact interior slope families.

Equivalently, the selected magnetic momentum at that coefficient is

    Y_*=exp[2pi i(lambda+1/2-xi)],
    Log Y_*=2pi i(lambda+1/2-xi) in i(0,pi).          (10a)

Thus the Fourier index prescribes the FULL local phase on this
selected radial saddle, not only the modulus of a multiplier. Its
radial boundary variable is the positive root (10), equivalently
w_*^2+2cw_*+C^2=s^2 tan^2(pi(1/2-xi+lambda)). Actual network
orientation and incidence are still needed to combine these local
characters into global equations.

## 4. Uniform actual coefficient rates

Take any compact family of limiting complete parameters with
1/2<tau<1, 0<xi<=1/2 and tau+xi>=1. Keep the coefficient slope
lambda strictly inside (0,xi), uniformly on that family. For all
legal integer sequences N,t,j,k approaching this family, use the
actual scaled values tau_N=t/N, xi_N=j/N, lambda_N=k/N. Define

    L(tau,xi,lambda)
       =F(tau,xi;y_*)-lambda y_*,                  (11)

where (10) fixes the unique positive tilt. Then

    log p_k=N L(tau_N,xi_N,lambda_N)+O(log N),        (12)

uniformly over that family and both level parities. The value in
(11) is also the infimum over all real y of F-lambda y. Its slope
derivatives obey

    L_lambda=-y_*, L_(lambda lambda)=-1/F_yy(y_*)<0. (13)

For completeness, no unbounded minimizer is hidden in (12). The
finite function F_N(y)=N^(-1)log P(exp y) is convex, and its derivative
is the tilted mean of k/N. Choose fixed endpoints y_-<y_+ beyond
the compact set of optimal tilts (10). By (9) there is a uniform
strict gap between F_y(y_-) and the target slopes, and between
those slopes and F_y(y_+). The derivative convergence in (7) puts
every finite minimizer of F_N-lambda_N y in [y_-,y_+] for large N.
The uniform value estimate (7), followed by (4), proves (12).

Boundary slopes k/N approaching zero or xi, unbounded tilts, and
physical degree endpoints tau=1/2 or tau=1 are outside this uniform
statement. Their exact finite inequality (4) remains valid; a rate
or relative amplitude at those boundaries needs its own estimates.
No relative coefficient amplitude is claimed even in the interior.

## 5. What this supplies for a sewn source

Each original coefficient has now an actual positive radial variational
description, retaining its normalizer and its Fourier index. This
permits the index k to remain a shared variable in an exact affine
wire/cycle compiler. If a positive comparison partition is assembled
from these coefficients, their actions must first be summed on that
shared incidence set before taking any maximum.

The original magnetic source is reconstructed with its displayed
Fourier factors and scalar c_t. A positive coefficient theorem does
not erase those phases, identify a graph contraction with the product
of coefficient envelopes, or prove a nonzero geometric overlap.
Those are separate requirements for the full volume conjecture.

Focused audit: [original positive coefficients and radial duality](../experiments/audit_actual_q_hahn_fourier_coefficient_variational.py).
Three formal identities check the log-concavity step, curvature and
inverse tilt. At 90 digits, 794 actual positive polynomials satisfy
3,938 log-concavity and tilted-mode checks; nine literal off-lattice
source values check the radial sign and normalization. Eighteen
interior coefficient sequences check the stated rate and tilt gradient.
The uniform theorem is proved above, not inferred from those sequences.

Independent analytical reviews: PASS. The root reader and an independent
reader checked the original polynomial support and scalar, log-concavity
including endpoints, modal infimum inequality, corrected radial sign,
selected characteristic and strict curvature, explicit tilt, and the
uniform trapping of finite minimizers. A fresh independent audit replay
passed all three formal identities, 794 polynomials, 3,938 mode checks,
nine original radial source values, and eighteen coefficient-rate checks.
The reviews retain discrete channels, interior slopes and the distinction
between positive coefficients and a coherently sewn graph source.
