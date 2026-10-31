# The proposed pretzel radial homotopy has no strict boundary-action gap

**Subsequent resolution for this source.** The obstruction proved below
remains valid, but the [full coherent period theorem](actual_pretzel_coherent_circle_and_period_asymptotic.md)
now combines the equal-height contributions by an exact finite inner
transformation and controls all remaining indices with both recurrence
branches. It proves complete-base survival without the false strict
boundary gap. The unfilled augmented link, not a fixed knot filling,
is the scope of that result.

29 October 2026. For the EXACT phase of the double sum in
[the complete original pretzel polynomial](actual_pretzel_complete_base_casimir_polynomial.md),
the original-radius diagonal boundary attains the SAME action as the
candidate shifted interior saddle, for EVERY fixed real w<-1.
Consequently no uniform strict boundary gap holds on the proposed
closed homotopy rho_X in [rho_*,0]. This does not refute a deformation
which coherently fills or combines that endpoint current. It identifies
the endpoint contribution such a deformation must retain.

## 1. Phase, branches, and the candidate saddle

Write w=-W, W>1, X=exp(rho+i theta), Y=exp(i phi), with
0<phi<theta<pi and rho<=0. Use the principal dilogarithm, taking the
boundary value of Li2(Y/X) from Im(Y/X)<0. Thus its continuation to
theta=phi at rho<0 is its LOWER-side value on (1,infinity).
The phase is

    S=-6Li2(1)-Li2(X^2)+4Li2(X)+Li2(1/X)-Li2(Y/X)
                      +Li2(w)+Li2(1/w)-Li2(wY)-Li2(Y/w)+3Li2(Y).

Put F=Im S. The lower-side convention is essential at the diagonal;
resetting its logarithm changes F by a radial mark.

Set A=W+W^(-1) and

    phi_*=2 arctan(sqrt(A+2)/2),
    Y_*=exp(i phi_*), X_*=(Y_*-1)/(Y_*+3),
    rho_*=log|X_*|, theta_*=arg X_*.

Then rho_*<0 and 0<phi_*<theta_*<pi. These are the specified
exponentiated stationary equations. On this chart D_X S=0 and
D_Y S=2pi i at the point. The retained mark -2pi i Log Y makes
the latter an actual zero derivative; because |Y|=1 this mark is
real on the angular triangle and does not change F or the result below.

## 2. An exact identity equates the diagonal and interior actions

For ANY 0<phi<pi, set Y=exp(i phi), X(Y)=(Y-1)/(Y+3), and define

    G(X;Y)=-Li2(X^2)+4Li2(X)+Li2(1/X)-Li2(Y/X).

The following equality is exact:

    Im G(X(Y);Y)=3 Cl2(phi)-Cl2(2phi)=Im G(Y;Y).       (1)

Here Cl2(a)=Im Li2(exp(i a)); it uses the same continuous principal
boundary values, not a changed dilogarithm sheet.

Proof. X(Y) is in the upper unit disk. Indeed Im X=4sin(phi)/|Y+3|^2
and |X|^2=(2-2cos(phi))/(10+6cos(phi))<1. Moreover

    1-Y/X=(1+Y)^2/(1-Y)

has argument (pi+phi)/2, so Y/X lies in the lower half-plane and
arg X>phi. All the displayed logarithms therefore vary continuously.
Direct differentiation gives

    D_X G=2Log(1-X^2)-4Log(1-X)
                              +Log(1-1/X)-Log(1-Y/X).

Its exponential is one at X=X(Y). Its limit as phi decreases to zero
is zero, fixing the integer logarithmic ambiguity, hence D_X G=0
on the entire interval. Thus

    d_phi Im G(X(Y);Y)=log|1-Y/X|
                     =2log|1+Y|-log|1-Y|.

The same derivative is obtained from 3Cl2(phi)-Cl2(2phi), since
d_a Cl2(a)=-log|1-exp(i a)|. Both sides of (1) tend to zero as
phi increases to pi. This proves (1), including its constant.

The other terms of S depend only on Y,w, so (1) proves

    F(rho_*,theta_*,phi_*;w)=F(0,phi_*,phi_*;w).       (2)

In particular the diagonal boundary of the original radius is not
strictly below the candidate interior action.

## 3. It is precisely the maximum on that boundary edge

On rho=0, theta=phi, inversion of the two w-dependent dilogarithms
gives the explicit real function

    B_W(phi)=6Cl2(phi)-Cl2(2phi)
                -2Im Li2(-exp(i phi)/W)+phi log W.     (3)

There is no omitted imaginary constant: Li2(-W),Li2(-1/W) are real,
and Log(-wY)=log W+i phi in the inversion formula. With
t=tan(phi/2)>0, differentiation and elementary sine algebra give

    B_W'(phi)=log([(A+2)+(A-2)t^2]/(4t^4)).           (4)

