# Actual multichannel Newton transport beyond the tame figure-eight source

28 October 2026. The actual five-crossing Newton source does NOT have a
polynomially bounded coefficient vector. This can be proved directly,
without using its volume theorem: a uniformly dominated initial transfer
branch forces exponential growth of a genuine Newton coefficient.
Consequently a polynomially bounded source-preserving comparison to the
previous tame UL response cannot exist in this universal Newton basis.

There is nevertheless a source-exact two-channel replacement. Both endpoint
source vectors have polynomial norms. Forward and backward Green transport
therefore give a strictly sharper coefficient barrier than the one-sided
largest-root bound. Combining it with the ORIGINAL complete evaluation,
and then the audited root-color Plancherel identity, gives an unconditional
quantitative upper bound for this full source. Its barrier is about
0.57776, whereas the selected invariant's known rate is about 0.45011.
The remaining outer phase cancellation has not been eliminated.

The matrix estimate in Section 4 applies to fixed-channel recurrences
generally. No new knot class or general volume bound is claimed.

## 1. The original coefficients and their exact monic recurrence

The independently proved WHOLE-source transform in
`five_two_cyclotomic_transform_proof.md` gives, at every primitive root,

    F_N(Y)=sum_(n=0)^(N-1) C_n T_n(Y),
    T_n(Y)=product_(r=1)^n(Y+Y^-1-Q^r-Q^-r),
    C_n=(-1)^n t^(n(n+3)/2) J_n(t), t=Q^-1,
    J_n(t)=sum_(j=0)^n t^(j(j+1)){n choose j}_t.   (1)

All original turns, Cartan scalars and framing are included in that
identity. No coefficient is chosen to fit an unknown scalar. The phases
preceding J_n have modulus one at the specified root.

The coefficients satisfy, GENERICALLY in t,

    J_0=1, J_1=1+t^2,
    J_n=(1+t-t^n+t^(2n))J_(n-1)
                         -t(1-t^(n-1))J_(n-2).  (2)

Here is an elementary derivation. Put F_n=(t;t)_n and, formally,

    E(z)=sum_(k>=0)z^k/F_k,
    G(z)=sum_(j>=0)t^(j(j+1))z^j/F_j,
    H(z)=sum_(n>=0)J_n z^n/F_n=E(z)G(z).

Coefficient comparison gives E(tz)=(1-z)E(z) and
G(z)-G(tz)=t^2 z G(t^2z). Eliminating E yields

    (1-z)(1-tz)H(z)-(1-tz)H(tz)-t^2zH(t^2z)=0.

Its n-th coefficient is (2). This is a formal identity before root
specialization; at n<N no vanishing factorial is divided out.

With w_n=(J_n,J_(n-1))^t, n>=1, the actual transfer is

    w_n=M_(N,n)w_(n-1),
    M_(N,n)=[[1+t-t^n+t^(2n), -t(1-t^(n-1))],
             [1,                 0          ]].   (3)

Its leading coefficient is ONE, so there is no singular forward division.
Its determinant is t(1-t^(n-1)), nonzero for 2<=n<=N-1.

## 2. The terminal source is known and polynomial too

At t^N=1, root reflection gives

    {N-1 choose j}_t=(-1)^j t^(-j(j+1)/2).

Thus J_(N-1) is the explicit quadratic Gauss sum
sum_(j=0)^(N-1)(-1)^j t^(j(j+1)/2), of modulus at most N.
Likewise

    {N-2 choose j}_t={N-1 choose j}_t
                              (1-t^(-1-j))/(1-t^-1).

Since |1-t^-1|>=4/N, (1) proves |J_(N-2)|<=N^2/2. Therefore both
w_1 and the ACTUAL terminal w_(N-1) have polynomial norms. These
endpoint bounds are finite coefficient identities, not an assumption
that the desired Kashaev value is small.

## 3. A direct all-level obstruction to a tame UL coefficient response

For x=n/N let z=exp(-2pi i x). The continuous transfer limit is

    M(x)=[[2-z+z^2, -(1-z)], [1,0]],
    p(z,L)=L^2-(2-z+z^2)L+1-z.                   (4)

For 0<=x<=1/32, |z-1|<=pi/16<1/5. Hence
|2-z+z^2-2|<1/5 and |1-z|<1/5. On |L-2|=1/2,
the unperturbed |L(L-2)| is at least 3/4, whereas the perturbation
is at most (1/5)(5/2)+(1/5)=7/10. Rouche's argument gives a single
analytic root L_+ in that disk, so |L_+|>=3/2. The other root has
modulus at most (1/5)/(3/2)=2/15. The eigenvectors (L_+,1) and
(L_-,1) give a uniformly smooth, invertible eigenframe on this interval.

