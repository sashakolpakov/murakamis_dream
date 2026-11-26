# A simple-sphere family for which every mark fails complete-radius balance

This concerns a sufficient estimate for the original full source. It does
not assert failure of the invariant's volume limit or of a sharper
fixed-sector comparison. No terminal tangle is added to the diagrams
studied here.

## 1. Statement and the exact local normalization

Let \(m\ge6\) be even. Take the bipyramid over the cyclically ordered
vertices \(v_0,\ldots,v_{m-1}\), with apices \(N,S\). Give its faces the
orientations
\[
 (N,v_j,v_{j+1}),\qquad (S,v_{j+1},v_j),\qquad j\in\mathbb Z/m.
\tag{1}
\]
Choose independently \(\alpha,\beta\in\{0,1\}\). Match the top
triangles across the spokes \(Nv_j\) with \(j\equiv\alpha\pmod2\),
and the bottom triangles across the spokes \(Sv_j\) with
\(j\equiv\beta\pmod2\). Each triangle is matched exactly once.
No equatorial edge is matching.

The resulting original augmented diagram has \(m\) crossing circles
and \(m+2\) white faces. Its white sphere is simple. The literal
matched-sphere construction produces a link in \(S^3\) and admits
a parity pattern with one main knot. Fix any such pattern and retain
its original disk frames and ordered source factors.

**Theorem.** For every permissible reduced mark, meaning every
nonmatching white edge, its complete marked packing has a matching
circle whose strict balance inequality fails by more than \(1/10\).
This holds for both choices of \(\alpha\) and both choices of
\(\beta\), and for every Möbius frame realizing the given mark.

The balance expression at a quartet \((x,b,c,y)\) is
\[
 B(x,b,c,y)=Q(x,b,y)+Q(x,c,y)-\log\max(b,c),
\tag{2}
\]
when at least one middle is positive. The potential \(Q\) is the
source-normalized half-degree triangle action of
`actual_triangle_entropy_algebraic_balance.md`, not a renormalized
volume atom. In particular
\[
 Q(A,0,0)=\tfrac12\log A,\qquad
 Q(1,r,0)=F(r)=\frac2\pi\operatorname{Ti}_2(\sqrt r),
\quad
 \operatorname{Ti}_2(t)=\int_0^t\frac{\arctan u}{u}\,du.
\tag{3}
\]
The source's positive triangle formula is symmetric in its three
weights. Using that scalar symmetry in (2) is not a change of the
ordered four-leg operator or of its carrier.

## 2. The original complete packing

Put
\[
 \theta=\frac\pi m,\qquad a=\csc\theta.
\tag{4}
\]
In the complex plane take the following white disks on the sphere:

* the interior disk \(N\) of center zero and radius \(a-1\);
* the exterior disk \(S=\{|z|\ge a+1\}\);
* the unit disks \(v_j\) of centers \(a e^{2ij\theta}\).

Consecutive unit centers have distance \(2a\sin\theta=2\).
Nonconsecutive ones have strictly larger distance. Every unit disk is
tangent to both \(N\) and \(S\), and there are no other contacts.
Thus this is the labeled bipyramidal packing, with precisely the
faces (1). All disks are positive and nondegenerate since \(a\ge2\).
The contact-circle construction supplies its convex ideal right-angled
polyhedron. The original matching and face maps give the augmented
exterior, as in `research_matched_sphere_morse_source.md` and the
simple-sphere construction of `actual_balanced_terminal_fan_volume.md`.

For a chosen contact \(p\), use \(w=1/(z-p)\) to send it to infinity.
For an ordinary interior disk of center \(c\), radius \(r\), not
containing \(p\), its new curvature is
\[
 k_p(c,r)=\frac{|c-p|^2-r^2}{r}.
\tag{5}
\]
It is zero when the boundary contains \(p\). For the exterior disk
of radius \(a+1\) the positive transformed curvature is instead
\[
 k_p(S)=\frac{(a+1)^2-|p|^2}{a+1}.
\tag{6}
\]
These formulas follow by substituting \(z=p+1/w\) into the circle
equation. A subsequent similarity changes all curvatures by the same
positive factor. Half-degree homogeneity makes (2) invariant under
that factor.

There is no further continuous Möbius optimization after fixing the
mark. Two Möbius transformations sending the same contact to infinity
differ by an affine map \(w\mapsto Aw+B\), \(A\ne0\). Its effect on
curvatures is just the common factor \(|A|^{-1}\). The two marked
white circles become parallel lines, and no other white circle does,
because the original packing has no unintended triple contact.

