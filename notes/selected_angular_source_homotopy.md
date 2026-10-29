# A source-sensitive angular homotopy: proved bounds and the remaining cycle theorem

28 October 2026. This note records two proved analytic facts useful for
transporting a selected angular source: an exponential boundary bound,
and properness of the critical set for a particular lattice-equivalent
phase homotopy. It also records the exact coefficient projection which
kills the dominant scalar endpoint expansion in a natural prototype
contour. These facts do not yet prove a selected geometric contribution.

The double sum below is now the exact transform proved in
[the finite five-crossing calculation](five_two_cyclotomic_transform_proof.md).
Its original triple source and all normalizations are retained.
Numerical homotopy continuation results are separated from the
proved lemmas. The subsequent selected contour argument is in
[the inner contour note](selected_inner_angular_contour.md); the
homotopy observations here alone are not that source proof.

## 1. The finite source and its exact phase

Let Q=exp(2 pi i/N), F_n=(Q;Q)_n. The candidate at completeness is

    Z_N=sum_(0<=j<=n<N) W_N(n,j),
    W_N(n,j)=Q^[-n(n+2)-j(n+1)] F_n^3/[F_j F_(n-j)]. (1)

Put x=n/N, y=j/N and J(s)=integral_0^s log(2sin(pi r))dr.
The actual factor phases give EXACTLY on this lattice

    W_N(n,j)=|W_N(n,j)|
       *exp{iN B(x,y)-pi i(3x+2y)},
    B(x,y)=pi(3x+2y-x^2-xy-y^2).                  (2)

The more immediate phase is -pi(x+x^2+xy+y^2). Its difference
from B is 4pi x+2pi y, whose N-fold exponential is one at
EVERY selected lattice point. This is a change of interpolation
mark with no change of the original finite source at the endpoint.

Define the actual finite homotopy of this candidate sum by

    Z_N(t)=sum |W_N(n,j)|
       *exp{it[N B(x,y)-pi(3x+2y)]}, 0<=t<=1.     (3)

At t=0 every summand is positive, and at t=1 (3) is exactly (1).
This is a specified deformation of the entire finite source, not
an inference from formal jets. It does not say that intermediate
t is a knot invariant or a quantum-group parameter.

On the holomorphic triangle

    T={ (x,y): 1/2<Re x<1, 0<Re y<Re x },

mark L(z)=Log(2sin(pi z)) by its real value on 0<z<1.
The sine has positive real part throughout that strip, so this
mark is holomorphic. Let J be its primitive agreeing with the
real J above, and put

    A(x,y)=3J(x)-J(y)-J(x-y), S_t=A+i t B.

The leading phase of (3) is S_t. Its derivatives are

    S_(t,x)=3L(x)-L(x-y)+it pi(3-2x-y),
    S_(t,y)=-L(y)+L(x-y)+it pi(2-x-2y).           (4)

The exact factorial interpolation supplies an actual analytic
summand with these uniform leading terms; no scalar exterior
Euler approximation is needed for that construction.

## 2. Strict real concavity and the actual boundary envelope

On the REAL late triangle 1/2<x<1, 0<y<x, A is strictly concave.
Indeed put a=cot(pi x), b=cot(pi y), c=cot(pi(x-y)). Then

    H_A/pi=[[3a-c,c],[c,-b-c]],
    b+c=sin(pi x)/[sin(pi y)sin(pi(x-y))]>0,
    a=(bc-1)/(b+c)<0.

The lower diagonal is negative, and

    det H_A/pi^2=3-2bc>1.                         (5)

Thus the real positive sum at t=0 has one nondegenerate late
interior maximum. Its y-coordinate is x/2. If
c_0=cos(pi x/2), the remaining equation is

    32(1-c_0^2)c_0^3=1,

which has one root in the interval corresponding to 1/2<x<1.
Numerically x=0.78786562191785..., y=x/2. The phase maximum
is about 0.6124533677523. These decimals are descriptive; the
uniqueness follows from strict concavity and the boundary signs.

Let

    c_*=max_(0<=s<=1)J(s)=J(5/6)=v_3/(2pi),

