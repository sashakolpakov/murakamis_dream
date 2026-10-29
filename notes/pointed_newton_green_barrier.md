# A pointed Newton--Green bound for the full figure-eight Fourier energy

28 October 2026. The actual affine rank-two figure-eight operator has an
exact positive Green presentation in its Newton lattice. Its central
determinant is elementary and its boundary-source response has a uniform
polynomial bound. Keeping the Newton evaluation metric then gives the
sharp upper exponent for the FULL root-color Fourier energy, instead of
the doubled largest-root integral of the earlier homogeneous estimate.

The Green estimate is uniform for a checkable class of fixed-width boundary
sources, with the broader finite-order pointed UL criterion in Section 3.1.
Its application to the figure-eight is an independently proved
known prototype, not a new knot class. No claim that arbitrary knot
A-operators have this Newton form is made.

## 1. The specified ACTUAL affine operator and its Newton lattice

Use the already independently derived operator in
`peripheral_normal_period.md`, Section 9:

    C=c_- T^(-1)+c_0+c_+T, T Y=Q Y T,
    D=Y(Y+1)(Q-Y^2)(QY^2-1),
    g=Q^2Y^2-QY^4+QY^3+QY-Q+Y^2,
    c_-=Y^2(Q-Y)(QY^2-1),
    c_0=-(Y-1)^2(Y+1)g,
    c_+=Y^2(QY-1)(Q-Y^2).

Set Q=exp(2pi i/N), U=Y^N, h=Y+Y^(-1), d=N-1, and

    a_r=Q^r+Q^(-r), s_r=2-a_r=4sin^2(pi r/N),
    t_0=1, t_k=product_(r=1)^k(h-a_r),
    c=t_N=U+U^(-1)-2.                           (1)

The product identity in (1) follows by writing every factor as
(Y-Q^r)(1-Q^rY)/(-Q^rY), or by the monic Chebyshev polynomial.
For generic U, the conjugates Q^jY+Q^(-j)Y^(-1) are distinct: equality
for j!=k would give Y^2=Q^(-j-k), hence U^2=1. Thus the t_0,...,t_d
are a basis of the degree-N field extension C(Y)/C(U).

Put A=D^(-1)C over this GENERIC field. This division is performed
before the complete fiber; D's zeros at special orbit points have
not been replaced by numerical values. The rational telescoping
certificate gives, exactly,

    A t_0=3-h,
    A t_k=-(h-2)(t_k-t_(k-1)), 1<=k<=d.          (2)

Indeed its certificate coefficient is
(Y-1)^2 Q^k/((Y-Q^k)(1-YQ^k))=-(h-2)/(h-a_k).
Multiplying by t_k cancels that last factor, including its whole germ.

Multiplication by h sends t_k to t_(k+1)+a_(k+1)t_k; at the last
column use t_N=c and a_N=2. Therefore A has the following matrix in
the Newton basis, with coincident entries added for small N:

    diagonal:       1+s_(k+1), 0<=k<d; last diagonal 1,
    subdiagonal:   -1,
    superdiagonal: -s_(k+1), row k, column k+1,
    extra corner:  -c in row 0, column d.           (3)

Its coefficients are regular in c. This explicitly defines the free
Newton lattice through c=0, retaining the double-point jets when the
ordinary orbit evaluation basis coalesces. Its generic relation to the
actual operator was proved first; (3) is not a replacement quantization.

## 2. Exact central determinant and the retained source

All row sums of (3) vanish except the first, which is 1-c. Hence

    A(c) 1=(1-c)e_0.                              (4)

The determinant is affine in c. The cofactor of the corner (0,d)
is exactly one: deleting its row and column leaves an upper triangular
matrix with diagonal -1, and the cofactor sign cancels its determinant
sign. At c=1, (4) gives a kernel. Consequently, at EVERY level,

    det A(c)=1-c=3-U-U^(-1),
    det C=Norm(D)*(3-U-U^(-1)).                    (5)

No large-period or classical-curve assumption enters (5). The original
affine source is C F_N=D(3-U-U^(-1)). In this lattice it is exactly
(1-c)e_0, so (4) gives its solution with ALL Newton coefficients one.
This is the already identified original whole state

    F_N(Y)=sum_(k=0)^d t_k(Y).                     (6)

The equality with the original knot cut is the earlier all-level
four-plat source theorem. No value of K_N was used to normalize A,
its source, the determinant, or the Newton basis.

## 3. Uniform Green bound for fixed-width boundary sources

