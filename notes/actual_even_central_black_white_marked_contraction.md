# Even paired black, ordinary-white and original marked contractions

29 October 2026. The actual EVEN central two-vertex source has an exact
positive marked contraction, despite the zero self-pairing of every paired
image. The calculation uses the true ordinary metric and a regular
generic lift of the full nilpotent coupon. It does not replace the paired
channel by a projector, move the mark onto an ordinary quotient, or
identify white with the Hermitian adjoint of black.

For N=2m>=4 put j=m-1, d=N-1, theta=pi/N. Write the already proved
actual black scalar as

    A_N=q^[1-m(m-1)] S_N,
    S_N=sum_(k=1)^(m-1) sin(k theta)cos(k theta) beta(m,k)^4>0.

Then the original marked two-vertex source, with all three circles in
this paired central sector, is EXACTLY

    Z_even=8 N^3 S_N^2/cos(theta)
          =(1/2)exp(2N v8/pi)[1+O(1/N)].             (1)

The N=2 central sector is zero. Other joint channels and their coherent
sum are not evaluated here. For comparison, the
[odd simple central contraction](actual_central_black_white_marked_contraction.md)
is N^3 S_N^2 with its different odd quartic S_N.

## 1. Actual paired image and its genuine pivotal dual

Use q=exp(pi i/N), Q=q^2, x=q^d, F_r=(Q;Q)_r. Let
W:Q_j->V_N tensor V_N be the full actual Clebsch map in the
[even normal source packet](actual_trivalent_even_central_normal_packet.md).
Q_j has dimension 2j+1=N-1 and its genuine ordinary metric is

    G_rr=sin((r+1)theta)/sin(theta), 0<=r<=2j,
    pi=G^(-1) W^dagger P,
    pi W=0,
    L_c=h0 W pi, h0=2N/sin(theta).                  (2)

L_c is the COMPLETE c=-2cos(theta) sector of the original circle.
Its first normal has already been applied in (2). It is nonzero and
nilpotent; it is not the spectral projector of that paired cluster.

The original physical self-duality is

    p_(a,b)=N x^(-b)delta_(a+b,d),
    ell_(a,b)=x^a/N delta_(a+b,d), ell=p^(-1).

On Q_j choose the ordinary self-duality with highest coefficient one:

    pQ_(r,2j-r)=(-q^(2j))^r Q^[-r(r+1)/2]
                             F_r F_(2j-r)/F_(2j),
    ellQ=pQ^(-1).                                  (3)

For a map W its genuine right dual is

    D(W)=pQ^T W^T(ell^T tensor ell^T)P.

It is a bilinear pivotal dual. The actual all-input equality is

    D(W)=gamma pi,
    gamma=q^[3m^2-2m+1]/N^2.                        (4)

Both maps preserve the actual INTEGER H grading. In that homogeneous
Hom space a map onto the simple Q_j has, after duality, a highest
vector in the uniquely determined pair kernel of degree m. Its highest equation is a
first-order recurrence with all its interior coefficients nonzero.
Thus this homogeneous Hom space is one-dimensional. Periodic K
aliases in other integer degrees are not asserted to be absent from
an unrelated ungraded Hom problem.

To fix the scalar without a normalization convention, take input
colors a,b with a+b=m. The actual lowest endpoint is

    W_(2j)(j+a,d-a)=q^j h_a,
    h_a=q^(ma) beta(m,a).

Since pQ_(2j,0)=q^(-2j), the left side of (4) is
q^(-j)x^m h_a/N^2; the right row before gamma is conjugate(h_b).
The ratio h_a/conjugate(h_b)=q^(m^2) gives (4).

The dual in the opposite direction satisfies D(pi)=gamma^(-1)W.
Indeed direct matrix multiplication gives

    D^2(W)=(K_V^(-1) tensor K_V^(-1)) W K_Q=W.

The signs from the two physical factors square to one. No use is
made of the false equality pi W=I.

Let J=p_16 p_23 p_45 be the original nested black cup source. Define

    U=pi^tensor3 J,
    Lambda=ell^S W^tensor3.

