# Fixed triangular boundaries and source certificates at ordinary faces

This private proof supplies the geometric and coercivity inputs to the thin-face construction. All diagrams and all numbers of attachments are finite and fixed before the quantum level tends to infinity. The conclusion below is about the newly assembled diagram, with its own primitive crossing disks and knot-component test. It does not preserve the input knot types.

The source comparisons use the original triangle potential and the existing full-real-spectral bounds. No finite quantum star-triangle identity is assumed or proved.

## 1. The disk action and its normalization

Let \(B\) be a simple triangulated oriented sphere with at least four vertices. Remove one face \(f=(u,b,v)\), leaving a triangular disk \(P\). Let \(I\) be its \(k\) interior vertices. The disk has \(2k+1\) triangles. For a nonnegative curvature vector \(w\), with at least one positive weight in each triangle, put
\[
Q(w_1,w_2,w_3)=
\max_{\substack{\alpha_i\ge0\\\alpha_1+\alpha_2+\alpha_3=1/2}}
\left\{\sum_i f(\alpha_i)+\sum_{w_i>0}\alpha_i\log w_i\right\},
\qquad
f(t)=\frac{\Lambda(\pi t)+\Lambda(\pi/2-\pi t)}{\pi},
\tag{1}
\]
where loads at a zero weight are required to vanish and
\(\Lambda(s)=-\int_0^s\log(2\sin r)\,dr\). In particular \(f(0)=f(1/2)=0\), \(f\ge0\), and \(f\) is strictly concave on \((0,1/2)\).

The boundary-dependent disk action is
\[
J_{u,v,b}(q_I)=\sum_{t\subset P}Q_t(w)-\sum_{i\in I}q_i,
\qquad w_i=e^{q_i},\qquad
\mathcal J_P(u,v,b)=\inf_{q_I}J_{u,v,b}(q_I).
\tag{2}
\]
Only interior targets are subtracted here. The three boundary loads are free; their total is \(1/2\). The claim is
\[
\boxed{\ \mathcal J_P(u,v,b)=Q(u,v,b)+C_P\ }\qquad(u,v,b>0).
\tag{3}
\]
The constant is determined below. This is an identity of classical source actions with their absolute normalization.

For a triangle with positive supported weights, its unique maximizing loads are
\[
\alpha_i=\frac1\pi\arctan\frac{w_i}{D_t},
\qquad D_t=\sqrt{w_1w_2+w_2w_3+w_3w_1}.
\tag{4}
\]
For two positive weights this is interpreted on those two corners; a singleton has load \(1/2\). The Hessian in supported log weights is a Laplacian, with off-diagonal entries
\[
-\kappa_{ij},\qquad
\kappa_{ij}=\frac{w_iw_j}{2\pi D_t(w_i+w_j)}>0.
\tag{5}
\]
Singletons contribute no Hessian. Thus a connected supported graph has only the common-scale kernel.

## 2. Existence for every positive boundary triple

Here is the finite feasibility and coercivity argument, separate from the subsequent development.

Each triangle supplies \(1/2\); every interior vertex demands one. Pool the three boundary destinations into one destination of demand \(1/2\), retaining their separate corners. A strictly positive transport table exists.

For a nonempty set \(S\) of interior destinations, put \(T=I\setminus S\). Puncture the capped sphere at a vertex of \(S\). The triangles supported on \(T\cup\{u,v,b\}\) are bounded faces of a simple planar graph on \(|T|+3\) vertices. There are at most \(2|T|+1\) bounded triangular faces; one is the removed face. Thus at most \(2|T|\) disk triangles miss \(S\), so at least \(2|S|+1\) touch it. Their supply is strictly greater than \(|S|\).

