# The complete crossing Green source has explicit ground and carry endpoints

28 October 2026. The exact two-Newton/one-Rogers crossing layer
gives a coupled source equation normal to its geometric holonomy.
After the original physical finite boundary restrictions, its entire
right side is explicit: a ground-output block, a ground-input block,
and one rank-one carry on pair degree N. Its original cup/marked-cap
value is the nonzero known number (Q(N-1)-1)/N, with the same external
Cartan line retained.

This is an inhomogeneous source theorem, not a claim that the currents
vanish. It also computes the exact shared full-Psi face fusion and
the remaining one-function Fourier kernel. The original relative
Fourier cycle is not replaced by a standard real contour.

Subsequent constructive resolution of the LOCAL comparison:
[the balanced finite Fourier kernel](actual_balanced_fourier_crossing_kernel.md)
uses an adaptive internal Fermat orbit and independent external
finite frames. All three source norms then vanish on that actual
sampling map, and an original E-current proves its four-full-Psi
kernel is EXACTLY the original crossing operator. Its uniform local
density is nonzero and polynomial. The global sewn source and
geometric noncancellation remain separate.

## 1. The actual positive crossing and paired Ward source

Use the [proved physical crossing layer](actual_trivalent_layer_crossing_source.md).
Let z_0,z_1 be the original inputs, z_6,z_7 the outputs, and t its
remaining internal variable. Put

    u=t/z_1, v=x^(-1)t/z_0,
    f=x^(-1)z_7/z_6, r=z_6/z_0, w=x^(-1)z_6/t,
    B_0(t)=B_N(u,v), F(w)=B_N(f,fw)R_N(r,w).

Then the original normalized positive core is the physical finite
block of CT_t B_0F, with its final original Hardy barrier. Its
common kappa, writhe/peripheral line and original source are unchanged.
All statements below are at the original fixed Q root for the whole
nonzero color x family unless completeness is explicitly specified.

Define the exact central sources

    D_0=1-u^N+v^N,
    D_B=1-f^N+f^Nw^N,
    D_R=1-r^N-w^N.

The finite Newton and Rogers recurrences give the FULL paired Ward

    F(w)-fr F(Qw)=H_pair(w),
    H_pair=D_B R_N(r,w)+f D_R B_N(f,Qfw).                  (1)

This is a polynomial identity, with every source endpoint retained.
In particular D_B+f^N D_R=1-(fr)^N is a boundary norm identity,
not a reason to discard both currents.

## 2. A source Green equation for the complete crossing

Multiply (1) by v B_0(t), integrate the COMPLETE polynomial CT,
and reindex t->Qt in its shifted term. The simultaneous-Q source
recurrence is

    v B_0(Qt)=(u-1)B_0(t)+D_0.

Because v(Qt)=Qv(t), the result is exactly

    CT_t[(v-Qfr(u-1))B_0F]
       =CT_t[v B_0 H_pair]+Qfr CT_t[D_0F].                (2)

The original q factor in the reindexing is compulsory. Its left
coefficient is the bounded-degree LINEAR polynomial

    v-Qfr(u-1)=x^(-1)/z_0
                       [t(1-Qz_7/z_1)+Qz_7].            (3)

At Q=1 its zero is precisely the regular stationary gluing equation
of the all-homogeneous Fourier kernel in Section 5. Thus (2) is an
actual sourced quantum normal equation, without localizing a
nilpotent face or dividing by an unknown period.

Equation (2) holds before restricting any boundary coefficient.
Apply the SAME original finite input/output boundary blocks to both
sides. Below L denotes this physical block of its left side. This
restriction is important for boundary monomials which can shift a
physical output past its original top; it is not an additional reset
inserted into one separated source sector.

## 3. Exact finite endpoint filtration

Write d=N-1, F_a=(Q;Q)_a and
p_j=(-1)^jQ^(j(j-1)/2)/F_j. On original input |a,b>,
0<=a,b<N, the physical form of (2) is

    L=G_out+G_top+G_in.                                    (4)

