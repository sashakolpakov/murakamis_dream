# The exact factorial interpolant with a moving quantum period

30 October 2026. The existing convergent
Gamma product extends to the ACTUAL moving quantum parameter. It
matches every original finite integer factorial, including the fixed
endpoint d=N-1, before taking derivatives. On specified complex
index charts it has uniform relative bounds and polynomial cost for
every fixed genuine q derivative. The index d stays N-1 when the
analytic period moves; no root reflection is differentiated as though
d were the moving period minus one.

## 1. The same convergent product at a complex period

Fix N>=3, q0=exp(pi i/N), and let

    zeta=q0 exp(epsilon),
    P=pi i/Log zeta=N/[1+N epsilon/(pi i)],
    Q_P=exp(2pi i/P)=zeta^2.                              (1)

The logarithm of zeta is the local one pi i/N+epsilon. Use the
analytic Log P near the positive number N and Log(Pk)=Log P+log k.
Define, initially where all Gamma arguments have positive real part,

    G_P(z)=(2pi/P)^z Gamma(z+1)
       *product_(k>=1) Gamma(Pk+z+1)
                   /[Gamma(Pk-z)(Pk)^(2z+1)],

    Fhat_P(z)=exp[pi i z(z+1)/(2P)-pi i z/2]G_P(z).        (2)

This uses the infinite Gamma product from the
[exact interpolation theorem](exact_factorial_interpolation_and_complex_contours.md),
not its finite Barnes product whose number of factors was an integer.
The log of the kth factor is locally uniformly O(k^-2), with
leading term -z(z+1)(2z+1)/(6P^2 k^2). Its 1/k coefficient
vanishes. The Gamma-ratio expansion therefore proves local uniform
convergence, including P and z derivatives. The function is
holomorphic and nonzero on the initial domain and G_P(0)=1.

The Gamma functional equation and the convergent sine product give
EXACTLY

    G_P(z+1)/G_P(z)=2sin(pi(z+1)/P),
    Fhat_P(z+1)=[1-Q_P^(z+1)]Fhat_P(z), Fhat_P(0)=1.       (3)

They also define its meromorphic continuation in z. Consequently,
with n a fixed nonnegative integer,

    Fhat_P(n)=(zeta^2;zeta^2)_n.                         (4)

In particular (4) holds for EVERY 0<=n<=d=N-1 on a neighborhood
of the original root. This is equality of generic analytic germs,
not merely of their root values. The marked power Q_P^z is always
exp(2z Log zeta).

There is also an exact SECOND difference equation,

    G_P(z+P)=-2sin(pi z)G_P(z),
    Fhat_P(z+P)=[1-exp(2pi i z)]Fhat_P(z).                  (4a)

To prove its constant, first take -1<Re z<0, so both z and z+P
are in the defining Gamma domain. The quotient of the products
truncated at k=K is

    (2pi/P)^P/[Gamma(z+1)Gamma(-z)]
      *Gamma(P(K+1)+z+1)Gamma(PK-z)
        /[P^(2PK)Gamma(K+1)^(2P)].

The last ratio tends to (2pi)^(1-P)P^P by the same uniform
complex-sector Stirling formula, with all powers marked by Log P.
The Gamma reflection identity then gives -2sin(pi z); equivalently
that elementary Gamma identity follows from its convergent product
and the sine product already used in (3). Meromorphic continuation
proves the first equation globally. The exponential in (2) has
P-shift quotient i exp(pi i z), proving the second equation with
the displayed scalar ONE.

The complex-P reflection is consequently exact as well:

    G_P(z)G_P(P-1-z)=P,
    Fhat_P(z)Fhat_P(P-1-z)
       =P exp[pi i z(z-P+1)/P].                            (4b)

