# The conditional critical root at the incoming unit endpoint

Private written deduction, 10 November 2026. The original upper
critical root has a regular algebraic continuation to \(X=1\),
although its logarithmic phase approaches a numerator wall there.
Its difference from \(X\) has an exact cubic factor. Consequently
the incoming action multiplier has an exact quadratic factor.
This identifies the singular part of the horizontal action derivative
without evaluating an action.

The note concerns the critical root and phase. It does not assert a
uniform finite-sum asymptotic at the coalescing endpoint.

## 1. The algebraic factorization

Use the cubic and original branch of
[the unit incoming branch theorem](research_mixed_four_conditional_unit_incoming_branch.md):
\[
 v(v-X)(v-Y)=X(v-1)^3,\qquad
 |X|=1,\quad \Im X>0,\quad \Im Y<0,\quad\Re Y<1.
 \tag{1}
\]
Let \(K\) be any compact subset of the stated outgoing \(Y\)-domain.
In particular \(1\notin K\).

**Lemma 1.** There is a fixed neighborhood of \(\{1\}\times K\)
and a holomorphic function \(f(X,Y)\) there such that
\[
 v(X,Y)=X+(1-X)^3 f(X,Y),\qquad
 f(1,Y)=\frac1{Y-1}.
 \tag{2}
\]
For upper unit \(X\) sufficiently close to one, \(v\) in (2) is
exactly the original upper root. After decreasing the neighborhood,
\(f\) is bounded and bounded away from zero on a fixed closed
neighborhood of \(\{1\}\times K\).

*Proof.* Write \(\varepsilon=1-X\), set
\(v=X+\varepsilon^3 f\), and define
\[
 \mathcal E(X,Y,f)
   =(X+\varepsilon^3 f)f(X+\varepsilon^3 f-Y)
                  +X(1-\varepsilon^2f)^3 .
 \tag{3}
\]
At \(X=1\), its zero is \(f_0(Y)=1/(Y-1)\), and
\[
 \partial_f\mathcal E(1,Y,f_0)=1-Y\ne0.
 \tag{4}
\]
The analytic implicit-function theorem gives a unique holomorphic
solution near each point of \(\{1\}\times K\). These germs agree
on their overlaps by the same local uniqueness. Compactness gives
a common sufficiently small \(X\)-neighborhood and an outgoing
neighborhood of \(K\). The nonzero initial function \(f_0\) and
compactness give the stated upper and lower bounds.

For \(X\ne1\), multiplying (3) by \(\varepsilon^3\) gives
exactly (1), with the \(v\) in (2). There has been no division
by a root-dependent quantity. At \(X=1\), the cubic has the
simple root \(v=1\), since its \(v\)-derivative there is \(1-Y\).
Thus (2) also gives its regular algebraic continuation.

It remains to identify this root with the original one, rather
than merely construct a root near the endpoint. Put
\(X=e^{i\phi}\), \(0<\phi<\pi/2\). Uniformly for \(Y\in K\),
\[
 |v-X|\le M|1-X|^3\le M\phi^3,\qquad
 \Im X=\sin\phi\ge\frac{2\phi}{\pi}.
 \tag{5}
\]
For a sufficiently small fixed \(\phi\), the right side of the
first inequality is less than half the last lower bound.
Hence \(\Im v>0\). The unit incoming branch theorem has exactly
one upper root, so this is that root. This also fixes its original
logarithmic lift. \(\square\)

The implicit-function argument is local at a divisor of the
logarithmic phase, but it is not singular for the cubic itself.
It gives no finite-\(N\) contour estimate near that divisor.

## 2. The original action derivative

For real \(a<1\), put
\[
 X=e^{-2\pi ia}=e^{2\pi i(1-a)},\qquad
 \omega=\frac{v-X}{1-X},\qquad
 \Theta(a,y)=Q(t(a,y);a,y).
 \tag{6}
\]
The original stationary identity, with its unchanged carrier, is
\[
                         e^{\Theta_a}=\omega .
 \tag{7}
\]
Equations (2) and (6) give the exact factorization
\[
                         \omega=(1-X)^2 f(X,Y).
 \tag{8}
\]
Taking moduli in (7), without selecting a new logarithmic branch,
yields
\[
 \partial_a\Re\Theta(a,y)
   =2\log|1-X|+\log|f(X,Y)|.
 \tag{9}
\]
In particular, uniformly for \(Y\in K\),
\[
 \partial_a\Re\Theta(a,y)
   =2\log\bigl(2\sin(\pi(1-a))\bigr)
       -\log|1-Y|+O(1-a)
       \quad\hbox{as }a\uparrow1.
 \tag{10}
\]
Here the bounded nonzero holomorphic function in Lemma 1 gives
\(\log|f(X,Y)|=-\log|1-Y|+O(|1-X|)\) uniformly.
This is an expansion of a derivative of the original critical
action, not a new value or additive normalization for that action.