The original nested matching is unchanged by right-dual reversal,
so exactly as an index identity,

    Lambda=gamma^3 D_Q(U).                          (5)

The true black tensor is

    U=s Theta, s=N^3 A_N/G_jj=N^3 A_N sin(theta),    (6)

where Theta is the actual invariant in Q_j^tensor3 normalized to one
at magnetic colors (2j,j,0). This is the independent ordinary 3j of
the even source theorem, not a tensor defined by dividing U by a
selected entry.

## 2. A generic finite theta evaluation, proved by Vandermonde

Temporarily take a generic parameter zeta, write Q=zeta^2 and
F_r=(Q;Q)_r. In the ordinary highest-weight 2j object, with the
cup (3), the highest vector for the same ordinary object inside its
square has entries

    h_a=(-1)^a Q^[-a(a+1)/2]
                     F_(j+a) F_(2j-a)/(F_j F_(2j)),
    0<=a<=j.                                       (7)

This follows directly from
h_(a+1)/h_a=-Q^(-a-1)(1-Q^(j+a+1))/(1-Q^(2j-a)).
Let WQ_r=F_pair^r h/F_r. Its entire lowest slice is

    WQ_(2j)(j+a,2j-a)=h_a.                         (8)

For a finite proof, both sides obey the same first-order lowest F
equation. At a=j the actual divided coproduct gives

    sum_(s=0)^j (Q^-j,Q^(j+1);Q)_s/F_s^2
       =(Q^-j;Q)_j/F_j=(-1)^j Q^[-j(j+1)/2].

This is the second finite Chu identity (obtained by base inversion
from the elementary finite proof in
[the quadratic source transform, section2](actual_half_color_quadratic_source_transform.md)).
It equals h_j, proving (8) with scalar one.

Schur's first-order highest recurrence makes D(WQ)WQ a scalar eta_j
times the identity. Evaluate it on the highest vector using (3),(8):

    eta_j=(-1)^j Q^[-j(j-1)/2]
         sum_(a=0)^j Q^[-(j+1)a]
                    [j+a choose a]_Q [2j-a choose j-a]_Q
       =(-1)^j Q^[-j(3j+1)/2] [3j+1 choose j]_Q.    (9)

The last equality is elementary Vandermonde: the summation is the
coefficient of u^j in

    1/[(uQ^(-j-1);Q)_(j+1)(u;Q)_(j+1)]
       =1/(uQ^(-j-1);Q)_(2j+2).

Expand each reciprocal finite product by its elementary coefficient
formula. This proves (9) as a finite rational identity, without a
published theta or 6j evaluation.

Set Theta0=(WQ tensor I)pQ. Its stated anchor is

    a_j=(Theta0)_(2j,j,0)=(-1)^j zeta^[-j(j+3)].     (10)

The actual cap/cup index contractions give K_Q T=eta_j I for the
cut theta, where T_st=sum_(a,b)Theta0_(a,b,s)D(Theta0)_(a,b,t).
Equivalently this follows from the invariant E equations, which
give K_Q T scalar, and the same highest coefficient used in (9).
Consequently the normalized invariant Theta=Theta0/a_j obeys

    D(Theta)Theta=eta_j [2j+1]_zeta/a_j^2.           (11)

At the even root this expression, and the entire effective cut,
are ZERO: [3j+1 choose j]_Q has a simple factor 1-Q^N, while
F_j and F_(2j+1) are units. This is why the odd retraction argument
cannot be reused.

## 3. Retain the physical mark by a regular normal trace quotient

Lift the physical V_N, the ordinary Q_j and their cups to the same
generic parameter zeta near q. An explicit regular lift of W starts
at physical degree t=d-j=m with highest coefficients

    h_a(zeta)=(-1)^a zeta^(-da)
       Q^[a(t-1)-a(a-1)/2] (Q^(j+1);Q)_a F_(d-a)/F_d,

