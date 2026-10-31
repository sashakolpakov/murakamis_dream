# Polynomial cost of the actual small-channel generic normals

30 October 2026. This note concerns the original generic highest-weight
N-1 columns, including the factors that simplify only at the root of
unity. On compact subsets of the joint central wedge, every fixed
generic-q derivative of a small-channel column has at most polynomial
cost relative to that column's root value. The estimate includes the
folded small channel and both parities. It does not bound the paired
large-channel derivative, the confluent spectral normal formed from
both channels, or the whole marked source.

## 1. The exact generic deformation

Fix N>=3, d=N-1 and q0=exp(pi i/N). Let q vary near q0; put

    Q=q^2, B=Q^(-N), A=B^(-1), x=q^d,
    t=u+v, U=Q^u, V=Q^v, T=UV, s=q^t,
    D_j(T)=product_(r=0)^(j-1)(T-Q^r).

All complex powers use log(q)=pi i/N+epsilon. Gaussian binomials and
Pochhammer products below have base Q. Define

    H_j^B(U,V)=sum_(a=0)^j (-1)^a B^a Q^[a(a+1)/2]
      [j choose a]_Q (B Q^(j-a+1);Q)_a/(BQ;Q)_a
      V^a product_(r<a)(U-Q^r) product_(r<j-a)(V-Q^r),

    C_j(q;t,u)=x^u H_j^B(U,V)/D_j(T),
    S_j^B(U,T)=U^j H_j^B(U,T/U).                       (1)

This is the actual generic column in
[the mixed compiler](actual_mixed_augmented_plat_compiler.md), section
2, at physical t,u. It also specifies a finite rational continuation
for complex t,u. To check the source before differentiating, its
highest-vector ratio is exactly

    R_(j,a)=(Q^(N-j);Q)_a/(Q^(N-a);Q)_a
      =Q^[a(a-j)] (B Q^(j-a+1);Q)_a/(BQ;Q)_a.          (2)

Converting the three Gaussian binomials in that compiler into finite
Newton products gives (1). In particular the additional factor is
B^a times the displayed Pochhammer ratio. Merely inserting a power
of -q^(-N) into the root-only squared-binomial formula would give the
wrong generic source and the wrong first derivative.

The exact leading scalar is

    S_j^B(0,T)=T^j K_j,
    K_j=(B^2 Q^(j+1);Q)_j/(BQ;Q)_j.                  (3)

Here is an elementary proof of the finite identity used in (3).
For generic a,c,Q and integer n>=0,

    sum_(k=0)^n (Q^(-n);Q)_k (a;Q)_k /
      [(Q;Q)_k(c;Q)_k] (c Q^n/a)^k
       =(c/a;Q)_n/(c;Q)_n.                           (4)

Multiply both sides by a^n(c;Q)_n. Each side is a polynomial of
degree at most n in a. At a=c Q^m, 0<=m<n, the quotient
(a;Q)_k/(c;Q)_k=(c Q^k;Q)_m/(c;Q)_m is a polynomial in Q^k of
degree m. For each of its powers Q^(rk), r<=m, the finite binomial
sum on the left is (Q^(r-m);Q)_n=0. Thus the left polynomial has
all the n roots of product_(r<n)(a-cQ^r). Its constant term, from
k=n alone, is (-1)^n c^n Q^[n(n-1)/2], fixing the multiplier to 1.
This proves (4) as a rational identity. Taking n=j,
a=B^(-1)Q^(-j), c=BQ gives (3), after converting (Q^(-j);Q)_a to
the Gaussian binomial. No asymptotic identity is used here.

## 2. The generic Casimir polynomial and its three-term recurrence

The exact equation for S=S_j^B is

    Q^(-j)(QU-A)(U-T) S(QU,T)
     +Q^j(BQT-U)(1-U) S(U/Q,T)
     +[(1+A)U+QT(1+B)U-(1+Q)U^2
                   -T(AQ^(-j)+BQ^(j+1))]S(U,T)=0.     (5)

