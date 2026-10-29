# A selected actual gauge period evaluates fixed observables at the algebraic point 2

27 October 2026. An actual source period now gives a direct local
instance of the proposed quantum-period-to-algebraic-point mechanism.
For the canonical primitive gauge g_N, its top-coefficient period,
normalized by its EXPLICIT Gauss period, converges on every fixed
polynomial observable to evaluation at z=2. Its universal moment
recursion and finite cyclic source are exact. This is a proved
selection statement for this local gauge period, rather than only
the construction of a formal critical branch.

The observable degree must be independent of N. The transformed
full knot word does not satisfy that restriction automatically.
This does not identify the knot's quantum A-module or prove a new
knot-volume limit. It supplies one fully sourced local comparison
which a whole-word construction may try to extend.

## 1. The actual period and its known normalization

Let Q=exp(2pi*i/N), N>=2, and let

    g_N(z)=sum_(r=0)^(N-1)c_r z^r

be the CANONICAL nilpotent polynomial of the primitive source gauge
v_N(z)v_N(Qz), as in
[the actual gauge theorem](actual_hilbert90_gauge_dilogarithm_action.md).
For a polynomial P define the actual linear period

    I_N(P)=[z^(N-1)] P(z)g_N(z),
    c_N=I_N(1)=c_(N-1).                            (1)

The [exact resonant calculation](actual_primitive_gauge_resonant_endpoint.md)
proves, including all endpoint terms,

    c_N=(1/N)sum_(r=0)^(N-1)(-1)^rQ^(r(r-1)/2)
        =omega_N/sqrt(N)+O(1/N),
    omega_N=exp[-pi*i*(N+1)/4-pi*i/(4N)].          (2)

Thus c_N is nonzero for all sufficiently large N and its modulus
is polynomially bounded above and below. Normalizing by c_N uses
this evaluated universal Gauss period. It does NOT divide by the
unknown knot invariant or choose its exponential normalization.

This is a sourced period of the same actual coefficient algebra.
For example it is realized by the original two-leg Euler cap with
its explicit insertion b=J_Q(z)^-1 P(z)g_N(z), apart from the
already specified cap scalar and the conversion f=z/x. No new
invariant is defined by (1).

## 2. An exact period Ward identity and a two-generator module

The UNREDUCED polynomial identity is

    (1-z)(1-Qz)g_N(Qz)-g_N(z)
                       =-(2/N)z^N+c_N z^(N+1).   (3)

Multiplying by any polynomial P and extracting degree N-1 kills
the right side. Rescaling the coefficient variable therefore gives
the exact source identity

    I_N[Q^-1 P(Q^-1z)(1-Q^-1z)(1-z)-P(z)]=0.    (4)

Put i_m=I_N(z^m), using the UNWRAPPED nonnegative degree m.
Then (4) is the N-independent recursion

    i_(m+2)=(1+Q)i_(m+1)+(Q^(m+2)-Q)i_m,
    i_0=c_N, i_1=(1+Q)c_N-2Q/N.                (5)

The second initial value follows from the degree-N relation in
(3). Degrees m>=N give i_m=0, consistently with (5); no cyclic
identification of that degree has been made.

Define universal integer polynomials H_m(Q),R_m(Q) by

    H_0=1, H_1=1+Q, R_0=0, R_1=-2Q,
    F_(m+2)=(1+Q)F_(m+1)+(Q^(m+2)-Q)F_m         (6)

for either F=H or F=R. Induction in the exact recurrence gives

    I_N(z^m)=H_m(Q)c_N+R_m(Q)/N                 (7)

for EVERY m>=0. Thus every fixed polynomial period is an explicit
linear combination of TWO known source periods, c_N and 1/N.
The coefficients in (6) are independent of level. This is stronger
than a purely formal large-N moment calculation.

