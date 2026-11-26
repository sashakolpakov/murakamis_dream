# Conditional action transport through the negative real output axis

Research proof, 8 November 2026. The original type-four conditional
critical point and its incoming action inequalities extend to an
output with real logarithmic coordinate \(1/2\). On the incoming
corner used by the next-transfer argument, the critical action
retains the original supporting-plane bound throughout the enlarged
output interval.

This is a branch and action theorem, together with a bound for the
complete cap times that action. A finite-source theorem for the
conditional polynomial still has to control its physical rows and
all contour errors. No numerical evaluation or change to a frozen
source is used.

## 1. The closed part of the output domain

Retain the phase, primitive and incoming domain from
[the algebraic transport theorem](research_mixed_four_conditional_algebraic_transport_domain.md):
\[
\begin{split}
 \mathcal X=\{X:\ &\Re X<0,\quad\Im X\ge0,\quad |X|\le1,\\
                 &|X|^2(3-2\Re X)\ge1\},\\
 Q(t;a,y)&=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat,\\
 X&=e^{-2\pi ia},\qquad Y=e^{-2\pi iy},\qquad v=e^{2\pi it}.
\end{split}
 \tag{1}
\]
Enlarge its outgoing domain only by the indicated boundary interval:
\[
 \mathcal Y_{\mathrm c}
 =\{Y:\Im Y<0,\ \Re Y<1\}\ \cup\ [-1,0).
 \tag{2}
\]
At a negative real output we take \(\Arg Y=-\pi\), so
\[
 y=\frac12+\frac{i}{2\pi}\log|Y|.
 \tag{3}
\]
Local logarithms at these boundary points continue from the lower
half-plane; they are not reset to argument \(+\pi\).

The exact critical polynomial is
\[
 P_{X,Y}(v)=(1-X)v^3+(2X-Y)v^2+X(Y-3)v+X,
 \tag{4}
\]
equivalently
\[
 v(v-X)(v-Y)=X(v-1)^3.
 \tag{5}
\]

**Theorem 1.** For \(X\in\mathcal X\) and
\(Y\in\mathcal Y_{\mathrm c}\), there is exactly one upper-half-plane
root of (4), counted with multiplicity. It is simple, and
\[
 0<\arg v<\arg X,\qquad
 t=\frac{\Log v}{2\pi i},\qquad
 0<\Re t<1-\Re a,\qquad Q_t(t;a,y)=0.
 \tag{6}
\]
It has a holomorphic continuation to a neighborhood of every point
of this parameter set. For
\[
 \Theta(a,y)=Q(t(a,y);a,y),\qquad
 \omega=\frac{v-X}{1-X},
 \tag{7}
\]
the original logarithmic derivative satisfies
\[
 \Theta_a=\Log\omega,\qquad
       \Im\omega>0,\quad 0<|\omega|<1,\quad 0<\Arg\omega<\pi .
 \tag{8}
\]
These strict properties, and uniform margins on compact subsets,
include the new negative real outputs.

### Root count at the added boundary

The open-domain assertions are already proved in the cited theorem.
Let \(Y=-R\), \(0<R\le1\).
If \(\Im X>0\), a real root would satisfy the original elimination
identity
\[
 Y=v-\frac{X(v-1)^3}{v(v-X)},\qquad
 \Im Y=-\frac{(v-1)^3\Im X}{|v-X|^2}.
 \tag{9}
\]
The values \(v=0,1,X\) are excluded by (5). Thus (9) rules out
every real root also at \(\Im Y=0\).
The upper root from \(Y-i\epsilon\) consequently stays in the
upper half-plane as \(\epsilon\downarrow0\). The other roots
cannot enter it without reaching the real axis. A multiple upper
root would give more than one nearby upper root counted with
multiplicity, contradicting the open-domain count.

If \(X=-\rho\) is real, its domain inequality is
\(\rho^2(3+2\rho)\ge1\), and hence \(1/2\le\rho\le1\).
The polynomial becomes
\[
 (1+\rho)v^3+(R-2\rho)v^2+\rho(R+3)v-\rho.
 \tag{10}
\]
The discriminant of its derivative, divided by four, is
\[
 (R-2\rho)^2-3\rho(1+\rho)(R+3)
 =R^2-(7\rho+3\rho^2)R-5\rho^2-9\rho<0 .
 \tag{11}
\]
Indeed \(R\le1<7\rho+3\rho^2\), and all remaining terms
have strictly negative sign. The derivative is therefore
positive on the entire real axis. The cubic has one simple
real root, lying in \((0,1)\), because its endpoint values
are \(-\rho\) and \((1+\rho)(1+R)\).
Its other two roots form a nonreal conjugate pair, each simple.
This proves exactly one upper root at every added boundary point.