The ground-SECOND-INPUT term is particularly simple:

    G_in|a,b>=delta_(b,0) Q sum_(e=1)^a
                                      x^(-e)|a-e,e>.       (5)

It has rank N-1. To prove it, the two nonconstant terms of
D_0 demand an incoming index at least N, and vanish on the
original finite inputs. The constant term gives
CT F=K_N(f)K_N(r). Multiplication by Qfr and the actual
finite boundary block yields exactly (5). In particular the
D_0F term is NOT zero.

The ground-SECOND-OUTPUT block has rank at most N-1:

    G_out|a,b>=0 unless a>=1 and a+b<N,

    G_out|a,b>=x^(-b-2) F_(a+b)/F_b
       *sum_(j=0)^(a-1)
         p_j x^(-2j)/[F_(a-j-1)(1-Q^(b+j+1))]
       *|a+b,0>.                                          (6)

All denominators in (6) are original nonzero factorial units:
b+j+1<=a+b<N. No singular determinant is inverted.

The remaining term is one rank-one carry on pair degree N:

    G_top|a,b>=0 unless b=N-a, 1<=a<N,

    G_top|a,N-a>=-x^(-N-a) F_d/F_(N-a) p_(a-1)
                 *sum_(e=1)^d x^(-e)|N-e,e>.              (7)

The rank is one because the output vector in (7) is fixed and
nonzero. It is not a rank-one assertion about the whole Green
operator or about an arbitrary crossing.

Here is a direct proof of the filtration. In the first term
vB_0 D_B R of the right side of (2), the -f^N summand has
negative first output, and the (fw)^N summand has second
output at least N. The original barriers remove both. Its
constant summand has second output zero; coefficient expansion
gives (6).

In the second term vfB_0 D_R B(f,Qfw), the constant summand
has negative first output, and -r^N demands first input at
least N. The -w^N term survives only when the B_0 total
order is EXACTLY d and the V-index of B(f,Qfw) is zero.
The resulting inputs and outputs have total degree N;
their coefficient is precisely (7). This also explains why
multiplying a primitive ground-cell Ward by a monomial may
expose an additional top carry. One must apply the physical
barriers AFTER the specified weighting, not beforehand.

## 4. The original complete cap detects a known nonzero boundary

At completeness x=-q^(-1), Qx^2=1. Keep exactly

    p=N sum_(a=0)^d x^(a-d)|a,d-a>,
    m|c,e>=x^e/N^2,
    mp=1.

Then

    m G_in p=Qd/N,
    m G_top p=0,
    m G_out p=-1/N,
    m Lp=(Qd-1)/N!=0.                                    (8)

The first equality follows immediately from the one surviving
input |d,0> in (5). The second follows because the original
cup has total degree d, while (7) requires degree N.

For the third, reorganize the finite coefficient sum in (6)
by k=b+j+1. Its inner coefficient is

    sum_(b+j=k-1) p_j/F_b=delta_(k,1),

the exact inverse Euler identity U(t)V(t)=1 modulo t^N.
Thus for the same literal vectors at general x this pairing is
-Q^(-1)x^(-2)/N; completeness makes it -1/N. This proves
(8) by finite algebra at EVERY level. The original unstripped
crossing carries its SAME external kappa multiplying this
source value; it has not been reset.

Equation (8) is a concrete boundary normalization of the
actual Green source. It cannot be replaced by an assertion
that every endpoint/current vanishes. It is also not a
global knot lower bound. Transporting the nonintertwining
ground/carry coupons through an arbitrary exterior needs
their actual Ward/source equations; bare cut relocation or
Schur scalarity does not justify that step.

## 5. Shared full-Psi face fusion, with its norm intact

