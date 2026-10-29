# Proven dilogarithm and endpoint regions of the full original Euler atoms

28 October 2026. The actual finite crossing polynomials have two
rigorously distinguishable exponential modes. The dilogarithm mode is
selected uniformly on an explicit fixed open domain containing the
upper half unit disk and a neighborhood of the regular ideal shape.
The top-degree mode is selected throughout
a fixed exterior region. Along an explicit family of positive ideal
tetrahedra the two regions meet at a sharp amplitude threshold. Positive
ideal angles alone therefore do not justify replacing a full atom by
its dilogarithm expression throughout that chamber.

These are results for the full original polynomials, rather than a
nilpotent evaluation, a new positive model, or a claimed finite list of
all Stokes sectors. They do not identify an atom argument with a shape
coordinate in every knot presentation, or construct the required whole
knot contour deformation.

## 1. The full functions and their source

Fix N >= 2, Q = exp(2 pi i/N), H_N = 2 pi i/N, and

    F_k = (Q;Q)_k,
    u_N(z) = sum_(k=0)^(N-1) z^k/F_k,
    v_N(z) = sum_(k=0)^(N-1) (-1)^k Q^[k(k-1)/2] z^k/F_k.

The literal unchecked crossing has Euler factor v_N(q rho^2 E_1 F_2)
and its literal inverse has u_N of that same argument, as proved in
[the crossing-argument calculation](euler_atom_source_family_and_crossing_argument.md).
No other factors of that crossing are discarded here.

As ORDINARY scalar polynomials these satisfy

    u_N(Qz) - (1-z)u_N(z) = z^N/N,                    (1)
    (1-z)v_N(Qz) - v_N(z) = -z^N/N.                  (2)

The terms on the right will not be set to zero. Iterating around the
full Q orbit, and using product_(j=0)^(N-1)(1-Q^j z)=1-z^N,
gives the exact global finite-product representations

    u_N(z) = (1/N) sum_(k=0)^(N-1)
                       product_(r=1)^k (1-Q^(-r)z), (3)
    v_N(z) = (1/N) sum_(k=0)^(N-1) (z;Q)_k.         (4)

Initially the iteration may be performed at z != 0; polynomial
continuation proves the formulas everywhere. Thus the cyclic norm
and the affine source are retained in these functions.

There is also an exact Cauchy representation useful for a future
contour comparison. Mark, on |w|<1,

    D_N(w) = product_(j=1)^(N-1) (1-Q^j w)^(j/N),
    D_N(0)=1,
    A_(N,u)=D_N, A_(N,v)=D_N^(-1).

The first N Taylor coefficients of A_(N,u) and A_(N,v) are those
of u_N and v_N respectively. Indeed for 1 <= k < N,

    [w^k] log D_N = 1/[k(1-Q^k)].

For either atom p_N=u_N or v_N and ANY 0<r<1,

    p_N(z) = (1/(2 pi i)) integral_(|w|=r)
             A_(N,p)(w) [1-(z/w)^N]/(w-z) dw.      (5)

The apparent pole at w=z is removable. Formula (5) is valid for
every scalar z, not just |z|<r. Separating its two terms gives, when
|z|<r, the exact analytic expression A_(N,p)(z) minus a retained
z^N Cauchy remainder. Agreement of nilpotent jets by itself would
not remove that remainder.

## 2. The threshold constant

Put

    J(s)=integral_0^s log(2 sin(pi y)) dy, 0<=s<=1,
    z(t)=1-exp(-2 pi i t), 0<t<1/2,
    r(t)=|z(t)|=2 sin(pi t).

There is a unique t_* in (0,1/2) satisfying

    -J(t_*) - (1-t_*) log r(t_*) = 0.              (6)

Numerically,

    t_* = 0.20877342895233375656...,
    R_* = r(t_*) = 1.21971547612163368901....

These decimals are descriptive, not premises of the results.
For B(t)=-J(t)-(1-t)log r(t),

    B'(t)=-(1-t) pi cot(pi t)<0,
    B(0+)=+infinity, B(1/2)=-log(2)/2.

This proves existence and uniqueness. The equivalent exterior
characterization is

    log R_* = max_(0<s<=1) J(s)/s.                 (7)

To see it, the numerator of the derivative of J(s)/s is
G(s)=s J'(s)-J(s), with G'(s)=s pi cot(pi s). It is positive
up to a unique zero in (1/2,1) and then negative. Using
J(1-t)=-J(t), that zero is s=1-t_* and (6) gives (7).

## 3. A full-polynomial dilogarithm theorem beyond the small disk