A proper destination set containing the boundary pool has nonempty complement \(T\subset I\). Triangles wholly on \(T\) number at most \(2|T|-5\) for \(|T|\ge3\), and none for \(|T|\le2\). The touching supply therefore strictly exceeds that set's demand. The full destination set has equality of totals. These are the strict finite transport Hall inequalities. Subtracting one sufficiently small positive amount from every allowed corner preserves feasibility; restoring those amounts gives a table \(\alpha^0_{ti}>0\) on every corner.

Fix positive boundary weights. For an interior direction \(h\), extend \(h\) by zero on the boundary. The recession of (2) is
\[
\mathcal R(h)=\frac12\sum_t\max_{i\in t}h_i-\sum_{i\in I}h_i
=\sum_t\sum_{i\in t}\alpha^0_{ti}
                  \left(\max_{j\in t}h_j-h_i\right).
\tag{6}
\]
It is nonnegative. Equality forces \(h\) to be constant on every triangle. The disk graph is connected and the boundary is grounded, so equality forces \(h=0\). Compactness of the unit sphere gives a positive recession margin.

More explicitly, \(Q_t(q)\ge\frac12\max_{i\in t}q_i\), while its difference from that maximum is bounded above by the finite maximum of \(\sum f\). Fixed boundary logarithms alter these estimates only by a bounded constant. Consequently
\[
J_{u,v,b}(q_I)\ge c\lVert q_I\rVert-C.
\tag{7}
\]
for constants \(c>0,C<\infty\). This proves coercivity, not merely strict convexity. The grounded Hessian (5) is positive definite, so the minimizer exists, is finite, and is unique. Its loads satisfy each interior demand exactly.

The resulting minimizer depends smoothly on the positive boundary log weights by the implicit function theorem and the positive definite interior Hessian.

## 3. Development and proof of the fixed-boundary identity

Set radii \(r_i=1/w_i\). For each triangle, the three lengths \(r_i+r_j\) form a nondegenerate triangle. Its center angle at \(i\) is \(2\pi\alpha_{ti}\), by the tangent-circle half-angle formula (4).

At the minimizer every interior vertex has total angle \(2\pi\). All boundary corner angles are positive; their sum over the three boundary vertices is \(\pi\), because there are \(2k+1\) triangles and \(k\) interior vertices. In particular every boundary angle sum is less than \(\pi\).

Develop the triangles with their given orientation. Continuation around an interior vertex has rotation \(2\pi\) and zero translation. Such loops generate the holonomy of the punctured disk, so the development is single-valued. Its boundary consists of three straight segments of lengths \(r_u+r_v,r_v+r_b,r_b+r_u\), traversing the prescribed convex center triangle once.

This development is injective. For a point outside the finite developed edges, each preimage is orientation preserving, so the number of preimages equals the boundary winding number: one inside the boundary triangle and zero outside. Local injectivity at edges and interior vertices, followed by continuity, extends this to the whole disk. Separating triangles inside \(P\) cause no change in this degree argument.

It follows that the total developed angle \(\Theta_u\) at the boundary vertex \(u\) is exactly the angle of the unrefined center triangle. Differentiating the optimized action gives
\[
\partial_{\log u}\mathcal J_P
=\frac{\Theta_u}{2\pi}
=\frac1\pi\arctan\frac{u}{\sqrt{uv+ub+vb}}
=\partial_{\log u}Q(u,v,b).
\tag{8}
\]
The same holds at \(v,b\). Hence the difference in (3) has zero differential throughout the connected positive octant and is constant. There is no extra boundary-linear term. Its logarithmic homogeneity is \(1/2\), since the disk has half-supply \(k+1/2\) and interior demand \(k\).

The developed disks have disjoint interiors and only the prescribed contacts: each disk sector lies inside its incident center triangle and stops before the opposite center edge. The contact-circle halfspaces give the original convex right-angled ideal piece. This identifies the variational development with the fixed-boundary packing, rather than just an abstract flat metric.

## 4. Two zero boundary weights: coercivity, uniqueness and the limit

