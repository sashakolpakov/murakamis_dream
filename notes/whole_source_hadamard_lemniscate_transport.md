# A controlled one-variable lemniscate for the whole original source

28 October 2026. The full original knot scalar, with ALL clocks and outer
phases retained, has a one-variable coefficient presentation whose selected
lemniscate has polynomial logarithmic mass. This bypasses the unproved
arbitrary-anchor interior-flow mass estimate for this particular whole-source
presentation. It does not prove a sharp geometric bound for the selected
lemniscate level. Taking the largest modulus of all critical values is
unnecessary and can be substantially worse.

No coefficient below is defined by the unknown value K_N. The input is the
whole original meridian cut polynomial computed from the finite R, followed
by explicit monic polynomial operations. It may be expensive, but is a
specified source construction rather than a favorable replacement invariant.

## 1. Exact full-source Hadamard master

Fix a zero-framed one-component knot diagram, or a fixed braid presenting it.
Use its original reduced reciprocal meridian polynomial F_N(Y), at
Q=exp(2pi i/N), with

    F_N(1)=K_N, F_N(Q^j)=C_j(q_N), C_1=1.

The actual finite-cut and Weyl theorems give F_N in C[Y,Y^-1], reciprocal
under Y inversion. Put h=Y+Y^-1 and expand by MONIC Newton division,

    F_N(Y)=sum_(n=0)^D a_(N,n) T_n(Y),
    T_n(Y)=product_(r=1)^n(h-Q^r-Q^-r).             (1)

Repeated nodes cause no division here: the T_n are monic polynomials in h.
The whole original polynomial is the input; one does not reconstruct a
missing coefficient from K_N. All original scalar and framing factors remain
those of that input.

At the root, T_N=Y^N+Y^-N-2 and T_(n+N)=T_N T_n. Consequently terms
n>=N vanish at EVERY root-color point Y=Q^j. With d=N-1 set

    A_N(z)=sum_(n=0)^d a_(N,n) z^n,
    w_n=T_n(1)=|(Q;Q)_n|^2,
    W_N(z)=sum_(n=0)^d w_n z^(d-n),
    f_N(z)=A_N(z)W_N(z)/z^d.                      (2)

Then the exact original scalar is

    K_N=CT_z f_N(z)=(2pi i)^(-1)integral f_N(z)dz/z. (3)

This retains every coefficient phase; it is not the absolute Newton
envelope. The truncation also retains all original root-color values,
so their audited Plancherel identity remains applicable.

The first Newton node is Q+Q^-1. Thus a_(N,0)=F_N(Q)=1. Also
w_0=1 and w_d=N^2. If m=degree A_N, the polynomial P_N=A_N W_N has

    P_N(0)=N^2, degree P_N=d+m, leading coefficient a_(N,m). (4)

If m=0, A_N=1 and (3) is exactly K_N=1. This one-pole case is treated
separately; no proper-two-pole assertion is made for the unknot case.
Otherwise f_N has genuine poles of orders d and m at zero and infinity.

## 2. Arithmetic size bounds come from the original finite word

For a fixed original diagram there are constants C,L such that:

* the Laurent degree of F_N is at most C N;
* its coefficients, and all their cyclotomic conjugates, have modulus
  at most exp(C N), after a harmless fixed power of N is absorbed in C;
* multiplying every coefficient by N^L makes it integral in the cyclotomic
  integer ring of the retained root field, of degree at most 4N.

Here is a direct justification. Each finite R term has a bounded number
of root factorial denominators, each with index below N, times a product
of at most N binomials in the meridian. The complement identity
F_a F_(d-a)=N times a unit root clears each inverse factorial with ONE
factor N, not N factors. Every conjugate root product has modulus at
most 2^N; each binomial expansion has coefficient sum at most 2^N.
The fixed diagram uses a fixed number of such factors and only a
polynomial number of state paths in N. Pivot exponents and the retained
zero-framing normalization have meridian degree O(N). The common
quadratic Cartan cancels against its prescribed zero-framing factor,
leaving the explicit meridian monomial, not an uncontrolled analytic
scalar. Thus the asserted degree, denominator and conjugate bounds follow
from the finite defining matrices. In the Gaussian-polynomial cut formula
the denominators can in fact be cleared integrally; the weaker N^L statement
suffices here.

Passing from reciprocal Laurent polynomials to h-polynomials uses the
integer recurrence Y^r+Y^-r=C_r(h), C_(r+1)=hC_r-C_(r-1). Its coefficient
norm is exponential in r. Monic Newton conversion introduces only the
complete homogeneous polynomials in the nodes Q^r+Q^-r. In every conjugate
their modulus is at most two, and

    |h_(j-n)(a_1,...,a_(n+1))|
                              <=binom(j,n)2^(j-n).

