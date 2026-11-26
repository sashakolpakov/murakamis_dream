# A quadratic root obstruction in the released horizontal height box

Research lemma, 5 November 2026. The independent ordinary-leg height
bounds do not keep the conditional type-three root in its original
half-index strip when both outer real parts range through the whole
source rectangle. This is an obstruction to that particular domain
argument. No actual open word is asserted to realize the two heights
below, and no failure of a finite conditional sum is concluded.

## 1. An exact right-half-plane criterion

Use the original quadratic cotangent equation from the
[closed-root theorem](research_mixed_closed_cotangent_roots.md),
\[
 F_0(S)=S^2+(P+Q)S-1+i(Q-P),\qquad
 P=p+i\alpha,\quad Q=q+i\beta,\quad p,q>0.
 \tag{1}
\]
There is no restriction on \(\alpha,\beta\) in the following
algebraic criterion. Put
\[
 A=p+q,\quad B=\alpha+\beta,\quad D=p-q,
 \quad C=1+\beta-\alpha,\quad
 v=D/A,\quad R=-v^2-Bv-C.
 \tag{2}
\]
The only possible imaginary-axis zero is \(S=iv\), and
\(R=\Re F_0(iv)\).

**Lemma 1.** If \(R<0\), precisely one quadratic root has
positive real part. If \(R=0\), one root has real part zero and
the other has negative real part. If \(R>0\), both roots have
negative real parts, counted with multiplicity.

*Proof.* The discriminant and a useful real comparison are
\[
 \Delta=(A+iB)^2+4(C+iD),\qquad L=A^2+B^2-4C.
 \tag{3}
\]
Direct expansion gives
\[
 L=A^2+(B+2D/A)^2+4R,
 \qquad |\Delta|^2-L^2=-16A^2R.
 \tag{4}
\]
For either square root of \(\Delta\), the squared magnitude
of its real part is
\((|\Delta|+\Re\Delta)/2\). Also
\((L+\Re\Delta)/2=A^2\). If \(R\ge0\), the first
identity in (4) makes \(L>0\); the second then gives
\(|\Re\sqrt\Delta|\le A\), with equality precisely when
\(R=0\). If \(R<0\), either \(L\le0\), or the second
identity directly gives \(|\Delta|>L\). In either case
\(|\Re\sqrt\Delta|>A\). The roots
\((-A-iB\pm\sqrt\Delta)/2\) prove the assertions.
\(\square\)

## 2. One rational target, with its limitation retained

Take
\[
 a=23/100-i/10,\qquad b=23/100+13i/200,
 \qquad P=\cot\pi a,\quad Q=\cot\pi b.
 \tag{5}
\]
Both targets are in the closed source rectangle
\([.23,.45]+i[-.12,.12]\). Their heights are strictly inside
the type-four and type-three ordinary height intervals
\((-.102,-.001)\) and \((-.065,.068)\), respectively, from
the [universal image estimate](research_mixed_cyclic_critical_height_bounds.md).
The positive height \(13/200=.065\) lies inside the latter
interval; it is not its negative endpoint.

A single outward evaluation of (2), with the exact arguments (5),
gives
\[
 p,q>0,\qquad
 -.059<v<-.058,\qquad R>3/50.
 \tag{6}
\]
For orientation, the enclosed value of \(R\) is approximately
\(.06664460441096488\). Lemma 1 shows that both roots are
strictly in the left half-plane. Since
\(\Re\cot\pi s>0\) whenever \(0<\Re s<1/2\),
the exponentiated conditional equation has no root in that entire
half-index strip. In particular it has none on the old central
rectangle \([.15,.49]+i[-.20,.20]\). The strict margin also
persists when both real targets are increased slightly into the
interior of the source rectangle.

This does not contradict an established conditional packet: (5)
is not claimed to lie on an actual coupled critical image. In
particular its independent height assignment has not been realized
by an open word. Nor does an algebraic exclusion identify the
continued original logarithmic branch after it leaves the strip.
No assertion about cancellation or noncancellation of the full
finite sum follows from (6).

The consequence is limited but useful. A horizontal extension to
the full released rectangle cannot infer containment of a moving
root from the two independent ordinary height intervals alone.
It must retain additional correlations, use a smaller horizontal
domain, or give an upper-source argument that does not require
that root containment. The fixed-reference contour approach remains
available and is not contradicted by this example.

## 3. Focused reproduction

The checker verifies (4) symbolically, the rational domain inclusions,
and only the one outward cotangent evaluation (5)--(6). It performs
no root search, parameter grid, or finite-kernel test.

```sh
python3 experiments/check_mixed_horizontal_root_obstruction.py --precision 256
python3 experiments/check_mixed_horizontal_root_obstruction.py --precision 320 --input repro/results/research-mixed-horizontal-root-obstruction.json --output repro/results/research-mixed-horizontal-root-obstruction-replay.json
```
