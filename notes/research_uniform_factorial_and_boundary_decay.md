# Uniform factorial bounds and decay in a free boundary angle

Research proof, 2 November 2026. This note gives upper bounds on the exact
Newton interpolation, including the places where a factorial argument
crosses zero. It also proves a decrease of the real phase in the remaining
boundary angle. These are inputs to a contour argument, not a proof that
any particular contour represents the dominant contribution.

## 1. A midpoint estimate that includes zero

Let $G_N$ be the canonical factorial in
[the factorial continuation note](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_terminal_reflected_factorials.md),
and let $J$ denote the primitive of $\log(2\sin\pi w)$ continued from
$0<w<1$. Fix $0<\delta<1$ and a finite $H>0$.

**Lemma 1.** There is a constant $C=C(\delta,H)>1$ such that, for all
$N\ge3$ and all $w$ with $0\le\Re w\le1-\delta$, $|\Im w|\le H$,

\[
 C^{-1}\sqrt N\,e^{N\Re J(w)}
 \le |G_N(Nw-1/2)|
 \le C\sqrt N\,e^{N\Re J(w)}.                          \tag{1}
\]

At $w=0$, set $J(0)=0$. The estimate includes that point.

**Proof.** Substitute $z=Nw-1/2$ into the defining Gamma product:

\[
 G_N(Nw-1/2)=
 (2\pi/N)^{Nw-1/2}\Gamma(Nw+1/2)
 \prod_{a\ge1}
 \frac{\Gamma(N(a+w)+1/2)}
 {\Gamma(N(a-w)+1/2)(Na)^{2Nw}}.                       \tag{2}
\]

Keep the first Gamma factor exact. For $z$ in the closed right
half-plane, define

\[
 Q(z)=\Gamma(z+1/2)e^z z^{-z},\qquad Q(0)=\sqrt\pi,
\]

using the principal logarithm. Its absolute value is bounded above
and bounded away from zero on that half-plane. On its intersection
with a fixed disk this follows by continuity, nonvanishing of Gamma,
and $z\log z\to0$. Outside a sufficiently large disk, the sectorial
midpoint Stirling expansion gives $Q(z)=\sqrt{2\pi}(1+O(1/|z|))$
uniformly for $|\arg z|\le\pi/2$.

In every other factor of (2), the real parts of $a\pm w$ are at
least $\delta$. Apply the same Stirling expansion there. Its first
corrections occur in the difference

\[
 -\frac1{24N}\sum_{a\ge1}
       \left(\frac1{a+w}-\frac1{a-w}\right),
\]

which is uniformly convergent because its terms are $O(a^{-2})$.
The remainders are bounded by a uniformly summable
$O(N^{-3}a^{-3})$ sequence, with the finitely many initial terms
absorbed into a constant depending on $\delta,H$. The resulting
error in the logarithm of the product is $O_{\delta,H}(1/N)$.