At c=0 write A_0=A(0). It is a killed birth-death matrix: its offdiagonal
entries are nonpositive, its row sums are zero except the killing rate
one at state zero, and every s_r is positive for 1<=r<N. A direct Green
formula proves positivity and the quantitative estimate, so no general
Markov-chain theorem is needed.

Let A_0 v=g. Write w_i=v_i-v_(i-1), 1<=i<=d. Then

    w_i-s_(i+1)w_(i+1)=g_i, 1<=i<d,
    w_d=g_d, v_0-s_1 w_1=g_0.                    (7)

Backward substitution gives the inverse. In particular for g=e_j,

    v_k=product_(r=1)^j s_r
          +sum_(i=1)^min(k,j) product_(r=i+1)^j s_r, j>=1,
    A_0^(-1)e_0=1.                              (8)

Empty products equal one. All entries are nonnegative. If g is supported
on states 0,...,J, where J is fixed independently of N, then s_r<=4 gives

    ||A_0^(-1)g||_2
       <=sqrt(N)(J+1)^(3/2)4^J ||g||_2.          (9)

Thus the source-restricted inverse is polynomially bounded, even though
the inverse on unrestricted bulk sources can be exponentially large.
For general c the exact rank-one formula is

    A(c)^(-1)g=A_0^(-1)g
        +[c/(1-c)]1 [e_d^t A_0^(-1)g].         (10)

Its only central denominator is the explicit 1-c in (5). This is the
boundary matching certificate which a mere half-orbit fold does not
automatically provide. The actual source (1-c)e_0 cancels it as a whole
and remains exactly (6).

### 3.1 A broader pointed UL criterion

The mechanism is not confined to nonnegative coefficients. In fact

    A_0=T_s(I-S),

where S is the nilpotent lower shift and T_s is upper bidiagonal with
diagonal one and superdiagonal -s_(k+1). For a boundary-supported source,
T_s^(-1) never sends its support past that same fixed boundary window;
(I-S)^(-1) then only takes partial sums. Thus (9) remains valid for
complex s_r with |s_r|<=4, without a positivity assertion.

More generally fix integers r>=1 and J>=0. Suppose an ACTUAL pointed
Newton-frame operator is

    L_N=U_N(I-S_N)^r,                              (10a)

where U_N is upper triangular and invertible. In its first J+1 rows
and columns assume |(U_N)_(ij)|<=N^a and |(U_N)_(ii)|>=N^(-a),
for a fixed a>=0. For every original source g supported in 0,...,J,

    ||L_N^(-1)g||_2
      <=binom(N+r-1,r)(J+1)^(J+1)
                            N^(a(2J+1))||g||_2.   (10b)

Proof: the first J+1 coordinate space is invariant under U_N and its
inverse, so inversion uses only that finite block. Write its inverse
as the finite Neumann sum after separating the diagonal. Its norm is
at most (J+1)^(J+1)N^(a(2J+1)). On the other factor,

    (I-S_N)^(-r)=sum_(k=0)^(N-1)binom(r+k-1,k)S_N^k,

whose operator norm is at most binom(N+r-1,r). This proves (10b).
Fixed r,J,a give a polynomial bound even if the unrestricted inverse
of U_N or L_N is exponential.

This is an independently checkable finite-order OPERATOR AND SOURCE
condition, not a condition on the desired value. Any comparison to it
must preserve the actual boundary source and track its evaluation
metric; an exponentially conditioned basis cannot be silently dropped.
An additional fixed-rank central boundary update is governed by its
explicit Schur matrix I-V^t L_N^(-1)U. Formula (10) is precisely the
rank-one instance with Schur factor 1-c. No polynomial inverse of that
Schur matrix is asserted without a separate algebraic certificate.

## 4. The actual root metric gives an endpoint barrier

The Newton lattice is NOT asserted isometric to the original orbit.
Retain its evaluation matrix

    V_(j,k)=t_k(Q^j), 0<=j,k<N.                   (11)

For j=0, t_k(1)=|F_k|^2, F_k=(Q;Q)_k. For 1<=j<N,

    t_k(Q^j)=0 if k>=min(j,N-j),
    |t_k(Q^j)|=|F_(j+k)| /
                   (|1-Q^j| |F_(j-k-1)|) otherwise. (12)

This follows by factoring each term into its two sine factors. The
ordinary indices in the second line stay between zero and N-1, so no
unmarked root wrap or division by F_N occurs.

Let J_0(x)=integral_0^x log(2sin(pi t))dt, 0<=x<=1, and put

    Delta=max J_0-min J_0=2 Lambda(pi/6)/pi.       (13)