It follows from the actual generic coproduct Casimir, whose column
eigenvalue is q^(2N-1-2j)+q^(-2N+1+2j). Alternatively, one can
verify its extension from physical columns by exactly the finite
degree argument used for the root equation in
[the joint determinant note](actual_q_hahn_joint_accretive_determinant.md).
The residual has degree at most j+1 in U: the top degree cancels;
its constant coefficient also vanishes. At each original complete
slice t=d-j,...,d, its original t+1 column values and U=0 force
the whole U polynomial to vanish. The residual has degree at most
j+1 in T. These j+1 slices, together with T=0, force its vanishing
identically. At T=0 use
S(U,0)=(-1)^j Q^[j(j-1)/2]U^j; the residual cancels directly.
This proves (5) in a neighborhood of the actual root, where all
these finite source columns and distinct slice values are defined.

Let R_n(z) be the monic reverse polynomial obtained from (1):

    R_n(z)=z^n S_n^B(s/z,s^2)/(s^(2n)K_n).

Equation (5) says L R_n=Lambda_n R_n for the triangular operator

    L z^n=Lambda_n z^n+b_n z^(n-1)+d_n z^(n-2),
    Lambda_n=AQ^(-n)+BQ^(n+1),
    b_n=[(1+A)+Qs^2(1+B)-Q^(-n)(Qs^2+A)
                                      -Q^n(BQs^2+1)]/s,
    d_n=Q^(1-n)+Q^n-1-Q.                              (6)

Terms with negative powers are absent, since b_0=d_0=d_1=0.
Write the two coefficients below the leading one as u_n,v_n.
Their exact expressions are

    u_0=0, u_n=b_n/(Lambda_n-Lambda_(n-1)), n>=1,
    v_0=v_1=0,
    v_n=(b_(n-1)u_n+d_n)/(Lambda_n-Lambda_(n-2)), n>=2.

For 0<=n<j, put

    alpha_n=u_(n+1)-u_n,
    beta_n=v_(n+1)-v_n-alpha_n u_n  (n>=1).

Then exactly

    R_0=1, R_1=z+alpha_0,
    R_(n+1)=(z+alpha_n)R_n+beta_n R_(n-1).             (7)

For completeness, a finite moment argument rules out extra lower
terms in (7). Set mu_0=1, mu_(-1)=0 and impose

    (BQ^(r+1)-A)mu_r
     +[(Qs^2+A)-(BQs^2+1)Q^r]mu_(r-1)/s
     +(Q^r-Q)mu_(r-2)=0, 1<=r<=2j-1.                (8)

The difference of the two monomial pairings for L factors as
(Q^n-Q^m)Q^(-n-m) times (8) at r=m+n. Thus L is symmetric for
this finite moment functional. Its eigenvalues of degrees 0,...,j
are distinct near the root. The usual finite orthogonality argument
now kills the terms below R_(n-1) in zR_n-R_(n+1); the top two
coefficients give (7). This argument can first be made at generic s,
where the preceding norms do not vanish: the norm recursion is
h_n=-beta_n h_(n-1). At B=1 the beta_n are the nonzero polynomials
in c displayed below, so generic nonvanishing follows inductively.
Rational continuation then proves (7) also when a particular beta_n
vanishes. No positive generic moment functional is assumed.

Combining (1),(3) gives the exact normalized source

    C_j=x^u q^(jt) K_j R_j(q^t/U)/D_j(Q^t).           (9)

All the generic coefficients in this section retain B=Q^(-N).
Equation (7) is not a deformation chosen after specialization.

## 3. A uniformly controlled generic neighborhood

Let W be the joint wedge

    1/2<Re(t/N)<1,
    |2Re(u/N)-Re(t/N)|<1/2.

For every compact K contained in W there are constants c_K,C_K>0,
independent of N and 0<=j<=floor((N-1)/2), such that

    |C_j(q0 exp(epsilon);t,u)/C_j(q0;t,u)|<=C_K
                   whenever |epsilon|<=c_K N^(-8), (t/N,u/N) in K.
                                                               (10)

In particular the denominator on the left is nonzero. The power 8
is a convenient conservative bound; no optimal power is claimed.

Here are explicit estimates proving the assertion. At epsilon=0,
put theta=pi/N, c=-cos((t+1)theta), z=q0^(t-2u). On a fixed K,
Re c and Re z have positive lower bounds for all sufficiently large
N. The root recurrence (7) is

    alpha_n=c/[cos(n theta)cos((n+1)theta)],
    beta_n=Bcal_n[cos^2(n theta)-c^2],
    Bcal_n=sin^2(n theta)/[cos^2(n theta)
                            sin((2n-1)theta)sin((2n+1)theta)].

