# The all-even shared-radius estimate and its original closed braid

This note fixes an even integer \(m\ge6\). It checks the three shared-radius vectors against the original opposite-offset sphere and gives a separate proof that the same-sign long-syllable case cannot hide a nonhyperbolic braid closure. The diagram size and the integer crossing powers are fixed before the quantum level tends to infinity.

The two inputs being checked are [the shared-radius proof](md-bipyramid-all-even-shared-radius-family.md), SHA256 `16e0411e6e521f221ea7c549b45521b32fc7979039d0c37a578ec58bd372a97e`, and [the original diagram and filling proof](md-bipyramid-all-even-original-diagram-and-filling.md), SHA256 `eb3c332afe2ab827bf0aad253a39fe0a3629c8070e390c39daf4d6d1ebadff2a`. Neither input has been changed.

## 1. The literal matching, braid and knot condition

The oriented sphere triangles are
\[
 (N_0,v_j,v_{j+1}),\qquad(S_0,v_{j+1},v_j),
 \qquad j\in\mathbb Z/m.
 \tag{1}
\]
Match \(N_0v_j\) at odd \(j\) and \(S_0v_j\) at even \(j\). The cyclic quadrilateral order is \((x,b,y,c)\), whereas the source argument order is \((x,b,c,y)\). Thus the two source rows are
\[
 (N_0,v_{j-1},v_{j+1},v_j)\quad(j\text{ odd}),\qquad
 (S_0,v_{j+1},v_{j-1},v_j)\quad(j\text{ even}).
 \tag{2}
\]
In particular the south middle order cannot be replaced by the north order when choosing the left anchor.

For sides \(0=xb,1=by,2=yc,3=cx\), the pure main strands pair \((0,3),(1,2)\); either odd half twist pairs \((0,2),(1,3)\). Following those exact pairs gives three annular tracks in the pure diagram. North boxes act on the inner two tracks and south boxes on the outer two. At the south box the transported chart reverses both time and transverse order, so it is a plane half-turn. It fixes the two crossing diagonals, preserves the overpass and retains the exponent of \(R^n\). There is no mirror operation or cancellation of a typed quarter-turn here.

Cutting the annulus immediately before box zero therefore gives
\[
 \beta_m=\sigma_2^{n_0}\sigma_1^{n_1}
           \sigma_2^{n_2}\sigma_1^{n_3}\cdots
           \sigma_2^{n_{m-2}}\sigma_1^{n_{m-1}}.
 \tag{3}
\]
The crossing circles surround exactly these original syllables. The axis of the annulus is not included in the link. A closure is a knot if and only if the permutation of (3) is a three-cycle. One odd exponent of each generator type, and all other exponents even, is a knot-producing pattern for every \(m\). All odd exponents instead give \(\gcd(3,m/2)\) components; that pattern must not be called a knot without the divisibility check.

![The sphere matching and its annular braid](md-bipyramid-matching-annular-braid.svg)

*The drawing uses \(m=6\). The two disks are hemispheres of the white sphere, with opposite boundary orientations. Colored matching edges and annular boxes carry the same crossing-disk index. The boxes contain the original signed powers, so the word below the drawing is the exact ordinary braid closure.*

## 2. The packing is the one used by the coefficient estimate

Let \(\theta=\pi/m\), \(a=\csc\theta\). The complete packing consists of the disk of radius \(a-1\) centered at zero, the exterior disk bounded by radius \(a+1\), and the unit disks centered at \(ae^{2ij\theta}\). Adjacent rim distances are \(2a\sin\theta=2\), all other rim distances are larger than two, and each rim disk is tangent to both pole disks. These are precisely the edges of (1).

Mark \(v_0v_1\). Its contact point is \(p=a\cos\theta e^{i\theta}\). Under \(w=2/(z-p)\), both pole disks become bounded unit disks, while \(v_0,v_1\) become the two boundary lines of a strip of width two. The other curvatures are
\[
 k_j=\frac{\cos\theta}{\sin^2\theta}
       \bigl[\cos\theta-\cos((2j-1)\theta)\bigr]
     =\frac{2\cos\theta}{\sin^2\theta}
       \sin(j\theta)\sin((j-1)\theta).
 \tag{4}
\]
The sign of the exterior-circle inversion is accounted for before taking its radius. Hence \(k_0=k_1=0\) exactly and every other \(k_j\) is positive. This is a curvature vector, not the reciprocal convention accidentally applied twice.

