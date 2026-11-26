# The nearest symbol roots at the half-frequency endpoint

Private algebraic and phase deduction, 9 November 2026. The nearest
zeros governing the zero-free Fourier weights are not, near frequency
one half, the zeros obtained from the selected inner-three action.
An exact factorization of the endpoint cubic identifies a closer
unselected pair and determines the leading root-distance asymptotic.

No mathematical numerical evaluation, saved-value arithmetic, or
frozen-source edit is used. The original finite source is retained.
This result obstructs an identification of two algebraic branches;
it does not disprove adequacy of the complete zero-free weight class.

## 1. Original symbol and an exact local form

Use the original symbol \(p(u,t)\), Laurent polynomial and
root distance \(r(t)\) of
[the zero-free inverse theorem](research_mixed_next_outer_zero_free_symbol_weights.md).
The frequency variable is \(t\); the complex angular variable is \(u\).
Write
\[
 c_o=\cos(u/2),\quad s_o=\sin(u/2),\quad
 A=3u/2+\pi t,\quad k=\cot(u/2)\cos A,\quad h=-\sin A.
                                                               \tag{1}
\]
The exact odd-inner square identity gives
\[
 w_3=4k^3-4k^2h+3k-h,\qquad
 p(u,t)=256\{s_o^6+F(u,t)^2\},                            \tag{2}
\]
where the pole-free expression is
\[
 F=4c_o^4\cos^3A
   +4c_o^3s_o\cos^2A\sin A
   +3c_o^2s_o^2\cos A+c_os_o^3\sin A.                    \tag{3}
\]
Indeed \(F=s_o^3c_ow_3\) away from \(s_o=0\), and
\(p=(4s_o^2)^3\,4(1+c_o^2w_3^2)\). Analytic continuation
proves (2) at the removed points as well. This is the original
symbol with character \(-e^{3iu+2\pi it}\), not a changed phase.

Set
\[
                       \delta=\tfrac12-t.
\]
At \(u=\delta a\), the function \(F\) is odd in \(\delta\)
and vanishes to order at least three. Hence
\[
 \mathcal H(a,\delta)=\delta^{-6}p(\delta a,\tfrac12-\delta)
\]
extends holomorphically to \(\delta=0\), locally uniformly for
bounded \(a\), and is even in \(\delta\). Direct expansion of
the sine and cosine at zero gives
\[
 \mathcal H(a,0)
 =4a^6\left[1+\mathcal W(2\pi/a-3)^2\right],\qquad
 \mathcal W(k)=4k^3+4k^2+3k+1.                            \tag{4}
\]
The apparent pole at \(a=0\) is removed. Explicitly,
\[
 \mathcal H(a,0)
 =4\left[a^6+
 (32\pi^3-128\pi^2a+174\pi a^2-80a^3)^2\right].           \tag{5}
\]
Its constant term is \(4096\pi^6\), and its leading
coefficient is \(25604\).

## 2. All six endpoint roots and the nearest pair

Put
\[
 \mathscr P_3(c)=4c^3-3c-i(4c^2-1).
\]
Then
\[
                     \mathcal W(ic)=-i\mathscr P_3(c).    \tag{6}
\]
The zeros in (4) therefore have the form
\[
 a=\frac{2\pi}{3+ic},\qquad \mathscr P_3(c)=1,
                                                               \tag{7}
\]
together with their complex conjugates. The denominator in (7)
cannot vanish, since \(\mathcal W(-3)=-80\ne\pm i\).
The exact factorization is
\[
 \mathscr P_3(c)-1
 =(c+\tfrac12)\{4c^2-(2+4i)c-2+2i\}.                     \tag{8}
\]
Thus the three roots in (7) are
\[
 c_0=-\tfrac12,\qquad
 c_\pm=\frac{1+2i\pm\sqrt{5-4i}}4,                        \tag{9}
\]
where the square root has positive real part. They are simple:
the quadratic discriminant is nonzero, and its value at
\(c=-1/2\) is \(4i\ne0\). The roots with
\(\mathscr P_3(c)=-1\) are \(-\overline{c_0}\) and
\(-\overline{c_\pm}\), which yield the conjugates in (7).
The two triples do not intersect. Hence (5) has six distinct,
nonzero roots.

