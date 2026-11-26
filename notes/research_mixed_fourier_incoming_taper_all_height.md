# Incoming right-taper transport on the original retained contours

Research deduction, 7 November 2026. On the right taper, raising
an unselected negative incoming height cannot increase the original
allocated incoming phase at any retained contour height. This
includes the positive retained aliases and their vertical joins.
The stronger negative-height estimate remains available on the
main and lower contours.

The phase and compact-profile estimates transport the incoming
height and, at positive retained heights, the incoming real target.
The complete assembled currents, their infinite ends and the
compensated tangent comparison remain separate.

Keep the original phase component
\[
 \mathcal J_\eta(s,a)
   =g(s+a)-(1+\eta/2)g(a)+2\pi ias,\qquad
                  \eta\in\{0,1\},
 \tag{1}
\]
from [incoming height transport](research_mixed_fourier_incoming_height_transport.md).
Let
\[
 s=u+iv,\quad u\in[1/8,1/2],\ v\in\mathbb R,\qquad
 a=x+ih,\quad x\in[.45,.5],\ h\le0 .
 \tag{2}
\]
Every branch is the original factorial branch: on
\(0<\Re z<1\), its derivative is
\(g'(z)=\Log(1-e^{-2\pi iz})\), continued from the original
lower-half-plane primitive. The boundary value at \(\Re z=1\)
is taken from the left.

**Lemma 1.** For \(c\le h\le0\),
\[
 \boxed{\quad
 \Re\mathcal J_\eta(u+iv,x+ih)
 \le\Re\mathcal J_\eta(u+iv,x+ic)
       -\pi(1-\eta/2)(.5-x)(h-c).
 \quad}
 \tag{3}
\]

*Proof.* First suppose \(u+x<1\). Write \(t=u+x\).
Then \(1/2<t<1\), and for every \(R>0\),
\[
 \pi(1-2t)<\Arg(1-Re^{-2\pi it})<0.
 \tag{4}
\]
Indeed \(1-Re^{-2\pi it}\) lies in the lower half-plane.
Its argument decreases continuously from zero to
\(\pi-2\pi t\) as \(R\) increases from zero to infinity:
its derivative is
\(\sin(2\pi t)/|1-Re^{-2\pi it}|^2<0\).
No upper bound on \(R=e^{2\pi(v+h)}\) was used.
For the incoming argument itself, \(e^{2\pi h}\le1\) and
\[
 0\le\Arg(1-e^{2\pi h}e^{-2\pi ix})
                      \le\pi(1/2-x).
 \tag{5}
\]
Differentiate (1) in \(h\), preserving the chirp:
\[
 \begin{split}
 \partial_h\Re\mathcal J_\eta
 &=-\Arg(1-e^{-2\pi i(s+a)})
       +(1+\eta/2)\Arg(1-e^{-2\pi ia})-2\pi u\\
 &\le\pi(2u+2x-1)
       +(1+\eta/2)\pi(1/2-x)-2\pi u\\
 &=\pi(1-\eta/2)(x-1/2)\le0.
 \end{split}
 \tag{6}
\]
Integration proves (3).

The only excluded real corner is \(u=x=1/2\). Put \(T=v+h\).
The exact reflected factorial phase has the continuous boundary
values
\[
              \Re g(1+iT)=\pi T_+,\qquad
              \Re g(1/2+ih)=0\quad(h\le0).
 \tag{7}
\]
For \(T<0\), the first equality follows from the real
dilogarithm of \(e^{2\pi T}\); for \(T>0\), it follows from
the original reflection
\(g(z)=\overline{g(\bar z)}+i\pi(z-z^2)\)
in real part. Constants have zero real contribution here.
Both limits agree at \(T=0\).
Thus (1) at this corner has real part
\[
                    \pi T_+-\pi T=\pi(-T)_+,
 \tag{8}
\]
which is nonincreasing in \(h\). This proves (3) at the
corner as well, including the isolated factorial-zero limit.
It does not differentiate a logarithm at that zero. \(\square\)

For \(v\le0\), the stronger bound in the preceding note gives
the additional decrease \(\pi(h-c)/10\). For \(v>0\),
(3) is still nonpositive, even when the upper factorial radius
exceeds one. All other terms of the original bare Fourier-cap
phase, and every retained cotangent alias penalty, are independent
of the incoming \(h\). Their complete central phase profiles
therefore obey the same transport inequality at fixed \(x,u,v,q\).

This covers the actual unselected type-four height
\(h=400(.5-x)^2c\), since its original \(c<0\), and any
incoming type-three case with \(c\le0\). The true incoming
halfweight remains on its absolute factorial upper-rate branch
through \(h=0\); no finite Fourier factor is divided out.
The low physical rows with \(u<1/8\) have not been included
in the lemma.

## Positive retained heights also have a favorable real direction

**Lemma 2.** If \(v\ge0\), \(h\le0\), and the other variables
are in (2), then \(x\mapsto\Re\mathcal J_\eta(u+iv,x+ih)\)
is nonincreasing on \([.45,.5]\).

*Proof.* Put \(R_a=e^{2\pi h}\le1\), \(t=e^{-2\pi v}\le1\).
The original chirp cancels the radial factor from the first
logarithm exactly, giving
\[
 \partial_x\Re\mathcal J_\eta
 =\log|t-R_a e^{-2\pi i(x+u)}|
       -(1+\eta/2)\log|1-R_a e^{-2\pi ix}|.
 \tag{9}
\]
The squared numerator is convex in \(t\in[0,1]\), so it is
at most
\[
            \max\{R_a^2,|1-R_a e^{-2\pi i(x+u)}|^2\}.
 \tag{10}
\]
Here \(u\ge1/8>1-2x\), hence
\[
 x+u\in[1-x,1+x],\qquad
              \cos(2\pi(x+u))\ge\cos(2\pi x).
 \tag{11}
\]
The second term of (10) is at most the squared own denominator
in (9). That denominator exceeds one, because
\(\cos(2\pi x)<0\), and therefore also exceeds \(R_a\).
Thus
\[
 \partial_x\Re\mathcal J_\eta
       \le-\frac{\eta}{2}\log|1-R_a e^{-2\pi ix}|\le0.
 \tag{12}
\]
At the isolated numerator zero \(u=x=.5,\ v+h=0\),
the logarithmic divergence of (9) is integrable.
The continuous factorial phase and absolute continuity from the
left prove the same monotonicity there. \(\square\)

Let \(b=.45\) and \(c\le h\le0\). Applying Lemma 2 at
height \(c\), then Lemma 1 at the new \(x\), gives
\[
 \Re\mathcal J_\eta(u+iv,x+ih)
 \le\Re\mathcal J_\eta(u+iv,b+ic)
       -\pi(1-\eta/2)(.5-x)(h-c)
              \qquad(v\ge0).
 \tag{13}
\]
Consequently every original positive-height phase profile whose
other variables are held fixed is bounded by its own profile at
the incoming plateau endpoint. This includes its original
retained alias penalty, which is independent of \(a\).

## The new numerator wall has a uniform finite upper bound

The only new central factorial wall is \(s+a=1\). It is a
numerator, not a pole. A direct finite product keeps its zero
and supplies the upper estimate needed on compact contours.
Write \(\Pi_N\) for the exact cyclotomic factorial.
For each fixed \(T<\infty\), there are \(C_T,A_T\) such that
\[
 |\Pi_N(w)|\le C_TN^{A_T}e^{N\Re g(w)}
 \quad\left(\frac{11}{20}\le\Re w\le1,\quad|\Im w|\le T\right)
 \tag{14}
\]
at all sufficiently large levels, using the same one-sided
branch at \(\Re w=1\).

To prove this, take \(m=\lfloor N/4\rfloor\) and use the exact
recurrence without dividing a factor:
\[
 \Pi_N(w)=\Pi_N(w-m/N)
       \prod_{k=0}^{m-1}
                 (1-e^{-2\pi i(w-k/N)}).
 \tag{15}
\]
For \(N\ge20\), the initial real part lies in \([.30,.80]\).
The original
[regular-strip factorial packet](exact_factorial_interpolation_and_complex_contours.md)
therefore applies
uniformly to \(\Pi_N(w-m/N)\) on its fixed compact height range.
The zero-safe truncated-log product estimate used in
[the retained-rate proof](research_mixed_fourier_right_cap_coherent_retained_rate.md),
equation (7), bounds the second factor by
\[
 N^{A_T}
 \exp\left\{N\int_0^{m/N}
               \log|1-e^{-2\pi i(w-t)}|\,dt\right\}.
 \tag{16}
\]
The proof works for radii on either side of one: the only
logarithmic singularity is integrable, the truncation has
\(O(\log N)\) variation, and an exact zero only improves the
upper bound. On the chosen original branch the integral is
\(\Re\{g(w)-g(w-m/N)\}\), by \(g'=\Log(1-e^{-2\pi iz})\).
This proves (14), including the continuous wall limit.

In a central cap row, all other incoming factors stay on their
old regular strips, while the incoming Fourier halfweight has
its true absolute upper rate on \(h\le0,\ x\le.5\).
Thus (14) supplies the only new compact numerator qualification
for the phase transports (3), (13). Half-grid real cuts have
the same property for all sufficiently large levels:
their upper endpoint is at most \(1/2\), and their lower
endpoint eventually exceeds \(1/10\), which suffices for
(11). No zero of the numerator or of a diagonal Fourier
polynomial is divided out.

These are uniform compact **profile** upper estimates.
They do not by themselves compare moduli of two canceled
complete currents. In particular the known right-current
assembly contains a separate replacement path with negative
retained height; Lemma 2 does not apply on that part. Its
incoming real-direction comparison and every infinite-end
bound must still be checked in the exact assembled identity.
The original complex marginal against the new target, recorded
in incoming height transport, equation (19), also remains.
Neither a whole positive-group bound on the new taper nor the
sign of its joint compensated bracket is inferred by omitting
these terms.
