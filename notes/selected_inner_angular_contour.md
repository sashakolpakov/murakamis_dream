# A selected inner angular contour with coefficient one

28 October 2026. The late inner block of the five-crossing source
has a genuine noncancelling contour. This is a selected contour
calculation, rather than the existence of a formal critical point.
Its real-parameter version is proved below. A complex-parameter
reduction gives explicit one-variable boundary tests for transporting
the outer contour. The full outer selected asymptotic is not proved
here.

The exact whole-source transform is supplied separately by
[the finite five-crossing transform](five_two_cyclotomic_transform_proof.md).
The calculation below concerns its explicitly specified inner block
and does not use a Jones formula or a published asymptotic proof.

## 1. The exact inner block and its continuous source

Put Q=exp(2pi i/N), F_n=(Q;Q)_n and

    W_N(n,j)=Q^[-n(n+2)-j(n+1)] F_n^3/[F_j F_(n-j)],
                                                   0<=j<=n<N.

Use the exact marked factorial interpolation Fhat_N(z). Its
reflection and finite-shift identities are

    Fhat_N(z)Fhat_N(N-1-z)
                        =N exp[pi i z(z-N+1)/N],
    Fhat_N(z+L)/Fhat_N(z)=(Q^(z+1);Q)_L           (1)

for nonnegative INTEGER L, with the stated analytic continuation.
Thus, with L=N-1-n, the actual interpolation after the harmless
lattice factor exp(2pi i z) is exactly

    W_N(n,z)exp(2pi i z)
       =C_(N,n) exp[-pi i z(z-N+1)/N]
                              (Q^(z+1);Q)_L,
    C_(N,n)=F_n^3/N * exp[-2pi i n(n+2)/N
                              -pi i n(n-N+1)/N]. (2)

All constants in (2) are retained. It equals W_N(n,j) at every
selected integer j. The right side is an ENTIRE finite-product
function of z. Define its selected ordinary integral

    I_(N,n)=C_(N,n) integral_0^n
       exp[-pi i z(z-N+1)/N](Q^(z+1);Q)_L dz.     (3)

The separate [finite Abel--Plana comparison](source_preserving_inner_quadrature.md)
controls the difference
between the discrete inner sum and (3) by
O_K(log N)|F_n|^2 for n/N in a compact late interval. The contour
theorem below proves a positive exponential gap over precisely
that endpoint scale; hence that comparison does not erase its
selected saddle coefficient.

## 2. The selected critical point for real x

Let 1/2<x<1, X=exp(2pi i x). The equation

    XY^2+(1-X)Y-X=0                              (4)

has a unique root with |Y|<1. Write it as

    Y=-R exp(i alpha), 0<R<1, 0<alpha<pi/2,
    y_s=Log(Y)/(2pi i)+1=b+i eta,
    b=1/2+alpha/(2pi), eta=-log(R)/(2pi)>0.

Then 1/2<b<x. One direct verification uses
beta=2pi(1-x), h=-log R and the identities

    sinh(h)cos(alpha)=sin^2(beta/2),
    cosh(h)sin(alpha)=sin(beta/2)cos(beta/2).      (5)

They give one positive h and alpha in (0,pi/2). For x>=3/4,
b<x is immediate. For 1/2<x<3/4, the ratio of the equations
in (5) gives alpha<pi-beta, hence again b<x.

Let J be the holomorphic primitive of Log(2sin(pi z)) marked
from 0<z<1. Up to an x-only constant the inner phase is

    Psi_x(y)=-J(y)-J(x-y)
                       +pi i[(2-x)y-y^2].       (6)

The chosen root solves Psi_x'(y_s)=0 in this mark. It is the
continuation from the real late source, not the other quadratic
root, whose real logarithmic coordinate lies outside (0,x).

## 3. The horizontal contour has a unique global maximum

Shift the interval [0,x] to [0,x]+i eta. For y=s+i eta,

    d_s Re Psi_x(s+i eta)
       =1/2 log[(sin^2(pi(x-s))+sinh^2(pi eta)) /
                         (sin^2(pi s)+sinh^2(pi eta))]
                                      +2pi eta=:F(s). (7)

One has F(0)>0 and F(x)<0. The first is immediate. For the
second, put S=sin^2(pi x), h=2pi eta, a=sinh h and c=cosh h.
Equation (5) gives

    a^4+(1-S)a^2-S^2=0, 0<a<1.                  (8)

