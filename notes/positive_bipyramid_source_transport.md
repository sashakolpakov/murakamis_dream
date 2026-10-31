# Positive bipyramid cycles and the actual reflected source charge

28 October 2026. Two local steps are now explicit. The independently
proved charged full-Phi pentagon has a genuine REAL internal cycle
selecting its geometric bipyramid block with multiplicity one,
uniformly on compact positive families. Separately, the original
scalar head source has exact zero internal charge after its positive
factorial orders are reflected, with an explicit full-Phi Gaussian
field and OUTER-ray source retained.

These facts are not yet an identification of that reflected
circle/outer-ray fiber with the positive charged real contour. The
remaining comparison is a definite twisted beta/Pochhammer contour
problem described in Section 6. Its original growing source is now
resolved further by the exact
[norm-pole/Barnes cycle](actual_trivalent_quantum_beta_source.md),
which retains its nonzero balanced block and normalization remainder.
No global geometric cycle or original knot coefficient is assumed
to exist here.

The [audit](../experiments/audit_positive_bipyramid_source_transport.py)
and [results](../experiments/positive_bipyramid_source_transport_results.json)
check the rational bipyramid equations, geometric charges and Gaussian,
the actual source graph before/after reflection, exact window and
full-Psi reflection, and the boundary-difference source identities.

## 1. An arbitrary positive ordered bipyramid

Let x,y be complex and put

    H=x+y-xy,
    s_1=x, s_3=y, s_2=H, s_0=x/H, s_4=y/H.      (1)

Assume ALL five s_j lie in the upper half-plane. This is the open
positive bipyramid family for this ordered pentagon. No modulus
restriction is imposed. On a compact subset all shapes and angles
stay uniformly away from degeneration.

Define its actual angle charges

    a_j=Arg(s_j)/(2*pi),
    c_j=-Arg(1-s_j)/(2*pi),
    beta_j=1/2-a_j-c_j.

All are positive. The elementary identities

    s_0 s_2=x, s_2 s_4=y,
    1-s_0=s_4(1-x), 1-s_4=s_0(1-y),
    1-s_2=(1-x)(1-y)

give, with the positive principal angles,

    a_1=a_0+a_2, a_3=a_2+a_4,
    c_1=c_0+a_4, c_3=a_0+c_4, c_2=c_1+c_3.     (2)

These are precisely the charges of the independently proved
[full-Phi kernel pentagon](faddeev_pentagon_audit.md). The branch
equalities have no hidden 2*pi term: their two positive angles add
to the indicated positive shape angle, and their negative complement
arguments add to its negative principal complement argument.
In particular c_2+beta_0+beta_4=1 is the new internal edge charge.

The ordinary five-term relation, applied to 1-x and 1-y, gives

    D(x)+D(y)=D(s_0)+D(s_2)+D(s_4).             (3)

## 2. The exact full-Phi kernel and its selected real normal cycle

Use EXACTLY the charged functions from the cited independent proof:

    f_(a,c)(t)=exp(-pi*i/12) psi_(c,beta)(t),
    psi_(a,c)(t)=nu(a-c)
       exp[-4*pi*i*c_b*a*(t-c_b(a+c))]/Phi_b(t-2c_b(a+c)),
    nu(r)=exp[-pi*i*c_b^2*(4r+1)/6],
    c_b=i(b+b^(-1))/2.

With charges (2), the true kernel identity, including its contour, is

    integral_R f_4(Y-t)f_2(t)f_0(Z-t)
                         exp[2*pi*i*(Y-t)(Z-t)]dt
       =mu_b f_1(Z)f_3(Y),
    mu_b=exp(pi*i*c_b^2*P/3),
    P=2(c_0+a_2+c_4)-1/2.                     (4)

The proof in the cited note starts with the defining full function,
Fourier inversion and its two shifts; its published proof is not a
premise. The positive charges give an absolutely convergent real
contour. For real b, |mu_b|=1; its exact phase remains attached.

At b=N^(-1/2), set

    Y=sqrt(N)*y_0, Z=sqrt(N)*z_0, t=sqrt(N)*tau,
    y_0=log|y|/(2*pi), z_0=log|x|/(2*pi),
    tau_*=log|H|/(2*pi).                         (5)

The REAL integration contour therefore passes through the geometric
normal point. This is a specified actual local cycle, not an
unspecified formal saddle or global knot thimble.

To verify its selection, use the exact full-Psi conversion

    f_j(sqrt(N)*v)=C_(j,N) exp(2*pi*(N+1)c_j*v)
          /Psi_N(2*pi*v+2*pi*i*(1+1/N)a_j),
    C_(j,N)=exp[-pi*i/12+pi*i*c_b^2*chi_j],
    chi_j=4c_j(c_j+beta_j)-(4(c_j-beta_j)+1)/6.   (6)

