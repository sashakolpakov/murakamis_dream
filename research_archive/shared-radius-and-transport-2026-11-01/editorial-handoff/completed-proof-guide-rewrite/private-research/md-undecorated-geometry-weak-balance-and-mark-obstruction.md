# Weak balance, the two circles beside a marked edge, and an obstruction to choosing the mark

This note concerns the original matched triangulated sphere, with no new crossing circles or terminal tangles. It gives a geometric necessary condition for weak balance at a proposed mark and proves that no choice of mark enforces weak balance in general. The obstruction applies to arbitrarily large simple spheres that admit knot parity patterns.

The positive result in the companion power-flattening theorem remains useful: if one mark satisfies weak balance, one shared change of Cauchy weights gives a strict full-source gap. The conclusion here is that choosing the mark cannot ensure its hypothesis. A different shared coefficient estimate may still succeed; in particular, the all-even bipyramid certificate uses several conditioned weight vectors even though every complete marked packing fails weak balance.

## 1. The exact triangle potential and what weak balance means

Fix a simple triangulated sphere \(T\), a perfect matching of its cubic dual, and a nonmatching white edge \(uv\). This edge is the marked strand edge. Its endpoints are the protected faces and have target zero in the original homogeneous source. Every other face has target \(d=N-1\).

At a matching edge \(xy\), the adjacent triangles have middle vertices \(b,c\). The ordered operator uses the quartet \((x,b,c,y)\). The letter used for a face below also denotes its nonnegative curvature in the complete marked packing. Curvature means reciprocal Euclidean radius; the two protected circles have been sent to parallel lines and have curvature zero.

The original triangle rate is
\[
\begin{aligned}
 Q(w_1,w_2,w_3)
 &=\max_{\substack{\alpha_i\ge0\\\sum_i\alpha_i=1/2}}
       \sum_i\{f(\alpha_i)+\alpha_i\log w_i\},\\
 f(t)&=\frac{\Lambda(\pi t)+\Lambda(\pi/2-\pi t)}{\pi}.
\end{aligned}
\tag{1}
\]
For a zero weight one imposes the corresponding \(\alpha_i=0\).
In particular
\[
 Q(A,0,0)=\tfrac12\log A,\qquad
 Q(cw_1,cw_2,cw_3)=Q(w_1,w_2,w_3)+\tfrac12\log c.
\tag{2}
\]
No volume constant has been removed. The local complete rate and its balance gap are
\[
 X=Q(x,b,y)+Q(x,c,y),\qquad
 B=X-\log\max(b,c).
\tag{3}
\]
The second expression is used only if a middle is positive. Weak balance means \(B\ge0\) at every matching edge. If both middles are protected, the two one-sided sectors vanish and there is no inequality to impose.

The outer pair \(xy\) is matching and cannot be the protected nonmatching pair. Thus \(x+y>0\). Consequently the triangle containing a positive overloaded middle has at least two positive weights.

Here and below, symmetry of the scalar function \(Q\) is used only to evaluate (3). It does not permute the legs of a physical operator.

## 2. A sharp local condition at the marked edge

Send the marked contact \(u\cap v\) to infinity. After a similarity the two protected disks are the outside half-planes bounded by
\[
 Y=0,\qquad Y=2H,\qquad H>0.
\tag{4}
\]
Consider either of the two triangles incident to \(uv\), and denote its third disk by \(a\). Since \(a\) is tangent to both parallel lines and lies in their strip, its radius is exactly \(H\).

The edge \(uv\) is not matching. The triangle \(uva\) is therefore matched across \(ua\) or \(va\). Write \(c\) for the third vertex of the triangle on the other side of that matching edge. The four vertices are distinct: two different triangles in a simple triangulated sphere cannot have the same three vertices. The disk \(c\) is ordinary, lies in the strip, and has radius \(h>0\).

Up to the literal choice of which side is the input middle, this matching edge has two protected entries, one outer and one middle. Its remaining entries are \(1/H\) and \(1/h\). Equations (1)–(2) therefore give exactly
\[
 B=F(r)-\log r,\qquad
 r=\frac{H}{h},\qquad
 F(r)=Q(1,r,0)=\frac2\pi\operatorname{Ti}_2(\sqrt r),
\tag{5}
\]
where
\[
 \operatorname{Ti}_2(t)=\int_0^t\frac{\arctan s}{s}\,ds.
\tag{6}
\]
For completeness, the supported two-variable maximum in (1) satisfies
\[
 \frac{\partial F}{\partial\log r}
       =\frac1\pi\arctan\sqrt r,\qquad F(0)=0,
\tag{7}
\]
which integrates to (5). Thus the additive constant in (5) is fixed by the original monomial endpoint.