The leading logarithm is $NJ(w)$: differentiating its convergent
series gives Euler's product for $\log(2\sin\pi w)$, and the value
at zero fixes the integration constant. The remaining constant is
$\sqrt{N/(2\pi)}\,Q(Nw)$. Its modulus is between two positive
multiples of $\sqrt N$. This proves (1), including $w=0$.
The argument uses only the defining Gamma product and the usual
[sectorial Stirling expansion](https://dlmf.nist.gov/5.11).
$\square$

## 2. Reciprocal bounds across the negative real axis

For $\Re w<0$, choose $J_+(w)$ above the negative real axis and
$J_-(w)$ below it. Their real boundary values on the axis agree.
The exact identity from the continuation note is

\[
 \frac1{G_N(Nw-1/2)}
       =\frac{2\cos(\pi Nw)}N G_N(-Nw-1/2).             \tag{3}
\]

On the upper side,
$J_+(w)=-J(-w)+i\pi w$ and
$2\cos(\pi Nw)=e^{-i\pi Nw}(1+e^{2\pi iNw})$.
The factor in parentheses has modulus at most two. On the lower side
use the conjugate sign. Lemma 1 therefore implies the following
uniform upper estimate:

\[
 \left|\frac1{G_N(Nw-1/2)}\right|
 \le C N^{-1/2}e^{-N\Re J_{\rm side}(w)},
 \quad -1+\delta\le\Re w\le1-\delta,
 \quad |\Im w|\le H.                                  \tag{4}
\]

For nonnegative real part, $J_{\rm side}$ is the ordinary continued
branch and (4) follows directly from (1). At negative real arguments,
(3) proves the bound with both cosine terms retained. Reciprocal
factorial zeros do not cause an exception: the left side can vanish,
and (4) is an upper bound. Thus (4) does not require staying a fixed
distance from the negative real axis or from zero.

## 3. The exact Newton interpolation

Put $d=N-1$ and

\[
 B_N(x,t)=
 \frac{G_N(d/2+Nt/(2\pi))G_N(d/2-Nt/(2\pi))}
 {G_N(d/2-Nx+Nt/(2\pi))G_N(d/2-Nx-Nt/(2\pi))G_N(Nx)^2}.
\]

The numerator is exactly $N$, by $G_N(z)G_N(d-z)=N$.
At every integer $k$ with $0\le k<N$, this is the original Newton
polynomial $e_k(-2\cos t)$ when $x=k/N$.

Let $x$ range over a compact rectangle
$0<\alpha\le\Re x\le\beta<1/2$, $|\Im x|\le H_x$.
Let $t$ range over a bounded complex set on which the real parts of

\[
 w_+=\frac12-x+\frac{t}{2\pi},\qquad
 w_-=\frac12-x-\frac{t}{2\pi}
\]

stay in $[-1+\delta,1-\delta]$ for some $\delta>0$. Apply (4) to
$w_\pm$ and (1) to $x+1/(2N)$; the finitely many small levels can
be handled by increasing the constant. Since $x$ stays away from
zero and one,
$N[J(x+1/(2N))-J(x)]$ is uniformly bounded. It follows that

\[
 |B_N(x,t)|\le\frac{C}{N}\exp\{N\mathfrak b(x,t)\},
 \qquad
 \mathfrak b(x,t)=
 -\Re J_{\rm side}(w_+)-\Re J_{\rm side}(w_-)-2\Re J(x).
                                                               \tag{5}
\]

The estimate includes all moving-zero faces and their intersections.
On a contour where the chosen branches are holomorphic,
$\mathfrak b(x,t)=\Re b(x,t)$. Elsewhere (5) specifies the real
upper exponent directly, using the side approached by each argument.
One must use those same branches in a certificate for a contour face.

For a real boundary angle $u\in[-\pi,\pi]$, the conditions on
$w_\pm$ hold uniformly on the entire rectangle in $x$. Thus (5)
also supplies an exact bound on the second boundary factor throughout
the whole real angular period.

## 4. Decay in the real boundary angle

**Lemma 2.** Write $x=\xi+ih$, where $0<\xi<1/2$. For
$-\pi\le u\le\pi$ one has

\[
 \mathfrak b(x,u)-\mathfrak b(x,0)
 \le-\frac{\sin(2\pi\xi)}{4\pi\cosh^2(\pi h)}
                                  (1-\cos u).          \tag{6}
\]

**Proof.** Evenness reduces to $0\le u\le\pi$. Away from zeros,
differentiation of the continued primitive gives

\[
 \partial_u\mathfrak b(x,u)
   =\frac1{4\pi}\log\frac{A}{B},
\]

\[
 A=\cos^2(\pi\xi+u/2)+\sinh^2(\pi h),\qquad
 B=\cos^2(\pi\xi-u/2)+\sinh^2(\pi h).
\]

Here $B-A=\sin(2\pi\xi)\sin u\ge0$ and
$B\le\cosh^2(\pi h)$. Hence

\[
 \partial_u\mathfrak b(x,u)
 \le-\frac{\sin(2\pi\xi)\sin u}{4\pi\cosh^2(\pi h)}.
\]

Integrating proves (6). When $h=0$, an interior zero of $A$ gives
an integrable logarithmic singularity. Apply the argument on the
two sides of that point and pass to the continuous primitive; no
bound on the pointwise logarithm at the zero is required. $\square$

In particular, on the fixed wire rectangle there is $c>0$ such that

\[
 |B_N(x,u)|\le\frac{C}{N}
   \exp\!\left[N\{\mathfrak b(x,0)-c(1-\cos u)\}\right]
 \qquad(-\pi\le u\le\pi).                             \tag{7}
\]

This applies to positive and negative wire heights and to every
intermediate height on a connecting surface. If a complete contour
argument bounds the remaining factors at the selected rate when
$u=0$, (7) supplies the extra real-boundary loss on the same contour.
It does not supply the missing contour argument or its nonzero
leading coefficient. Its role is to make that argument usable after
the terminal tangle is glued to another tangle.