Indeed the z derivative of the first logarithm, truncated at K,
telescopes to psi(PK+z+1)-psi(P(K+1)-z), which tends to zero.
Its constant is G_P(P-1). Differentiating (4a) at z=0 gives
G_P'(P)=-2pi. Differentiating (3) at z=P-1 gives
G_P'(P)=-(2pi/P)G_P(P-1), hence the constant is P. The marked
exponentials in (2) then give the second equation of (4b).

## 2. The complex-period asymptotic is uniform

Let K be a compact subset of 0<Re x<1. Uniformly for z=Nx,
x in K, and P in a sufficiently small relative complex disk about
N, put y=z/P. On a slightly smaller disk y stays in a fixed
compact of the same strip. The DIRECT Stirling proof in the
interpolation theorem then gives

    Log G_P(z)=P J(y)+(1/2)Log(2P sin(pi y))
                 +pi cot(pi y)/(12P)+O_K(|P|^-3),           (5)

where J'=Log(2sin(pi y)) has its original mark, continued from
0<y<1. Formula (5) is proved for complex P term by term: the
Gamma arguments z,Pk+z,Pk-z remain in fixed right-half-plane
sectors; the kth Stirling remainder is O_K(|P|^-3 k^-3).
Summing it is uniform. The sine product sums the leading terms
and the cotangent identity sums the 1/P terms just as before.
This argument does not interpolate an identity known only at
integer periods.

The remainder is holomorphic on a larger relative P disk, so its
P derivative at FIXED z is O_K(N^-4) by Cauchy's formula. The
derivative of the leading term is

    partial_P[P J(z/P)]=J(y)-y J'(y).

The two elementary exponential factors in (2) also have bounded
P derivatives on this chart. Thus

    |partial_P Log Fhat_P(z)|<=C_K.                       (6)

Since |P'(epsilon)|=|P|^2/pi=O(N^2), (6) implies

    |partial_epsilon Log Fhat_(P(epsilon))(z)|<=C_K N^2   (7)

for fixed marked z=Nx in this interior chart. The logarithm here
is the relative one at epsilon=0. There is no principal-root or
dilogarithm reset when epsilon varies.

## 3. Fixed integer shifts cover the nonreal exterior rows

Let K be any compact scaled-index set with

    |x|<=M, |Im x|>=delta>0, z=Nx.                       (8)

Choose on each of finitely many smaller charts an integer k_N,
FIXED as epsilon moves, with |k_N|<=C_K N and

    (z+k_N)/N in a compact subset of 0<Re x<1.

Such charts cover K by shifting the real part into the middle
of the strip. For k_N>=0, use the exact formula

    Fhat_P(z)=Fhat_P(z+k_N)
                  /product_(j=1)^(k_N)(1-Q_P^(z+j));        (9)

for k_N<0 use the reciprocal-direction finite product. These
are evaluations of the SAME meromorphic function by (3), not
new independent factorial choices.

For epsilon on the disk used below, all intermediate (z+j)/P
have imaginary part bounded away from zero. Their real and
imaginary parts remain bounded. Therefore each finite sine or
Pochhammer factor in (9) and its inverse is bounded by constants
depending only on K. Its logarithmic epsilon derivative is

    -2(z+j) zeta^[2(z+j)]/[1-zeta^[2(z+j)]]=O_K(N).

There are O_K(N) factors. Combining this with (7) proves the
same O_K(N^2) logarithmic derivative for these exterior rows.
In particular negative rows and rows above N are controlled
when their scaled imaginary parts stay away from zero.
The statement does NOT give a bound across their real integer
zeros or poles. Those are retained by the exact interpolation.

## 4. The fixed endpoint and all physical factorials

For every original fixed integer 0<=n<=d, use (4) itself. On
a sufficiently small disk about epsilon=0,

    partial_epsilon Log Fhat_P(n)
       =sum_(j=1)^n -2j zeta^(2j)/(1-zeta^(2j)).             (10)