Thus its determinant is M_0=zI+cD+Kskew, with the actual positive
D and real skew matrix Kskew in the joint determinant note.
Accretivity gives ||M_0^(-1)||<=1/Re z, uniformly in the channel,
including the fold.

Construct the generic tridiagonal matrix M_epsilon with diagonal
z(q)+alpha_n(q). Freeze its upper entries to their ROOT values

    r_n=sqrt(Bcal_n)[c+cos(n theta)], 1<=n<j,

and use lower entries -beta_n(q)/r_n. Its determinant is R_j by
(7), and at epsilon=0 it is exactly M_0. There is no square-root
choice for the generic beta_n. Since sqrt(Bcal_n)>=1/2 and Re c
is uniformly positive, |r_n| is bounded below independently of N.

The only spectral differences in (6),(7) factor as

    Lambda_n-Lambda_(n-1)
       =(1-Q)A Q^(-n)(1-B^2 Q^(2n)),
    Lambda_n-Lambda_(n-2)
       =(1-Q^2)A Q^(-n)(1-B^2 Q^(2n-1)).             (11)

At the root their nonzero factors give lower bounds c/N^2 for
all required n<=j. All elementary exponents have size O(N), so
these bounds persist in a disk |epsilon|<=c N^(-3). On a smaller
such disk, direct differentiation of (6),(7) gives uniformly

    |u_n|=O(N^2), |u_n'|=O(N^5),
    |v_n|=O(N^4), |v_n'|=O(N^7),
    |alpha_n'|=O(N^5), |beta_n'|=O(N^7).             (12)

Here primes mean d/d epsilon. The coefficients b_n,d_n,Lambda_n
are O(1), with derivatives O(N); (12) follows by the quotient
rule and (11). Consequently the tridiagonal operator norm satisfies

    ||M_epsilon-M_0||<=C_K N^7 |epsilon|.

On the disk in (10), ||M_0^(-1)(M_epsilon-M_0)||<=C_K c_K/N.
Choose c_K small. The determinant ratio is bounded by
(1+C_K c_K/N)^j, and hence uniformly bounded; it is also nonzero.

The remaining scalar factors in (9) have controlled ratios on the
same disk. The exponents of x^u q^(jt) have size O(N^2).
Each root factor of K_j has size at least c/N, its derivative is
O(N), and there are O(N) factors; thus |(log K_j)'|=O(N^3).
The factors of D_j(Q^t) are separated uniformly from zero on K,
so its logarithmic derivative is O(N^2). Integration over the
N^(-8) disk bounds all these scalar ratios. This proves (10).
Finitely many remaining N can be absorbed by changing constants;
j=0 follows immediately from C_0=x^u.

## 4. Consequence for actual generic derivatives, and its limit

Cauchy's estimate applied to the exact source in (10) gives, for
every fixed integer m>=0,

    |(q d/dq)^m C_j(q0;t,u)|
        <=C_(K,m) N^(8m) |C_j(q0;t,u)|.              (13)

The derivative holds t,u,N fixed, exactly as the original generic
compiler does. At physical integer t,u it is its actual generic
normal; at complex t,u it is the derivative of the finite source
continuation (1). Combining (13) with the proved joint root-value
amplitude preserves its leading exponential action, as an upper
bound, for these fixed-order small-channel derivatives.

The mixed compiler's confluent column is proportional to
D C_j-D C_(N-1-j). Except at the simple folded endpoint, its second
term is a LARGE channel. In that channel K_l vanishes at the root
and the monic recurrence crosses resonant eigenvalue differences.
The argument above does not apply. In particular (13) is not a
bound for that difference, its spectral derivative, a complete
mixed kernel, or a generic normal of the whole pointed invariant.

Focused audit: [actual generic values and normals](../experiments/audit_actual_q_hahn_small_channel_generic_normals.py),
with [saved results](../experiments/actual_q_hahn_small_channel_generic_normals_results.json).
It passed 1,304 original generic value-and-derivative comparisons,
216 generic determinant identities, 216 generic Casimir identities,
216 Vandermonde value-and-derivative identities, and 1,041 original
root-normal comparisons in exact finite-field dual arithmetic. At
100 digits, 48 nonphysical generic comparisons and 24 original
root-normal comparisons passed; 96 points on the stated polynomial
disk were also sampled. The disk samples are regressions, not the
proof of uniform control.

The result is restricted to the stated small-channel domain and fixed-t,u Cauchy derivative convention.

The paired large channel is excluded.