The endpoint-uniform factorial estimate, proved by extracting log t and
log(1-t) and applying Stirling to the remainder, is
log|F_k|=N J_0(k/N)+O(log N). Also |1-Q^j|>=2sin(pi/N)>=4/N.
Equations (12) and the logarithmic endpoint modulus of continuity imply

    log max_(j,k)|V_(j,k)|<=N Delta+O(log N).     (14)

At j=0 this uses 2max J_0=Delta; elsewhere it uses the DIFFERENCE of
the two endpoint values J_0((j+k)/N)-J_0((j-k-1)/N), bounded by Delta.
This is an endpoint barrier, not a full-circle integral of the pointwise
largest root.

For ANY polynomially bounded fixed-width source g in (9), its Newton
response r=A_0^(-1)g has polynomial norm. Keeping (11) gives

    ||V r||_2^2<=poly(N) exp(2N Delta).           (15)

The unitary root-color Fourier transform has exactly that same norm.
For the actual source r=1, it is the FULL energy
E_N=|K_N|^2+sum_(j=1)^(N-1)|C_j(q_N)|^2, with its original pointing.
The independent ordinary-color audit bounds the second term by a
polynomial, but (15) already bounds the entire norm directly.

The actual marked regulator calibration gives Vol(4_1)=4Lambda(pi/6).
Thus (15) yields

    limsup (pi/N)log E_N<=2pi Delta=Vol(4_1),     (16)

where the earlier homogeneous largest-root envelope was 2Vol(4_1).
For this particular source the positive sum at j=0 also supplies the
known matching lower rate by a bulk factorial term. This is a prototype
calibration of the Green mechanism, not a new broad-class theorem.

### 4.1 Stress check: the metric estimate is uniform on the whole unit circle

The upper exponent is not an artifact of sampling exactly at root nodes.
Let G(t)=log|2sin(pi t)|, periodically extended, and let J_0 be its
periodic primitive of mean-zero derivative. Uniformly for real u and
0<=k<N,

    sum_(r=1)^k G(u+r/N)
       <=N integral_0^(k/N)G(u+s)ds+O(log N).     (16a)

For completeness, partition the sampled interval into monotonicity pieces
of G. Away from the at most bounded number of mesh cells adjacent to a
zero of sin, the Riemann-sum error telescopes and is O(log N): the retained
cell endpoints are at distance at least 1/N from that zero. In the removed
cells every sampled value is at most log 2; the cell integrals are bounded
below by -(log N+C)/N, including when a zero lies inside the cell. A sample
arbitrarily close to zero can only DECREASE the sum. This proves the
one-sided uniform estimate, with no root-separation assumption on u.

For Y=exp(2pi i u), the two sine factors in t_k give from (16a)

    log|t_k(Y)|
       <=N[J_0(u+k/N)-J_0(u-k/N)]+O(log N)
       <=N Delta+O(log N),                       (16b)

uniformly on the full unit circle, including all zeros by continuity.
Thus the same sharp exponential metric bound applies to the continuous
unit-circle Fourier norm as well as the original root-color norm. It
also permits fixed q-tags in the arguments without changing the rate.
Conversely the complete entry t_k(1)=|F_k|^2 at k/N near 5/6 has rate
Delta. Hence the root evaluation matrix itself satisfies

    lim_(N->infinity) N^(-1)log||V_N||=Delta.       (16c)

All exponential scale in this pointed Green example is therefore carried
by a specified, quantitatively estimated evaluation metric. It is not
hidden by calling the Newton change of basis unitary.

## 5. Checkable class and genuine generalization requirement

The estimate (9) is a uniform source-independent theorem for every
birth-death matrix (3) with 0<=s_r<=4 and every fixed-width boundary
source. The root-metric estimate (15) applies whenever the ACTUAL
operator/source has the Newton representation (1)--(3), or a uniformly
polynomially conditioned comparison preserving its boundary source and
evaluation. Neither hypothesis is an assertion about the unknown scalar.
They can be checked by finite operator identities, as above.

For a general knot, Weyl symmetry alone neither supplies (3) nor controls
a folded boundary determinant. The original ordinary-color bounds fix
the polynomial tail, but do not prove that the pointed normal response
is a tame boundary-source Green vector in a basis with a controlled
geometric evaluation metric. Establishing such a source-exact basis or
an analogous multichannel Green estimate would be a substantive next
step. No new knot, bridge family, or general volume upper bound is claimed.

[Audit](../experiments/audit_pointed_newton_green_barrier.py): actual
generic-orbit conjugacy including all c/D factors, central determinant,
boundary-source Green formulas and bounds, root-evaluation endpoint
products, and exact full-energy Plancherel through the original colors.
