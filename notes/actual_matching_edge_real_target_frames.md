# Which actual geometric target frames have real magnetic rows?

30 October 2026. Independently reviewed. This is a local
classification for the ACTUAL inverse-turn target, not a common-frame
existence theorem for the whole link. It supplies a real cross-central
frame for every strict certified target c<1. Its total degree can be
below 1/2; the existing Green theorem allows that range. One other
apparently favorable branch is killed by the exact finite-source
bandwidth, including all generic-q normals.

## 1. Keep the actual ordered target and both degree adapters

Use the marked inverse turn of
[the polynomial generating-action theorem](actual_matching_edge_polynomial_geometric_action.md).
For a certified crossing-circle rectangle with 0<c<1, write

    c=sech eta, eta>0, k=sinh^2 eta,
    J=-exp(-2eta), T=diag(J,J^-1),
    R=(1+i sqrt(k))/(1-i sqrt(k)), D=diag(R,1).

After a centralizer normalization, its first target input and output are

    A=[[a,1],[kappa,d]], A_out=D A D^-1,
    a=-2J/(J+1), d=-2/(J+1),
    kappa=-(J-1)^2/(J+1)^2.                         (1)

The second input is T A^-1. These are the actual inverse-turn pair,
whose product trace is 2-4/c^2, and its actual conjugator eigenratio.
In particular D is not chosen to fit magnetic coordinates. The
[rectangle bound](actual_matching_circle_rectangle_bound.md) proves
c<=1 in the certified class; the parabolic equality c=1 is excluded
from the present diagonalization argument.

A physical frame is represented by a rank-one trace-one projector Pi.
Let the normalized target degree be real, 0<tau<1. The low adapter has

    E=Tr(T Pi)=exp(-2pi i tau), e=exp(-pi i tau).

The high adapter instead has E=exp(+2pi i tau), e=exp(+pi i tau).
In BOTH cases put c0=-cos(pi tau) in (-1,1), and write

    Pi=[[p,q],[r,1-p]], p=(E-J^-1)/(J-J^-1),
    X=r/e, Y=kappa q/e,
    K=(c0^2+k)/(4k^2), d0=-c0/k.

The determinant-zero condition and the two actual prefix traces are
exactly

    XY=K,
    z_in=Tr(A Pi)/e=d0+X+Y,
    z_out=Tr(A_out Pi)/e=d0+R X+R^-1 Y.            (2)

For example the diagonal trace in (2) follows from
`k=-(J+1)^2/(4J)` and `c0=-(e+e^-1)/2`; the same substitutions give
`kappa p(1-p)/e^2=K`.

Here z_in,z_out denote normalized traces, not tetrahedron shapes.
In the low adapter the physical coordinate is U=-1/Tr(A Pi), so
the centered exponential is U/exp(pi i tau)=-1/z_in. In the high
adapter the actual dictionary is

    T_phys=1/T_low, U_phys=U_low/T_low,

and U_low/exp(pi i tau)=-1/z_in again. The output is identical with
A replaced by A_out. Thus in both adapters the two rows are REAL
if and only if |z_in|=|z_out|=1. Their strict physical support is
equivalent to

    Re z_in<c0, Re z_out<c0.                       (3)

Indeed the centered magnetic argument has the unique marked lift in
(-pi tau,pi tau), and z=-exp[-2pi i(nu-tau/2)]. This proves (3)
also for tau<1/2; that range must not be discarded merely because
an ordinary complete-channel column needs a larger total degree.
The present exceptional operator is the polynomial p_a(J_t).

## 2. All strictly physical real solutions are anti-diagonal

Since K>0, parameterize every solution of XY=K by

    X=sqrt(K) exp(sigma+i phi),
    Y=sqrt(K) exp(-sigma-i phi), sigma,phi real.

Put beta=atan sqrt(k), chi=phi+beta, and L=2sqrt(K). Then

    z_in =d0+L[cosh(sigma)cos(chi-beta)
                         +i sinh(sigma)sin(chi-beta)],
    z_out=d0+L[cosh(sigma)cos(chi+beta)
                         +i sinh(sigma)sin(chi+beta)].          (4)

Their squared-modulus difference factors as

    |z_in|^2-|z_out|^2
      =4L sin(chi)sin(beta)
          [d0 cosh(sigma)+L cos(beta)cos(chi)].       (5)

If sin chi=0, the two traces are complex conjugates. To exclude the
other possibility from strict support, put M=cosh^2 sigma and use
the vanishing of the bracket in (5). The common unit-modulus equation
then gives

    M=k/(1-c0^2)+1/(1+k),
    cos^2 chi=c0^2 M(1+k)/(c0^2+k).                 (6)

Consequently Delta=1-c0^2(k+2)>=0 is necessary. Directly computing
the mean and difference of the two real parts gives

    (c0-Re z_in)(c0-Re z_out)
      =-Delta [c0^4(k+2)-2c0^2+k^2+k+1]
          /[(1-c0^2)^2(1+k)^2].                   (7)

The bracket is strictly positive: Delta>=0 implies
c0^2<=1/(k+2)<1/2, so already 1-2c0^2>0 and all other terms are
nonnegative. Thus (7) is nonpositive, contradicting BOTH strict
inequalities (3). This also excludes the equality Delta=0.

