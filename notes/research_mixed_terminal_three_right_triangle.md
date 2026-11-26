# The entire real right triangle reduces to one half-period face

Research deduction, 5 November 2026. A strict entropy-envelope
inequality reduces every original real row with transform index
\(i/N\ge1/2\) to a single raw face at \(t=1/2\).
The external factor remains its exact zero-safe product; no branch
of \(g(a+t)\) is continued across a divisor. Thus one calibrated
half-face comparison would suppress the whole right triangle by a
positive-majorant estimate. That comparison is a stated hypothesis
here. There is no source computation or new root enclosure in the
argument.

## 1. Original rows and their reflected entropy

Retain the exact type-three terminal source from
[the Newton reduction](research_mixed_terminal_three_newton_reduction.md):
\[
 \mathcal V_{0,N}(w,X)
 =N\sum_{i+l<N}(-q)^{-l}e_l(w)
       \frac{X^{-i}p_i(X)P_{i+l}}{P_i^3P_l^2}.
 \tag{1}
\]
The variables are \(r=e^{-2\pi i/N}\), \(q=e^{\pi i/N}\),
\(P_j=(r;r)_j\), \(p_i(X)=(rX;r)_i\), and
\(X=e^{-2\pi ia}\). Write
\[
 a=y+iH\in[.22,.45]+i[-.12,.12],\qquad
 t=i/N,\quad u=l/N,
 \quad 1/2\le t<1,\quad 0\le u<1-t.
 \tag{2}
\]
All original support zeros and both level parities are included.
In particular \(u<1/2\) in this entire triangular sector.

Put \(L(x)=-J(x)\) for \(0\le x\le1/2\), using its
continuous endpoint values. The exact external numerator and chirp
have the continuous rate
\[
 Q_a(t)=\int_0^t\log|1-e^{-2\pi i(a+s)}|\,ds-2\pi Ht
       =\int_0^t\log|e^{-2\pi H}-e^{-2\pi i(y+s)}|\,ds.
 \tag{3}
\]
The zero-safe uniform estimates in
[the high-Newton theorem](research_mixed_terminal_three_high_newton.md)
and [the low-Newton theorem, equation (4)](research_mixed_terminal_three_low_newton.md)
give the complete-color double-row rate
\[
 R(a;t,u)=-2J(1/2-u)-4J(u)+J(t+u)-3J(t)+Q_a(t).
 \tag{4}
\]
This is an upper rate at product zeros, not a relative symbol there.
It is continuous up to the real support wall. It retains the full
ordinary Newton entropy, the three transform factorials, the two
additional Newton factorials and the chirp.

Set \(v=1-t\). Reflection \(J(1-x)=-J(x)\) rewrites (4) as
\[
\begin{split}
 R(a;1-v,u)&=F(v,u)+Q_a(1-v),\\
 F(v,u)&=2L(1/2-u)+4L(u)+L(v-u)-3L(v),\\
 &\hspace{35mm}0\le u\le v\le1/2.
\end{split}
 \tag{5}
\]
The height and external angle occur only in \(Q_a\); they are
not released from the original product or optimized independently
inside the entropy calculation.

## 2. A strict derivative bound for the optimized entropy

For \(0<v\le1/2\), define
\[
                     M(v)=\max_{0\le u\le v}F(v,u).
 \tag{6}
\]
The maximizer is unique and lies strictly between zero and \(v\).
Indeed, with \(x=\pi u\), \(z=\pi(v-u)\),
\[
\begin{split}
 F_u&=2\log(2\cos x)-4\log(2\sin x)+\log(2\sin z),\\
 F_{uu}&=-\pi(2\tan x+4\cot x+\cot z)<0.
\end{split}
 \tag{7}
\]
The first derivative tends to \(+\infty\) at \(u=0\)
and to \(-\infty\) at \(u=v\). Thus the implicit function
theorem and the envelope derivative apply on \(0<v<1/2\),
with a one-sided limit at \(v=1/2\).

