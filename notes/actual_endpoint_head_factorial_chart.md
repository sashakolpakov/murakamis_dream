# Subexponential factorial charts at the original head endpoints

28 October 2026. A factorial change of head basis can be exponentially
conditioned on the whole physical color space. On either sublinear
endpoint band its condition number is subexponential, uniformly at
every level. This makes the natural blowup coordinates of a noncentral
endpoint meridian accessible at no additional exponential rate.

The change preserves the full original tensor source. It does not turn
a truncated head identity into an equality of its two conjugate
positions. That normal matching source is calculated explicitly below.
In particular this is a quantitative chart estimate, not the sharp
whole-knot bound or geometric survival theorem.

## 1. Uniform condition number, including all normal coefficients

Put Q=exp(2*pi*i/N), d=N-1, F_a=product_(j=1)^a(1-Q^j), and
D=diag(F_0,...,F_d) in the ORIGINAL orthonormal balanced head basis.
For 0<=R<=floor(d/2), let P_R project onto

    {0,...,R} union {d-R,...,d}.

Define H_N(0)=1 and H_N(R)=(e*N/R)^R for R>=1. Then

    max_(a in P_R) |F_a| <= N H_N(R),
    max_(a in P_R) |F_a|^(-1) <= H_N(R),
    cond(D restricted to P_R) <= N H_N(R)^2.       (1)

Proof. For 1<=a<=R<N/2 the elementary sine inequalities give

    (4/N)^a a! <= |F_a| <= 2^a.

Using a!>=(a/e)^a and the increase of r*log(e*N/r) for r<N,
both |F_a| and its reciprocal are at most H_N(R). The a=0
case is one. The exact reflection formula, with its phase retained, is

    F_a F_(d-a)=N (-1)^a Q^(a(a+1)/2).

Thus the upper band has |F_(d-a)|<=N H_N(R) and reciprocal at
most H_N(R)/N. These prove (1), without evaluating a factorial
at its forbidden zero F_N.

If R=R_N=o(N),

    log cond <= log N+2R log(e*N/R)=o(N).          (2)

This estimate controls the ENTIRE band vector and every linear
functional on it, not just the value at its endpoint or a fixed
number of derivatives. It does not bound a fiber that has already
summed over unrestricted bulk labels.

There is also an everywhere invertible, globally tame finite matrix

    D_R=D P_R+(I-P_R),
    ||D_R|| ||D_R^(-1)||<=N H_N(R)^2.              (3)

For a fixed tensor network, independent copies of (3) at any fixed
number of physical wires still have exp(o(N)) combined condition
number. Nothing is assumed about the size of the knot invariant.

## 2. Exact source-preserving changes and the retained endpoint arrows

For adjacent tensors A and B on a shared physical head, insert

    B A=(B D_R)(D_R^(-1) A).                       (4)

All other heads are spectators. The original pivots commute with
D_R because both are diagonal; an exposed cup, cap or marked row
is transformed by the same explicit inverse pair rather than reset.
Consequently any fixed collection of such changes preserves the
ORIGINAL scalar exactly, for arbitrary crossing signs and braid
width. The factors in the norm comparison are bounded by (3).

Let S be the physical unilateral raising matrix, S|a>=|a+1> for
a<d and S|d>=0. The balanced raising operator is exactly

    Fcal=D S D^(-1),
    Fcal|a>=(1-Q^(a+1))|a+1>  (a<d).               (5)

With the cyclic unitary shift X|d>=|0>, the formula instead is

    Fcal=D X D^(-1)-(1/N)|0><d|.                  (6)

The rank-one term is mandatory: F_d=N, and the original raising
operator is nilpotent. Replacing (5) by a cyclic Weyl generator
without (6) changes the source. A coefficient 1/N alone is not a
reason to discard its contraction with an unrestricted exterior.

For the tame truncated gauge D_R, (5) holds on arrows with BOTH
ends in its endpoint band. Globally the exact conjugated raising
matrix has coefficient

    (1-Q^(a+1)) g_a/g_(a+1),
    g_a=F_a on P_R and g_a=1 otherwise,             (7)