and uses the actual divided-F descendants through r=2j. Its highest
recurrence proves covariance, and factorial reflection gives exactly
the root h_a in section1. All defining factorial denominators have
index <=d<N, including F_d in this highest lift. They are units.
Define the regular lift

    pi(zeta)=gamma^(-1) D(W(zeta)),

using the FIXED root gamma from (4). It specializes to the genuine
pi in (2). Thus h0 W(zeta)pi(zeta) is a regular Hopf coupon whose
root value is the exact full-normal circle sector L_c.

This is a chosen regular lift for a FIXED-ROOT identity. It is not a
claim that the original moving-q circle or pivot has this entire
generic normal germ.

The lifted U is s(zeta)Theta(zeta), with s holomorphic and its root
value given by (6). The generic ordinary closed physical diagram
with coupons W pi is therefore, by (5),(11),

    F(zeta)=gamma^3 s(zeta)^2
                     eta_j(zeta)[2j+1]_zeta/a_j(zeta)^2. (12)

Cut the original marked physical arc before closing it. Its open
map is a scalar t(zeta)I on the physical highest-weight d module.
All its entries are regular, so t is holomorphic at q. The physical
cup has p0=N zeta^(-d^2), and direct cup/cap multiplication gives

    ell p^T=(-1)^d K_V,
    F(zeta)=(-1)^d [N]_zeta t(zeta).                (13)

At the root this is exactly the original pivot K^(1-N), since
K^N=(-1)^d I. The unrestricted original marked row satisfies
m p=1, so its fixed-root closure is t(q). The mark has remained on
the physical V_N strand throughout. No paired projector or arbitrary
modified-trace axiom is introduced.

The zero in (11) is simple. Since N=2m, j=m-1 and 3j+1=N+j-1,
factor that zero explicitly in (9), giving

    lim_(zeta->q) eta_j [2j+1]_zeta/[N]_zeta
       =(-1)^j q^[-3j(j+1)+d]
                           N/[(1-Q^j)F_(2j)].      (14)

Indeed F_(3j+1)/(1-Q^N) specializes to N F_(j-1).
Equation (14) retains the normal responsible for the original
marked scalar; it is not obtained by setting the ordinary zero to
a positive value.

From (12)--(14), the marked scalar for three W pi coupons is

    t(q)=(-1)^(m+1) q^(-2)
                         sin(theta)^2 tan(theta) A_N^2. (15)

Substitute gamma from (4), s from (6), a_j from (10), and use

    F_(2j)=N/(1-Q^-1),
    (1-Q^-1)/(1-Q^j)=i tan(theta).

These identities give every phase in (15). Multiplying by h0^3,
then using A_N=q^[1-m(m-1)]S_N and q^N=-1, cancels the remaining
phase and proves (1). Each fixed edge twist R^e L_c contributes its
literal unit omega_j^e, where

    omega_j=kappa(-1)^j q^[j(j+1)].

The complete expression therefore acquires omega_j^(e1+e2+e3).
Any external original line factor chi_N stays outside this raw formula.

## 4. An explicit checkable marked co-source identity

Use the unscaled W-coordinate white tensor Vm of the
[literal branching vertex](actual_trivalent_complete_circle_vertex_kernel.md),
and the independently normalized Theta in (6). The same result is
equivalently the full coherent magnetic sum

    sum_(r1,r2,r3) Theta_(r1,r2,r3) conjugate(Vm_(r1,r2,r3))
       =N^4 sin(theta)^2/cos(theta) conjugate(A_N).   (16)

The ordinary white covector is nonzero and equals (5), but its
closed pairing with U is zero. Formula (16) evaluates the original
marked normal co-source instead. It does not assert equality of
the marked white tensor with an adjoint black tensor on arbitrary
exteriors, and gives no full magnetic norm estimate.

The [focused audit](../experiments/audit_actual_even_central_black_white_marked_contraction.py)
checks the generic finite theta evaluation separately from exact
root source/duality data and literal full physical marked closures.
The analytic argument above proves every even level N>=4, including
composite levels. The N=2 zero is retained separately.
