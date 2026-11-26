# A quartic source minimum at the branching products

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

After the prescribed leaf transports have been fixed, many remaining
products are linear in the unknown boundary packets. They can be
eliminated exactly with constant coefficients. Only a product whose
two inputs both come from other products needs nonlinear variables.

If there are \(q\) such products, the quartic minimum needs only
\(2q\) full boundary packets. Its minimum and original source
comparison are unchanged. Its Hessian still lies between \(I\)
and \(3I\), and its half-gradient step is an inward contraction.
The eliminated linear responses require no solve depending on a
trial packet. Their coherent action remains part of the coefficients.

## 1. Start from the already clamped source

Use the source theorem on the internal Conway edges. Fix a level
\(N\ge2\) and a literal expression with \(p\ge1\) binary products.
Each packet belongs to the full \(N\)-dimensional Newton boundary
space \(H_N\), including all repeated-Casimir directions. The
original positive packet norm is used.

That theorem first eliminates the unary corridors and then fixes
each leaf-to-product input at its known normalized transport.
There remain \(p-1\) packet variables \(y_e\), one for each
connection from a nontop product to its next product ancestor.
They lie in their unit balls. Denote the resulting objective by
\(\widetilde F(y)\). Its original normalization satisfies
\[
 B_{\rm tot}^{\,2}\min\widetilde F\le |K_N|^2
       \le\gamma B_{\rm tot}^{\,2}\min\widetilde F,
                  \qquad \gamma=\frac{197}{196}.
 \tag{1}
\]
The original budget \(B_{\rm tot}\), closing row and markings are
fixed. The complete real Hessian and half-gradient bounds are
\[
 I\le D^2\widetilde F\le3I,\qquad
 \left(y-\tfrac12\nabla\widetilde F(y)\right)_e
                      \in\frac{33}{256}\overline{\mathbb B}.
 \tag{2}
\]
The half-gradient map contracts by \(1/2\).
Gradients use the real inner product
\(\operatorname{Re}\sum_e h_e^*k_e\).

Here is the local form of the same objective. Let \(v_*\) be
the highest product. For each product \(v\), its two inputs
\(z_{v,L},z_{v,R}\) are either known leaf transports or
the appropriate variables \(y_e\). Its normalized bilinear
map is \(\Phi_v\). There are known constant linear corridor
maps \(P_v\), positive matrices \(W_v\), a known closing
row \(c\), and a positive scalar \(D_*\), such that
\[
 \begin{split}
 \widetilde F(y)
 ={}&\sum_{v\ne v_*}
   \|y_{e(v)}-P_v\Phi_v(z_{v,L},z_{v,R})\|_{W_v^{-1}}^2\\
 &+\frac{|cP_{v_*}\Phi_{v_*}(z_{v_*,L},z_{v_*,R})|^2}{D_*}.
 \end{split}
 \tag{3}
\]
Here \(e(v)\) is the outgoing internal connection of \(v\),
and \(\|w\|_H^2=w^*Hw\). Formula (3) is precisely the
constant-corridor and scalar-root formula from the direct source.
All omitted leaf-block costs are zero at their prescribed centers.

## 2. Count the products that remain bilinear

Classify a product by the number of its inputs represented by
internal variables:

* With no internal input, its output expression is a known constant.
* With one internal input, its output expression is a known linear
  function of that packet, because its other input is prescribed.
* With two internal inputs, its output expression remains bilinear.

Let \(u\) count the middle class and \(q\) the last class.
Every nontop product contributes exactly one internal connection
to one input of a product above it. Therefore
\[
                              p-1=u+2q.
 \tag{4}
\]
In particular \(2q\le p-1\).

Retain the input packet on each of the two incoming internal
connections of every product in the last class. These \(2q\)
packets are distinct, since a product output has only one parent.
Call their list \(w\), and call the other \(p-1-2q\) packets
\(z\). The classification is made from the expression tree and
the already prescribed leaf inputs. No unknown internal product
output is set to its true value.

**Theorem.** The exact partial minimum
\[
             F_{\rm br}(w)=\min_{\|z_e\|\le1}\widetilde F(w,z)
 \tag{5}
\]
is a real polynomial of degree at most four on \(2q\) full
packets, or \(4Nq\) real coordinates. Its inner minimizer is
unique and interior. On the retained product of balls,
\[
                         I\le D^2F_{\rm br}\le3I.
 \tag{6}
\]
Its half-gradient step stays in the \(33/256\) packet balls
and contracts by \(1/2\). Its minimum equals that of
\(\widetilde F\) exactly. Consequently
\[
 \boxed{\quad
 B_{\rm tot}^{\,2}\min F_{\rm br}\le |K_N|^2
          \le\gamma B_{\rm tot}^{\,2}\min F_{\rm br}.
 \quad}
 \tag{7}
\]
All constants and the budget are those in (1).

## 3. A constant linear system removes all other packets

Every input of a product with two internal inputs has been retained.
No omitted packet can therefore occur in a product with another
variable input. The one-input products in Section 2 are already
known linear maps. Taking constant positive square roots of the
metrics in (3), and including its scalar closing component, gives
the exact residual form
\[
                      \widetilde F(w,z)=\|Az+b(w)\|^2.
 \tag{8}
\]
The complex matrix \(A\) is constant in both \(w,z\). The vector
\(b(w)\) is polynomial of degree at most two. It uses the actual
normalized products, fixed leaf packets, corridor metrics and
closing row; no coefficient is an unknown knot value.

