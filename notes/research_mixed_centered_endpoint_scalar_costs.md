# Centered scalar costs and a free private-edge flow

Research deduction, 6 November 2026.

This note strengthens the proved scalar majorant in
[the static endpoint budget](research_mixed_selected_endpoint_legendre_budget.md).
It retains the actual center of the private edge, proves a negative
credit for the final first-coordinate restriction, and explicitly
optimizes a dual flow that the earlier trial fixed. It does not prove
the remaining uniform endpoint inequality or a finite-source theorem.

All notation, fixed heights, the original outgoing tangent, and the
actual first-four/next-three reference are as in that note. In particular
\[
 H=7/625,\quad -.07<c<-.02,\quad
 \ell=2\pi(H-c),\quad d=\ell-B,\quad
 h=3C-(B+\ell)/2,
 \qquad 0<d<\ell.
 \tag{1}
\]
The inequalities below hold for every such actual reference, with no
new source root, parameter cover, or independent choice of marginal.

## 1. Additional signs of the logarithmic increments

The existing reference ranges imply the strict bounds
\[
 \ell/4<A<\ell/2,\qquad 2\ell/5<C<\ell/2,
 \qquad \ell/5+d/2<h<\ell/2+d/2.
 \tag{2}
\]
In particular \(h>7d/10>0\). If \(d\ge3\ell/5\), they
also imply \(A-h<0\).

For the upper bound on \(A\), the full fixed-reference segment has
\(h_e+k<0\), since \(h_e<-.019\) and \(k\le H=.0112\).
For any fixed real angle \(t\),
\[
 \frac{d}{dk}\log|1-e^{2\pi(k-it)}|
 =\pi+\frac{\pi\sinh(2\pi k)}
                   {\cosh(2\pi k)-\cos(2\pi t)}.
 \tag{3}
\]
Thus the derivative giving \(A\) is less than \(\pi\).
Its positivity follows from the negative cosine of the private summed
angle, as in the original endpoint budget. Integration proves the
upper bound.

For the stronger lower bound, put
\(\alpha=\ell/2-A\) and
\(q_e=\cos(2\pi\Re(e_*+z_*))\). The real summed interval
\((.579,.713)\) gives \(q_e<-1/5\): at its upper endpoint,
\(-q_e\ge\sin(.074\pi)>\sin(.23)>.23-.23^3/6>1/5\).
The two negative heights \(h_e+c<h_e+H<0\) have absolute
arguments below \(.242\pi<77/100\). On that argument interval,
the same positive-series estimate as (5) gives
\(\sinh t/t<9/8\). Applying the logarithmic-difference argument
used below to these two heights therefore yields
\[
 \frac\alpha\ell
 <\frac{(9/8)\pi(-2h_e-c-H)}{2(6/5)}
 <\frac{(9/8)(22/7)(201/1250)}{2(6/5)}
 =\frac{6633}{28000}<\frac14.
\]
This proves \(A>\ell/4\).

Put \(x=z_{*,R}\), \(q_z=\cos(2\pi x)\),
\(a=-2\pi c\), and \(b=2\pi H\). Then
\[
 C=\ell/2-\gamma,\qquad
 \gamma=\frac12\log
       \frac{\cosh a-q_z}{\cosh b-q_z}>0.
 \tag{4}
\]
Here \(0<b<a<.14\pi<11/25\), and
\(q_z<\sin(.008\pi)<13/500\). The positive series gives
\[
 \frac{\sinh t}{t}
 \le1+\frac{t^2}{6(1-t^2/20)}<21/20
                  \quad(0\le t\le11/25).
 \tag{5}
\]
Integrating this bound and using \(\log(1+r)\le r\) yields
\[
 \frac\gamma\ell
 <\frac{(21/20)\pi(-c-H)}{2(487/500)}
 <\frac{(21/20)(22/7)(147/2500)}{2(487/500)}
 =\frac{4851}{48700}<\frac1{10}.
 \tag{6}
\]
This proves the two bounds on \(C\). Finally
\(h=3C-\ell+d/2\), proving all remaining assertions of (2).
No sign of \(A-h\) is asserted outside the displayed sufficient
condition.

