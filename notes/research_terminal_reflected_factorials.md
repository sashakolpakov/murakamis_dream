# Factorial continuation for terminal-filling contours

Research note, 2 November 2026. The first two sections prove identities
and uniform expansions for the exact factorial used in the finite
source. The last section gives a rigorously enclosed counterexample
to concavity of a proposed contour. These results help specify a
contour argument; they do not supply the missing global estimate for
terminal powers of absolute value at least three.

## 1. Exact reflection across the first factorial zero

Fix an integer $N\ge3$ and put $d=N-1$. We use the canonical factorial
from [the interpolation lemma](../papers/conway-asymptotics/factorial.tex):

\[
 G_N(z)=\left(\frac{2\pi}{N}\right)^z\Gamma(z+1)
 \prod_{a=1}^{\infty}
 \frac{\Gamma(Na+z+1)}{\Gamma(Na-z)(Na)^{2z+1}}.
 \tag{1}
\]

The powers in this formula have positive real bases. In its original
strip, $-1<\Re z<N$, it is holomorphic and nonzero. Its exact shift
and reflection identities are

\[
 G_N(z+1)=2\sin\frac{\pi(z+1)}N\,G_N(z),
 \qquad G_N(z)G_N(d-z)=N.                         \tag{2}
\]

The shift identity continues $G_N$ meromorphically. Iterating it $N$
times and using the finite sine product gives

\[
 G_N(z+N)=-2\sin(\pi z)G_N(z).                    \tag{3}
\]

For example, the sine product is first evaluated on $-1<\Re z<0$,
where all intermediate factors are in the original strip; equality
elsewhere follows by meromorphic continuation. Substituting
$d-z=N+(-z-1)$ into (2) and then using (3) yields

\[
 G_N(z)G_N(-z-1)=-\frac{N}{2\sin(\pi z)}.
\]

Consequently, for every complex $w$, as an identity of meromorphic
functions,

\[
 \boxed{\quad
 \frac1{G_N(Nw-\tfrac12)}
   =\frac{2\cos(\pi Nw)}N\,G_N(-Nw-\tfrac12).
 \quad}                                                   \tag{4}
\]

This formula is particularly useful when the real part of a denominator
factorial becomes negative. It retains the two exponential terms in
the cosine. No new choice of a periodic multiplier is permitted in
(4): both sides refer to the function fixed by (1).

## 2. Uniform expansion above and below the negative real axis

Let

\[
 J(w)=\int_0^w\log(2\sin(\pi v))\,dv
\]

on $0<w<1$, continued to the upper or lower half-plane as appropriate.
We write $J_+$ for continuation above the negative real axis and
$J_-$ for continuation below it. In particular, when $-1<\Re w<0$,

\[
 J_+(w)=-J(-w)+i\pi w\quad(\Im w>0),\qquad
 J_-(w)=-J(-w)-i\pi w\quad(\Im w<0).                 \tag{5}
\]

Here $J(-w)$ is continued from the positive interval. The signs in
(5) follow from the boundary values of the logarithm of a negative
real number; differentiation and the value at zero fix the
integration constant.

On each compact subset of
$\{-1<\Re w<1,\ \Im w>0\}$, one has

\[
 G_N(Nw-\tfrac12)
 =\sqrt N\,
 \exp\left\{
       NJ_+(w)-\frac{\pi\cot(\pi w)}{24N}
                    +O(N^{-3})\right\}.            \tag{6}
\]

The analogous formula below the real axis uses $J_-$. On the
positive real part of these domains the branch agrees with the
usual bulk expansion. The error is uniform on compact sets, as
are its fixed derivatives on smaller compact sets.

Here is a direct derivation, including the continuation across
$\Re w=0$. At the midpoint argument, (1) reads

\[
 \left(\frac{2\pi}{N}\right)^{Nw-1/2}
 \Gamma(Nw+\tfrac12)
 \prod_{a=1}^{\infty}
 \frac{\Gamma(N(a+w)+\tfrac12)}
      {\Gamma(N(a-w)+\tfrac12)(Na)^{2Nw}}.          \tag{7}
\]

On a fixed compact set in the upper domain, the arguments $w$ and
$a\pm w$ stay in closed sectors avoiding the negative real axis.
The half-integer Stirling formula is therefore uniform:

\[
 \log\Gamma(Nv+\tfrac12)
 =Nv(\log(Nv)-1)+\tfrac12\log(2\pi)
            -\frac1{24Nv}+O(N^{-3}|v|^{-3}).
\]

The error can be summed over $a$. The leading exponent in (7) is
$N P(w)$, where

\[
 P(w)=w(\log(2\pi w)-1)
 +\sum_{a\ge1}
 \left[
 (a+w)\log(1+w/a)-(a-w)\log(1-w/a)-2w
 \right].
\]

The series and its derivatives converge on smaller compact sets.
Euler's sine product gives