No root escapes to infinity in these limiting arguments:
the coefficients remain bounded on each compact parameter set
and \(1-X\) stays away from zero. Nor can a root approach zero,
because \(X\ne0\).

The incoming-ray exclusion in equations (12) of the open theorem
also remains strict. For \(v=sX\), \(s>1\), it forces
\(\Im Y>0\) when \(\Im X>0\); for \(0<s<1\), it forces
\(\Re Y>1\). Both conclusions contradict the present boundary.
For real negative \(X\), its ray is outside the upper half-plane.
This proves the strict argument inequality in (6).
In particular the real parts of \(t,a+t,y+t\) remain in their
original open strips, including when \(\Re y=1/2\).
The original zero logarithmic lift therefore continues from the
open domain. Simplicity gives the local holomorphic continuation.

### The multiplier remains strictly inside its original quadrant

At negative real \(X\), \(\Im\omega>0\) follows at once from
\(\Im v>0\). For \(\Im X>0\), repeat the real-multiplier
exclusion of the open theorem, retaining the equality case.
If \(\omega\) were real, its values zero and one would be
excluded by (5). Since \(v=\omega+(1-\omega)X\), its being
in the upper half-plane forces \(\omega<1\).
A negative \(\omega\) would contradict \(\arg v<\arg X\).
Thus \(0<\omega<1\).

Put \(A=\Re v\), \(r=|v|^2\), \(d=1-A\).
As in the original proof, the restrictions on \(X\) give
\[
 A<\omega,\qquad r\le1-2\omega d,
 \qquad
 Y=2-\frac1v+\frac{(v-1)^2}{\omega}.
 \tag{12}
\]
The imaginary part of the last identity, at \(\Im Y=0\),
is now the equality
\[
                 \omega=2rd .
 \tag{13}
\]
Consequently
\(\omega\le2d/(1+4d^2)\le1/2\), and \(A<1/2\).
But the real part gives
\[
 \omega r(\Re Y-1)
 =\omega(r-A)+r(2A^2-2A+1-r)=:M.
 \tag{14}
\]
This is strictly positive. If \(A\le0\), its first term is
positive and its second is nonnegative. If \(A>0\), then
\(r<2A^2-2A+1\) by (12) and \(\omega>A\); this proves
positivity when \(r\ge A\). If \(r<A\), substitute (13)
to get exactly
\[
                  M=r(1-2A)(r+1-2A)>0 .
 \tag{15}
\]
Each case contradicts \(\Re Y<1\).

The open theorem's unit-modulus exclusion is unchanged:
at \(|\omega|=1\) with \(\Im\omega>0\), its exact equations
(20)--(22) force \(\Im Y>0\), still impossible at this boundary.
Continuation from the open domain therefore gives both strict
inequalities in (8). The logarithmic identity follows from its
original zero lift, with no new additive multiple of \(2\pi i\).
This finishes the proof of Theorem 1.

## 2. The critical strip for the enlarged incoming corner

For the actual contour application it is enough to take
\[
 \frac12\le x\le\frac7{10},\quad 0\le\eta\le\frac9{125},
 \quad a=x-i\eta,\qquad
 \frac{11}{50}\le q\le\frac12,\quad
 0\le\xi\le\frac{27}{250},\quad y=q-i\xi.
 \tag{16}
\]
These parameters lie in (1)--(2), because
\(|X|>5/8\), \(\Re X<0\) and \(|Y|\le1\).
The strict radius bound follows from the same positive-series
estimate \(e^{23/50}<8/5\) used in the original corner sources.

The root bounds of
[the middle-source reduction, Section 5](research_mixed_conditional_lower_output_middle_reduction.md)
extend to this closed output interval:
\[
 \frac15<|v|<2,\qquad
 \frac2{25}<\Re t<1-x,\qquad
                 |\Im t|<\frac{\log5}{2\pi}.
 \tag{17}
\]
Here is why each use of its old angular range is still valid.
The cubic and reciprocal Cauchy bounds use only
\(|X|>5/8\), \(|Y|\le1\), so \(1/5<|v|<5\) is unchanged.
The exclusion of \(|v|\ge2\) uses the three small-radius
logarithms and the incoming chirp: it gives
\(\Im Q_t\ge2\pi x-5\pi/6>0\).