## 2. The clipped quadratic first-coordinate credit

On the full connecting interval \([.22,.35]\),
\[
 P_z''(t)=3\pi\Re\cot\pi(t+iH)>3\pi/2.
 \tag{7}
\]
The real cotangent decreases on this interval: its derivative has the
sign of \(\cosh(2\pi H)\cos(2\pi t)-1<0\).
At \(t=.35\), use
\[
 \cosh(2\pi H)<201/200,\quad
 \sin(.7\pi)=\cos(\pi/5)>161/200,\quad
 -\cos(.7\pi)=\sin(\pi/5)<3/5.
 \tag{8}
\]
These imply \(\Re\cot\pi(.35+iH)>(161/200)/(321/200)>1/2\).
The cosine bound follows from \(\sqrt5>111/50\); the sine bound
follows from \(\sqrt5>11/5\). The hyperbolic bound follows by
substituting \(2\pi H<(14/625)(22/7)\) in
\(1+t^2/2+t^4/[24(1-t^2/30)]\).

Writing \(x=z_{*,R}\), the restricted conjugate consequently obeys
\[
 \pi\phi_z^*(a)
 \le\max_{v\in[.22-x,.31-x]}
              \{\pi av-3\pi^2v^2/4\}
 \le a^2/3.
 \tag{9}
\]
In particular
\[
 \pi\phi_z^*(0)
 \le-\frac{3\pi^2}{4}(x-.31)_+^2.
 \tag{10}
\]
This is a negative credit when the actual center is above its final
target interval, rather than a change of the reference center.

## 3. A centered cubic majorant for the private-edge conjugate

Set
\[
 q=\Re(e_*+z_*)-\tfrac12\in(.079,.213),\quad
 \kappa=40\pi^2/41,\quad
 a_0=1/50,\quad b_0=21/100.
 \tag{11}
\]
The target interval for this edge is \([.52,.71]\), so its target
\(y=t-1/2\) lies in \([a_0,b_0]\). The full connecting interval
is contained in \((.5,.713)\). Equation (32) of the endpoint budget
proves \(Q_e''(t)\ge\kappa(t-1/2)\) there. Consequently
\[
 D_{Q_e}(y-q)\ge
 K_q(y):=\frac\kappa6\{y^3-q^3-3q^2(y-q)\}.
 \tag{12}
\]
This follows by subtracting \(\kappa(t-1/2)^3/6\) from \(Q_e\):
the difference is convex on the entire connecting interval, so its
Bregman remainder is nonnegative.

Define the explicit function
\[
 \begin{split}
 Y_q(u)&=\operatorname{clip}_{[a_0,b_0]}
       \sqrt{\max\{0,q^2+2u/\kappa\}},\\
 T_q(u)&=u\{Y_q(u)-q\}-K_q(Y_q(u)).
 \end{split}
 \tag{13}
\]
Then, for every real flow \(u\),
\[
                       \chi_e^*(u)\le T_q(u).
 \tag{14}
\]
Indeed \(T_q(u)=\max_{a_0\le y\le b_0}\{u(y-q)-K_q(y)\}\).
The derivative of its objective is
\(u-\kappa(y^2-q^2)/2\), which decreases strictly on the positive
target interval. This gives exactly (13), including clipping and the
case \(q>b_0\).

The new bound dominates both branches of the earlier majorant:
\[
                        \pi T_q(u)\le\mathcal E(u).
 \tag{15}
\]
For \(u\le0\), positive displacements have nonpositive objective.
For a negative displacement \(-v\), the exact model remainder is
\(\kappa(qv^2/2-v^3/6)\ge\kappa v^3/3\), because
\(v\le q\). The same cubic maximization as before proves the first
branch of (15). For \(u\ge0\), negative displacements have
nonpositive objective; positive ones have remainder at least
\(\kappa qv^2/2>79\pi^2v^2/2050\). This proves the second branch.
The argument remains valid when zero displacement is not a permitted
target.

## 4. Explicit optimization of a free private-edge flow