Now take \(u=v=0,b=1\). Every triangle of \(B\) has an ordinary supported corner. Write \(O=I\cup\{b\}\). On the full sphere assign demand one to every member of \(O\), and supply \(1/2\) to each triangle.

This supported transport has a strictly positive table on every allowed corner. For a nonempty proper \(S\subset O\), put \(T=O\setminus S\). Puncture at a vertex of \(S\). Triangles missing \(S\) are bounded triangular faces of a simple planar graph on \(|T|+2\) vertices, at most \(2|T|-1\). Thus at least \(2|S|+1\) sphere triangles touch \(S\). The full destination set has equality of totals. Subtracting a small positive corner amount yields strict relative feasibility, with singleton rows fixed at their forced \(1/2\) load.

The removed face \((u,b,v)\) is such a singleton. Removing its load leaves interior demands one and \(b\)-demand \(1/2\) in the disk. Let \(\alpha^0\) be the resulting strictly supported table.

Deleting \(u,v\) from a simple triangulated sphere leaves a connected graph. One direct proof deletes \(u\) by rerouting a path through its cyclic link, then deletes \(v\) by rerouting through its link with \(u\) removed, which is still connected. Removing the face \((u,b,v)\) removes no edge between two ordinary vertices. Therefore the supported co-occurrence graph of the disk is connected to \(b\).

For \(h_b=0\), the same formula as (6), now using only supported corners, gives
\[
\mathcal R_0(h)=
\sum_t\sum_{i\in\operatorname{supp}(t)}
\alpha^0_{ti}\left(\max_{j\in\operatorname{supp}(t)}h_j-h_i\right)>0
\quad(h\ne0).
\tag{9}
\]
It proves \(J_{0,0,1}(q)\ge c_0\lVert q\rVert\) up to a harmless constant. Formula (5) grounds the only kernel. There is consequently a unique finite minimizer \(q^0\).

The full protected-sphere action is exactly \(J_{0,0,1}\): restoring the removed singleton contributes \(\frac12\log b\), and subtracting its ordinary target contributes \(-\log b\), both zero at \(b=1\). Hence
\[
\min J_{0,0,1}=\Phi_B.
\tag{10}
\]
The known original simple-sphere calibration identifies \(2\pi\Phi_B\) with the augmented volume of \(B\). No full-source estimate is needed for (10).

For \(u,v\ge0\), monotonicity of \(Q\) gives \(J_{u,v,1}\ge J_{0,0,1}\). Its interior Hessian retains that same connected positive support and it remains coercive; no Loewner comparison of the old and new Hessians is required. Its unique minimizer \(q^{u,v}\) satisfies
\[
J_{0,0,1}(q^{u,v})
\le J_{u,v,1}(q^{u,v})
\le J_{u,v,1}(q^0)\longrightarrow J_{0,0,1}(q^0).
\tag{11}
\]
Here \(Q\) is continuous as supported weights tend to zero: maximizing loads at the disappearing corners tend to zero, their entropy tends to zero, and their logarithmic terms are nonpositive; the reverse inequality comes from the old supported maximizing load. Coercivity confines \(q^{u,v}\) to a compact set, and uniqueness implies
\[
q^{u,v}\longrightarrow q^0\qquad(u,v\to0).
\tag{12}
\]
The convergence is joint and uniform on sufficiently small boundary squares: the upper bound in (11) is at most \(J_{\eta,\eta,1}(q^0)\) when \(u,v\le\eta\).

