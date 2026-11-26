# Geometric entropy gaps at the two protected-row endpoints

This note proves strict entropy bounds for the two original endpoint-conditioned sources of a protected one-sided row on any fixed matched simple triangulated sphere. The upper endpoint is a fixed-triangle face of the original angle polytope. The lower endpoint is a literal identity-smoothing capacity. Its comparison uses an explicitly constructed representation with a kernel, not an assertion that smoothing preserves volume.

The positive gaps may depend on the diagram. The result does not bound coefficients of an inverse face operator: those can mix a linear number of original face loads before their endpoint coefficients are extracted.

## 1. Original sphere, mark, and entropy

Let \(T\) be a finite oriented simple triangulated sphere with a perfect matching of its dual graph. A matched pair of triangles is the two sides of an original crossing disk. Construct the augmented link in \(S^3\) using the original sphere, disjoint disk collars, and their cyclic orders. The protected vertices are the endpoints of a chosen nonmatching edge, that is, an original strand edge.

Suppose a selected disk has the ordered triangles
\[
                 (x,b,y),\qquad(x,c,y),                 \tag{1}
\]
where \(b,y\) are protected and \(x,c\) ordinary. Simplicity makes these four vertices distinct. The matching edge is \(xy\); the protected edge is \(by\).

There are \(R\) ordinary vertices and \(2R\) triangles. The original normalized flows satisfy
\[
 a_{tf}\ge0,\qquad \sum_{f\in t}a_{tf}=\frac12,\qquad
 \sum_{t\ni f}a_{tf}=
 \begin{cases}1&f\text{ ordinary},\\0&f=b,y.\end{cases}  \tag{2}
\]
Repeated incidences arising later are counted with multiplicity. Define
\[
\begin{aligned}
 \Lambda(t)&=-\int_0^t\log|2\sin v|\,dv,\\
 f(s)&=\frac{\Lambda(\pi s)+\Lambda(\pi/2-\pi s)}{\pi},
                          &&0\le s\le\frac12,\\
 \mathcal{C}(a_1,a_2,a_3)&=\sum_i f(a_i),
                          &&\sum_i a_i=\frac12.
\end{aligned}                                          \tag{3}
\]
Thus \(f(0)=f(1/2)=0\). The calibrated triangle rate is
\[
 Q_t(L)=\max_{\substack{a_f\ge0\\\sum a_f=1/2}}
             \left(\mathcal{C}(a)+\sum_{f\in t}a_f\log L_f\right).
                                                        \tag{4}
\]
A protected zero curvature forces its corner to zero.

The original complete packing gives the unique relative-interior maximizer \(a^*\), and
\[
 \Phi_T=\sum_t\mathcal{C}(a_t^*)
       =\inf_{L>0}\left(\sum_tQ_t(L)-\sum_{f\ \mathrm{ordinary}}\log L_f\right)
       =\frac{\operatorname{Vol}(Y_T)}{2\pi}.             \tag{5}
\]
The geometric input is [the Morse geometric theorem, sections 1–2](/private/tmp/murakamis_dream-publication/notes/actual_morse_geometric_contribution.md), not a volume interpretation inferred from a formal maximum. The simple-sphere proof includes strict Hall feasibility, entropy boundary exclusion, positive multipliers, injective center-triangle development, and disjoint supporting halfspaces; separating triangles are permitted. Retained half twists change original face maps and peripheral words but not this complete volume: the specified gluing doubles the same right-angled cut polyhedron.

## 2. Original endpoint constraints

Delete only the two rows (1). For \(0\le u\le1/2\), let \(\mathcal{A}(u)\) consist of spectator flows of row mass \(1/2\), protected loads zero, and targets
\[
\begin{aligned}
 \sum_{t\ni x}a_{tx}&=1-u,& \sum_{t\ni c}a_{tc}&=u,\\
 \sum_{t\ni f}a_{tf}&=1
       &&(f\text{ ordinary},\ f\ne x,c).
\end{aligned}                                          \tag{6}
\]
Set
\[
 E_T(u)=\max_{a\in\mathcal{A}(u)}
          \sum_{t\ne t_{\mathrm{in}},t_{\mathrm{out}}}\mathcal{C}(a_t), \tag{7}
\]
with value \(-\infty\) for an infeasible target. The selected one-sided factor has four-loads
\[
                         (u,0,1-u,0).                  \tag{8}
\]
Thus (6) preserves every original shared target and every neighboring central row.