All C_(j,N) have modulus one. The uniform full-Psi symbol on its
selected strip gives, uniformly in real v,

    f_j(sqrt(N)*v)=C_(j,N) A_j(v) exp(F_j(v)/h)(1+O(1/N)),
    h=2*pi*i/N,
    F_j(v)=-Li_2(exp(2*pi*v+2*pi*i*a_j))+4*pi^2*i*c_j*v,
    A_j(v)=exp(2*pi*c_j*v)
                     (1-exp(2*pi*v+2*pi*i*a_j))^(a_j-1/2). (7)

All branches are the selected upper-strip branches. The first
derivative grows at most linearly at infinity and is included in
A_j; the next derivatives and the full-Psi relative remainder are
uniform there. The amplitudes have at most exp(C|v|) growth.

The three-side leading phase is

    W(tau)=F_4(y_0-tau)+F_2(tau)+F_0(z_0-tau)
                              -4*pi^2*(y_0-tau)(z_0-tau). (8)

For each factor the negative imaginary part is the radial Legendre
function Im Li_2(s)-2*pi*c_j*log|s|. It is STRICTLY convex in its
real log radius, with its unique minimum at the shape s_j. The
three minima occur simultaneously at tau=tau_*. Thus Re(W/(2*pi*i))
has its unique global maximum on the entire REAL line at tau_*.
Its limiting slopes have strict signs, uniformly on compact positive
families, so its tails have a linear gap. The chirp in (8) is real
on this contour and does not alter the modulus.

The COMPLEX derivative also vanishes: it is 2*pi times

    Log(1-s_2)-Log(1-s_0)-Log(1-s_4)+Log s_0+Log s_4,

which is zero by the identities and angle marks above. Moreover

    G=-W''(tau_*)/(2*pi*i)
       =-2*pi*i*(2+sum_(j=0,2,4)s_j/(1-s_j)),
    Re G=2*pi*sum_(j=0,2,4) Im(s_j)/|1-s_j|^2>0. (9)

The real-contour Gaussian has its unambiguous square root Re G>0.
Its leading term is

    C_(0,N)C_(2,N)C_(4,N)
       A_0 A_2 A_4 sqrt(2*pi/G) exp(W(tau_*)/h)(1+O(1/N)). (10)

The sqrt(N) measure in (5) cancels the Gaussian N^(-1/2).
Every factor is nonzero and bounded above/below on a compact
positive family. The strict global modulus gap proves that the
REAL local move cycle selects this geometric block with coefficient
+1; its other normal ends are lower. This is stronger than just
checking det G is nonzero.

Its rate in THIS charged-kernel orientation is
-[D(x)+D(y)]/(2*pi). No sign is changed to fit a different knot-state
normalization. The exact identity (4) carries the selected block to
the two-side product with multiplier mu_b. This is a nonzero tame
map of the local geometric kernel lines; it does not create a
nonzero global exterior source coefficient.

## 3. Which complete sources pass through this move unchanged

For the multiplicative variables

    r_4=exp(2*pi*b*(Y-t)), r_2=exp(2*pi*b*t),
    r_0=exp(2*pi*b*(Z-t)),

the internal torus acts by
(r_4,r_2,r_0)->(lambda^(-1)r_4,lambda r_2,lambda^(-1)r_0).
Its boundary invariants are

    U=r_2 r_4=exp(2*pi*b*Y), V=r_2 r_0=exp(2*pi*b*Z).

The explicit coordinate change r_4=U/r_2, r_0=V/r_2 proves

    C[r_4^+-1,r_2^+-1,r_0^+-1]^(G_m)
                                  =C[U^+-1,V^+-1].       (11)

A Laurent monomial source has internal character
delta=h_2-h_4-h_0. It descends to these common scalar boundary
ports if and only if delta=0. A general source descends exactly
when all its nonzero Laurent coefficients have character zero.
Character delta instead gives r_2^delta times a boundary function;
this is a specified twisted line, not a removable scalar by fiat.

For a descending complete source, (4) may be paired with its SAME
exterior boundary functional. Finite Cauchy/window factors, original
cap factors and external full-Psi circle/ray integrals are all carried
by linearity and the stated Fubini/continuation conditions. Intervals
may first be evaluated to their finite polynomial to check (11),
then reinserted exactly; individual fractional-interval integrands
need not descend separately. No radial or interval endpoint term is
dropped in this procedure. On a compact common holomorphy chamber
this is ordinary analytic contraction; a continuation outside it
must keep its transported contour and residues.

