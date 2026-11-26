# A quadratic upper bound for the conditional action

Research deduction, 7 November 2026. The earlier half-face comparison
replaced a strictly concave conditional action by its supporting line.
That replacement discarded a definite quadratic decrease in the
outgoing coordinate. Here we bound that decrease uniformly and retain
it in both alternatives of the Fourier weight.

This is an analytic improvement of the sufficient comparison. It does
not assert that the improved comparison holds on the following
geometric family. The completed, inconclusive calculation in
[the saved-data outcome](research_mixed_half_face_saved_affine_outcome.md)
is unchanged. No numerical evaluation is used.

## 1. The real maximization problem

Use the original conditional phase and primitive from
[the complete conditional theorem](research_mixed_half_face_complete_conditional_packet.md).
For real \(0<t,x<1/2\), put
\[
 q(t,x)=\Re Q(t;1/2,x),\qquad
 \bar q(x)=\max_{0<t<1/2}q(t,x),\qquad
 c=-J(1/4),\qquad J'(x)=\log(2\sin\pi x).
 \tag{1}
\]
Throughout this note,
\[
 I=[11/50,9/20],\qquad x_0=1/4,\qquad \delta=x-x_0.
 \tag{2}
\]
The maximum in (1) exists in the open interval. Indeed, \(q_t\)
tends to \(+\infty\) as \(t\) tends to zero and to \(-\infty\)
as \(t\) tends to \(1/2\). The strict concavity proved in
[the scalar comparison, Section 2](research_mixed_half_face_scalar_envelope_obstruction.md)
makes this maximum unique. Denote its location by \(t(x)\).
The implicit function theorem makes \(t(x)\) and \(\bar q(x)\)
smooth on \(I\).

Write
\[
 u=\cot\pi t(x),\qquad v=\cot\pi x.
 \tag{3}
\]
Taking the real derivative of the original phase, with its incoming
chirp retained, gives
\[
 e^{q_t(t,x)}
  =\frac{\cos\pi t\,\sin\pi(t+x)}{2\sin^3\pi t}
  =\frac{u(u+v)\sqrt{1+u^2}}{2\sqrt{1+v^2}}.
 \tag{4}
\]
Thus the last expression equals one at \(t(x)\).

**Lemma 1.** Uniformly for \(x\in I\),
\[
 0<v<\frac32,\qquad \frac12<u<\frac76.
 \tag{5}
\]

*Proof.* Since \(x>1/5\),
\[
 v^2<\cot^2(\pi/5)=\frac1{5-2\sqrt5}<2<\frac94.
\]
Here \(\sqrt5<9/4\) suffices for the middle inequality.
For fixed \(v>0\), the last expression in (4) is strictly
increasing in \(u>0\). At \(u=1/2\), it is bounded above by
\[
 \frac{\sqrt5}{8}(1/2+v)<\frac{\sqrt5}{4}<1.
 \tag{6}
\]
At \(u=7/6\), the inequality
\[
 (u+v)^2-u^2(1+v^2)
    =v\{2u-(u^2-1)v\}>0
 \tag{7}
\]
follows from \(v<3/2\), since
\[
 2u-(u^2-1)v>\frac73-\frac{13}{24}>0.
\]
Consequently the expression in (4) at \(u=7/6\) is at least
\[
 \frac{u^2\sqrt{1+u^2}}2
      =\frac{49\sqrt{85}}{432}>1.
 \tag{8}
\]
The last squared comparison is \(204085>186624\).
Monotonicity and (4) give (5). \(\square\)

## 2. Curvature after maximizing over the internal coordinate

**Lemma 2.** The real optimized action satisfies
\[
                         \bar q''(x)<-\frac{2\pi}{3}
                         \qquad(x\in I).
 \tag{9}
\]

*Proof.* With \(B=(uv-1)/(u+v)\), the real Hessian is
\[
 \pi^{-1}q''=
 \begin{pmatrix}
  -1/u-3u+B&B\\
  B&B-v
 \end{pmatrix}.
 \tag{10}
\]
Implicit differentiation of \(q_t(t(x),x)=0\) gives
\[
 -\frac{\bar q''(x)}{\pi}
   = v-B-\frac{B^2}{1/u+3u-B}
   =\frac{1+v^2+(3+2v^2)u^2+uv}
          {2u+3u^3+2u^2v+v}.
 \tag{11}
\]
The denominator is positive. Subtract two thirds of that
denominator from its numerator. The result is
\[
 \begin{split}
 &1+3u^2-\frac43u-2u^3\\
 &\qquad +(1+2u^2)v^2
             +\left(u-\frac43u^2-\frac23\right)v.
 \end{split}
 \tag{12}
\]
For \(1/2\le u\le7/6\), the first line is at least
\[
 1-\frac43u+\frac23u^2
          =\frac13+\frac23(u-1)^2\ge\frac13.
 \tag{13}
\]
Also \(1+2u^2\ge3/2\). The concave quadratic
\(u-4u^2/3-2/3\) has endpoint values \(-1/2\) and
\(-71/54\) on this interval, both greater than \(-4/3\).
The second line of (12) is therefore bounded below by
\[
 \frac32v^2-\frac43v
           =\frac32(v-4/9)^2-\frac8{27}\ge-\frac8{27}.
 \tag{14}
\]
Thus (12) is at least \(1/27>0\). Equation (11) proves (9).
\(\square\)