Use the exact, SOURCE-selected Newton and Rogers blocks:

    S_B(u,v)=(N/phi_N)u^N Psi_+(h-Logu)Psi_+(Log(v/u))
                                              exp[-Log(v/u)Logu/h],

    T_R(r,w)=phi_N Psi_-(Logr-h)Psi_-(Logw-h)
                                              exp[-Logr Logw/h].

The latter is the proved [opposite-root Rogers source](actual_rogers_sink_opposite_beta_source.md).
It is NOT obtained by substituting the balanced norm r^Nw^N
off its balancing divisor. Its equivalent plus-oriented form
contains (1-r^N)(1-w^N).

Put

    A=Logz_0, B=Logz_1, C=Logz_6, D=Logz_7, X=Logx,
    tau=Logt,
    beta=B-A-X, f_log=D-C-X,
    rho=C-A, sigma=C-tau-X, l_u=tau-B.

The shared face sewing is EXACTLY

    Psi_-(sigma-h)Psi_+(sigma)=1-exp(Nsigma),               (9)

not one. Therefore the complete all-homogeneous product is

    S_B(u,v)T_R(r,w)S_B(f,fw)
       =(N^2/phi_N)(uf)^N(1-r^N)(1-w^N)
         *Psi_+(h-l_u)Psi_+(beta)Psi_+(h-f_log)/Psi_+(rho)
         *exp[-(beta*l_u+sigma*(f_log+rho))/h].             (10)

All four remaining full functions and both central norm
factors are explicit. Since f_log+rho=D-A-X, its internal
tau dependence separates as

    boundary_constant *(1-(x^(-1)z_6/t)^N)
       *Psi_+(h+B-tau)
       *exp[(D-B+2pi*i)tau/h].                             (11)

The boundary constant, including phase, is

    (N^2/phi_N)exp[N(f_log-B)](1-r^N)
       *Psi_+(beta)Psi_+(h-f_log)/Psi_+(rho)
       *exp{[beta*B-(C-X)(f_log+rho)]/h}.

In particular the affine 2pi*i*tau term from u^N is retained.
The remaining integral is a one-full-Phi Fourier FUNCTIONAL
with a two-term central source; it is not a bare transform.

The principal growth chambers of the two original local
factors on this face have opposite signs. Their exact sewing
(9) must be done before choosing their joint symbol or
discarding a central factor. Separate local norm-gap
theorems cannot be simultaneously asserted on this shared face.

## 6. A reference Fourier evaluation and the missing cycle equation

For comparison only, the independently proved full-Phi Fourier
formula gives the specified real/shifted Fourier functional

    F_ref(lambda)=1/(2pi*i)integral_GammaF
                                  Psi_+(z)exp(-lambda*z/h)dz

    =zeta_0/(i sqrt(N))
       *exp[i sqrt(N)lambda c_b-iNlambda^2/(4pi)]
       *Psi_+(lambda+2pi*i+h),

    c_b=i(sqrt(N)+1/sqrt(N))/2,
    zeta_0=exp[pi*i(1-4c_b^2)/12].                         (12)

Initially take Im lambda<0 and the common convergent contour
from the [independent Fourier proof](faddeev_pentagon_audit.md).
Elsewhere (12) means its recorded meromorphic continuation.
It retains the exact scalar and the full-function norm.

Its dual step is

    F_ref(lambda-2pi*i)
                         =(1-exp(-Nlambda))F_ref(lambda). (13)

For the field (11), set z=h+B-tau,
lambda=D-B+2pi*i and K=exp[N(C-X-B)]. Its source is the
combination F(lambda)-K F(lambda-2pi*i), up to the explicit
orientation and boundary exponential from that change of variable.
On the REFERENCE Fourier chain this would give multiplier

    1-K+K exp(-Nlambda)
       =1-(x^(-1)z_6/z_1)^N+(x^(-1)z_6/z_7)^N.             (14)

Neither this multiplier nor the one in (9) is silently set
to one. Formula (14) is a genuine reference-chain evaluation,
not an evaluation of the original Cauchy source.