An independent coefficient proof can be useful. For 0<=m<N,
the root factorial reflection gives

    c_(N-1-m)=(1/N)sum_(r=0)^(N-1-m)
               (-1)^r Q^(r(r-1)/2)(Q^(r+1);Q)_m.

Expanding its finite product and using
t_r Q^(sr)=(-1)^s Q^(-s(s-1)/2)t_(r+s) gives

    H_m(Q)=sum_(s=0)^m Q^s {m choose s}_Q,
    |I_N(z^m)-H_m(Q)c_N|<=m 2^m/N.             (8)

For the last estimate compare each shifted Gauss interval with the
full interval: at most m terms are missing, all of modulus one.
The Gaussian binomial has nonnegative integer polynomial
coefficients with total binomial(m,s), so its modulus on |Q|=1
is at most that number. Equations (5)-(8) agree exactly.

## 3. The selected leading symbol is evaluation at 2

At Q=1 the universal coefficients obey

    H_m(1)=2^m,
    R_0(1)=0, R_m(1)=-2^m for m>=1.            (9)

For a FIXED polynomial P, with coefficients independent of N,
(7)-(9) and Q_N=1+O(1/N) therefore imply

    I_N(P)=P(2)c_N+[P(0)-P(2)]/N+O_P(N^(-3/2)), (10)
    I_N(P)/I_N(1)=P(2)+O_P(N^(-1/2)).           (11)

The constants may depend on that fixed polynomial. In particular
P(2)!=0 proves nonvanishing for all sufficiently large N. If
P(2)=0 and P(0)!=0, the boundary period 1/N is instead leading.
If both vanish, (10) only gives the indicated smaller-order
bound; it is not a nonvanishing claim.

The classical limit of the actual Ward relation (4) is

    ((1-z)^2-1)P(z)=z(z-2)P(z).

Its two algebraic support points are 0 and 2. The ACTUAL Gauss
normalization and moments select the point 2. Consequently the
map in (11) is asymptotically multiplicative on every fixed
polynomial window: both P and PR are evaluated at 2. No regular
map from the nilpotent finite algebra to that point is asserted.

This is a genuinely nonlocal period selection: the coefficient
degree increases with N. Directly specializing the finite
nilpotent generator to the scalar 2 would be invalid. The
period calculation supplies the comparison instead.

The exact rational endpoint observable (1-z)^-1, interpreted by
its Taylor expansion at zero before coefficient extraction,
also fits this picture in this particular case:

    I_N((1-z)^-1)=g_N(1)=2/N-c_N.

Its leading value is -1=1/(1-2). This assertion follows from
the separately proved exact endpoint identity, not from extending
(11) to every rational function without a new estimate.

## 4. The leading period also intertwines ordered gauge meridian steps

Let q=exp(pi*i/N), Q=q^2. For any FIXED integer r use the actual
primitive gauge increment

    D_r(z)=g_N(q^r z)/g_N(z) in z^N=0.            (12)

All quotients are units in that algebra, with canonical normal
forms. Positive r gives the ordered product of the actual
M->qM gauge increments; negative r uses their genuine inverses.
The [whole-word gauge theorem](whole_word_primitive_source_gauge.md)
proves the r=1 increment before any endpoint evaluation. Exactly,

    I_N(P D_r)=q^(r(N-1)) I_N(P(q^-r z)).       (13)

Indeed D_r g_N=g_N(q^r z) modulo z^N; multiplying by a
polynomial P and extracting degree N-1 gives (13) by rescaling
the variable. The source phase q^(r(N-1))=(-1)^r q^-r is
retained. It cannot be replaced by one before evaluation.
Combining (11) with (13) gives the sourced meridian relation

    I_N(P D_r)/c_N -> (-1)^r P(2).             (14)

This extends to every fixed finite Ore observable

    Ahat=sum_r P_r(q,z) T^r, Tz=qzT,
    T(g_N)(z)=g_N(qz),