The packing's star equations give the original coefficient saddle. If \(Q\) is the calibrated triangle entropy and \(\Lambda(t)=-\int_0^t\log|2\sin u|\,du\), then
\[
 \Phi_m=2\sum_j Q(1,k_j,k_{j+1})
                -\sum_{j=2}^{m-1}\log k_j.
 \tag{5}
\]
The ordered cut of the two right-angled polyhedra, with the matching in (1), gives
\[
 2\pi\Phi_m
 =8m\left[
  \Lambda\!\left(\frac{\pi}{4}+\frac{\pi}{2m}\right)
 +\Lambda\!\left(\frac{\pi}{4}-\frac{\pi}{2m}\right)
 \right]
 =\operatorname{Vol}(Y_m^\epsilon).
 \tag{6}
\]
This matching is not the usual pretzel matching of the same polyhedron. The source uses the former throughout. Its ordinary incidence graph is connected after deleting the two protected vertices, and its only common-scale Hessian kernel is removed by the coefficient gauge.

## 3. Uniform inequalities, including the two protected-zero anchors

The source local rates are
\[
 \begin{split}
 X&=Q(x,b,y)+Q(x,c,y),\\
 H&=\max\bigl(X,\{\log b:b>0\},\{\log c:c>0\}\bigr),\\
 A_L&=\max\bigl(\log c,Q(x,b,y)+\tfrac12\log c\bigr),\quad c>0,\\
 A_R&=\max\bigl(\log b,Q(x,c,y)+\tfrac12\log b\bigr),\quad b>0.
 \end{split}
 \tag{7}
\]
A protected overloaded middle gives a zero sector and is omitted. These rates are the true uniform local envelopes: for example \(Q(x,b,y)\ge\frac12\log b\), so the mixed spectator terms are already at most \(X\). No independent optimization of shared occurrences is being made.

Put \(F(r)=Q(1,r,0)\), \(a_*=9/4\), \(C=27/4\), and
\[
 \lambda=\frac{9}{16\cos^2\theta},\qquad w_j=\lambda k_j.
 \tag{8}
\]
The poles remain one. The vector \(W\) has
\[
 w_2=w_{m-1}=a_*,\qquad
 w_3=w_{m-2}=c=a_*(4\cos^2\theta-1)\in[9/2,C].
 \tag{9}
\]
Use \(W\) except at \(1L\), where replace \(w_2\) by one, and at \(0L\), where replace \(w_{m-1}\) by one.

Here is a direct account of the bounds that cover all sizes.

**The total scaling cost.** For \(P(t)\) obtained by scaling every ordinary rim weight by \(t\), the pole half-angles are
\[
 \alpha_j(t)=
 \arctan\frac1{\sqrt{t(k_j+k_{j+1})+t^2k_jk_{j+1}}}.
 \tag{10}
\]
The monomial triangle is \(j=0\), with \(\alpha_0=\pi/2\). The complete pole star has \(\sum_j\alpha_j(1)=\pi\). Writing \(D^2=t(u+v)+t^2uv\),
\[
 -\frac{d\alpha}{d\log t}
 =\frac{t(u+v)+2t^2uv}{2D(1+D^2)}
 \le\frac{D}{1+D^2}\le\alpha.
 \tag{11}
\]
The first inequality is just \(t(u+v)+2t^2uv\le2D^2\), including a single zero entry. It implies \(\alpha_j(t)\le\alpha_j(1)/t\), and hence
\[
 P(\lambda)-\Phi_m
 \le\lambda^{-1}-1+\log\lambda
 \le D_0=\frac{16}{9}-1+\log\frac9{16}.
 \tag{12}
\]
The direction of integration is important: the lower derivative bound is integrated from \(\lambda\) to one. This is the whole action cost, with no factor growing with \(m\).

**Ordinary anchors.** For \(3\le j\le m-2\), the two neighbor ratios are
\(\sin((j-2)\theta)/\sin(j\theta)\) and
\(\sin((j+1)\theta)/\sin((j-1)\theta)\). Their monotonicity gives the uniform range \([1/3,2]\). Dropping the pole entry and using that \(F\) is increasing while \(F(r)-\log r\) and \(F(r)-\frac12\log r\) decrease gives
\[
 \begin{split}
 X-\log\max(b,c)&\ge F(1/3)+F(2)-\log2,\\
 Q(x,b,y)-\tfrac12\log b&\ge F(2)-\tfrac12\log2.
 \end{split}
 \tag{13}
\]
At \(j=2,m-1\), use \(b=0\) or \(c=0\), outer rim \(a_*\), and the other middle \(c\le C\). The corresponding losses are at least
\[
 F(a_*)+Q(1,C,a_*)-\log C,\qquad
 Q(1,C,a_*)-\tfrac12\log C.
 \tag{14}
\]
Thus every unanchored coupon at \(W\) has \(H=X\), including \(j=0,1\), since \(F(a_*)>\log a_*\).

