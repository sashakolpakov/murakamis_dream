# An exact criterion for the type-three conditional critical point

Research deduction, 7 November 2026. The full twice-negatively-crossed
Fourier source reduces to a type-three conditional polynomial with a
Fourier boundary parameter as its second argument. That parameter need
not belong to the smaller domains of the existing conditional-source
theorems. This note gives an explicit criterion for its critical point
to lie in the original cotangent strip. It does not estimate the finite
sum or prove that this critical point contributes to it.

## 1. Parameters and the criterion

For complex numbers
\[
 P=p+i\alpha,\qquad Q=q+i\beta,\qquad
 p,q>0,\qquad |\alpha+\beta|<2,
 \tag{1}
\]
define
\[
 \mathcal B(P,Q)
 =p^2+q^2-(p+q)(\alpha q-\beta p).
 \tag{2}
\]
The letters \(P,Q\) here denote cotangents, not the finite factorials
or the root of unity used in the source formulas. Put
\[
 F(S;P,Q)=S^2+(P+Q)S-1+i(Q-P),\qquad
 \mathcal S=\{S:\Re S>0,\ |\Im S|<1\}.
 \tag{3}
\]
This is the original type-three critical polynomial in
[the cotangent root theorem](research_mixed_global_cotangent_roots.md),
equation (4).

**Theorem 1.** Under (1), the following alternatives are exhaustive.

1. If \(\mathcal B>0\), the polynomial has exactly one root in
   \(\mathcal S\), counted with multiplicity. This root is simple.
2. If \(\mathcal B<0\), it has no root in \(\mathcal S\) or on
   its boundary.
3. If \(\mathcal B=0\), it has the simple boundary root
   \[
     S_0=i\frac{p-q}{p+q}.
     \tag{4}
   \]
   Its other root has strictly negative real part, so there is
   no root in \(\mathcal S\).

In particular, (2) is a necessary and sufficient condition for a
critical point in this specified strip. It is not a condition for the
existence of a critical point elsewhere.

## 2. Root count and the direction of the only possible crossing

On the two horizontal sides of the strip, direct expansion gives
\[
 \begin{split}
 \Im F(u+i)&=u(2+\alpha+\beta)+2q>0,\\
 \Im F(u-i)&=u(-2+\alpha+\beta)-2p<0
                         \qquad(u\ge0).
 \end{split}
 \tag{5}
\]
Thus a root cannot lie on either side. On the imaginary axis,
\[
 \begin{split}
 \Im F(iv)&=(p+q)v+q-p,\\
 \Re F(iv)&=-1-v^2+\alpha(1-v)-\beta(1+v).
 \end{split}
 \tag{6}
\]
The first equation vanishes at just one real value,
\(v_0=(p-q)/(p+q)\in(-1,1)\). At that value the second is
\[
                 \Re F(iv_0)=-\frac{2\mathcal B}{(p+q)^2}.
 \tag{7}
\]
At a boundary root, \(\Re F_S=p+q>0\), proving its simplicity.
The sum of the two roots has real part \(-(p+q)\), which proves
the assertion about the other root when \(\mathcal B=0\).

To count roots away from the boundary, keep \(p,q\) fixed and
replace \((\alpha,\beta)\) by \((t\alpha,t\beta)\),
\(0\le t\le1\). The bounds (5) persist. The boundary value is
now governed by
\[
 \mathcal B_t=p^2+q^2-t(p+q)(\alpha q-\beta p).
 \tag{8}
\]
At \(t=0\), there is exactly one root in \(\mathcal S\).
Indeed (5)--(7) exclude boundary roots for all positive real
\(p,q\); deforming them to \(p=q=1\) preserves the count,
and the roots at that point are \(-1\pm\sqrt2\).
Every polynomial along each compact deformation is monic with
bounded coefficients. Its roots therefore remain bounded; no
root can enter or leave through infinity.

If \(\mathcal B_1>0\), (8) is positive along the entire segment,
so the count remains one. Counting multiplicities gives simplicity.
If \(\mathcal B_1<0\), (8) vanishes exactly once, at some
\(t_0\in(0,1)\). Write \(D=\alpha q-\beta p\). Then
\(D>0\), and at this simple boundary root
\[
 \left.\frac{\partial F}{\partial t}\right|_{S=iv_0}
       =\frac{2D}{p+q}>0,\qquad
 F_S=p+q+i\{2v_0+t_0(\alpha+\beta)\}.
 \tag{9}
\]
Implicit differentiation consequently gives
\[
 \left.\Re\frac{dS}{dt}\right|_{t=t_0}
 =-\frac{2D}{(p+q)^2+\{2v_0+t_0(\alpha+\beta)\}^2}<0.
 \tag{10}
\]
The unique right-hand root crosses into the left half-plane.
There is no second boundary crossing, so the final count is zero.
Equations (5)--(7) also exclude final boundary roots. This proves
all three alternatives. \(\square\)