Write \(\sqrt{5-4i}=x-iy\), \(x,y>0\). Then
\[
 xy=2,\qquad x^2-y^2=5,\qquad
                         \frac73<x<\frac52,\quad
                         \frac45<y<\frac67.              \tag{10}
\]
For example \(x^2=(5+\sqrt{41})/2\); the strict inequalities
\(6<\sqrt{41}<7\), together with \(11/2>49/9\) and
\(6<25/4\), prove the bounds for \(x\). The bounds for \(y\)
follow from \(y=2/x\). These are exact written inequalities.

For \(c=a+ib\),
\[
 \left|\Im\frac{2\pi}{3+ic}\right|
                 =\frac{2\pi|a|}{(3-b)^2+a^2}.           \tag{11}
\]
At \(c_0=-1/2\), this is \(4\pi/37\). For \(c_+\), (10)
gives \(a>5/6\), \(a<1\), and \(0<b<1\), so the ratio
in (11), divided by \(2\pi\), is greater than \(1/12\),
which exceeds \(2/37\). For \(c_-\), write \(a=-a_-\).
Then
\[
 \frac13<a_-<\frac38,\qquad \frac7{10}<b<\frac57.
\]
Its denominator in (11) is less than
\[
 (23/10)^2+(3/8)^2=\frac{8689}{1600}<6.
\]
Its ratio divided by \(2\pi\) is therefore greater than
\(1/18>2/37\). Thus the unique closest conjugate pair among
the six slopes comes from \(c_0\), with
\[
                 a_0=\frac{24\pi+4\pi i}{37}
                      \quad\hbox{and}\quad\overline{a_0}.         \tag{12}
\]

The implicit function theorem applied to the simple roots of
(5) gives six holomorphic branches \(a_j(\delta)\).
Evenness of \(\mathcal H\) and uniqueness give
\(a_j(\delta)=a_j(0)+O(\delta^2)\). Thus their angular zeros are
\[
                       u_j(\delta)=\delta a_j(0)+O(\delta^3).
                                                               \tag{13}
\]
Conjugate roots stay conjugate for real \(\delta\), because
\(p(u,t)\) is real for real \(u,t\).

There are no other roots approaching the unit circle. Indeed at
\(t=1/2\), for real \(u\notin2\pi\mathbb Z\), the original
all-character theorem gives \(p(u,1/2)>0\). At zero, (2) gives
\[
                         p(u,1/2)=25604\,u^6+O(u^8).      \tag{14}
\]
The Laurent polynomial has nonzero extreme coefficients and
degree 22 after clearing \(z^{-11}\), \(z=e^{iu}\). Thus
\(z=1\) has multiplicity exactly six, and all other sixteen
roots have a fixed positive distance in log modulus from the
unit circle. Continuity of the full polynomial root multiset,
together with the six branches (13), preserves that separation
for small \(\delta\). The strict slope comparisons above then
identify the nearest pair.

Consequently there is \(\delta_0>0\) such that the nearest
roots for \(0<\delta<\delta_0\) are precisely the pair in
(12)--(13), and
\[
 \boxed{\qquad
 r(\tfrac12-\delta)=\frac{4\pi}{37}\delta+O(\delta^3).
 \qquad}                                                 \tag{15}
\]
Here \(|\log|e^{iu}||=|\Im u|\) exactly. In particular,
\[
 \int_{1/2-\varepsilon}^{1/2}r(t)\,dt
              =\frac{2\pi}{37}\varepsilon^2+O(\varepsilon^4).
                                                               \tag{16}
\]
The unestimated last frequency interval offers only this
quadratic additional accumulated weight near its endpoint.

## 3. Comparison with the original selected action branch

Let \(S(u)=S_3(0,u)\) be the originally calibrated action from
[the cubic continuation](research_mixed_next_inner_three_cubic_continuation.md).
Near zero, its selected inner half-cosine \(c_*(u)\) satisfies
\[
 \mathscr P_3(c_*(u))=\cos(u/2),\qquad c_*(0)=c_+,
 \qquad
 S'(u)=-\pi^{-1}\operatorname{arsinh}\{c_*(u)\tan(u/2)\}.
                                                               \tag{17}
\]
The identification \(c_*(0)=c_+\) follows from its proved
\(\Re c_*(0)>3/4\); the other roots in (9) have negative
real part. Its original Hessian is
\[
                             S''(0)=-c_+/(2\pi).         \tag{18}
\]