where v_3 is the regular ideal tetrahedron volume. The uniform
root-factorial estimate gives

    log|W_N(n,j)|=N A(n/N,j/N)+O(log N)            (6)

on the ENTIRE closed triangle, including its endpoint rows.
The implied constant is independent of n,j,N.

For x<=1/2, J(x)<=0 and J(s)>=-c_*, hence

    A(x,y)<=2c_*.

On y=0 or y=x one has A=2J(x)<=2c_*. On x=1,
J(y)+J(1-y)=0 and A=0. Therefore the complete low-n region
and every triangular boundary face have absolute exponential
envelope at most

    2c_*=v_3/pi=0.32306594721945....              (7)

By continuity the same statement, with arbitrarily small fixed
error, holds in fixed collars of those faces. More precisely for
every eta>0 there is delta>0 such that the portion outside

    K_delta={1/2+delta<=x<=1-delta,
                         delta<=y<=x-delta}

has absolute sum <=N^C exp[N(2c_*+eta)], uniformly for ALL
0<=t<=1 in the exact finite homotopy (3). This includes the
number of lattice terms, which is only O(N^2).

This is an actual absolute source bound for (1)--(3), rather
than a bound on a proposed saddle coefficient. It places all
possible contributions above that envelope in a fixed real
interior subtriangle. A higher selected exponent is still to
be proved, so this is not used as a relative error statement.

## 3. The good-gauge critical set cannot escape on a fixed real subtriangle

**Properness lemma.** Fix delta>0 and let t range over [0,1].
All critical points of S_t with

    1/2+delta<=Re x<=1-delta,
    delta<=Re y<=Re x-delta

have uniformly bounded imaginary parts. In particular a sequence
of such critical points cannot escape at imaginary infinity.

Here is a proof retaining the affine forcing of the chosen mark.
For 0<Re z<1 and Im z tending to either infinity,

    L(z)=-i pi sigma z+i pi sigma/2+o(1),
    sigma=sign(Im z),                            (8)

uniformly on fixed real substrips. Suppose first that Im x,
Im y and Im(x-y) all diverge in modulus along a subsequence.
With signs sigma_x,sigma_y,sigma_d, equation (4) becomes

    grad S_t=-i pi M_sigma(t)(x,y)^t
                               +i pi f_sigma(t)+o(1),
    M_sigma(t)=C_sigma+t[[2,1],[1,2]],
    C_sigma=[[3sigma_x-sigma_d,sigma_d],
             [sigma_d,-sigma_y-sigma_d]],
    f_sigma(t)=((3sigma_x-sigma_d)/2,
                         (sigma_d-sigma_y)/2)^t+t(3,2)^t. (9)

The real parts of x,y stay bounded. Any such critical sequence
must therefore have a limiting t at which M is singular, and
every null vector v of that limiting matrix must satisfy
v^t f=0. This follows by taking the real part of (9)/(i pi)
and then projecting onto v; it does not infer critical escape
merely from a degenerate Hessian at infinity.

The six consistent sign cones give the following determinants:

    (+++): (t+1)(3t-5),
    (++-): 3t^2+10t-1,
    (-+-): (t-1)(3t+1),
    (+-+): (t+1)(3t-1),
    (--+): 3t^2-10t-1,
    (---): (t-1)(3t+5).

In the second cone the only root in [0,1] is
alpha=(2sqrt(7)-5)/3; a null vector is (2alpha,1-alpha),
and its forcing projection is (1-19alpha)/3, which is nonzero.
In the fourth cone, t=1/3 and v=(1,-2), with v^t f=-4/3.
The third and sixth cones have t=1 and v=(1,0), with v^t f=2.
The other cones have no root in [0,1]. All full-cone escapes
are therefore impossible.

It remains to allow one of the three imaginary combinations to
stay bounded. Passing to subsequences reduces to six cases.
If Im x stays bounded while Im y tends to +infinity, the second
component of (4), divided by i pi, is

    (1-t)x-2t y+(2t-1)+o(1).

Its imaginary part forces t->0, and its real part then forces
Re x->1, excluded by delta. For Im y->-infinity the corresponding
expression is -(1+t)x-2t y+(1+2t), with the same contradiction.