At the root |1-q0^(2j)|>=c min(j,N-j)/N. Perturbing epsilon
by at most c/[N^2(1+log N)] keeps every denominator comparable
to its root value. Summing the displayed elementary bounds gives

    |partial_epsilon Log Fhat_P(n)|
                            <=C N^2(1+log N),               (11)

UNIFORMLY in n, including n=d=N-1. No asymptotic estimate at
the endpoint x=1 is being inferred from an interior compact.
The finite index n, and specifically d, is fixed throughout.

At the root one may use the already proved exact identity with
N-1-z for evaluating root values. It is NOT an identity with
that same fixed endpoint after P moves. For example its generic
integer factorial factors have the nonzero logarithmic derivatives
(10). Replacing the fixed d by P-1 during differentiation would
change the source and is not part of this construction.

The second period also supplies an exact normal-transport equation.
Put H_N(z)=partial_epsilon Fhat_(P(epsilon))(z)|_0, with z
FIXED. Since P'(0)=iN^2/pi, differentiating (4a) gives

    H_N(z+N)=[1-exp(2pi i z)]H_N(z)
                         -(iN^2/pi)partial_z Fhat_N(z+N).    (11a)

The undivided identity remains meaningful at the physical zeros.
The last term is essential: the left argument in (4a) moves
with P. Thus actual generic normals do not obey a root-only
N-shift rule obtained by omitting that index derivative.

More generally put Delta=N-P and c(z)=1-exp(2pi i z). There is
the exact local analytic identity

    Fhat_P(z+N)=exp(Delta partial_z)[c(z)Fhat_P(z)].          (11b)

Indeed z+N=(z+Delta)+P, so this is just (4a) at z+Delta.
Modulo epsilon^(J+1), Delta belongs to the ideal (epsilon),
and the exponential in (11b) is the FINITE differential operator

    sum_(j=0)^J Delta^j partial_z^j/j!.