**The two near-mark anchors.** At \(1L\), replacing \(w_2\) by one makes the anchor rate zero. Its complete rate is \(F(1)\). The whole complete-action change and only possible spectator excess are
\[
 \begin{split}
 T(c)&=2[F(1)-F(a_*)+Q(1,1,c)-Q(1,a_*,c)]+\log a_*,\\
 E(c)&=\max(0,\log c-F(1)-Q(1,1,c)).
 \end{split}
 \tag{15}
\]
Both increase with \(c\), so they are bounded by their values at \(C\). The only other changed coupon is \(j=3\), where the balance is at least \(F(4/27)+F(2)-\log2>0\). At the endpoint \(m=6\), \(w_4=w_3=c\), which still satisfies every ratio used here. Thus no uncounted near-mark coupon appears in the smallest size. Reflection \(j\mapsto1-j\), together with exchange of poles, maps the scalar \(L\)-anchor formula to the \(0L\) formula and preserves the full shared vector. It does not reverse an ordered quantum coupon.

The fixed Arb enclosures were replayed without changing the frozen inputs. The weakest ordinary loss minus the global scaling cost is
\[
 0.283921301410\ldots-0.202413632874\ldots>0.0815.
 \tag{16}
\]
The near-mark correction saves more than \(0.371241794242\ldots-D_0>0.1688\). The small positive spectator margin \(F(9/4)-\log(9/4)\) is enclosed below by \(0.000662828798\ldots\). Therefore the declared uniform anchor margin \(7/100\) survives.

The replay uses the absolutely bounded Fourier tail
\(\left|\Lambda(t)-\frac12\sum_{\nu\le8192}\sin(2\nu t)/\nu^2\right|\le1/16384\)
and 192-bit Arb arithmetic. It evaluates fixed constants only. The all-\(m\) conclusion comes from (10)–(15), not a sampled family.

## 4. A prime projection for every nonzero power vector

The twist-collapsed projection graph is \(G_m=C_m^2\): equator strips give edges \(j\leftrightarrow j+1\), and unmatched pole spokes give \(j\leftrightarrow j+2\). It has no two-edge cut. Indeed any nonempty proper vertex subset has at least two boundary edges in the cycle \(C_m\). If the total boundary were two, it would be a single cyclic interval and there would be no distance-two boundary. The latter condition makes its indicator two-periodic, which is incompatible with a proper interval when \(m\ge6\). Also \(G_m-\{j\}\) is connected, since the remaining distance-one edges contain a spanning path.

Replacing box \(j\) by \(|n_j|\ge1\) crossings expands its vertex into a chain with two parallel edges between successive crossing vertices and two exterior edges at each end. Let \(G(\mathbf n)\) be this expanded graph. Suppose a nonempty proper subset of its vertices had boundary at most two. If every twist chain lies wholly on one side, contraction gives a forbidden boundary of size at most two in \(G_m\).

Otherwise an internal transition along a chain contributes two boundary edges. There can be exactly one such transition, in exactly one chain, and no other boundary edge anywhere. Every other chain then lies wholly on one side. Since \(G_m-\{j\}\) is connected, all those chains lie on the same side. Both end pairs of the exceptional chain are incident to them, so its two ends must lie on that same side too. A chain cannot have exactly one internal transition with both ends on the same side. This contradiction proves
\[
                  |\partial U|\ge4
 \quad\text{for every nonempty proper }U\subset V(G(\mathbf n)).
 \tag{17}
\]
A Jordan curve meeting the projection in two edge interiors and enclosing crossings on both sides would give such a two-edge cut. Thus the displayed closure projection is prime. The argument is independent of crossing signs and uses the original projection, not an alternate presentation.

## 5. Same-sign powers cannot give torus or satellite closures

