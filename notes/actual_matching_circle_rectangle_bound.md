# The marked crossing-circle rectangle has ratio at most one

A crossing circle in an augmented link surrounds two main strands. Its complete cusp has a distinguished rectangle determined by the original crossing disk and its meridian paths. This note proves that the positive ratio \(c\) of that disk-framed rectangle satisfies
\[
                         0<c\le1. \tag{1}
\]
The hypothesis is an actual complete right-angled matching-polyhedron certificate, including its labeled face pairings and primitive peripheral curves. An abstract ideal rectangle without those identifications need not satisfy (1).

The consequence is a restriction on the trace used by the quantum recoupling formula: it lies at or below \(-2\). The proof is geometric but short. The marked paths make the target an element of the complete manifold's holonomy group. If \(c>1\), that element would be an elliptic rotation with an interior fixed axis, contradicting the free deck action. The endpoint \(c=1\) is a nonidentity parabolic element and is allowed.

## 1. The rectangle and the based meridian matrices

Assume the labeled cut, complete cusp metric and primitive crossing-circle paths of the [matching-polyhedron certificate](general_augmented_plat_matching_geometry.md). In its disk-framed coordinate, the rectangle has vertices
\[
 (1,E,-1,-E),\qquad E=e^{2\pi i x},\qquad
 0<x<\tfrac12,\qquad c=\cot(\pi x)>0.
\]
The parameter \(x\) describes this rectangle. The number \(c\) is its ratio in the stated disk framing, not an arbitrary choice of Euclidean scale.

Let \(A,B\) be determinant-one lifts of the two based main-meridian holonomies. Their basepaths are those of the original threading diagram. They can be normalized as
\[
 A=-\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
 B=-\begin{pmatrix}1&0\\-4&1\end{pmatrix}.
\]
Put \(P=BA\), \(H=P+I\), so \(H^2=0\). The pure transport through the crossing disk has the form \(C=I+bH\), and the transported outgoing meridian is \(B_{\mathrm{out}}=CBC^{-1}\).

The retained half-twist sign is \(\epsilon\in\{0,+1,-1\}\). Let \(\tau_\epsilon\) be the primitive cusp shape in that actual signed diagram. The collar calculation and quantum sign calibration give
\[
 \tau_\epsilon=\frac{2ic}{1-\epsilon ic},\qquad
 b-\frac\epsilon2=\frac1{\tau_\epsilon},\qquad
 b=-\frac{i}{2c}. \tag{2}
\]
Thus the same coefficient \(b\) is obtained for all three retained signs.

The inverse cup bend in the quantum contraction fixes the target word. It is
\[
 W=B^{-1}B_{\mathrm{out}},\qquad
 \operatorname{Tr}W=2+16b^2=2-\frac4{c^2}. \tag{3}
\]
This is the [actual geometric target formula](actual_matching_edge_geometric_target_polynomial.md). To use completeness, we must know that \(W\) really belongs to the marked holonomy group. For a half-twisted disk, that does not follow by simply assuming that the pure transport \(C\) is itself a group element. The next step supplies the actual words.

## 2. Recovering the group word at each half-twist sign

Set \(S=I+H/2\), and let \(\mu\) be the based auxiliary meridian. The primitive-collar reconstruction in the [critical-scheme theorem](actual_augmented_plat_critical_scheme.md), at its complete endpoint \(J=-1\), gives the projective identity
\[
                         \mu=C^{-1}S^\epsilon. \tag{4}
\]
The scalar in this identity is accounted for explicitly. The generic factor \((P^{-1}-I)^\epsilon\) specializes through
\[
                         P^{-1}-I=-2S,
\]
and the recorded factor \(h_J^{-\epsilon}=(-2)^{-\epsilon}\) cancels it. Any remaining central lift sign does not affect conjugation. Thus (4) represents the primitive meridian rather than a substituted half-longitude.

Direct multiplication gives
\[
 SBS^{-1}=A,\qquad S^{-1}BS=BAB^{-1}. \tag{5}
\]
Substituting \(C=\mu^{-1}S^\epsilon\) into \(B_{\mathrm{out}}=CBC^{-1}\) yields
\[
 B_{\mathrm{out}}=
 \begin{cases}
 \mu^{-1}B\mu,&\epsilon=0,\\
 \mu^{-1}A\mu,&\epsilon=+1,\\
 \mu^{-1}BAB^{-1}\mu,&\epsilon=-1.
 \end{cases} \tag{6}
\]
Every line is an actual based holonomy word in the same complete manifold. The common basepaths of \(A,B,\mu\) come from the original threading convention. Therefore \(W=B^{-1}B_{\mathrm{out}}\) is a group element for every retained sign. Nothing requires \(S\) itself to belong to that group. Changing a determinant-one lift sign cannot change whether the corresponding projective element is elliptic or parabolic.

## 3. Completeness rules out a ratio greater than one

The certified metric is complete, and its universal developing cover is hyperbolic three-space. Its holonomy acts by deck transformations and hence freely: no nonidentity element fixes an interior point.

Suppose \(c>1\). Equation (3) gives \(-2<\operatorname{Tr}W<2\). The determinant-one matrix then has distinct eigenvalues \(e^{i\theta},e^{-i\theta}\), with \(0<\theta<\pi\). Its projective action is a nontrivial rotation about the geodesic joining its two ideal fixed points. That rotation fixes the interior points of its axis, contradicting the free deck action. Consequently \(c\le1\), which proves (1).

This argument uses the actual marked word (6). It needs no additional conjectural packing inequality. It also explains the role of the hypothesis: an abstract rectangle does not supply a deck transformation, so the same contradiction would not be available.

At equality, the target is parabolic rather than the identity. In the chosen lift,
\[
 W=\begin{pmatrix}
 8b^2-4b+1&4b^2\\
 16b^2&8b^2+4b+1
 \end{pmatrix}.
\]
When \(c=1\), equation (2) gives \(b=-i/2\), and
\[
 W+I=\begin{pmatrix}2i&-1\\-4&-2i\end{pmatrix}\ne0,
 \qquad (W+I)^2=0.
\]
A nontrivial parabolic transformation has no interior fixed point, so completeness does not exclude this case. A strict inequality would require another argument about this particular word.

## 4. Consequence for the spectral target

For every crossing circle covered by the complete marked certificate,
\[
 \begin{array}{ll}
 c<1:&\operatorname{Tr}W<-2,\\
 c=1:&\operatorname{Tr}W=-2.
 \end{array}
\]
Thus the target is either real and outside the physical Casimir interval \([-2,2]\), or at its parabolic endpoint. The formal branch \(c>1\) still exists in the local algebraic four-parabolic relation, but it cannot be the complete geometry with these marked identifications.

The conclusion concerns the trace, not every entry of a surrounding operator. It does not place all physical rows in a favorable support domain, identify the surrounding continuant state, or prove that a contour contribution survives. Those are separate analytical tasks. The [focused calculation](../experiments/audit_actual_matching_circle_rectangle_bound.py) checks the scalar cancellation, the three based words, the trace and the nonidentity endpoint matrix through sixteen exact identities; the free-deck argument above proves the general geometric restriction.