## 3. Every permissible spoke mark

Suppose first that the mark is \(Nv_k\). It is permissible exactly
when \(k\not\equiv\alpha\pmod2\). Rotate the indexing so that
\(k=0\). Then both neighboring top spokes have odd index and are
matching. The marked contact is \(p=a-1\), and (5) gives
\[
 L_N=L_{v_0}=0,\qquad
 L_{v_j}=4a(a-1)\sin^2(j\theta).
\tag{7}
\]
The top matching circle at \(Nv_1\) has the literal oriented
source quartet
\[
 H(N,v_0,v_2,v_1).
\tag{8}
\]
Indeed the two top faces are \((N,v_0,v_1)\) and
\((N,v_1,v_2)\); their cyclic quadrilateral is
\((N,v_0,v_1,v_2)\). In the convention \(H(x,b,c,y)\), the
input and output middle faces are \(v_0,v_2\), respectively.
After common scaling by \(L_{v_1}\), (8) is exactly
\[
 (x,b,c,y)=(0,0,r,1),\qquad
 r=\frac{\sin^2(2\theta)}{\sin^2\theta}=4\cos^2\theta.
\tag{9}
\]
The two protected vertices are one outer and one middle, namely
\(N,v_0\). They are not the two matching endpoints.

For a permissible south mark \(Sv_k\), reindex to \(k=0\) and use
\(p=a+1\). Then
\[
 L_S=L_{v_0}=0,\qquad
 L_{v_j}=4a(a+1)\sin^2(j\theta).
\tag{10}
\]
The bottom orientation in (1) makes its matching source quartet
\(H(S,v_2,v_0,v_1)\). Its normalized value is
\((0,r,0,1)\), with exactly the same \(r\). This treats all
permissible spoke marks, with either matching offset on either
hemisphere. It uses their recorded source order, not a reflection
of an open coupon.

## 4. Every equatorial mark

Every equatorial edge \(v_kv_{k+1}\) is nonmatching and therefore a
permissible mark. Reindex it as \(v_0v_1\). Its contact is
\[
 p=a\cos\theta\,e^{i\theta}.
\tag{11}
\]
Equations (5)--(6) now give
\[
 L_N=L_S=2,\qquad L_{v_0}=L_{v_1}=0,
\]
\[
 L_{v_j}=4a^2\cos\theta\,
       \sin(j\theta)\sin((j-1)\theta),\qquad
 L_{v_2}=L_{v_{-1}}=8\cos^2\theta.
\tag{12}
\]
For example \(|p|^2=a^2-1\), so the numerator in the interior
apex formula is \(2(a-1)\), and the exterior apex formula has
numerator \(2(a+1)\). This checks the two equal positive apex
curvatures, including the orientation of the exterior disk.

Exactly one of the top spokes \(Nv_0,Nv_1\) is matching. If it is
\(Nv_1\), its quartet (8), scaled by two, is
\((1,0,r,0)\). If it is \(Nv_0\), its quartet is
\(H(N,v_{-1},v_1,v_0)\), giving \((1,r,0,0)\).
In both cases \(r=4\cos^2\theta\). The bottom matching offset
does not enter this argument. Thus it covers every equatorial mark
for all four pairs \((\alpha,\beta)\).

Together (9)--(12) exhaust all permissible marks: the white edges are
exactly the north spokes, south spokes, and equatorial edges.

## 5. A uniform exact negative gap

Each of the literal quartets just found has balance gap
\[
 B=F(r)-\log r.
\tag{13}
\]
This uses the zero monomial value \(Q(1,0,0)=0\) and the scalar
triangle symmetry explained after (3). It does not regularize either
protected zero.

The identity
\(\arctan t+\arctan(t^{-1})=\pi/2\) gives, by differentiation
and evaluation at one,
\[
 \operatorname{Ti}_2(t)-\operatorname{Ti}_2(t^{-1})
                  =\frac\pi2\log t.
\]
Consequently
\[
 F(r)-\log r
  =\frac2\pi\operatorname{Ti}_2(r^{-1/2})-\frac12\log r.
\tag{14}
\]
Since \(m\ge6\), \(r=4\cos^2(\pi/m)\ge3\). For \(t>0\),
\(\operatorname{Ti}_2(t)<t\). Also \(\pi>3\),
\(\sqrt3>5/3\), and
\(\log3=2\operatorname{artanh}(1/2)>1\). Therefore
\[
 F(r)-\log r
 <\frac2{\pi\sqrt3}-\frac12\log3
 <\frac25-\frac12=-\frac1{10}.
\tag{15}
\]
The strictness is uniform over every size \(m\), matching offset,
mark, and allowed common scale in the family. It is a source-normalized
entropy bound, not a comparison of uncalibrated local volumes.

