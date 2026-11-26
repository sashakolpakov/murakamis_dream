# A static endpoint budget for the first selected height

Research deduction, 6 November 2026.

For the actual first-four/next-three factorial comparison, a bound at
one final height suffices in place of a pointwise optimizing-curvature
bound. This note gives its exact convex dual in the original source
variables and an explicit one-parameter trial. It does not prove the
remaining scalar inequality or a whole selected-source estimate.

## 1. The original reference and the required final gain

Use the joint phase \(\mathcal F(e,s;z,b)\) of
[the sharper common-branch budget](research_mixed_forced_optimizer_sharper_budget.md),
with the same original outgoing affine subtraction. The word has
length at least three, its first type is four, and its next type is
three. Write \(f(x,k)\) for that real phase, where
\(x=(e_R,s_R,z_R,b_R)\) and \(\Im z=k\). The other three
heights stay at their actual reference values. Set
\[
 H=\frac7{625},\qquad c=\Im z_*>-\frac7{100},\qquad
 x_*=(\Re e_*,\Re s_*,\Re z_*,\Re b_*),\qquad
 M=f(x_*,c),\quad G(k)=\max_x f(x,k).
 \tag{1}
\]
All starred quantities come from the same original coupled reference.
In particular the outgoing affine marginal is
\(p_* =\mathcal F_b(e_*,s_*;z_*,b_*)\); it is not a free
parameter or an independently chosen box value. The original
unexponentiated equations give
\(f_x(x_*,c)=0\), \(f_k(x_*,c)=0\), and \(G(c)=M\).

The actual reference has
\(.333<\Re e_*<.363\), \(.246<\Re z_*<.350\), and
\(.267<\Re s_*,\Re b_*<.433\), by the reference enclosures in
[the coupled-height note](research_mixed_first_four_attached_height_bound.md),
Section 1, and [the cap-height note](research_mixed_first_cap_height_tangent.md),
equation (1). Its summed real parts obey
\(1/2<\Re(e_*+z_*),\Re(s_*+z_*)<1\).
Also \(\Re(s_*+b_*)>1/2\): both actual ordinary type-three
outputs have real part greater than \(.267\) in the
[open local-factor coverage](research_mixed_open_local_factor_coverage.md).
Equivalently this is the reference-height case of the second-sum
theorem in [the positive-sum note](research_mixed_factorial_positive_sum.md),
Section 5.
The elementary method of the
[direct-curvature bound](research_mixed_positive_height_factorial_bounds.md),
Proposition 2, is stronger on the fixed vertical line
\(x=x_*\) than on the full moving-maximizer domain. Indeed, for
\(x=\Re z_*\),
\[
 \frac{f_{kk}(x_*,k)}\pi
 =\Re\{3\cot\pi z_k-\cot\pi(e_*+z_k)
                         -\cot\pi(s_*+z_k)\}
 \le F(x):=3\cot\pi x+\tan\pi(x-.137)+\tan\pi(x-.067)
 <\frac{41}{10}.
 \tag{2}
\]
Here \(z_k=\Re z_*+ik\). The first inequality uses only
\(\Re e_*<.363\), \(\Re s_*<.433\), and the displayed
summed-real-part ranges; imaginary displacement decreases the
magnitude of a negative real cotangent. The function \(F\) is
convex on \([.246,.350]\). At its two endpoints use
\[
 \begin{array}{lll}
 \cot(.246\pi)<103/100,&\tan(.109\pi)<9/25,&
                                      \tan(.179\pi)<16/25,\\
 \tan(.15\pi)<13/25,&\tan(.213\pi)<4/5,&
                                      \tan(.283\pi)<5/4.
 \end{array}
 \tag{2a}
\]
These give \(F(.246)<409/100\) and
\(F(.350)<361/100\). For explicit rational witnesses for
the five tangent bounds, put
\(s_5(t)=t-t^3/6+t^5/120\) and
\(c_6(t)=1-t^2/2+t^4/24-t^6/720\).
At \(t=a(22/7)\), direct substitution gives
\(s_5(t)<r c_6(t)\), with positive \(c_6(t)\), for
\((a,r)=(.109,9/25),(.179,16/25),(.15,13/25),
(.213,4/5),(.283,5/4)\). The alternating Taylor bounds
then give \(\tan(a\pi)<r\). For the cotangent bound use
\(\cot(.246\pi)=(1+\tan(.004\pi))/(1-\tan(.004\pi))\)
and \(\tan(.004\pi)<3/203\); the latter follows already
from \(\sin t\le t\), \(\cos t\ge1-t^2/2\), and
\(t=.004\pi<11/875\). More explicitly,
\((13/1000)(1-(11/875)^2/2)-11/875
=654677/1531250000>0\), and \(13/1000<3/203\).
Consequently
\[
 V_*:=f(x_*,H)-M
 <\frac{41\pi}{20}(H-c)^2.
 \tag{3}
\]