The remaining cycle distinction is exact. Under tau->tau+2pi*i,
the field in (11) has multiplier

    (z_7/z_1)^N[1-(z_1/t)^N],                              (15)

which depends on t. Its original lifted head-circle edge
therefore does NOT close as an independent all-homogeneous
period. The accompanying source currents restore the original
single-valued finite crossing. Identifying this full relative
functional with the reference chain in (12) requires precisely
those current transports. Even its affine lambda mark often
lies outside the initial Fourier convergence chamber; deleting
the 2pi*i shift to reach that chamber would change the source.

## 7. What is now available for global composition

The complete crossing has an actual sourced normal equation
(2)--(3), with every physical endpoint and its nonzero original
cap normalization known in (4)--(8). This is stronger than an
unidentified right side of a transport equation. Its source
terms are restricted ground cells and one degree-N carry.
Their subsequent global transport may be studied with the
original finite-head source and its Ward rules.

One cannot simply remove these terms or declare them smaller:
they have nonzero original source values, and current deck
transport can contain the same geometric block. A proof of
global endpoint induction, or an exact relative Fourier
comparison retaining them, remains required. No global volume
lower bound follows from the reference Fourier formula alone.

The [audit](../experiments/audit_actual_crossing_shared_face_fourier_source.py)
checks ten complete polynomial Ward/Green identities, fourteen
physical color/level endpoint filtrations, the original complete
cup/full marker, original full-pivot word insertions, three exact
shared-face full-function fusions and the reference Fourier dual
step. It keeps the physical barriers AFTER the weighted currents.

## 8. The top carry is a controlled idempotent and a normal Ward source

At completeness the coefficient of (7) simplifies completely:

    F_d/F_(N-a) *p_(a-1)=Q^(1-a).

This is ordinary root-factorial reflection. Put

    w=sum_(e=1)^d x^(-e)|N-e,e>.

Since Qx^2=1, equation (7) becomes

    G_top=-Q w w^t=Q E, E=-w w^t,
    w^t w=-1, E^2=E.                                      (16)

The transpose here is BILINEAR, not a Hermitian adjoint.
Indeed sum_(e=1)^d x^(-2e)=sum_(e=1)^d Q^e=-1.
Thus the carry is not a nilpotent error. Its normalized
rank-one projector has operator norm N-1 in the original
Euclidean metric, since ||w||^2=N-1 and its row has the
same norm. It is polynomially controlled without selecting
an exponentially conditioned full flag basis.

There is also an exact algebra for repeated carry contractions.
Let P_* be the one-head projection onto indices 1,...,d,
and let W be the coefficient matrix of w. Then

    W^2=x^(-N)P_*, x^(-2N)=1,
    E_12 E_23 E_12=E tensor P_*,
    E_23 E_12 E_23=P_* tensor E.                            (17)

To verify the first identity, W has its sole entry in row a
at column N-a, equal to x^(a-N); the two opposite entries
multiply to x^(-N). Expanding three rank-one contractions
uses W^2 twice and gives the other two identities. Disjoint
E_i commute. Hence on all nonzero heads these are idempotent
Temperley--Lieb relations. Globally the ground projections
P_* in (17) must remain; no quotient of the original source
or preservation by R is inferred. In particular this small
endpoint algebra does not prove that an arbitrary interleaved
braid word is polynomially bounded.

The carry VECTOR also has an actual meridian-normal Ward
description. Retain the original balanced coproduct

    F_tot=F_1+K_1^(-1)F_2, K_1=x Z_1^(-1),
    D_M=x partial_x at fixed physical Q.

Direct application to the original complete p gives

    (D_M F_tot)p=N(1-Z_1)w.                                (18)

Only the K_1^(-1)F_2 term differentiates. Its output
|a,N-a>, 1<=a<N, has coefficient
N x^(a-N)(1-Q^a), proving (18) entrywise.
On this degree-N subspace every first index is nonzero,
so 1-Z_1 IS a unit there. Thus

    w=N^(-1)(1-Z_1)^(-1)(D_M F_tot)p

