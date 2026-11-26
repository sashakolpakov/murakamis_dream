# A smaller terminal main optimizer box

Research deduction, 6 November 2026. At the original terminal reference
heights, both complete-weight main alternatives attain their maximum
with \( .22<t_R<.4 \). For terminal type four one also has \(e_R<.4\).
The type-four terminal block has a useful diagonal curvature bound on
this smaller product. These are whole-target localization statements,
not a new sign of the main comparison. No root, source, primitive or
target evaluation is performed.

## 1. Scope and the scalar derivative

Use the literal joint main phase \(D_\nu\), its original incoming
affine marginal, and both complete-weight alternatives from
[the joint-main budget](research_mixed_terminal_joint_main_budget.md),
equations (2)--(8). The selected height can be any
\(0\le H\le7/500\). The factorial target for \(a_R\) is
\(P=[.22,.45]\); the forced target may be restricted to
\([.4,.45]\) by complete-weight dominance. The argument below holds
even on its containing full-\(P\) product.

Every other target keeps its original reference height. In particular,
the [original endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md)
give
\[
\begin{array}{c|c|c}
\epsilon&h_t&h_v\\ \hline
0&(-.072,.021)&h_\xi\in(.049,.077)\\
1&(-.108,-.020)&h_e\in(-.051,-.019).
\end{array}
\tag{1}
\]
The private real target is the entire original interval
\(\xi_R\in[.1,.4]\) or \(e_R\in[.27,.49]\).
No restriction on the incoming \(b\)-height beyond the joint-main
theorem is used here. In particular the separate ordinary-index
barrier requiring \(h_b\le.021\) is not being imported.

Write \(x=t_R\), \(y=a_R\), \(z=v_R\), and put
\[
r=e^{2\pi h_t},\qquad R=e^{-2\pi H},\qquad s=e^{2\pi h_v}.
\]
Both terminal phases have the same transform derivative, so
\[
\exp(2\Re\Phi_{\epsilon,t})=
\frac{\{R^2+r^2-2Rr\cos2\pi(x+y)\}
      \{1+r^2s^2-2rs\cos2\pi(x+z)\}}
     {\{1+r^2-2r\cos2\pi x\}^{3}}.
\tag{2}
\]
This retains the chirp \(2\pi iat\): its modulus contribution
is precisely the replacement of \(1\) by \(R\) in the first
factor. The ordinary block, selected weight, and incoming affine
subtraction are independent of \(t\).

The elementary height bounds used below are
\[
\begin{array}{c|c|c}
\epsilon&r&s\\ \hline
0&(1/2,6/5)&(1,5/3)\\
1&(1/2,1)&(7/10,1).
\end{array}
\qquad 10/11<R\le1.
\tag{3}
\]
For example \(e^{.216\pi}<2\) is the already proved elementary
bound in [the last-row proof](research_mixed_selected_four_three_last_rows.md).
The remaining bounds also follow directly from
\[
e^x\le1+x+\frac{x^2}{2(1-x/3)}\quad(0\le x<3),
\qquad e^x\le(1-x)^{-1}\quad(0\le x<1).
\]
Use \(.154\pi<1/2\), \(.102\pi<1/3\),
\(.042\pi<1/6\), and \(.028\pi<1/11\), respectively.
At \(x=1/2\) the first majorant is \(33/20<5/3\);
at \(x=1/3\) it is \(67/48<10/7\).

## 2. Both transform barriers

**Proposition 1.** For every original reference satisfying (1),
both joint-main alternatives have every maximizer in
\[
                         .22<t_R<.4.
\tag{4}
\]

At \(x=.22\), uniformly for \(y\in P\),
\(\cos2\pi(x+y)<-12/25\) and
\(\cos2\pi x>9/50\). For type four,
\(x+z\in[.49,.71]\) gives
\(\cos2\pi(x+z)<-6/25\). For type three,
\(x+z\in[.32,.62]\) gives
\(\cos2\pi(x+z)<-2/5\).
These strict rational witnesses follow from
\[
\sin(.16\pi)>.48,\quad \sin(.08\pi)>.24,\quad
\sin(.14\pi)>.4,\quad \sin(.06\pi)>.18.
\tag{5}
\]
For each, use \(157/50<\pi<22/7\) in
\(\sin u\ge u-u^3/6\); the arguments are below \(51/100\).