At even level \(N=2m\), \(d=N-1\), the protected row has monomials \(L_x^jL_c^{d-j}\), \(0\le j\le m-1\). The two limiting endpoints are \(j/N\to0\) and \(j/N\to1/2\). The half-block degrees \(m-1\), intervening linear factors, and \(d=N-1\) remain exact in the finite source; they produce \(O(N^{-1})\) normalized corrections.

**Endpoint theorem.** For each fixed \(T\) there are \(\gamma_0,\gamma_1>0\) such that
\[
 E_T(0)\le\Phi_T-\gamma_0,\qquad
 E_T(1/2)\le\Phi_T-\gamma_1.                             \tag{9}
\]
The corresponding inequalities persist with smaller positive gaps in neighborhoods of the endpoint face-load vectors, including small perturbations of the ordinary target vector. No uniform lower bound on \(\gamma_i\) across all sphere sizes is asserted.

## 3. Upper endpoint: one original triangle fixed at a vertex

At \(u=1/2\), append the rows
\[
 a_{t_{\mathrm{in}}}=\tfrac12e_x,\qquad
 a_{t_{\mathrm{out}}}=\tfrac12e_c.                           \tag{10}
\]
This gives an exact bijection with the face of (2) having these rows. Both rows have entropy zero. The input singleton is already forced in the original problem; the output row is not. Indeed its complete values are
\[
 a^*_{t_{\mathrm{out}},x}
  =\frac1\pi\arctan\sqrt{\frac{L_x}{L_c}}>0,\qquad
 a^*_{t_{\mathrm{out}},c}=\frac12-a^*_{t_{\mathrm{out}},x}>0.       \tag{11}
\]
For \(0<s<1/2\),
\[
                   f''(s)=-\frac{2\pi}{\sin(2\pi s)}
                          \le-2\pi.                   \tag{12}
\]
First variation at the relative-interior complete flow vanishes on the affine constraints. Integration of (12), followed by boundary continuity, gives
\[
 \sum_t\mathcal{C}(a_t)
       \le\Phi_T-\pi\sum_{t,f}|a_{tf}-a^*_{tf}|^2.       \tag{13}
\]
Forced singleton rows are fixed, so no infinite derivative at their corners is used. Consequently
\[
 E_T(1/2)\le\Phi_T
      -2\pi\bigl(a^*_{t_{\mathrm{out}},x}\bigr)^2
 =\Phi_T-\frac2\pi
       \left(\arctan\sqrt{\frac{L_x}{L_c}}\right)^2.      \tag{14}
\]
This is precisely the [fixed-triangle capacity comparison](/private/tmp/murakamis_dream-publication/notes/actual_fixed_triangle_boundary_capacity_gap.md) on the original rows. It needs neither a new diagram nor independent boundary caps.

## 4. Lower endpoint: connected marked identity smoothing

At \(u=0\), every spectator \(c\)-corner is zero. Identify \(b,c\) to a protected vertex \(\bar b\), delete the two triangles (1), and sew \(xb\) to \(xc\) and \(by\) to \(cy\) in their original orders. Call the resulting triangular sphere \(T_0\).

The following topology is literal.

* The deleted adjacent triangles form a disk with embedded quadrilateral boundary \(x,b,y,c,x\). Their complement is a triangulated disk, whose triangle-adjacency dual is connected. Sewing its two boundary paths preserves connectedness.
* Only \(b,c\) are identified. The other mark \(y\) remains distinct. The old marked strand \(by\) is sewn to \(cy\), giving the marked strand \(\bar b y\), with its original cut.
* The other matched triangle pairs and their corner orders are unchanged. The quotient is a triangular sphere cellulation. It may have loops or parallel edges; these must be retained.