is a valid restricted identity. It does not invert the
singular operator 1-Z_1 on the entire finite module.
Nor does it replace a full normal co-source by this one
operator-normal insertion. It identifies the carry line
which the global endpoint/current transport must retain.

These relations give an explicit finite endpoint calculus:
ground heads, a rank-one degree-N projector and its actual
normal Ward source. Sliding them through other crossings
still requires the original coproduct/current equations;
the relations alone supply no global geometric lower bound.

## 9. Exact flat-metric norm of the COMPLETE Green source

At completeness, the ground-output coefficient (6) is just a
unit phase:

    G_out|a,b>=x^(-b-2)|a+b,0>,
                    a>=1, a+b<N.                         (19)

This is a simplification of the FULL weighted endpoint, not
of the unweighted ground cell of the primitive clock Ward.
To prove it, use the partial-fraction identity

    1/(z;Q)_a=sum_(j=0)^(a-1)
       (-1)^j Q^(j(j+1)/2)
          /[F_j F_(a-1-j)(1-zQ^j)].                      (20)

The residues at each of the a simple poles agree; both sides
vanish at infinity, proving (20) without an asymptotic step.
Set z=Q^(b+1). Since x^(-2)=Q, the sum in (6) is
F_b/F_(a+b), which proves (19). No denominator vanishes:
b+a<N. The support filtration in Section 3 is unchanged;
there is no additional ground block.

Use the original orthonormal finite-head basis and let
d=N-1. Equations (5), (16), and (19) imply

    ||G_in||=||G_out||=sqrt(d), ||G_top||=d,

    ||L||=max[d,sqrt(d+sqrt(d))]
         =d for N>=3, and sqrt(2) for N=2.                (21)

Here the norm is the actual operator norm, not a norm after
an exponentially conditioned gauge. To see sharpness, fix
total degree t with 1<=t<N and write |b>=|t-b,b>.
The complete lower-degree block is

    L_t=Q[|0>r_t^t+u_t<0|],
    (r_t)_b=x^(-b) for 0<=b<t, (r_t)_t=0,
    (u_t)_0=0, (u_t)_e=x^(-e) for 1<=e<=t.

The two displayed output ranges are orthogonal. Therefore
L_t^*L_t=conjugate(r_t) r_t^t+t|0><0|.
Its possibly nonzero eigenvalues are t+sqrt(t), t-sqrt(t), since
||r_t||^2=t and |(r_t)_0|=1. The degree-N block is Q E;
all other degree blocks vanish. This proves (21) including
the small-level exception. The unstripped crossing retains
the SAME external kappa, of modulus one at completeness.

Thus the actual normal Green source of a crossing is only
linearly large in N in the original metric, even though its
individual unweighted clock ground kernel may be exponentially
large. In a tensor word this gives an explicit local defect
bound. Controlling its contraction through arbitrary exterior
crossings still requires that exterior; (21) alone gives no
global scalar lower bound or cancellation theorem.

## 10. The carry is fixed by its SAME original crossing

Let B=R_+/kappa=C D U_+ C^(-1) at completeness. The vector
w in Section 8 obeys the exact two-sided identities

    B w=w, w^t B=w^t, B E=E B=E.                          (22)

Consequently the same holds for B^(-1). The original R_+
has eigenvalue kappa on this line, and R_- has kappa^(-1).
These are identities in the original physical finite heads;
no arbitrary cut relocation is asserted.

Here is an all-level proof directly from the actual fusion.
On total degree N its coefficient is

    C_(u,v;a,b)=x^(u-a) F_a F_v/[F_(a-u)F_b],
                       u<=a, v=b+a-u.