Set \(D(r)=1+r^2-9r/25\). Equation (2) gives the lower
bounds \(N_\epsilon(r)/D(r)^3\), where
\[
\begin{split}
N_1(r)&=(100/121+r^2+48r/55)
                    (1+49r^2/100+42r/125),\\
N_0(r)&=(100/121+r^2+48r/55)(1+r^2+4r/5).
\end{split}
\tag{6}
\]
Both lower bounds exceed one on their complete intervals (3).
For an exact polynomial certificate, the Bernstein coefficients of
\(N_1-D^3\), after \(r=(1+q)/2\), \(0\le q\le1\),
in degree six are
\[
\left(
\frac{43997911}{60500000},\
\frac{77099581}{90750000},\
\frac{576209067}{605000000},\
\frac{77085023}{75625000},\
\frac{76940223}{75625000},\
\frac{20131531}{22687500},\
\frac{355951}{687500}
\right).
\tag{7}
\]
For \(N_0-D^3\), after \(r=1/2+7q/10\), they are
\[
\left(
\frac{13982027}{11000000},\
\frac{1024159637}{605000000},\
\frac{24648179771}{11343750000},\
\frac{102062300947}{37812500000},\
\frac{45442859603}{14179687500},\
\frac{9965059639}{2835937500},\
\frac{749221629}{236328125}
\right).
\tag{8}
\]
All are strictly positive. Thus \(\Re\Phi_{\epsilon,t}>0\)
on the entire face \(t_R=.22\).

At \(x=.4\), the first summed real part belongs to
\([.62,.85]\), hence \(-\cos2\pi(x+y)<3/4\).
Also \(\cos(.8\pi)<-4/5\), and the second numerator
factor is at most \((1+rs)^2\). The two trigonometric
bounds follow from
\(\cos(.24\pi)<3/4\) and \(\cos(.2\pi)>4/5\),
using the degree-four upper and degree-two lower cosine polynomials.
Consequently (2) is strictly below
\[
\frac{(1+r^2+3r/2)(1+5r/3)^2}
     {(1+r^2+8r/5)^3}.
\tag{9}
\]
The denominator minus numerator is positive for every \(r\ge1/2\):
its coefficients in powers of \(q=r-1/2\) are
\[
\left(
\frac{136289}{72000},\
\frac{24309}{2000},\
\frac{539767}{18000},\
\frac{41063}{1125},\
\frac{21287}{900},\
\frac{39}{5},\
1
\right).
\tag{10}
\]
Thus \(\Re\Phi_{\epsilon,t}<0\) on the whole face \(t_R=.4\).

For fixed values of the other targets, the full joint phase is
strictly concave as a function of \(t_R\), by joint-main Lemma 1.
Its derivative is therefore positive below the lower face and
negative above the upper face. Moving toward the interval improves
the phase, including at the two faces. This proves (4) on the
original target product, without assuming an interior critical point.
\(\square\)

## 3. Type-four private localization and curvature

**Proposition 2.** For terminal type four, every maximizer further
satisfies \(e_R<.4\). On the resulting containing product
\[
a_R\in P,\qquad t_R\in[.22,.4],\qquad e_R\in[.27,.4],
\tag{11}
\]
at the heights above, the bare terminal block obeys
\[
-\Re\Phi_1''\succ
\pi\,\operatorname{diag}
\left(\frac{13}{100},\frac{63}{100},\frac{47}{172}\right)
\quad\hbox{in the order }(a,t,e).
\tag{12}
\]