where the r range and polynomial degrees in z are independent
of N, and the coefficient functions are regular at q=1. Define
its actual period by I_N[(Ahat g_N)/g_N]. Then

    I_N[(Ahat g_N)/g_N]/c_N
                      -> sum_r (-1)^r P_r(1,2).  (15)

The limit is a character of the commutative symbol algebra at
(z,T)=(2,-1). Products of any two such fixed observables stay
in the same class, and the Ore coefficient shifts q^r z tend
to z, so the leading evaluation is multiplicative as well.
This is an actual local period/connection comparison, not only
moment evaluation. The meridian steps here are the GAUGE PART
of the knot's transport. Fusion, actual word coefficients and
the full peripheral line remain separate data.

The gauge wave equation itself has the fixed operator

    [(1-z)(1-Qz)T^2-1]g_N=0 modulo z^N,

whose unreduced source is (3). Its classical symbol is
(1-z)^2 T^2-1; the selected character (2,-1) lies on it.
It is not the knot's quantum A-polynomial.

## 5. The moment recursion has a retained cyclic source

For reference set X_m=Q^m and let E raise m. Then EX=QXE,
and (5) is the actual local source recursion

    P_cap=E^2-(1+Q)E+Q(1-QX).                    (16)

Its ordinary commutative symbol is (E-1)^2-X. At X=1 the two
roots are 0 and 2; the selected branch in (11) is the unit root 2.
This is a recursion of the universal cap-gauge moments. The index
m is observable degree, NOT the knot's meridian color, and
P_cap is not identified with its quantum A-polynomial.

Folding i_0,...,i_(N-1) into a cyclic array changes (16). The
exact cyclic residual is

    (P_cap i)_m=c_N delta_(m,N-2)
                         -(2Q/N)delta_(m,N-1).    (17)

For m<N-2 use (5). At m=N-2 the wrapped i_N contributes c_N
in place of zero. At m=N-1 the wrapped i_(N+1) and i_N give
i_1-(1+Q)i_0=-2Q/N. This proves (17), also at N=2.
The finite cyclic source cannot be erased by calling (12) an
unpointed homogeneous spectral equation. The Gauss period and
its smaller boundary term are its specified source data.

## 6. Its root norm curve is exactly its classical curve, with the source retained

The moment recursion in (16) has companion matrix

    C(X)=[[0,1],[-Q(1-QX),1+Q]],
    V_(m+1)=C(Q^m X)V_m.

Let H_N(X)=C(Q^(N-1)X)...C(X) be its forward cyclic monodromy.
Its characteristic polynomial is EXACTLY

    det(v-H_N)=(v-1)^2-U, U=X^N,                 (18)

at every level. This is the same polynomial as the classical
symbol of (16), after identifying its central variables with
the classical variables. No conjectural norm-curve equality
is used to obtain it.

Here is a direct proof. The determinant is the full product

    det H_N=product_(j=0)^(N-1)Q(1-Q^(j+1)X)
           =1-X^N.

The trace is invariant under X->QX by cyclic conjugacy wherever
C(X) is invertible, hence as a polynomial identity. In a closed
walk contributing to the trace, each occurrence of the X-dependent
lower-left edge must be paired with an upper-right edge. Thus
the trace has degree at most floor(N/2)<N. A Q-invariant
polynomial of that degree is constant. At X=0 the companion
has eigenvalues 1,Q, so its Nth power has trace 2. This gives
(18), including composite levels and all determinant zeros.

The selected finite source still matters. At X=1 its nonzero
initial vector is

    V_0=(c_N,(1+Q)c_N-2Q/N)^t.

The exact unwrapped moments give V_N=(i_N,i_(N+1))=0, so

    H_N(1)V_0=0.                                 (19)

It is in the central v=0 kernel, while the leading fixed-degree
period in (11) selects the classical point z=2. The two facts
refer to different selections: finite cyclic monodromy of the
sourced state and the leading local observable period. They
cannot be identified merely because the two defining curves
in (18) agree. The singular orbit and the source in (17)
must be retained. In particular the generic invertible norm-torsor
description alone does not extend through this v=0 fiber.

