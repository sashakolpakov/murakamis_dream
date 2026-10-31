# An exact accretive determinant for the joint magnetic source

30 October 2026. The finite rational continuation specified in
[the magnetic corridor note](actual_q_hahn_magnetic_complex_corridor.md),
section 6, has an exact tridiagonal determinant. Its Hermitian part is
positive on a joint complex domain in the pair degree and the magnetic
coordinate. This proves joint zero exclusion and uniform logarithmic
derivative bounds for the original finite source, including both
parities, composite levels and the folded channel endpoint. The domain
is a central wedge; it is smaller than the fixed-real-degree strip.
No global source cycle, magnetic stationary point, or volume limit is
selected by this theorem.

## 1. The exact finite source, including its scalar

Put d=N-1, theta=pi/N, q=exp(i theta), Q=q^2, x=q^d and
0<=j<=floor(d/2). Gaussian binomials below have base Q. The source is

    fhat_j(u,v)=x^u H_j(U,V)/D_j(UV),
    U=Q^u, V=Q^v, T=UV=Q^t, t=u+v,
    D_j(T)=product_(r=0)^(j-1)(T-Q^r),

    H_j(U,V)=sum_(a=0)^j [j choose a]_Q^2 q^[a(a-d)] V^a
        product_(r=0)^(a-1)(U-Q^r)
        product_(r=0)^(j-a-1)(V-Q^r).                  (1)

All exponential powers use these displayed logarithms. At physical
integer u,v this is the original normalized complete-circle column;
(1) also specifies its continuation, without interpolating samples.
Set

    S_j(U,T)=U^j H_j(U,T/U).

Since q^[a(a-d)]=(-1)^a Q^[a(a+1)/2], this is the polynomial

    S_j(U,T)=sum_(a=0)^j (-1)^a Q^[a(a+1)/2]
      [j choose a]_Q^2 T^a
      product_(r=0)^(a-1)(U-Q^r)
      product_(r=0)^(j-a-1)(T-UQ^r).                  (2)

It has degree at most j separately in U and T. Two exact evaluations are

    S_j(U,0)=(-1)^j Q^[j(j-1)/2] U^j,
    S_j(0,T)=T^j [2j choose j]_Q.                    (3)

For the second, the finite coefficient identity
sum_a Q^(a^2)[j choose a]_Q^2=[2j choose j]_Q follows by comparing
z^j in product_(r=0)^(2j-1)(1+Q^r z), split into its two j-factor
blocks. All scalar factors in (3) are nonzero: 2j<N.

## 2. A joint Casimir identity, proved before continuation

The exact polynomial identity is

    -Q^(-j)(U-T)(1-QU) S_j(QU,T)
    -Q^j(U-QT)(1-U) S_j(U/Q,T)
    +[2(1+QT)U-(1+Q)U^2
                      -T(Q^(j+1)+Q^(-j))] S_j(U,T)=0.              (4)

Here is a finite proof which does not extend an integer-t recurrence
without justification. For the j+1 original complete slices
T=Q^(d-j),...,Q^d, the exact physical Casimir equation gives (4).
The entire-U equation on each slice is already proved in section 4 of
the magnetic corridor note: its leading U^(j+2) coefficient cancels,
and its U=0 value and all original t+1 column nodes make the remaining
polynomial of degree at most j+1 vanish. This includes t=d-j=j when
N is odd and the channel is maximal.

The left side of (4) has degree at most j+1 in T. At T=0, substitute
the first identity in (3); the remaining factor is

    -U(1-QU)-U(1-U)+2U-(1+Q)U^2=0.

The j+1 distinct nonzero complete slices and T=0 are j+2 distinct
zeros, so (4) holds identically in T and U. This argument proves the
complex-degree source identity at every admissible N directly. The
focused audit also verifies (4) coefficientwise at formal Q for j=2
through 6; the proof does not depend on those checks.

Write

    c=-cos((t+1)theta),
    P_j(z;c)=S_j(q^t z,Q^t)/[Q^(jt) [2j choose j]_Q].                (5)

The constant coefficient is 1. Substitution into (4), followed by
coefficient comparison, gives, with p_(j,-1)=0 and p_(j,0)=1,

    sin(k theta) sin((2j+1-k)theta) p_(j,k)
      =2c sin^2((j+1-k)theta) p_(j,k-1)
       +sin((j+2-k)theta) sin((j+1-k)theta) p_(j,k-2).               (6)