**Proposition 1.** It suffices to prove the single endpoint inequality
\[
                 L_*:=G(H)-f(x_*,H)\le\frac\pi{128}
 \tag{4}
\]
to obtain the common central Fourier gap \(1/500\).

Indeed \(H-c<203/2500\), and (3)--(4) give
\[
 G(H)-M<\frac{5332263\pi}{250000000}
       <\frac{535717\pi}{25000000}.
 \tag{5}
\]
The last difference is \(24907\pi/250000000\). The last
quantity is exactly the sufficient total-excess budget in the cited
sharper common-branch theorem. Thus its factorial and forced
comparisons both apply, including the proved forced ceiling
\(\Re z<2/5\). No assertion about \(G''\) is needed.

## 2. The endpoint gradient is explicit in the actual reference

Put
\[
 E_*=e^{-2\pi i e_*},\quad S_*=e^{-2\pi i s_*},\quad
 Z_*=e^{-2\pi i z_*},\qquad
 \lambda=e^{2\pi(H-c)},\quad \ell=\log\lambda,
 \tag{6}
\]
and define the real increments
\[
 \begin{split}
 A&=\log\left|\frac{1-\lambda E_*Z_*}{1-E_*Z_*}\right|,\\
 B&=\log\left|\frac{1-\lambda S_*Z_*}{1-S_*Z_*}\right|,\\
 C&=\log\left|\frac{1-\lambda Z_*}{1-Z_*}\right|.
 \end{split}
 \tag{7}
\]
All factors are nonzero on the original regular strips. Comparing
the original derivatives at \((x_*,H)\) and \((x_*,c)\)
gives the exact real gradient
\[
              p:=f_x(x_*,H)=(A,\ B-\ell,\ A+B-3C,\ 0).
 \tag{8}
\]
In particular \(-\ell\) retains the original
\(2\pi izs\) chirp. The last entry is zero because
\(\mathcal F_b\) is independent of \(z\), and the original
outgoing marginal has already been subtracted. The reference
\(b_*\) and its height still occur in the costs below; this
zero does not erase their correlation with the outgoing tangent.

## 3. The exact static convex dual

The proved positive-height and face exclusions put every final
factorial maximum in the convex set
\[
 \begin{gathered}
 .3\le e_R\le.4,\quad .2\le s_R\le.5,\quad
 .22\le z_R\le.31,\quad .22\le b_R\le.45,\\
                     s_R+z_R\ge.5,\qquad s_R+b_R\ge.5.
 \end{gathered}
 \tag{9}
\]
Only an original \(b\) endpoint can be active at the actual
maximum; all the other displayed boundary inequalities are strict
there. This follows from the
[lower](research_mixed_factorial_lower_face_exclusion.md) and
[upper](research_mixed_factorial_upper_face_exclusion.md) face
exclusions and [the positive-height theorem](research_mixed_factorial_positive_sum.md),
Section 6. Restricting the maximization to (9) thus leaves \(G(H)\)
unchanged.