Consider only the local charged stationary equation
\[
                S'(u)+\frac{3iu}{2\pi}-i\delta=0.        \tag{19}
\]
Its derivative in \(u\) at zero is
\((-c_++3i)/(2\pi)\ne0\). It has a unique local holomorphic
solution, and evenness of \(S\) gives
\[
                  u_*(\delta)=\frac{2\pi}{3+ic_+}\delta
                                     +O(\delta^3).       \tag{20}
\]
This is in fact one of the exact symbol-zero branches (13).
To check the unsquared sign, put
\(R=\operatorname{arsinh}(c_*(u)\tan(u/2))\) on its original
local sheet and \(C=\cos(u/2)\). Equation (19) gives
\[
 R=i(3u/2-\pi\delta),\qquad k=ic_*(u),\qquad h=-\cosh R.
\]
Let \(T_3,U_2\) be the usual Chebyshev polynomials and
\(D=c_*^2+C^2-c_*^2C^2\). The root \(\sqrt D=C\cosh R\)
equals one at \(u=0\). The identity
\(T_3(c)^2+(1-c^2)U_2(c)^2=1\), together with
\(T_3(c_*)-iU_2(c_*)=C\), implies
\[
                          CT_3(c_*)-iU_2(c_*)\sqrt D=1. \tag{21}
\]
For a direct branch check, squaring
\((CT_3-1)/(iU_2)\) gives \(D\), and its value at zero is
one; \(U_2(c_+)\ne0\), so this proves (21) on a small
neighborhood without changing the square-root sign.
Substitution into \(Cw_3=-iCT_3-U_2\sqrt D\) gives
\(Cw_3=-i\), hence \(p=0\).

However, (11) proves that the leading distance of this selected
branch is strictly larger than \(4\pi\delta/37\). Thus (15)
is not its action-transport slope. The nearer lower-half-plane
root corresponds at the endpoint to \(c=+1/2\) on
\(\mathscr P_3(c)=-1\); its upper conjugate corresponds to
\(c=-1/2\) on \(\mathscr P_3(c)=1\). Neither is the original
selected \(c_+\) branch. No finite kernel, logarithmic lift or
competing saddle contribution is assigned to those algebraic roots.

## 4. The limiting optimal-weight criterion

The root-distance function extends continuously to \(t=1/2\)
by \(r(1/2)=0\). This follows also directly from the root
multiset continuity above. The complete outgoing action profile
\(E_Z(t)\) is continuous and decreasing on \([0,1/2]\).
For the optimizer of the zero-free theorem, one therefore has
\[
 \boxed{\quad
 \sup_{0<\alpha<1/2}\mathcal J_Z(\alpha)
   =\min_{0\le t\le1/2}
       \left[E_Z(0)-E_Z(t)+\int_t^{1/2}r(s)\,ds\right].
 \quad}                                                   \tag{22}
\]
Indeed \(\mathcal J_Z(\alpha)\) is nondecreasing: when
\(\alpha\) increases, the old candidate values increase by the
added integral, while every new candidate is at least
\(E_Z(0)-E_Z(\alpha_{\rm old})\ge\mathcal J_Z(\alpha_{\rm old})\).
Uniform continuity of the two functions and the vanishing final
integral identify its limit with the displayed minimum.
This limit does not authorize inversion at \(\alpha=1/2\);
a strict budget would still have to be realized at a fixed
smaller cutoff.

Equations (15),(22) provide an exact endpoint constraint and a
single action/root-distance comparison. They prove neither a
sufficient value nor a failure of that comparison. In particular
a finite signed-source bound is not inferred from the local
charged phase (19), and failure of the naive selected-branch
identification is not failure of the original volume statement.

## Frozen sources

- Original zero-free operator, Laurent polynomial and optimizer:
  b499a21141be11650f30b94498626e01383c9493edd670e4ef38e5ec985e11d6.
- Exact odd-inner square identity:
  7cb28ceade66edd8477715caec4a9204c2dcda0740e915fd6ccfcaeefa2c0eba.
- Original selected cubic, logarithmic lift and action Hessian:
  8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a.
- All-character symbol:
  c88ba98093fc147f5acfcf1790aa5b6f0f26edda6d741d2efc7c55315942e55e.
- Original anchored outgoing profile:
  e39abb76185b6969901b6ee4c95a4f947bdda5f74d8ff57062ed4b6591a0c029.