Let K be any compact subinterval of (0,t_*) and W any compact
subset of C. Uniformly for t in K, w in W and

    z=z(t) exp(w/sqrt(N)),

one has

    v_N(z) = (1-z)^(1/2)
                 exp[Li_2(z)/H_N] (1+O_(K,W)(N^(-1/2))). (8)

Uniformly for z=conjugate(z(t)) exp(w/sqrt(N)),

    u_N(z) = (1-z)^(-1/2)
                 exp[-Li_2(z)/H_N] (1+O_(K,W)(N^(-1/2))). (9)

All logarithms, square roots and Li_2 continue from z=0 along
the indicated upper or lower arc. In particular these full atoms
are nonzero throughout those windows for all sufficiently large N.
The coefficient of the displayed dilogarithm mode is exactly one
in those marks; it is not an undetermined nonzero normalization.

At t=1/6, z(t)=exp(pi i/3), the regular ideal shape. Thus (8)
and (9) control complex N^(-1/2) windows crossing |z|=1. They
are not merely estimates on a disk strictly inside that circle.
Section 6 upgrades these windows to a fixed open domain by the exact
finite rotation equation, retaining its affine source throughout.

### Direct proof retaining all coefficients

For s=k/N in a compact subinterval of (0,1), elementary
Euler--Maclaurin and Stirling estimates give

    P_(N,k):=|F_k|
       = sqrt(2N sin(pi s)) exp[N J(s)] (1+O(1/N)). (10)

For example apply Euler--Maclaurin to
log(sin(pi s)/(pi s)) after removing the k! factor at zero.
Globally, for 0<=k<N, the weaker uniform statement

    log P_(N,k) = N J(k/N)+O(log N)                (11)

suffices. It follows by subtracting both endpoint logarithms:
log(2 sin(pi s))-log s-log(1-s) extends smoothly to [0,1],
and the remaining two sums are factorials. In (11), k=0 is
interpreted separately as P_(N,0)=1.

The exact phases are

    [z^k]v_N = exp[-pi i k/2 + pi i k(k-3)/(2N)]/P_(N,k),
    [z^k]u_N = exp[ pi i k/2 - pi i k(k+1)/(2N)]/P_(N,k).

For v define

    S_v(s,z)=s Log z-J(s)+(pi i/2)(s^2-s).

At z=z(t), S_v has its stationary point at s=t, since
Log z(t)=log r(t)+i(pi/2-pi t), and

    S_v''(t,z(t))=-pi cot(pi t)+pi i.             (12)

The real part of the phase is

    phi_t(s)=s log r(t)-J(s).

Its only interior stationary points are the maximum s=t and
the minimum s=1-t. Its endpoint values are 0 and log r(t).
The first is strictly below phi_t(t), and the second is strictly
below precisely when B(t)>0. Thus for t in K the UNIQUE global
amplitude maximum is s=t, with a uniform gap away from it.
Estimate (11) therefore bounds every discarded portion of the
FULL finite sum exponentially relative to the central band.

In that band (10), the displayed exact phase, and the variable
xi=(k-Nt)/sqrt(N) reduce the sum to a convergent complex Gaussian.
Its real quadratic part is strictly negative by (12). The usual
Taylor remainder is bounded by an integrable Gaussian times a
polynomial; the mesh is 1/sqrt(N). Both errors are O(N^(-1/2)),
uniformly also with the bounded complex tilt w. In particular no
unknown stationary-cycle coefficient is inserted in this calculation.

At w=0 the resulting leading coefficient simplifies exactly to

    exp(-3 pi i t/2) /
         sqrt(sin(pi t)(cot(pi t)-i)) = exp(-pi i t).

Also, with the stated marks,

    S_v(t,z(t))=Li_2(z(t))/(2 pi i),
    exp(-pi i t)=(1-z(t))^(1/2).

The action identity follows by differentiating along t and using
Log(1-z(t))=-2 pi i t, with common value zero at t=0.
For bounded w the tilted Gaussian contributes exp[-w^2/(2S_v'')].
This is exactly the quadratic Taylor term of
N Li_2(z(t) exp(w/sqrt(N)))/(2 pi i), because
d^2[Li_2(z)/(2 pi i)]/d(Log z)^2=-1/S_v'' at the saddle.
The remaining action and amplitude errors are O(N^(-1/2)).
This proves (8). The same calculation with
S_u(s,z)=s Log z-J(s)+(pi i/2)(s-s^2), or the exact identity

    u_N(z)=conjugate(v_N(Q conjugate(z))),

proves (9). Its Gaussian factor is exp(-pi i t)=(1-z)^(-1/2)
on the lower arc, as required.

