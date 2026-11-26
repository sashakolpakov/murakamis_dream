# A smaller shared-index debit for two selected heights

Research deduction, 6 November 2026. The ordinary index shared by the
two selected lifts has opposite real forces. Its exact conjugate is
asymmetric in a favorable direction: a negative force costs no more
than the positive force of the same magnitude. This gives an explicit
additional debit which vanishes when the negative force is at most
twice the positive force. The condition is not asserted uniformly.
No new gain, primitive, reference, or source evaluation is performed.

## 1. The same fixed-center cost for both lifts

Write \(g_h(x)=\Re g(x+ih)\), with the original regular-strip
primitive. Fix
\[
 I=[11/50,1/2],\qquad x_*\in[6/25,9/25],\qquad
 |h|\le27/250,\qquad k>0,
 \tag{1}
\]
and define the exact Bregman cost and its conjugate by
\[
 \begin{split}
 \phi(x)&=k\{g_h(x)-g_h(x_*)-g_h'(x_*)(x-x_*)\},\\
 G(q)&=\sup_{x\in I}\{q(x-x_*)-\phi(x)\}.
 \end{split}
 \tag{2}
\]
Thus \(G\) is convex, \(G(q)\ge0\), and \(G(0)=0\).
All statements below use this same center, height, coefficient and
target interval. They do not compare separately rounded gains with
different centers.

**Lemma 1.** On (1), \(g_h''\) is nonnegative and strictly decreasing
on \(I\). For every \(q\ge0\),
\[
                              G(-q)\le G(q).
 \tag{3}
\]
On the positive half-line \(G\) is nondecreasing and has Lipschitz
constant \(1/2-x_*\).

*Proof.* With \(C=\cosh(2\pi h)\),
\[
 g_h''(x)=\frac{\pi\sin(2\pi x)}{C-\cos(2\pi x)},\qquad
 \frac{d}{dx}g_h''(x)=
 \frac{2\pi^2\{C\cos(2\pi x)-1\}}
                         {(C-\cos(2\pi x))^2}.
 \tag{4}
\]
The [cubic-cost bounds](research_mixed_terminal_cubic_cost_and_response_bounds.md)
give \(C<31/25\). Also
\(\cos(2\pi x)\le\cos(.44\pi)=\sin(.06\pi)<33/175\).
Hence \(C\cos(2\pi x)<1\), proving strict decrease; the first
formula is nonnegative on \(I\).

For \(0\le d\le x_*-11/50\),
\[
 \begin{split}
 \phi(x_*-d)&=k\int_0^d(d-y)g_h''(x_*-y)\,dy\\
 &\ge k\int_0^d(d-y)g_h''(x_*+y)\,dy
                                      =\phi(x_*+d).
 \end{split}
 \tag{5}
\]
The reflected target is allowed because
\[
       x_*-11/50\le1/2-x_*\quad\Longleftrightarrow\quad x_*\le9/25.
 \tag{6}
\]
For force \(-q\), targets above the center have nonpositive objective,
so a maximizer can be taken below it. Reflection in (5) then proves
(3). For \(q\ge0\), the same argument without reflection allows
restriction to \(x\ge x_*\). Thus \(G(q)\) is the supremum of
affine functions of \(q\) with slopes in \([0,1/2-x_*]\).
This proves monotonicity and the Lipschitz assertion. \(\square\)

The lemma applies to the terminal shared index with
\[
              x_*=\Re s_*,\qquad h=\Im s_*,\qquad k=2.
 \tag{7}
\]
The actual reconstructed family satisfies the stricter ordinary
height range \(-.102<\Im s_*<-.001\). The coefficient two is the
single shared cost from the symmetric pair theorem, not two
separately available copies of that cost.

## 2. Cancellation and an explicit debit

Let \(u<0<v\), and put \(a=-u>0\). Define the exact extra debit
\[
             R(u,v)=\max\{0,G(u+v)-G(v)\}.
 \tag{8}
\]
All positive parts below mean \(x_+=\max\{0,x\}\).

**Proposition 2.** For the cost (2),
\[
 0\le R(u,v)\le
 \min\left\{
       (1-v/a)_+\,G(-a),\
       (1/2-x_*)(a-2v)_+
      \right\}.
 \tag{9}
\]
In particular \(a\le2v\) implies \(R(u,v)=0\).
Both bounds in (9) are no larger after taking their minimum with
any other valid upper for the exact debit.

*Proof.* If \(a\le v\), convexity on \([0,v]\) gives
\[
                 G(v-a)\le(1-a/v)G(v)\le G(v).
 \tag{10}
\]
If \(a>v\), convexity on \([-a,0]\) gives
\[
                    G(v-a)\le(1-v/a)G(-a).
 \tag{11}
\]
Subtracting the nonnegative \(G(v)\), and then taking the positive
part, proves the first upper in (9). In particular this bound
never exceeds the previous debit \(G(u)=G(-a)\).

For the second upper, only \(a>v\) remains. By reflection,
\(G(v-a)\le G(a-v)\). If \(a-v\le v\), monotonicity makes this
at most \(G(v)\). Otherwise the positive-force Lipschitz bound gives
\[
            G(a-v)-G(v)\le(1/2-x_*)(a-2v).
 \tag{12}
\]
This proves the second upper and the vanishing assertion.
The linear upper alone need not be smaller than \(G(u)\) for
arbitrary force sizes; their minimum retains that improvement
without an extra force-size assumption. \(\square\)

The proof also gives the signed comparison
\[
 G(u+v)-G(v)\le
 \begin{cases}
 -(a/v)G(v),&a\le v,\\
 (1-v/a)G(-a)-G(v),&a>v.
 \end{cases}
 \tag{13}
\]
It can provide a favorable negative contribution. A future
outward implementation must not subtract a saved *upper* bound
for \(G(v)\) as if it were a lower bound. Equation (9) avoids
that issue entirely. Its linear option uses no new scalar gain.

## 3. The original two-height forces and their correlation

Use the exact reconstructed references
\((c_*,r_*,b_*,s_*,a_*,t_*,v_*)\) from the
[reference reconstruction](research_mixed_terminal_two_selected_reference_reconstruction.md).
Suppress stars in the following formulas. Set
\[
 H=1/100,\quad \Delta_b=H-\Im b>0,\quad
 \Delta_a=H-\Im a>0,\quad
 \bar b=b+i\Delta_b,\quad\bar a=a+i\Delta_a.
 \tag{14}
\]
Let \(L(z;d)=g'(z+id)-g'(z)\). The two forces acting on \(s\) are
\[
                 u=\Re L(s+b;\Delta_b)-2\pi\Delta_b,\qquad
                 v=\Re L(s+a;\Delta_a).
 \tag{15}
\]
They obey \(u<0<v\), as proved in the
[budget composition](research_mixed_terminal_two_selected_budget_composition.md).
The whole vertical segments have real parts in \((.48,.72)\);
there \(|\Im\cot\pi z|<1\).

For the normalized means
\[
 I_b=\int_0^1\Im\cot\pi(s+b+i\theta\Delta_b)\,d\theta,\qquad
 I_a=\int_0^1\Im\cot\pi(s+a+i\theta\Delta_a)\,d\theta,
 \tag{16}
\]
the exact formulas are
\[
             -u=\pi\Delta_b(1+I_b),\qquad
               v=\pi\Delta_a(1-I_a).
 \tag{17}
\]
Thus the sufficient vanishing condition in Proposition 2 is precisely
\[
                \Delta_b(1+I_b)\le2\Delta_a(1-I_a).
 \tag{18}
\]
No independent endpoint choices for the two sides of (18) are imposed:
all coordinates and both means refer to the same old complex
parameter \(b\) on \(\Omega^K_{\gamma,\epsilon}\).
Neither the ordinary image rectangles alone nor the sign
\(u<0<v\) proves (18).

Original \(s\)-stationarity also gives a useful alternative exact
expression:
\[
 u+v=\Re\{g'(s+\bar b)+g'(s+\bar a)-3g'(s)+2\pi i\bar b\}.
 \tag{19}
\]
Indeed subtract
\(g'(s+b)+g'(s+a)-3g'(s)+2\pi ib=0\).
The incoming chirp changes by the real quantity
\(-2\pi\Delta_b\), exactly as in (15). Formula (19) does not
identify an affine approximation center with the stationary point.
It removes the separate old-height differences before bounding
the shared force; no new logarithm evaluation is supplied here.

## 4. Smaller sufficient ordinary-lift inequalities

Retain \(T_{b,\mu},A_r,A_{b,\mu},G_r,G_{b,\mu}\) and both
complete-weight alternatives \(\mu=1,0\) from the budget-composition
theorem. Every completed terminal route, including its alternative
\(\nu\) and original label \(\sigma\), has before outward rounding
the form
\[
               \mathfrak A_{\sigma,\nu}
                     =T_{\sigma,\nu}+G_s(v)+R_{\sigma,\nu}.
 \tag{20}
\]
Its two-height comparison therefore satisfies
\[
 \begin{split}
 \mathfrak D_{\mu,\nu,\sigma}
 &\le\mathfrak A_{\sigma,\nu}
       +T_{b,\mu}+G_r(A_r)+G_{b,\mu}(A_{b,\mu})\\
 &\hspace{30mm}+G_s(u+v)-G_s(v)\\
 &\le\mathfrak A_{\sigma,\nu}
       +T_{b,\mu}+G_r(A_r)+G_{b,\mu}(A_{b,\mu})+R(u,v).
 \end{split}
 \tag{21}
\]
This uses the one shared Hessian cost before applying its conjugate.
It does not spend that cost twice.

Consequently the following pair of inequalities is a sufficient
replacement for the two original added-budget inequalities:
\[
 T_{b,\mu}+G_r(A_r)+G_{b,\mu}(A_{b,\mu})+
 \min\left\{
 (1-v/(-u))_+G_s(u),\
 (1/2-\Re s)(-u-2v)_+
 \right\}\le0,\qquad \mu=0,1.
 \tag{22}
\]
When (18) is proved, the entire final term in (22) is zero.
Without (18), the second option is an explicit force-size debit
requiring no additional gain; the first option guarantees an
improvement over simply adding \(G_s(u)\).
The original \(b\)-gain stays signed on any permitted restricted
forced interval. Nothing in this argument enlarges that interval
or removes a complete Fourier alternative.

The still missing assertion is uniform validity of (22) on the
actual filtered families. No ratio condition, negative budget,
source gap or new knot-family theorem is concluded here.
All original source eligibility, reference correlations and
ordinary-color hypotheses of the completed terminal routes remain.