If \(z\) is nonempty, (2) implies
\[
                         \tfrac12 I\le A^*A\le\tfrac32 I.
 \tag{9}
\]
For each feasible \(w\), consider the partial half-gradient map
\[
                      z\longmapsto
                         z-\tfrac12\nabla_z\widetilde F(w,z).
 \tag{10}
\]
Its components are components of the full map in (2), so it
sends the omitted product of balls into their \(33/256\)
balls. Its derivative has norm at most \(1/2\), by (9).
The iteration converges to a unique interior fixed point.
Since (8) is a strictly convex quadratic in \(z\), this is its
unconstrained stationary point:
\[
                         z_*(w)=-(A^*A)^{-1}A^*b(w).
 \tag{11}
\]
Thus the original ball constraints are inactive in this inner
problem, rather than being removed by assumption.

The projection formula is consequently
\[
 \begin{gathered}
 \Pi=I-A(A^*A)^{-1}A^*,\\
                       F_{\rm br}(w)=b(w)^*\Pi b(w).
 \end{gathered}
 \tag{12}
\]
Both \(\Pi\) and the operator in (11) are constant. They can
be formed once for each level and fixed source expression.
Each subsequent objective evaluation uses only fixed linear
maps and degree-two expressions. There is no trial-dependent
linear solve. Since \(b\) has degree at most two, (12) proves
the degree-four assertion.

If no packet is omitted, take \(F_{\rm br}=\widetilde F\);
no inverse is needed. If \(q=0\), no outer packet remains:
(11)--(12) evaluate a constant quadratic-response minimum.
The same convention covers an already constant objective.

The linear responses can also be assembled along their constant
corridors instead of forming a dense global projection.
After a fixed leaf input is inserted, the resulting map may be
multiplication by a known packet. Such a map need not be unitary.
Its response Gram is constant but need not be a scalar multiple
of the identity, unlike a corridor containing only genuine turns.
Those matrices and all their phases must remain.

## 4. Conditioning and the original source survive elimination

The inner point (11) depends smoothly on \(w\). At that point,
write \(H=D^2\widetilde F\) in retained and omitted coordinates.
The real Schur formula gives
\[
 D^2F_{\rm br}=H_{ww}-H_{wz}H_{zz}^{-1}H_{zw},\qquad
 h^{\mathsf T}D^2F_{\rm br}h
        =\min_k(h,k)^{\mathsf T}H(h,k).
 \tag{13}
\]
The lower bound in (2) gives at least \(\|h\|^2\);
choosing \(k=0\) gives at most \(3\|h\|^2\).
This proves (6). The formulas extend to the boundary of the
retained balls, using the same interior margin for \(z_*\).

The inward statement follows from the envelope identity
\[
                        \nabla F_{\rm br}(w)
                         =\nabla_w\widetilde F(w,z_*(w)).
 \tag{14}
\]
Its half-step is the retained component of the full feasible
half-step in (2). The \(33/256\) bound follows directly.
Averaging the Hessian bound (6) along a segment proves
contraction by \(1/2\). The minimum is therefore unique and
interior whenever variables remain.

Exact partial minimization gives
\(\min F_{\rm br}=\min\widetilde F\), proving (7),
including zeros. The only restriction of a previous feasible set
was the earlier, explicit leaf-transport clamp in the direct source.
This note adds elimination, not further clamping. No normalization
budget is reassigned to a fused linear map.

When \(p=0\), the source has only its prescribed leaf and linear
transport; the direct source already evaluates its scalar response.
When \(p\ge1\) but \(q=0\), all remaining maps after the known
leaf inputs are inserted are linear or constant. Equation (12)
then contains the whole finite problem without an outer
minimization. This does not simplify the geometric asymptotics
of that coherent linear expression.

## 5. What this does not remove

Every retained packet is still the full \(H_N\). Eliminated
coordinates contribute through the exact constant response;
no Casimir derivative or original marked closing is quotiented
out. The result changes neither the original tangle nor its
finite source.

The smaller number of nonlinear packets does not make a source
coefficient positive, or give it the hyperbolic-volume rate.
Known linear maps can still carry strong phases and cancellation.
A geometric trial certificate must control those actual responses
and the original closing. Nor does convexity alone imply an exact
degree-four semidefinite relaxation of the newly reduced
objective; no such assertion is made.

## Complete proof source

The sole complete proof direct was read at its matching pin:

| Source | SHA-256 |
|---|---|
| [Quartic minimum on the internal Conway edges](research_conway_binary_skeleton_quartic.md) | 294220039d913fd349b867f9705670215c3ca98f581461c6f406db0dac20c7a3 |

It supplies the clamped objective, its constant response metrics,
conditioning, source comparison and original normalization.
The additional reduction here uses the count (4), known linear
responses after prescribed leaf inputs, and a second exact
constant-coefficient elimination. No novelty is claimed for
least squares or Schur complements.

Only written mathematics and text/hash operations were used.
No mathematical program, numerical experiment, test, build,
git operation or earlier-final edit was performed.