Consequently every coefficient of A_N and P_N still has all conjugates
bounded by exp(C' N), with the same fixed N-denominator budget. This
includes confluent nodes. No small Vandermonde divisor occurs.

If a_(N,m)!=0, apply the field norm to the nonzero integral element
N^L a_(N,m). Its norm is a nonzero integer. Bounding all other conjugates
above gives

    |a_(N,m)|>=exp(-C'' N^2).                     (5)

Constants depend on the fixed original diagram, not its invariant value.

## 3. The source selects a pole-separating level, not every critical value

For m>=1 view f=f_N as a rational function on the sphere. For any R>0,
every connected component of {|f|>R}, with poles included, contains a pole.
Otherwise its closure avoids both poles and is compact; the maximum
principle for f would contradict |f|>R inside and |f|=R on its boundary.
There are therefore at most TWO such components.

For sufficiently large R they are disjoint neighborhoods of zero and
infinity. For sufficiently small R the superlevel is the sphere with
small disjoint zero neighborhoods removed, so the two poles are in the
same component. Define R_sep to be their merger threshold:

    R_sep=inf{R>0: the superlevel components of 0 and infinity are distinct}. (6)

Separation persists as R increases. Thus for every regular level R>R_sep
the zero component is bounded in the plane. It has a unique OUTER boundary
circle Gamma_R lying in |f|=R and winding once around zero. Any additional
boundary circles surround holes without zero and have winding zero.
Their periods of f dz/z vanish individually. Hence Gamma_R ALONE, with
multiplicity one and the original positive orientation, represents (3).

There is no integer boundary-matrix inversion or accumulated cell
multiplicity in this construction. Connectivity can change only at a
nonzero critical level, since between regular levels the compact level
annulus admits the ordinary gradient trivialization. Thus R_sep is the
modulus of a regular critical value of f. It can be smaller than the
largest critical modulus; inaccessible criticals are not included merely
because they are algebraic roots of f'.

The definition (6) is a marked algebraic connectivity condition independent
of K_N. It is equivalent to the least level supporting a pole-separating
closed curve, but (6) specifies it using the actual two pole components.

## 4. The selected circle has polynomial logarithmic length

Let Dp=degree P_N<=2N-2. Every radial ray meets the real algebraic curve

    |P_N(z)|^2-R^2|z|^(2d)=0

at most 2Dp times. Every fixed-radius circle also meets it at most 2Dp
times: the highest angular harmonic has the nonzero product of the
leading coefficient of P_N and its constant N^2, so it cannot vanish
identically on such a circle. One-dimensional coarea gives

    integral_(Gamma_R)|dz/z|
              <=4pi Dp+2Dp log(r_max/r_min).     (7)

The radii have a uniform quantitative bound. The critical equation is
zP_N'-dP_N=0; its leading coefficient is m a_(N,m) and its constant
is -dN^2. The coefficient bounds and (5), followed by the elementary
Cauchy polynomial root bound and its reversed-polynomial version, put
all its roots between exp(-C N^2) and exp(C N^2). It follows that the
largest regular critical modulus is at most exp(C N^3).

For |w|=R, every point of the level is a root of
P_N(z)-w z^d. Because m>=1, its leading coefficient remains a_(N,m),
and its constant remains N^2, independent of w. For
R_sep<R<=R_sep+1, the same root bounds therefore give

    |log|z||<=C N^3.                              (8)

This estimate is uniform as R decreases to R_sep; no inverse critical
value separation or inverse R-R_sep is used. Equations (7)--(8) prove

    (2pi)^(-1)integral_(Gamma_R)|dz/z|<=C N^4.     (9)

The circles are explicit components of degree-O(N) algebraic curves,
with coefficient one. Thus this is controlled ORIGINAL-source transport,
not merely a conditional estimate for a prospective chain.

## 5. Whole-source estimate and its exact remaining scope

Define R_src=R_sep when m>=1 and R_src=1 in the one-pole case m=0.
Integrate (3) on Gamma_R, use (9), and take regular R down to R_sep.
There is a constant C depending only on the fixed original diagram with

    |K_N|<=C N^4 R_src.                           (10)

The audited ordinary-color theorem and exact root-color Plancherel identity
then give a corresponding positive whole-energy bound

    E_N=|K_N|^2+poly(N)
                       <=poly(N) max(1,R_src^2).  (11)

ALL clocks, original Newton coefficients and outer phases are inside f_N;
none were separately estimated before this contour was constructed.

This does not establish an upper bound by knot volume. The critical
points of a product of finite generating polynomials need not be genuine
stationary points of a single classical WKB branch: branch cancellation
or anti-Stokes interfaces can create extra critical values. The largest
critical envelope already overshoots in simple prototypes. Even the
selected R_src is not proved to have the hyperbolic-volume rate for
general knots. The required remaining theorem must estimate THIS marked
level with its exact source, or refine its cycle further; it cannot simply
identify every finite polynomial critical point with a knot representation.

As a check, for the figure-eight the actual A_N=1+z+...+z^d and every
coefficient of W_N is positive. Thus R_src<=max_(|z|=1)|f_N(z)|
=f_N(1)=N K_N. Together with (10), the selected level has the same known
exponential rate as K_N in this prototype. This does not extend the
positivity argument to the complex five-crossing coefficients.

[Audit](../experiments/audit_whole_source_hadamard_lemniscate.py): exact
original Laurent cuts, monic confluent Newton conversion, all-color
truncation, Hadamard source equality and known one-pole treatment. Numerical
connectivity diagnostics are kept separate from the proof and are not used
to assert a geometric barrier or a new volume theorem.
