# Relative framing transgression and the literal finite cut projector

Research note, 27 October 2026. This constructs an explicit relative
boundary complex whose source and co-source are the original finite
cut projector e and marked defect D. The marked meridian supplies
the relative fiber endpoints; no Haar-volume division is introduced.
There are two exact presentations: an intrinsic finite-root residue
model and a smaller logarithmic residue model using the original
canonical representatives. Their chain projection is literally e.

This realizes the finite boundary source. It does not identify the
internal quantum pushforward with the geometric Gaussian framing
pushforward. In particular it does not prove survival of the geometric
block in the selected global period or the volume conjecture.

## 1. The classical form needs a relative source

At the complete meridian M=1, use the original framing chart

    Omega_cut=-dr wedge ds/[s(1+s)],
    V=s partial_r, A=1/(1+s), t=r/s.

Then V=partial_t and

    beta=dlog A=-ds/(1+s),
    Omega_cut=dt wedge beta,
    iota_V Omega_cut=beta.                       (1.1)

The ordinary two-form is exact: Omega_cut=d(t beta). This primitive
is not harmless for a relative source, because its endpoint values
are different.

The relative endpoints have a marked geometric meaning. The regular
meridian centralizer in the existing note is
C_b=[1+kappa*b b;0 1], with kappa=M-M^(-1), and its action at M=1
is r->r+b s. The meridian itself is the centralizer section b=M,
so at M=1 it translates t to t+1. A choice of initial framing section
therefore gives the relative pair t=0,t=1. Replacing that section by
t_0(A) translates both endpoints together. Since
(dt-dt_0) wedge beta=dt wedge beta, the transgressed source below
is independent of this choice on its invariant forms whenever the
section change is regular on the retained source chart. A section
with a pole at an added root requires its own boundary lattice data;
no extension through that pole is inferred here.

The geometric invertible-framing chart has s!=0, so A!=1. For the
finite cut source we use the explicit extension

    F_tilde=A^1_t times G_m,A.

It agrees with the framing chart at A!=1. Its added A=1 divisor is
boundary source data, not an assertion that the original geometric
frame remains invertible there.

The generic meridian has a further marked period which must not be
silently replaced by one. At fixed M, t=r/s gives

    Omega_cut=[dt/(1+kappa*t)] wedge dlog A,
    A=M/(M+s), V=(1+kappa*t)partial_t.

The meridian sends t=0 to t=M. On its specified local logarithmic
branch its relative centralizer period is

    L(M)=integral_0^M dt/(1+kappa*t)
         =Log(M^2)/kappa, L(1)=1.              (1.2)

This is a marked regular period, not a rational function. The
centralizer power adapter already proved in the existing note gives

    L(M^N)=[N/u_N(M)]L(M),
    u_N(M)=(M^N-M^(-N))/(M-M^(-1)).              (1.3)

Indeed the adapted power map is
t'=[(1+kappa*t)^N-1]/(kappa*u_N), and it pulls back the invariant
differential to (N/u_N)dt/(1+kappa*t). Formula (1.3) retains exactly
the actual modified-dimension factor 1/u_N. The generic centralizer
also has an absolute multiplicative cycle, absent in the additive
fiber. We do not identify its entire generic relative de Rham group
with the polynomial additive resolution below. The finite source
coefficients themselves retain their full M dependence throughout.

## 2. A relative complex with an explicit contraction

For any characteristic-zero vector space E define a two-term complex

    R(E)^1=E[t],
    R(E)^2=E[t] direct_sum E direct_sum E,
    delta h=(partial_t h,h(0),h(1)).             (2.1)

All other degrees are zero. Define

    L(a,b_0,b_1)=integral_0^1 a(t)dt-b_1+b_0,
    i(f)=(f,0,0).                               (2.2)

The integral is polynomial antiderivation over a characteristic-zero
field; no analytic convergence or contour choice is used. We have
L delta=0 and L i=I. Moreover the explicit degree-minus-one map

    H(a,b_0,b_1)(t)
       =b_0+integral_0^t [a(u)-L(a,b_0,b_1)]du  (2.3)