For the private barrier use the original
\[
D_e(e,t)=\Re\{S'(e)+g'(e+t)-g'(e)-i\pi/2+i\pi e\}.
\]
The already certified private test in
[the optimizer bounds](research_mixed_selected_boundary_optimizer_bounds.md),
Section 2, gives \(D_e(.4+ih_e,.22+.014i)<-1/20\)
for every \(h_e\in[-.051,-.019]\).
At \(e_R=.4\), \(D_e\) decreases with \(t_R\in[.22,.4]\),
because \(\Re\cot\pi(e+t)<0\).
At \(t_R=.22\) it increases with \(h_t\) up to \(.014\):
the summed real part is \(.62\), where the doubled-angle cosine
is negative, and therefore
\(\partial_{h_t}D_e=\pi(1-\Im\cot\pi(e+t))>0\).
The original \(h_t<0\) is covered. Concavity in \(e_R\) now
excludes every \(e_R\ge.4\). This uses an existing scalar
certificate, not a new evaluation of the cap branch.

For (12), write \(C(w)=\Re\cot\pi w\) and
\(V(x,y)=J(x+y)-J(x)-J(y)\). Up to a real-coefficient
imaginary quadratic, the terminal phase is
\[
                   S(e)+V(t,a)+V(t,e)-J(t).
\tag{13}
\]
The [terminal-three scalar bounds](research_mixed_terminal_three_joint_zero_mode.md),
equations (7)--(9), imply \(C(a)>13/100\),
\(C(t),C(e)>1/4\) on (11); if an individual real part is
at most \(.3\) and at least \(.2\), its cotangent exceeds \(7/12\).
All heights here have absolute value at most \(.12\).

If \(t_R+a_R\ge.5\), the negative Hessian of \(V(t,a)\)
dominates \(\pi\operatorname{diag}(C(t),C(a))\).
Otherwise both real coordinates lie in \([.22,.28]\), while
\(0<C(t+a)\le\cot(.44\pi)<1/5\).
The rank-one term is bounded using
\((dt+da)^2\le2(dt^2+da^2)\).
In both cases
\[
                 -\Re V(t,a)''\succ(13\pi/100)I_2.
\tag{14}
\]
Similarly \(V(t,e)\) dominates \((\pi/4)I_2\) if the
sum is at least \(.5\). Otherwise the two individual cotangents
exceed \(7/12\), and \(C(t+e)<\cot(.49\pi)<1/30\),
which gives the same bound. The two tangent upper bounds follow
from \(\tan u<u/(1-u^2/2)\) at \(u=.06\pi,.01\pi\).
Finally \(-J(t)\) contributes more than \(\pi/4\) in the
\(t\)-coordinate, and the
[original cap Schur bound](research_mixed_first_cap_plateau_phase.md),
equation (9), gives \(-\Re S''>\pi/43\).
Adding these four bounds proves (12). \(\square\)

For terminal type three, (4) places the whole optimizing product
inside the original smaller terminal box, so its already proved
\(-\Re\Phi_0''\succ(3\pi/50)I_3\) applies. No private
type-three interval is shortened here.

## 4. What real elimination permits

The [terminal-three critical curve](research_mixed_terminal_three_critical_curve.md)
solves the full complex equations \(\Phi_t=\Phi_\xi=0\),
allowing both complex coordinates to move. It must not be substituted
for the horizontal maximizer at fixed original heights. For example,
writing \(w=e^{-2\pi i\xi}\), \(z=e^{-2\pi it}\), the
actual interior horizontal private equation is only
\[
              |1+w|^4|1-wz|^2=|1-w|^8.
\tag{15}
\]
It does not assert
\((1+w)^2(1-wz)=(1-w)^4\), which also imposes an
unavailable imaginary equation. Original logarithmic branches remain
fixed throughout; exponentiating a real derivative here only uses
the modulus of its original exponential.

There is an exact real Schur reduction on each free private face.
Put \(p=C(t)\), \(b=C(a)\), \(d=C(t+a)\),
\(c=C(t+v)\), and
\[
K_0=4C(\xi)+2\Re\tan\pi\xi,\qquad
K_1=-\Re S''(e)/\pi+C(e).
\]
The real terminal negative Hessian divided by \(\pi\), in
the order \((a,t,v)\), is
\[
\begin{pmatrix}
b-d&-d&0\\
-d&3p-d-c&-c\\
0&-c&K_\epsilon-c
\end{pmatrix}.
\tag{16}
\]
At an interior conditional private maximizer its reduced Hessian is
the real Schur complement
\[
\begin{pmatrix}
b-d&-d\\
-d&3p-d-\displaystyle\frac{cK_\epsilon}{K_\epsilon-c}
\end{pmatrix}.
\tag{17}
\]
The denominator is positive by the proved joint concavity. At a
fixed private endpoint the correction \(c^2/(K_\epsilon-c)\)
is absent. The active-face theorem in
[the original curvature budget](research_mixed_active_face_curvature_budget.md),
Section 1, supplies this distinction without assuming strict
complementarity or differentiability at every face transition.

These implications give valid stronger domains and curvature for a
quadratic or Bregman main budget. They do not prove its final negative
sign, localize the ordinary/incoming coordinates, justify a complex
moving-root substitution, or control the other terminal profiles.
Only exact rational polynomial arithmetic was used to verify
(7), (8), and (10); no saved source value was recomputed.
