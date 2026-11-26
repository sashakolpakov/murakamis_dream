# A coupled budget for the second-selection half row

Research deduction, 6 November 2026. This gives static upper budgets
for the two main/right-half-row terms in the
[four-profile reduction](research_mixed_second_selected_four_profile_reduction.md).
The original complex half-row constant, both boundary marginals, and
the reference own-factorial contribution are retained. The signs of
the resulting correlated scalar tests are not proved. No source,
root, parameter cover, or numerical diagnostic is evaluated.

## 1. Exact phase, allocation, and reference

Fix a mixed positive three/four word of length \(m\ge4\), with
first three flags \((\alpha,1,\beta)\), where
\(\alpha,\beta\in\{0,1\}\). Position 1 is unselected and
position 2 is selected at \(H=1/100\). Use
\[
 (a_*,u_*,z_*,v_*,b_*)=(r_1,s_2^*,r_2,s_3^*,r_3),
 \quad z_*=x_*+ic,\quad c<0,\quad z_H^*=x_*+iH,
 \tag{1}
\]
from the [original reference curve](research_mixed_second_selected_reference_curve.md).
All these quantities belong to one actual reference. In particular
\(u_*,v_*\) are ordinary indices, including at length four.
Write \(P=[.22,.45]\), and keep the target heights
\[
 a=a_R+i\Im a_*,\quad u=u_R+i\Im u_*,\quad
 z=z_R+iH,\quad b=b_R+i\Im b_*.
 \tag{2}
\]
Initially \(u_R\in[.125,.5]\) and \((a_R,z_R,b_R)\in P^3\).

The bare phase and its exact half-row separation are
\[
 \begin{split}
 Q_\epsilon(s;a,b)&=g(s+a)+g(s+b)-(2+\epsilon)g(s)
                           -g(a)-g(b)+2\pi ias,\\
 q(w)&=g(w+1/2)-g(w),\\
 Q_\beta(1/2;z,b)&=q(z)+q(b)-(2+\beta)g(1/2)+\pi iz.
 \end{split}
 \tag{3}
\]
The original normalization gives \(g(1/2)=i\pi/8\). Its real
part is zero, but the complex constant in (3) has not been removed
from the phase. In particular the reference term involving
\(\beta g(v_*)\) cannot be removed when comparing (3) with the
original critical action.

Let
\[
 \begin{split}
 F_*={}&Q_1(u_*;a_*,z_*)+Q_\beta(v_*;z_*,b_*)
       -\frac\alpha2g(a_*)-g(z_*)-\frac\beta2g(b_*),\\
 M={}&\Re F_*,\\
 p_L={}&g'(a_*+u_*)-(1+\alpha/2)g'(a_*)+2\pi iu_*,\\
 p_R={}&g'(v_*+b_*)-(1+\beta/2)g'(b_*).
 \end{split}
 \tag{4}
\]
These are precisely \(M_{23},p_L,p_R\) of the original local
product. For \(\nu=1\) (factorial) or \(\nu=0\) (forced), define
\[
 \begin{split}
 \Xi_\nu={}&Q_1(u;a,z)+Q_\beta(1/2;z,b)
             -\frac\alpha2g(a)-\nu g(z)-\frac\beta2g(b),\\
 f_\nu={}&\Re\{\Xi_\nu-p_L(a-a_*)-p_R(b-b_*)\}-2\nu\pi H.
 \end{split}
 \tag{5}
\]
The boundary heights are unchanged, so the affine terms in (5)
are exactly the two terms in \(\Lambda_{23}\). The defect of the
corresponding main/half-row profile is
\[
                 D_{0R,\nu}=\max f_\nu-M.
 \tag{6}
\]
This includes the outgoing halfweight for \(\beta=1\) before
its marginal is subtracted. No Fourier factor is divided out.

## 2. The exact trial constant and four gradients