Futer, Kalfagianni and Purcell prove that a prime diagram of a closed positive braid with at least three crossings in every syllable is hyperbolic; the negative case follows by reflection. The precise statement is Corollary 1.2 of *Hyperbolic semi-adequate links*, Communications in Analysis and Geometry 23 (2015), 993–1030, [author PDF](https://users.math.msu.edu/users/kalfagia/hyp-inks.pdf).

By (17), this applies directly to (3) if every \(n_j\ge3\), or if every \(n_j\le-3\). In particular, the same-sign part of the long-filling theorem has no hidden torus, satellite or composite knot exception. This hyperbolicity is already covered by the literature and is not a new claim of the shared-radius argument.

There is also a short algebraic check of the braid itself. Under the standard map to \(\operatorname{PSL}_2(\mathbb Z)\),
\[
 \sigma_1\longmapsto
 \begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
 \sigma_2\longmapsto
 \begin{pmatrix}1&0\\-1&1\end{pmatrix}.
 \tag{18}
\]
After cyclic conjugation, a positive word consists of pairs \(\sigma_1^a\sigma_2^b\), \(a,b\ge3\). The representative
\[
 C(a,b)=
 \begin{pmatrix}ab-1&-a\\b&-1\end{pmatrix}
 \tag{19}
\]
maps the cone \(x>0,\ 0\le y/x\le1/2\) strictly into itself. Its new slope is
\[
 r'=\frac{b-r}{ab-1-ar}\in(0,1/2),
 \qquad x'\ge\frac{13}{2}x.
 \tag{20}
\]
For the upper inequality use
\((a-2)b-1-(a-2)r>0\). A product of \(m/2\) such matrices has a positive eigenvector in the cone and eigenvalue at least \((13/2)^{m/2}>1\). Its determinant is one, so its projective matrix is hyperbolic. Negative words are treated by inversion and reversal. This rules out a finite-order or parabolic projective braid matrix. That matrix check alone would not prove hyperbolicity of the closure; the diagram theorem just applied does.

For broader coverage, Futer and Purcell's *Links with no exceptional surgeries*, Commentarii Mathematici Helvetici 82 (2007), 629–664, [Theorem 1.4](https://users.monash.edu/~jpurcell/papers/futer-purcell-surgery.pdf), treats prime twist-reduced diagrams with at least six crossings per twist region. We do not use it here without a separate proof of its twist-reduction hypothesis. General closed-three-braid geometry and quantitative volume estimates are also treated in Futer–Kalfagianni–Purcell, [*Cusp areas of Farey manifolds and applications to knot theory*](https://arxiv.org/abs/0808.2716). These coverage statements do not supply the particular root-of-unity asymptotic proved by the private shared-radius argument.

## 6. Why arbitrary signed long powers still have the stated actual target

The all-sign proof is the original marked filling construction, not a same-sign argument extended by analogy. The positive two-polyhedron exterior is fixed for each half-twist pattern. Every original disk has the primitive based longitude \(P=B_{\mathrm{in}}A_{\mathrm{in}}\), and the south half-turn carries both based paths with it. The selected complete branch has
\[
 U_j=-\operatorname{Log}R_{0,j}+2\pi i\epsilon_j\delta_j,
 \qquad V_j=-4\pi i\delta_j,\qquad
 U_j+p_jV_j=-2\pi i,\qquad n_j=\epsilon_j-2p_j.
 \tag{21}
\]
For independently sufficiently long signed \(n_j\), the selected charge has
\(\operatorname{Im}\delta_j>0\), hence \(\operatorname{Re}V_j>0\). The actual small generator log periods are fixed before multiplication by \(p_j\). The rank-two logarithmic cusp lattice then completes smoothly at the primitive \(2\pi\) filling meridian. The regulator identity uses the same boundary triangulation and gives the metric volume of the original filled \(S^3\) exterior. Thus hyperbolicity and the action target are established for both signs; no abstract trace solution at a parabolic slope is being mistaken for metric filling.

The uniform source bound from Section 3 is applied at the original targets \(d=N-1\). The finite Hermite functional has norm at most \(\prod_j(1+|n_j|/2)\), independent of \(N\) for fixed powers. The already proved entire all-CROSS Morse period has a nonzero leading coefficient at the same original geometric action. Once the action drop is less than half the shared-radius margin, the full source remainder is exponentially smaller. All thresholds may depend on the fixed \(m\). The knot test in Section 1 remains mandatory.

No argument here classifies all alternate Conway presentations of these knots. The visible disk-labeled diagram has no nontrivial four-ended separation of two or more boxes on both sides, but an arbitrary isotopic presentation is a different question. Neither that coverage question nor the known hyperbolicity literature is being used to claim novelty.

## 7. Reproduction record

The fixed constant replay is [md-bipyramid-all-even-reaudit-constants.json](md-bipyramid-all-even-reaudit-constants.json). The figure files share the basename `md-bipyramid-matching-annular-braid` and are native TikZ, PDF, SVG and PNG. They illustrate one size only. All original formulas and all-size arguments remain in the two unchanged inputs identified above.