**Lemma 1.** Throughout this interval,
\[
                           M'(v)>\log4.
 \tag{8}
\]

*Proof.* Let \(V=\pi v\), and let \(x_*\),
\(z_*=V-x_*\) denote the maximizing angles. Equation (7) gives
\[
             \sin z_* =\frac{2\sin^4x_*}{\cos^2x_*}.
 \tag{9}
\]
For \(0<V<\pi/2\), put \(s=\sin V\),
\(z_0=\arcsin(s^3)\), and \(x_0=V-z_0\). All are in
their positive real ranges, and
\[
\begin{split}
 \sin x_0
 &=s\sqrt{1-s^2}\bigl(\sqrt{1+s^2+s^4}-s^2\bigr)\\
 &<s\sqrt{1-s^2}.
\end{split}
 \tag{10}
\]
The strict inequality uses \(\sqrt{1+s^2+s^4}<1+s^2\).
Consequently
\[
 \frac{2\sin^4x_0}{\cos^2x_0}
 <\frac{2s^4(1-s^2)^2}{1-s^2+s^4}<s^3=\sin z_0.
 \tag{11}
\]
For the second inequality, the maximum of
\(2s(1-s^2)\) on \([0,1]\) is
\(4/(3\sqrt3)<1\). Thus
\(2s(1-s^2)^2<1-s^2<1-s^2+s^4\).

By (7), the derivative \(F_u\) is positive at \(x_0\).
Strict concavity therefore forces \(x_*>x_0\), and hence
\(\sin z_*<\sin z_0=s^3\). Differentiating (6) at its
stationary maximizer now gives
\[
 M'(v)=3\log(2\sin V)-\log(2\sin z_*)
       =\log\frac{4\sin^3V}{\sin z_*}>\log4.
 \tag{12}
\]
At \(V=\pi/2\), the maximizer remains interior, so
\(\sin z_*<1=\sin^3V\); the same strict one-sided formula
holds. This proves (8). \(\square\)

The comparison is at the coupled optimizing row. No concavity of
\(M\) itself, or independent substitution for the two angles in
(9), is required. Also \(M(v)\to0\) as \(v\downarrow0\),
by uniform continuity of (5) on its shrinking triangle.

## 3. The zero-safe full-triangle transport

The function \(Q_a(t)\) is absolutely continuous in \(t\).
At almost every \(t\),
\[
 Q_a'(t)=\log|e^{-2\pi H}-e^{-2\pi i(y+t)}|
       \le\log(1+e^{.24\pi})<\log(63/20).
 \tag{13}
\]
The last inequality is the elementary bound
\(e^{.24\pi}<43/20\), already proved in
[the physical cap extension, equation (7)](research_mixed_physical_three_cap_right_extension.md).
An external zero has only an integrable logarithmic singularity; no
lower bound for the product is needed.

It follows from (8) and (13), on every compact subinterval of
\(0<v\le1/2\), that
\[
 \frac{d}{dv}\{M(v)+Q_a(1-v)\}>\lambda,
                    \qquad \lambda=\log(80/63)>0
 \tag{14}
\]
almost everywhere. Integrating, and then using continuity at the
remaining endpoint, proves the following pointwise rate theorem.

**Theorem 2.** For every target (2) and every real supported row,
\[
 R(a;t,u)\le M(1/2)+Q_a(1/2)-\lambda(t-1/2),
          \qquad 1/2\le t\le1,\quad 0\le u\le1-t.
 \tag{15}
\]
In particular the maximum of the whole right triangle is attained on
the half-period face. This is a bound on each original absolute row;
it is valid for any restriction of that real triangular sector.