satisfies delta H+H delta=I-iL. Therefore

    H^1 R(E)=0, H^2 R(E)=E, R(E) equivalent to E[-2]. (2.4)

Every linear map E->E' acts coefficientwise on this complex and
commutes with delta,L,i,H. This naturality will retain every actual
finite quantum matrix, source and cut.

Geometrically, (2.1) is the relative de Rham complex along t=0,1
after taking a residue quotient in the A direction. A pair of the
form (a(t)dt wedge omega,b_0 omega,b_1 omega) represents its degree
two element, where omega is the chosen logarithmic normal form.
The relative differential is (d omega,restriction omega-d eta).
It gives precisely (2.1). The transgression is (2.2).

In particular (dt wedge beta,0,0) gives a nonzero relative class:
its image is beta. The ordinary primitive t beta has endpoint pair
(0,beta), so its relative coboundary is
(dt wedge beta,0,beta), whose transgression vanishes. Ordinary
exactness does not kill the sourced relative class.

## 3. The intrinsic finite-root residue realization

Fix the actual N>=2 and Q primitive of order N, over a field k
containing its roots. Let

    C_N=k[A,A^(-1)]/(A^N-1),
    D_N={A^N=1},
    omega_N=A^(N-1)dA/(A^N-1)
                       =(1/N)dlog(A^N-1).       (3.1)

On F_tilde take logarithmic forms along A^1_t times D_N modulo
forms regular along that divisor, and take their relative cone for
t=0,1. The quotient has terms C_N[t] omega_N in degree one and
C_N[t] dt wedge omega_N in degree two; differentiation is partial_t.
Its relative complex is exactly R(C_N).

The actual state f in C_N is the class i(f). Its cut functional is

    Phi_N(a,b_0,b_1)=(1/N)Tr_(C_N/k) L(a,b_0,b_1). (3.2)

To see its literal residue meaning, first transgress in t and then
sum residues at the N points of D_N. At A=Q^j,

    Res_(A=Q^j) f omega_N=f(Q^j)/N.

Thus for an actual boundary vector f,

    Phi_N i(f)=(1/N)sum_(j=0)^(N-1) f(Q^j)
                       =phi_N(f),              (3.3)

the original balanced co-source. This is intrinsic to the finite
algebra: replacing a representative by (A^N-1)g changes its form
by one regular at D_N, hence changes no residue class.

For a whole normal family retain U and use
C_U=k[U,U^(-1),A]/(A^N-U). If f is regular at U=1, then

    Tr_dR(f dlog A)=(Tr f/N)dlog U,
    Tr_dR(f omega_N)=(Tr f/N)dlog(U-1),
    Res_(U=1)Tr_dR(f omega_N)=phi_N(f|_(U=1)). (3.4)

Here omega_N is pulled back as (1/N)dlog(U-1). The factor U-1
is retained before specialization. Equation (3.4) is also a direct
trace/residue realization of the source's normal direction.

## 4. The logarithmic zero-residue source and the exact projector

Let R(k) be the same relative complex with logarithmic normal form
beta=dA/A along the added A=0 source boundary of the A-line. This
added boundary is not a new geometric critical point. For a finite
state use its original canonical
representative

    f_tilde(A)=sum_(j=0)^(N-1) f_j A^j.

Transgression followed by Res_(A=0) sends
(dt wedge f_tilde beta,0,0) to f_0. Root orthogonality gives

    f_0=phi_N(f).                                (4.1)

Thus the original canonical representative defines a strict cochain
map R(C_N)->R(k), applying phi_N to every coefficient. Its section
R(k)->R(C_N) applies the constant vector psi=1. Their composition
on R(C_N) is the coefficientwise chain map

    e=psi phi_N=(1/N)sum_(j=0)^(N-1) S^j,
    S f(A)=f(QA).                               (4.2)