For \(u=\Re t\le2/25\), put \(U=1/|v|>1/2\).
If \(U\ge8/5\), the own argument is greater than
\(\pi-2\pi u-7\pi/30\). The incoming argument is nonpositive.
The outgoing argument still has the upper bound
\(14\pi/25-2\pi u\): only the lower bound \(q\ge11/50\)
is used when that argument is positive. The original calculation
then gives \(\Im Q_t<-\pi/50\), a contradiction.
If \(1/2<U<8/5\), the incoming summed real coordinate lies
in \([.5,.78]\) and the outgoing one in \([.22,.58]\).
Both cosines are less than \(1/5\). The original squared-force
bound remains
\[
 |e^{Q_t}|^2>
                 \frac{24/25}{(5/6)^3}>1,
 \tag{18}
\]
again impossible. This proves the additional assertions in (17).

The prewall curvature proof also extends. For
\[
 \frac2{25}\le\Re s<1-x,\qquad
                 |\Im s|\le\frac{\log5}{2\pi},
\]
the incoming shifted real cotangent is negative.
If \(q+\Re s\ge1/2\), the outgoing one is nonpositive
because \(q+\Re s<1\), and the own cotangent is positive.
If \(q+\Re s<1/2\), the original remaining case and its
bound \(\Re Q_{ss}<-43\pi/2440\) apply without change.
Thus \(\Re Q_{ss}<0\) on the strict prewall strip.
In particular on the right-hand output interval
\(q\in[.45,.5]\), only the first, simpler case occurs.

The strict separations in (17) are uniform on the compact set
(16). This gives the regular critical neighborhood needed by
the original Gaussian deformation, but does not estimate that
deformation's other terms.

## 3. The critical action at the incoming half face

Now use the actual ordinary-next reference
\((a_*,s_*,y_*,t_*,z_*)\) and original notation
\[
 A=\Re a_*,\quad\alpha=\Re y_*,
 \quad h_a=\Im a_*,\ h_s=\Im s_*,\ h_y=\Im y_*,
 \qquad a_L=\frac12+ih_a .
 \tag{19}
\]
In particular
\(.278\le A\le.391\), \(-.072<h_a<0\),
\(.24<\Re s_*,\alpha<.36\), and
\(-.102<h_s,h_y<-.001\).
Keep precisely the original allocated quantities from
[the incoming-corner theorem, equations (3)--(5)](research_mixed_next_unselected_incoming_corner_union.md):
\[
\begin{split}
 F(s;a,y)&=Q(s;a,y)-\frac12g(y),\\
 p_L&=Q_a(s_*;a_*,y_*),\\
 p&=\Re\{g'(s_*+y_*)-\tfrac32g'(y_*)\},\\
 A_*&=\Re\{T_0(a_*)+F(s_*;a_*,y_*)\},\\
 B_*&=\Re T_0(a_*)-\Re p_L(\tfrac12-A)
                         -\kappa(\tfrac12-A)^2,\qquad
 \kappa=1/2500000,\quad B_*>7/8.
\end{split}
 \tag{20}
\]

**Theorem 2.** Uniformly over these actual references and
\(y=q+ih_y\), \(q\in[.45,.5]\),
\[
 B_*+\Re\Theta(a_L,y)-\frac12\Re g(y)
       \le A_*+p(q-\alpha)-4\cdot10^{-9}.
 \tag{21}
\]

First extend the reference-height supporting inequality to
\[
 a_R,y_R\in[.22,.5],\qquad 1/8\le s_R\le1/2 .
 \tag{22}
\]
When both outside coordinates lie in \(P=[.22,.45]\), this
is the original three-variable curvature theorem. The
incoming extension \(a_R\ge.45,\ y_R\in P\) is proved
in Section 2 of the incoming-corner theorem. The outgoing
extension \(a_R\in P,\ y_R\ge.45\) is proved in Section 2
of [the central shoulder theorem](research_mixed_next_lower_right_shoulder_central_prefix.md).
When both exceed .45, the decomposition
\[
 F=V(s,a)+V(s,y)-g(s)-\tfrac12g(y)+2\pi ias,\qquad
 V(s,b)=g(s+b)-g(s)-g(b),
 \tag{23}
\]
has negative semidefinite real Hessian directly: the own
cotangents are nonnegative and both shifted cotangents
are nonpositive. All heights remain fixed at the original
negative values. At closed half faces take their regular
lower-half limits.

