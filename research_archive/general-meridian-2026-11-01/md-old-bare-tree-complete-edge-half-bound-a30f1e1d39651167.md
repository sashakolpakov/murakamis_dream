# Physical edge labels at the complete maximum of an old bare tree

Private proof, 1 November 2026. This is an old positive-pressure
statement. It supplies a regular-window fact and makes no estimate
for additional moving-quotient trace terms.

## 1. Statement and conventions

Let a finite connected tree have actual bare product hubs of full
valence at least three. Its hub-to-hub edges are physical
quarter-turns. Every external incidence carries a rigid boundary
profile \(g(a)+c\), with \(0\le a\le1/2\), where
\[
 g(a)=J(2a)-4J(a),\qquad
 J(u)=\int_0^u\log(2\sin\pi t)\,dt.
\tag{1}
\]
The constants are retained. Resolve each hub by its original ordered
positive binary products; artificial edges inside this resolution
are unturned and have complementary covariant end labels. Physical
quarter-turn edges have equal covariant end labels.

The original complete positive contraction has a unique strict
maximum. At that maximum, every physical hub-to-hub covariant label
\(z_e\) satisfies
\[
                              0<z_e\le1/2.
\tag{2}
\]
Equality occurs if and only if the entire component consists of two
trivalent hubs, each with two external rigid leaf incidences. In that
exception the single internal label is exactly half. In every other
component, all physical internal labels are strictly below half.

The statement allows arbitrary fixed valences and arbitrary fixed
additive constants. It concerns physical edges only: hidden
unturned-resolution labels are not required to be below half.

## 2. What remains after an actual edge is cut

Cut a physical edge and use its incidence as the root on each side.
At a root hub of full valence \(D\), there are \(D-1\ge2\) ordered
inputs. An external input is a rigid leaf of type \(L\). An input
coming from a child hub is the actual quarter-turn of that child's
unturned product. By induction, the child product has type \(A\),
with full strict ordinary output interval \((0,1)\), and its turn
again has type \(A\). Thus each rooted side is an unturned product
of at least two \(L/A\) inputs. This statement retains the actual
order and every physical turn; it is not an inference from
commutativity of a scalar trace.

Let \(f_A(b)\) and \(f_B(b)\) be the two rooted positive profiles at
their ordinary outputs. They retain their full subtrees and all
hidden product variables. The strict support, endpoint barrier and
negative Hessian arguments give continuous profiles on \([0,1]\),
analytic strictly concave profiles on \((0,1)\), and unique strict
constrained optimizers there. These are the original profile results
for unturned products with \(L/A\) children; their hypotheses have
just been checked recursively for these particular sides.

The covariant label \(z\) of the cut edge is the same at both ends.
The ordinary output of each rooted side is therefore \(1-z\).
The exact optimized cut action is
\[
                         \mathcal P(z)=f_A(1-z)+f_B(1-z).
\tag{3}
\]
No external leaf or cap is inserted in (3). Maximizing this action
and then the two conditional subtrees recovers the original whole
positive contraction.

## 3. The response inequality and its strict case

For completeness, the local product argument is as follows. At the
strict optimizer of an unturned product with ordinary output \(b\),
put
\[
 B=\cot\pi b,\qquad
 X^2=\frac{1+B^2}{1+\kappa},\qquad
 Y^2=\kappa X^2,
 \qquad \kappa=e^{-f'(b)}.
\tag{4}
\]
A rigid leaf has \(B_i=X\), \(Y_i=1\). A proper type-\(A\)
input has \(-Y_i<B_i<X\). Its actual turn has
\((B_i,X,Y_i)\mapsto(-B_i,Y_i,X)\), so it remains proper. Every
unturned product output is proper as well. These are precisely the
response inequalities preserved in the original strict geometry.

At the last binary product, both inputs share \(X\), strict support
gives \(B<B_i\le X\), and direct differentiation of the product
action gives
\[
 Y^2=(B_1-B)(B_2-B)\le(X-B)^2,
 \qquad X^2+Y^2-B^2=1.
\tag{5}
\]
All factors in the first product are positive. Hence
\[
 X\ge X_2(B)=\frac{B+\sqrt{B^2+2}}2,
 \qquad
 f'(b)=\log\frac{X^2}{1+B^2-X^2}
       \ge f_2'(b)=2\log(2X_2(B)^2).
\tag{6}
\]
The logarithm is strictly increasing in \(X\) on its allowed
positive interval. If either input is proper, the first inequality
in (5), and therefore the derivative inequality in (6), is strict.

If the root hub has more than two inputs, its last binary product
has at least one composite proper child. If it has exactly two
inputs but either comes from a child hub, that physical turned
subtree is proper. The only equality case is therefore a root hub
with exactly two rigid external leaf inputs and no child hub.
Its profile is \(f_2\) plus the two fixed constants.

For \(0<b<1/2\), one has \(B>0\),
\(X_2(B)>1/\sqrt2\), and
\[
 f_A'(b),f_B'(b)>0;\qquad
 f_A'(1/2),f_B'(1/2)\ge0.
\tag{7}
\]
At half, each derivative is strictly positive except for the single
trivalent side with two rigid leaves just described. The proof of
(5)–(6), including the unsquared branch choice, is also recorded in
`notes/actual_conway_unflagged_probe_geometry.md`, Appendix A.

## 4. Maximizing the physical edge

For \(z>1/2\), the ordinary output \(1-z\) lies below half. Thus
\[
             \mathcal P'(z)
                =-f_A'(1-z)-f_B'(1-z)<0.
\tag{8}
\]
No strict interior maximum can occur there. At \(z=1/2\), the same
derivative is strictly negative unless both rooted sides are single
trivalent hubs with two rigid leaves. In that nonexceptional case,
moving \(z\) slightly below half increases the action, so its unique
maximum lies below half.

If both sides are the exceptional two-leaf product, then
\(\mathcal P(z)=2f_2(1-z)+c\). The profile \(f_2\) is strictly
concave and symmetric under \(b\mapsto1-b\), with derivative zero
at half, so its unique maximum is exactly \(z=1/2\). This also
proves the asserted converse and the complete equality
classification. The original strict maximum keeps the label away
from zero in every case.

Apply this argument to each physical edge of the same whole
optimizer. The conditional profiles in (3) are exact, so the
separate edge arguments do not replace different neighbors by
independent capped maxima. This proves (2) simultaneously.

For any fixed nonexceptional tree, finiteness now gives a compact
window in which all physical internal labels and all original leaf
labels stay in \((0,1/2)\). The hidden unturned product labels and
all factorial arguments retain their original strict bulk windows.
In the exceptional two-hub tree, its physical internal label stays
in a compact interval inside \((0,1)\) containing half; it need not
be forced to one side in a complex continuation.

This is only a statement about the original positive optimizer and
its local continuation. It neither excludes moving additional terms
away from that window nor supplies a bound for their total
contribution. In particular it does not repair the valence-nine
pointwise moving/complete trace comparison.