Flows in \(\mathcal{A}(0)\) correspond exactly to the flows of \(T_0\): the zero \(b,c\)-corners become its zero \(\bar b\)-corners and the other demands stay unchanged. Hence
\[
                            E_T(0)=\Phi(T_0).           \tag{15}
\]
This also has an exact finite coefficient meaning. The identity kernel is
\[
 H_I(L_b,L_c)=\sum_{i=0}^dL_b^iL_c^{d-i},\qquad
                    H_I(0,L_c)=L_c^d,                 \tag{16}
\]
and therefore
\[
 [\,\prod_{f\ \mathrm{ordinary}}L_f^d\,]\,L_c^d P
 =
 [\,\prod_{\substack{f\ \mathrm{ordinary}\\f\ne c}}L_f^d\,]\,
                       P\big|_{L_c=0}.                 \tag{17}
\]
Both protected variables were already zero. This retains the shared target, not just a pointwise local bound.

## 5. General-Morse smoothing capacity and strict geometric loss

The existing smoothed-block proof is stated for flat plats. The following checks give precisely its extension needed for this single protected smoothing. They do not assert a general multiple-smoothing forest theorem.

### 5.1 Closed capacities and simple blocks

A triangular cellulation with adjacent protected marks has capacity equal to its maximum closed entropy even when no positive-radius minimizer exists. To see this, maximize continuous concave entropy on the product of row simplexes with specified face demands. Its upper semicontinuous concave value function has a closed hypograph. Separation above that hypograph supplies finite shared logarithmic multipliers approximating the maximum; infeasible demand vectors give capacity \(-\infty\) by separation in face coordinates. This is the exact normalization (4), without an additive constant.

A loop makes the polytope empty. On a side with no interior protected vertex, a one-edge disk with \(v\) interior vertices has \(2v-1\) triangles. Their total row mass \(v-1/2\) cannot meet interior demand \(v\). Such a side exists because the marks are joined by an actual edge.

For a two-edge cycle, the same side has \(2v\) triangles. Its interior demand exhausts their row mass \(v\), forcing all boundary corners there to zero. Identifying the two boundary edges separates the problem exactly into two triangular spheres: the inner one protected at the cycle vertices, and the outer one retaining the original mark. Their feasible polytopes form a Cartesian product, and entropy adds. This does not factor the finite quantum contraction.

Repeated cuts terminate. A terminal three-vertex double triangle has zero entropy. Every other terminal block is a simple sphere with the positive packing proved by Hall feasibility, boundary exclusion, and development. If \(Q_\alpha\) are its convex right-angled polyhedra, then
\[
                    2\pi\Phi(T_0)
                  =2\sum_\alpha\operatorname{Vol}(Q_\alpha). \tag{18}
\]
This is initially an equality of block quantities. The representation and the fundamental chain must still be identified.

### 5.2 Original marked group and block assembly

Use the same matched sphere \(T\) with zero retained half twists as a comparison exterior \(Y_T^0\). Its cut polyhedron is the original one, so
\[
                         \operatorname{Vol}(Y_T^0)=2\pi\Phi_T.
                                                        \tag{19}
\]
This choice does not replace a target filled knot. It only supplies a strict scalar bound for (15), whose right side is the same complete augmented volume for every original signed half-twist pattern. In particular no odd finite coupon is silently declared to be an identity.

Root the block tree. At a two-edge cut, the two shared white circles are tangent in each closed block. Send their contact to infinity and match the ordered parallel halfplanes by a positive similarity and a translation. Recursing identifies both white reflections at every shared face. A double-triangle block uses three tangent circles and has zero volume. No global embedding of all block packings is required.

Each cut crosses either two strand edges or two matching edges. Indeed its interior contains an even number of cubic-dual vertices, and each vertex has one matching incidence, so the number of crossing matching edges is even. In the strand case the original pairings identify the same main meridian. In the matching case retain the original input/output triangle pairing across blocks, rather than identifying whole auxiliary tori.

