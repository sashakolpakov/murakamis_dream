# Acute conditional gradients and vertical phase transfer

Research proof, 5 November 2026. This gives exact gradient bounds for the
original allocated critical phase and a lower bound when real outer
parameters acquire admissible imaginary parts. It is a phase comparison;
it does not give a lower bound for a finite conditional kernel or prove a
seam comparison.

## 1. Phase, root and logarithms

For \(\eta,\epsilon\in\{0,1\}\), retain
\[
 \begin{split}
 g(z)&=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},\\
 Q_\epsilon(s;a,b)&=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias,\\
 \phi_{\eta\epsilon}(a,b)&=Q_\epsilon(s_*(a,b);a,b)
                  -(1+\eta/2)g(a)-(1+\epsilon/2)g(b),\\
 f_{\eta\epsilon}(a,b)&=\Re\phi_{\eta\epsilon}(a,b).
 \end{split}                                                     \tag{1}
\]
First take \(0<a,b\le1/2\), and put
\(p=\cot\pi a\ge0\), \(q=\cot\pi b\ge0\). The
[closed cotangent-root theorem](research_mixed_closed_cotangent_roots.md)
supplies the unique simple original zero-lift root
\(S=\cot\pi s_*=u+iv\), where \(u>0\), \(|v|<1\), of
\[
 F_0(S)=S^2+(p+q)S-1+i(q-p),\qquad
 F_1(S)=(S+i)(S+p)(S+q)-2i(p-i)(q+i).
 \tag{2}
\]
This includes \(p=0\), \(q=0\), and their intersection. The roots
are continuous on the entire closed real quadrant, and holomorphic on
a neighborhood of each finite parameter pair.

