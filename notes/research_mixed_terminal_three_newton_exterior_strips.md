# Bounding the Newton-index strips outside the central rectangle

Research deduction, 5 November 2026. The lower and upper Newton-index
strips can be estimated by moving their phase to the nearest horizontal
edge of the central rectangle. Only the transform index is deformed;
the Newton index remains a real summation index. The monotonicity and
the estimate near the half-level are proved here. The contour estimate
uses two of the explicit alias comparisons in the
[twelve-family criterion](research_mixed_terminal_three_alias_reduction.md).
It is conditional on those comparisons until their certificate is complete.
This note makes no estimate for the remaining region with transform
index greater than half the level.

## 1. Variables and the original finite source

Let \(a=y+iH\), with \(y\in[.22,.45]\) and \(|H|\le .12\).
The transform and Newton indices are \(t=i/N\) and \(u=l/N\).
We use the exact double summand \(\mathcal I_N(a;t,u,w)\) in
[the joint interpolation](research_mixed_terminal_three_joint_zero_mode.md),
equation (15c), including its factor \(N\). The ordinary color is
\(w\); its complete value is \(-2\). On regular compact sets the
complete-color exponential phase is
\[
\begin{split}
\mathcal T(a;t,u)={}&-2J(1/2-u)-2J(u)+g(a+t)+g(t+u)\\
 &-3g(t)-2g(u)-g(a)+i\pi u+2\pi iat,\\
g(v)&=J(v)+i\pi(v-v^2)/2,\qquad
J'(v)=\log(2\sin\pi v).
\end{split}
\tag{1}
\]
The logarithms are the original continuations on the regular sine
strips. We retain the exact support \(i+l<N\).

Write \(I_t=[.15,.50]\). For the phase comparisons in the next
section, \(t=x+ih\) may have any \(x\in I_t\), \(|h|\le .12\),
whereas \(u\) is real and lies in \((0,1/2)\). All the arguments
in (1) remain in their regular strips. Compactness is imposed before
using a finite-source asymptotic; no uniform expansion at \(u=0\)
or \(u=1/2\) is assumed.

## 2. Monotonicity toward the central rectangle

**Lemma 1.** For all the external targets and transform coordinates
just specified,
\[
\begin{array}{ll}
\partial_u\Re\mathcal T(a;t,u)>\log14,
   &0<u\le1/10,\\
\partial_u\Re\mathcal T(a;t,u)<-\log7,
   &2/5\le u<1/2.
\end{array}
\tag{2}
\]
The external variable does not enter these derivatives.

*Proof.* At real \(u\), differentiation of (1) gives
\[
\partial_u\Re\mathcal T
 =\log\left(
 \frac{(2\cos\pi u)^2}{(2\sin\pi u)^4}
 \left|1-e^{-2\pi i(t+u)}\right|\right).
\tag{3}
\]
For a positive number \(R\), minimizing
\(|1-Re^{-i\theta}|\) over \(R\ge0\) gives
\(|\sin\theta|\) when \(\cos\theta\ge0\), and \(1\)
otherwise. If \(0<u\le .1\), then
\(.15<\Re(t+u)\le .60\). Consequently the last factor in
(3) is at least \(\sin(3\pi/10)=\cos(\pi/5)>4/5\).
The inequality follows from
\(\cos(\pi/5)\ge1-(22/35)^2/2>4/5\).
Also
\[
 2\cos\pi u>19/10,\qquad 2\sin\pi u<2/3.
\tag{4}
\]
For the first inequality use
\(\cos(\pi/10)\ge1-(11/35)^2/2>19/20\);
the second follows from \(\sin x\le x\) and \(\pi<22/7\).
Thus the expression inside the logarithm exceeds
\[
 (19/10)^2(4/5)(3/2)^4>14.
\tag{5}
\]

For \(.4\le u<.5\), instead use
\[
 2\cos\pi u<2/3,\qquad 2\sin\pi u>19/10,
 \qquad |1-e^{-2\pi i(t+u)}|\le1+e^{.24\pi}<4.
\tag{6}
\]
Here \(.24\pi<1\) and \(e<3\), the latter following directly
from its factorial series. Since \((19/10)^4>13\), the expression
in (3) is less than \(16/117<1/7\). This proves (2). \(\square\)

In particular, at each fixed complex \(t\),
\[
\begin{array}{ll}
\Re\mathcal T(a;t,u)
 \le\Re\mathcal T(a;t,.1)-(\log14)(.1-u),&0<u\le .1,\\
\Re\mathcal T(a;t,u)
 \le\Re\mathcal T(a;t,.4)-(\log7)(u-.4),&.4\le u<.5.
\end{array}
\tag{7}
\]
An alias penalty depending only on \(\Im t\) can be subtracted
on both sides. This order of argument matters: transport to the
central edge first, then use height convexity there. A joint Hessian
estimate outside the central Newton interval is unnecessary.