At height \(H\), minus \(f\), modulo affine terms, is the sum
of the following four node potentials and three edge potentials:
\[
 \begin{array}{ll}
 P_e(t)=-\Re S(t+ih_e)+\Re g(t+ih_e),&
 P_s(t)=2\Re g(t+ih_s),\\
 P_z(t)=3\Re g(t+iH),&P_b(t)=\Re g(t+ih_b),\\[2pt]
 Q_e(t)=-\Re g(t+i(h_e+H)),&
 Q_s(t)=-\Re g(t+i(h_s+H)),\\
 Q_b(t)=-\Re g(t+i(h_s+h_b)).&
 \end{array}
 \tag{10}
\]
The three edge arguments are respectively \(e_R+z_R\),
\(s_R+z_R\), and \(s_R+b_R\). Both original quadratic
chirps are real affine functions of the real coordinates when the
heights are fixed, so omitting them in (10) loses no Bregman cost.
Their gradient contributions have already been retained in (8).

For a scalar potential \(W\), centered at \(t_*\), write
\[
       D_W(v)=W(t_*+v)-W(t_*)-W'(t_*)v.
 \tag{11}
\]
Let \(\phi_i\) be (11) for \(P_i\), with value \(+\infty\)
when its target lies outside the corresponding node interval in (9).
Let \(\chi_e,\chi_s,\chi_b\) be (11) for the edge potentials,
with respective target intervals
\([.52,.71]\), \([.5,.81]\), and \([.5,.95]\).
Each center is the corresponding starred real coordinate or starred
sum. All these potentials are convex on the union of their target
interval and the interval connecting it to the center: the node
cotangents have nonnegative real part and the edge cotangents have
nonpositive real part. The canonical private potential is strictly
convex by the cap estimate cited below.

Centers need not belong to target intervals. In particular
\(\Re z_*\) can exceed \(.31\), and the reference private
sum can exceed \(.71\). Definitions (10)--(11) retain those
actual centers. All inequalities use the entire connecting segment,
not a curvature bound available only inside the final target interval.

For any of these restricted scalar costs use the conjugate convention
\(\phi^*(v)=\sup_t\{vt-\phi(t)\}\). Then
\[
 \begin{split}
 L_* =\inf_{u,v,w\in\mathbb R}\bigl\{&
 \phi_e^*(A-u)+\phi_s^*(B-\ell-v-w)
 +\phi_z^*(A+B-3C-u-v)+\phi_b^*(-w)\\
 &+\chi_e^*(u)+\chi_s^*(v)+\chi_b^*(w)\bigr\}.
 \end{split}
 \tag{12}
\]

To prove the upper inequality, apply the scalar Fenchel inequality
on each node and edge. The edge linear forms contribute
\((u,v+w,u+v,w)\), exactly canceling the differences between
the node arguments in (12) and (8). The sum of all seven Bregman
costs is the Bregman cost of \(-f(\cdot,H)\), so the result
is the required upper bound on every admissible target.

For equality, take the actual final maximizing point and let
\(u,v,w\) be the three edge-cost derivatives there. Its real
stationarity equations give equality in each node Fenchel inequality;
at an original \(b\) endpoint the corresponding one-sided
condition gives the same equality for the restricted conjugate.
The edge inequalities are equalities by the definition of their
derivatives. Thus the infimum in (12) is attained. This proof retains
the original constrained maximum and introduces no independent
replacement reference.

## 4. Scalar evaluation and an explicit trial

