# The original ordinary update does not preserve a height half-plane

Private written deduction, 10 November 2026. Even strictly negative
heights of both external legs do not force both outputs of the
original own-three update to have nonpositive height. This is an
exact local-map obstruction to a proposed invariant-product or
scalar maximum-principle proof. The external inputs constructed
below are not asserted to occur in an actual finite open word.
No new finite-source bound or actual-word counterexample follows.

## 1. The original zero-lift map at an exact real point

Use the ordinary map of
[universal critical localization](research_mixed_cyclic_critical_localization.md),
equations (5)--(6), with own type three. Its external legs are
\(a,b\), and its two outputs are \(s,t\). On the original
regular logarithmic branches the two equations are
\[
\begin{split}
f_1&=J'(s+t)+J'(s+a)-2J'(s)+i\pi(a-t)=0,\\
f_2&=J'(s+t)+J'(t+b)-2J'(t)+i\pi(b-s)=0,
\qquad J'(z)=\Log(2\sin\pi z).
\end{split}
\tag{1}
\]
At
\[
                      a=b=s=t=1/3
\tag{2}
\]
these equations vanish with their zero lifts: the positive real
sines at \(1/3\) and \(2/3\) agree and both displayed
chirps vanish. The point \(1/3\) is strictly inside the
original type-three disk, and also inside its reduced disk.
For example its squared distance from \(7/20-i/100\) is
\((1/60)^2+(1/100)^2<(83/1000)^2\).
Thus the already proved holomorphic ordinary map is the branch
through (2), by uniqueness in the original chamber. This does
not select a root merely from exponentiated equations.

Since \(J''(1/3)=\pi/\sqrt3\) and
\(J''(2/3)=-\pi/\sqrt3\), its exact Jacobians at (2) are
\[
 f_{(s,t)}=\pi
 \begin{pmatrix}
 -4/\sqrt3&-1/\sqrt3-i\\
 -1/\sqrt3-i&-4/\sqrt3
 \end{pmatrix},\qquad
 f_{(a,b)}=\pi(-1/\sqrt3+i)I_2.
\tag{3}
\]
In particular the first matrix is nonsingular, consistently
with the original holomorphic existence theorem.

For a small real parameter \(\xi\), first set
\(a=1/3+\xi\), \(b=1/3-\xi\). The antisymmetric
eigenvalue of the first matrix in (3) is
\(\pi(-\sqrt3+i)\). Implicit differentiation therefore gives
\[
\begin{split}
s'(0)&=-\frac{-1/\sqrt3+i}{-\sqrt3+i}
                  =-\frac12+\frac{i}{2\sqrt3},\\
t'(0)&=\frac12-\frac{i}{2\sqrt3}.
\end{split}
\tag{4}
\]
All displayed identities are exact algebraic differentiations
of (1); no root or numerical value has been evaluated.

**Proposition 1.** There are external inputs strictly inside the
original reduced type-three disks, with both heights strictly
negative, whose original own-three outputs have opposite height
signs, the first strictly positive.

Indeed use instead
\[
 a(\xi)=1/3+\xi-i\xi^2,
 \qquad b(\xi)=1/3-\xi-i\xi^2.
\tag{5}
\]
For all sufficiently small real \(\xi>0\), both inputs
remain in the stated disks and both have negative height.
Their first derivatives at zero are unchanged, so holomorphy
and (4) give
\[
 \Im s(\xi)=\frac{\xi}{2\sqrt3}+O(\xi^2)>0,
 \qquad
 \Im t(\xi)=-\frac{\xi}{2\sqrt3}+O(\xi^2)<0.
\tag{6}
\]
The outputs remain in the original chamber and on the same
zero-lift branch. This proves the proposition.

Thus neither the closed nor the open lower-height product is
invariant under every original own-three block update. In
particular, the universal local-map existence and accretivity
theorems cannot by themselves prove nonpositive ordinary
heights by iterating that product.

## 2. The exact height equation at an actual open reference

There is also a direct way to see the sign issue without choosing
an auxiliary input. For a real \(x\in(0,1)\) and a real
height \(y\), define
\[
 \overline C(x,y)=\int_0^1\Re\cot\pi(x+i\theta y)\,d\theta.
\tag{7}
\]
The real sine logarithm at height zero and vertical integration
of its original derivative give
\[
              \Im J'(x+iy)=\pi y\overline C(x,y).
\tag{8}
\]
This identity also holds at \(y=0\); it divides by no height.
The averaged coefficient \(\overline C(x,y)\) is positive
for \(0<x<1/2\) and negative for \(1/2<x<1\),
independently of \(y\), by the exact real cotangent formula.

