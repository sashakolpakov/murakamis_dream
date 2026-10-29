# A proved outer maximum for the cubic reduced phase

28 October 2026. For the exact double-sum phase supplied by the
[finite transform](five_two_cyclotomic_transform_proof.md), the
selected inner critical branch has a rigorously concave reduced
outer action on a full horizontal band. The explicit bent contour
through its cubic stationary point also has a unique global
maximum there. The sloped part is controlled analytically, without
a mesh-based positivity assumption.

This is a theorem about the explicit reduced phase and its contour.
The original outer sum still has to be carried to that contour,
including its aliases and the inner endpoint pieces. Equality of
the cubic critical value with the marked hyperbolic regulator is
also separate: numerical agreement or equality of trace fields
does not prove that action identity.

## 1. The phase and a specified inner critical branch

Use the branch J'(z)=Log(2sin(pi z)) continued from 0<z<1,
and set

    S(x,y)=3J(x)-J(y)-J(x-y)
               +i*pi*(3x+2y-x^2-xy-y^2).          (1)

Its added lattice characters are retained in this definition.
Let

    1/2<Re x<1, 0<=Im x<=Log(2)/(2pi),
    X=exp(2pi*i*x), T=1/X-1.

The number T lies in the upper half-plane and
1<=|T+1|<=2. The quadratic

    v-1/v=T                                      (2)

has exactly one root in the first quadrant. Indeed its two
roots have product -1 and share the sign of their imaginary
parts. A root could be purely imaginary only if
T belonged to i[2,infinity). The present circles, centered at
-1 with radii at most 2, meet the imaginary axis below sqrt(3),
so they avoid that ray. The chosen root is analytic here.

Put

    Y=-v, y_s(x)=1+Log(Y)/(2pi*i)
                  =1/2+Log(v)/(2pi*i),           (3)

where 0<Arg v<pi/2 and -pi<Arg Y<-pi/2.
Then 1/2<Re y_s<Re x<1 and 0<Re(x-y_s)<1/2.
For the latter inequality, (T+1)v=v^2+v-1 has positive
imaginary part, so Arg(T+1)+Arg v lies strictly between
zero and pi. All three J arguments in (1) therefore stay
on their stated strips.

The quadratic equation gives S_y(x,y_s)=0. Exponentiating
that derivative gives

    1-X/Y=X(1-Y).

The logarithmic derivative itself is zero, rather than an
unretained multiple of 2pi*i: it is constant modulo that
multiple on this connected branch and tends to zero at
x->1 from the real interval. Define

    W(x)=S(x,y_s(x)).                             (4)

## 2. Exact reduced Hessian

Differentiating (1)--(3), or taking its Schur complement,
gives exactly

    W''(x)=2pi*i R(v),
    R(v)=(v^2+v+4)(v^2+v-1)/(1-v^4).             (5)

Equivalently, with s=v+1/v=sqrt(T^2+4) on its marked branch,

    R=(T+1)/(2T)*[(3T-2)/s-5].                   (6)

These formulas are independent of an added constant logarithmic
flattening. Such a flattening still matters for W and W'.

## 3. Horizontal strict concavity on the whole band

Write v=a+ib, a,b>0, r=a^2+b^2, and d=|T+1|^2.
The present band has 1<=d<=4. Equation (2) gives the exact
constraint

    r^2+(3-d)r+1+2a(r-1)-4a^2=0.                (7)

Direct multiplication gives Im R=b P_0/|1-v^4|^2. Reducing
its real polynomial numerator by (7) gives

    P=a[2r^2+(6d+4)r-8]
                     +2r^3+2r^2+(13-5d)r+8.    (8)

This numerator is STRICTLY positive on the stated domain.
Here is an elementary certificate. Its constant part is at least

    C(r)=2r^3+2r^2-7r+8>0.

For 0<=r<=1 this is at least 8-7r>=1. For r>=1 it is
increasing and C(1)=5. If the coefficient of a in (8) is
nonnegative, this proves the claim. Otherwise r<1. Since
a<=sqrt(r), replacing a by w=sqrt(r) gives a lower bound.
The result is affine in d, with coefficient w^2(6w-5).

For w<=5/6 its minimum over 1<=d<=4 occurs at d=4:

    L_4=2w^6+2w^5+2w^4+7w^2(4w-1)+8(1-w)>0.

For w>=1/4 every displayed term is nonnegative. For w<1/4,
the last two terms alone exceed 6-7/16>0. For w>=5/6 the
minimum occurs at d=1:

    L_1=2w^6+2w^5+2w^4+10w^3+8(w^2-w+1)>0.

Thus Im R>0. Consequently

    partial_u^2 Re W(u+i eta)<0                  (9)

for EVERY horizontal line in the band. This proves global
horizontal concavity directly from the explicit phase, rather
than assuming that a different positive triangulation controls
these original reduced coordinates.

## 4. The cubic stationary point and its exact flattening

Let rho be the unique real root of rho^3+rho^2-1=0. Elementary
evaluation gives 3/4<rho<4/5. Let v_g be the upper-half-plane
root of

    v^3-v^2+1=0,
    Re v_g=(1+rho)/2, |v_g|^2=1/rho.