Taking this limit in (3), with \(Q(u,v,1)\to0\), identifies its constant:
\[
C_P=\Phi_B.
\tag{13}
\]
Equations (3) and (13) extend to the closed boundary square with \(b>0\) by the same monotonicity argument. In particular, for the closed expression with no \(u,v\) targets,
\[
\widehat P_B=\sum_{t\subset B}Q_t-\sum_{i\in I}q_i-\log b,
\qquad
\inf\widehat P_B=\Phi_B+\Delta,\quad
\Delta=2Q(u,v,b)-\log b\ge0.
\tag{14}
\]
For positive boundaries, every interior packing disk has curvature at least
\[
u+v+b+2\sqrt{uv+ub+vb}>\max(u,v,b).\tag{14a}
\]
Indeed, let the three boundary centers and radii be \(p_i,r_i\). On their center triangle maximize \(r(z)=\min_i(|z-p_i|-r_i)\). It is nonpositive on the boundary, whose sides are covered by the two incident tangent disks, and positive in the interstice. At a positive interior maximum there cannot be just one active distance. With two active distances, their gradients either admit a common increasing direction, or are opposite; in the latter case the center lies between tangent boundary centers and the common empty radius is nonpositive. Thus all three distances are active. Eliminating the center from the three tangency equations gives \((k-u-v-b)^2=4(uv+ub+vb)\). At equal boundary curvatures the bounded-interstice disk takes the plus sign. The maximum empty radius varies continuously with the three positive boundary radii (maximize the continuous distance function on their continuously varying compact center triangle), and the two algebraic roots never meet on the positive octant. The plus sign therefore holds throughout that connected octant, proving (14a). Every interior packing disk is contained in this interstice, so its radius cannot exceed that maximum. In particular the central conditional root always has \(a>v\) for positive boundary data.

The root middle \(a\in I\) has \(e^{q_a^{u,v}}\to e^{q_a^0}>0\). Thus \(a\ge v\) for all sufficiently small \(u/b,v/b\), after common scaling.

An equivalent boundary-load statement is available. Maximizing entropy subject to the interior demands and a boundary vector \(\beta\) of total \(1/2\) gives a closed concave function. Its conjugate is (3). Closed concave duality therefore identifies that function with \(\sum f(\beta_i)+\Phi_B\) on the whole closed half-simplex. This preserves aggregate boundary loads, including zero loads; it does not add boundary coefficient demands.

## 5. Oriented sewing and exact target allocation

Let the fixed core have its own protected nonmatching edge, away from the selected all-ordinary faces. At one selected core region and one block root use the polynomial argument orders
\[
e_D=(u,v,c,b),\quad f_D=(u,v,b);
\qquad
e_B=(u,a,v,b),\quad f_B=(u,b,v).
\tag{15}
\]
The removed triangles have opposite orientations. Their common matching side is \(ub\), and their retained partners are \((u,b,c)\) and \((u,a,b)\). After gluing, those partners form the new region
\[
e_{\mathrm{new}}=(u,a,c,b).
\tag{16}
\]
Every other matching pair and cyclic order is retained. The four vertices of (16) are distinct because block interiors are fresh and \(a\) is an interior vertex.

Each boundary identification glues two punctured spheres along an embedded three-cycle. Fresh interiors give no loops or duplicate edges other than the boundary edges deliberately identified. The result is again a simple oriented triangulated sphere. The old common matching side is retained once and all other matching pairs are untouched. The core mark remains nonmatching.

If \(B\) has \(R_B=k+1\) regions, the insertion adds precisely \(k\) ordinary vertices and \(k\) matching regions. Its target count is
\[
\mathcal O_{\mathrm{new}}=\mathcal O_D\sqcup I,\qquad
R_{\mathrm{new}}=R_D+R_B-1.
\tag{17}
\]
In particular, ordinary \(u,v\) retain their single core targets. They acquire no second targets from the block.

