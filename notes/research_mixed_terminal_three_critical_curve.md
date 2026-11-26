# The original critical curve of the terminal type-three Newton sum

Research deduction, 5 November 2026. The exact terminal Newton reduction
has a rational critical curve. Its selected branch is the original
geometric endpoint branch, with the same logarithmic lifts and absolute
action. The parametrization alone neither selects a finite integration
cycle nor controls its complement.

## 1. Original reduced equations and the existing cap relation

Use the exact whole-polynomial identity and phase of
[the terminal Newton reduction](research_mixed_terminal_three_newton_reduction.md).
At complete color put
\[
\begin{split}
\mathcal T(a;t,u)={}&-2J(1/2-u)-2J(u)
 +g(t+a)+g(t+u)-3g(t)\\
 &-2g(u)-g(a)+i\pi u+2\pi iat,\qquad
 g(v)=J(v)+i\pi(v-v^2)/2 .
\end{split}
\tag{1}
\]
The ordinary color is fixed at \(-2\); the variable \(w\) below is
an exponential coordinate, not that color. Set
\[
 z=e^{-2\pi it},\qquad w=e^{-2\pi iu},\qquad
 A=e^{-2\pi ia}.
\tag{2}
\]
The original zero-lift equations are
\[
\begin{split}
\mathcal T_t&=g'(a+t)+g'(u+t)-3g'(t)+2\pi ia=0,\\
\mathcal T_u&=2\Log(2\cos\pi u)+g'(u+t)
                   -4\Log(2\sin\pi u)+2\pi iu=0.
\end{split}
\tag{3}
\]
All logarithms are continued on the original regular sine strips.
In particular \(g'(v)=\Log(1-e^{-2\pi iv})\) there, with that
specified lift.

Exponentiating (3), without discarding any nonzero factor, gives
\[
 (1-Az)(1-wz)=A(1-z)^3,\qquad
 (1+w)^2(1-wz)=(1-w)^4 .
\tag{4}
\]
For the second identity,
\((2\cos\pi u)^2/(2\sin\pi u)^4
 =w(1+w)^2/(1-w)^4\), and \(e^{2\pi iu}=w^{-1}\).
The lift \(+i\pi u\) in (1) is essential to the derivative in (3).

On the regular branch, \(w\ne0,-1\), and the second equation yields
\[
 z=z(w)=\frac{6-5w+4w^2-w^3}{(1+w)^2}.
\tag{5}
\]
This is already the type-three cubic in
[the first-cap critical theorem, equation (4)](research_mixed_first_cap_critical.md),
with its exponential variable \(U=1/w\). The new terminal equation
specifies the external coordinate:
\[
\begin{split}
A=A(w)
 &=\frac{1-wz(w)}
         {z(w)(1-wz(w))+(1-z(w))^3}\\
 &=-\frac{(w-1)(w+1)^4}
 {(3w^2-6w+7)(w^3-7w^2+7w-17)} .
\end{split}
\tag{6}
\]
Thus a selected value of \(w\) satisfies the degree-five equation
\[
 A(3w^2-6w+7)(w^3-7w^2+7w-17)
                         +(w-1)(w+1)^4=0.
\tag{7}
\]
The private endpoint exponent is
\[
 v=e^{-2\pi ie}
   =\frac{w-1}{1-z(w)}
   =\frac{(1+w)^2}{w^2-2w+5}.
\tag{8}
\]
Useful exact factor identities are
\[
\begin{split}
1-z(w)&=\frac{(w-1)(w^2-2w+5)}{(1+w)^2},\\
1-wz(w)&=\frac{(w-1)^4}{(1+w)^2},\\
1-vz(w)&=\frac{(w-1)^3}{w^2-2w+5},\qquad
1-v/w=\frac{(w-1)^3}{w(w^2-2w+5)} .
\end{split}
\tag{9}
\]
They also verify (6) by substitution. Zeros of denominators or original
factorial arguments are excluded before using this parametrization.
Clearing denominators does not authorize an exceptional point or choose
one of the roots of (7).

## 2. An off-shell elimination with its absolute normalization

Write the original terminal endpoint action, at fixed external \(a\),
as
\[
\begin{split}
\mathcal F(a;e,t,u)={}&-2J(1/2-u)-3J(u)-J(e-u)
 +J(e+t)+J(a+t)\\
 &-2J(t)-J(a)+i\pi\{e(u-t)+at\}.
\end{split}
\tag{10}
\]
Its three derivatives are precisely the own-type-three endpoint
equations in
[open-word localization, equation (6)](research_mixed_open_word_critical_localization.md).
This includes the ordinary endpoint variable \(u\), not a fixed
boundary insertion.

Consider the open rectangular product
\[
\begin{split}
\mathcal W_t&=(.278,.391)+i(-.072,.021),\\
\mathcal W_u&=(.218,.242)+i(.049,.077).
\end{split}
\tag{11}
\]
The [exact endpoint-image extraction](research_mixed_open_word_endpoint_rectangles.md)
places every actual type-three endpoint pair \((t,u)\) strictly in
(11), on both original external input disks.

For \((t,u)\) in (11), define \(e=e(t,u)\) by
\[
 e^{-2\pi ie}=\frac{e^{-2\pi iu}-1}{1-e^{-2\pi it}},
                   \qquad 0<\Re e<1/2.
\tag{12}
\]
This branch exists holomorphically throughout (11). Here is a direct
argument that also fixes its action constant. For \(0<\lambda\le1\),
replace \(u\) by \(\lambda u\), and set
\(\theta_\lambda=\arg\sin(\pi\lambda u)\),
\(\theta_t=\arg\sin(\pi t)\). The elementary bounds are
\[
 0<\theta_\lambda<.36,\qquad -.23<\theta_t<.07.
\tag{13}
\]
Indeed \(\cot x<1/x\), \(\tanh y<y\) give
\(\theta_\lambda<\Im u/\Re u<.077/.218<.36\).
For \(t\), its real part exceeds \(1/4\), so
\(|\arg\sin(\pi t)|<\pi|\Im t|\); use \(\pi<22/7\)
separately on its two height signs.
The continuously chosen branch in (12) has
\[
 \Re e_\lambda=\frac12-\frac{\Re t}{2}
  +\frac{\lambda\Re u}{2}
  -\frac{\theta_\lambda-\theta_t}{2\pi}.
\tag{14}
\]
Since \((.36+.23)/(2\pi)<.1\) and \(.07/(2\pi)<.012\),
the whole radial path satisfies
\[
 0<\Re e_\lambda<1/2,\qquad
 0<\Re(e_\lambda-\lambda u)<1/2,\qquad
 1/2<\Re(e_\lambda+t)<1 .
\tag{15}
\]
For example the respective restrictive bounds are
\(.5-.278/2+.242/2+.012<.5\),
\(.5-.391/2-.242/2-.1>0\), and
\(.5+.278/2-.1>.5\).
Thus the quotient in (12) has its argument strictly between
\(-\pi\) and zero, and determines a single holomorphic \(e\).

The private equation is
\[
 \mathcal F_e=g'(e+t)-g'(e-u)+2\pi iu=0.
\tag{16}
\]
Equation (12) makes its exponential equal to one.
As \(\lambda\downarrow0\), \(\Im e_\lambda\to-\infty\)
and the residual in (16) tends to zero. Its continuous integral
lift is therefore zero throughout the path.

**Elimination identity.** On (11), for every external \(a\) for
which the displayed original arguments are regular,
\[
                   \mathcal T(a;t,u)
                    =\mathcal F(a;e(t,u),t,u).
\tag{17}
\]
To verify the constant as well as the derivatives, subtract the two
cap parts, as in the original physical cap calibration. Their difference
is
\[
 g(u+t)-g(e+t)+g(e-u)-g(u)-g(t)
                      +i\pi u+i\pi u^2-2\pi ieu.
\tag{18}
\]
Its \(u\)-derivative vanishes under (16), with the original
logarithms. One may check the lift directly: the remaining derivative
has exponential one by (12), and tends to zero along
\(\lambda u\to0\). Expression (18) itself tends to zero:
\(g(e_\lambda+t)\) and \(g(e_\lambda-\lambda u)\) have
the same limit \(i\pi/12\), \(u e_\lambda\to0\), and
\(g(\lambda u+t)-g(t)\to0\).
Consequently (18) vanishes on the radial path. Adding the same
adjacent Gram-pair action to both cap parts gives (17).
No finite-source asymptotic is continued by this identity.

## 3. The selected geometric branch and its nondegeneracy

For each external input \(a\) in either of the original typed disks,
the completed endpoint localization gives its original zero
\((e_*(a),t_*(a),u_*(a))\). Equation (16) and the sine chamber
identify \(e_*=e(t_*,u_*)\). Identity (17) therefore gives
\[
 \mathcal T_t(a;t_*,u_*)=\mathcal T_u(a;t_*,u_*)=0,\qquad
 \mathcal T(a;t_*,u_*)=\mathcal P_0(a),
\tag{19}
\]
where \(\mathcal P_0\) is the original optimized terminal action.
The equality includes its complex additive constant. By the completed
[geometric/source identification](research_mixed_geometric_source_identification.md),
this is the actual geometric branch at every original open-word
reference. Its external derivative is likewise unchanged:
\[
 \mathcal P_0'(a)
       =g'(a+t_*)-g'(a)+2\pi it_* .
\tag{20}
\]

There is also uniqueness in the small reduced product (11).
For \(a\in Q=[.23,.45]+i[-.12,.12]\) and horizontal real
differentials in \((e,t,u)\), the negative real Hessian of (10) is
\[
\begin{split}
-\Re d^2\mathcal F={}&
\pi\Re(2\tan\pi u+3\cot\pi u)\,du^2
+\pi\Re\cot\pi(e-u)\,(de-du)^2\\
&-\pi\Re\cot\pi(e+t)\,(de+dt)^2
+\{2\pi\Re\cot\pi t-\pi\Re\cot\pi(a+t)\}\,dt^2 .
\end{split}
\tag{21}
\]
Every coefficient is positive on the eliminated chart by (11),(15)
and \(.508<\Re(a+t)<.841\). In particular
\(\mathcal F_{ee}\ne0\), and the complex Schur complement gives
\[
 -\Re\mathcal T''_{(t,u)}>0,\qquad
 \det\mathcal F''_{(e,t,u)}
             =\mathcal F_{ee}\det\mathcal T''_{(t,u)}\ne0.
\tag{22}
\]
The usual Hermitian quadratic-form proof of Schur accretivity applies;
the eliminated first component of \(\mathcal F''v\) is zero.
Integrating the accretive Hessian along a segment in the convex product
(11) proves injectivity of the reduced gradient there. Thus the root
in (19) is its unique zero in that product. This is not uniqueness
among every algebraic solution of (7).

The curve has no projection ramification at the selected references.
Indeed
\[
 \mathcal T_{tu}=g''(t+u)\ne0,\qquad
 \mathcal T_{ta}=g''(t+a)+2\pi i
                         =\frac{2\pi i}{1-Az}\ne0.
\tag{23}
\]
Implicit differentiation gives
\(u_*'(a)=\mathcal T_{tu}\mathcal T_{ta}/
\det\mathcal T''_{(t,u)}\ne0\).
Hence \(w\) is a local parameter and \(A'(w)\ne0\) on this
branch. In particular the selected root of (7) is simple.
The exact rational equation is useful for algebraic elimination;
the original chamber and zero logarithmic lifts select its meaning.

## 4. What this supplies to a contour argument

The critical point lies strictly in the lower Newton strip, with
\(.218<\Re u_*<.242\), \(.049<\Im u_*<.077\), and the
attached range (11). It is therefore separated from the real support
walls \(t=0\), \(u=0\), \(u=1/2\), and \(t+u=1\).
The action, its external marginal and the eliminated Gaussian
determinant agree with the original geometric endpoint.

These facts supply the selected local saddle and an exact branch
dictionary for the two-variable finite triangle. They do not prove
that the remaining complete triangle deforms to that saddle with
a nonzero coefficient, or bound its real cuts, mixed vertical
currents and aliases. An algebraic solution of (4) outside the
selected chart can carry nonzero integral logarithmic residuals;
those integers cannot be removed by resetting principal logarithms.
The exact finite Newton sum, including its original support and
ordinary-color data, must still be retained in a global contour proof.