At the trial \((a_*,u_*,z_H^*,b_*)\), put
\[
 \begin{gathered}
 U=e^{-2\pi iu_*},\quad Z=e^{-2\pi iz_*},\quad
 V=e^{-2\pi iv_*},\quad B=e^{-2\pi ib_*},\qquad
 \lambda=e^{2\pi(H-c)},\\
 A=\log\left|\frac{1-\lambda UZ}{1-UZ}\right|,\qquad
 P_\nu=\log\left|
       \frac{(1-\lambda UZ)(1+\lambda Z)}
                            {(1-\lambda Z)^{2+\nu}}\right|,\\
 D_b=\log\left|\frac{1+B}{1-VB}\right|.
 \end{gathered}
 \tag{7}
\]
All modulus expressions are shorthand for real parts of original
logarithmic differences. They do not specify a new complex lift.
Define the relative trial value by the literal difference
\[
 \begin{split}
 T_\nu={}&\Re\{Q_1(u_*;a_*,z_H^*)-Q_1(u_*;a_*,z_*)\\
 &+Q_\beta(1/2;z_H^*,b_*)-Q_\beta(v_*;z_*,b_*)
                         +g(z_*)-\nu g(z_H^*)\}-2\nu\pi H.
 \end{split}
 \tag{8}
\]
For direct evaluation, the fully canceled expression is
\[
 \begin{split}
 T_\nu=\Re\{&g(u_*+z_H^*)-g(u_*+z_*)
              +g(1/2+z_H^*)-g(v_*+z_*)\\
 &+g(1/2+b_*)-g(v_*+b_*)
                 -(2+\beta)[g(1/2)-g(v_*)]\\
 &+3g(z_*)-(2+\nu)g(z_H^*)
                 +2\pi i[\tfrac12z_H^*-z_*v_*]\}-2\nu\pi H.
 \end{split}
 \tag{9}
\]
In particular the own flag in the second line of (9) still affects
the real comparison, even though the bare half-row constant has
zero real part. The last line retains the original incoming chirp.

**Lemma 1.** In real coordinate order \((a,u,z,b)\), the trial data are
\[
 f_\nu(a_*,u_*,z_H^*,b_*)-M=T_\nu,
 \qquad \nabla f_\nu=(0,A,P_\nu,D_b).
 \tag{10}
\]