For that latter pairing, normalize the common outer parabolic product to
\[
 P=-I+H,\qquad H^2=0,\quad H\ne0,\qquad
 H=\begin{pmatrix}0&h\\0&0\end{pmatrix}.                 \tag{20}
\]
For the raw ordered puncture pair \(BA=P\), \(\operatorname{tr}A=\operatorname{tr}B=-2\), the trace relation gives \(A_{21}=4/h\), and
\[
 A_{22}=-2-A_{11},\qquad
 A_{12}=-\frac{(A_{11}+1)^2}{A_{21}}.                   \tag{21}
\]
The centralizer \(I+tH\) acts simply transitively on these pairs. Its unique input/output element is exactly the ordered three-contact shaded map. This supplies the full two-generator relation, not merely a matching eigenratio.

Morse cups and caps cause no additional obstruction. If a slice has regions \(F_0,\ldots,F_k\), its raw heads and prefixes are
\[
 H_j=\mathcal{R}_{F_j}\mathcal{R}_{F_{j-1}},\qquad
 H_j\cdots H_1=\mathcal{R}_{F_j}\mathcal{R}_{F_0}.             \tag{22}
\]
At an \(F,G,F\) cup or cap the inserted pair has product \(I\); unchanged wires keep their based region labels. Equations (21)–(22) are the literal Morse/van Kampen relations, as checked in the published Morse geometric theorem. The argument does not use a constant head count or an acyclic matching graph.

Restore the selected pure crossing circle. Its middle reflections are equal, so its ordered input and output pairs agree. Set the original auxiliary meridian to \(I\). The original threading word then satisfies both generator relations, even if the outer product is central. This yields
\[
 \rho_0:\pi_1(Y_T^0)\longrightarrow\operatorname{PSL}_2(\mathbb C),
              \qquad \rho_0(\mu_{\mathrm{selected}})=1.      \tag{23}
\]
The whole meridian is killed, not just its eigenvalue.

### 5.3 The fundamental chain and the strict inequality

The original projection and crossing-disk cuts give two balls, also for a general Morse drawing. A two-edge cut bounds a proper disk with one arc in each common white face. Both ideal endpoints develop to their contact. Collapsing it gives the closed block balls with relative degree one.

The corresponding volume limit retains the face maps. Normalize each common white pair to strip width one and use its canonical horospheres. Replace all vertices of a collapsed disk at height \(T\) with bounded horizontal coordinates. White reflections and the actual shaded maps transport these incidence decorations. Two replacement vertices have distance \(O(T^{-1})\). A tetrahedron with two finite vertices at distance \(\ell\) has absolute volume at most
\[
                     2\pi\int_0^\ell\cosh^2 t\,dt.     \tag{24}
\]
Thus the finite collapse chains have volume tending to zero. Horospherical comparison tails vanish as well. The remaining block chains have relative degree one and contribute their positive \(\operatorname{Vol}(Q_\alpha)\).

All original face boundaries cancel. Across matching cuts the shaded triangles were not cut internally and retain (21). Develop the whole second ball with one common reflection; do not reflect different blocks independently. Its opposite topological orientation gives the same positive contribution. The restored meridian has a zero-volume axis or parabolic cap. Consequently the original relative fundamental chain gives
\[
             \operatorname{Vol}(\rho_0)
                =2\sum_\alpha\operatorname{Vol}(Q_\alpha)
                =2\pi\Phi(T_0).                        \tag{25}
\]
These finite-chain details are the construction in [the smoothed-block representation proof, sections 1–4](/private/tmp/murakamis_dream-publication/notes/actual_smoothed_block_representation_volume.md). The connected sphere, adjacent marks, two cut balls, actual matching order, and variable-headcount Morse relations required for it have been verified above.

The meridian in (23) is nontrivial in the original complete hyperbolic group. The [strict kernel-volume theorem](/private/tmp/murakamis_dream-publication/notes/general_representation_volume_kernel_strictness.md), which allows arbitrary commuting peripheral images, now gives
\[
 2\pi\Phi(T_0)=\operatorname{Vol}(\rho_0)
            <\operatorname{Vol}(Y_T^0)=2\pi\Phi_T.       \tag{26}
\]
This proves the lower endpoint of (9). No regular minimum for the whole smoothing capacity, absence of digons, or three-manifold decomposition of the smoothed link was assumed. No representation is assigned to a general entropy flow: (20)–(25) constructed one for the optimized block problem.