Write \(\log_{\rm R}\) for the logarithm on the open right half-plane,
with argument in \((-\pi/2,\pi/2)\). All four numbers
\(S+p,S+q,S-i,S+i\) lie in that half-plane. The exact original
gradient identities are
\[
 \begin{split}
 \phi_a&=\log_{\rm R}(S+p)-\log_{\rm R}(S-i)
                                      -\frac\eta2g'(a),\\
 \phi_b&=\log_{\rm R}(S+q)-\log_{\rm R}(S+i)
                                      -\frac\epsilon2g'(b).
 \end{split}                                                     \tag{3}
\]
Indeed, stationarity eliminates derivatives of \(s_*\). With
\(A=e^{-2\pi ia}=(p-i)/(p+i)\),
\(B=e^{-2\pi ib}=(q-i)/(q+i)\),
\(U=e^{-2\pi is}=(S-i)/(S+i)\), exponentiation gives
\[
 \frac{1-AU}{(1-A)U}=\frac{S+p}{S-i},\qquad
 \frac{1-BU}{1-B}=\frac{S+q}{S+i}.
 \tag{4}
\]
These are the exponentials of
\(g'(s+a)-g'(a)+2\pi is\) and \(g'(s+b)-g'(b)\), respectively.
To fix their additive multiples of \(2\pi i\), initially take real
\(S>0\), so \(0<s<1/2\). In the original regular strip,
\(g'(z)=\log(2\sin\pi z)+i\pi(1/2-z)\), with the sine logarithm
having positive-real-part argument. The two differences then have
imaginary parts \(\pi s\) and \(-\pi s\), exactly the differences
of the right-half-plane arguments in (3). Connectedness of
\(u>0,|v|<1,p,q\ge0\) and nonvanishing of all the factors extends
these equalities throughout that domain. All arguments \(a,b,s+a,s+b\)
stay in their original regular strips. This proves (3) on the original
lift, including either half-period endpoint.

## 2. Both ratios are acute

**Theorem 1.** At either selected root in (2),
\[
 0<\theta_a:=\Arg\frac{S+p}{S-i}<\frac\pi2,\qquad
 -\frac\pi2<\theta_b:=\Arg\frac{S+q}{S+i}<0.
 \tag{5}
\]
The arguments here are exactly the differences of the logarithms in
(3), with no reduction modulo \(2\pi\).

The imaginary numerators of the two ratios are
\(u+p(1-v)>0\) and \(-u-q(1+v)<0\). Their real numerators are
\[
 N_a=u^2+up+v^2-v,\qquad N_b=u^2+uq+v^2+v.
 \tag{6}
\]
It remains to prove both positive.

For \(\epsilon=0\), set \(T=2u+p+q\). The real and imaginary
equations imply \(uT=u^2+v^2+1\) and \(vT=p-q\). Consequently
\[
 \begin{split}
 2N_a&=(1+v)u^2+v^2(v+3)+1-v>0,\\
 2N_b&=(1-v)u^2+v^2(3-v)+1+v>0.
 \end{split}                                                     \tag{7}
\]
Every displayed term has the stated sign for \(-1<v<1\).

For \(\epsilon=1\), first exclude a zero of \(N_a\). Such a zero
would require \(0<v<1\) and
\(p=(v-v^2-u^2)/u\). Substitute this value into \(F_1\), and let
\(R=u\Re F_1\), \(I=u\Im F_1\). These are real polynomials
after substitution. Their resultant in \(q\), with \(x=u^2>0\), is
\[
 \begin{split}
 \operatorname{Res}_q(R,I)
 ={}&x^2(v^3+6v^2+4)
   +2x\{v^3(v+1)^2+2(3v^2-2v+1)\}\\
   &+v^2(1-v)^4(v+2)>0.
 \end{split}                                                     \tag{8}
\]
Here \(3v^2-2v+1=3(v-1/3)^2+2/3>0\). The nonzero resultant
contradicts the simultaneous real and imaginary root equations.

A zero of \(N_b\) would instead require \(v=-t\), \(0<t<1\),
and \(q=(t-t^2-u^2)/u\). After this substitution define
\(R=u\Re F_1\), \(I=u\Im F_1\) again. Their resultant in \(p\)
is
\[
 \begin{split}
 \operatorname{Res}_p(R,I)=-\bigl[&x^2(t^3-6t^2+4t+4)\\
 &+2x(t^5-4t^4+t^3+4t^2-2t+2)\\
 &+t^2(1-t)^2(1+t)(t^2-t+2)\bigr]<0.
 \end{split}                                                     \tag{9}
\]
The strict sign follows from the exact decompositions
\[
 \begin{split}
 t^3-6t^2+4t+4&=4(1-t^2)+2t(2-t)+t^3,\\
 t^5-4t^4+t^3+4t^2-2t+2
   &=t^5+t^3+4t^2(1-t^2)+2(1-t),\\
 t^2-t+2&=(t-1/2)^2+7/4.
 \end{split}                                                     \tag{10}
\]
Thus neither real numerator can vanish anywhere on the closed
\((p,q)\)-quadrant.

For their signs, use the selected root at \(p=q=0\). Its real
equation gives \(u^2=3v^2+2v\), and its imaginary equation then gives
\(4v^3+4v^2+v-1=0\). Since \(u>0\), either \(v>0\) or
\(-1<v<-2/3\). In the latter interval,
\(4v^2(v+1)+v-1<4/3-5/3<0\), a contradiction. Therefore \(v>0\)
and
\[
 N_a=4v^2+v>0,\qquad N_b=4v^2+3v>0.
 \tag{11}
\]
The globally specified simple root is continuous along every compact
path from \((0,0)\) to \((p,q)\) in the closed quadrant. Equations
(8)--(9) prohibit either sign from changing. This proves the cubic
case without a numerical root-count or base-sign premise. The strict
imaginary signs and the right-half-plane logarithms now prove (5).
On compact real outer parameter sets, both angles stay uniformly
inside their respective open acute intervals. \(\square\)

**Corollary 1 (only the differentiated endpoint is real).** The first
acute inequality in (5) still holds if \(p\ge0\) is real but
\(Q=q+i\beta\), \(q\ge0\), \(|\beta|<1/2\). The second still
holds if \(q\ge0\) is real but \(P=p+i\alpha\), \(p\ge0\),
\(|\alpha|<1/2\). The corresponding identity in (3) has the same
original logarithmic lift. No acute inequality for the other,
nonreal endpoint is asserted.

**Proof.** The closed-root theorem still gives \(u>0,|v|<1\).
For a real left endpoint, \(N_a>0\) is automatic when \(v\le0\).
For the quadratic and \(v>0\), its equations give
\[
 2N_a=(1+v+\beta)u^2+v^3+(3+\beta)v^2
                                     +(2\beta-1)v+1+\beta.
 \tag{11a}
\]
This expression increases with \(\beta\). At \(\beta=-1/2\),
its \(u^2\) coefficient is \(1/2+v>0\), and its remaining part is
\(v^3+(5/2)(v-2/5)^2+1/10>0\). The quadratic right-endpoint
claim follows by the exact symmetry
\(F_0(\overline S;\overline Q,\overline P)
=\overline{F_0(S;P,Q)}\).

For the cubic left endpoint, impose \(N_a=0\) as before. The
resultant in (8) becomes
\[
 \begin{split}
 P_a(x,v,\beta)={}&x^2\{v^3+6v^2+4+\beta(v+2)^2\}\\
 &+2x\{v^5+2v^4+v^3+6v^2-4v+2
                           +\beta(v^4+7v^2-2v+2)\}\\
 &+v^2(1-v)^4(v+2+\beta).
 \end{split}                                                     \tag{11b}
\]
Every coefficient increases with \(\beta\), since
\(v^4+7v^2-2v+2=v^4+7(v-1/7)^2+13/7>0\). At
\(\beta=-1/2\), the coefficients of \(x^2\) and \(x\) are
respectively
\[
 v^3+\frac{11}{2}(v-2/11)^2+\frac{20}{11},\qquad
 2v^5+3v^4+2v^3+5(v-3/5)^2+\frac15.
 \tag{11c}
\]
The constant is positive. Hence \(P_a>0\), excluding a zero.

For the cubic right endpoint, impose \(N_b=0\), set \(v=-t\),
and eliminate \(p\). The resultant is \(-P_b(x,t,\alpha)\), where
\[
 \begin{split}
 P_b={}&x^2\{t^3-6t^2+4t+4-\alpha(t-2)^2\}\\
 &+2x\{t^5-4t^4+t^3+4t^2-2t+2
                    +\alpha(-t^4+2t^3+t^2-2t-2)\}\\
 &+t^2(1-t)^2(1+t)\{t^2-t+2-\alpha(t+1)\}.
 \end{split}                                                     \tag{11d}
\]
All coefficients decrease with \(\alpha\): the middle slope equals
\(-(t^2-1)^2+2t(t^2-1)-t^2-1<0\). At \(\alpha=1/2\), the
\(x^2\) coefficient is
\(t^3+6t(1-t)+2-t^2/2>3/2\), and the constant bracket is
\((t-3/4)^2+15/16>0\). The \(x\) coefficient is
\[
 \begin{split}
 2t^5-9t^4+4t^3+9t^2-6t+2
 &=\sum_{j=0}^5 b_j\binom5j t^j(1-t)^{5-j},\\
 (b_0,\ldots,b_5)&=(2,4/5,1/2,3/2,12/5,2),
 \end{split}                                                     \tag{11e}
\]
so it too is positive on \(0<t<1\). Neither cubic real numerator
can vanish. Both have their positive signs at the real base
\(p=q=0\) already proved in (11). Each of the present parameter
domains is connected to that base within the closed cotangent chamber;
continuity therefore proves the signs everywhere. The imaginary
numerators and logarithmic calibration are unchanged when the
differentiated endpoint remains real. \(\square\)

## 3. Exact affine transfer to complex heights

For real \(0<x\le1/2\), put \(\alpha(x)=\pi/2-\pi x\). Then
\(\Im g'(x)=\alpha(x)\). Equations (3) and (5) give
\[
 \Im\phi_a=\theta_a-\frac\eta2\alpha(a),\qquad
 \Im\phi_b=\theta_b-\frac\epsilon2\alpha(b).
 \tag{12}
\]
In particular the type-dependent shifts in these gradients have not
been dropped.

For the complex targets use the same typed polygons as in
[the attenuation theorem](research_mixed_seam_attenuation_vertices.md),
Lemma 1:
\[
 \begin{split}
 \Omega_3&=\operatorname{conv}\{.1,.22-.03i,.45-.03i,.5,
                                     .45+.02i,.22+.02i\},\\
 \Omega_4&=\operatorname{conv}\{.1,.22-.057i,.45-.057i,.5,
                                     .45+.014i,.12+.014i\}.
 \end{split}                                                     \tag{13}
\]
The inherited scalar cotangent bounds give
\(\Re\cot\pi z\ge0\), \(|\Im\cot\pi z|<1/2\) on these
whole polygons. The closed-root theorem and its triangle/complex-Schur
argument consequently give \(-\Re\phi''>0\) on their independent
products. This is an ambient phase statement, not concavity after a
varying-height substitution. The complete finite-source coverage of
these products is recorded separately in that attenuation theorem.

Fix \(a,b\in[.1,.5]\) and targets
\(a+ih\in\Omega_{3+\eta}\), \(b+ik\in\Omega_{3+\epsilon}\).
Convexity of the polygons puts their entire straight vertical segment
from \((a,b)\) inside the same product. For selections
\(0\le\sigma_a\le\eta\), \(0\le\sigma_b\le\epsilon\), both
integer, define the original allocated coherent upper rate
\[
 \begin{split}
 e_\sigma(z,w)&=\Re\phi_{\eta\epsilon}(z,w)
                     +\tfrac12\sigma_a\chi(z)+\tfrac12\sigma_b\chi(w),\\
 \chi(z)&=\max\{\Re g(z),-2\pi\Im z\}.
 \end{split}                                                     \tag{14}
\]
Both Fourier alternatives are retained, including ties at real part
\(1/2\). In the maximum of the holomorphic branches, choose the
frequency alternative at both selected endpoints:
\(\psi_0(z,w)=\phi(z,w)+\pi i(\sigma_a z+\sigma_b w)\).
Its real value at \((a,b)\) is \(f(a,b)\), and
\(e_\sigma\ge\Re\psi_0\) everywhere. Its height Hessian equals
\(-\Re\phi''>0\).

**Theorem 2.** Under these hypotheses,
\[
 e_\sigma(a+ih,b+ik)\ge f(a,b)
       -\{\Im\phi_a(a,b)+\pi\sigma_a\}h
       -\{\Im\phi_b(a,b)+\pi\sigma_b\}k.
 \tag{15}
\]
This is the tangent inequality for the convex real function
\(\Re\psi_0(a+ih,b+ik)\), with its derivatives evaluated at
the original real root. It requires no differentiability of the
maximum in (14). Substituting (12) gives its explicit affine form.

Writing \(x_+=\max(x,0)\), the acute bounds further imply
\[
 \begin{split}
 e_\sigma(a+ih,b+ik)\ge f(a,b)
 &-\frac\pi2 h_+-\frac\pi2(-k)_+
   +\frac\eta2\alpha(a)h+\frac\epsilon2\alpha(b)k\\
 &-\pi\sigma_a h-\pi\sigma_b k.
 \end{split}                                                     \tag{16}
\]
The two one-sided losses come from \(0<\theta_a<\pi/2\) and
\(-\pi/2<\theta_b<0\), respectively. All type and selected-frequency
terms remain explicit. The bounds also hold when a height is zero or
an outer real coordinate equals \(1/2\). No numerical reserve for a
general seam configuration is asserted by (16).

**Corollary 2 (one height changes, the neighbor may be complex).**
For fixed \(w\in\Omega_{3+\epsilon}\), real \(a\in[.1,.5]\), and
\(a+ih\in\Omega_{3+\eta}\),
\[
 e_\sigma(a+ih,w)\ge e_\sigma(a,w)
               -\{\Im\phi_a(a,w)+\pi\sigma_a\}h.
 \tag{17}
\]
Likewise, for fixed \(z\in\Omega_{3+\eta}\), real \(b\in[.1,.5]\),
and \(b+ik\in\Omega_{3+\epsilon}\),
\[
 e_\sigma(z,b+ik)\ge e_\sigma(z,b)
               -\{\Im\phi_b(z,b)+\pi\sigma_b\}k.
 \tag{18}
\]
The gradient in (17) satisfies the first formula and acute range in
(12); the gradient in (18) satisfies the second, by Corollary 1.
Thus their losses are bounded by the corresponding one-coordinate
terms on the right of (16).

To prove this for the maximum envelope, note that \(J(x)=\Re g(x)\)
has \(J(0)=J(1/2)=0\), \(J''(x)=\pi\cot\pi x>0\) on the
open real half-period. Hence \(J(x)\le0\). At the real endpoint
the frequency branch is therefore maximizing. At its complex neighbor
choose either branch that attains the maximum there. This gives a
holomorphic branch \(\psi_f\) attaining the entire value of
\(e_\sigma\) at the base point. The neighbor's added term contributes
no derivative at the differentiated endpoint. Its vertical curvature
is positive by the selected triangle/Schur argument of the attenuation
theorem: the remaining allocated coefficients are
\((\eta-f_a)/2,(\epsilon-f_b)/2\ge0\). Apply its convex tangent
inequality and then use \(e_\sigma\ge\Re\psi_f\). This also handles
branch ties and real half-period endpoints.

## Reproduction

    python3 experiments/check_mixed_acute_gradient_height_transfer.py

The checker verifies the exponentiated gradient identities, both exact
resultants, all positive polynomial and Bernstein decompositions, the
endpoint base identities and the height-derivative signs. It binds the current original
root and polygon-curvature inputs. No source cells or numerical roots
are recomputed. The noncrossing, logarithmic calibration and convexity
arguments are the analytic proofs above.