## 6. Literal knot realization and the scope of the obstruction

The top and bottom spoke matchings above are perfect matchings of
the cubic dual. Every matched pair has four distinct white vertices.
The actual construction contracts disjoint neighborhoods of the matched
dual edges to four-terminal boxes, uses the physical untwisted pairing
\((0,1),(2,3)\), and connects the outside terminals by the embedded
nonmatching dual edges. The perpendicular crossing circles lie in
disjoint balls. Thus it is a link in \(S^3\) with precisely this
white sphere and source ordering.

Its incidence graph has the untwisted physical main circles as vertices
and the crossing boxes as edges. It is connected. Choosing a spanning
tree and making exactly its boxes odd merges the main circles one at
a time. This gives a knot parity pattern for each member of the family,
with either sign at each odd box. Fixing that parity and assigning
independently long powers changes no endpoint pairing. This is a
topological qualification of the obstruction family; no new volume
theorem for its undeformed full source is inferred.

The result excludes a universal theorem asserting that some permissible
mark makes the complete packing satisfy the local balance inequalities.
It also excludes an extra continuous Möbius parameter as a remedy after
the mark is fixed. The scalar Cauchy radii used in a genuinely shared
fixed-sector estimate remain independent comparison variables. The
present argument does not constrain the success of those sharper
estimates, finite sector covers, or cancellation in the original signed
source.

## 7. Why a single unconditioned envelope cannot be repaired by new weights

Fix one mark of any connected simple white sphere. Put \(z_f=\log L_f\)
at its ordinary faces and keep its protected coordinates zero. Let
\[
 V_C(z)=\sum_e X_e(z)-\sum_f z_f,\qquad
 X_e=Q(x_e,b_e,y_e)+Q(x_e,c_e,y_e),
\]
\[
 V_H(z)=\sum_e\max\{X_e(z),\log b_e,\log c_e\}-\sum_fz_f,
\tag{16}
\]
where protected logarithms are omitted. These are the shared complete
cost and the unconditioned local envelope, respectively. The complete
packing minimizes \(V_C\), uniquely modulo common scaling, with value
\(\Phi\).

For clarity this minimum cannot be approached by an escaping sequence
after fixing scale. Let \(\alpha_{tf}>0\) be the complete supported
triangle loads, of row sum \(1/2\) and ordinary column sum one.
For a direction \(z\), the recession function is
\[
 V_C^\infty(z)
 =\sum_t\left(\frac12\max_{f\in t,\,L_f>0}z_f
                   -\sum_f\alpha_{tf}z_f\right).
\tag{17}
\]
Every summand is nonnegative. It is zero only when all supported
coordinates of that triangle agree. The ordinary adjacency graph is
connected after deleting the two protected adjacent vertices; every
ordinary adjacency is detected in a supported triangle. Hence (17)
vanishes only for a common constant. On the unit sphere of a fixed
scale slice it has a positive minimum. The bounded closed triangle
entropy then makes \(V_C\), and thus \(V_H\), coercive on that slice.

It follows that
\[
 \inf V_H=\Phi
 \quad\Longleftrightarrow\quad
 \max\{X_e,\log b_e,\log c_e\}=X_e
 \text{ at every complete quartet.}
\tag{18}
\]
Indeed \(V_H\ge V_C\ge\Phi\); equality forces the unique
complete minimizer and equality of every nonnegative local difference.
Conversely that minimizer realizes equality if all the local conditions
hold. A failed complete condition therefore gives a strictly larger
minimum for this single envelope, even after arbitrary shared positive
vertex weights. For the family above this happens at every mark.

This last observation is deliberately about the unconditioned envelope
(16). A genuine fixed non-CROSS sector fixes at least one local label;
its cost is different. A finite collection of conditional shared-radius
certificates can succeed when (16) or an anchored envelope fails. No
minimax interchange or fixed-sector obstruction is claimed here.