## 3. A uniform positive bound just below half the level

The estimates of
[the upper Newton half](research_mixed_terminal_three_high_newton.md)
also control a fixed neighborhood immediately below \(u=1/2\).
This avoids any use of a regular interpolation at the zero of
\(\cos\pi u\).

**Lemma 2.** There exists \(\varepsilon_0>0\) such that the positive
double-sum majorant for the rows
\[
 1/2-\varepsilon_0\le l/N<1/2,\qquad 0\le i<N-l
\tag{8}
\]
is bounded by \(CN^A e^{879N/1000}\), uniformly over the full external
target rectangle. The bound holds on a fixed ordinary-color disk
about \(-2\), includes both level parities, and gives the same rate
for every fixed ordinary-color derivative on a smaller disk.

*Proof.* Define the continuous functions on their closed real intervals
\[
\begin{split}
E(u)&=\int_0^u\log(4\cos^2\pi s)\,ds-2J(u),\\
I_a(t)&=\int_0^t\log|1-e^{-2\pi i(a+s)}|\,ds,\\
R(u,t,a)&=E(u)+J(u+t)-2J(u)-3J(t)+I_a(t)-2\pi Ht.
\end{split}
\tag{9}
\]
This is the positive row rate for the original double summand,
not a new phase. In particular the two additional factors of \(P_l\)
are present in \(-2J(u)\); \(E\) already includes the Newton
denominator. The uniform Newton bound and the zero-safe product
estimate in Sections 2--3 of the upper-half theorem apply to (9)
on the entire closed physical triangle. They permit any prescribed
positive total rate tolerance, uniformly near the complete color.

The function \(I_a(t)\) is jointly continuous on the compact external
rectangle and \(0\le t\le1\). Indeed its only possible zeros are
simple logarithmic singularities. The regularized logarithms used
in that theorem have uniformly convergent integrals; their continuous
integrals therefore have continuous limit. The functions \(E,J\)
are continuous, including at their logarithmic endpoints. Hence
\(R\) is uniformly continuous on the compact physical triangle
times the external rectangle.

At \(u=1/2\) and \(0\le t\le1/2\), the upper-half theorem gives
\[
 R(1/2,t,a)\le\frac{95458861}{108769600}<.878.
\tag{10}
\]
For a point in (8), compare it with
\((1/2,\min(t,1/2),a)\). Both coordinates change by at most
\(\varepsilon_0\), since the physical support gives
\(t\le1-u\le1/2+\varepsilon_0\). Uniform continuity therefore
allows \(\varepsilon_0>0\), independent of \(a\), such that
the row rate is less than \(.8785\) on (8). Choose the ordinary
color disk and the finite-product tolerance to use less than \(.0005\).
The at most \(N^2\) summands and the original factor \(N\) contribute
only a polynomial factor. Cauchy's formula supplies the fixed
ordinary derivatives without division by a Newton value. \(\square\)

Thus the existing supporting-plane loss \(1/100\) for the upper
half also holds for (8), using the reference floor \(>.89\) and
the same neighboring halfweight comparison. No effective value of
\(\varepsilon_0\) is claimed or needed for this existence statement.

## 4. Exact one-variable summation on the two strips

Fix an actual terminal reference \(a_*\), its transform height
\(h_t=\Im t_*\), and the original allocated plane \(B_\nu(a_*;y)\)
from the [zero-mode completion](research_mixed_terminal_three_zero_mode_completion.md).
Let \(I_{t,N}\subset I_t\) have the same inward half-grid cuts
as the central rectangular sum. At each fixed real physical Newton
index \(u=l/N\), sum \(\mathcal I_N\) over \(i/N\in I_{t,N}\).
For either of the fixed strips
\[
 1/200\le u\le .1,\qquad
 .4\le u\le1/2-\varepsilon_0,
\tag{11}
\]
the product is regular and strictly inside \(t+u<1\).

Apply the exact one-variable residue identity to the transform
index, then deform its constant mode to height \(h_t\). It has one
shifted horizontal segment, two joins, two alias horizontal segments
at heights \(\pm.12\), and four vertical alias half-sides. There
is a literal factor \(N\) from this one residue operation; the
Newton index is still summed, not integrated.

