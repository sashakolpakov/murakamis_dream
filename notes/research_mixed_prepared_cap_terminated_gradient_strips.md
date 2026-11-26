# Logarithmic derivative bounds for the terminating cap formula

Research deduction, 7 November 2026. The exact terminating formula
has no logarithmic derivative with imaginary part reaching either
\(2\pi\) or \(-2\pi\) on its regular contour box. This gives
a useful comparison for simultaneous Fourier corrections. It does
not establish their required exponential gaps. The proof uses only
elementary inequalities and the previously proved domain bounds.

## 1. Domain and original logarithms

Use the exact source, phase \(\widetilde F\), and box in
[the terminating chart](research_mixed_prepared_cap_terminated_chart.md).
Thus
\[
\begin{split}
 u&\in[.1,.4]+i[-.12,.12],&
 t&\in[.22,.5]+i[-.072,.021],\\
 p,q&\in[.2,.42]+i[-.102,.015].
\end{split}
\tag{1}
\]
The fixed original Fourier parameter satisfies
\(.18299<\Re y<.18301\), with \(Y=e^{2\pi iy}\),
\(|Y|<5/8\), and \(|Ye^{-2\pi iq}|<7/10\).
All logarithms have the branches of that source theorem.
For \(0<\Re z<1\), write
\[
 A(z)=\arg\sin(\pi z)\in(-\pi/2,\pi/2).
\]
This follows because the real part of the sine is positive.
For \(0<\Re z<1/2\),
\[
 A(z)=\arctan\bigl(\cot(\pi\Re z)\tanh(\pi\Im z)\bigr).
\tag{2}
\]
The corresponding cosine argument is
\(-\arctan(\tan(\pi\Re z)\tanh(\pi\Im z))\).

**Proposition.** On (1),
\[
 |\Im\partial_j\widetilde F|<2\pi
                   \qquad(j=u,t,p,q).
\tag{3}
\]
The inequalities have a common positive margin and persist on a
sufficiently small fixed neighborhood of the original parameters.

## 2. The three outer derivatives