Define

    X_g=1/(1+v_g^2),
    x_g=1+Log(X_g)/(2pi*i)=u_g+i eta_g,
    y_g=1/2+Log(v_g)/(2pi*i).

The critical identities v_g^2(1-v_g)=1 and
v_g^5=-(1+v_g) give T_g=v_g^2. On the branch of Section 1,

    W'(x)=3Log T-Log v-Log(1+v)-i*pi.

At the cubic point this is 5Log v_g-Log(1+v_g)-i*pi=0.
The sign of pi is fixed: the argument difference lies between
-pi/2 and 5pi/2 and is an odd multiple of pi, hence equals pi.
Thus (x_g,y_g) is a genuine stationary point of (1) in its
stated flattening, not merely a solution of exponentiated
equations.

Useful exact values are

    |T_g|=1/rho<4/3,
    Re(1/T_g)=(1-rho)/2>1/10,
    D:=|1+T_g|^2=3+rho-rho^2<13/4<4.

It follows that eta_g=Log(D)/(4pi)<Log(2)/(2pi).
Numerically

    x_g=.869193400032383...+.092187637885157...i,
    y_g=.612022435578528...-.022377151124418...i,
    Re W(x_g)=.450109610025218....

The last decimal is an evaluation of (1). It is not used as
a proof of regulator calibration or source intersection.

## 5. Analytic dominance on the sloped outer segment

Set theta_g=2pi(1-u_g)=Arg(1+T_g),
c=eta_g/(1-u_g)=Log|1+T_g|/theta_g. Then 0<c<1.
For completeness theta_g>pi/4: writing 1+T_g=A+iB gives

    A=(3-rho^2)/2,
    B^2-A^2=(-2+rho+3rho^2)/2>0.

Also Log|1+T_g|<(1/2)Log(13/4)<pi/4.

On the sloped segment x=u+i c(1-u), u_g<=u<1, write

    theta=2pi(1-u), T=exp[(c+i)theta]-1.

The function |T| increases with theta on [0,theta_g], so
|T|<=4/3. A further useful lower bound is

    Re(1/T)>=(1-rho)/2>1/10.                    (10)

To prove it, let

    h(theta)=sinh(c theta)
                -(2-rho)[cosh(c theta)-cos theta].

It vanishes at both endpoints, by the exact geometric value
of Re(1/T_g). Its second derivative is strictly negative:
2-rho>1 and 0<=theta<=theta_g<pi/2. Thus h>=0,
which is (10) after using the elementary real coth formula.

Equation (6) also gives an absolutely convergent expansion

    R=-3/T-9/4+E(T),
    E=(3/4)T+(T+1)(3T-2)/(4T)
                          *[(1+T^2/4)^(-1/2)-1].

For r_T=|T|<2 the binomial derivative bound yields

    |E|<=3r_T/4+(1+r_T)(2+3r_T)r_T
                         /[32(1-r_T^2/4)^(3/2)].

At r_T<=4/3 the right side is at most
1+63/(20sqrt(5)). Combining with (10),

    Re R<=(63/sqrt(5)-31)/20<0.                 (11)

The horizontal-band theorem already gives Im R>0 here.
Therefore the ENTIRE sloped reduced action satisfies

    d^2/du^2 Re W(u+i c(1-u))
       =2pi[2c Re R-(1-c^2)Im R]<0.             (12)

Its first derivative vanishes at u_g, so it strictly decreases
to the right. This proves the sloped dominance analytically.

## 6. An explicit sufficient outer saddle contour

Fix any alpha in (1/2,u_g). The piecewise contour

    x(u)=u+i min(eta_g,c(1-u)), alpha<=u<=1      (13)

has a UNIQUE global maximum of Re W at x_g. The left piece
is covered by (9), the right piece by (12), and W'(x_g)=0.
There is a strict action gap away from every neighborhood of
x_g. The finite endpoint value at u=1 is submaximal by strict
decrease, without requiring a separate numerical bound.

For an analytic nonzero amplitude with a controlled uniform
asymptotic expansion on this contour, ordinary one-variable
saddle evaluation therefore has a nonzero Gaussian leading
coefficient at x_g. The kink at x_g is harmless: its two
tangent directions, 1 and 1-i c, lie in the same negative
Gaussian cone. In fact W''(x_g) has negative real AND negative
imaginary parts, and c<1, so rotating between those directions
keeps the quadratic real part strictly negative. The two local
half-rays give the full marked Gaussian, rather than an
undetermined zero intersection factor ON THIS specified path.

This is not a proof that the original outer residue cycle equals
(13). That step must control the actual outer aliases and the
inner connector/end-point integrals along the deformation.
For example, a constant-height translation of the WHOLE triangle
would retain an inner endpoint with action larger than the cubic
value; reduced saddle concavity alone would miss it. The exact
[inner quadrature theorem](source_preserving_inner_quadrature.md)
is an input for that separate source-preserving comparison,
not permission to discard its remaining complex endpoint pieces.

[Algebra and contour audit](../experiments/audit_five_two_reduced_outer_concavity.py)
and [saved diagnostics](../experiments/five_two_reduced_outer_concavity_results.json).