One also has
\[
             t(a,y)=1-a+O((1-a)^3)
 \tag{11}
\]
as a complex statement, uniformly on \(K\). Indeed (2) gives
\(v=X\{1+O((1-X)^3)\}\); the logarithm near one and the original
upper-root argument give
\(\Log v=\Log X+O((1-X)^3)\).
The strict side of the numerator wall is supplied by the branch
theorem: \(0<\Re t<1-a\).

## 3. A joint comparison with a regular cap point

For the original type-four cap, its incoming dependence at a fixed
private point \(e\) is the factorial quotient with logarithmic
derivative
\[
       \partial_a\Re\widehat\Psi(e,a)
        =\log\frac{|1-Xe^{-2\pi ie}|}{|1-X|},
 \tag{12}
\]
on each side of its numerator period wall. This is the
zero-safe continuous rate of
[the global cap transport](research_mixed_first_four_cap_lower_right_horizontal.md).
The additional period term is independent of the real coordinate
\(a\), so the same derivative applies after continuation.

Here is the domain extension used in this statement. The recurrence
in [the global numerator chart](research_mixed_fourier_right_cap_joint_global_chart.md)
can be iterated exactly \(N\) times to give
\[
 \Pi_N(q+1)=(1-e^{-2\pi iNq})\Pi_N(q).
 \tag{12a}
\]
For \(1<\Re q<2\), the resulting upper rate is
\(\Re g(q-1)+2\pi(\Im q)_+\). Its real-coordinate derivative is
\(\log|1-e^{-2\pi iq}|\), since the added period term is constant
in that direction. For the original cap rectangle and \(a<1\)
near one, \(1<\Re(a+e)<1.49<2\).
Thus (12) uses this exact continued numerator and the regular
incoming denominator, not a formula whose asserted range stops
at \(\Re(a+e)=1.2\). Both terms of the period multiplier are kept.

Let \(E\) be a fixed compact set of regular private cap coordinates
on which that numerator continuation and the cap coefficient are
defined. In particular one may take the original retained rectangle
\([.27,.49]+i[-.055,.04]\). With \(p=e^{2\pi ie}\), \(p\) is
bounded away from zero and \(|1-X/p|\) is bounded uniformly for
\(e\in E\) and \(X\) near one. Combining (9) and (12) gives
\[
 \partial_a\{\Re\widehat\Psi(e,a)+\Re\Theta(a,y)\}
       =\log|1-X|+\log|1-X/p|+\log|f(X,Y)|.
 \tag{13}
\]
If a numerator vanishes, this is interpreted by its integrated
upper rate; it does not divide a finite symbol by zero.

**Corollary 2.** For each such \(E\) and outgoing compact set \(K\),
there is a fixed \(a_*<1\) such that the joint rate in (13)
strictly decreases for every \(a_*<a<1\), uniformly for
\(e\in E\), \(Y\in K\). More precisely, its upper derivative
is at most \(\log|1-X|+C_{E,K}\).

*Proof.* The last two logarithms in (13) have a common finite
upper bound, whereas \(|1-X|\) tends uniformly to zero as
\(a\uparrow1\). Choose a fixed neighborhood on which their
upper sum plus \(\log|1-X|\) is negative.
Integrating the continuous zero-safe rate includes a numerator
zero if one occurs. All choices precede the level limit. \(\square\)

This comparison includes the retained cap profiles and their fixed
sampling penalties. It does not include every conditional physical
row, a new conditional contour decomposition, or the genuine cap
endpoint groups. A monotone joint rate still requires a calibrated
starting value before it can pay a finite contribution. Neither
Corollary 2 nor the cubic factorization supplies that missing
calibration on the intervening right-hand interval.

## Direct source versions

| Direct source | SHA-256 |
|---|---|
| research_mixed_four_conditional_unit_incoming_branch.md | b6c8fdaffd436ec82670ec864629d93d36e7c7a8ae7e81033b684e3f86e92e43 |
| research_mixed_first_four_cap_lower_right_horizontal.md | 4d41a967edabf0710fc7b04b723bb3e2fb7a407d44bb5a0fc1678e3f9ee5ee6e |
| research_mixed_fourier_right_cap_joint_global_chart.md | bf0069e52715e82c34be008c5814373017b43c019dd2a1a71dcd381e96b4da9f |

The statements are algebraic and analytic deductions for the
original critical root and continuous rates. No mathematical
numerical evaluation, saved-value arithmetic, test, import,
compilation or frozen-source edit was used. Independent proof
and direct-source review is required before adoption.