A straight segment from the reference stays in the union
of these four domains. Integration of its nonpositive
real Hessian, followed by adding \(B_*\), gives
\[
 B_*+\Re F(s;a_L,y)
 \le A_*+p(q-\alpha)-\kappa(\tfrac12-A)^2,
 \qquad s=t+ih_s,\quad 1/8\le t\le1/2.
 \tag{24}
\]
The retained cap loss satisfies
\[
 \kappa(\tfrac12-A)^2
 \ge\frac{11881}{2500000000000}>4\cdot10^{-9}.
 \tag{25}
\]
For \(2/25\le t\le1/8\), the exact chirp-folded force
from the old corner proof is greater than one: the two
shifted cosines are negative since
\(.5+t\in[.58,.625]\) and \(q+t\in[.53,.625]\),
whereas the own modulus squared is at most \(3/5\).
The phase increases to \(t=1/8\), so (24)--(25)
also bound that additional index interval.

To compare the moving critical point with this fixed-height
bound, set
\[
 m(\sigma)=\max_{2/25\le t\le1/2}
                      \Re Q(t+i\sigma;a_L,y).
 \tag{26}
\]
The curvature just proved in Section 2 makes each profile
vertically convex before the half face; its continuous
one-sided boundary value at \(t=1/2\) is convex as well.
At a numerator zero the derivative has an upward jump,
consistent with this convexity. Thus \(m\) is convex on
\(|\sigma|\le\log5/(2\pi)\).
At the critical height, (17) and strict horizontal
concavity give a unique interior maximum in (26).
Its height derivative is \(-\Im Q_s=0\); hence this
height minimizes \(m\).
The actual \(h_s\) belongs to the same interval.
Consequently
\[
                    \Re\Theta(a_L,y)\le m(h_s).
 \tag{27}
\]
Combining (24)--(27) proves (21). The argument uses
the original continuous primitive, including at \(q=1/2\).
It assumes no concavity of the eliminated action.

## 4. The complete cap times the transported action

Theorem 1 gives, on every compact subset under consideration,
\[
 \partial_x\Re\Theta=\log|\omega|<0,\qquad
 \partial_h\Re\Theta=-\Arg\omega<0,\qquad a=x+ih.
 \tag{28}
\]
It follows that \(\Re\Theta(a,y)\le\Re\Theta(a_L,y)\)
on both directed replacement segments
\[
 a_L\longrightarrow .7+ih_a,\qquad
 .7+ih_a\longrightarrow .7 .
 \tag{29}
\]
These segments stay in (16); this includes the output
endpoint \(q=1/2\).

The complete cap estimates in Sections 4--5 of the
incoming-corner theorem are independent of \(y\).
On the horizontal segment they have rate \(B_*\);
on the vertical segment their rate is at most
\(3907/4500<7/8<B_*\).
The original full Fourier weight, with its forcing retained,
satisfies
\[
 |d_N(e^{-2\pi iy})|^{1/2}
 \le C_\tau N^{B_\tau}
                  e^{N\{-\Re g(y)/2+\tau\}}.
 \tag{30}
\]
This holds on the closed lower strip \(q\le1/2\):
\(-\Re g(y)\ge0\), with equality allowed at \(q=1/2\);
the forcing alternative has rate zero. No nonzero
factorial approximation or division is used at that endpoint.

Thus, on (29), for every prescribed sufficiently small tolerance,
\[
\begin{split}
 &|U_{0,N}(w,e^{-2\pi ia})|\,|d_N(Y)|^{1/2}
                                      e^{N\Re\Theta(a,y)}\\
 &\qquad\le C_\tau N^{B_\tau}
 e^{N\{A_*+p(q-\alpha)-4\cdot10^{-9}+\tau\}} .
\end{split}
 \tag{31}
\]
This retains the complete coherent cap for all real ordinary
colors, both parities and the original Fourier polynomial.
On small complete-color neighborhoods the same assertion
uses the original complex cap bound.
It estimates the cap times the conditional action, not
the entire conditional polynomial.

The exact replacement of the incoming corner remains the
rectangle identity for the original finite Laurent source,
with measure \(N\,da\). To turn (31) into a bound for that
source, the conditional finite integral and its two kinds of
errors must be extended to this same output interval.
The following kernel also retains its separate estimate.
Neither an arbitrary short-filling theorem nor a whole
next-transfer asymptotic follows from the action comparison alone.
