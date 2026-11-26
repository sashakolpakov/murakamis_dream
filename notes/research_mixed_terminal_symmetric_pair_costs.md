# Retaining convexity in both variables of an adjoining pair

Research note, 6 November 2026.

The terminal estimate can retain more of the curvature of its original
phase. The earlier allocation kept half of the outer-variable curvature
of an ordinary pair and discarded its index-variable curvature. The same
pair in fact retains half of each. Applying this to the ordinary and
terminal factors gives three larger scalar costs, with coefficients
\[
             2,\qquad \nu+1,\qquad \frac{3+\epsilon}{2}.
\tag{1}
\]
Here \(\nu=1\) is the factorial alternative of the complete selected
weight, \(\nu=0\) its forced alternative, and \(\epsilon=0,1\) denotes
the terminal type three or four. These are inequalities for the original
phase. They do not replace a signed quantum sum by a positive model.

## 1. The pair inequality

Use the original holomorphic primitive \(g\), whose second derivative on
its prescribed regular strip is
\[
                    g''(z)=\pi\cot(\pi z)-i\pi.
\tag{2}
\]
Put \(V(z,w)=g(z+w)-g(z)-g(w)\). All Hessians below are with respect
to the real parts of the variables, holding their imaginary parts fixed.
For \(z=x+ih\), write \(g_h(x)=\Re g(x+ih)\).

**Lemma 1.** Suppose
\[
 x,y\in[11/50,1/2],\qquad |h|,|k|\le3/25,\qquad x+y<1,
 \quad z=x+ih,\quad w=y+ik .
\tag{3}
\]
Then
\[
 -\Re V''(z,w)\succeq
       \frac12\operatorname{diag}\bigl(g_h''(x),g_k''(y)\bigr).
\tag{4}
\]
The notation \(\succeq\) means that the difference is positive
semidefinite as a real symmetric matrix. A purely imaginary quadratic
with real coefficients, such as the original chirp \(2\pi izw\),
does not alter this inequality. The restriction \(x+y<1\) excludes
the singular corner of the original logarithm.

*Proof.* Set
\[
 a=\Re\cot(\pi z),\quad c=\Re\cot(\pi w),\quad
 C=\Re\cot(\pi(z+w)).
\]
Direct differentiation gives
\[
 -\pi^{-1}\Re V''=\operatorname{diag}(a,c)
                    -C\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\tag{5}
\]
Both \(a,c\) are nonnegative. If \(C\le0\), subtracting half
of the displayed diagonal leaves a sum of positive semidefinite
matrices, proving (4), including an individual endpoint \(x=1/2\).

Suppose \(C>0\). Since \(0<x+y<1\), the formula for the real
part of the cotangent implies \(x+y<1/2\). Thus both \(x,y<.28\).
Put \(p=\cot(\pi x)\) and \(q=\cot(\pi y)\). Then
\[
        0<p,q<5/4,\qquad pq>1,\qquad
        C\le\cot(\pi(x+y))=\frac{pq-1}{p+q}.
\tag{6}
\]
The individual height bounds imply
\[
 a>\frac8{11}p,\qquad c>\frac8{11}q.
\tag{7}
\]
Indeed
\[
 \frac{\Re\cot\pi(x+ih)}{\cot(\pi x)}
  =\frac{1-\cos(2\pi x)}
         {\cosh(2\pi h)-\cos(2\pi x)}>\frac8{11},
\tag{8}
\]
using \(\cos(2\pi x)<1/5\) and \(\cosh(.24\pi)<13/10\).
The ratio decreases as either the cosine or the hyperbolic cosine
increases, and its value at \(1/5,13/10\) is \(8/11\).
The same calculation applies to \(c\).

For positive \(a,c\), the rank-one matrix test says that
\(\frac12\operatorname{diag}(a,c)-C{\bf1}{\bf1}^{T}\)
is positive definite exactly when \(2C(1/a+1/c)<1\).
Here
\[
 2C(1/a+1/c)
 <\frac{11}{4}\frac{pq-1}{pq}
 <\frac{11}{4}\left(1-\frac{16}{25}\right)
 =\frac{99}{100}<1 .
\tag{9}
\]
This proves (4).

All elementary constants used here have rational witnesses.
The bound \(157/50<\pi<22/7\) gives
\(\cos(.44\pi)=\sin(.06\pi)<33/175<1/5\).
For \(u=69/100<.22\pi\), the sine lower and cosine upper
Taylor polynomials give
\[
 5(u-u^3/6)-4(1-u^2/2+u^4/24)
                 =\frac{18132793}{200000000}>0,
\]
and therefore \(\cot(.22\pi)<5/4\).
Finally, for \(v=132/175>.24\pi\), the positive series gives
\[
 \cosh v\le1+\frac{v^2/2}{1-v^2/12},\qquad
 \frac{13}{10}-\left(1+\frac{v^2/2}{1-v^2/12}\right)
                 =\frac{399}{291730}>0 .
\]
This establishes all bounds in (6)--(8). \(\square\)