The exact formulas, after writing
\(g'(z)=\Log(2\sin\pi z)+i\pi/2-i\pi z\), give
\[
\begin{split}
 \Im\widetilde F_t
   &=A(u+t)+A(t+p)-3A(t)
                   +\pi(-1/2-\Re u+\Re t+\Re p),\\
 \Im\widetilde F_p
   &=A(t+p)+A(p+q)-3A(p)
                   +\pi(-1/2+\Re t+\Re p-\Re q),\\
 \Im\widetilde F_q
   &=A(p+q)-A(q)+\pi(2\Re y-\Re p)
                   -\arg(1-Ye^{-2\pi iq}).
\end{split}
\tag{4}
\]
For each of \(t,p,q\), its real part is at least \(.2>1/6\)
and at most \(1/2\), and
\(\pi|\Im z|\le .102\pi<1/3\). Equation (2) therefore gives
\[
 |A(t)|,|A(p)|,|A(q)|<\pi/6:
 \qquad
 |\cot(\pi\Re z)\tanh(\pi\Im z)|
       <\sqrt3/3.
\tag{5}
\]
Every sum in (4) remains in the open sine strip, so its argument
has absolute value less than \(\pi/2\). The affine term in
the first line of (4) belongs to \([-.48,.32]\pi\); in the
second line it belongs to \([-.5,.22]\pi\). These bounds
prove (3) for \(t,p\).

The disk of radius \(7/10<1/\sqrt2\) centered at 1 lies
strictly between the rays of arguments \(\pm\pi/4\). Thus
\(|\arg(1-Ye^{-2\pi iq})|<\pi/4\). Also
\(|2\Re y-\Re p|<1/5\). The last line of (4) is consequently
bounded in modulus by
\((1/2+1/6+1/5+1/4)\pi=67\pi/60<2\pi\).

## 3. The Newton-index derivative

Put \(x=\Re u\), \(h=\Im u\), \(a=\Re t\),
and \(v=\Im t\). Direct differentiation of the calibrated
phase gives
\[
 \widetilde F_u
 =2\Log(2\cos\pi u)-4\Log(2\sin\pi u)
   +\Log(2\sin\pi(u+t))+i\pi(u-t+1/2).
\tag{6}
\]
Let \(k=\tanh(\pi|h|)\). The elementary inequality
\(\cosh(.24\pi)<13/10\), already used in the chart's
curvature proof, implies
\[
 k^2<3/23<9/64,
 \qquad k<3/8.
\tag{7}
\]
For \(b=\tan(\pi x)\), define
\[
 D_k(b)=4\arctan(k/b)+2\arctan(kb).
\tag{8}
\]
Its derivative, for \(k>0\), has the sign of
\((1-2k^2)b^2-(2-k^2)\). It has at most one critical
point, a minimum. Thus its maximum on any interval is at an
endpoint.

Write \(b_0=\tan(\pi/10)\). The exact cosine of \(\pi/5\)
gives \(b_0<1/3\) and \(b_0^{-1}<10/3\). Hence
\[
 \arctan(kb_0)<1/8<\pi/24,
 \qquad
 \arctan(k/b_0)<\arctan(5/4)<7\pi/24.
\tag{9}
\]
For the last comparison use
\(\arctan(5/4)=\pi/4+\arctan(1/9)\) and
\(1/9<\pi/24\). On
\(b\in[b_0,b_0^{-1}]\), the larger endpoint in (8) is
\(b_0\). On \(b\in[1,b_0^{-1}]\), compare its two endpoints;
at 1 use \(k<3/8<\tan(\pi/8)\). We obtain
\[
 D_k(b)<5\pi/4\quad(.1\le x\le.4),
 \qquad
 D_k(b)<3\pi/4\quad(.25\le x\le.4).
\tag{10}
\]
The case \(k=0\) is immediate.

Let \(C=A(u+t)\) and \(d=x-a+1/2\). Then
\(.1\le d\le.68\), \(|C|<\pi/2\), and (6) becomes
\[
 \Im\widetilde F_u
   =-\operatorname{sgn}(h)D_k(b)+C+\pi d.
\tag{11}
\]
If \(h\ge0\), (10)--(11) place this strictly between
\(-1.65\pi\) and \(1.18\pi\). Suppose \(h<0\).
The lower bound is greater than \(-.4\pi\). If \(C\le0\),
the upper bound is less than \(1.93\pi\).

It remains to treat \(h<0\), \(C>0\). If \(h+v>0\),
then \(|h|<.021\). In this case
\(k<.021\pi<1/14\), so both arctangents in (8) are
less than \(\arctan(5/21)<\pi/12\). Thus \(D_k<\pi/2\),
and (11) is less than \(1.68\pi\).

In the remaining case \(h+v<0\), positivity of \(C\)
forces \(x+a>1/2\). If \(x\le1/4\), this gives
\(d<2x\le1/2\). Also \(a\le1/2\) gives
\[
 |\cot(\pi(x+a))|\le\tan(\pi x)\le1,
 \qquad C<\pi/4.
\]
Together with (10), these imply
\(\Im\widetilde F_u<5\pi/4+\pi/4+\pi/2=2\pi\).
If \(x\ge1/4\), use the second inequality of (10) instead;
the upper bound is less than
\((.75+.5+.68)\pi=1.93\pi\).
This exhausts the possible signs and proves (3) for \(u\).
The closed box is compact, all branches are regular, and every
bound is strict. Continuity proves the final assertion of the
proposition.

## 4. Consequence for paid Fourier heights

For a real point \(x\) in the box and an allowed height vector
\(v\), set
\[
 W(x,v)=\Re\widetilde F(x+iv)-2\pi\sum_j|v_j|.
\tag{12}
\]
Within either sign of a height coordinate,
\[
 \frac{\partial W}{\partial |v_j|}
 =-\operatorname{sgn}(v_j)\Im\widetilde F_j-2\pi<0.
\tag{13}
\]
Consequently resetting an additional paid height to zero can only
increase this upper rate. Every combination of horizontal aliases
is bounded by a corresponding single-coordinate alias, with the
other three coordinates at height zero. This reduces the relevant
maxima to eight scalar-domain comparisons, but establishes none
of their signs relative to the original critical action.

There is an important qualification for a proposed full contour
argument. The previously proved six outer-face bounds concern the
source with its first cap already summed. They are not automatically
bounds for the absolute Newton rows of the new formula. Such rows
cannot be substituted on connecting contours without a proof.
The present result is a derivative and height-comparison lemma,
not a completed source asymptotic.