**Proposition 3.** Assume the two transform-index single-alias
comparisons with Newton height zero from the twelve-family criterion,
each with gap \(1/2000\), as required by the alias certificate.
Then each sum over (11), with \(i/N\in I_{t,N}\), has allocated
upper rate at most \(B_\nu(a_*;y)-1/4000\), after choosing a
sufficiently small fixed ordinary-color disk and sufficiently large
\(N\). Fixed ordinary-color derivatives have the same conclusion on
smaller disks. The assertion also covers the \(O(1/N)\) strips
between the inward Newton cuts and their limiting values \(.1,.4\).

*Proof.* Transport the phase of every contour point to \(u=.1\)
or \(u=.4\) by (7). For the shifted horizontal segment, the
result is exactly a completed flattened Newton face. Its gap is
\(1/2000\). For each join, height convexity on the central edge
reduces it to that face or a completed real-real corner. For an alias
horizontal side, its weighted phase is one of the two assumed
single-alias comparisons. For a vertical alias side, convexity on
each sign half, after subtracting its linear kernel penalty, reduces
to this comparison or a completed corner. No unestimated raw face
occurs because the undeformed Newton coordinate has reached a cut.

The comparisons hold for all real transform coordinates in \(I_t\).
Moving a vertical half-grid cut from its limit changes the phase by
\(O(1/N)\). The same bounded-derivative argument handles any Newton
rows between an inward central cut and its limiting edge. The exact
interpolation is uniform on the compact strips (11), including all
these contour pieces. Small color perturbations, the bounded contour
lengths, the factors of \(N\), and the at most \(N\) Newton rows
can be paid from half the strict gap. The external halfweight is
independent of both internal variables and uses its original convex
comparison. Cauchy's formula proves the derivative statement.
\(\square\)

## 5. The two real corner regions on the left

There is also an unconditional positive bound for the two corner
regions to the left of the transform interval. Fix \(\delta>0\)
inside the already proved terminal end-index cutoff. Consider
\[
 \delta\le t\le .15,\qquad
 u\in[1/200,.1]\ \text{or}\ u\in[.4,1/2-\varepsilon_0].
\tag{12}
\]
Both indices are real in this argument.

**Proposition 4.** The positive sum of the absolute values of the
original double summands over either region (12), with its original
external allocation, has upper rate at most
\(B_\nu(a_*;y)-1/4000\). This holds on a fixed small ordinary-color
disk and for all fixed derivatives on smaller disks. The same bound
holds for the strips of width \(O(1/N)\) needed to match the inward
cuts. No alias hypothesis is used.

*Proof.* For real \(0<t\le .15\), \(0<u<.5\),
\[
 \Re\mathcal T_t
 =\log|e^{-2\pi H}-e^{-2\pi i(y+t)}|
   +\log(2\sin\pi(t+u))-3\log(2\sin\pi t).
\tag{13}
\]
The first modulus is greater than \(9/10\):
\(y+t\in[.22,.60]\) and
\(\cos(2\pi(y+t))\le\sin(.06\pi)<1/5\), so its
square exceeds \((e^{-2\pi H}-1/5)^2+24/25\).
Moreover \(u\le1-2t\), which implies
\(\sin\pi(t+u)\ge\sin\pi t\). Therefore
\[
 \Re\mathcal T_t>
 \log\frac{9/10}{(33/35)^2}=\log(245/242)>0.
\tag{14}
\]
First transport \(t\) to \(.15\). Lemma 1 then transports
\(u\) to \(.1\) or \(.4\). The resulting values are the
two completed real-real corners, whose bare defects are less than
\(-1/2000\). Their original external halfweight has the same
favorable convex comparison.

On the compact regions (12), every original factorial argument
is regular; in particular \(t+u<.65\) and \(a+t\) has real
part at most \(.60\). The exact interpolation or the direct
finite-product bound consequently gives the row upper rate
\(\Re\mathcal T\), uniformly near the complete ordinary color.
All signs may be discarded here because every row has already been
placed strictly below the plane. The at most \(N^2\) rows,
original source prefactor, small color perturbation and inward-cut
changes use only half the gap. Cauchy's formula, applied to each
summand before summing its bound, retains all fixed derivatives.
\(\square\)

Lemma 2 and the existing low-Newton theorem treat the singular ends
omitted from (11)--(12). The terminal end-index theorem must first
be applied to its entire coherent Newton sum; no estimate for
arbitrary partial Newton sums is inferred inside that end sector.
Proposition 3, Proposition 4 and the
[left central-Newton strip](research_mixed_terminal_three_left_strip.md)
then cover the corresponding exterior portions of the remaining
transform half \(t\le .5\), with matched inward cuts.
These deductions make no assertion about the right-hand physical
triangle, the full terminal polynomial, or arbitrary short fillings.