Six costs in (12) have the form (11) for
\(W(t)=\mu\Re g(t+ih)\), with
\(\mu=2,3,1,-1,-1,-1\). Their scalar derivative equation
at a conjugate argument \(a\) is exactly
\[
 \begin{split}
 N_h(t)&=N_h(t_*)e^{2a/\mu},\\
 N_h(t)&=1+r^2-2r\cos(2\pi t),\qquad r=e^{2\pi h}.
 \end{split}
 \tag{13}
\]
For a node use the branch \(0<t<1/2\); for an edge use
\(1/2<t<1\). If \(a\) lies outside the derivative range
on its permitted interval, its maximizer is the appropriate clipped
endpoint. Otherwise (13) determines the unique cosine solution on
the stated branch. All values \(N_h(t_*)\) in (13) use the
height of that potential in (10), including the final height \(H\),
not the original height \(c\). These scalar operations do not
choose or solve an endpoint or conditional source root.

For the remaining private cost, the
[canonical cap estimate](research_mixed_private_cap_curvature_bound.md)
gives
\[
 P_e''(t)=\pi\{\Re\sigma(t+ih_e)+\Re\cot\pi(t+ih_e)\}
 >\frac{163\pi}{90},\qquad
 \phi_e^*(a)\le
 \max_{t\in[.3-e_{*,R},.4-e_{*,R}]}
              \left\{at-\frac{163\pi}{180}t^2\right\}.
 \tag{14}
\]
The bound holds on the full connecting interval and is a clipped
quadratic, not an alteration of the canonical phase.

For one explicit family of trial flows, choose any real \(\theta\)
and put
\[
 u=\theta A,\qquad v=(1-\theta)A+B-3C,\qquad
 r=3C-\ell-(1-\theta)A,\qquad w=r/4.
 \tag{15}
\]
The four node forces then become
\(((1-\theta)A,3r/4,0,-r/4)\). Since every Bregman cost
is nonnegative on its domain, \(\phi_z^*(0)\le0\), including
when its center is outside its target interval. Hence (12) gives
\[
 \begin{split}
 L_*\le{}&
 \phi_e^*((1-\theta)A)+\phi_s^*(3r/4)+\phi_b^*(-r/4)\\
 &+\chi_e^*(\theta A)
 +\chi_s^*((1-\theta)A+B-3C)+\chi_b^*(r/4).
 \end{split}
 \tag{16}
\]
In particular \(\theta=1/4\) is a fully specified trial depending
only on the same actual reference and \(H\). Combining (13)--(16)
reduces a sufficient integrated budget to six clipped scalar terms,
one of which has the explicit quadratic upper bound (14). Proving
that their sum is at most \(\pi/128\), for one permitted choice
of \(\theta\) at every actual reference, would establish (4).
No such uniform bound is asserted here. The fixed-reference and
outgoing-marginal correlations in (6)--(8) remain essential.

## 5. A nonlinear bound for the edge adjacent to its flat endpoint

The \(Q_s\) edge has zero real curvature at its permitted endpoint
\(t=1/2\). A positive uniform quadratic bound on the entire
edge interval therefore cannot replace its clipped conjugate. Its
specific factorial form nevertheless gives a uniform nonlinear bound:
\[
 \boxed{\displaystyle
       \chi_s^*(v)\le
       \frac{2}{3\pi}\sqrt{\frac{15}{14}}\,(-v)^{3/2}
                       \qquad(v\le0).}
 \tag{17}
\]
This holds for every actual fixed height in the present problem and
every such chosen dual flow; it requires no optimizing-point
curvature hypothesis.

To prove it, put \(\nu=2\pi(h_s+H)\) and
\(u=2\pi(t-1/2)\). The actual height range gives
\(|\nu|<1/2\), and \(0\le u\le.62\pi<2\). Thus
\[
 Q_s''(t)=\frac{\pi\sin u}{\cosh\nu+\cos u}
       \ge\frac{14\pi^2}{15}(t-1/2)=:\kappa(t-1/2).
 \tag{18}
\]
Here \(\cosh\nu<8/7\) follows from the positive series
\(\cosh(1/2)<1/(1-(1/2)^2/2)=8/7\). For the other
inequality in (18), the function
\[
 F(u)=\frac{15}{7}\sin u-u\left(\frac87+\cos u\right)
\]
vanishes at zero and has derivative
\[
 F'(u)=2\sin(u/2)
       \left\{u\cos(u/2)-\frac87\sin(u/2)\right\}\ge0.
 \tag{19}
\]
Indeed \(\tan w/w\) increases for \(0<w<1\), and
\(\tan1\le(101/120)/(389/720)=606/389<8/5\), using
the same alternating Taylor bounds. Consequently
\(2w\cot w>5/4>8/7\), which proves (19) at
\(w=u/2<1\). The denominator in (18) remains positive.

