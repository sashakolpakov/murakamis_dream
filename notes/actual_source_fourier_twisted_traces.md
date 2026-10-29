# The original source has an exact Fourier resolution into twisted traces

27 October 2026. The all-strand endpoint source admits a resolution
into UNIT-density Frobenius traces on one common matrix algebra of
actual word coefficients. Their source-conjugation transport satisfies
an explicit nonabelian norm equation. Primitive Fourier sectors have
finite cyclic transport (as do gcd-two sectors); the remaining
transport is unipotent, with index EXACTLY gcd(k,N). The zero sector has index EXACTLY N
when N>2. Thus nilpotence exists but is not uniformly bounded in level.

Individual sectors are not knot invariants: an actual braid-conjugacy
test changes their values while preserving their marked Fourier sum.
No sector is identified here with a geometric A-period, nor is its
coefficient bounded subexponentially. This note does not replace the
already proved symmetric trace on the full E,F,K centralizer in
[the integral cut theorem](integral_projective_cut_duality.md).

## 1. The actual endpoint is a Nakayama-relative line

Use the actual root algebra and cap of
[the Euler/Cauchy theorem](actual_euler_cap_cauchy_boundary.md):

    A_0=<H,f | H^N=1, Hf=Q^-1 fH, f^N=0>,
    e_j=(1/N)sum_k Q^(jk)H^k,
    tau(f^a e_j)=delta_(a,N-1),
    nu(H)=QH, nu(f)=f,
    tau(ab)=tau(b nu(a)).

Set z=xf, J=1/[(1-z)(1-Qz)] and

    E=e_(N-1)J, nu(E)=e_0 J, s=f^(N-1)e_0.

The rational expression J is an actual finite polynomial because z
is nilpotent. Its degree-(N-1) coefficient is zero at Q^N=1.
Also e_(N-1)J e_(N-1)=e_(N-1). Consequently

    E^2=E, tau(E)=0, tau(s)=1,
    E a nu(E)=rho_0(Ja) s for EVERY a in A_0,       (1)
    rho_0=[f^(N-1)e_0].

For (1), the two endpoint idempotents in e_(N-1)Ja e_0 select
exactly its f^(N-1)e_0 coefficient. Right multiplication by J does
nothing to s since s f=0. Thus the actual source is a specified
rank-one linear compression between DIFFERENT projectives.

Ordinary compression E a E would erase it: E is a primitive
idempotent lifting e_(N-1), so E A_0 E=C E, and tau vanishes on
that entire corner. More explicitly put n=e_(N-1)(J-1). Then
n^2=0, n e_(N-1)=0, and

    E=(1-n)e_(N-1)(1+n).

The corner claim follows from e_(N-1)A_0 e_(N-1)=C e_(N-1).
In contrast (1) is nonzero at a=s.

This linear compression is not a word quotient. Already at N=2,
the actual positive crossing coefficient is

    a_R=eta I+(eta^-1/2)s, eta=exp(pi*i/4).

Here J=1. The map P(a)=E a nu(E) has P(e_0)=0 but
P(a_R e_0)=(eta^-1/2)s!=0. Transport on the selected scalar line
alone would lose real word data. One must retain the projective
memory E A_0, or another independently proved source complex.

Nor is the single cap a twisted trace for some automorphism merely
because tau is. If tau(Eab)=tau(Eb theta(a)) for every a,b, Frobenius
nondegeneracy implies

    nu(E)nu(a)=theta(a)nu(E).

Thus nu(E)A_0=A_0 nu(E). A normal idempotent is central: both off-
diagonal corners vanish. But the center of A_0 is C and E is a
proper primitive idempotent. This rules out that shortcut. The
Fourier resolution below instead uses invertible densities.

## 2. Align all tail heads on ONE actual coefficient algebra

The [all-strand source theorem](all_strand_euler_cauchy_cap.md)
decomposes the closed tail into r=N^(b-2) normalized Borel heads.
For b>=3 label them lambda=(t,j), with y_lambda=YQ^-j;
for b=2 use one head and j=0. Let C_lambda be its actual two-leg
fusion. The physical GLOBAL H=K_total/(xY) acts in that local
regular frame as Q^-j times left multiplication by H.

Replace that local frame by

    Psi_lambda=C_lambda composed with nu^-j.        (2)

Indeed nu^-j(Ha)=Q^-j H nu^-j(a), so (2) intertwines the same
global H and f on every copy. Consequently the full actual braid,
INCLUDING all off-diagonal tail transitions, acts on row vectors by
right multiplication by a matrix A in B=Mat_r(A_0). Transposing
the usual array of block right coefficients gives this row-vector
convention. Operator composition is right action in its original
order; no diagonal blocks are extracted during multiplication.

The physical Euler-dressed coefficient matrix is

    b=U^-1 A U, U=diag(u(z)),
    u(z)=sum_(a=0)^(N-1) z^a/(Q;Q)_a.