## 4. A uniform full exterior expansion

For EVERY fixed R>R_* and integer d>=1, uniformly for |z|>=R,

    u_N(z) = z^(N-1)/N [
      sum_(k=0)^(d-1) (-1)^k Q^[-k(k+1)/2] F_k z^(-k)
                                  +O_(R,d)(N^(-d))], (13)
    v_N(z) = Q z^(N-1)/N [
      sum_(k=0)^(d-1) Q^k F_k z^(-k)
                                  +O_(R,d)(N^(-d))]. (14)

Here N>d. In particular both are nonzero for all sufficiently
large N throughout that exterior region, and their exponential
rate at every fixed z there is log|z|. The leading factors are
literal top coefficients of the original finite polynomials.

For the proof, F_(N-1)=N gives the exact reversed coefficients

    [z^(N-1-k)]u_N = (-1)^k Q^[-k(k+1)/2] F_k/N,
    [z^(N-1-k)]v_N = Q^(k+1) F_k/N.               (15)

In either reversed series the modulus of its k-th coefficient
term is P_(N,k)|z|^(-k). For k>=epsilon N, (7) and (11) bound
their sum by a polynomial in N times
exp[-epsilon N log(R/R_*)]. For k<epsilon N choose epsilon
small enough that 2 pi epsilon/R<1/2. Successive term moduli
then have ratio at most 2 pi epsilon/R. Since the d-th term is
O_(R,d)(N^(-d)), its tail is bounded by a geometric series.
This proves (13)--(14) without an oscillatory cancellation premise.

## 5. A genuine distinction inside the positive ideal-shape chamber

For every 0<t<1/2, z(t) is in the upper half-plane and is a
valid positively oriented ideal tetrahedron shape. Its three
angles are

    (pi/2-pi t, 2 pi t, pi/2-pi t).

For 0<t<t_* equation (8) yields

    lim (1/N)log|v_N(z(t))|=Im Li_2(z(t))/(2 pi).

For t_*<t<1/2, r(t)>R_*, so (14) instead yields

    lim (1/N)log|v_N(z(t))|=log r(t)
                          > Im Li_2(z(t))/(2 pi). (16)

Indeed the difference of the right sides is -B(t)>0. The
transition t=t_* itself is not evaluated here. Nor do the two
proved regions assert that all other complex sectors are exhausted.

Consequently a Rivin volume maximum and positivity of its ideal
angles do not alone establish a uniform dilogarithm replacement
of every original atom on a proposed global deformation. A whole
word proof must retain the exact finite source (1)--(5), control
the actual argument maps, and either stay in justified atom regions
or account for the endpoint modes and any other sectors crossed.
This is an obstruction to that inference, not to the volume
conjecture or to a source-preserving whole-word cancellation.

## 6. Exact rotation gives a fixed open dilogarithm domain

There is a larger explicit uniform result. On the upper half-plane
use the principal continuation of Li_2 and put

    g(z)=Im Li_2(z)/(2 pi),
    D_+={z: Im z>0 and g(z)>log|z|},
    D_-=conjugate(D_+).

Then, uniformly on EVERY compact subset of D_+,

    v_N(z)=(1-z)^(1/2) exp[Li_2(z)/H_N]
                                      (1+O(N^(-1/2))). (17)

Uniformly on every compact subset of D_-,

    u_N(z)=(1-z)^(-1/2) exp[-Li_2(z)/H_N]
                                      (1+O(N^(-1/2))). (18)

The marks are the same ones as in Section 3. These statements
therefore give a nonzero leading coefficient ONE throughout fixed
open domains, not just on the arc or on shrinking windows. The exact
cyclic source has been estimated, rather than discarded. In particular
all large-N atoms in (17)--(18) are nonzero on those compact subsets.

The domain D_+ contains the entire upper half of |z|<=1. For
1<|z|<R_* it contains an angular bulge described by its displayed
inequality. It has no point with |z|>=R_*.

### Angular geometry of this domain

For z=r exp(i theta), 0<theta<pi,

    partial_theta g=-log|1-z|/(2 pi),
    partial_theta^2 g=-r sin(theta)/(2 pi |1-z|^2)<0. (19)

For 0<r<2 its unique angular maximum is at
theta_a(r)=arccos(r/2). That point is exactly z(t) of Section 2,
with r=2 sin(pi t). Its excess over log r is B(t). Consequently
the superlevel set g>log r on a circle is an interval containing
that anchor, nonempty precisely for r<R_*. For r>=2, |1-z|>=1
and g is decreasing in theta; its boundary maximum is
g(r+i0)=log(r)/2<log r. Thus there is no additional component
at larger r. For r<=1, g is strictly positive in the upper
half-plane, whereas log r<=0, which proves the asserted disk
inclusion. Positivity follows as well by integrating
partial_r Im Li_2(r exp(i theta))=-arg(1-r exp(i theta))/r>0
from r=0.