The precise conclusion is a kernel-line transport: if a matched
exterior source has geometric coefficient c_N on one side, its
coefficient on the other is mu_b c_N in the stated trivializations.
It may be zero on both sides. If charges are themselves integrated,
the known phase mu_b stays INSIDE that functional; it is not pulled
out as though it were constant.

## 4. The original source law, checked on the actual reduced graph

The original moment/head graph has positive-factorial atomic orders
reflected by d=N-1. At a cap-free trivalent vertex its three atomic
arrows are oriented the SAME way, with the original head charge
plus or minus d. Its exact law is

    h_0+h_4+h_2=d,                               (12)

not unshifted scalar descent. For example one positive crossing's
nine atom slots in traversal order have the actual internal laws

    h_0+h_1+h_3=d, h_2+h_4+h_6=d,
    h_3+h_4+h_5=d, h_5+h_7+h_8=d.

Each triple has one positive-factorial edge. This holds pointwise
in the external moment/Gaussian variables, independently of the
full-Psi coefficient values or choice of circle/ray piece. It is
an incidence equation of the original full source, not a condition
imposed only at its geometric critical point.

There is an exact global unreflection. For each positive-factorial
kernel put s=z_out/z_in and write

    N s^d K_N(Q/(s t))
       =N Q^d t^(-d) K_N(Q^(-1)t s).             (13)

This is the polynomial reversal K_N(v)=v^d K_N(v^(-1)). Equivalently
replace its atomic order h by a=d-h, reverse its incidence edge,
and put r=t^(-1). The explicit factor NQ^d t^(-d) is retained as
part of the REFLECTED FIELD density. It must not be called tame
uniformly in t or deleted.

All reflected-factorial head charges cancel. Every cap-free internal
head vertex now has ZERO Kirchhoff charge; the original cup/cap
charges remain at the boundary. At a trivalent vertex (12) becomes
a=h_0+h_4, exactly the descent equation (11) in the corresponding
oriented variables. Higher-valence head vertices keep their full
zero-charge Kirchhoff equation rather than being called a single
pentagon port.

In incidence notation, if v_e is a reflected-factorial edge column,
gamma its original head charge and h_e=d-a_e, then
gamma+sum v_e h_e becomes
gamma'=gamma+d sum_F v_e with reversed columns -v_e on F.
The original reflected monomials are exactly -d sum_F v_e;
therefore gamma' consists ONLY of the original boundary charges.
This proves the law for every strict original word. The audit checks
it after actual Hardy-forest contraction for both signs and longer
original words, retaining their original source boundary rows.

The finite marked full-Phi clock fixes the affine phase precisely:

    Psi_+(h(a+1))=phi_N/F_a,
    phi_N=sqrt(N)exp{i*pi[1/4-(N+N^(-1))/12]}.

Thus the unreflected head a is marked by a+1, never by the bottom
zero mark. If a=b+k and all three clocks are so marked, their exact
relation is Q^(a+1)=Q^(-1)Q^(b+1)Q^(k+1). The Q^(-1) and phi_N
are retained. They cannot be removed because their classical limits
look simpler.

## 5. The actual reflected full-Phi field AND its ray

Let r=t^(-1), S=Log r, b=N^(-1/2). The original full-Phi inversion
identity gives the exact reflected field formula

    Psi_+(-S)=zeta_b exp[pi*i*(sqrt(N)S/(2*pi)+c_b)^2] Psi_-(S),
    zeta_b=exp[-pi*i*(1+2c_b^2)/6].               (14)

Equivalently Psi_-(S)=(1-r)(1-r^N)/Psi_+(S). This displays the full
central norm when the opposite orientation is written as an inverse;
it is not permission to invert a vanishing factor separately.
Combining the character in (13) with (14) yields

    r^d Psi_+(-S)=zeta_b exp(pi*i*c_b^2)
       exp[i*N*S^2/(4*pi)+(N-3)S/2] Psi_-(S).   (15)

The prefactor is unit modulus at real b; the Gaussian and linear
action in (15) are explicit and may be exponentially significant.

The source CIRCLE maps to |r|=R^(-1), with its reversed logarithmic
parameter, and density NQ^d r^d Psi_+(-S). The original negative
RAY does not become the standard inner negative ray. It becomes

    r in (-infinity,-R^(-1)),
    +NQ^d/(2*pi*i) Psi_+(-S) dr/r^2,
    S=log|r|-i*pi.                              (16)