## 2. Allocation in the original terminal comparison

Keep the original phase, canonical reference, incoming affine marginal,
and complete selected weight from
[the joint main comparison](research_mixed_terminal_joint_main_budget.md).
The preceding ordinary block has type four. In its notation,
\[
 Q_1(s;b,a)=V(s,b)+V(s,a)-g(s)+2\pi ibs,
\tag{10}
\]
and the terminal phase decomposes as
\[
 \Phi_\epsilon(a;t,v)
   =V(t,a)+V(t,v)-g(t)+R_\epsilon(v)+2\pi iat.
\tag{11}
\]
For type three \(v=\xi\), while for type four \(v=e\).
The real defect \(D_\nu\) includes the additional terms
\(-\nu\Re g(a)-(\beta/2)\Re g(b)\), the original affine
subtraction, and the selected constant \(-2\pi\nu H\).
The flag \(\beta\in\{0,1\}\) records the incoming type.

Assume the original endpoint height bounds
\[
\begin{array}{c|c|c}
\epsilon&\Im t_*&\Im v_*\\ \hline
0&[-.072,.021]&[.049,.077]\\
1&[-.108,-.020]&[-.051,-.019]
\end{array}
\tag{12}
\]
and \(|\Im b_*|,|\Im s_*|\le.12\).
The selected height is \(H=.01\). The real targets initially
range over their full original intervals.

The [terminal optimizer localization](research_mixed_terminal_main_optimizer_localization.md),
Proposition 1, restricts every main maximum to \(.22<t_R<.4\).
The [full-input ordinary index barrier](research_mixed_terminal_full_input_index_barrier.md)
restricts the ordinary index to \(.22\le s_R\le.5\) on its
stated incoming domains. These changes improve or preserve the
original objective for every fixed choice of the other real targets.
They apply to both selected-weight alternatives.

Consider the resulting containing product
\[
 b_R,a_R\in P=[.22,.45],\qquad
 s_R\in[.22,.5],\qquad t_R\in[.22,.4],
\tag{13}
\]
with \(\xi_R\in[.1,.4]\) or \(e_R\in[.27,.49]\).
Suppose, as for the original strong reference images, that the
reference real parts belong to these intervals. For the forced
alternative its reference \(a_R\) need only lie in the containing
interval \(P\), even when its targets are restricted to \([.4,.45]\).
Every segment from the lifted reference to a target then remains
in the containing product.

**Proposition 2.** On this product,
\[
 -\Re D_\nu''\succeq\operatorname{diag}
 \left(\frac{1+\beta}{2}g_{h_b}''(b_R),\
       2g_{h_s}''(s_R),\
       (\nu+1)g_H''(a_R),\
       \frac{3+\epsilon}{2}g_{h_t}''(t_R),\ 0\right)
\tag{14}
\]
in the order \((b,s,a,t,v)\).

*Proof.* Apply Lemma 1 to \(V(s,b)\) and \(V(s,a)\).
Their contributions in \(s\), together with \(-g(s)\),
give \(2g_{h_s}''\). They retain half of each outer curvature.
Adding the incoming allocation yields the first entry of (14).

The pair \(V(t,a)\) retains half of the \(t\) and \(a\)
curvatures. Together with the ordinary half and the selected
factorial, this gives \((\nu+1)g_H''\). The term \(-g(t)\)
gives another full \(t\) curvature.

For \(\epsilon=0\), the real negative Hessian of
\(V(t,\xi)+R_0(\xi)\) is positive semidefinite by Lemma 1 of
[the original three-cost proof](research_mixed_terminal_joint_main_curvature_budget.md).
Its proof covers the larger interval \(t_R\in[.18,.5]\)
and all the private and height intervals used here. Discarding
that nonnegative form leaves \(3g_{h_t}''/2\).

For \(\epsilon=1\), apply Lemma 1 also to \(V(t,e)\).
Both real parts are at least \(.22\), both individual heights
are at most \(.12\), and \(t_R+e_R\le.89<1\).
The original cap theorem gives
\(-\Re R_1''=-\Re S''>0\) on the required private interval.
This yields another half of the \(t\) curvature; the remaining
private curvature may be discarded. Thus its total is \(2g_{h_t}''\).
All retained matrices are added before comparison, so simultaneous
motions of the variables are included. \(\square\)

## 3. The stronger three-cost bound

