# Height monotonicity of the original terminal factorial main phase

Research deduction, 6 November 2026. The factorial joint main phase
decreases pointwise with the selected height on its full original
real target product. This retains the shared chirp and the complete
selected weight. It is a new joint-phase statement, distinct from
the earlier terminal halfweight transport against a horizontal plane.
No reference, primitive or finite source is evaluated.

## 1. Fixed reference and full original targets

Use \(Q_1,\Phi_\epsilon,M_*,p_*\) from
[the joint-main theorem](research_mixed_terminal_joint_main_budget.md).
Fix an original coupled reference and all target heights except
\(a=x+iH\), where \(0\le H\le7/500\). Its factorial defect is
\[
 D_1(H)=\Re\{Q_1(s;b,a)+\Phi_\epsilon(a;t,v)
                 -g(a)-\tfrac\beta2g(b)-M_*-p_*(b-b_*)\}
                    -2\pi H .
 \tag{1}
\]
Here \(\beta,\epsilon\in\{0,1\}\). The original main real product is
\[
 b_R,a_R\in P=[.22,.45],\quad s_R\in[.125,.5],\quad
 t_R\in[.15,.5],\quad
 v_R\in[.1,.4]\ (\epsilon=0),\quad
 v_R\in[.27,.49]\ (\epsilon=1).
 \tag{2}
\]
Assume the original source branches and regularity conditions on this
product. The height bounds needed for the following derivative estimate
are only \(h_s=\Im s\le-.001\) and \(h_t=\Im t\le.021\).
In particular it does not require the restricted incoming height
\(h_b\le.021\), or a lower-index barrier for \(s\). The full original
type-four ordinary and type-three/type-four terminal reference images
have these upper height bounds.