The center \(t_* =\Re(s_*+z_*)\) lies strictly inside
\([.5,.81]\), by the actual reference bounds in Section 1.
For a displacement \(-d\le0\) within this edge interval,
the full Bregman remainder satisfies
\[
 \begin{split}
 D_{Q_s}(-d)
 &=\int_{t_*-d}^{t_*}(r-(t_*-d))Q_s''(r)\,dr\\
 &\ge\kappa\int_0^d w\{t_*-d-1/2+w\}\,dw
 \ge\frac{\kappa d^3}{3}.
 \end{split}
 \tag{20}
\]
For a negative flow, targets to the right of the center have
nonpositive conjugate objective. Targets to the left satisfy
\[
 |v|d-D_{Q_s}(-d)\le |v|d-\kappa d^3/3
                    \le\frac{2|v|^{3/2}}{3\sqrt\kappa},
 \tag{21}
\]
including the clipped endpoint. Substituting \(\kappa\) proves
(17).

The outgoing edge has a companion bound
\[
 \boxed{\displaystyle
       \chi_b^*(w)\le
       \frac{2}{3\pi}\sqrt{\frac65}\,(-w)^{3/2}
                       \qquad(w\le0).}
 \tag{22}
\]
For a negative flow its maximizing target lies no farther right than
the reference center, which is less than \(.866<7/8\). Thus
only \(t\in[.5,7/8]\) matters. The fixed heights give
\(\cosh(2\pi(h_s+h_b))<7/5\). For an elementary witness,
\(.272\pi<43/50\) and
\[
 \cosh(43/50)
 \le1+\frac{(43/50)^2}{2}
       +\frac{(43/50)^4}{24(1-(43/50)^2/30)}<\frac75.
\]
On \(0\le u\le3\pi/4\), the function
\((12/5)\sin u-u(7/5+\cos u)\) is nonnegative. Its
derivative is \(2\sin(u/2)\{u\cos(u/2)-(7/5)\sin(u/2)\}\).
Because \(u\cot(u/2)\) decreases, this derivative changes
sign at most once, from positive to negative. The function's
minimum is therefore at an endpoint. Its value at zero is zero;
its other endpoint value exceeds
\(42/25-33/20=3/100\), using \(\sqrt2>7/5\) and
\(\pi<22/7\). Consequently
\(Q_b''(t)\ge(5\pi^2/6)(t-.5)\) on the required interval.
The same Bregman integral as (20)--(21) proves (22).

These bounds can be used in (12), or in (16) when its chosen flows
are nonpositive. One may also retain the omitted
\(\phi_z^*(0)\) from (12): when \(z_{*,R}>.31\), it is
the strictly negative Bregman cost at the target endpoint \(.31\),
an explicit additional credit.

## 6. A trial with both ordinary edge signs fixed

The original reference ranges imply
\[
                          A>0,\qquad 0<B<\ell.
 \tag{23}
\]
For \(A\), the real sum \(\Re(e_*+z_*)\) lies in
\((.579,.713)\), so \(\Re(E_*Z_*)<0\) and its modulus
increment in (7) is strictly positive. To treat \(B\), put
\(P=S_*Z_*\). Its real angle satisfies
\(1/2<\Re(s_*+z_*)<.783\), whence
\(\cos(2\pi\Re(s_*+z_*))<1/4\). Also
\[
                         \frac25<|P|<\frac85.
 \tag{24}
\]
Indeed \(h_s+c>-.135\), \(h_s+c<.068\), and the
positive-series estimate
\(e^t\le1+t+t^2/[2(1-t/3)]\), applied at
\(t=9/10\) and \(43/100\), proves
\(e^{.27\pi}<5/2\) and \(e^{.136\pi}<8/5\).
Thus \(|P|^2>\Re P\), which makes
\(|1-\lambda P|>|1-P|\). Further,
\(\Re P<2/5<1/2\), and
\[
 \lambda^2|1-P|^2-|1-\lambda P|^2
       =(\lambda-1)\{\lambda+1-2\lambda\Re P\}>0.
 \tag{25}
\]
This proves (23), with no independence assumption on the reference.