On a chart where c is a unit, divide by the root multiplier and
write

    U=c^-1 exp(Delta partial_z)c
       =exp[Delta(partial_z+c'/c)].

The conjugation identity follows by applying partial_z to c times
a test function. Its logarithmic connection has explicit simple
poles at the integers. On the order-J jet module,
U-I raises the epsilon filtration and therefore
(U-I)^(J+1)=0. Its inverse is the finite geometric series in
-(U-I). This is an actual unipotent transport of finite quantum
jets, with the differential correction (11a) at order one.
The localization excludes the original c-divisors; the statement
does not remove physical support zeros, prove convergence of an
infinite jet expansion, or select a global degree cycle.

The two exact shifts themselves form a flat rank-one difference
connection. With a_P(z)=1-exp[2pi i(z+1)/P], one has
a_P(z+P)=a_P(z) and c(z+1)=c(z), so applying the unit shift
and the P shift in either order gives the same multiplier.
At P=N, their compatibility includes the literal cyclotomic norm

    product_(j=1)^N(1-exp[2pi i(z+j)/N])
                                      =1-exp(2pi i z).

The Gamma product (2) chooses a section of this connection.
These equations alone do not establish global uniqueness of a
section: a factor periodic under both shifts preserves them.
Nor do they determine the original source period or its cycle.

## 5. Uniform relative disks and genuine normal bounds

Consider a fixed finite list of factorial arguments, each either

* a fixed original integer between 0 and N-1;
* z=Nx in a fixed compact of the interior strip; or
* z=Nx in a fixed compact satisfying (8), continued by (9).

All indices are held fixed when the generic parameter varies.
Affine O(1) offsets are allowed by enlarging the compacts slightly.
For sufficiently small c_K>0, on

    |epsilon|<=rho_N=c_K/[N^2(1+log N)]                     (12)

every listed factorial is nonzero and holomorphic, and

    C_K^-1 <= |Fhat_(P(epsilon))(z)/Fhat_N(z)| <= C_K.       (13)

The same holds for any fixed finite product or quotient of the
listed factors. Equations (7),(9),(11), integrated along the
epsilon segment, prove (13), with a consistent relative logarithm.
Cauchy's formula on (12) proves for every fixed j

    |partial_epsilon^j Fhat_(P(epsilon))(z)|_0
       <=C_(K,j)[N^2(1+log N)]^j |Fhat_N(z)|.               (14)

Inverse factorials have the corresponding relative bound. In
particular the entire assertion holds on the smaller actual
normal disk |epsilon|<=c N^-10, at cost at most C_(K,j)N^(10j).

The marked factors exp(pi i z), zeta^[z(L-z-1)] and the original
physical cup scalar N zeta^(-d^2) cause no further difficulty:
L and all indices are O(N), so the epsilon derivative of their
logarithms is O_K(N^2), and higher derivatives follow on (12).
Thus the original continued cups and inverse cups formed from
these factors also satisfy (13),(14). No unit phase is discarded.

One can specify the formerly ambiguous off-grid symmetric gauge
as well. For a fixed integer L<N, set

    b_L(epsilon,z)=zeta^[z(L-z)]
                   Fhat_P(z)Fhat_P(L-z)/Fhat_P(L),
    g_L(epsilon,z)=[b_L(epsilon,z)/b_L(0,z)]^(1/2).           (15)

Use the analytic square root equal to 1 at epsilon=0. Whenever
the two index arguments satisfy the preceding hypotheses, (13)
on a smaller disk makes this a specified holomorphic unit with
the same relative jet bounds. It is symmetric under z->L-z and
agrees with the original physical gauge at every admissible
integer index. Its continuation is now fixed by (2), rather than
inferred from bounded values on a finite integer set.

At epsilon=0 the displayed phases cancel exactly, giving
b_L(0,z)=G_N(z)G_N(L-z)/G_N(L). The already proved FIXED-root
reflection therefore gives b_d(0,z)=1 meromorphically, also at
noninteger z. This is useful for evaluating the root cup. It
does not say that b_d(epsilon,z) is constant when P moves.
In fact (4b) gives the exact fixed-endpoint correction

    b_d(epsilon,z)=P/Fhat_P(d)
       *exp[pi i z(N-P)/P]
       *Fhat_P(d-z)/Fhat_P(P-1-z).                          (16)

The final quotient retains the difference between the original
fixed d=N-1 and the moving endpoint P-1. Formula (16), or its
derivative, may be used for boundary transport; replacing that
quotient by one away from the root changes the genuine normal.

## 6. Application scope at the slightly nonreal geometric degree

For the actual channel cup, the needed arguments are r=a-h and
2a-r, while the physical cups use v,d-v,l,d-l. In the joint
deficient geometric corridor take a small but fixed NONZERO
imaginary part of the degree. Then r/N and (2a-r)/N lie in
nonreal exterior compacts, with opposite imaginary signs; the
physical cup arguments have real parts strictly inside (0,1).
The remaining factorials F_a,F_m,F_(2a),F_d have fixed integer
indices below N. The lemma therefore controls all these explicit
boundary factors and their genuine generic derivatives together.

It does not justify crossing their real degree poles, deform the
original support cycle, or prove a nonzero geometric contribution.
Source assembly must still use the actual large-partner white
columns and all original tensor marks. The present result is the
moving-period analytic input for that assembly, not a replacement
for its finite tensor identity or its global period argument.

## 7. Finite checks and scope

The [focused audit](../experiments/audit_actual_moving_period_factorial_normals.py)
and its [results](../experiments/actual_moving_period_factorial_normals_results.json)
check the actual generic integer factorials, independent Gamma/Barnes
evaluations, relative disks, fixed-endpoint derivatives, exterior
gauges, second-period and complex-period reflection identities,
and fixed-N first and second normal transport. Its largest relative
identity error at 85 digits was below 5.3e-82. These finite checks
support, and do not replace, the proofs above.

The moving-period theorem does not transport degree globally across retained divisors or identify a contributing quantum cycle.