and is zero at the top. Thus the two possible band-interface
arrows remain explicitly in (7); the middle arrows are unchanged.
Their norm is at most 2 cond(D_R), hence subexponential. No band
interface or cyclic endpoint is silently deleted.

## 3. The classical endpoint chart is genuinely noncentral

At complete color use the actual commuting head symbols

    K=-B^(-1), f=(1-B)z, e=(B^(-1)-1)/z.

The actual Gauss meridian is

    G=[[K,e],[f*K,f*e+K^(-1)]],
    det G=1, Tr G=-2.

On B!=1 the change from z to f is canonical:

    dlog B wedge dlog f=dlog B wedge dlog z.        (8)

Its generating derivative is log(1-B), precisely the factorial
shift in (5). In the chart (B,f),

    e=(1-B)^2/(B f).                              (9)

This chart is regular at B=1 when f!=0, and there

    G=[[-1,0],[-f,-1]].                           (10)

Thus z=f/(1-B) escaping to infinity can describe a FINITE,
NONCENTRAL meridian. An argument that substitutes B=1 while
keeping z bounded misses (10). The complementary chart (B,e)
has f=(1-B)^2/(B e); at B=1 and e!=0 it gives the upper
noncentral unipotent. Its symplectic orientation is recorded by
dlog B wedge dlog e=-dlog B wedge dlog z, or by using B^(-1)
as its momentum. The two charts cover all noncentral trace -2
matrices with G_11=-1; the central matrix is the remaining point.

This is a regular chart of the actual meridian surface. It is not
an assertion that a restricted face stationary point glues its
two neighboring meridians. The quantum estimate (1) makes the
factorial part of this chart affordable on the physical collar;
it does not prove a full contour comparison through that collar.

## 4. What the exact normal source still requires

Across a shared head, the two copies of the factorial basis change
cancel coefficient by coefficient. In particular they do not alter
the low-band projector P_low=sum_(a=0)^R |a><a|. In the unitary
finite Fourier basis its exact kernel is

    (1/N) sum_(a=0)^R Q^(a(j-i)).                  (11)

Keeping the unwrapped complex position ratio t in the same finite
polynomial gives

    (1/N) K_R(t), K_R(t)=sum_(a=0)^R t^a
                     =(1-t^(R+1))/(1-t).          (12)

Both numerator and denominator in (12) are retained, with value
R+1 at t=1. On |t|<=C,

    |K_R(t)|<= (R+1) max(1,C)^R=exp(o(N))          (13)

when R=o(N) and C is fixed. But for every fixed |t|<1 and R->infinity,
K_R(t)->1/(1-t), which is nonzero when t!=1. Hence a tame
endpoint source does NOT impose equality of its two positions.

The estimate also controls every fixed logarithmic derivative of
this EXACT source. If |Log t|<=C and s is a fixed nonnegative integer,

    |(t*d/dt)^s [(1/N)K_R(t)]|
        <= N^(-1)(R+1)^(s+1) exp(CR).             (13a)

This follows term by term from the finite sum, including s=0 and
R=0. Thus fixed normal jets of a low-band seam have the same
subexponential cost for R=o(N), without using an asymptotic delta
function or dividing by 1-t. It does not remove the upper-band
factor t^(d-R), whose modulus can have an N-order rate off the
unit circle.

Splitting (12) into 1/(1-t)-t^(R+1)/(1-t) creates two apparent
matching poles at t=1. Their residues cancel exactly. On a bounded
logarithmic ratio chamber and R=o(N), BOTH terms have zero N-order
rate away from the pole; one cannot discard the second as having
a strictly lower exponential rate. The upper band has its additional
factor t^(d-R), which must also be retained.

In chart (9), the original shared-head equation is f_left=f_right,
because the common B is the same and z_left=z_right before taking
its limit. Evaluating only at B=1 or replacing its normal source by
(13)'s numerical bound does not supply that equation. The full
head contraction retains it; an isolated endpoint packet has (12)
instead. This pinpoints the remaining need for a coupled contour
or exact cancellation across the head bands, rather than claiming
that a tame chart alone proves the volume estimate.