The numerator minus 4t^4 equals

    -(1+t^2)(4t^2-A-2).

Hence B_W has a UNIQUE maximum, at t^2=(A+2)/4, which is exactly
phi_*. Combining (2)--(4),

    max_(0<=phi<=pi) F(0,phi,phi;w)=F_* .             (5)

Equations (2) and (5) disprove the requested strict uniform boundary
gap for every w<-1. They do not assert that another boundary edge or
an intermediate radius exceeds F_*, nor that a fixed strictly shifted
triangle lacks its own boundary gap. No such extra statement is needed.

For reference, the opposite far corner has the exact lower-side value
F(rho,pi,pi;w)=pi(log W-rho). It rises under the radial shift and
therefore also cannot be dismissed by an unmarked endpoint rule.

## 4. The equal-action boundary is present in the original finite source

The exact double summand in formula (11a) of the original polynomial
is, with F_j=(Q;Q)_j,

    A_(v,r)=F_(2v)/F_v^4 * (Q^(-v);Q)_r Q^r/F_r^3
                                      *(qw;Q)_r(q/w;Q)_r,
    0<=r<=v<=M=floor((N-1)/2).

At the DIAGONAL physical endpoint r=v it is exactly

    A_(v,v)=(-1)^v Q^(-v(v-1)/2)
          *F_(2v)(qw;Q)_v(q/w;Q)_v/F_v^6.           (6)

Every factor in (6) is nonzero for w<-1 and 0<=v<=M. In particular
this is not an outside-support zero of (Q^(-v);Q)_r: that zero first
occurs at r=v+1. The outer polynomial/source factors N^2/kappa
remain as in the original formula. No nonzero coefficient for the
ENTIRE period is inferred by taking a single endpoint term.

An exact factorial completion also makes the retained endpoint plain.
Put h=2pi i/N, delta=v-r, alpha_+=d/2+Log(W)/h and
alpha_-=d/2-Log(W)/h. With the exact Fhat_N of
[the original factorial interpolation](exact_factorial_interpolation_and_complex_contours.md),
the following meromorphic function takes the literal values A_(v,r):

    Ahat(v,r)=exp(pi i r+h[-vr+r(r+1)/2])
        *Fhat(2v)/[Fhat(v)^3 Fhat(v-r)Fhat(r)^3]
        *Fhat(alpha_++r)/Fhat(alpha_+)
        *Fhat(alpha_-+r)/Fhat(alpha_-).               (7)

Both alpha choices satisfy Q^(alpha_++1)=qw and
Q^(alpha_-+1)=q/w. Their sum uses the actual negative-w logarithmic
marks; the product has no unspecified periodic factor. Formula (7)
follows from the exact factorial shift and
(Q^(-v);Q)_r=(-1)^r Q^(-vr+r(r-1)/2) F_v/F_(v-r)
at the physical integers. The physical change (v,r)->(delta,r) is
unimodular, so its local lattice residues have no new Jacobian. This
constructs the SAME finite residue functional in the new coordinates;
it is not a pointwise identity between two products of cotangents or
permission to omit their chart-change currents.

Near delta=0 and a compact tangential neighborhood of the equal-action
point, Fhat(delta) is holomorphic, nonzero and Fhat(0)=1; all other
scaled factorial arguments lie in regular compact substrips. Thus the
cot pole at delta=0 has its original NONZERO residue (6). Conversely
1/Fhat(delta) has simple zeros at delta=-1,-2,...,-m for any fixed
small normal collar m<N, canceling those newly enclosed cot poles
provided the remaining factors stay regular. This permits the familiar
zero-side local filling; it does not delete delta=0 or supply a strict
action gap there. Finite-height connecting contours and all their
currents must be retained exactly as in the proved simple seam filling.

An exact residue cycle is the sum of small product circles about
(delta,r) in Z_>=0^2 with delta+r<=M, with density Ahat times the two
unit-residue cotangent factors. It is the original finite sum. Moving
it to the shifted saddle requires an actual relative-cycle operation
through this equal-action endpoint packet. Its coefficient, possible
coherent cancellation, and any resulting uniform asymptotic remain
unproved by radial concavity alone.

The subsequent [coherent finite inner elimination](actual_pretzel_coherent_inner_gauss_elimination.md)
does handle this packet without postulating that radial homotopy: an
exact balanced finite transformation keeps the half shift and proves
its nonzero amplitude in the geometric range. The
[whole circle/period assembly](actual_pretzel_coherent_circle_and_period_asymptotic.md)
uses that coherent sum and an all-index two-branch upper envelope,
rather than the false strict boundary-gap premise disproved here.

[Audit](../experiments/audit_actual_pretzel_radial_boundary_gap.py)
supplements the proof with high-precision branch/derivative equalities
and literal finite-factorial diagonal identities. It is not used to
infer an asymptotic or a selected thimble coefficient.