All denominators for 1<=k<=j are positive. Thus this identity determines
P_j for every complex t, not only for physical slices. Define the monic
reverse polynomial R_j(z;c)=z^j P_j(1/z;c). Equation (1) is exactly

    fhat_j(u,t-u)=x^u q^(jt) [2j choose j]_Q
                   R_j(q^t/U;c)/D_j(Q^t).                         (7)

In particular no root-dependent normalization is discarded.

## 3. The ordinary three-term recurrence

For 1<=n<floor(d/2), put

    B_n=sin^2(n theta)/[cos^2(n theta)
                         sin((2n-1)theta)sin((2n+1)theta)].         (8)

The recurrence is

    R_0=1, R_1=z+c/cos(theta),
    R_(n+1)=[z+c/(cos(n theta)cos((n+1)theta))]R_n
                +B_n[cos^2(n theta)-c^2]R_(n-1).                  (9)

We prove that no lower-degree terms are hidden in (9). Set
[r]=sin(r theta)/sin(theta) and D_q z^r=[r]z^(r-1). Equation (6) is
equivalent to

    L_c R_n=[n][n+1]R_n,
    L_c=D_q ((z^2+2cz+1)D_q).                                    (10)

Indeed L_c z^r=[r][r+1]z^r+2c[r]^2z^(r-1)+[r][r-1]z^(r-2).
The eigenvalues for n=0,...,J, J=floor(d/2), are distinct: their
successive differences are [2n]>0.

Define finite moments mu_0=1, mu_(-1)=0, and

    [r+1]mu_r+2c[r]mu_(r-1)+[r-1]mu_(r-2)=0
                           (1<=r<=2J-1).                         (11)

No denominator vanishes, since 2J<N. On available degrees let
<z^m,z^n>=mu_(m+n). The difference <z^m,L_c z^n>-<L_c z^m,z^n>
is [n-m] times the left side of (11) at r=m+n, by the elementary
sine addition identities. Thus the R_n are pairwise orthogonal
whenever the requisite total degree is at most 2J-1.

Inductively assume the lower norms are nonzero for generic c. In the
expansion of zR_n-R_(n+1), pairing with R_k, k<=n-2, kills every
coefficient below R_(n-1), since multiplication by z is symmetric.
The two remaining coefficients are read from the top powers. Equation
(6) gives

    p_(n,1)=c tan(n theta)/sin(theta),
    p_(n,2)=[2c sin^2((n-1)theta)p_(n,1)
                   +sin(n theta)sin((n-1)theta)]
                        /[sin(2theta)sin((2n-1)theta)],            (12)

where p_(1,2)=0. Subtracting these coefficients at n and n+1 gives
exactly (9). The norm identity is

    <R_n,R_n>=-B_n[cos^2(n theta)-c^2]<R_(n-1),R_(n-1)>.

It proves the generic nonvanishing needed for the next induction
step, starting at norm 1; hence there is no assumption of positivity
of this auxiliary moment functional. Polynomial continuation in c
then gives (9) for every c. Only moments through 2J-1 are used,
including for the maximal channel. The moment functional is a proof
device, not a new quantum inner product.

## 4. A positive definite real part

For a chosen size j, define real j-by-j matrices D and K, with indices
0,...,j-1. Their diagonal and adjacent entries are

    D_(n,n)=1/[cos(n theta)cos((n+1)theta)],
    D_(n-1,n)=D_(n,n-1)=sqrt(B_n),
    K_(n-1,n)=sqrt(B_n)cos(n theta),
    K_(n,n-1)=-sqrt(B_n)cos(n theta), K_(n,n)=0.                    (13)

All other entries are zero. Thus D is symmetric and K is
skew-symmetric. The tridiagonal determinant recurrence and (9) give

    R_j(z;c)=det(zI+cD+K).                                        (14)

Every leading principal minor of D is explicitly

    det D_m=2^m product_(r=1)^m sin(r theta)
                     /product_(r=m+1)^(2m) sin(r theta)>0,
                  1<=m<=j.                                     (15)

