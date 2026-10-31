# Original crossing layers: a punctured Casimir norm torus and its parabolic limit

30 October 2026. This is derived from the ACTUAL
homogeneous root crossing kernel and its coefficient composition.
It solves the local classical transport for every integer power.
It does not prove a selected finite-cycle contribution, a kernel norm
bound, a knot A-polynomial identification or a filled-volume limit.

Throughout N>=3,d=N-1,q=exp(pi i/N), hbar=2pi i/N. Fix the original
outer face variables x,y and put A=x+y,P=xy,f(z)=(z+x)(z+y).
The letters P and sigma below are not new quantum parameters.
The generic algebra is over characteristic zero with xyA nonzero;
all source divisors explicitly recorded below remain excluded.

## 1. The exact original kernels and their composition

The [frozen homogeneous theorem](actual_homogeneous_casimir_face_source.md) gives the original coupon polynomial
H_F(x,b,c,y), homogeneous of degree d. For literal polynomials F,G
in the SAME pair Casimir, including their full repeated-node data,

    H_FG(x,b,c,y)=[z^d] H_F(x,b,z,y) H_G(x,z,c,y).          (1)

Indeed H_G is the matrix of G on input monomials c^j, and H_F is
the matrix of F on their output powers z^j. The coefficient condition
t_left+i_right=d is exactly matrix multiplication. There is no extra
N or mark factor in (1). If F,G are at different original ports,
(1) does NOT assert that they commute or share one Casimir.

For epsilon=+/-1 the full original crossing is
R^epsilon=lambda0^epsilon r_N^epsilon(Omega),
lambda0=q^(d^2/2), with the original square-root lift. The normalized
homogeneous coefficient at x^k b^i y^l c^t, i+k+l+t=d, is exactly

    (-1)^(k+l+1) q^[epsilon(kl-(i+1)(t+1))]
                          N/(S_i S_k S_l S_t).         (2)

No Hermite derivative has been replaced by nodal values. Formula(1)
therefore gives R^n with its EXACT lambda0^n for every integer n,
including negative n. All original cups, caps, physical endpoint
zeros and marked face targets remain those of the homogeneous theorem.

Write normalized simplex variables I,K,L,T with sum1 in the leading
limit. The principal phase of (2), INCLUDING lambda0, is

    E_simplex + I Log b+K Log x+L Log y+T Log c
       +pi i(K+L)+epsilon pi i(KL-IT)+epsilon pi i/2.  (3)

Here E_simplex=(Lambda(pi I)+Lambda(pi K)+Lambda(pi L)
+Lambda(pi T))/pi on its recorded continuation. The finite source is
still (2), with i+k+l+t=N-1; its order-one phases and finite offsets
are not discarded by using (3) for a principal characteristic.

## 2. Both signs and the actual input/output convention

At a regular critical point of (3) put
E_I=exp(2pi i epsilon I), and similarly E_K,E_L,E_T.
Taking the three constrained differences of derivatives gives

    E_I^-1=1-b v, E_K=1+x v,
    E_L=1+y v, E_T^-1=1-c v.

For either sign, exp(pi i epsilon)=-1 and the actual linear sign in
(3) is exp(pi i)=-1. Thus the same equations hold; no epsilon-dependent
integer character has been silently changed. Product E_I E_K E_L E_T=1
implies

    v[(x+y+b+c)+(xy-bc)v]=0.

The v=0 branch has all sine factors zero and is excluded from the
regular critical chart. Consequently, with D=P-bc and L0=A+b+c,

    E_I=D/f(b), E_T=D/f(c),
    E_K=-(x+b)(x+c)/D, E_L=-(y+b)(y+c)/D.                (4)

The recorded regular open set is

    xybc D f(b)f(c)L0 !=0.                              (5)

In particular every E_j-1 remains nonzero. These are exponentiated
critical equations, not a claim selecting logarithms or an integration
chain. The linear signs and lambda0 are still present in (2),(3).