The incoming boundary derivative depends only on \(a,u\), so its
original subtraction in (4) still cancels at the trial. The original
index equation \(Q_{1,u}(u_*;a_*,z_*)=0\) leaves exactly the
increment \(A\). The real derivative in \(z\) of the current
phase is
\[
 \Re\{g'(u_*+z_H^*)+g'(1/2+z_H^*)
                       -(2+\nu)g'(z_H^*)+\pi i\}=P_\nu.
 \tag{11}
\]
Finally, the outgoing derivative simplifies to
\[
 \Re\{g'(1/2+b_*)-(1+\beta/2)g'(b_*)-p_R\}
               =\Re\{g'(1/2+b_*)-g'(v_*+b_*)\}=D_b.
 \tag{12}
\]
The cancellation in (12) requires the correct outgoing halfweight.
Equations (8)--(9) prove the value assertion.

The original correlated reference gives \(A>0\), by the increment
inequality in Section 2 of the
[central main/main budget](research_mixed_second_selected_central_budget.md).
Neither \(P_\nu\) nor \(D_b\) is assigned a sign. In particular
the main/main gradient in the selected coordinate cannot be reused
after the right index has been replaced by its real half row.

## 3. The left index restriction and joint scalar costs

The maximum in (6) is unchanged on
\[
             K_R=P\times[.22,.5]\times P\times P.
 \tag{13}
\]
Indeed its \(u\)-derivative is exactly the same original
\(Q_{1,u}\) as in Proposition 2 of the
[second-selection index-barrier proof](research_mixed_second_selected_horizontal_concavity.md).
The right half row, both affine subtractions, and both Fourier
alternatives are independent of \(u\). That proof's positive face
gradient at \(.22\), and its monotonicity down to \(.125\),
therefore exclude every smaller index here too. The actual trial
index lies strictly inside (13).

Let \(g_h(t)=\Re g(t+ih)\), and use final height \(H\) for
the selected coordinate. Introduce three scalar potentials
\[
 \begin{split}
 P_u(t)&=g_{h_u}(t),\\
 P_{z,\nu}(t)&=-\Re q(t+iH)+(\nu+1/2)g_H(t),\\
 P_{b,\beta}(t)&=-\Re q(t+ih_b)+(\beta/2)g_{h_b}(t).
 \end{split}
 \tag{14}
\]
The first is convex on \([.22,.5]\); the other two are strictly
convex on \(P\). The latter assertion follows from
\[
                q''(w)=-\frac{2\pi}{\sin(2\pi w)},
 \qquad \Re\frac1{\sin(2\pi(t+ih))}>0\quad(0<t<1/2),
 \tag{15}
\]
and the nonnegative real cotangent there.

The type-four pair estimate, Section 2 of the
[left-cut/main-contour majorant](research_mixed_selected_four_four_left_main_majorant.md),
applies to both \(V(u,a)\) and \(V(u,z)\) on (13): the index
and outer absolute heights are at most \(.102\). It gives
\[
 -\pi^{-1}\Re V(s,w)''\succeq
                  \operatorname{diag}(0,\tfrac12\Re\cot\pi w).
 \tag{16}
\]
Combining these two matrices with the remaining exact terms in (5),
one obtains the joint diagonal lower bound
\[
 -\nabla^2 f_\nu\succeq
 \operatorname{diag}\left(
     \frac{1+\alpha}{2}g_{h_a}'',\ P_u'',\ P_{z,\nu}'',\ P_{b,\beta}''
                       \right)
 \quad\hbox{on }K_R.
 \tag{17}
\]
This is a matrix inequality with arbitrary simultaneous real motions;
it does not fix the incoming coordinate at its reference value.

For any potential \(P_j\) in (14), centered at the corresponding
actual real coordinate \(t_j^*\) but at the potential's final height,
write
\[
 \phi_j(d)=P_j(t_j^*+d)-P_j(t_j^*)-P_j'(t_j^*)d,
 \qquad
 \phi_j^*(p)=\max_{t_j^*+d\in I_j}\{pd-\phi_j(d)\},
 \tag{18}
\]
with \(I_u=[.22,.5]\) and \(I_z=I_b=P\).
All three costs are nonnegative, with their centers in their intervals.
Integrate (17) along the full segment from the trial to a target.
The incoming boundary gradient is zero and its remaining convex
cost is nonnegative. Dropping that favorable cost gives the bound
\[
 \boxed{\quad D_{0R,\nu}\le
 T_\nu+\phi_u^*(A)+\phi_{z,\nu}^*(P_\nu)+\phi_{b,\beta}^*(D_b).
 \quad}
 \tag{19}
\]
Thus three one-variable conjugates suffice, while all reference data
and the half-row trial action remain coupled. Equality in (19) is not
claimed; the pair estimate is an upper-majorant construction.

## 4. Explicit clipping and a simpler quadratic budget

The first conjugate has the elementary clipped formula. Put
\[
 r_u=|U|,\qquad
 c_u=\frac{1+r_u^2-|1-U|^2e^{2A}}{2r_u},\qquad
 \widehat u=\operatorname{clip}(T(c_u),.22,.5),
 \tag{20}
\]
where \(T(c)\) is the continuous clipped value of
\(\arccos(c)/(2\pi)\), equal to \(.5\) for \(c\le-1\)
and zero for \(c\ge1\). Then
\[
                  \phi_u^*(A)=A(\widehat u-u_{*,R})
                               -\phi_u(\widehat u-u_{*,R}).
 \tag{21}
\]
This follows by differentiating the centered convex potential.
It includes a possible upper-endpoint maximizer; no lower-coordinate
curvature at \(u=.5\) is required. Since \(A>0\), its maximizing
displacement is nonnegative.

Both remaining conjugates are also uniquely determined by a monotone
scalar equation and endpoint clipping. Their potentials have the form
\[
 P_{m,h}(t)=m g_h(t)-\Re g(t+1/2+ih),\qquad
 m=3/2+\nu\ \hbox{or}\ 1+\beta/2.
 \tag{22}
\]
With \(X_t=e^{-2\pi i(t+ih)}\), their derivative is
\(m\log|1-X_t|-\log|1+X_t|\).
For a force \(p\), the critical equation of the conjugate is
\[
 \frac{|1-X_t|^{2m}}{|1+X_t|^2}
       =e^{2p}\frac{|1-X_{t_*}|^{2m}}{|1+X_{t_*}|^2}.
 \tag{23}
\]
The left side increases strictly on \(P\). If its target is
outside the endpoint range, select the corresponding endpoint;
otherwise the unique solution gives the maximizing target.
This is a scalar conjugate evaluation, not a source critical-root
problem. The actual center is never clipped or replaced.

A fully quadratic alternative is available for these two terms:
\[
 P_{z,\nu}''>\mu_\nu,\qquad P_{b,\beta}''>\gamma_\beta,
 \quad
 \mu_0=32/5,\quad\mu_1=69/10,\quad
 \gamma_0=57/10,\quad\gamma_1=41/10.
 \tag{24}
\]
Here is an explicit verification. At height \(H=.01\),
the half-row estimates give
\(\Re\csc(2\pi z)>100/101\) and
\(\Re\cot\pi z>3/20\), hence
\[
 P_{z,\nu}''>
 \pi\left\{\frac{200}{101}+(\nu+1/2)\frac3{20}\right\}.
 \tag{25}
\]
Using \(\pi>157/50\), the differences from \(\mu_0,\mu_1\)
are respectively greater than
\(10771/202000\) and \(4913/202000\).

For \(\beta=0\), put \(a=\sin(2\pi t)>3/10\) and
\(C=\cosh(2\pi h_b)<11/10\). Then
\[
 \Re\csc(2\pi(t+ih_b))=\frac{Ca}{a^2+C^2-1}>\frac{10}{11}.
 \tag{26}
\]
The expression decreases with \(C\); at \(C=11/10\),
its only interior extremum as a function of \(a\) is a maximum.
The endpoint values at \(a=3/10,1\) are \(11/10,10/11\).
Thus \(P_{b,0}''>20\pi/11>57/10\), with rational reserve
\(1/110\) after using \(\pi>157/50\).
For \(\beta=1\), this is exactly Lemma 1 of the
[next-four half-row proof](research_mixed_selected_four_four_half_row_majorant.md),
which retains the outgoing halfweight and proves \(P_{b,1}''>41/10\)
on the present ordinary type-four height range.
The same proof and the
[next-three half-row proof](research_mixed_selected_four_three_half_row_majorant.md)
supply the elementary bounds used in (25)--(26).

For \(l\le0\le r\), let
\[
 \Gamma_\eta(p;l,r)=p\tau-\frac\eta2\tau^2,
 \qquad \tau=\operatorname{clip}(p/\eta,l,r).
 \tag{27}
\]
Equations (19) and (24) give the simpler sufficient budget
\[
 \boxed{\quad D_{0R,\nu}\le T_\nu+\phi_u^*(A)
 +\Gamma_{\mu_\nu}(P_\nu;.22-x_*,.45-x_*)
 +\Gamma_{\gamma_\beta}(D_b;.22-b_{*,R},.45-b_{*,R}).\quad}
 \tag{28}
\]
One may independently use the exact conjugate or its quadratic upper
bound for each of the last two terms.

## 5. Scope of the resulting tests

A uniform negative bound for both right sides of (19), or of (28),
would control the two main/right-half-row terms of the four-profile
reduction. The main/main terms are the separate central-budget problem.
Every quantity in these tests must be evaluated from the same original
endpoint parameter and two transfers, with the original branch and
necessary suffix conditions retained. In particular \(A,P_\nu,D_b\),
the trial value \(T_\nu\), and all centers are not independent intervals
to be optimized separately.

No pointwise assertion that a fixed ordinary main trial dominates the
right half row is used. The trial in (8) is measured against the
original coupled action, and its exact change need not have a prescribed
sign before the correlated estimate is proved. The signs of (19) and
(28), and the whole finite-source second-selection comparison, remain
open. Both complete Fourier alternatives and both original boundary
tangents remain explicit throughout.