The matrix Frobenius functional and Nakayama map are

    T(b)=sum_lambda tau(b_(lambda,lambda)),
    nu acts entrywise,
    T(ab)=T(b nu(a)).

Changing from the local head to (2) sends its word coefficient
to nu^j of the local coefficient. Therefore the ORIGINAL source
from the all-strand theorem becomes EXACTLY

    P_W=chi_W gamma_0 T(D b),
    gamma_0=N x^(b(1-N))Q,
    D=diag_lambda[Q^-j e_(j-1)J].                 (3)

All original framing and full peripheral factors remain in chi_W.
This is valid for varying actual meridian x=-M/q at the fixed root
on its original source lattice. It does not equate central-F and
moving-q normals. Formula (3) follows either from the literal
pivotal trace or from rho_j(Jb)=tau(e_(j-1)Jb); no invariant is
divided out to choose the frame.

## 3. Fourier resolution into genuine unit-density traces

The idempotent Fourier formula gives

    D=(1/N)sum_(k=0)^(N-1) C_k,
    C_k=diag_lambda[Q^(-j+(j-1)k)] H^k J.          (4)

Every C_k is a UNIT of B. Define

    Phi_k(a)=T(C_k a),
    theta_k=Ad_(C_k) composed with nu.

Then Phi_k is a nondegenerate Frobenius functional and

    Phi_k(ab)=Phi_k(b theta_k(a)),
    P_W=(chi_W gamma_0/N)sum_k Phi_k(b).          (5)

For the twisted trace identity, T(C_k ab)=T(b nu(C_k)nu(a)).
Since nu(C_k)=Q^k C_k, its scalar multiplier cancels in inner
conjugation, giving theta_k as stated. These are actual whole-word
source sectors, not characters assigned to semisimple root points.
Their Fourier SUM recovers the original nonunit source density D.

If desired the space of all invertible Frobenius densities is a
torsor under the noncommutative unit group B^times. It is not yet
the G_m/norm-one torus of a simple quantum A-eigenline. Passing to
that latter object requires its own central spectral compatibility.

## 4. Exact finite-order and unipotent source transport

Put g=gcd(k,N), d=N/g, taking g=N,d=1 when k=0. The scalar-
diagonal phases in C_k have Nth power one. Using HfH^-1=Q^-1 f,
the product formula for its Nth power is

    C_k^N=G_k(z) I_r,
    G_k(z)=[(1-z^d)(1-Q^d z^d)]^-g.              (6)

Indeed multiplication visits every dth-root orbit of z exactly g
times. The two factors in J give the two products displayed in (6).
All are units on the actual nilpotent source. Also nu(C_k)=Q^k C_k
and nu^N=Id. Hence

    theta_k^N=Ad_(G_k(z) I_r).                    (7)

In particular primitive k has g=1, z^N=0, so G_k=1 and
theta_k^N=Id. This conclusion is valid at every composite N too.
The same holds for g=2: Q^d=-1 and the two denominator factors
multiply to 1-z^N=1. For g>2 the bound (8) is sharp.

For the remaining k, G_k=1+O(z^d). On the basis f^a H^j,

    Ad_(G_k)(f^a H^j)
       =f^a [G_k(z)/G_k(Q^-j z)] H^j.

The factor in brackets minus one belongs to (z^d), and Ad_(G_k)
fixes all functions of z. Iterating a difference therefore gains
one further factor z^d on each iteration, proving the sharper bound

    (theta_k^N-Id)^g=0.                           (8)

To see sharpness, the leading term for g>2 is

    G_k(z)=1+g(1+Q^d)z^d+O(z^(2d)).

The ratio at j=1 has nonzero leading coefficient
g(1+Q^d)(1-Q^-d)z^d. Its (g-1)st power survives because
d(g-1)<N. Thus the index is exactly g. In particular there is
no uniform level-independent bound. For k=0 and N>2,

    G_0(z)=J(z)^N=1+N(1+Q)z+O(z^2).

Its ratio at j=1 has nonzero linear coefficient
N(1+Q)(1-Q^-1). Thus (Ad_(G_0)-Id)^(N-1)(H)!=0, while its
Nth power is zero: the index in (8) is EXACTLY N. The exception
N=2 has J=1, so its cyclic transport is already finite order.
The growing index and the unestimated word coefficients prevent
using nilpotence alone as a subexponential norm estimate.

There is an explicit Hilbert-90 gauge in every g<=2 sector.
Put C_k^0=diag_lambda[Q^(-j+(j-1)k)]H^k and
mu_k=Ad_(C_k^0) composed with nu. It sends z to Q^-k z.
Choose the finite nilpotent exponential

    g_k(z)=exp sum_(a=1)^(N-1)
                (1+Q^a)z^a/[a(Q^(ka)-1)].          (8a)