In that frame each finite step (3) equals diag(L_+,L_-)+O(1/N),
uniformly, including the frame change at adjacent x. Its initial vector
w_1 tends to (2,1), the L_+ eigenvector at x=0. The ratio of the second
component to the first is O(1/N) initially and remains O(1/N): the
offdiagonal entries are O(1/N), while |L_-/L_+|<=4/45<1. Induction
therefore keeps a fixed O(1/N) cone. The first component is multiplied
at each step by L_+(x)+O(1/N), and the resulting product error is
bounded above and below by constants on this fixed-length x interval.
The original first coordinate J_n has the same exponential rate.

For n=floor(N/32), this proves the unconditional lower estimate

    liminf_N (1/N)log||C^(N)||_2
                          >=log(3/2)/32>0.       (5)

The tame fixed-window UL theorem has polynomial coefficient response.
Equation (5) therefore rules out representing THIS actual coefficient
vector by that response under a comparison whose map AND inverse have
polynomial norms and preserve the pointed source. In particular a
diagonal unitary phase gauge cannot fix it. This statement does not
rule out a different metric, a genuine multichannel transport, or
later source-exact fusion; their exponential evaluation cost must stay.

## 4. A uniform two-boundary matrix estimate

Let T_(N,n) be a fixed-size matrix family converging uniformly to
continuous T(x). Suppose rho(T(x)) and rho(adj T(x)) are positive on
the parameter interval, and every actual determinant in its interior
is nonzero. For a specified solution with polynomial endpoint norms,
forward and backward propagation give

    (1/N)log||w_n|| <=min{ H_f(n/N), H_b(n/N)}+o(1), (6)

uniformly in n, where

    H_f(x)=integral_0^x log rho(T(s))ds,
    H_b(x)=integral_x^1 log rho(adj T(s))ds
                   -lim (1/N)sum_(ell=n+1)^(N-1)log|det T_(N,ell)|.

An endpoint factorial product or leading-germ identity must justify the
last limit uniformly; it is not silently inferred at an exact zero.

To prove the numerator estimates, fix epsilon>0 and use the positive
Lyapunov metric

    H_eps(x)=sum_(k>=0)(T(x)^*)^k T(x)^k
                             /(rho(T(x))+epsilon)^(2k).

For bounded matrices of fixed size this converges uniformly, is
continuous, is at least I and bounded above. In its norm, a step costs
at most rho(T(x))+epsilon+o(1); neighboring metric changes cost 1+o(1).
Products over ANY prefix therefore obey the integral bound uniformly
in the prefix endpoint. Apply the same argument to adj T in reverse
order, and use the EXACT identity T^-1=adj T/det T. The polynomial
endpoint norms cost o(N). Let epsilon decrease to zero. Positivity
of the continuous spectral radii makes the logarithmic limit uniform.
This proves (6), with the original endpoint vectors retained.

It is a source-sensitive bound on a specified solution, not a claim
that the entire inverse norm is controlled or that every growing
channel couples to the source.

## 5. Actual two-channel barrier and the full Fourier energy

For (4), write R(x)=rho(M(x)) and

    H(x)=integral_0^x log R(s)ds,
    J(x)=integral_0^x log(2sin(pi s))ds.

The eigenvalues are explicit:

    L_±=(2-z+z^2 ± z sqrt(z^2-2z+5))/2.           (7)

The square root has its principal analytic branch here, since its
argument has real part at least 7/2 on the unit circle. R is continuous
and positive; for example |2-z+z^2|^2>=7/8 gives R>=sqrt(14)/8.
For a two-by-two matrix, rho(adj M)=rho(M). The determinant product
in backward propagation is exactly

    product_(ell=n+1)^(N-1)|det M_(N,ell)|
                   =|F_(N-2)|/|F_(n-1)|.        (8)

The endpoint-uniform factorial estimate and |F_(N-2)|=O(N^2) give
its logarithm as -N J(n/N)+O(log N), uniformly for n>=1. Thus

    (1/N)log|C_n| <=h(n/N)+o(1),
    h(x)=min{H(x), H(1)-H(x)+J(x)}.              (9)

Retain the ORIGINAL complete evaluation T_n(1)=|F_n|^2 in (1).
The triangle bound on this exact sum, now with its n-dependent
coefficient transport retained, gives

    limsup_N (1/N)log|K_N|
        <=B_2:=max_(0<=x<=1){2J(x)+h(x)}.        (10)

By the independently audited ordinary-color theorem, the full root-color
Fourier energy E_N=|K_N|^2+poly(N) consequently satisfies

    limsup_N (pi/N)log E_N<=2pi max(0,B_2).       (11)

This use of Plancherel keeps the actual cancellations of ordinary rows;
bounding every entry of the Newton evaluation matrix separately would
lose that information and give a larger estimate.