In fact every root with \(\Re S=u\ge0\) obeys
\[
 \Im S=\frac{p-q-(\alpha+\beta)u}{2u+p+q}\in(-1,1).
 \tag{11}
\]
Thus the same criterion counts roots in the whole open right
half-plane, not just in its intersection with the strip.

## 3. Holomorphic branch and the original logarithmic equation

Let \(\mathcal D\) be the open parameter set described by (1)
and \(\mathcal B>0\). On this set the unique root in
\(\mathcal S\) is a globally defined holomorphic function of
\((P,Q)\). Simplicity gives local implicit functions; uniqueness
makes them agree on overlaps.

The set \(\mathcal D\) is connected. The preceding deformation
of imaginary parts stays in it, since (8) is a positive convex
combination of \(\mathcal B_0\) and \(\mathcal B_1\).
Its positive real parameter quadrant is connected as well.

Define the three inverse cotangents by
\[
 a=\frac{1}{2\pi i}\Log\frac{P+i}{P-i},\qquad
 b=\frac{1}{2\pi i}\Log\frac{Q+i}{Q-i},\qquad
 s=\frac{1}{2\pi i}\Log\frac{S+i}{S-i}.
 \tag{12}
\]
These principal logarithms are holomorphic: for any variable
\(W\) with positive real part,
\[
 \Im\frac{W+i}{W-i}=\frac{2\Re W}{|W-i|^2}>0.
 \tag{13}
\]
In particular \(0<\Re a,\Re b,\Re s<1/2\). All arguments
\(a,b,s,s+a,s+b\) remain in the original regular strips of
the marked factorial primitive \(g\). Its logarithmic derivative
is the branch of \(\log(1-e^{-2\pi iz})\) prescribed there.

At the root, the polynomial equation is equivalent to
\[
 \exp\{g'(s+a)+g'(s+b)-2g'(s)+2\pi ia\}=1.
 \tag{14}
\]
The exponent is holomorphic on the connected set \(\mathcal D\)
and takes values in \(2\pi i\mathbb Z\), so it is constant.
At \(P=Q=1\), one has \(a=b=1/4\) and \(s=3/8\).
The original sine-log formula makes that exponent zero.
Consequently the root solves the original equation with zero
logarithmic lift throughout \(\mathcal D\):
\[
       g'(s+a)+g'(s+b)-2g'(s)+2\pi ia=0.
 \tag{15}
\]

It is a nondegenerate critical point of the conditional phase.
Writing that phase as
\[
 Q_0(s;a,b)=g(s+a)+g(s+b)-2g(s)+2\pi ias,
\]
its second derivative at the root satisfies
\[
 -Q_{0,ss}
 =\frac{\pi(1+S^2)(2S+P+Q)}{(P-i)(Q+i)}\ne0.
 \tag{16}
\]
This follows by differentiating the exact expression
\(\exp(Q_{0,s})=(S+P)(S+Q)/((P-i)(Q+i))\) and using
\(dS/ds=-\pi(1+S^2)\). Every displayed denominator is
nonzero in the stated domains. No sign of the real part of (16)
is asserted on this larger parameter set.

## 4. How to use the criterion for a transformed source

For a conditional polynomial with additive arguments \((a,y)\),
the proposed geometric branch in this strip can be tested using
only
\[
 P=\cot(\pi a),\qquad Q=\cot(\pi y),
\]
and the real inequality (2), provided (1) holds. Equivalently,
these cotangents are rational functions of the exponentiated
boundary variables. Thus the test requires no choice of a
dilogarithm value or numerical stationary-point approximation.

The theorem does not assert (2) for every actual incoming reference
of the twice-crossed source. Those references retain their original
geometric correlations, which must be used when testing (2).
Even when the criterion holds, the whole finite-source proof must
still control its endpoint terms, Fourier corrections and the
contribution of this critical point. The earlier
[complex-parameter obstruction](research_mixed_complex_horizontal_obstruction.md)
explains why root existence alone cannot replace those comparisons.