Set \(d=\ell-B>0\) and choose the following member of (15):
\[
 \begin{gathered}
 h=3C-\frac{B+\ell}{2},\qquad
 u=A-h,\quad v=-d/2,\quad w=-d/8,\qquad
 \theta=u/A,\\
 \text{node forces}=(h,-3d/8,0,d/8).
 \end{gathered}
 \tag{26}
\]
The two ordinary edge flows now have the signs required for (17)
and (22). Hence an entirely static sufficient test for (4) is
\[
 \begin{split}
 &\phi_e^*(h)+\phi_s^*(-3d/8)+\phi_b^*(d/8)
                    +\chi_e^*(A-h)+\phi_z^*(0)\\
 &\quad+\frac{2}{3\pi}\sqrt{\frac{15}{14}}(d/2)^{3/2}
       +\frac{2}{3\pi}\sqrt{\frac65}(d/8)^{3/2}
                         \le\frac\pi{128}.
 \end{split}
 \tag{27}
\]
The private term admits (14); all other conjugates in (27) are
the explicit clipped scalar functions from (13). This removes two
small-curvature denominators from the trial rather than replacing
them by independent minima. No sign for \(h\) or \(A-h\)
has been imposed. The inequality (27) itself remains unproved;
separate extremal bounds on \(A,B,C\) can lose their original
common-reference correlation.

## 7. An elementary sufficient inequality on the actual reference

The remaining terms in (27) also have uniform scalar majorants with
their required signs. For \(a\ge0\),
\[
 \phi_s^*(-a)\le\frac{5a^2}{4\pi},\qquad
 \phi_b^*(a)\le\frac{10a^2}{3\pi},\qquad
 \phi_e^*(h)\le\frac{45h^2}{163\pi}.
 \tag{28}
\]
For the first bound, only targets at most \(s_{*,R}<.433\)
can contribute a positive conjugate value. On the full connecting
interval \([.2,.433]\),
\(\Re\cot\pi(t+ih_s)>1/5\), so \(P_s''>2\pi/5\).
The real cotangent decreases with \(t\) on this interval.
At the upper endpoint its lower bound follows from
\[
 \cosh(.136\pi)<11/10,
 \qquad 5\sin(.134\pi)-\cos(.134\pi)>11/10.
 \tag{29}
\]
For the second inequality, use the increasing function
\(5\sin t-\cos t\) at \(t=.42<.134\pi\), with
the cubic sine lower and quartic cosine upper Taylor bounds.
The first follows from the positive-series bound for \(\cosh\)
at \(.43>.136\pi\).

For a positive force on the outgoing node, only targets at least
\(b_{*,R}\) matter. On the connecting interval up to \(.45\),
\[
 \Re\cot\pi(t+ih_b)
 \ge\frac{\sin(.1\pi)}{\cosh(.136\pi)+\cos(.1\pi)}
 >\frac{.308}{1.1+.952}>\frac3{20}.
 \tag{30}
\]
The sine and cosine bounds follow from their Taylor polynomials at
\(157/500<\pi/10\), using \(\pi>157/50\).
Thus \(P_b''>3\pi/20\). Applying the quadratic Bregman
bound with these curvatures proves the first two parts of (28).
The third is the unrestricted quadratic upper bound in (14).

