# Two explicit tests for a left outgoing contour

Research deduction, 7 November 2026. A contour returning to the
real axis at its left endpoint may avoid a separate unpenalized
vertical join there. This note reduces the derivative of the joint
phase on one proposed contour to two explicit real functions. A direct
estimate proves positivity for the first hundredth of the real
coordinate; the rest remains to be checked. The reduction does not assert an
estimate for the finite source or discard any connecting contour.

## 1. The proposed contour and its original derivative

Keep the global factorial chart and the original phase from
[the right-main comparison](research_mixed_fourier_right_cap_upper_main_arc.md).
Write
\[
 c=\frac{11}{50},\qquad y=\xi+i\upsilon=x_0,\qquad
 Y=e^{2\pi iy}=\rho e^{i\phi},\qquad \phi=2\pi\xi\in(0,\pi/2).
 \tag{1}
\]
For the original negative outgoing critical height \(h_q\), put
\[
 \lambda=-h_q/c,\qquad 0<\lambda\le\frac{51}{110},\qquad
 q(x)=x-i\lambda x\quad(0<x\le c).
 \tag{2}
\]
Then \(q(c)=c+ih_q\). The retained index is
\[
 s=u+ih_s,\qquad \frac18\le u\le\frac12,
 \qquad -.102\le h_s\le-.001.
 \tag{3}
\]
The incoming parameter and its halfweight are unchanged.
They are independent of the outgoing coordinate in the derivative
below. Every varying primitive in this derivative belongs to its
original lower-half-plane disk branch.

For \(Q=e^{-2\pi iq}\) and \(S=e^{-2\pi is}\),
\[
 D(s,q)=\partial_q\mathscr F_\eta
   =\Log(1-SQ)-\Log(1-Q)-\Log(1-YQ)+\log\rho+i\phi .
 \tag{4}
\]
The three logarithms are their disk branches. Thus the derivative
along (2) is exactly
\[
 \frac{d}{dx}\Re\mathscr F_\eta(s,a,q(x))
                         =\Re[(1-i\lambda)D(s,q(x))].
 \tag{5}
\]
It is important to retain the imaginary part of (4) in (5).
A bound for the horizontal derivative alone is a different claim.

## 2. Eliminating the retained real index and radius

Put
\[
 r=e^{-2\pi\lambda x},\qquad
 f_\lambda(t,\theta)=
 \frac12\log(1+t^2-2t\cos\theta)
 +\lambda\arg(1-te^{-i\theta}).
 \tag{6}
\]
Here \(0\le t\le r<1\), so the argument is the unique one
in \((-\pi/2,\pi/2)\). The same expression has its continuous
values on the endpoint ranges used below. In the first term of
(4), \(t=r e^{2\pi h_s}\) and \(\theta=2\pi(x+u)\).
The inherited exponential bound gives
\(e^{2\pi h_s}>1/2\), so its actual radius interval is
contained in \([r/2,r]\).

**Lemma 1.** For fixed \(x,\lambda,t\) in these ranges, the
minimum of \(f_\lambda(t,2\pi(x+u))\) over
\(u\in[1/8,1/2]\) occurs at one of the two endpoints.

*Proof.* For \(t=0\), the function is constant and the claim is
immediate. Assume \(t>0\). Its derivative with respect to \(\theta\) has the sign of
\[
                 n(\theta)=\sin\theta+\lambda(\cos\theta-t).
 \tag{7}
\]
The angle interval is contained in \([\pi/4,36\pi/25]\).
For \(\theta\ge\pi\), both summands in (7) are nonpositive,
and the second is negative because \(\cos\theta<0\).
For a zero with \(\theta<\pi\), one has
\(t-\cos\theta>0\) and
\(\lambda=\sin\theta/(t-\cos\theta)\). At that zero,
\[
          n'(\theta)=\frac{t\cos\theta-1}{t-\cos\theta}<0.
 \tag{8}
\]
Every interior stationary point is therefore a strict maximum.
The minimum is at an endpoint. \(\square\)

For a fixed endpoint angle, direct differentiation gives
\[
 \partial_t f_\lambda(t,\theta)
     =\frac{t-\cos\theta+\lambda\sin\theta}
                  {1+t^2-2t\cos\theta}.
 \tag{9}
\]
The denominator is positive. Define
\[
 \begin{split}
 \theta_-&=2\pi(x+1/8),\qquad \theta_+=2\pi(x+1/2),\\
 t_\pm&=\min\{r,\max\{r/2,\cos\theta_\pm
                                      -\lambda\sin\theta_\pm\}\}.
 \end{split}
 \tag{10}
\]
Equation (9) proves that \(t_\pm\) is the minimizing radius
on the closed containing interval \([r/2,r]\). Combining this
with Lemma 1 gives the uniform inequality
\[
 \Re[(1-i\lambda)\Log(1-SQ)]
       \ge\min_{\nu\in\{-,+\}}f_\lambda(t_\nu,\theta_\nu).
 \tag{11}
\]
This is an exact minimization on the containing rectangle;
it does not treat the actual retained heights as independently
attained extrema of the geometric family.