Let
\[
 \begin{split}
 C_0(d)={}&\frac{175}{768}d^2
 +\frac23\sqrt{15/14}\,(d/2)^{3/2}
 +\frac23\sqrt{6/5}\,(d/8)^{3/2},\\
 D={}&\frac{298}{489},\qquad m=A-\frac{163}{298}h.
 \end{split}
 \tag{16}
\]
In the exact dual keep \(v=-d/2\), \(w=-d/8\), and allow the
private-edge flow \(u\) to vary. The four node forces are then
\[
                  (A-u,-3d/8,A-h-u,d/8).
 \tag{17}
\]
The proved node and ordinary-edge bounds, (9), and (14) give
\[
 \pi L_*\le C_0(d)+\frac{45}{298}h^2
              +\inf_{u\in\mathbb R}\{D(u-m)^2+\pi T_q(u)\}.
 \tag{18}
\]
The coefficient and center follow from completing the square in
\((45/163)(A-u)^2+(A-h-u)^2/3\).

The infimum in (18) has an explicit evaluation. Define
\[
 J(y)=\frac{\pi(y-q)}{2D}+\frac\kappa2(y^2-q^2).
 \tag{19}
\]
This function increases strictly for \(y>0\). Set \(y_*=a_0\)
if \(m\le J(a_0)\), and \(y_*=b_0\) if \(m\ge J(b_0)\).
Otherwise let \(y_*\) be the unique root in \((a_0,b_0)\) of
\[
                \kappa D(y_*^2-q^2)+\pi(y_*-q)=2Dm.
 \tag{20}
\]
This is a quadratic equation with positive derivative on the target
interval. Put \(v_*=y_*-q\). Then
\[
 \boxed{\displaystyle
 \pi L_*\le C_0(d)+\frac{45}{298}h^2
        +\pi m v_*-\frac{\pi^2v_*^2}{4D}-\pi K_q(y_*).}
 \tag{21}
\]

For a direct proof of the infimum evaluation, maximize the strictly
concave function
\[
 \pi m(y-q)-\frac{\pi^2(y-q)^2}{4D}-\pi K_q(y)
                         \quad(a_0\le y\le b_0).
 \tag{22}
\]
Its derivative is \(\pi\{m-J(y)\}\), so its unique maximum
occurs at the specified \(y_*\). Set
\(u_*=m-\pi v_*/(2D)\). The same endpoint or interior derivative
condition shows that \(y_*\) maximizes
\(u_*(y-q)-K_q(y)\); hence it attains \(T_q(u_*)\).
Completing the square in \(u\) shows that (22) is a lower bound
on \(D(u-m)^2+\pi T_q(u)\) for every \(u\), and is equal to it
at \(u_*\). This proves (21) without an interchange of an
unverified infimum and supremum.

Alternatively retain the balanced flow \(u=A-h\) and the clipped
credit (10). This proves the distinct bound
\[
 \pi L_*\le C_0(d)+\frac{45}{163}h^2+\pi T_q(A-h)
                         -\frac{3\pi^2}{4}(x-.31)_+^2.
 \tag{23}
\]
Both right sides (21) and (23) are at most the previous majorant
\(\mathcal B(A,B,C)\): in (18) one may choose \(u=A-h\),
and (15) applies. Their minimum is therefore a proved improvement
on that majorant at every actual reference.

## 5. A simpler bound with no clipped root

The centered model also supplies a useful quadratic bound on both
signs. For every permitted target, \(2q+y>89/500\), and
\[
 K_q(y)=\frac\kappa6(2q+y)(y-q)^2
       \ge\frac{89\pi^2}{3075}(y-q)^2.
 \tag{24}
\]
Consequently
\[
 \pi\chi_e^*(u)\le k_0u^2\quad(u\in\mathbb R),
                       \qquad k_0=\frac{3075}{356\pi}.
 \tag{25}
\]
This bound uses the full Bregman remainder; it does not assert that
the edge has this uniform pointwise curvature down to its target
endpoint. Centers above the target interval are still retained.