There is a useful exact simplification of (10). R(1-x)=R(x),
J(1-x)=-J(x), and

    d/dx[2H(x)-J(x)]
              =log(|L_max(x)|/|L_min(x)|)>=0.

The switch in (9) is therefore at x=1/2. Since J<=0 on [0,1/2],

    B_2=max_(0<=u<=1/2){H(u)-3J(u)}.             (12)

This is a completely specified one-variable positive-norm barrier,
not the desired volume inserted as a hypothesis. The audit bounds it
rigorously between 0.5775 and 0.5780; its numerical value is approximately
0.57776062097. It improves the one-sided envelope, approximately 0.94608,
but is above the known selected rate 0.45010961003. Hence even these
two exact endpoint sources do not eliminate the remaining outer phase.

### 5.1 A certificate for the global norm barrier

The location of the maximum in (12), and the quoted interval, can be
verified without an unproved plot. Put v=4sin^2(pi u), so 0<=v<=4.
The derivative of H-3J has the sign of log[R/v^(3/2)]. For v<1,
R>=sqrt(|1-z|)=v^(1/4)>v^(3/2), so the derivative is positive.

For v>1 use the quadratic Schur test on L^2-A L+B, with
A=2-z+z^2 and B=1-z. Its roots lie inside radius r precisely when
|B|<r^2 and |r^2 A-B conjugate(A)|<r^3-|B|^2/r. To prove this test,
normalize r=1 and subtract b times the reversed conjugate polynomial
from w^2+a w+b. On the unit circle the subtracted term has modulus
|b| times the original. Rouche's argument reduces the root count to
w[(1-|b|^2)w+a-b conjugate(a)], giving the stated inequality.

Here r=v^(3/2). The first condition is exactly v>1; squaring the
second and using z+z^(-1)=2-v reduces it to P(v)>0, where

    P(v)=v^10-2v^9+6v^8-9v^7+9v^6-6v^5
                         -2v^4+5v^3-4v^2+1.      (12a)

The identities used in this reduction are
|A|^2=4-5v+2v^2 and
conjugate(B)A^2+B conjugate(A)^2=v(v^3-5v^2+9v-4).
The exact Euclidean Sturm sequence for P has sign variations 4 at
v=1 and 3 at v=4, omitting zero terms. It also has variations 4 and
3 at 57/50 and 29/25 respectively. Thus P has exactly one root v_*
in (1,4), with 57/50<v_*<29/25. Since P(1)<0 and P(4)>0, the
derivative changes from positive to negative there. This proves that
u_*=asin(sqrt(v_*)/2)/pi is the UNIQUE global maximizer in (12).
The audit computes the exact Sturm signs and verifies the polynomial
reduction before any numerical integration.

On 0<=u<=u_* the larger-modulus root is L_+ in (7). Indeed equality
of root moduli would force A^2/B real. Its imaginary part can vanish,
away from the endpoints, only if 4c^3-6c^2+5c-1=0, c=cos(2pi u).
For c>=2/5 that polynomial is positive, since its derivative is
12(c-1/2)^2+2 and its value at 2/5 is positive. Here
c>=1-v_*/2>2/5, so no root-modulus crossing occurs before u_*.

For the actual rigorous interval in the audit, isolate v_* to a rational
width below 10^(-35), use interval arithmetic for u_*, and integrate
log|L_+| by 4096 interval RANGE cells on [0,u_*]. Every cell's whole
image is enclosed, so this is a rigorous integral bound without a
quadrature error assumption. The log-sine primitive is evaluated by
J(u)=-Im Li_2(exp(2pi i u))/(2pi), also with complex interval arithmetic.
The resulting enclosure lies strictly between 0.5775 and 0.5780.

## 6. The same two-channel system retains the geometric algebra

The failure of polynomial coefficient growth does not sever the source
from the geometric curve. Before taking absolute values, the coefficient
phase in (1) changes its consecutive ratio to -z L. Complete Newton
evaluation contributes -(1-z)^2/z. Thus the joint complex stationary
equation is

    L(1-z)^2=1.

Eliminating L from this and (4) gives exactly

    -z^2(z^3-4z^2+7z-5)=0.                      (13)

The nonzero cubic has discriminant -23 and is the already identified
five-crossing geometric critical field. Equation (13) is an algebraic
coupling calculation, not a new thimble-selection or cancellation proof.
It makes precise what the wider mechanism must retain: the non-tame
coefficient channel together with the evaluation phase, rather than
separate positive norm maxima.

[Audit](../experiments/audit_actual_multichannel_newton_green.py): generic
finite identities, all-index actual root coefficients, both polynomial
endpoint vectors, exact determinant products, dominated initial branch,
two-sided propagation diagnostics, certified barrier, and cubic elimination.