The last edge is controlled on both signs. Define
\[
 \mathcal E(u)=
 \begin{cases}
 \dfrac23\sqrt{41/40}\,(-u)^{3/2},&u\le0,\\[3pt]
 \dfrac{1025}{158\pi}\,u^2,&u\ge0.
 \end{cases}
 \qquad \pi\chi_e^*(u)\le\mathcal E(u).
 \tag{31}
\]
Indeed \(|2\pi(h_e+H)|<.08\pi\), so its hyperbolic cosine
is less than \(21/20\), by the same positive-series estimate.
The connecting real interval has upper endpoint less than
\(.713<.75\). For \(0\le v\le\pi/2\), the derivative of
\((41/20)\sin v-v(21/20+\cos v)\) is nonnegative, since
\(v\cot(v/2)\ge\pi/2>21/20\). Consequently
\[
                  Q_e''(t)\ge\frac{40\pi^2}{41}(t-.5).
 \tag{32}
\]
For negative flows the cubic Bregman argument proves the first part
of (31). For positive flows, targets below the center have
nonpositive objective. Along a target above the center,
\(t\ge e_{*,R}+z_{*,R}>.579\), and (32) gives
\(Q_e''>79\pi^2/1025\); its quadratic conjugate bound
gives the second part. If the center exceeds the target interval,
all objectives for a positive flow are nonpositive instead, so this
upper bound still holds.

Combining (17), (22), (26), (28), and (31) proves the explicit bound
\[
 \begin{split}
 \pi L_*\le\mathcal B(A,B,C):={}&
 \frac{45}{163}h^2+\frac{175}{768}d^2
 +\frac23\sqrt{\frac{15}{14}}(d/2)^{3/2}\\
 &+\frac23\sqrt{\frac65}(d/8)^{3/2}
 +\mathcal E(A-h),\\
 d={}&\ell-B,\qquad h=3C-\frac{B+\ell}{2}.
 \end{split}
 \tag{33}
\]
Here the nonpositive \(\pi\phi_z^*(0)\) has been dropped;
it can be added back for a sharper comparison. Thus the single
reference inequality
\[
                    \mathcal B(A,B,C)\le\frac{\pi^2}{128}
 \tag{34}
\]
would suffice for the common central gap. It contains no unknown
optimizer displacement, curvature, outgoing active set, or scalar
conjugate. The only input values are the exact logarithmic increments
(6)--(7) of the same original coupled reference.

More concretely, the
[rational critical transport](research_mixed_rational_critical_transport.md),
Sections 1--2, parametrizes those data by the single original
complex endpoint coordinate \(U=e^{2\pi i u_*}\):
\[
 \begin{gathered}
 E_*=E(U),\qquad Z_*=Z_1(U),\qquad S_*=S_1(U),\qquad
 \lambda=\frac{e^{2\pi H}}{|Z_1(U)|},\\
       (\mathscr B_*,\mathscr C_*)=R_2(Z_1(U),S_1(U)).
 \end{gathered}
 \tag{35}
\]
Here \(\mathscr B_*=e^{-2\pi ib_*}\) is the outgoing
ordinary leg and \(\mathscr C_*\) is its next external leg;
these script letters are distinct from the logarithmic increments
\(B,C\). The canonical endpoint sheet, original logarithmic
lifts, all typed ordinary or attached domains, and the remaining
word's compatibility remain required. An arbitrary rational
preimage is not automatically an admissible reference.
Thus (34) is a concrete test on that original one-complex-parameter
family. The values \(A,B,C,d,h,u\) must be evaluated together
from (35), not optimized over independent intervals. Its derivation
does not assert (34). The exact dual (12) can also succeed where
this explicit trial and its majorants fail.

The endpoint test permits arbitrary intermediate curvature spikes.
It supplies neither the desired total scalar sign nor bounds for
private tails, aliases, joins, and other finite-source sectors. Its
proved contributions are the exact static comparison and the explicit
scalar majorants,
rather than a new conditional pointwise-curvature statement.