For real \(x_*\), define the scalar remainder
\[
 \phi_h(x;x_*)=g_h(x)-g_h(x_*)-g_h'(x_*)(x-x_*).
\tag{15}
\]
Let \(A=\Re a_*\). Keep the original lifted value
\(T_\nu\) and gradient components \(A_s,A_{a,\nu},A_t\)
from equations (9)--(10) of the joint main comparison.
Its exact gradient is \((0,A_s,A_{a,\nu},A_t,0)\).
Integrating (14) along the segment from that lifted reference gives
\[
\begin{split}
 \sup D_\nu\le T_\nu
 &+\sup_{x\in[.22,.5]}
       \{A_s(x-\Re s_*)-2\phi_{h_s}(x;\Re s_*)\}\\
 &+\sup_{x\in I_\nu}
       \{A_{a,\nu}(x-A)-(\nu+1)\phi_H(x;A)\}\\
 &+\sup_{x\in[.22,.4]}
       \{A_t(x-\Re t_*)-\tfrac{3+\epsilon}{2}
                          \phi_{h_t}(x;\Re t_*)\}.
\end{split}
\tag{16}
\]
Here \(I_1=P\); either \(I_0=P\) or the previously proved
forced restriction \(I_0=[.4,.45]\) can be used at height \(.01\).
The signed supremum is retained when the forced reference lies
outside its target interval. The incoming and private gradient
components vanish, so their nonnegative costs require no added gain.

The exact cubic conjugate \(\mathcal G_K\) defined in
[the cubic-cost note](research_mixed_terminal_cubic_cost_and_response_bounds.md),
equation (9), therefore gives the explicit bound
\[
\begin{split}
 \sup D_\nu\le T_\nu
 &+\mathcal G_{88/5}(A_s;\Re s_*,[.22,.5])\\
 &+\mathcal G_{(\nu+1)49/5}(A_{a,\nu};A,I_\nu)\\
 &+\mathcal G_{(3+\epsilon)22/5}
                       (A_t;\Re t_*,[.22,.4]).
\end{split}
\tag{17}
\]
The coefficients \(44/5\) for the individual \(s,t\) costs
require \(|h_s|,|h_t|\le.108\), in addition to the broader
height range allowed in Lemma 1. These narrower heights hold
for the original strong ordinary and terminal images; they must
be checked when applying (17) to an auxiliary canonical family.
The incoming height needs only the hypotheses of the index barrier
and \(|h_b|\le.12\); no incoming cubic cost is used.

Equation (17) improves the earlier allocation without changing
the trial point, selected height, primitive normalization, Fourier
alternatives, or incoming marginal. Proving its right side negative
on every required reference remains a separate task.

## 4. Consequence for the four completed reference configurations

The saved four-reference guards give
\[
 A_s<.141,\quad .5-\Re s_*>.186,\quad |h_s|<.061,
 \quad -A_t<.255,\quad .5-\Re t_*>.15,\quad |h_t|<.066 .
\]
The force signs are \(A_s>0>A_t\). With the doubled \(s\)
coefficient, its concave cubic has an upper tangent at
\(\delta=23/500\) with slope \(-731/500000\) and intercept
\[
                \frac{2341883}{750000000}<\frac1{320}.
\]
The least terminal coefficient is \(3/2\). Its negative-displacement
cubic has an upper tangent at \(v=93/1000\), with slope
\(-53409/20000000\) and intercept
\[
                \frac{64633977}{5000000000}<\frac{13}{1000}.
\]
Both slopes are negative, so the intercept bounds the tangent on
nonnegative displacements. These bounds use the same monotonicity
in force and reference distance as the earlier cubic proof.

For \(\nu=1\), the saved guards \(A<.314\) and
\(-.255<A_{a,1}<0\), together with \(g_H''>2\) on the
relevant interval to the left of \(A\), bound the selected gain by
\(.255^2/8=2601/320000\). Thus \(T_1<-.0463\) gives
\[
 \sup D_1<
 -\frac{463}{10000}+\frac1{320}+\frac{13}{1000}
                         +\frac{2601}{320000}
 =-\frac{1411}{64000}<-\frac1{50}.
\tag{18}
\]
For the full-\(P\) forced alternative, even discarding its larger
selected cost and keeping the old affine gain \(1071/20000\)
gives, with \(T_0<-109/1000\),
\[
 \sup D_0<
 -\frac{109}{1000}+\frac1{320}+\frac{13}{1000}
                         +\frac{1071}{20000}
 =-\frac{1573}{40000}<-\frac1{50}.
\tag{19}
\]
These are deductions from the existing saved guards, rather than
new reference evaluations. The reusable improvement is (14)--(17).
Neither the four-reference inequalities nor the pair lemma alone
settles the remaining terminal profiles, the whole finite quantum
sum, or the finite-exceptions theorem.