Put \(G(r)=F(r)-\log r\). Then
\[
 \frac{dG}{d\log r}
       =\frac1\pi\arctan\sqrt r-1<0.
\tag{8}
\]
Moreover, \(G(r)\to+\infty\) as \(r\downarrow0\) and \(G(r)\to-\infty\) as \(r\to\infty\). The latter follows from
\[
 \operatorname{Ti}_2(t)-\operatorname{Ti}_2(t^{-1})
       =\frac\pi2\log t.
\tag{9}
\]
There is therefore a unique positive number \(r_*\) with \(G(r_*)=0\).

It satisfies
\[
 \frac94<r_*<3.
\tag{10}
\]
The lower bound follows from the explicit rational estimate
\[
 G(9/4)>
 \frac{155342}{382725}-\frac{177391}{437500}
 =\frac{57269}{136687500}>\frac1{2500}.
\tag{11}
\]
Indeed, use the alternating four-term lower sum for
\(\operatorname{Ti}_2(2/3)\), the upper bound \(\pi<22/7\), and the positive \(\operatorname{artanh}(1/5)\) series for \(\log(3/2)\), together with (9). For the upper bound in (10), \(\operatorname{Ti}_2(t)<t\), \(\pi>3\), \(\sqrt3>5/3\), and \(\log3>1\) give
\[
 G(3)=\frac2\pi\operatorname{Ti}_2(1/\sqrt3)
                -\frac12\log3<-\frac1{10}.
\tag{12}
\]

**Marked-edge necessary condition.** At each of the two triangles beside the proposed marked edge, the fourth circle selected by its original matching must have
\[
                         h\ge H/r_*.
\tag{13}
\]
If either circle violates (13), the complete packing fails weak balance. This is an exact condition for these two particular matching edges, not a sufficient condition for all other edges.

The condition is intrinsic to the marked packing. Two Möbius maps sending the same contact to infinity differ by an affine map; their effect on all radii is one common positive factor. Thus neither \(H/h\) nor (5) can be improved by changing the Möbius frame after fixing the mark.

There is also an angular form. Place the radius-\(H\) disk at \((0,H)\), and suppose the fourth disk is tangent to the lower line and lies on its right. Its center is \((2\sqrt{Hh},h)\). If \(\varphi\) is the angle on the first circle from its lower contact to its contact with the fourth disk, then
\[
 \tan(\varphi/2)=\sqrt{h/H},\qquad
 r=\cot^2(\varphi/2).
\tag{14}
\]
Condition (13) is equivalently
\(\varphi\ge2\arctan(r_*^{-1/2})\), with the reflected convention on the other side. This angle refers to the strip-normalized contact circle, not to the dihedral angle of the three-dimensional polyhedron.

## 3. An arbitrary-size obstruction that exhausts every mark

Let \(m\ge6\) be even and set
\[
 \theta=\pi/m,\qquad a=\csc\theta.
\tag{15}
\]
Use the bipyramid with oriented triangles
\[
 (N,v_j,v_{j+1}),\qquad(S,v_{j+1},v_j),
                  \qquad j\in\mathbb Z/m.
\tag{16}
\]
Match north spokes \(Nv_j\) of one parity and south spokes \(Sv_j\) of either parity. Each triangle is matched exactly once. All equatorial edges are nonmatching.

Its complete packing consists of the radius-\((a-1)\) disk \(N\), the exterior disk \(S=\{|z|\ge a+1\}\), and unit disks \(v_j\) centered at \(ae^{2ij\theta}\). Consecutive centers are distance two; all nonconsecutive center distances are greater than two. The unit disks are tangent to both apex disks and there are no extra contacts. This gives exactly the labeled simple sphere (16).

For \(w=1/(z-p)\), an interior circle of center \(c\), radius \(R\), not containing \(p\), has curvature
\[
 k_p(c,R)=\frac{|c-p|^2-R^2}{R}.
\tag{17}
\]
For the exterior disk \(S\),
\[
 k_p(S)=\frac{(a+1)^2-|p|^2}{a+1}.
\tag{18}
\]
These follow by substitution in the circle equation. Protected circles have zero curvature.

For a permitted north-spoke mark, reindex it as \(Nv_0\); the neighboring north matching spokes have odd indices. Its contact is \(p=a-1\), so
\[
 k_N=k_{v_0}=0,\qquad
 k_{v_j}=4a(a-1)\sin^2(j\theta).
\tag{19}
\]
The matching edge \(Nv_1\) has the ordered quartet
\((N,v_0,v_2,v_1)\), hence after scaling \((0,0,r,1)\), where
\[
                  r=4\cos^2\theta.
\tag{20}
\]
For a permitted south-spoke mark \(Sv_0\), the contact is \(p=a+1\) and the same calculation gives
\[
 k_S=k_{v_0}=0,\qquad
 k_{v_j}=4a(a+1)\sin^2(j\theta).
\tag{21}
\]
The south orientation gives the quartet \((S,v_2,v_0,v_1)\), hence \((0,r,0,1)\). The same value (20) results.

