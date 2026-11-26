# Actual half-block coefficient entropy is not convex in the terminal row

Private proof, 31 October 2026. This rules out the proposed fixed-outer-degree
endpoint-convexity shortcut. It does not disprove a shared forest bound,
nor rule out an exchange that changes other degrees in a controlled way.

Use the ACTUAL even-level half block N=2m,M=m-1. For 0<=i<=j<=M,
the coefficient of b^i c^(N-1-j) in P_left is the homogeneous degree
r=j-i polynomial

    (4/a_i) Q_(i,j)(x,y),
    a_j=4cos^2((j+1/2)pi/N), s_j=2sin(jpi/N),
    Q_(i,i)=1,
    Q_(i,i+1)=[s_(i+1)^2/a_(i+1)](x+y),
    Q_(i,j)=[s_j^2/a_j](x+y)Q_(i,j-1)
              +[s_js_(j-1)/a_j]xyQ_(i,j-2).             (1)

These are the original source factors. No level-m substitution is made.
On compact subsets of 0<mu<nu<1/2, a_i and its inverse are bounded, so
4/a_i contributes zero exponential rate. The actual coefficient tested
below is precisely

    [x^k b^i c^(N-1-j)y^(j-i-k)]P_left.

Take any even levels N->infinity and integer sequences with
i/N->mu, j/N->nu, k/N->xi, where
0<mu<nu<1/2 and 0<xi<nu-mu. All assertions are locally uniform on
compact subsets of these strict inequalities, and integer rounding
changes no displayed exponential rate.

## 1. The coefficient limit, not merely a weighted limit

Put a'_j=s_j^2/a_j and normalize (1) by product_(v=i+1)^j a'_v.
The resulting monic polynomial p_r(x,y) satisfies

    p_0=1,p_1=x+y,
    p_r=(x+y)p_(r-1)+gamma_r xy p_(r-2),
    gamma_r=a_(i+r-1)/(s_(i+r)s_(i+r-1))>0.             (2)

Substitute x/y=-z^2 and divide by z^r. The recurrence becomes a
Jacobi recurrence in t=z^(-1)-z:

    q_r(t)=t q_(r-1)(t)-gamma_r q_(r-2)(t).

Its r roots are real and simple because its symmetric tridiagonal
matrix has positive off-diagonal entries sqrt(gamma_r). The map
z>0 ->z^(-1)-z maps onto the real line. Hence p_r(x,1) has r
negative real roots. On any stated compact source interval, gamma_r
has fixed positive upper/lower bounds. The Jacobi norm bound therefore
places all roots of p_r in a fixed compact negative interval away from
zero and infinity. The polynomial is also reciprocal, by (2).

Thus after any bounded real tilt x=exp(l),y=1, its normalized
coefficient distribution is a sum of r independent Bernoulli variables,
whose probabilities are uniformly bounded away from0 and1. For a
target k/r in a compact subset of(0,1), the unique tilt giving mean k
stays bounded. The probability of the exact mean is between positive
constants times r^(-1/2). This last assertion follows directly by
Fourier inversion: the centered characteristic function has Gaussian
expansion on |theta|<=r^(-2/5), variance comparable to r, and modulus
at most exp[-c r sin^2(theta/2)] elsewhere. Uniform third moments make
the expansion relative1+o(1). In particular its logarithm is O(log N).

The already proved original continuant Riemann limit is

    Phi(mu,nu,l)=integral_mu^nu log L(t;e^l,1)dt,
    L(t;x,y)^2-(x+y)tan^2(pi t)L(t;x,y)-xy tan^2(pi t)=0,
    L>0.                                               (3)

Combining that limit with the exact Bernoulli coefficient identity
gives the actual source coefficient entropy

    E(mu,nu,xi)=inf_(l real)[Phi(mu,nu,l)-xi l].          (4)

For clarity, convergence of the exact tilts follows without assuming
derivative convergence: the normalized log polynomials are convex and
converge locally uniformly to the differentiable strictly convex Phi;
their derivatives then converge on compact intervals by the two
secant inequalities. The unique limiting tilt satisfies Phi_l=xi.
The root bounds and the Bernoulli variance give Phi_ll>0. This also
proves the locally uniform coefficient limit and smoothness of E.

## 2. An exact negative curvature at fixed outer degree

Write tau=tan(pi t). The positive root in (3) has the exact expression

    log L(t;e^l,1)
       =l/2+log tau+asinh(tau cosh(l/2)).               (5)

At l=0 its first l derivative is1/2 and its second is sin(pi t)/4.
Therefore at the balanced target xi=(nu-mu)/2 the minimizing tilt is
l=0, and

    Phi_(nu,l)=1/2,
    Phi_(l,l)=[cos(pi mu)-cos(pi nu)]/(4pi),
    Phi_(nu,nu)=pi cos(pi nu)/[sin(pi nu)(1-sin(pi nu))].

Now hold mu and xi FIXED while varying nu near this balanced point.
The actual Legendre Hessian is the Schur complement

    E_(nu,nu)=Phi_(nu,nu)-Phi_(nu,l)^2/Phi_(l,l)
      =pi cos(pi nu)/[sin(pi nu)(1-sin(pi nu))]
                      -pi/[cos(pi mu)-cos(pi nu)].      (6)

At nu=1/4, the first term is pi/(1-1/sqrt2). For EVERY
0<mu<1/4, cos(pi mu)<1, so the second term is strictly larger.
In particular mu=1/8,nu=1/4,xi=1/16 is a regular strictly interior
source point at which E_(nu,nu)<0. Levels divisible by16 realize
these base degrees exactly; the uniform statement above covers nearby
integer roundings and both even congruence classes generally.

In particular choose a sufficiently small fixed rational epsilon>0.
For large even levels realizing i=N/8,k=N/16 and
j_0=N/4,j_+=N(1/4+epsilon),j_-=N(1/4-epsilon), the actual
coefficients A_N(j) in (1) satisfy

    log A_N(j_0)-[log A_N(j_-)+log A_N(j_+)]/2 >= c_epsilon N>0.

Thus even a finite coefficientwise log-convex exchange in this exact
direction fails exponentially. The polynomial factor4/a_i is the same
in these three coefficients and does not alter the comparison.

This is an exact obstruction to asserting convexity in nu AFTER fixing
the outer degree xi. The weighted-rate convexity at fixed positive
x/y is valid but does not survive this coefficient constraint. It
therefore cannot by itself justify pushing all source row variables
to endpoints by total unimodularity. It remains possible that a
different joint exchange preserving the ORIGINAL face constraints,
or a stratified Green/representation argument, proves the forest bound.

There is also a genuinely different direction: holding the outer
PROPORTION xi/(nu-mu) fixed changes xi when nu changes. Equation(6)
does not address convexity in that direction. Using such a direction
globally would require checking its changes at both outer faces, not
only the middle-edge incidence matrix.