The desired F(x)<0 is equivalent to

    S>a(a+c)(c-1)=:R_0.

The polynomial P(z)=z^2+a^2z-a^2(1+a^2) is increasing for
z>=0 and has positive root S. If v=exp(h), direct factorization
gives

    P(R_0)=(v-1)^2(v+1)^2(v^2+1)(v^2-2v-1)
                                      (v^2-v+1)/(16v^4)<0,

because 1<v<1+sqrt(2). This proves F(x)<0.

The equation F(s)=0, after exponentiation and expansion of the
two sine squares, is a constant plus one sine and one cosine of
2pi s. It has at most two zeros in an interval of length x<1,
counting multiplicities. Opposite endpoint signs therefore force
exactly one zero. It is s=b, the already known critical point,
and it crosses from positive to negative. Thus y_s is a strict,
nondegenerate GLOBAL maximum of the real part on this horizontal
contour. The Gaussian square root is fixed by this actual
left-to-right orientation.

## 4. Both connecting segments are lower

Connect 0 to i eta, and x+i eta to x, using vertical segments.
All endpoint values below use the one-sided J mark from
0<Re y<Re x; evaluating a principal dilogarithm directly on its
cut can give the wrong value.

On the left segment y=i tau, tau>0, the imaginary part of
Psi_x'(y) is

    arg sin(pi(x-i tau))+pi(3/2-x)>0.

Consequently Re Psi strictly decreases upward. Its maximum is
the original endpoint y=0.

On the right segment y=x+i tau, tau>0, one obtains

    d_tau Re Psi_x(x+i tau)
       =arg sin(pi(x+i tau))+pi(3x-3/2)>0.

Indeed arg sin(pi(x+i tau))> -pi(x-1/2), leaving the positive
lower bound pi(2x-1). Its maximum is therefore the horizontal
endpoint x+i eta, strictly below the horizontal saddle.

It remains to compare the LEFT original endpoint with the saddle.
Restore the outer phase and define

    S(x,y)=3J(x)-J(y)-J(x-y)
                       +pi i(3x+2y-x^2-xy-y^2),
    D(x)=Re S(x,y_s(x))-2J(x).                   (9)

Then

    D(x)>0, 1/2<x<1.                            (10)

Here is a direct proof. The critical equation gives

    D'(x)=log[|1-X|/(R|1-Y|)].                  (11)

Use S_0=sin^2(pi x), a=sinh h, c=cosh h as in (8). Formula
(11) becomes

    D'(x)=1/2 log[2S_0 a/(ac+S_0)]+3h/2.        (12)