## 3. The two remaining scalar expressions

Define the part of (5) independent of the retained index by
\[
 \begin{split}
 K(x,\lambda)={}&
 \log\frac{\rho}{|1-Q|\,|1-YQ|}\\
 &+\lambda\{\phi-\arg(1-Q)-\arg(1-YQ)\},
 \qquad Q=e^{-2\pi i(x-i\lambda x)}.
 \end{split}
 \tag{12}
\]
All arguments in (12) have the original disk determinations.
Put
\[
                 H_\pm(x,\lambda)
                      =K(x,\lambda)+f_\lambda(t_\pm,\theta_\pm).
 \tag{13}
\]
The proved directional comparison is
\[
 \boxed{\quad
 \frac{d}{dx}\Re\mathscr F_\eta(s,a,q(x))
               \ge\min\{H_-(x,\lambda),H_+(x,\lambda)\}.
 \quad}
 \tag{14}
\]
It is independent of the incoming parameter \(a\) and its type.
The only fixed geometric output in (12) is the original \(Y\).

## 4. Positivity near the endpoint

**Lemma 2.** For \(0<x\le1/100\), \(0\le\lambda\le51/110\),
and the entire containing retained rectangle
\(1/8\le\Re s\le1/2\), \(1/2\le|S|\le1\), the derivative
in (5) is strictly greater than \(3/4\). In particular both
minimized functions \(H_\pm\) satisfy that bound there.

*Proof.* Write \(v=2\pi x\). Then \(0<v<11/175\) and
\(Q=e^{-(\lambda+i)v}\). Integration of this exponential gives
\[
 |1-Q|\le v\sqrt{1+\lambda^2}<\frac98v<\frac{99}{1400}.
 \tag{15}
\]
The original geometric output satisfies \(3/5<\rho<5/8\)
and \(\phi>8/7\). For the latter inequality it suffices to use
\(\xi>91/500\) and \(\pi>157/50\). Also
\(|1-YQ|<1+\rho<13/8\).

The angle \(\theta=2\pi(\Re s+x)\) belongs to
\([\pi/4,\pi+v]\). Therefore \(\cos\theta<3/4\).
For every \(0\le t\le1\), minimizing
\(1+t^2-2t\cos\theta\) in \(t\) shows
\[
       |1-te^{-i\theta}|>3/5.
\]
Apply this with \(t=|SQ|\). The real part of (4) consequently
obeys
\[
 e^{\Re D}
 =\frac{\rho|1-SQ|}{|1-Q||1-YQ|}
 >\frac{9}{25}\frac{11200}{1287}
 =\frac{4032}{1287}>3.
 \tag{16}
\]

If \(\theta\le\pi\), the numerator argument is nonnegative.
If \(\pi<\theta\le\pi+v\), write
\(1-te^{-i\theta}=1+te^{-i(\theta-\pi)}\); its argument lies
between \(-(\theta-\pi)\) and zero. Thus in both cases
\(\arg(1-SQ)\ge-v\). Furthermore
\(\arg(1-Q)<\pi/2\), while \(\phi-v\in(0,\pi/2)\)
implies \(\arg(1-YQ)<0\). All are the branches in (4).
It follows that
\[
 \Im D>\frac87-\frac{11}{175}-\frac{11}{7}
                   =-\frac{86}{175}.
 \tag{17}
\]
Since \(0\le\lambda<1/2\), (16)--(17) imply
\[
 \Re[(1-i\lambda)D]
 >\log3-\frac{43}{175}
 >\frac{132}{175}>\frac34.
 \tag{18}
\]
Here \(\log3>1\) follows from the elementary bound \(e<3\).
The argument applied to every point of the containing rectangle,
so it applies to each minimizing radius and endpoint angle in
(10). The case \(\lambda=0\) is included by the same inequalities;
none of the logarithms vanishes for \(x>0\). \(\square\)

## 5. The remaining comparison and finite-source requirements

If both functions in (13) are nonnegative throughout the stated
rectangle, integration of (14) would compare the entire proposed
left contour with its already controlled endpoint at
\(q=c+ih_q\). The phase has a continuous limit as \(x\downarrow0\),
because the lower-half-plane primitive \(g_-(q)\) tends to zero
there. Lemma 2 settles \(0<x\le1/100\). The remaining criterion
is positivity on the fixed compact rectangle
\([1/100,11/50]\times[0,51/110]\). No numerical test has been
performed in this note.

Even a proof of that criterion would still need the exact contour
assembly: the actual half-grid endpoint is \(-1/(2N)\), the
finite reciprocal factorial must be bounded uniformly near zero,
and the endpoint-height change must retain its vertical difference.
The retained-index corrections and the other portions of the
outgoing boundary current are not removed by (14).
No new source asymptotic or knot-family conclusion is asserted.