Put \(T=Q(u,v,b)\), \(Q_a=Q(u,a,b)\), \(Q_c=Q(u,c,b)\). Then
\[
X_D=T+Q_c,\quad X_B=Q_a+T,\quad X_{\mathrm{new}}=Q_a+Q_c.
\tag{18}
\]
The block comparison expression subtracts its interior targets and one \(b\)-target, but none at \(u,v\). Combining it with the core therefore duplicates only \(b\). The exact complete action identity and a general sector inequality are
\[
P_{\mathrm{new}}=P_D+\widehat P_B-\Delta,\qquad
G_{\mathrm{new},\omega}\le
G_{D,\omega_D}+\widehat G_{B,\omega_B}-\Delta+\varepsilon_e,
\quad \Delta=2T-\log b.
\tag{19}
\]
The local sector map is
\[
C\mapsto(C,C),\qquad L\mapsto(L,C),\qquad R\mapsto(C,R).
\tag{20}
\]
Its defects may be taken to be
\[
\varepsilon_C=0,\qquad
\varepsilon_L=(T-Q_a)_+,\qquad
\varepsilon_R=(T-Q_c)_+,\qquad
0\le\varepsilon_e\le\Delta/2.
\tag{20a}
\]
For example the old left expression after subtracting \(2T\) is
\(\max(q_c+Q_a-T,Q_a+q_c/2)\); adding \((T-Q_a)_+\) bounds the new left rate \(\max(q_c,Q_a+q_c/2)\). The right calculation interchanges \(a,c\). Finally \(Q_a,Q_c\ge\frac12\log b\), proving the last bound without any middle-order assumption.

Eliminating the block variables in the first equality of (19) using (14) gives, for every core vector, exactly \(P_D+\Phi_B\). Therefore
\[
\Phi_{\mathrm{new}}=\Phi_D+\Phi_B.
\tag{21}
\]
All original core face derivatives and target demands are unchanged.

For finitely many attachments choose distinct core matching pairs; no removed face or its partner is used twice. Boundary vertices may coincide. Their weights remain the same core coordinates, and each retains one core target. Every block expression duplicates its own \(b\)-target once, and its own correction in (19) cancels that duplication, even when several such \(b\)'s are the same core vertex. Fresh interiors remain disjoint. Thus
\[
R_{\mathrm{new}}=R_D+\sum_j(R_{B_j}-1),
\qquad
\Phi_{\mathrm{new}}=\Phi_D+\sum_j\Phi_{B_j}.
\tag{22}
\]

## 6. From protected certificates to a full source estimate

Assume each block has a finite unabridged certificate at its standalone protected mark \(uv\), with gap \(\gamma_B>0\). It covers every locally allowed noncentral string, including old strings whose global extraction happened to vanish.

Choose one positive interior witness per old string at \(u=v=0,b=1\). Their rates are continuous when \(u,v\to0\), because every triangle contains a positive ordinary corner. Finiteness preserves half the gap on one common small square. A newly allowed side overloaded at \(u\) or \(v\) has rate
\[
\max\{\log u,\ Q_{\mathrm{retained}}+\tfrac12\log u\}
\]
or its \(v\)-analogue. At one fixed positive interior vector it tends uniformly to \(-\infty\); all other local factors are bounded above. This treats every newly allowed string. At an exactly zero overloaded weight the term is absent.

Combining these finite choices with (12), there is \(\eta_B>0\) such that \(u/b,v/b\le\eta_B\) permits a central conditional minimizer of value \(\Phi_B+\Delta\), or a noncentral witness of value at most \(\Phi_B-\gamma_B/2\). The central conditional root satisfies \(a>v\) by (14a); no ordering is required of noncentral witnesses.

Suppose the core has an unabridged certificate whose finitely many witnesses, together with its complete vector, meet the selected thin-boundary conditions. There is no required inequality between core middles. Choose one induced core witness, then classify each induced **whole block string**:

* If the entire block is central, use its conditional packing minimizer. Its root is central, so the new bridge can only be central or left. A central bridge is exact, and a left bridge has zero defect because (14a) gives \(a>v\) and hence \(Q_a\ge T\). Its value \(\Phi_B+\Delta\) cancels the \(-\Delta\) in (19).
* If the block has any noncentral label, use the finite extended certificate. Its value is at most \(\Phi_B-\gamma_B/2\), while its bridge defect is at most \(\Delta/2\). It therefore contributes at most \(\Phi_B-\gamma_B/2-\Delta/2\) after the correction.