Hence, with b=N-a, the component of w^t C is

    x^(-b) F_a sum_(h=0)^(a-1) Q^h [b+h choose h]_Q
       =x^(-b)F_a [N choose a-1]_Q.

It is zero unless a=1. The surviving row is
x^(-d)F_1<1,d|. This row is fixed by D U_+: D_d=1 and
only transfer order zero can reach its output from this
finite total-degree sector. This proves the left equality.

For the right equality, the original inverse-fusion Euler
convolution gives z=C^(-1)w with

    z_(N-v,v)=-x^(-v)(-1)^v Q^(v(v-1)/2)/F_(N-v),
                                          1<=v<N.

Indeed its convolution is the full inverse-Euler coefficient
zero minus its missing final term. Put m=N-v. Applying D U_+
to this vector multiplies its common output prefactor by

    D_v sum_(h=0)^(m-1)
       (-1)^h Q^(h(h-1)/2+(v+1)h)/[F_h F_(m-h)].

The sum extended through h=m is
(Q^(v+1);Q)_m/F_m=0. Subtract its last term and use
D_v=(-1)^v Q^(v(v+1)/2); the displayed factor is 1/F_m,
because -(-1)^N Q^(N(N+1)/2)=1 for every N, including even
N. Thus D U_+z=z. Together with the left identity and
E=-ww^t, this proves (22).

Equation (22) is compatible with (17), but it does not say
that an adjacent crossing preserves the carry sector.
Transport through neighboring heads remains a separate
question with the ground projections retained.

## 11. An exact resonant Fourier source, including its closure current

The remaining one-function field admits an exact finite-orbit
comparison with (12), with no undetermined central scalar.
Write h=2pi*i/N, retain the previously fixed phi_N, and put

    zeta=exp[-pi*i*(1+2c_b^2)/6],
    zeta_0=exp[pi*i*(1-4c_b^2)/12],
    A=exp(N lambda)(1-exp(Nz)), D=1-A.

On the same logarithmic cover define the FINITE source

    T_N(z,lambda)=sum_(j=0)^d
                         Psi_+(z-hj) exp(lambda*j).       (23)

Its exact original source decomposition is

    T_N=H_N(z,lambda) F_ref(lambda)
           +Psi_+(z) D I_-(exp lambda,
                                      exp(lambda+z-h)),

    H_N=i sqrt(N) phi_N zeta_0
          *(exp(Nlambda)-1)(1-exp(Nz))
          *exp[(N+z/h)lambda].                          (24)

