# Height monotonicity of the twice-crossed conditional action

Research deduction, 7 November 2026. The original conditional critical
point for every actual type-three incoming input lies in the right
quarter of the left half-period. Its critical action strictly decreases
with the incoming height. Relative to the exact endpoint forcing, the
action gap increases up to height zero and decreases afterward.
Consequently the sign of that gap on the whole containing rectangle
reduces to its two extreme-height faces.

No sign of either remaining face is asserted. This is a statement
about the original critical action, not a whole-source asymptotic or
a comparison of separately bounded contour pieces. No numerical
evaluation is used.

## 1. The transformed index is in the right quarter

Keep the fixed original output \(y=x_0\) and
\[
 \mathcal A=[267/1000,433/1000]+i[-9/125,17/250].
 \tag{1}
\]
The [actual-input theorem](research_mixed_three_conditional_actual_input_subdomain.md)
and the [left zero-mode theorem](research_mixed_three_fourier_conditional_left_zero_mode.md)
give a simple holomorphic critical branch \(s_*(a)\), with its
original logarithmic lift. Write
\[
 \begin{gathered}
 P=\cot(\pi a)=p+i\alpha,\qquad
 Q=\cot(\pi y)=q-i b,\\
 S=\cot(\pi s_*)=u-i v,\qquad
 p,q,u>0,\quad 0<v<1,\\
 c_+=b+\alpha>0,\qquad d=q-p>0 .
 \end{gathered}
 \tag{2}
\]
All these strict signs hold uniformly on (1); in particular
\(b>17/25\), \(|\alpha|<387/1000\), and \(q-p>37/100\).
The selected root satisfies the original equation
\[
             S^2+(P+Q)S-1+i(Q-P)=0.
 \tag{3}
\]

**Lemma 1.** On (1),
\[
                  |S|<1,\qquad 1/4<\Re s_*<1/2.
 \tag{4}
\]

*Proof.* Put \(R^2=u^2+v^2\). Taking the real part of (3)
after division by \(S\), and multiplying by \(R^2\), gives
\[
 u(R^2-1)+(p+q)R^2+c_+u-d v=0.
 \tag{5}
\]
If \(R^2\ge1\), its left side is strictly greater than
\[
                   p+q-d=2p>0,
 \tag{6}
\]
because \(u,c_+>0\) and \(0<v<1\). This contradicts (5).
For the original inverse-cotangent branch \(0<\Re s_*<1/2\),
\[
 |\cot\pi(x+iH)|^2
   =\frac{\cosh(2\pi H)+\cos(2\pi x)}
          {\cosh(2\pi H)-\cos(2\pi x)}.
 \tag{7}
\]
Thus \(|S|<1\) is equivalent to \(\cos(2\pi\Re s_*)<0\),
which proves (4). \(\square\)

The strict bounds in (4) persist uniformly on the compact family.
Together with the already proved positive critical height they imply
\[
 \frac12<\Re(s_*+a)<1,\qquad \Im s_*>0 .
 \tag{8}
\]
The first strict lower inequality uses \(\Re a\ge267/1000>1/4\).
This identifies an original shifted-factor strip; it does not replace
its upper-half logarithm by a periodic disk branch.

## 2. The exact action derivative

Use the normalized conditional phase and action
\[
 \begin{split}
 \mathscr F(s;a,y)
   &=g(s+a)+g(s+y)-2g(s)-g(a)-g(y)+2\pi ias,\\
 \Phi(a)&=\mathscr F(s_*(a);a,y),\qquad
 \mathscr M(x,h)=\Re\Phi(x+ih).
 \end{split}
 \tag{9}
\]
This is the phase of \(C_{0,N}\) before the exact outside factor
\(\kappa^{-2}e^{\pi i(N-1)y}/N\). All primitives and logarithms
have their original factorial lifts. The stationary chain rule gives
\[
 \Phi_a=g'(s_*+a)-g'(a)+2\pi i s_* .
 \tag{10}
\]