The locally central root alone does not imply that the whole block is central. The split above uses every label of that block. At least one induced input is noncentral when the output is noncentral. For any fixed finite number of blocks this proves
\[
\gamma_{\mathrm{new}}\ge
\min\{\gamma_D,\gamma_{B_1}/2,\ldots,\gamma_{B_s}/2\}>0.
\tag{23}
\]
All boundary incidences use the actual core weights. No summed defect budget is needed: each block absorbs its own defect.

The local bounds are uniform in phases and all real spectral variables at both parities. The number of sector strings is finite for the fixed assembly. Hence (23) bounds the entire complementary source polynomial on its original full real spectral cube. It is not an estimate for independent local radii or for a changed collection of face targets.

## 7. Original primitive fillings and the actual volume conclusion

The new sphere and matching are fed into the original Morse inverse-cut construction. This constructs the augmented link \(Y_{\mathrm{new}}\) in \(S^3\), its crossing-circle balls, local signed half twists, outside strands and disk-framed primitive bases. It is not necessary to interpret the operation as a preexisting named topological sum.

There is one new crossing circle at each merged pair. Its primitive word is the ordered two-head product from its new quartet. The two input crossing circles do not survive as two independently fillable cusps. The independent integers in the conclusion belong to the **final** regions. Choose a retained parity pattern passing the final one-component test; such a pattern exists by the original spanning-tree pairing argument. No old knot parity or knot type is silently transported.

The simple-sphere packing theorem applies to the final sphere and fixes its positive complete cells. Equations (21)–(22) identify its actual augmented action:
\[
2\pi\Phi_{\mathrm{new}}=\operatorname{Vol}(Y_{\mathrm{new}}).
\tag{24}
\]
This is not a claim that filled volumes add.

Appendices N and O now apply to the final original Morse source. The exact scalar is retained; every final ordinary face has target \(d=N-1\), and each final spectral variable has degree at most \(d\). The full filling norm costs at most
\(\prod_e(1+|n_e|/2)\). The entire central period is nonzero at both parities for independently sufficiently long fixed signed powers.

The representation constructed from the final original circles has
\[
U_e+p_eV_e=-2\pi i,\qquad n_e=\epsilon_e-2p_e.
\tag{25}
\]
The small individual-generator logarithms, nonunit auxiliary holonomy and primitive logarithmic period give smooth solid-torus completion. The main cusp remains complete. The original disk surgery is in \(S^3\), so the metric is on the final knot complement. The same boundary triangulation and relative fundamental chain supply the absolute regulator comparison
\[
2\pi\operatorname{Re}S_{\boldsymbol n}
=\operatorname{Vol}(S^3\setminus K_{\boldsymbol n}).
\tag{26}
\]
No comparison manifold or only exponentiated filling equation is substituted.

Finally choose the fixed long-filling threshold so that
\(\Phi_{\mathrm{new}}-\operatorname{Re}S_{\boldsymbol n}
<\gamma_{\mathrm{new}}/2\). The full complementary contribution then has smaller exponential rate. For the original reduced, zero-framed invariant normalized by the unknot,
\[
\lim_{N\to\infty}\frac{2\pi}{N}
\log\left|\langle K_{\boldsymbol n}\rangle_N\right|
=\operatorname{Vol}(S^3\setminus K_{\boldsymbol n}).
\tag{27}
\]
Every block, core length, retained parity and final integer is fixed first. The threshold may depend on the entire finite assembly; there is no claim uniform in growing assemblies or quantum-level-dependent powers.

## 8. Nonprotected interfaces exist for arbitrary certified blocks