On each angular path inside that superlevel interval, concavity
implies that the minimum of g-log r occurs at one of its two
endpoints. For a compact target set K contained in D_+, all paths
from the corresponding anchors to K therefore form a compact
upper-half-plane set C and obey

    min_C [g(z)-log|z|] >= delta_K > 0.             (20)

The anchors have t in a compact subinterval of (0,t_*).
In particular C avoids both the singular point z=1 and all real
logarithmic cuts. An O(1/N) angular adjustment of its anchors
preserves a fixed positive gap for large N.

### Propagation using the actual affine equation

Put

    V_N(z)=(1-z)^(1/2) exp[Li_2(z)/H_N].

A Taylor expansion on a fixed compact neighborhood of C gives

    (1-z)V_N(Qz)/V_N(z)=1+O_C(N^(-2)).             (21)

To check the cancellation explicitly, D_z=z partial_z satisfies
D_z Li_2=-Log(1-z) and D_z^2 Li_2=z/(1-z).
The order-H_N term from Li_2(Qz)/H_N is therefore
+(H_N/2)z/(1-z), and the order-H_N term from the square-root
amplitude is its negative. This is why the actual prefactor in
(17) is necessary.

For any z in K choose an integer j so z_0=Q^(-j)z has the same
radius as z and lies within pi/N in angle of its anchor. The
partial rotation path z_l=Q^l z_0 from z_0 to z stays within
O(1/N) of C, uses O(N) steps, and can be taken forward or backward.
The anchor theorem (8) applies, since its logarithmic displacement
is O(1/N), and gives

    v_N(z_0)/V_N(z_0)=1+O_K(N^(-1/2)).

Write R_l=v_N(z_l)/V_N(z_l) and
c=z_0^N/N=z_l^N/N. Dividing the EXACT equation (2) by V_N yields

    R_(l+1)=(1+epsilon_l)^(-1)
                        [R_l-c/V_N(z_l)],
    epsilon_l=(1-z_l)V_N(z_(l+1))/V_N(z_l)-1
                                               =O_K(N^(-2)). (22)

The inverse of (22) is equally exact for a backward step. By
(20) and the bounded nonzero square-root amplitude on C,

    |c/V_N(z_l)| <= (C_K/N) exp(-delta_K N/2).     (23)

Products of O(N) factors 1+epsilon_l differ from one by O_K(1/N).
Summing the actual source terms (23) is exponentially small.
Thus (22) proves (17), with the same leading coefficient one as
at the anchor. No assumption about the exhaustion of Stokes modes
or an analytic continuation of asymptotic jets is involved: the
propagation is the exact original polynomial recurrence.

Finally use the exact conjugation identity of Section 3. On a
compact subset of D_-, Q conjugate(z) remains in D_+ for large N.
Conjugating (17) and expanding by one H_N step gives

    (1-Q^(-1)z)^(1/2)
       exp[-Li_2(Q^(-1)z)/H_N]
       =(1-z)^(-1/2) exp[-Li_2(z)/H_N](1+O(1/N)).

This proves (18), including its mark and prefactor.

The selected dilogarithm domain is large enough to contain the
regular ideal tetrahedron in a fixed complex neighborhood. It
does not contain the entire upper ideal-shape chamber: Section 5
gives valid positive shapes where the exact endpoint mode is
larger. Proving a whole-knot contour can be kept in the appropriate
atom domains, or transporting it across the remaining regions
with all source terms, is still a separate problem.

There is nevertheless a simple classical atlas relevant to that
choice. For every positive ideal shape z, the three usual quad-type
shapes

    z, 1/(1-z), 1-1/z

all belong to the upper half-plane and their product is -1.
At least one therefore has modulus <=1 and belongs to D_+.
Thus the three inverse images of D_+ under these transformations
cover the entire positive ideal-shape chamber. On compact sets
of nondegenerate positive angles, the resulting chosen atom charts
have a uniform positive source gap after taking a finite subcover.
This supplies possible CLASSICAL chart choices. It does not supply
an exact quantum change of the actual Euler polynomial, its full
word argument, the source or the contour; those transformations
must still be established with their boundary terms.

[The saved audit](../experiments/full_euler_atom_regions_results.json)
checks the exact representations and reverse coefficients, and
compares the full-polynomial asymptotics on the arc, complex windows
and exterior region. The direct estimates above are the proofs.