It follows that every strictly physical real pair is conjugate.
Write z_in=rho+i sqrt(1-rho^2), z_out=conjugate(z_in), allowing
their exchange. Substitution in (2) gives precisely

    [(1+k)rho+c0]^2=k+2,
    rho_+=(sqrt(k+2)-c0)/(1+k),
    rho_-=(-sqrt(k+2)-c0)/(1+k).                   (8)

The value rho=-1 gives the common central row; strict cross-central
rows require -1<rho<c0. Conversely every branch of (8) with this
inequality supplies an actual projector: solve the two linear
equations (2) for X,Y, set r=eX and q=eY/kappa, and (8) gives
XY=K. The linear determinant is nonzero because R!=R^-1 for k>0.
Both target prefix traces are units. No purely formal independent
choice of the input and output rows is involved.

The two marked row coordinates are

    nu_low=(tau-1)/2+acos(rho)/(2pi),
    nu_high=tau-nu_low,
    0<nu_low<tau/2<nu_high<tau.                    (9)

For the displayed upper-half-plane z_in, the INPUT is nu_high and
the OUTPUT is nu_low. Exchanging the signs of both trace imaginary
parts swaps input and output. Their exchange has the same support and
distance. This proves the
classification in BOTH actual degree adapters.

## 3. Exact bandwidth selects only the minus branch

The original target matrix J_t(zeta) is tridiagonal at generic zeta.
The exact matching-edge operator is a scalar normalization times
p_a(J_t), where p_a has degree a. Therefore EVERY generic entry with
|u-v|>a vanishes identically. This remains true after taking any fixed
generic-q derivative, clearing its scalar normalizers, or combining
the retained partner normal. It is not a semiclassical estimate.

For (9) the row distance is

    delta=nu_high-nu_low
         =1-acos(rho)/pi=1/2+asin(rho)/pi.         (10)

The plus branch is strictly physical precisely when
c0>1/sqrt(k+2). It always has rho_+>0. Thus delta>1/2, and for
actual folded degrees a/N->1/2 every sufficiently nearby integer
matrix entry is IDENTICALLY ZERO. Its real frame cannot serve as a
direct nonzero exceptional kernel. The finite-propagation identity
for a whole continuant vector does not contradict this entrywise fact.

The minus branch has rho_-<0, hence delta<1/2. It avoids this exact
support obstruction. This does not by itself prove a nonzero matrix
element, an asymptotic, a contributing spectral saddle, or absence
of cancellation in the full marked contraction.

## 4. Real cross-central local frames exist for every strict target

The minus branch is strict cross-central and physical exactly when

    -1/sqrt(k+2)<c0<min(1,k+1-sqrt(k+2)).           (11)

The interval is nonempty for EVERY k>0, since

    k+1-sqrt(k+2)+1/sqrt(k+2)
       =(k+1)(1-1/sqrt(k+2))>0.

Choose any c0 in this open interval and set
tau=acos(-c0)/pi. Equations (2),(8) construct a common local frame
with the strict real cross-central rows (9) and distance below 1/2.
It therefore lies in the real parameter range of the
[cross-central Green action](actual_matching_edge_cross_central_green_action.md).
That theorem allows every 0<tau<1, so no additional tau>1/2
hypothesis is needed for this local application.

There IS a useful limitation if one insists on tau>1/2: then c0>0,
and (11) has a solution precisely when

    k>(sqrt(5)-1)/2,
    c<sqrt((sqrt(5)-1)/2).                         (12)

For larger rectangles the required real total must be below 1/2.
The already certified isolated cylinders C(h^s), s>=5, have
c=cos(pi/s) above this threshold by
[the arbitrary-width seed theorem](actual_conway_arbitrary_width_seeds.md).
They illustrate why imposing the ordinary complete-column domain
on the exceptional Green operator would falsely create an obstruction.
No theorem about a universal global choice of frame follows instead.

## 5. The original selected frame is still an additional constraint

The inverse pivotal turn changes the basepoint. With A_old,out the
original first output meridian, the projectors obey

    Pi_target=A_old,out Pi_old/Tr(A_old,out Pi_old),
    Pi_old=A_old,out^-1 Pi_target/Tr(A_old,out^-1 Pi_target).     (13)

For a direct check, the actual first lower factor is
L_1=[[1,0],[-G_21,G_11]], and
L_1^-1 E_11 L_1=G E_11/G_11. Conjugating back gives (13).
The denominator in the inverse formula is the nonzero first target
prefix trace, so the local projectors constructed here pull back.

The selected-strip conditions for EVERY other disk must be imposed
on this Pi_old and its actual prefixes. They are not conditions on
independently selected target diagonals. The present classification
neither proves nor disproves their simultaneous compatibility with
(11). In particular it does not replace the global prescribed-pair
theorem by a real-slice assertion, identify the complementary state
with a continuant, or infer that a real spectral saddle contributes.

Focused audit: [actual target traces, classification and bandwidth](../experiments/audit_actual_matching_edge_real_target_frames.py).

Primary-agent full analytical review: PASS. The reader checked the
rank-one trace equations, both physical adapters, exclusion of the
nonconjugate branch, both exact roots and their support intervals,
the generic bandwidth argument, and the inverse-turn pullback. The
input/output ordering in (9) is explicit.

Independent full analytical review and fresh redirected replay: PASS.
A second reader reproduced eight formal identities, thirty-six actual
local frames, seventy-two adapter row checks, thirty nonconjugate
support failures and 222 exact generic bandwidth entries. Neither
review infers compatibility with the other disks of the link.