For every real height \(H\), the original logarithm obeys
\[
 \begin{array}{ll}
 0<\Im g'(r+iH)<\pi(1-2r),&0<r<1/2,\\
 \pi(1-2r)<\Im g'(r+iH)<0,&1/2<r<1.
 \end{array}
 \tag{11}
\]
Indeed \(g'(z)=\log(1-e^{-2\pi iz})\), and the ray
\(1-R e^{-2\pi ir}\), \(R>0\), stays in its prescribed
upper or lower half-plane. Its arguments lie strictly between zero
and their indicated infinite-radius limit. This uses the original
strip branch at every height.

Put \(\sigma=\Re s_*\) and \(a=x+ih\). By (8) and (11),
\[
 0<
 \Im g'(a)-\Im g'(s_*+a)
 <\pi(1-2x)-\pi(1-2x-2\sigma)=2\pi\sigma.
 \tag{12}
\]
Since \(\partial_h\Re\Phi=-\Im\Phi_a\), equations (10)--(12)
prove the uniform strict derivative bounds
\[
 \boxed{\qquad
        -\pi<-2\pi\sigma<
             \partial_h\mathscr M(x,h)<0
          \qquad ((x,h)\in\mathcal A).
 \qquad}
 \tag{13}
\]
Uniformity here means the continuous strict quantities have a
positive reserve on (1), not a newly evaluated numerical reserve.

## 3. Reduction of the critical-action/forcing comparison

The [complete endpoint-current theorem](research_mixed_three_fourier_conditional_endpoint_current.md)
retains the exact conditional forcing rate
\[
 \mathcal F(h)=2\pi(-h)_++2\pi\Im y .
 \tag{14}
\]
Define the action gap
\[
                   \Delta(x,h)=\mathscr M(x,h)-\mathcal F(h).
 \tag{15}
\]
The outside twice-crossed scalar subtracts the same
\(\pi\Im y\) from both rates, so (15) is also their difference
after that scalar is restored. An incoming allocation, if present,
likewise subtracts the same quantity from both sides.

Equation (13) proves
\[
 \boxed{\quad
 \begin{array}{ll}
 \pi<\partial_h\Delta(x,h)<2\pi,&-9/125\le h<0,\\
 -\pi<\partial_h\Delta(x,h)<0,&0<h\le17/250.
 \end{array}
 \quad}
 \tag{16}
\]
Consequently, for each fixed \(x\in[267/1000,433/1000]\),
\[
 \begin{split}
 \max_{-9/125\le h\le17/250}\Delta(x,h)&=\Delta(x,0),\\
 \min_{-9/125\le h\le17/250}\Delta(x,h)
   &=\min\{\Delta(x,-9/125),\Delta(x,17/250)\}.
 \end{split}
 \tag{17}
\]
These are exact reductions of the continuous action comparison,
not proposed parameter tests. In particular, a strict positive gap
on both extreme-height faces would prove it on the whole rectangle;
a nonpositive gap at either face would rule out that uniform
rectangle conclusion. No value on those faces has been evaluated
or its sign inferred here.

The left zero-mode theorem already proves a nonzero Gaussian for
the entire left horizontal path and pays its left connector relative
to \(\mathscr M\). Equations (13)--(17) do not estimate the remaining
right path or rule out cancellation with the endpoint current.
The closed finite
[conditional difference equation](research_mixed_three_fourier_conditional_difference_equation.md)
also retains its forcing; it supplies no missing action comparison.

The source inputs used here were read at hashes
\(86eb9f66dec74dab81b7c65159dc1213d99cbc1abddee01fb88a919bd789a8e1\)
(root criterion),
\(8634fdaadacc8387b7904bc528bac65fcdf6e490b7de99413b95c2083119de9d\)
(actual input),
\(450ddf50d6066d726ad09fcf590bb305503ee2d471120fff17c83c16caa68595\)
(left zero mode), and
\(3875ef15c77bd4327eb496f8bc14cbc80ef88e3faef59ce3d9cad4a9db6cb96c\)
(endpoint current).