Substitution in (18) and the exact quadratic minimum give
\[
 \begin{split}
 \pi L_*&\le C_0(d)+\frac{45}{298}h^2
       +\frac{Dk_0}{D+k_0}
                    \left(A-\frac{163}{298}h\right)^2\\
 &\le\boxed{\displaystyle
 C_0(d)+\frac{45}{298}h^2
       +\frac12\left(A-\frac{163}{298}h\right)^2}.
 \end{split}
 \tag{26}
\]
Indeed \(Dk_0/(D+k_0)<1/2\) is equivalent to
\(\pi>329025/106088\), which follows from \(\pi>157/50\).
The minimizing flow for the first line is
\(u=Dm/(D+k_0)\). Formula (26) is an unconditional endpoint
majorant on the stated actual-reference domains, expressed only in
the correlated logarithmic increments and \(\ell\). It keeps
the cross term between \(A\) and \(h\), and has no edge-sign
case or clipped scalar operation. The sharper bound (21) is at most
the first line of (26).

## 6. The actual outgoing sum improves its ordinary-edge cost

There is a stronger existing bound on the outgoing reference sum.
Proposition 1 and Section 3 of
[the reduced-disk pair-sum theorem](research_mixed_reduced_disk_pair_sums.md)
apply to every ordinary vertex of the original open word and give
\[
             3/5<\Re(s_*+b_*)<77/100.
 \tag{27}
\]
The two external legs of vertex 2 belong to its full reduced-disk
products by the actual nonprivate-leg inclusion theorem, including
when the next external leg is attached at word length three.
Thus (27) applies to the same actual reference used throughout;
it does not impose a new ordinary root or a moving-target sum bound.

Put \(q_b=\Re(s_*+b_*)-1/2>1/10\) and
\(\kappa_b=5\pi^2/6\). For a nonpositive outgoing flow only
targets at or to the left of the center can give positive conjugate
objective. Their full connecting intervals are inside \([.5,.77]\),
where the proved bound \(Q_b''(t)\ge\kappa_b(t-.5)\) applies.
For a left displacement \(-v\), with \(0\le v\le q_b\),
\[
 D_{Q_b}(-v)\ge\kappa_b(q_bv^2/2-v^3/6)
 \ge\kappa_bq_bv^2/3\ge\pi^2v^2/36.
 \tag{28}
\]
The resulting one-sided quadratic conjugate bound is
\[
             \pi\chi_b^*(w)\le\frac9\pi w^2
                            \qquad(w\le0).
 \tag{29}
\]
In every bound above one may therefore replace \(C_0(d)\) by
\[
 C_1(d)=\left(\frac{175}{768}+\frac9{64\pi}\right)d^2
             +\frac23\sqrt{15/14}\,(d/2)^{3/2}.
 \tag{30}
\]
This is smaller than \(C_0(d)\) throughout the actual interval
\(0<d<\ell<203\pi/1250\). Indeed the comparison of the two
outgoing terms is equivalent to \(d<64\pi^2/1215\), and
\(203\pi/1250<64\pi^2/1215\) follows from
\(\pi>246645/80000\), itself implied by \(\pi>157/50\).

In particular the following simpler all-sign endpoint estimate is
proved on the original actual-reference domains:
\[
 \boxed{\displaystyle
 \pi L_*\le
 \left(\frac{175}{768}+\frac9{64\pi}\right)d^2
 +\frac23\sqrt{15/14}\,(d/2)^{3/2}
 +\frac{45}{298}h^2
 +\frac12\left(A-\frac{163}{298}h\right)^2.}
 \tag{31}
\]
If only rational coefficients outside the single remaining radical
are desired, \(175/768+9/(64\pi)<211/768\) follows from
\(\pi>3\). The sharper clipped bound (21) and negative-credit
bound (23) may likewise use \(C_1\).

These are explicit inequalities with no unknown maximizing source
point or scalar conjugate. They do not assert that either right side
is uniformly at most \(\pi^2/128\). The data \(A,B,C,q,x\) must
still come together from the same original reference, with the
canonical sheet and the next ordinary vertex's compatibility retained.