To see the formula without solving a separate determinant problem,
compare the leading c^m coefficient of R_m(0;c)=p_(m,m)(c) in (14).
Iteration of the highest-c terms of (6) gives precisely (15).
All factors are positive because 2m<N. Sylvester's criterion gives
D positive definite, including when j=floor(d/2).

If Re c>0, the Hermitian part of cD+K is (Re c)D>0. For any
eigenvector, its eigenvalue therefore has positive real part. The
zeros of R_j all lie strictly in Re z<0; reversal gives the same
statement for P_j. No real-rootedness assertion is needed or made
for noninteger t. For positive real c the coefficients in (6) are
positive, so R_j(1;c)>0.

More generally A=zI+cD+K is invertible whenever Re z>=0 and Re c>0.
In the open product of right half-planes its logarithmic derivatives
satisfy

    |partial_z log det A|<=j/Re z,
    |partial_c log det A|<=j/Re c.                                (16)

The first follows from Re A>=(Re z)I and the inverse operator norm.
For the second conjugate by D^(-1/2):

    D^(-1/2) A D^(-1/2)
        =zD^(-1)+cI+D^(-1/2)KD^(-1/2).

Its Hermitian part is at least (Re c)I, and its inverse has trace
partial_c log det A. Thus (16) uses no uniform lower eigenvalue
bound for D, which could degenerate as the channel approaches 1/2.

## 5. An N-independent joint central wedge

Use scaled variables tau=t/N and upsilon=u/N, retaining j as its
actual integer channel. Consider the convex domain

    W={ (tau,upsilon) in C^2:
             1/2<Re tau<1,
             |2Re upsilon-Re tau|<1/2 }.                         (17)

For every admissible N and j,

    c=-cos(pi(tau+1/N)),
    z=exp(pi i(tau-2upsilon)).                                    (18)

The first has positive real part on (17): for N>=2 its cosine
argument has real part strictly between pi/2 and 3pi/2. The second
has positive real part by the second inequality. Also D_j(Q^t)
has no zero on W. Such a zero would require tau=r/N plus an integer,
with 0<=r<=j-1<N/2, contrary to 1/2<Re tau<1.
Consequently the exact original finite function (7) is holomorphic
and nowhere zero throughout W, simultaneously in tau and upsilon.
The zero channel j=0 is the explicit nonzero exponential and needs
no matrix.

On every compact subset of W the quantities Re c, Re z and the
separation from the denominator zeros have positive lower bounds
uniformly for sufficiently large N. Equations (7), (16), and the
product formula for D_j show that both first logarithmic derivatives
of N^(-1)log fhat are uniformly bounded. Higher derivatives on
smaller compacts follow from Cauchy's formula. Since W is convex,
a logarithm is fixed by one marked base value, and normalized
logarithmic ratios are locally bounded uniformly in N and j.

There is a convenient exact phase normalization at a REAL center
upsilon=tau/2 with 1/2<tau<1, even when t=N tau is noninteger.
Here c>0 and R_j(1;c)>0. Writing each D_j factor as
2i q^(t+r)sin((t-r)theta), and using
[2j choose j]_Q=q^(j^2) times a positive sine-binomial, gives

    Arg fhat_j(t/2,t/2)=pi[d(t-j)+j^2]/(2N).                       (19)

This is a specified continuous argument, rather than its value
modulo 2pi. Thus the joint continuation carries the same marked
center phase as the original real-degree corridor.

## 6. What this removes, and what it leaves

The pair degree is now genuinely complex in an exact source-defined
zero-free domain. Neither integer sampling nor a formal WKB solution
is used to declare that continuation. The logarithmic estimates are
uniform at the folded endpoint and can support a subsequent normal
family or finite-shift argument for a joint selected action.

The present theorem does not assert a joint amplitude asymptotic,
a globally admissible frame for an arbitrary plat, or intersection
of its original cycle with the geometric critical point. In
particular W is a central wedge, not the whole fixed-t magnetic
strip, and simultaneous membership of all source coupons in W
is an additional global question. These distinctions remain even
though (14) is an exact algebraic identity.

Audit: [exact joint determinant and source checks](../experiments/audit_actual_q_hahn_joint_accretive_determinant.py).

This is a local joint theorem. It does not supply a global source frame, asymptotic amplitude or selected cycle.