This is the literal original finite cut projector, not just a map
with the same scalar norm. In the evaluation basis A=Q^a, its
matrix has every entry 1/N. It has rank one and e^2=e on H^2.
The averaging identity and idempotence also hold strictly on the
two-term resolution; rank one here refers to its finite H^2.

The two residue presentations agree by (3.3)--(4.1). They are not
an identification of their unweighted ambient differential forms.
In the D_N residue model the appropriate normal source is

    omega_N=[A^N/(A^N-1)] beta.                  (4.3)

The unweighted beta is regular along D_N and has zero image in
that particular quotient. In the A=0 model beta already is its
logarithmic source. The chain map in (4.2), with the prescribed
canonical representatives, is the exact comparison between them.
Neither formula permits evaluating the source's pole first and
then discarding its normal class.

## 5. The original pivot and marked defect lift unchanged

In the same balanced evaluation basis, the original pivot is

    g(A)=x^(1-N)A^(-1), x=-M/q.

This section first works in C_N, where A^N=1, so the displayed
formula equals the literal power K^(1-N) for K=xA^(-1).

Multiplication by g and g^(-1) gives coefficientwise chain maps
on R(C_N). Define

    D=g^(-1)e.                                  (5.1)

Then on H^2, identified with the original color space, and also
coefficientwise on its resolution,

    gD=e, D^2=0, DgD=D, Tr_(H^2)(gD)=1.         (5.2)

Indeed phi_N(g^(-1))=x^(N-1)phi_N(A)=0 for N>=2. In the
evaluation basis (5.1) has the original matrix
D_(a,b)=x^(N-1)Q^a/N. For every finite cut matrix C,

    Tr_(H^2)(g D C)=Tr_(C_N)(e C)
                            =phi_N(C psi).      (5.3)

Every such C lifts coefficientwise and commutes with the explicit
relative contraction (2.3). Hence arbitrary finite internal matrix
composition and contraction commute with this boundary realization.
The same applies when tensoring the cut leg with the remaining
finite color spaces. This is exact finite linear algebra at every
level, not a semiclassical or knot-by-knot assertion.

The marked defect is still not an ordinary Hopf-intertwining coupon.
This lift does not authorize moving D unchanged through a crossing.
The whole full-ADO factor d_N(M), with its phase, pole, residue and
normal jet, remains a separate marked line multiplying (5.3). In
particular the 1/N from the cut source and the value eta_N/N of
the modified dimension at completeness are distinct normalizations.

For a whole C_U normal extension, one must distinguish the reduced
representative g_red=x^(1-N)A^(-1) from the literal clock power
g_lit=(xA^(-1))^(1-N)=U g_red. Their defects are respectively
D_red=g_red^(-1)e and D_lit=U^(-1)D_red. Both products equal e,
so the cut comparisons above remain exact. Their physical normal
derivatives do differ: D_phys g_red=-g_red, while
D_phys g_lit=(N-1)g_lit, with opposite rates for the two defects.
Thus the U adapter is retained whenever a normal pivot jet is
compared; a coefficientwise root representative is not relabeled
as the literal clock power away from U=1. See the exact
[Mellin lift comparison](fock_cyclic_normal_mellin_map.md), Section 2.

## 6. The representative carry and deleted-root obstruction remain

The map (4.1) is linear and is not an algebra map. Canonical
representatives satisfy the actual carry identity

    A f_tilde-(Af)_tilde=f_(N-1)(A^N-1).         (6.1)

In particular phi_N(Af)=f_(N-1), although Res_(A=0) A f_tilde beta
is zero. Taking f=A^(N-1) gives phi_N(Af)=1 while
phi_N(A)phi_N(f)=0. Thus the zero-residue source is compatible
with multiplication only through the retained canonical carry.
With U retained, its term is U f_(N-1); no normal source is removed.

The open geometric framing chart A!=1 also cannot by itself carry
the whole finite cut. The idempotent

    epsilon_1=(1/N)sum_(j=0)^(N-1) A^j