As a function of S_0 in (0,1), a and h are strictly increasing.
Also c/S_0 is strictly decreasing. To verify the latter, put
T=a^2; equation (8) gives

    T'=(T+2S_0)/(2T+1-S_0)>0,
    sign d_(S_0)(c/S_0)
       =sign[S_0 T'-2(1+T)]<0,

since after clearing its positive denominator the numerator is
S_0(T+2)-2(T+1)^2<0. Therefore
2S_0 a/(ac+S_0)=2/(c/S_0+1/a) is strictly increasing.
The right side of (12) is strictly increasing in S_0. Since
S_0 strictly decreases with x on (1/2,1), D''(x)<0.

Finally D(1/2+)=D(1-)=0. At x=1 the limiting saddle is y=1/2,
and J(1)=J(1/2)=0. At x=1/2 the saddle is
y=1/2+i asinh(1)/(2pi); the one-sided identities
Re J(1/2+i eta)=0 and Re J(-i eta)=-pi eta/2 make the two
real terms cancel. Strict concavity proves (10).

Thus every connector and the Abel--Plana endpoint scale is
strictly below the selected saddle, uniformly when x lies in
a compact subinterval of (1/2,1).

## 5. The resulting selected Gaussian, with its source coefficient

Let P'(z)=Log(1-exp(2pi i z)), with its inherited strip mark,
and put

    Phi_x(y)=P(y+1-x)-P(y)+pi i(y-y^2),
    a_x(y)=exp(-pi i y) /
       sqrt[(1-exp(2pi i y))(1-exp(2pi i(y+1-x)))].

For n/N=x in any compact K contained in (1/2,1), the selected
integral (3) satisfies uniformly

    I_(N,n)=C_(N,n) sqrt(N) a_x(y_s)
          sqrt[2pi/(-Phi_x''(y_s))]
          exp[N Phi_x(y_s)] (1+O_K(1/N)).         (13)

Every displayed factor is nonzero. The multiplier of this
Gaussian is ONE. This follows by an exact contour deformation
of the entire integrand (2); no thimble intersection is guessed.

For completeness, the finite product on the horizontal segment
has the uniform Euler--Maclaurin expansion

    (Q^(Ny+1);Q)_(N-1-n)
       =exp{N[P(y+1-x)-P(y)]} /
          sqrt[(1-exp(2pi i y))(1-exp(2pi i(y+1-x)))]
                                      *(1+O_K(1/N)).

Its arguments stay strictly inside the unit disk there, and
away from one, uniformly on K. The quadratic Gaussian in (2)
contributes exp[N pi i(y-y^2)]exp(-pi i y).
The two connector bounds follow with a uniform O(log N)
logarithmic product error, treating their simple endpoint
zeros by rectangle sums. Their strict phase gap makes them
exponentially negligible in (13). Ordinary one-variable complex
Laplace expansion at the unique horizontal maximum then proves
(13), including the orientation and coefficient one.

Combined with the finite Abel--Plana endpoint bound stated in
Section 1, the SAME selected Gaussian is the asymptotic of the
original discrete inner sum, uniformly on real compact K.
This is an inner source-selection theorem. Outer cancellation
is a further operation and has not been suppressed by wording.

## 6. A complex-x reduction for the actual outer contour

The following identities reduce the complex continuation to
explicit one-variable boundary tests. Let

    x=u+i h, 1/2<u<1,
    |1/X|<=2, X=exp(2pi i x),
    T=1/X-1,
    v=(T+sqrt(T^2+4))/2, Re sqrt(T^2+4)>0,
    Y=-v, y_s=b+i lambda=Log(Y)/(2pi i)+1.

The condition 0<Im T<2 is enough to make v lie in quadrant I;
it cannot cross an axis without T becoming real or satisfying
Im T>=2. Hence 1/2<b<min(u,3/4). The latter inequality follows
from the ratio of real and imaginary parts of v-1/v=T when
u<3/4; it is automatic when u>=3/4. The root has no collision
on this domain.

At the selected root,

    S_yy=-2pi i(v^2+1)/[v(v+1)],
    sign Re S_yy=sign(|v|^2-2Re v-1)<0.           (14)

For the last inequality write a=Re v>0, r=|v|^2. Then

    |1+v-1/v|^2=r+3+2a+(1-2a-4a^2)/r.

At r=2a+1 its excess over four is
(4a^2+2a+1)/(2a+1)>0, and it is strictly increasing for
r>=2a+1. Thus |1/X|<=2 forces r<2a+1. In particular the
selected root remains a nondegenerate strict horizontal maximum.

On y=s+i lambda, 0<=s<=u, one has

    F(s)=d_s Re S
      =1/2 log[(sin^2(pi(u-s))+sinh^2(pi(h-lambda))) /
                         (sin^2(pi s)+sinh^2(pi lambda))]
                              +pi(h+2lambda).    (15)

There are at most two horizontal stationary points. Also F(0)>0.
An exact proof of the latter is available directly from the root:
put R=|v| and c=cos(arg v). After squaring the equivalent
modulus inequality, its positive difference is

    2(c+1)[(R-1)^2(R+1)+2R^2(1-c)]>0,

after multiplication by a positive power of R. The sign, rather
than that irrelevant positive scaling, is what is used.

Together with (14), this shows that the maximum over the WHOLE
horizontal segment is either the selected saddle or the right
endpoint u+i lambda. Unlike the real-x case, F(u) can be positive;
there can be a second stationary point, which is a minimum.

The polygon 0 -> i lambda -> u+i lambda -> x has particularly
simple connectors. The left phase is strictly decreasing as a
function of its vertical parameter tau. Its maximum is therefore
at tau=min(0,lambda). On the right put

    theta_u(tau)=arg sin(pi(u+i tau)).

This is strictly decreasing. The vertical derivative of Re S is

    theta_u(tau)+pi(3u-5/2), tau<h,
    theta_u(tau)+pi(3u-3/2), tau>h.              (16)

Each connector segment is strictly concave. Its maximum is at
an endpoint or the single stationary value obtained by solving
theta_u(tau)=-pi(3u-c), c=5/2 or 3/2, when that value belongs
to the segment. Explicitly

    tau=(1/pi)artanh[tan(pi(3u-c))/(-cot(pi u))], (17)

with the actual arctangent range checked before using (17).

Consequently an outer contour construction need only bound
the selected outer action and these finitely many ONE-VARIABLE
endpoint/stationary connector functions. No sampling of the
whole two-dimensional polygon is required for a rigorous bound.

At the geometric outer x, diagnostic values are

    Re S(x,y_s)=0.450109610025218...,
    max left connector=0.10745960674786...,
    max right connector=0.43978988922391....

The right maximum occurs at tau=0.04913510458548..., rather
than at either endpoint. The exact formulas (14)--(17) reduce
the whole-contour comparison to one real parameter. The following
certificate completes those phase bounds; the displayed decimals
above are not used as proof.

## 7. Rigorous bounds for the full inner polygons and outer source edges

[The Arb certificate](../experiments/certify_selected_inner_contours.py)
uses 192-bit outward-rounded acb/arb arithmetic. Its
[saved result](../experiments/selected_inner_contour_certificate.json)
reports `RIGOROUS_ARB_PASS`. Polynomial root isolation, every
analytic function enclosure, every pass/fail comparison and every
interval subdivision are certified balls; floats are used only
for displaying already-proved bounds.

Let x_g=u_g+i h_g be the exact cubic point from
[the outer phase theorem](five_two_reduced_outer_contour_concavity.md),
and put h(u)=min(h_g,h_g(1-u)/(1-u_g)). The certificate proves:

* For .51<=u<=.99 on x=u+i h(u), ALL left inner connectors
  have phase below .200 and ALL right inner connectors have
  phase below .445. The two contour pieces require 523 and
  734 dyadic parameter cells respectively.
* On x=u-.1i, .51<=u<=.99, the maximum phase of the ENTIRE
  inner polygon, after adding the exact lower-kernel weight
  -.2pi, is below .400. This includes the selected horizontal
  saddle, the horizontal endpoint and both connectors; 187
  parameter cells suffice.
* For u in EACH of [.5099,.5101] and [.9899,.9901], every
  full inner polygon on the vertical outer source edges has
  phase below .440. On the upper edge 0<=h<=h(u) this is
  unweighted. On the lower edge -.1<=h<=0 it includes the
  actual kernel weight +2pi h. These four boxes require 388
  further cells. The real u variable is kept as its whole
  Arb interval, so these are two-parameter box enclosures,
  not evaluations at just u=.51,.99.

The total is 1832 verified cells. The same calculation encloses
the selected cubic rate between .45010 and .45012. Thus all
connector and lower-source bounds have a STRICT positive gap.
The phase calibration is supplied by the separate
[marked Bloch calculation](five_two_selected_bloch_calibration.md).

Here is why the maximum reductions make this a full certificate.
On each parameter cell the code encloses the selected quadratic
root and checks its first-quadrant branch. Formula (14) and
F(0)>0 imply that every horizontal maximum is either the saddle
or its right endpoint. The left connector maximum is one of
its two endpoints. On the right, the derivative is decreasing;
the code includes both endpoints and the unique candidate (17)
unless an interval sign proves it irrelevant. Ambiguous cases
are subdivided. It therefore cannot omit an actual maximum.
The interval cells cover both closed parameter ranges, including
their common cubic endpoint.

The [exact finite-height outer source formula](source_preserving_outer_finite_height_quadrature.md)
uses precisely these weights and edges. Its half-integer real
edges lie in the certified u boxes for every sufficiently large
N (N>=10000 is sufficient for its specified rounding). The
uniform factorial bound in that theorem includes BOTH inner
endpoints, with only polynomial factors; hence a certified
phase bound controls the actual whole inner function there.

The upper kernel also has an explicit gap. On this window
h(u)>.007. The outer theorem gives selected reduced phase
at most the cubic value, and the remaining upper connectors
are below .445. Consequently the full upper polygon, after
its kernel weight -2pi h, is below .407. Combining the upper,
lower and vertical bounds in the exact outer formula gives
an outer discretization error O(N^(5/2)exp(.440N)). This is
strictly below the selected cubic action. No outer alias or
finite source edge is discarded by its formal symbol.

These estimates supply the source-error and inner-contour inputs
for combining the exact finite transform, selected saddle and
marked volume calibration. They do not constitute a general
knot theorem; extension to broader bridge networks requires
analogous source-preserving reductions and contour bounds.