At \(x=x_0\), the maximizing internal coordinate is \(t=1/4\).
The original normalization gives
\[
 \bar q(x_0)=5c,\qquad \bar q'(x_0)=\frac12\log2.
 \tag{15}
\]
Integrating (9) on either side of \(x_0\) proves
\[
 \boxed{\quad
 \bar q(x)\le
       5c+\frac12\log2\,\delta-\frac{\pi}{3}\delta^2.
 \quad}
 \tag{16}
\]
For the allocated real action
\(\bar f(x)=\bar q(x)-J(x)/2\), it is useful first to retain
the primitive exactly:
\[
 \bar f(x)\le
 \frac{11}{2}c+\frac14\log2\,\delta-\frac{\pi}{3}\delta^2
 -\frac12\{J(x)-J(x_0)-J'(x_0)\delta\}.
 \tag{17}
\]
The expression in braces is nonnegative because \(J\) is convex
on \((0,1/2)\). More explicitly, throughout \(I\),
\[
 J''(x)=\pi\cot\pi x
 \ge\pi\tan(\pi/20)>\frac{5\pi}{32},
 \tag{18}
\]
using \(\tan s>s\) and \(\pi>25/8\). Hence
\[
 \boxed{\quad
 \bar f(x)\le
 \frac{11}{2}c+\frac14\log2\,\delta
                      -\frac{143\pi}{384}\delta^2.
 \quad}
 \tag{19}
\]
Both (16) and (19) hold for every real internal row, since its
action is bounded by the corresponding maximum.

## 3. The two upper costs with their curvature retained

Retain the notation and exact sufficient comparison from
[the scalar comparison, Section 1](research_mixed_half_face_scalar_envelope_obstruction.md).
In particular,
\[
 H=1/100,\qquad
 \widehat M=\frac{203}{200}-\frac{1303}{7680000}.
 \tag{20}
\]
The source theorem bounds the complex conditional action by the
largest real-row action at outgoing coordinate \(x+iH\).
Moving that row from \(x\) to \(x+iH\) costs at most \(\pi H\).
The selected halfweight obeys
\[
 h_{\rm sel}(x)\le
       \max\{-J(x)/2-3\pi H/4,0\}.
 \tag{21}
\]
These are the already proved, original-source bounds; neither an
alias nor a Fourier alternative is omitted in using them.

Define
\[
 \begin{array}{lll}
 K_{\rm fac}=\widehat M+\frac{11}{2}c+\frac{\pi H}{4}+\frac7{250},
 & b_{\rm fac}=\frac14\log2,
 & \mu_{\rm fac}=\frac{143\pi}{384},\\[2mm]
 K_{\rm force}=\widehat M+5c+\pi H+\frac7{250},
 & b_{\rm force}=\frac12\log2,
 & \mu_{\rm force}=\frac{\pi}{3}.
 \end{array}
 \tag{22}
\]
Equations (16), (19), and (21) imply
\[
 M_{\rm half}+\Re\Theta(x+iH)+h_{\rm sel}(x)+\frac7{250}
 \le
 \max_{\sigma\in\{{\rm fac},{\rm force}\}}
       \{K_\sigma+b_\sigma\delta-\mu_\sigma\delta^2\}.
 \tag{23}
\]
An established upper bound for \(c\) may replace \(c\) in
\(K_\sigma\), if a purely elementary constant is desired.
No such replacement is required for the theorem.

## 4. Eliminate the outgoing coordinate exactly

For a fixed actual following reference, let \(A_*,a_*,p_*\)
denote its allocated action, real outgoing coordinate, and real
marginal, respectively, as defined in equation (5) of the scalar
comparison. Its supporting affine function is
\[
                         A_*+p_*(x-a_*).
 \tag{24}
\]
Here these three quantities must come from the same original
critical solution.

Put \(d_-=-3/100\), \(d_+=1/5\), and, for \(\mu>0\), define
\[
 H_\mu(s)=
       \max_{d_-\le d\le d_+}(sd-\mu d^2).
 \tag{25}
\]
Completing the square gives the explicit formula
\[
 H_\mu(s)=
 \begin{cases}
 sd_- -\mu d_-^2,&s\le2\mu d_-,\\
 s^2/(4\mu),&2\mu d_-\le s\le2\mu d_+,\\
 sd_+ -\mu d_+^2,&s\ge2\mu d_+.
 \end{cases}
 \tag{26}
\]

**Proposition.** A sufficient condition for the required strict
half-face comparison at this reference, for every \(x\in I\),
is the following pair of scalar inequalities:
\[
 \boxed{\quad
 A_*+p_*(x_0-a_*)-K_\sigma
       >H_{\mu_\sigma}(b_\sigma-p_*)
       \quad(\sigma={\rm fac},{\rm force}).
 \quad}
 \tag{27}
\]

*Proof.* Subtract (24) from each alternative on the right side
of (23). The difference is
\[
 K_\sigma-A_*-p_*(x_0-a_*)
        +(b_\sigma-p_*)\delta-\mu_\sigma\delta^2.
 \tag{28}
\]
Its maximum over \(I\) is exactly the left constant in (28)
plus \(H_{\mu_\sigma}(b_\sigma-p_*)\). Thus (27) makes both
alternatives strictly negative on the full interval. \(\square\)

Unlike the previous affine costs, the maximum in (28) can lie
inside the interval. Testing just its endpoints would be
incorrect. Formula (26) retains this possibility exactly.

This reduction has not been verified on the full actual following
family. In particular it does not authorize reinterpreting the
old saved certificates under a different acceptance test.
Nor does it settle the original incoming connector, continue the
complete cap throughout the incoming interval, or prove a new
knot family. Its contribution is the uniform curvature bound
(9), the strictly sharper upper costs (23), and the exact
one-variable elimination (27).