Here I_- is precisely the conjugate opposite-root Newton
Barnes current of the [Rogers source theorem](actual_rogers_sink_opposite_beta_source.md#3-carry-the-opposite-root-contour-and-the-full-norm),
with its inherited DOWNWARD orientation and its continued
logarithmic marks. Equation (24) is a meromorphic identity;
at a collision it means the SAME continued combined source.
Neither lambda nor z is reduced modulo 2pi*i.

To prove (24), use the full-function shift exactly j times:

    Psi_+(z-hj)exp(lambda*j)
      =Psi_+(z) product_(k=0)^(j-1)
                       [exp lambda-Q^(-k)exp(lambda+z-h)].

Thus (23) equals

    Psi_+(z) B_(Q^(-1))(exp lambda,
                                      exp(lambda+z-h)).  (25)

Apply the independently proved opposite-root Newton source,
including its exact normalizer N/phi_-=phi_N. Its homogeneous
term is

    phi_N exp(Nlambda)(1-exp(Nz))
        *Psi_-(-h-lambda) exp[(z-h)lambda/h].

The compulsory sewing factor 1-exp(Nz) follows from
Psi_+(z)Psi_-(z-h)=1-exp(Nz). Finally full inversion gives

    Psi_-(-h-lambda)
       =(1-exp(-Nlambda)) zeta^(-1)
          exp[-pi*i*(sqrt(N)lambda/(2pi)+c_b)^2]
          *Psi_+(lambda+2pi*i+h).

Substitute (12) and
zeta_0^2 zeta exp(pi*i*c_b^2)=1. This is exactly (24),
including its affine exponential, phase, and two norm factors.

In the actual field (11), take

    tau_j=tau_0+hj, z=h+B-tau_0,
    lambda=D-B+2pi*i.

Its extra factor 1-exp[N(C-X-tau_j)] is constant on this
finite orbit and is retained outside (23). The scalar A
in (24) is EXACTLY the full-turn multiplier in (15).
Consequently the remaining Barnes current is multiplied by
the precise closure defect 1-A of the actual field. This
is a computed source, not a normalization imposed on it.

On the balanced divisor A=1, that current vanishes and
T_N=H_N F_ref exactly. On its regular finite part H_N is
nonzero: 1-exp(Nz)=exp(-Nlambda), and exp(Nlambda)-1
cannot vanish there. This proves a normalized, nonzero
resonant reference coefficient on THAT divisor. The
original whole source has NOT been shown to be supported
on A=1. Off it the current remains compulsory and may
contain the same continued homogeneous block.

### Why this finite orbit is compatible with the original source

There is a separate exact finite-source fact, before any
homogeneous/current split. The COMPLETE raw positive kernel
K(t)=B_0(t)F(t) is a Laurent polynomial with exponents in
[-2d,d]. For any fixed nonzero scalar t_0,

    (1/N)sum_(j=0)^d K(t_0 Q^j)
       =CT_t K+t_0^(-N)[t^(-N)]K.                       (26)

There is only one alias, since 2d<2N and d<N.
The sampling point may also depend on degree-zero auxiliary
parameters, including the retained Gaussian variables. It
must not carry nonzero total head degree; otherwise its
power in (26) would change the grading argument below.
For a monomial indexed by the actual nonnegative atom
orders, minus its t exponent is the output total head
degree minus the input total head degree. Thus the alias
in (26), after the original finite head restrictions,
raises integer degree by N. For the negative crossing the
same statement follows from its exact two-Newton/Rogers
layer, with its ONE shared continuous Gaussian retained;
the Gaussian changes coefficients and not these degrees.

Replace ANY collection of complete internal CTs in any
original signed word by (26). Each resulting error raises
total degree by a positive multiple of N; all original
crossings preserve total degree. In the original one-cut
pointed trace every traced head has identical input/output
index. The remaining cut index would have to increase by
at least N, impossible for indices 0,...,d.

For the original k-pair pointed plat, the cups have total
degree k d and its k-1 ordinary caps require (k-1)d.
The marked pair would therefore have degree at least
d+N=2N-1>2d, impossible for its two finite heads. This
uses the actual marked row, not an assertion that this row
is itself fixed-degree: it has coefficients x^e/N^2 on
all |c,e>. Thus every nonempty alias selection vanishes.
Hence this finite
root-orbit replacement preserves the entire original
whole source for arbitrary word length and bridge count.
It also preserves its original scalar normalization.
It is not asserted for arbitrary degree-lowering coupons.

This is a source-level circle-to-finite-orbit map. One may
apply (24) to its all-homogeneous summand, while retaining
EVERY other B/R current sector with the SAME logarithmic
marks. Neither (26)'s alias deletion nor its degree proof
can be reapplied separately to a meromorphic S/I sector,
whose Fourier support is different. Thus (24)--(26) do
not yet identify the WHOLE original Fourier functional
with the bare reference chain plus a polynomially bounded
endpoint operator. The missing bound concerns the joint
continued B/R currents, not the exact coefficient H_N.

This last limitation concerns the INTERNAL-orbit map alone.
The subsequent [balanced external Fourier theorem](actual_balanced_fourier_crossing_kernel.md)
supplies an additional source-preserving polarization that makes
all three original norms vanish together. Its exact current
rigidity eliminates the remaining physical alias errors. That
result resolves the local operator comparison, while retaining
every finite adapter and the original global co-source.