The homogeneous kernel has LEFT output b, RIGHT input c. The actual
coefficient target in (1) is degree d, hence the principal gluing law
is T_left+I_right=1, NOT zero. Use the momentum
r=exp(2pi i I) at the left face; the matching right momentum is
r'=exp(-2pi i T). Then the coefficient/pullback advance from left to
right is

    F_+(b,r)=(c,r'), c=[P-r f(b)]/b,
                         r'=f(c)/(P-bc),
    F_-(b,r)=(c,r'), c=[P-f(b)/r]/b,
                         r'=(P-bc)/f(c).             (6)

Direct substitution proves F_-=F_+^-1. Thus inverse crossings have
opposite canonical transport. If the kernel is viewed instead as a
map FROM its input phase point TO its output, the displayed advance
is reversed. This is an orientation convention, not a new inverse
crossing. The exact R R^-1 coefficient contraction is H_1.

For equal signs in two successive layers, (4) and the target give

    (P-bz)(P-zc)=f(z)^2.                               (7)

For opposite signs they give b=c on the regular chart, as required
by (6). A cancelled pair can have a nonisolated middle critical
variable; the finite identity is (1), not a claim about a Gaussian
saddle of that identity kernel.

## 3. The invariant is the principal original Casimir

The original face operator T has principal symbol

    T(b,r)=-(r+r^-1)+(2-r-r^-1)(A/b+P/b^2).

Since the actual Casimir is Omega=-T, its symbol is

    sigma=2+[(r-1)^2/r] f(b)/b^2.

Insert r=(P-bz)/f(b) (or its reciprocal for the inverse sign):

    sigma=2+(b+z+A)^2/(P-bz).                           (8)

This is the actual conserved pair Casimir, not a chosen first integral
of an unrelated recurrence. On (7), putting d1=P-bz,d2=P-zc and
f=f(z), the relation d1d2=f^2 gives

    (b+z+A)^2/d1=(f-d1)^2/(z^2d1)
                  =(d1+d2-2f)/z^2
                  =(z+c+A)^2/d2.

Hence sigma is preserved, and (7) becomes EXACTLY

    c=-sigma z-b-2A.                                  (9)

Conversely (8),(9) imply (7) wherever the recorded units hold.
Thus the full local layer sequence obeys

    b_(j+1)+sigma b_j+b_(j-1)+2A=0.

Here and in (10), (b,z) denotes the POSITIVE companion chart on
the common phase space: z=[P-r f(b)]/b. A negative crossing acts
by the inverse of this map, rather than silently reusing its actual
negative-layer right neighbor as that positive companion coordinate.
All integer powers are powers of the one affine matrix

    M_sigma=[[0,1,0],[-1,-sigma,-2A],[0,0,1]],
    (b_j,b_(j+1),1)^t=M_sigma^j(b_0,b_1,1)^t.           (10)

Its determinant is1, so this includes negative powers. It is one
formula for arbitrary fixed signed twist lengths, not a recurrence
established by checking finitely many powers.

## 4. Explicit norm-one coordinate and the source punctures

The fixed-Casimir conic is

    b^2+z^2+sigma bz+2A(b+z)+A^2-(sigma-2)P=0.          (11)

Assume sigma^2!=4 and
C0=(sigma-2)[P-A^2/(sigma+2)] !=0. Put

    u=b+2A/(sigma+2), v=z+2A/(sigma+2),
    lambda^2+sigma lambda+1=0.

Then

    (u-lambda v)(u-lambda^-1 v)=C0.                    (12)

The involution is lambda<->lambda^-1. The conic is a torsor for the
norm-one group of this quadratic spectral algebra, and the actual
map (9) multiplies the first factor by lambda and the second by
lambda^-1. In particular it is diagonal after this spectral cover.
There is even an explicit norm trivialization:

    w=((lambda+1)/(lambda-1))*(x+lambda y),
    Norm(w)=C0,
    a=(u-lambda v)/w, Norm(a)=1, a ->lambda a.           (13)

To verify the norm, use
Norm((lambda+1)/(lambda-1))=-(sigma-2)/(sigma+2) and
Norm(x+lambda y)=x^2-sigma xy+y^2. Both factors are units under the
stated generic hypotheses. The inverse crossing gives a->lambda^-1 a
in the same phase-space convention (6). Thus arbitrary signed powers
are explicit multiplication by lambda^n.

The reference point a=1 is b=-x,z=-y. It lies on EVERY conic, but is
an EXCLUDED SOURCE POINT: P-bz=0, f(b)=f(z)=0. Thus (13) is an
algebraic norm trivialization; it does not make the actual source
regular at its reference point. On the spectral cover,

    u=[lambda bar(w)/a-lambda^-1 w a]/(lambda-lambda^-1),
    v=[bar(w)/a-w a]/(lambda-lambda^-1).

The regular SOURCE STATIONARY chart is the complement of (5) after
this substitution. These are divisors of that classical critical
chart, not new poles of the finite homogeneous polynomial H_R. In particular the possibly coincident basepoints b,z=(-x,-y),(-y,-x)
have norm coordinates 1 and (y+lambda x)/(x+lambda y). Their adjacent
lambda and lambda^-1 translates give the f(b) and f(z) zeros. The
b=0,z=0 divisors are retained too. A word analyzed in this regular critical chart must retain the
preimages of these divisors under ALL its intermediate powers.
Transport of the completed algebraic conic is not permission to
move the original source contour through them.

## 5. Exact Darboux factor and existing quantum Gaussian

For this coordinate calculation always use the POSITIVE companion
z=[P-r f(b)]/b as a rational coordinate on the common phase space,
regardless of the sign of the next actual crossing. Then, for fixed
x,y, the actual cotangent two-form is

    omega=dLog r wedge dLog b=db wedge dz/(P-bz).

Let F be the left side of (11) and eta=u-lambda v. Then

    d sigma=(F_b db+F_z dz)/(P-bz),
    lambda F_b+F_z=(lambda-lambda^-1)eta,
    d sigma=-(lambda-lambda^-1)dLog lambda.

These imply, with NO factor2 or sign ambiguity,

    omega=dLog lambda wedge dLog eta
      =dLog lambda wedge dLog a.                   (14)

The scalar w depends only on lambda at fixed x,y and thus contributes
zero to the wedge. With the explicit convention i_X omega=-dH,
H=(Log lambda)^2/2 generates the displayed pullback advance
a->lambda a. This agrees with (6); the opposite input-to-output
interpretation reverses that map.

This recovers an explicit classical coordinate for the EXISTING
full-Hermite Gaussian functional calculus, rather than replacing it.
The [existing Gaussian theorem](actual_coherent_filling_gaussian_chirp.md), section1, proves
R^(2P)=q^(P d^2/2) exp[P K(Omega)/hbar], where
K(sigma)=arccosh(-sigma/2)^2 is analytic off[2,infinity) with its
removable value at sigma=-2. The same node and derivative check gives
for every integer n

    R^n=q^(n d^2/4) exp[n K(Omega)/(2hbar)].             (15)

Indeed at c_j=q^(2j+1)+q^(-2j-1), with x_j=pi i(2j+1)/N,
K(c_j)=(x_j-pi i)^2, and the actual normalized crossing value is
nu_j=exp[pi i(j^2-dj)/N]. This uses (-1)^j=exp(-pi i j), the
unwrapped sign required by the original derivative. The derivative
of the exponential at the node is the literal multiplier
-n(d-2j)/[2(q^(2j+1)-q^(-2j-1))]; paired nodes retain this derivative,
and the odd simple node needs no quotient0/0. Values and derivatives
therefore agree in the full Casimir quotient. Negative n are allowed
because all crossing eigenvalues are units.

On the classical spectral cover K=(Log lambda)^2, so (14),(15) give
the same Hamiltonian, with the recorded scalar factors unchanged.
The finite ratio nu_(j+1)/nu_j=-q^(2j+2) has principal limit
lambda=-exp(2pi i j/N), a root of lambda^2+sigma lambda+1=0.
Its extra finite q shift is not dropped from (15) or from the kernels.
Neither the unit-modulus node values nor the torus action bounds the
full quantum operator or its shared-face coefficient.

## 6. The two endpoint fibers are different

At sigma=-2, with A!=0, the original conic is the reduced parabola

    (b-z)^2+2A(b+z)+A^2+4P=0.

Put t=b-z. Then the actual affine map gives t->t+2A, and

    b=-[(t-A)^2+4P]/(4A), z=-[(t+A)^2+4P]/(4A).

The affine matrix M_-2 satisfies (M_-2-I)^3=0, and its square is
nonzero when A!=0. Thus

    M_-2^n=I+n(M_-2-I)+n(n-1)(M_-2-I)^2/2              (16)

for EVERY integer n. This is concrete nilpotent/unipotent classical
transport at the parabolic Casimir, with quadratic face dependence.
It does not imply polynomial growth of an original quantum period.

At sigma=+2 the SCHEME (11) is the nonreduced double line

    (b+z+A)^2=0.

Its reduced line has z=-b-A and the map is the involution (b,z)->(z,b).
The full affine matrix retains its Jordan data: (M_2+I)^2(M_2-I)=0.
Explicitly, if e=b+z+A with e^2=0, then
M_2^2(b,z)=(b-2e,z+2e). Thus the reduction loses a real normal
transport even though it is an involution on ordinary points.
Do not call this fiber the same additive torsor as sigma=-2, and do
not replace the double-line scheme by its reduction when retaining
normal data. The regular one-layer critical chart excludes the
reduced line because L0=0. This is a degeneration of the closure.

For sigma^2!=4 but C0=0, (12) is a pair of lines rather than a norm-one
torsor. Formula(10) still gives exact algebraic transport. The generic
torus theorem does not assert that this reducible fiber is nonsingular.

## 7. Existing repository scope and the remaining source question

The repository already has exact full-Hermite Gaussian powers in
[the Gaussian source note](actual_coherent_filling_gaussian_chirp.md) and its Fourier-Hermite
source dependencies. It also has [the uniform group-relator note](uniform_twist_relator_source.md),
sections1--2: a quadratic norm group for the TWIST-KNOT GROUP RELATOR
w^k, explicitly not the original quantum crossing-source torsor.
The [intrinsic quantum-A norm-torsor](intrinsic_quantum_a_norm_torsor.md) construction is a different
cyclic quantum-A norm group. None of those statements is being
reproved or relabeled as this local theorem. A focused search of the
current notes found no displayed source-face conic (11) or the
coefficient-layer recurrence (9).

The additional interface here is the explicit original R-layer
critical relation, its preserved ACTUAL pair Casimir, signed inverse
conventions, norm coordinate, source punctures, and two distinct
parabolic endpoint schemes. It holds at a local port independently
of bridge width. Whole networks still require their original shared
face targets, exterior phases and mark. No eliminated knot variety,
period contribution, or volume estimate follows just from this
algebraic linearization. No literature novelty claim is made.

Coverage only: [Goldman, The complex-symplectic geometry of
SL(2,C)-characters over surfaces](https://math.umd.edu/~wmg/csymp.pdf),
PDF dated2 September2003, Proposition2.6.1 and sections2.6.1--2.6.2,
already relates Dehn twists to Hamiltonian trace flows and distinguishes
generic multiplicative from noncentral parabolic additive orbits.
The [arXiv record](https://arxiv.org/abs/math/0304307v2) is version2,
3 October2003. Those statements are coverage context, not inputs to
this proof. The present conic has not thereby been identified with
that surface character variety; multiplicative/additive twist dynamics
is not being claimed as new in itself.

## 8. Verification scope

The [focused exact audit](../experiments/audit_actual_crossing_casimir_torus.py),
with [saved results](../experiments/actual_crossing_casimir_torus_results.json),
checks 14 symbolic identities, 450 signed-integer torus steps, 866
inverse-chart checks, 20 excluded reference points and 180 parabolic
or reduced-endpoint steps. It independently compares 28 original
integer crossing powers, including identity cases, on 3,024 physical
entries and 966 wrong-unwrapped-total zeros. Twelve mixed inverse
compositions, 70 exact Gaussian node VALUES and 14 adjacent spectral
ratios retain all displayed scalar phases. The full-Hermite Gaussian
DERIVATIVE assertion is the analytical node-and-derivative proof in
section5 and its existing source theorem; these 70 value checks are
not advertised as an independent numerical derivative audit.

The crossing-Casimir torsor does not determine a quantum norm, a selected finite-cycle contribution or a long-filled volume estimate.