## 6. Stable neighborhoods and bounded finite shifts

The spectator row simplexes are compact and entropy is continuous. For any sequence of feasible target vectors tending to an endpoint in (6), choose maximizing flows and pass to a convergent subsequence. The limit is feasible at that endpoint, so its entropy is bounded by (9). This proves a strict gap in some closed neighborhood of each endpoint. If the endpoint is infeasible, compactness instead gives an infeasible neighborhood.

The statement includes \(O(1)\) finite degree changes, the \(N-1\) offset, and fold linear factors. Polynomial scalar factors do not affect the exponential rate. Unit complex \(q\)-shifts of shared variables do not change absolute coefficient bounds, but their positions and requested target must still be retained. Transporting an order-\(N\) amount of a face target is not a bounded shift.

## 7. The exact-current interface remains separate

After extracting the other original targets, write the remaining central contraction as
\[
                         B(z)=\sum_{k=0}^d b_kz^k.     \tag{27}
\]
The raw protected endpoint terms of \([z^d]GB\) have spectator coefficients near \(b_d\) and \(b_{d-m}\), with the exact one-unit offset fixed by the finite convention. These are the original endpoint sources analyzed above.

The face-current identity instead has the form
\[
 [z^d]G\,\mathcal{D}_\sigma B
        =\chi b_d+s_m^2v_M b_{d-m}.                    \tag{28}
\]
To use it on \([z^d]GB\), one first sets \(A=\mathcal{D}_\sigma^{-1}B\). Its two displayed endpoint coefficients are coefficients of \(A\), not \(B\). They can contain alternating sums over a linear number of original loads. More explicitly, at \(\sigma=2\) the exact identity is
\[
 [z^d]G B=4A_d+4N(-1)^{m-1}A_{d-m},
                 \qquad A=\mathcal D_2^{-1}B.           \tag{28a}
\]
These are the coefficients and offsets in
[the adjacent-transport obstruction, sections 1–2](/private/tmp/md-protected-left-adjacent-transport-obstruction.md).

The distinction has an exact local support obstruction. The adjacent central factor can, with legitimate fixed exterior monomial loads, supply a single interior power \(B=K_N z^{d-j_0}\), \(1\le j_0\le m-1\), \(K_N\ne0\). Both raw endpoints vanish whereas \([z^d]GB=K_Nv_{j_0}\ne0\) at \(\sigma=2\). The exact all-level construction is section 3 of the linked note: extracting \(a^mt^{d-m}\) at region 18 forces the unique all-\(a\) path and a nonzero polynomial-size \(K_N\); the exterior monomial then fixes the displayed power. Therefore an identity valid for arbitrary exterior loads cannot replace the pair by only its two raw endpoints. This does not assert that those particular exterior loads extend to a global R54 configuration.

Entropy concavity cannot supply the missing estimate either. It gives lower bounds by chords, not upper bounds. For the actual 54-circle sphere, with protected vertices \(50,29\) and selected quartet \((0,50,16,29)\), the rational witness gives
\[
 E_T\left(\frac{548219162717}{2\cdot10^{12}}\right)
                           >\Phi_T+\frac15.            \tag{29}
\]
Every original target and spectator triangle is retained. This is the companion endpoint-energy obstruction, not a signed coefficient lower bound.

The adjacent central input triangle is \((41,0,16)\). It shares strand edge \(0\,16\) with selected output triangle \((0,29,16)\), with opposite induced orientations. A coherent contraction may exploit signs and shifted Casimir relations across this edge. Its effective currents must still be shown to retain constraints (6), or their additional face-load transport must be bounded directly. Calling the coefficients of an inverse operator “boundary currents” does not make them the sources (10) or (17).

Thus the geometric result is the strict endpoint theorem (9), with its stable endpoint neighborhoods. A reduction of the actual filled remainder to those sources remains an additional analytic obligation.