At g=1 every displayed denominator is a unit. At g=2 the sole
resonant degree a=d has numerator zero too; choose that coefficient
to be zero rather than interpret a zero-over-zero expression.
Coefficient comparison in the finite logarithm proves

    g_k(Q^k z)/g_k(z)=J(z),
    theta_k=Ad_(g_k) composed with mu_k
                         composed with Ad_(g_k^-1). (8b)

For k=1 this gauge is especially concrete:

    g_1(z)=v(z)v(Qz)=[u(z)u(Qz)]^-1
                       =(1-z)^-1 u(z)^-2.         (8c)

Thus the finite cyclic transport is explicitly solved, but its
comparison gauge contains TWO quantum Euler factors. It is not a
polynomial-norm estimate and must retain those factors in a regulator
comparison. For g>2 the nonzero resonant term at degree d prevents
solving the same scalar-polynomial gauge equation: its numerator
1+Q^d is nonzero while Q^(kd)-1=0. This is precisely the remaining
unipotent defect rather than an omitted normalization choice.

The subsequent [uniform actual-gauge action proof](actual_hilbert90_gauge_dilogarithm_action.md)
now makes this metric issue quantitative. For the CANONICAL finite
polynomial g_1, uniformly on |z|<=1/4,

    g_1(z)=exp[(2/h)Li_2(z)+O(1/N)], h=2pi*i/N.

Its flat right-regular operator and inverse have positive exponential
norm rates, so its condition number grows exponentially. This is
the specified actual source gauge, not an arbitrary rescaling.
In contrast, [its Euler meridian half-step](actual_euler_meridian_half_step.md)
has a polynomial condition bound and a nonzero exact sourced endpoint.
Both results retain their degree-N carries and stated metrics.

## 5. The source-conjugation torsor has a concrete norm equation

For any actual invertible word coefficient c, or any unit of B,
put

    h_k(c)=c theta_k(c)^-1.

Twisted cyclicity gives the exact PERIOD equation

    Phi_k(c^-1 b c)=Phi_k(b h_k(c)).               (9)

This states precisely how the sector co-source must be transported
under conjugation. Its ordered cyclic norm telescopes:

    product_(r=0)^(N-1) theta_k^r(h_k(c))
        =c theta_k^N(c)^-1
        =c G_k c^-1 G_k^-1.                     (10)

Sectors with gcd(k,N)<=2 therefore have a genuine nonabelian norm-one
source equation; the other sectors retain an explicit unipotent
commutator defect. On an independently identified commutative
simple eigenline this would become an ordinary Hilbert-90-type
comparison. Neither that eigenline nor its geometric support is
assumed here. The nonprimitive defect and the marked Fourier
sum cannot simply be deleted.

The individual values Phi_k(b) are not knot invariants. There is
an exact actual-matrix witness with the SAME braid index and writhe:
at N=3 over F_1009, the figure-eight word beta=(1,-2,1,-2)
has sector values

    [224,545,410], average 393,

whereas sigma_1 beta sigma_1^-1=(1,1,-2,1,-2,-1) has

    [619,845,724], average 393.

All external normalization factors are identical in this comparison.
Thus an adapter depending only on level, color, braid index and
writhe cannot turn these fixed sectors into ordinary-color knot
evaluations. Equation (9), with its actual transported co-source,
is required. The sum in (5) does give the original invariant.

There is also a local E-commutation obstruction: at N=2, J=1
and theta_k sends the nonconstant part f e_0 of the actual crossing
to Q^-k f e_1. After undoing the Euler/fusion frame its right
operator no longer commutes with the actual total E. The audit
checks a nonzero literal commutator. Consequently theta_k is an
automorphism of the full Borel-relative algebra, not generally of
the smaller actual E,F,K centralizer. Its sectors must not be
identified with that centralizer's existing symmetric cut trace.

## 6. What this advances and what remains

This gives an explicit source-preserving Fourier family with a
fully solved finite-level cyclic transport equation, including its
nonabelian norm defect. It also identifies the exact linear source
line and shows why ordinary corner compression erases it. These
are algebraic statements about the actual selected source and the
completed original word at arbitrary braid index.

They do not supply a nonzero selected geometric A-sector, a bound
for the sector sum, or a sharp volume norm. In particular finite
cyclic transport, even in primitive sectors, does not bound the
value of a word; the norm-one condition alone permits large
comparison matrices. The zero sector's nilpotence index grows
with N and its contribution has not been proved negligible.
The source family is therefore an exact input for the required
singular/nonlocal geometric comparison, not that comparison itself.

The [audit](../experiments/audit_actual_source_fourier_twisted_traces.py)
and [saved results](../experiments/actual_source_fourier_twisted_traces_results.json)
check seven levels N=2,...,8, all basis relative-line compressions,
twisted cyclicity, sector inverses, exact norm equations, the sharp
zero-sector nilpotence index, and the common-frame ORIGINAL source
on six signed words of braid indices two, three and four. The
noninvariance and E-commutation witnesses use literal original
crossing matrices and pivots, not replacement traces.