Equation (16) uses N-d=1 exactly. Its tail at negative infinity is
the image of the original integrable zero end. Thus (13)--(16) carry
the COMPLETE original circle/ray/window source, with no endpoint
discarded and no unspecified exponential matrix frame.

## 6. The exact internal fiber still needing contour transport

For the actual sink triple consisting of a reciprocal U coefficient,
a V coefficient and the reflected F field, strip its constant NQ^d
and use the boundary invariants U=r t_U, V=r t_V. Its field is

    F_N(L;U,V)=r^d Psi_-(Log U-L) Psi_+(Log V-L) Psi_+(-L),
    r=exp L.                                    (17)

Its exact q-step and central norm are

    F_N(L+h)/F_N(L)
       =Q^d (1-Q^(-1)V/r)(1-Q^(-1)/r)/(1-U/r),
    h=2*pi*i/N,
    F_N(L+2*pi*i)/F_N(L)
       =(r^N-V^N)(r^N-1)/[r^N(r^N-U^N)].        (18)

These follow from the original full-Psi steps, or by multiplying
the first equation over its complete Q orbit. The factor r^d gives
the retained 2*pi*i logarithmic mark in the classical phase. Its
stationary algebraic relation is

    r=V/(1+V-U).                                (19)

There is an exact classical/central compatibility worth recording.
Put R=r^N, U_0=U^N and V_0=V^N. If M_N denotes the central ratio
in (18), then

    M_N-1=-[(1+V_0-U_0)R-V_0]/[R(R-U_0)].       (19a)

Thus its multiplier-one locus is the Frobenius copy of precisely
the linear stationary gluing polynomial (19). This is a genuine
local support candidate. The original relative coefficient source
can be inhomogeneous under this shift, so (19a) alone does not
place that source on M_N=1 or remove either denominator divisor.

The denominator and all full norm factors are retained. Equations
(17)--(18) specify the twisted beta/Pochhammer fiber of the actual
source, including its 0/0/infinity-Hankel origin. The arbitrary
positive charged REAL contour of Section 2 cannot simply be assigned
to this field. Transporting that fiber, or a normalized root
residue/derivative of it, into the positive separating contour with
its complete monodromy is the remaining local cycle problem. The
[subsequent exact source theorem](actual_trivalent_quantum_beta_source.md)
does not guess this adapter: it pushes the complete coefficient
source to a single circle/outer-Hankel current, then to an explicit
NONZERO balanced norm-pole block plus a uniformly bounded Barnes
factor times the full norm. It also gives a positive-bipyramid
example where the scalar fiber remains bounded; a universal positive
volume rate does not follow without its exterior source.

## 7. Exact difference transport of nonzero internal source characters

For completeness the charged kernel has an exact boundary observable
map. Put q=exp(2*pi*i*b^2) and

    alpha_j=exp(-4*pi*b*c_b*c_j),
    D_j=q^(-1/2)exp[-4*pi*b*c_b(c_j+beta_j)].

The original full-Phi shift gives

    f_j(x-i b)=alpha_j f_j(x)/(1+D_j exp(2*pi*b*x)),
    f_j(x+i b)=alpha_j^(-1)(1+q D_j exp(2*pi*b*x))f_j(x).

For the three-factor integrand K(Y,Z;t) in (4), z=exp(2*pi*b*t),
U=exp(2*pi*b*Y), V=exp(2*pi*b*Z), this yields POINTWISE

    z K=[alpha_4 V T_(Y+i b)-q D_4 U]K,
    (z+D_4 U)T_(Y-i b)K=alpha_4 V K.             (20)

Thus every positive polynomial source in z has an explicit boundary
difference operator. For J_h=integral z^(-h)K dt, negative powers obey

    (alpha_4 V-D_4 U T_(Y-i b))J_h
                          =T_(Y-i b)J_(h-1).  (21)

This is a source extension, not an instruction to invert that
difference operator or discard its kernel. Integrated boundary
shifts carry their translated contours and any residues. In
particular degree O(N) shifts cannot be declared harmless from a
fixed-degree pole-free contour argument.

At b=N^(-1/2) the negative-power integrals themselves converge for
0<=h<=d: their left scaled-tail exponent is
2*pi*((N+1)-h), since c_2+beta_0+beta_4=1. Their right tail only
improves. This keeps the affine +1 in the source law; it does not
prove uniqueness or a tame scalar inverse of (21).

The local positive kernel-line transport, the exact original
unreflection/descent and the outstanding fiber transport have been
kept distinct. Completing the last step is necessary before using
the positive contour as the original knot source's cycle or claiming
its geometric coefficient survives the move.