This is an explicit, fully evaluated local example of both
norm-curve compatibility AND its limitations for selected periods.
It is not an assertion of either compatibility or a particular
central character for the knot's own quantum A-module.

## 7. The selected action and prefactor have a marked dilogarithm calibration

The exact Gauss proof identifies the period, its phase and its
nonzero prefactor. There is a compatible classical critical-action
calibration. For coefficient extraction I_N(1) the relevant action
in the logarithmic coordinate x=Log z is

    S(z)=2Li_2(z)-2pi*i Log z.

Continue from the unit disk to 2 through the upper half-plane.
Then Log(1-2)=-pi*i, and the elementary dilogarithm reflection
identity gives

    Li_2(2+i0)=pi^2/4+pi*i log 2,
    S(2)=pi^2/2, D_z S(2)=0, D_z^2 S(2)=-4.     (20)

Here D_z=z partial_z. The phase exp[S(2)/h], h=2pi*i/N,
is exactly exp[-pi*i*N/4], the leading phase of c_N in (2).
The measure also matters: [z^(N-1)] is the Cauchy measure
dz/z^N, so choosing the above action leaves amplitude z dx,
with value 2 at the saddle. A quadratic Fresnel calculation
with that amplitude and Hessian -4 gives

    exp[-pi*i*N/4] exp[-pi*i/4]/sqrt(N),

again the actual leading Gauss prefactor. Omitting the amplitude
z would lose a factor two.

This is an independently matched action/density calibration.
The Gauss argument proves selection and the asymptotic directly;
no unproved deformation of an analytic dilogarithm contour beyond
the established small-disk chart is used as its proof. At this
real shape 2 the Bloch--Wigner value is zero: its Li_2 imaginary
part cancels Log|2| Arg(1-2). Thus this local source comparison
has zero volume rate and does not introduce a knot's hyperbolic
volume by interpreting a gauge-chart value as that volume.

## 8. Scope for the general torsor program

This proves the requested kind of algebraic leading-period
mechanism in a real local part of the original source: a quantum
Ward module, a selected period, an algebraic critical point and
a nonvanishing criterion P(2)!=0, with known polynomially sized
normalization and all cyclic source terms retained.

It does not prove that the FULL transformed word, whose degree
and number of entries grow with N, has such a fixed presentation.
It does not intertwine the knot's meridian insertion with this
degree recursion. It does not identify the point 2 with a geometric
knot holonomy or assign it a positive hyperbolic volume. The
leading hyperbolic action and global sector cancellation remain
the original open problem.

Nor may (11) be naively extended to Laurent observables: the
formal coefficient of z^-1 g_N at degree N-1 is zero, rather
than (1/2)c_N. Rational localization needs a sourced period
construction; it is not inversion of a nilpotent finite matrix.

Even rational expressions regular at 2 need their actual source
lattice. For example (3) gives EXACTLY

    I_N(J_Q)=Q^-1 c_N,
    I_N((1-z)^-2)=c_N+(1-Q)g_N(Q).

The second identity follows by differentiating (3) at z=1 and
using I_N((1-z)^-2)=N g_N(1)-g_N'(1). These rational functions
have the same classical expression (1-z)^-2 but different
quantum pole arrangements. The displayed additional endpoint
term is not controlled by the fixed-polynomial theorem. Its
vanishing or size cannot be assumed from pointwise convergence
of the two rational expressions away from their poles.

[The audit](../experiments/audit_actual_gauge_critical_evaluation.py)
and [saved results](../experiments/actual_gauge_critical_evaluation_results.json)
check the exact moment, two-period and cyclic-source equations
at finite-field roots. High-precision fixed-degree samples
diagnose the proved algebraic evaluation limit. A separate
agent independently verified the reflection/q-binomial moment
proof and its error estimate before this note was written.