\[
 P'(w)=\log(2\pi w)+\sum_{a\ge1}\log(1-w^2/a^2)
      =\log(2\sin(\pi w)).
\]

Thus $P=J_+$, by continuation from the positive interval. The
constant factors in (7) leave exactly $\sqrt N$, and the first
correction is

\[
 -\frac1{24N}
 \left[\frac1w+\sum_{a\ge1}
   \left(\frac1{a+w}-\frac1{a-w}\right)\right]
 =-\frac{\pi\cot(\pi w)}{24N}.
\]

This proves (6). The same argument gives further fixed orders if
needed. It uses the usual sectorial Gamma expansion, whose standard
statement is in [DLMF, Section 5.11](https://dlmf.nist.gov/5.11).

There is also a useful form that exposes the exponentially smaller
term. On a compact set with $-1<\Re w<0$ and $\Im w>0$, substitute
the ordinary bulk expansion at $-w$ into (4):

\[
 \frac1{G_N(Nw-\tfrac12)}
 =N^{-1/2}e^{-NJ_+(w)}
   \bigl(1+e^{2\pi iNw}\bigr)
   \exp\left\{\frac{\pi\cot(\pi w)}{24N}
                         +O(N^{-3})\right\}.       \tag{8}
\]

The second term in parentheses has modulus $e^{-2\pi N\Im w}$.
For a compact negative real interval the same expression follows
directly from (4) and remains uniform as $\Im w$ tends to zero,
provided both terms are retained. The relative expansion in (6),
in contrast, is asserted only away from the negative real cut.
Deleting the second term at the cut would destroy the exact
factorial zeros.

For the edge interpolation, the denominator that first changes sign
has normalized argument

\[
 w=\frac12-x-\frac{t}{2\pi}.
\]

At the translated three-crossing saddle, write

\[
 h_x=\frac{\log2}{4\pi},\qquad
 h_t=2\operatorname{arsinh}
            \sqrt{\frac{\sqrt2-1}{4}},
 \qquad x=\xi+ih_x,\quad t=\tau-ih_t.               \tag{9}
\]

Then $\Im w=h_t/(2\pi)-h_x>0$. To check the strict inequality
algebraically, compare

\[
 \frac{\sqrt2-1}{4}
   >\sinh^2\!\left(\frac{\log2}{4}\right)
   =\frac{3\sqrt2-4}{8}.
\]

Thus (6) supplies a uniform expansion through $\Re w=0$ on compact
parts of this translated contour. On a connecting surface that
scales both imaginary shifts by a parameter tending to zero, (4)
or (8) retains the extra term when it is no longer exponentially
small. Estimates for that term and for the connecting surface
are still required.

## 3. The translated phase is not concave on its whole central domain

For the original two-variable phase at parent angle zero, put

\[
 \Phi_n(x,t)=b(x,t)+b(x,0)+\frac{in}{4\pi}t^2-it,
 \qquad
 b(x,t)=\int_0^x\log(2\cos(2\pi v)+2\cos t)\,dv-2J(x).
\]

On a horizontal translated contour, its real Hessian has entries
equal to the real parts of

\[
 \begin{aligned}
 H_{xx}&=-\frac{2\pi\sin(2\pi x)}{\cos(2\pi x)+\cos t}
          -4\pi\cot(\pi x)
          -\frac{2\pi\sin(2\pi x)}{\cos(2\pi x)+1},\\
 H_{xt}&=-\frac{\sin t}{\cos(2\pi x)+\cos t},\\
 H_{tt}&=-\frac{\tan(\pi x+t/2)+\tan(\pi x-t/2)}{4\pi}
                            +\frac{in}{2\pi}.
 \end{aligned}                                                   \tag{10}
\]

The last term has zero real part. Take $n=3$, the shifts in (9), and
the exact point

\[
 x=\frac1{200}+ih_x,\qquad t=2-ih_t.
\]

The real coordinates lie inside the central range $0<t<2\pi/3$
and inside the original triangle $x+t/(2\pi)<1/2$. Nevertheless,
rigorous ball evaluation of (10) gives

\[
 \det(\Re H)<-\frac45.
\]

Its approximate value is $-0.8645685705$. Hence the real Hessian is
indefinite there. This does not contradict the proved negative
definiteness at the selected saddle. It shows that the saddle
calculation cannot be extended to the whole translated triangle by
an assertion of global concavity.

The certificate is reproduced by

    python3 experiments/audit_terminal_translated_hessian.py

It uses exact rational and algebraic inputs and Arb enclosures;
the strict rational comparison, rather than the printed decimal,
is the certificate. No numerical maximization is used.

The [real outer-angle estimate](research_terminal_real_angle_tail.md)
discards $|t|\ge2\pi/3$ below every selected rate with $|n|\ge3$.
The example above lies in the remaining region. A successful proof
must therefore also control the small-wire boundary, use a different
contour, or establish the needed maximum without global concavity.
None of these alternatives is proved here.