At an actual own-three ordinary vertex write
\(a=x_a+iy_a,s=x_s+iy_s,t=x_t+iy_t\). Define
\(C_s=\overline C(x_s,y_s)\),
\(C_{st}=\overline C(x_s+x_t,y_s+y_t)\), and similarly
\(C_{as}\). The imaginary part of the first original open
equation, namely
[open critical localization](research_mixed_open_word_critical_localization.md)
(3), is exactly
\[
 (2C_s-C_{st}-C_{as})y_s-C_{st}y_t-C_{as}y_a=x_a-x_t.
\tag{9}
\]
The reduced-disk wire and vertex bounds in
[the pair-sum theorem](research_mixed_reduced_disk_pair_sums.md),
(2)--(3), apply to every actual ordinary open vertex and give
\[
 0<x_s<1/2,
 \qquad 1/2<x_a+x_s<1,
 \qquad 1/2<x_s+x_t<1
\tag{10}
\]
for own type three. Consequently
\[
 C_s>0,\qquad C_{st}<0,\qquad C_{as}<0.
\tag{11}
\]
Equation (9) has a positive diagonal coefficient and positive
off-diagonal height coefficients. It is not an equation with
nonpositive off-diagonal coefficients to which the usual scalar
maximum principle for a nonpositive boundary height applies.
The real-coordinate forcing \(x_a-x_t\) is retained and has
not been assigned a universal sign. The reversed equation has
the analogous forcing from the other external leg.

This observation does not refute the original positive real
Hessian: accretivity is an invertibility and quadratic-form
statement, whereas the missing implication would require an
order-preserving response. The exact response (4) demonstrates
the distinction on the original map itself.

## 3. The actual endpoint compatibility remains necessary

For the first ordinary vertex of an actual word, its left input
is an attached endpoint output, not a freely chosen input in
the type-three disk. In the notation of
[rational critical transport](research_mixed_rational_critical_transport.md),
equations (3)--(8), it satisfies
\[
 (A,S)=(Z_\alpha(U),S_\alpha(U)),\qquad
 (B,C)=R_{2+\epsilon}(A,S),
\tag{12}
\]
where \(U\) is the original complete-end parameter and all
four quantities retain their actual zero-logarithmic lifts.
The later iterates must also meet the actual right endpoint
conditions (17) of that source. The endpoint rectangles and
ordinary image bounds are necessary enclosures for this coupled
system; arbitrary points in their product need not satisfy it.

Proposition 1 does not impose (12) or the right endpoint
matching. It therefore proves neither an actual word with a
positive first private height nor the failure of a stronger
correlated sign statement on actual references. Conversely,
no such actual-reference sign follows from the independent
negative-height input hypothesis, even strengthened to strict
negativity. A proof that removes the remaining positive private
height sector must use additional endpoint/downstream
compatibility or estimate that sector directly. No high-row,
alias, selected-weight or whole-boundary payment is claimed here.

## Direct source bindings

The following sources were read directly. Only written algebra,
differentiation and the existing source theorems were used; no
mathematical numerical evaluation, saved-value arithmetic,
import, compilation, test or frozen-source edit was performed.

| Source | SHA-256 |
|---|---|
| research_mixed_cyclic_critical_localization.md | ccb8b144e6068c434059b707cd13d9aed8bb88a40e7fa0cf0e6bc655bff7fa71 |
| research_mixed_open_word_critical_localization.md | a3f8a0f781abd43f8ca17321171081ba37c91b284f83f22a4f7ae34e270424fa |
| research_mixed_reduced_disk_pair_sums.md | 6c93f96db406e73aca137c5e492d65cb1c8e2333d410c89d945d5ef3d071ed96 |
| research_mixed_rational_critical_transport.md | 0cba78ed20d7e98d65414b61a96412a8ee6f3e43b766d7d10f9900ea36a96635 |
| research_mixed_open_word_endpoint_rectangles.md | ac5603badc00d42e98d17a1c5948cae011a6abd991d5249fa61d4224a829ad07 |