At the half face,
\[
 F(1/2,u)=3L(1/2-u)+4L(u).
 \tag{16}
\]
Its unique maximizing \(u_\circ\) is independent of the external
target and reference. It lies in \((1/10,2/5)\): (7) is positive
at \(u=1/10\) and negative at \(u=2/5\), using
\(\cos(\pi/10)>9/10\), \(\sin(\pi/10)<1/3\),
\(\cos(2\pi/5)<1/3\), and \(\sin(2\pi/5)>9/10\).
Its exact equation is
\[
 \cos^3(\pi u_\circ)=2\sin^4(\pi u_\circ),
 \qquad 4p^4=(1-p)^3,\quad p=\sin^2(\pi u_\circ).
 \tag{17}
\]
Thus the remaining scalar maximum in (15) is precisely the raw
face \(t=1/2\), \(u\in[.1,.4]\). At that face
\(\Re(a+t)\in[.72,.95]\), so (4) agrees with the original
regular phase \(\Re\mathcal T(a;1/2,u)\), with its unchanged
logarithmic lift and allocation.

## 4. One calibrated comparison would suppress the entire finite sector

Let \(a_*=A+iH\) be an actual type-three terminal reference,
\(a=y+iH\), and let \(B_0(a_*;y)\) be its original
quadratic supporting plane, as in
[the twelve-family reduction, equation (3)](research_mixed_terminal_three_alias_reduction.md).
The only additional calibrated comparison needed here is
\[
 \Re\mathcal T(y+iH;1/2,u)
       \le B_0(a_*;y)-\delta_R
 \quad (y\in P,\ u\in[.1,.4]),
                    \qquad\delta_R>0.
 \tag{18}
\]
It is not one of the twelve alias tests: both index heights in (18)
are zero and there is no frequency penalty. A test of (18) may use
all original reference witnesses, but no such pass is assumed in this
note. The universal optimizer (17) permits a fixed Newton trial;
strict-concavity certification over the two real targets is another
valid way to check it.

**Corollary 3.** Suppose (18) holds uniformly on the stated reference
family. The positive majorant of the literal part of (1) with
\(i/N\ge1/2\), including its entire physical Newton support,
then has allocated finite upper rate
\[
                    B_\nu(a_*;y)-\delta'
        \qquad\text{for every }0<\delta'<\delta_R,
 \tag{19}
\]
on a sufficiently small fixed ordinary-color disk, for all sufficiently
large \(N\). Both parities and each fixed ordinary-color derivative
are included. Here \(\nu\) is the external type minus three,
and \(B_\nu\) retains its original Fourier halfweight.

*Proof.* Equations (15)--(18) bound every original complete-color row
by \(B_0-\delta_R-\lambda(t-1/2)\). The uniform whole-color
Newton estimate, sine-factorial estimates up to their endpoints, and
zero-safe external product bound cited after (4) supply the same
finite upper rate with any prescribed fixed positive tolerance.
Every denominator factorial index is below \(N\). The exact
support wall and any odd-level Newton zeros remain present; no
division by a Newton value or numerator product occurs. The literal
factor \(N\) and at most \(N^2\) double rows add only a polynomial
prefactor. Choose the total tolerance below \(\delta_R-\delta'\).

For fixed ordinary derivatives, apply Cauchy's formula to each
original Newton polynomial on a smaller fixed disk before summing its
absolute value. This preserves the positive-majorant statement and
permits arbitrary restrictions of the sector. If \(\nu=1\),
the actual external height is negative. Its original halfweight rate
\(-\Re g(y+iH)/2\), together with horizontal convexity of
\(\Re g\), subtracts a nonnegative Bregman remainder from the
bare defect. Thus it gives exactly the allocated plane in (19).
The external factor is independent of the ordinary color and is
counted once. \(\square\)

This theorem replaces every far-right interior row optimization by
the single new face (18), without changing the finite source or
requiring an off-grid transform contour. It does not prove (18), a
type-four terminal analogue, or noncancellation of the full projected
invariant. The previously proved coherent right-band estimate and
its alias inputs remain valid independently.