[Independent finite audit](../experiments/audit_actual_endpoint_head_factorial_chart.py)
checks the norm bound, the cyclic correction, actual signed full-word
gauge invariance, and the Fourier source with its canceled matching
residues. These checks supplement the uniform arguments above.

Independent proof reread (Euler/source agent): (1)--(13a) verified
directly, including the exact phase in factorial reflection, the
1/N cyclic arrow, the two band-interface arrows, both noncentral
Gauss charts and the complete finite geometric-series seam. The
normal-matching limitation in Section 4 is essential; no whole-source
or geometric critical-value bound follows merely from (13a).

## 5. Nilpotent reconstruction retains a genuine source current

Let 1<=s<N, P=I-S^s(S*)^s=P_low(s-1), and let
T_s(C)=S^s C(S*)^s on the ORIGINAL finite orthonormal head.
Direct multiplication, before any source evaluation, gives

    (I-T_s)C=P C+S^s[(S*)^s,C].                  (14)

The inverse I+T_s+T_s^2+... is finite and has norm at most
ceil(N/s), since S is a contraction. Thus it controls the ENTIRE
right side of (14), including its commutator current. At the actual
marked knot cut C=K_N I this commutator vanishes, but reconstruction
then only repartitions the same unknown scalar K_N among its head
bands. At an internal open wire with the original modified mark
retained elsewhere, its environment need not be scalar, so deleting
the current in (14) is not justified by the marked-cut identity.

There is a concrete obstruction to extending the polynomial norm
claim merely by inserting degree-preserving original crossings.
On TWO actual heads put S_1=S tensor I, let R be the original
COMPLETE positive checked crossing including kappa, and define

    T_R(A)=R S_1^s A(S_1*)^s R^(-1).              (15)

This superoperator is nilpotent: it raises the total degree of
both the row and column of A by s. Its nilpotence order is at most
ceil((2d+1)/s). Nevertheless its Green inverse is exponentially
conditioned, for every s=s_N=o(N).

Here is an exact matrix certificate. Set k=floor(N/2), j=floor(N/4)
and a=k+j. For all sufficiently large N, s<=j and a<=d. The
original crossing has the DIAGONAL coefficient

    r=R_((a,j),(a,j))
      =kappa x^(-2j) Q^(j^2) F_a^2/(F_k F_j^2).  (16)

It is diagonal because transfer k=a-j sends input (a,j) to
(j+k,a-k)=(a,j); this uses the checked-crossing order. The exact
complete-color inverse relation R^(-1)=Flip conjugate(R) Flip
gives R^(-1)_((j,a),(j,a))=conjugate(r), with every scalar kept.
Take the unit Hilbert--Schmidt matrix

    A=|a-s,j><j-s,a|.

Then the ((a,j),(j,a)) entry of T_R(A) is EXACTLY |r|^2.
The row and column total degrees of T_R^ell(A) are both
a+j-s+ell*s. Thus no other ell contributes to that entry, and
different powers are Hilbert--Schmidt orthogonal. Consequently

    ||(I-T_R)^(-1)||_(HS->HS)>=|r|^2
       =exp[(v_8/pi)N+O(log N)],                 (17)

where v_8 is the regular ideal octahedron volume. The last equality
uses the uniform factorial estimate and the exact bulk maximizer
proved in [the weighted crossing audit](weighted_crossing_source_gap.md):
log|r|/N -> -4J(1/4)=v_8/(2pi). In particular this failure is not
an arbitrary nilpotent-matrix example or an omitted half-Cartan
factor; it occurs for the literal original R and its inverse.

Statement (17) rules out a polynomial OPERATOR transport estimate
from positive grading and nilpotence alone. It does not prove an
exponential lower bound for the original scalar pairing of this
Green kernel. Such a pairing can cancel large intermediate matrix
entries, so Hopf-Ward control of the full current in (14) remains
the constructive question. No internal-current cancellation or
whole-knot volume conclusion is asserted here.