The explicit core in the thin-face note uses the octahedral sphere with poles \(P,S\), rim \(v_0,\ldots,v_3\), protected mark \(v_0v_1\), and complete curvatures \(P=S=1,\ v_2=v_3=2\). Stellar insertions inside the all-ordinary face \((v_2,P,v_3)\), with the stated zigzag matching, produce
\[
b_j=3j^2+4\sqrt2\,j+2
 =3(j+\sqrt2)(j+\sqrt2/3).
\tag{28}
\]
At an even terminal length \(n\), the final interface has
\[
u/b_n=2/b_n\to0,\qquad v/b_n=1/b_n\to0,\qquad
c=b_{n-1}\ge v.
\tag{29}
\]
The strict-balance proof is uniform in the chain index: the ratios \(b_j/b_{j-1}\) decrease, and the displayed triangle allocations in the thin-face note reduce every internal comparison to one fixed constant. Its three constant lower bounds are \(0.06,0.25,0.09\), respectively. The accompanying Arb calculation bounds each Lobachevsky value by its finite Fourier sum with rigorous tail \(1/(2K)\). It verifies only those fixed constants, not the geometric theorem. For each fixed \(n\), the complete vector supplies all unabridged core witnesses, with a positive minimum mixed-branch loss.

Thus any fixed block satisfying the old unabridged certificate can be attached after choosing a sufficiently large even \(n\). Finitely many cores can first be joined at their protected mark, leaving their ordinary terminal disks intact; one sufficiently long chain per disk permits any fixed finite list of certified blocks. These are explicit cores satisfying the hypothesis of Section 6, not an assumed gap for the final diagram.

There is a precise distinction from nontrivial protected sums at the same recorded mark. The octahedral sphere has no separating three-cycle. All vertices subsequently inserted in the selected ordinary disk, including all block interior vertices, attach only within that all-ordinary disk. Therefore any three-cycle containing both original protected vertices is unchanged and still bounds an original face. The final graph has no separating three-cycle containing that protected pair.

Every nontrivial protected triangular sum at that mark creates a separating three-cycle containing the two protected vertices, with vertices on both sides. Hence the single-core ordinary-face assemblies just described cannot be decomposed as a nontrivial protected sum at their recorded mark. This is a combinatorial distinction of marked presentations. It does not exclude another mark, another knot presentation, or an independently known volume theorem.

For the seventeen-region certified block attached at its safe crossing-15 face, an explicit action test preserves the weak-balance failure. The old restricted-dual table has zero load at both protected vertices, so after making them ordinary boundary variables the same table is feasible and gives
\[
\widehat G_{\mathrm{restricted}}(u,v;q_I)>
\Phi_B+\frac1{40}\qquad(b=1).\tag{30}
\]
It uses the right anchor at region 12 and mixed spectators only at 2,4,7. If all four of these regions satisfied weak balance at the conditional complete vector, then every mixed spectator would equal its complete rate and the anchor would be bounded by its complete rate. Consequently (14) would give
\[
\widehat G_{\mathrm{restricted}}
\le\widehat P_B=\Phi_B+\Delta.\tag{31}
\]
Choosing the thin boundary so that \(\Delta=2Q(u,v,1)<1/40\) contradicts (30). This condition is possible since \(Q(u,v,1)\to0\). Attachment at region 15 leaves all four candidates untouched. Thus the new marked diagrams can fail complete weak balance while having the full-source certificate. This uses the existing exact restricted-dual certificate; it requires neither an interior continuity modulus nor a new numerical search.

## 9. Dependencies and review limits

The proof of Sections 1–4 gives the missing fixed-boundary identity, supported coercivity and joint limit directly, using finite transport feasibility and the center development. Its complete geometric calibration is the existing simple-sphere theorem. Sections 5–7 retain the source rates and the published N/O interface; they do not reprove the local spectral-envelope estimates or the all-charge asymptotic.

The explicit chain matching and the three fixed constant inequalities in Section 8 are recorded in the frozen thin-face note and verifier. A separate source audit is checking all those incidences, every induced sector and the multiple-attachment target count. No public source has been changed.