If Im y stays bounded and Im x->+infinity, the first component
is -(1+t)(2x+y)+(1+3t)+o(1), whose imaginary part cannot vanish.
For Im x->-infinity it is

    (1-t)(2x+y)+(3t-1)+o(1).

The imaginary part forces t->1, and the real part then tends
to 2, again impossible.

Finally suppose Im(x-y) stays bounded and Im x,Im y diverge
together. For positive infinity, the SUM of (4), divided by
i pi, is

    -(3+3t)x+(1-3t)y+(1+5t)+o(1),

whose imaginary part cannot vanish. For negative infinity it is

    (3-3t)x+(-1-3t)y+(-1+5t)+o(1).

This forces t->1/3, where its real part is
2Re(x-y)+2/3>0. These cases exhaust all escapes and prove
the lemma. It does not exclude finite degeneracies, additional
bounded critical points or crossings of the REAL subtriangle's
boundary; those are separate questions.

## 4. Exact endpoint annihilation in the natural coefficient contour

The inner polynomial in (1) has the exact finite identity

    H_n(t)=sum_(j=0)^n {n choose j}_Q t^j
          =F_n [z^n]u_N(tz)u_N(z), n<N.          (10)

For any delta>0 and n<=(1-delta)N, the coefficient functional
in (10) annihilates EVERY fixed number of terms of the exterior
top-degree expansion of u_N(tz). Each such term has degree
N-1-k in z, with k fixed, whereas the other atom has only
nonnegative powers. Thus its contribution is exactly zero once
N-1-k>n. This is a source identity, not an estimate.

Consequently that coefficient can be governed by a scalar atom
sector which is beyond every fixed order of the dominant exterior
expansion. Uniform pointwise dominance before contraction cannot
by itself identify this selected coefficient.

For the geometric algebraic critical points of the candidate,
the proper-ratio equations give

    Y^3+Y^2-1=0, X=Y/(1+Y-Y^2),
    (1-X)^3=X^3Y(1-Y),
    X Y^2+(1-X)Y-X=0.                            (11)

At the corresponding formal saddle of (10), its two u arguments
are 1-Y and 1-X/Y. Let rho be the real root of Y^3+Y^2-1,
so 0<rho<1. For either nonreal root,

    |1-Y|^2=2+rho+rho^(-1)>4.                    (12)

The full scalar u_N at that argument is therefore in the PROVED
top-degree region of the [actual atom theorem](full_euler_atom_dilog_and_endpoint_regions.md).
Equation (10) nevertheless kills its fixed-order top-degree
expansion as just explained. A correct coefficient-contour
comparison must retain that cancellation or use the marked
factorial interpolation. Substitution of two bare u dilogarithm
branches at (11) would not justify the selected source.

## 5. Numerical guide, not a cycle proof

Implicit-ODE continuation of grad S_t=0 from the real positive
maximum follows a bounded nondegenerate branch to

    x=0.86919340003238+0.09218763788516 i,
    y=0.61202243557853-0.02237715112442 i.

Then exp(2pi i x),exp(2pi i y) solve (11). In the Riley field
t^3+t^2+2t+1=0 they are

    Y=t^2+t+1, X=(t^2+2t+4)/5.

The sampled continuation has Re(x-y)>=0.244, 1-Re x>=0.1308
and |det Hess S_t|>=27.09. These are numerical observations,
not interval-certified bounds or a theorem excluding other
critical points. The simpler lattice gauge B=pi(x-x^2-xy-y^2)
does NOT follow this bounded branch: numerical continuation
instead approaches a degenerate infinite branch. Hence a phase
mark cannot be changed during a homotopy without checking it.

The remaining theorem must show that the fixed finite source
cycle in (3), equivalently its exact cotangent-residue contour,
transports to the tracked geometric thimble with nonzero integer
coefficient. Properness on fixed subtriangles, local saddle
uniqueness and the real boundary envelope do not alone prove it.
Possible finite degeneracies, competing bounded critical points,
the outer real boundaries, and the exact Poisson/cotangent source
still have to be controlled. No selected 5_2 volume theorem is
claimed in this note.

[Exact algebra and numerical continuation audit](../experiments/audit_selected_angular_source_homotopy.py)
and [saved results](../experiments/selected_angular_source_homotopy_results.json).