Write
\[
 A(y,k)=\arg(1-e^{2\pi k-2\pi iy}),\qquad 0<y<1 .
 \tag{3}
\]
This is the imaginary part of the prescribed logarithm \(g'(y+ik)\),
computed as the principal argument of \(1-e^{2\pi k-2\pi iy}\).
Every summed real argument below is strictly between zero and one.
Differentiating (1), including its shared chirp, gives exactly
\[
 \partial_HD_1
  =-A(s_R+x,h_s+H)-A(t_R+x,h_t+H)
                         +3A(x,H)-2\pi t_R-2\pi .
 \tag{4}
\]
The incoming coordinate and private coordinate do not occur in (4).

## 2. Elementary argument bounds

Every real or imaginary component in this section refers to the
complex number \(1-r e^{-2\pi iy}\) inside a logarithm, not to the
value of the logarithm.

Put \(r_s=e^{2\pi(h_s+H)}\), \(r_t=e^{2\pi(h_t+H)}\),
and \(r_a=e^{2\pi H}\). Uniformly on the height interval,
\[
                 r_s<11/10,\qquad r_t<5/4,\qquad 1\le r_a<11/10.
 \tag{5}
\]
Indeed the first and third exponents are at most \(.028\pi<11/125\),
and \(e^{11/125}<125/114<11/10\).
For the second exponent use \(.07\pi<11/50\) and
\[
 e^{11/50}
 \le 1+\frac{11}{50}
       +\frac{(11/50)^2}{2(1-11/150)}
 =\frac{17321}{13900}<\frac54 ,
 \qquad \frac54-\frac{17321}{13900}=\frac{27}{6950}.
 \tag{6}
\]
The exponential majorant follows directly from the positive series.

First suppose \(x\le.4\). The summed real arguments lie respectively
in \([.345,.9]\) and \([.37,.9]\). Their doubled-angle cosines
are at most \(\cos(\pi/5)<13/16\). Hence the complex number
inside the first logarithm has strictly positive real part and
\[
 A(s_R+x,h_s+H)>-\pi/2.
 \tag{7}
\]
The real part of the complex number inside the second logarithm
is greater than \(-1/64\).
If it is negative, its summed real argument exceeds \(.75\), its
radius exceeds one, and the absolute imaginary component is greater
than \(\sin(\pi/5)>29/50\). Thus, also when its real component is
nonnegative,
\[
 A(t_R+x,h_t+H)>-\pi/2-\frac{25}{928}>-\pi/2-\frac3{100}.
 \tag{8}
\]
For the number \(1-r_a e^{-2\pi ix}\) inside the own logarithm,
\(\cos(2\pi x)<1/5\), so its real part exceeds \(39/50\),
and its imaginary part is positive and less
than \(11/10\). Since \(55/39<3/2<\sqrt3\),
\(A(x,H)<\pi/3\). Substitution in (4) gives
\[
               \partial_HD_1<\frac3{100}-2\pi t_R
                         \qquad(x\le.4).
 \tag{9}
\]

Now suppose \(x\ge.4\). The summed real arguments lie in
\([.525,.95]\) and \([.55,.95]\). If the complex number inside
a corresponding logarithm has negative real part, its summed real argument is greater
than \(.75\) and the absolute imaginary component exceeds
\(\sin(\pi/10)>3/10\). Its negative real component has magnitude
less than \(r-1\). From (5) and \(\arctan q\le q\),
\[
 A(s_R+x,h_s+H)>-\pi/2-\frac13,\qquad
 A(t_R+x,h_t+H)>-\pi/2-\frac56 .
 \tag{10}
\]
These inequalities remain true when that complex number has
nonnegative real part. For the number \(1-r_a e^{-2\pi ix}\)
inside the own logarithm, \(\cos(2\pi x)<-4/5\) and
\(\sin(2\pi x)<3/5\). Its real part exceeds \(9/5\)
and its imaginary part is less than \(33/50\). Therefore
\(A(x,H)<11/30\), and
\[
        \partial_HD_1<\frac{34}{15}-(1+2t_R)\pi
                                      \qquad(x\ge.4).
 \tag{11}
\]
All trigonometric estimates above follow from
\(11/5<\sqrt5<9/4\), the exact fifth- and tenth-root values, and
\(\sin(.06\pi)<.06\pi<1/5\).

## 3. Pointwise decrease and maximized main rates

**Proposition 1.** On the full original product (2),
\[
                         \partial_HD_1<-9/10.
 \tag{12}
\]
On its subset \(t_R\ge.18\), the stronger bound is
\[
                         \partial_HD_1<-11/10.
 \tag{13}
\]
For (12), equations (9) and (11) give respectively
\(.03-.30\pi<-9/10\) and \(34/15-(13/10)\pi<-9/5\).
For (13), they give \(.03-.36\pi<-11/10\) and
\(34/15-(34/25)\pi<-2\). These rational comparisons use only
\(\pi>157/50\).

The pointwise terminal-index barriers in
[type-three completion](research_mixed_terminal_three_selected_height_completion.md),
equation (15), and
[type-four completion](research_mixed_terminal_four_selected_height_completion.md),
equations (7)--(8), hold uniformly for \(a\in P+i[0,.014]\).
For the original endpoint height images and full private intervals
there, they permit every main maximum to be restricted to \(t_R\ge.18\).
Neither the ordinary factor nor the selected weight depends on \(t\).
No incoming-height restriction is added by this step.

Consequently, if \(G_1(H)\) is the maximum of (1) over its original
real product, then for \(0\le H_0<H_1\le.014\),
\[
 G_1(H_1)\le G_1(H_0)-\frac{11}{10}(H_1-H_0).
 \tag{14}
\]
In particular the four factorial gaps in
[the curvature completion](research_mixed_terminal_joint_main_curvature_completion.md)
propagate from \(H=.01\) to every \(H\in[.01,.014]\), gaining
at least \(11(H-.01)/10\). Their reference actions and original
incoming complex tangents are unchanged.

This does not transport the completed two-branch main-current theorem
to a higher contour. The forced alternative must be compared at that
same height; the complete selected weight is one additive two-rate
bound there. A forced estimate at \(H=.01\) cannot be combined with a
factorial estimate at \(H=.014\). Its forced target interval is
\([.4,.45]\) through height .01, whereas the available general
[branch-domain theorem](research_mixed_selected_weight_branch_domains.md)
only gives \([.36,.45]\) through height .014. No sign for that larger
forced domain, other terminal profile, or complete terminal source is
asserted here.
