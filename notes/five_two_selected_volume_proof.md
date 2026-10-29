# A selected-contour proof for the original five-crossing prototype

28 October 2026. This assembles an independent, computer-assisted proof
of the volume asymptotic for the ORIGINAL normalized Kashaev invariant
of the marked 7/3 five-crossing knot 5_2. It uses exact finite source
transforms, explicit contours, and outward-rounded interval bounds.
No Jones asymptotic or published quantum-state asymptotic theorem is an
input. This is a prototype for the broader goal, not a proof for a broad
class of hyperbolic knots.

Coverage only: this knot's asymptotic is already the subject of
[Ohtsuki, Quantum Topology 7 (2016), 669-735](https://ems.press/journals/qt/articles/14527).
Only the publisher's bibliographic record and abstract were consulted
for that coverage check. No novelty claim is made for the knot case,
and that paper's proof is not an input to the argument below.

## 1. Statement and normalization

Let K_N denote the original reduced Kashaev invariant with the cut,
Cartan, cups/caps and zero framing specified in
[the literal four-plat source](five_two_whole_source_reduction.md).
Thus K_2=-7 in this handedness. Let v be the upper nonreal root of

    v^3-v^2+1=0,
    X=1/(1+v^2), Y=-v,
    x_g=1+Log(X)/(2pi i), y_g=1+Log(Y)/(2pi i).

Write J'(z)=Log(2sin(pi z)) on 0<Re z<1 with J(0)=0, and

    S(x,y)=3J(x)-J(y)-J(x-y)
                      +pi i(3x+2y-x^2-xy-y^2),
    S_g=S(x_g,y_g).

Then

    K_N=C N^(3/2) exp(N S_g) [1+O(1/N)],        (1)
    C != 0,
    Re S_g=Vol(S^3 minus 5_2)/(2pi).            (2)

The O constant is for this fixed knot and normalization. In particular

    lim_(N->infinity) (2pi/N)log|K_N|
                           =Vol(S^3 minus 5_2). (3)

The phase S_g has its stated logarithmic mark, not a value chosen
modulo a constant after taking absolute values. The constant in (1) is

    C=2pi a(x_g,y_g)/
                    [sqrt(-S_yy(x_g,y_g)) sqrt(-W''(x_g))],
    a(x,y)=sqrt(2)
       exp{[3Log sin(pi x)-Log sin(pi y)-Log sin(pi(x-y))]/2
                                             -pi i(3x+2y)}, (4)
    W(x)=S(x,y_s(x)).

The root y_s and both Gaussian square roots are fixed below by the
actual oriented contours. In particular the principal square roots
of -S_yy and -W'' at the selected point have positive real parts.
Every factor of (4) is nonzero.

## 2. Exact original finite source and controlled real collars

The [finite whole-meridian transform](five_two_cyclotomic_transform_proof.md)
proves, before taking any asymptotic, that

    K_N=sum_(0<=j<=n<N)
       Q^[-n(n+2)-j(n+1)] F_n^3/[F_j F_(n-j)],
    Q=exp(2pi i/N), F_n=(Q;Q)_n.                (5)

This identity retains the original normalization and all fixed-root
meridian derivatives. It is a finite q-binomial proof, not root-color
interpolation.

The uniform real factorial estimate, including both endpoint rows,
gives for each summand in (5)

    log|summand|=N A(n/N,j/N)+O(log N),
    A(x,y)=3J(x)-J(y)-J(x-y).                   (6)

Let c_*=max_[0,1]J=J(5/6), so 2c_*=Vol(4_1)/(2pi)<.324.
For x<=.51, J(x)<=.01 log 2, and J(y),J(x-y)>=-c_*.
Thus A<.345 throughout that low-index region.

For x>.5 the REAL angular Hessian of A is strictly negative:
if a=cot(pi x), b=cot(pi y), c=cot(pi(x-y)), then b+c>0,
a=(bc-1)/(b+c)<0 and det Hess A/pi^2=3-2bc>1.
Its inner maximum is therefore at y=x/2. For x>=.99,

    A(x,y)<=3J(x)-2J(x/2)
       <=3*.01[1-log(.04)]+.01 log 2 <.134.    (7)

Here 2sin(pi t)>=4t for 0<=t<=1/2 bounds J(x), and
J(x/2)>=-.005 log 2 bounds the other term. Enlarging these
strict bounds slightly handles a change of at most 1/N in
either cutoff.

Take a_N=ceil(.51N+1/2), b_N=floor(.99N-1/2). The omitted
terms of (5) have total size O(N^B exp(.345N)) for some fixed B.
There are only O(N^2) terms, already included in this polynomial.

## 3. Inner quadrature with the original endpoint source

For n in this window, use the ENTIRE interpolation

    f_(N,n)(w)=Q^[-n(n+2)-w(n+1)]
               F_n^3/[Fhat_N(w)Fhat_N(n-w)] exp(2pi i w).

It agrees with the original summand at every allowed integer w.
Exact factorial reflection turns it into a Gaussian times the
finite product (Q^(w+1);Q)_(N-1-n). The
[inner quadrature theorem](source_preserving_inner_quadrature.md)
proves

    |sum_(j=0)^n f_(N,n)(j)-integral_0^n f_(N,n)(w)dw|
                          <=C log(N+1)|F_n|^2.             (8)

Summing (8) costs at most C log(N+1) K_(4_1),N, whose proved
exponent is 2c_*<.324. All inner discrete corrections are
therefore below the selected rate; no Fourier mode is assumed.

Define the holomorphic outer function using the SAME interpolation:

    g_N(z)=exp(4pi i z) integral_0^z
       Q^[-z(z+2)-w(z+1)]
         Fhat_N(z)^3/[Fhat_N(w)Fhat_N(z-w)] exp(2pi i w)dw. (9)

At integer z=n its value is exactly the integral in (8).
Thus the original invariant equals sum_(n=a_N)^(b_N)g_N(n),
up to the explicitly bounded collar and inner-quadrature errors.

## 4. Exact outer quadrature, with all four source edges

Set L=a_N-1/2, R=b_N+1/2, ell=L/N, r=R/N. Define

    u_g=Re x_g, h_g=Im x_g, c=h_g/(1-u_g),
    h(u)=min(h_g,c(1-u)),
    x_+(u)=u+i h(u), x_-(u)=u-.1i, ell<=u<=r.             (10)

The [finite-height outer residue formula](source_preserving_outer_finite_height_quadrature.md)
expresses the original integer sum EXACTLY as the unweighted
integral over z=N x_+(u), plus:

* the upper contour with kernel 1/(exp(-2pi i z)-1);
* the lower contour with kernel 1/(exp(2pi i z)-1);
* the two upper vertical source edges with weights
  1/(1+exp(-2pi t));
* the two lower vertical source edges with weights
  1/(1+exp(2pi t)).

The half-integer edges enclose precisely the original integers.
The formula retains the off-lattice exp(4pi i z) character,
rather than silently replacing the selected Poisson source.

For each complex x on these paths the actual inner contour can
be changed, by holomorphy, to

    0 -> i lambda(x) -> Re x+i lambda(x) -> x,
    T=exp(-2pi i x)-1,
    v(x)=[T+sqrt(T^2+4)]/2,
    y_s(x)=1/2+Log(v(x))/(2pi i),
    lambda(x)=Im y_s(x).                                  (11)

The square-root branch puts v in quadrant I. All factorial
arguments y,x-y have nonnegative real part, at most .99,
and stay in a bounded imaginary range. The endpoint-uniform
Gamma-product bound in the outer note proves

    |g_N(Nx)|<=C N^(3/2) exp[N G(x)],
    G(x)=max_(inner polygon) Re S(x,y).                    (12)

Thus an endpoint singularity contributes at most a polynomial
factor; the interior asymptotic is not being applied at zero.

## 5. The rigorous whole-contour bounds

There are two independent types of evidence here.

The [analytic outer concavity proof](five_two_reduced_outer_contour_concavity.md)
shows that W(x)=S(x,y_s(x)) has its unique global maximum of
real part on x_+ at x_g. It proves both the constant-height
and sloped segments, using their explicit algebraic Hessian.

The [analytic inner maximum reduction](selected_inner_angular_contour.md)
shows that the full horizontal inner segment has its maximum
at the selected saddle or the RIGHT endpoint. Both vertical
connectors reduce to their endpoints and at most one explicit
stationary point. It proves these assertions for the whole
complex strip used in (10)-(11), not merely on sampled points.

The resulting one-variable tests have the following certified
outward-rounded Arb bounds:

| Actual contour piece | Certified phase upper bound |
|---|---:|
| Upper inner left connector | .200 |
| Upper inner right connector, including its interior maximum | .445 |
| Entire lower inner polygon, after the outer kernel weight | .400 |
| All four outer vertical source edges, with their prescribed weights | .440 |
| Selected critical value | .45010 < Re S_g < .45012 |

The executable proof is
[certify_selected_inner_contours.py](../experiments/certify_selected_inner_contours.py),
with [the interval certificate](../experiments/selected_inner_contour_certificate.json).
It uses 192-bit acb/arb arithmetic and covers its closed parameter
intervals by 1,832 verified dyadic cells. Floating-point displays
are not used in a passing comparison. Boundary values use the
one-sided J mark, including Re J(i tau)=-pi|tau|/2.

The vertical source boxes include u in [.5099,.5101] and
[.9899,.9901], so contain the rounded half-grid endpoints for
all sufficiently large N. The top and bottom curve bounds hold
throughout [.51,.99]. On the upper curve h>=.007, so its weighted
phase is at most .45012-2pi*.007<.407, using the analytic
outer maximum and the certified inner connectors.

Equation (12) and the EXACT outer formula consequently give

    sum_(n=a_N)^(b_N) g_N(n)
       =integral_(N x_+) g_N(z)dz
                              +O(N^(5/2) exp(.440N)).       (13)

The still retained inner connectors of the MAIN upper integral
have total size O(N^B exp(.445N)). This is below Re S_g.
No cancellation assumption is used to discard any of these pieces.

## 6. The surviving local Gaussian is nonzero

On the upper horizontal inner segment, the selected saddle is
a strict nondegenerate maximum; the analytic proof gives

    S_yy=-2pi i(v^2+1)/[v(v+1)], Re S_yy<0.
    W''=2pi i (v^2+v+4)(v^2+v-1)/(1-v^4).

On a fixed complex neighborhood of x_g all connector gaps persist
uniformly. The actual
interpolation has its nonzero analytic interior amplitude

    exp(4pi i Nx)K_N(Nx,Ny)
        =sqrt(N) a(x,y) exp[N S(x,y)] (1+O(1/N)),           (14)

with a as in (4). Ordinary one-variable Gaussian integration
on the specified inner segment gives

    g_N(Nx)=N a(x,y_s(x)) sqrt(2pi/[-S_yy(x,y_s(x))])
                                  exp[N W(x)](1+O(1/N)).  (15)

Equation (15) holds uniformly on that fixed complex neighborhood;
away from it only the absolute phase estimates are used.
This Gaussian has coefficient one: the integral was deformed
from its actual finite interval to this single horizontal
maximum, with its connectors separately bounded.

The analytic outer proof gives Re W''(x_g)<0 and
Im W''(x_g)<0, and 0<c<1. Therefore both tangent directions
1 and 1-i c of the bent upper curve belong to the same
negative Gaussian cone. The two oriented half-rays combine
to the full Gaussian; there is no undetermined intersection
coefficient at the kink. A local contour deformation within
that cone also gives the usual integer-power expansion.

Outside any fixed neighborhood of x_g the strict analytic
outer maximum and the certified inner endpoint bounds give
an exponential gap. Integrating (15), including dz=N dx,
therefore gives (1) with precisely (4). Its power N^(3/2)
is N^2 from the two integration measures, sqrt(N) from the
factorial amplitude, and N^-1 from two nondegenerate
Gaussian variables. Every omitted contribution in Sections
2-5 has a strictly smaller exponential rate.

## 7. Exact marked volume calibration and scope

[The explicit Bloch calibration](five_two_selected_bloch_calibration.md)
proves, at this same marked critical point,

    2pi Re S_g=-3D(X)+D(Y)+D(X/Y)=3D(v)
                                =Vol(S^3 minus 5_2).      (16)

The first equality uses the marked stationary equations, so
all logarithmic modulus terms are accounted for. The second
uses one explicit five-term relation and three duplications.
The last uses the independently audited three-tetrahedron
positive angle maximum and the actual knot marking. Neither
numerical agreement nor equality of trace fields is the
calibration argument. Equations (1) and (16) prove (3).

The broad hyperbolic-knot goal remains open. The reusable part
is concrete: an exact finite bridge transform; quadrature whose
errors retain and bound the original endpoints; and a certified
contour with one nonzero geometric Gaussian. Extending these
properties to a sufficiently broad class is required before
claiming a general torsor or A-polynomial volume theorem.

[Finite-level normalization diagnostics](../experiments/audit_five_two_selected_volume.py)
check the displayed nonzero prefactor and marked action against the
exact original double sum through N=192. They support the normalization
audit; the proof of the limit is the argument and interval certificate
above, not extrapolation of those values.

Assembly audit, 28 October: two independent agent reviews checked the
whole proof, including the finite source identity, both quadratures,
the analytic maximum reductions and outward-rounded certificate, the
fixed-neighborhood Gaussian expansion, its prefactor and contour
orientation, and the exact Bloch/three-tetrahedron calibration. Both
reported no remaining conditional source or cycle identification for
this prototype. The root review independently checked the source
transform, quadrature signs and endpoint estimates, reran the rigorous
certificate, and verified the marked finite-level normalization.