is killed by localization at A-1 but satisfies phi_N(epsilon_1)=1/N.
Thus phi_N does not descend through C_N->C_N[(A-1)^(-1)]. This
is a precise source obstruction to deleting the excluded framing
point. It is distinct from the projector e in (4.2), although both
involve a finite average. Epsilon_1 is multiplication by one root's
idempotent; e is averaging the shift and has constant image.

There is now a precise repair after adjoining the actual matrix
Ward differential. The [source localization theorem](ward_source_localization.md)
replaces the boundary representative by

    P=1-epsilon_1, e_S=[N/(N-1)]P e P.

Its matrix cut row has the same Ward class as the original cut,
while its color co-source factors through A-1 localization. An
explicit chain retraction and homotopy extend this comparison to
the combined relative-Ward complex. With U retained, the deleted
branch is marked by alpha(U)^N=U, alpha(1)=1, and removed as a
whole regular idempotent summand; every normal carry is retained.
The original color co-source's obstruction above remains valid
on R(C_N) alone. The repair uses Ward currents and changes its
representative with the exact factor N/(N-1).

This is a boundary comparison. Compressing two internal operators
separately omits the excursion L C(I-P)D J, so the theorem does not
authorize deletion inside crossings or an internal geometric
Gaussian comparison without those additional currents.

## 7. What is still needed for the internal geometric pushforward

This gives a concrete relative boundary object, explicit chain
projection and contraction, and literal realizations of psi,phi,e,D.
The marked meridian rather than an arbitrary group volume supplies
its relative centralizer interval. Absolute exactness of the
classical framing form is therefore not by itself a vanishing
argument for a source-compatible relative period.

The finite boundary resolution is natural for every actual matrix,
so ordinary finite internal elimination respects it. Its auxiliary
relative coordinate t is not thereby identified with the zero mode
r/s produced by the internal semiclassical Gaussian pushforward.
Constructing that comparison, including (6.1), the missing root
idempotent, and the normal divisor (4.3), remains necessary.

In particular a constant geometric principal density would have
nonzero image under this relative functional if the internal
pushforward were proved to give this class. The boundary model
does not prove that premise or select a global thimble. It supplies
the explicit cochain target and the exact source defects that the
missing map must transport.

### Finite contraction and formal Gaussian reduction are different maps

The exact naturality statement is the commuting finite diagram

    R(C_N) tensor V_rest  --lift(C)--> R(C_N) tensor V_rest
            | L                              | L
            v                                v
       C_N tensor V_rest    --C-->       C_N tensor V_rest,

with the analogous inclusion and explicit homotopy. Thus actual whole
finite internal contraction really does induce a chain map on this
boundary resolution. What has not been constructed is a comparison
from this diagram to the formal Gaussian normal module at a geometric
critical representation, sending the auxiliary relative t to its
internal framing zero mode r/s and intertwining the canonical carry.

There is a concrete failure of the naive source map. The functions
A^N and one are equal in C_N, whereas

    Res_(A=0) A^N dlog A=0,
    Res_(A=0) dlog A=1.                         (7.1)

Consequently unreduced rational framing functions followed by the
ordinary zero residue do not define a map out of the finite cut
algebra. Canonical reduction, or its full normal-U source, must
precede that operation. On the actual q trajectory h=Log Q,
N=2pi*i/h, this lost character is

    A^N=exp((2pi*i/h)Log A).

It is not a coefficientwise formal unit in h at a fixed classical
shape. A local formal Gaussian contraction does not automatically
transport its finite-root relation to one. The meromorphic extension
of the principal framing two-form alone does not repair (7.1).

Hence the present result establishes a compatible nonzero relative
principal class and an exact finite source resolution. Calling it
an actual nonzero *selected geometric formal summand* would require
the additional commuting microlocal/source map just described.
No such summand or global selected thimble is inferred here.

[Exact audit](../experiments/audit_relative_framing_source.py).
[Results](../experiments/relative_framing_source_results.json).