For an equatorial mark \(v_0v_1\), its contact is \(p=a\cos\theta\,e^{i\theta}\), and
\[
\begin{aligned}
 k_N=k_S&=2,\qquad k_{v_0}=k_{v_1}=0,\\
 k_{v_j}&=4a^2\cos\theta\sin(j\theta)\sin((j-1)\theta),\\
 k_{v_2}=k_{v_{-1}}&=8\cos^2\theta.
\end{aligned}
\tag{22}
\]
Exactly one of \(Nv_0,Nv_1\) is matching. Its ordered quartet is respectively \((1,r,0,0)\) or \((1,0,r,0)\), after scaling by two. Again \(r\) is (20).

Equations (19)–(22) cover every nonmatching white edge and either matching offset on either hemisphere. Because \(r\ge3>r_*\), (5), (8), and (12) give
\[
       B\le G(3)<-\frac{1}{10}.
\tag{23}
\]
This holds at at least one matching edge for every mark. It disproves a universal choice-of-mark weak-balance theorem, including the nonstrict version.

## 4. These are original knot diagrams, not abstract packing graphs

The oriented sphere (16) and its dual matching determine the usual two projection balls with the labeled crossing-disk identifications. Contracting each matched dual edge yields the connected four-valent projection graph; small disjoint balls around its vertices contain the physical two-strand crossing boxes. The remaining dual arcs join their four endpoints in the original planar order. The auxiliary circles bound the recorded two-punctured crossing disks in these balls.

Thus this is an original augmented link in \(S^3\), with a well-defined ordered face source. No covering of the link exterior, identification of unrelated tensor networks, or replacement by a different matching is used in the estimate.

There is a parity pattern producing one main knot. To see this without a special knot calculation, start with any of the two allowed pairings at each box. If the main strands have more than one component, connectedness of the projection implies that some box has its two local strands on different components. Switching its parity replaces the current pairing by the other physical pairing and merges exactly those two components. Repeating reduces the component count to one. Once selected, retain this parity pattern; independent long integer powers of those parities do not change it.

For the opposite-offset bipyramid one can alternatively use the literal annular three-strand presentation. The original boxes alternate the two adjacent generators. Making one box of each generator odd and every other box even gives a three-cycle permutation, hence a knot. This optional identification is not needed for (23), which includes both matching-offset types.

The complete packing and its weak-balance failure do not depend on the integer twists subsequently inserted. The failure of (18) in the power-flattening note is therefore compatible with fixed independently long fillings of these original knot diagrams.

## 5. What the power-flattening argument does and does not supply

Its entropy calculation is consistent with the original normalization. In logarithmic ordinary weights \(q\), the supported triangle potential satisfies
\[
 E_t(\beta)=Q_t(\beta q)-\beta q\cdot\nabla Q_t(\beta q),
 \qquad
 E_t'(\beta)=-\beta q^{\mathsf T}Q_t''(\beta q)q\le0.
\tag{24}
\]
The overloaded-middle triangle has at least two ordinary corners, so \(E_t(1)>0\). The local gain under \(q\mapsto(1-t)q\) is linear in \(t\), while the whole complete-action cost is quadratic because the original complete vector is stationary. This proves the stated weak-balance implication on every fixed simple matched sphere, regardless of its cycles.

The bipyramid calculation does not disprove the companion criterion that permits a positive imbalance. It shows that the zero-defect hypothesis cannot be obtained merely by selecting a different protected pair. Nor does it rule out several conditioned Cauchy vectors, spectral cancellation, or another full-source estimate.

The known all-even bipyramid proof is precisely a distinction of this kind: the complete vectors fail (23), whereas three explicit conditioned vectors control the original full remainder. Its success cannot be rephrased as a weak-balance mark.

## 6. Scope of a positive geometric classification

The local test (13) is a useful preliminary obstruction for any proposed combinatorial class: it uses only the two matching pairs incident to the candidate marked edge. Passing it still leaves all nonincident matching pairs to check. A graph degree bound or a symmetry that does not preserve the protected contact does not supply those inequalities.

No new arbitrary-cycle positive family is proved here. The precise completed conclusion is the marked-edge radius/angle criterion and the all-marks obstruction (23). Equal-middle reflection families and the published reduced-layer family remain positive examples with their own geometric arguments. Constructing a wider positive class requires an additional packing comparison; neither a covering operation nor changing the diagram is a mark change.

The primitive filling equations and the original hyperbolic volume are unchanged by any allowed Cauchy reweighting. This note supplies no new filling theorem from the failed test and makes no claim that a negative value in (23) is a volume-conjecture obstruction.
