# Exact boundary messages for cyclic physical sources

This note separates three finite constructions which have different scopes. A two-strand Conway box has a scalar Casimir description. A general plat has an exact matching-graph source, with coupled magnetic channels and a physical trace normal. An arbitrary finite tensor network can also be evaluated by polynomial boundary messages, provided those messages retain every physical boundary index. These statements do not identify the latter two constructions with the scalar edge kernel of an all-circle tree.

All diagrams, their orders and their integer crossing powers are fixed before \(N\) tends to infinity. No new volume theorem for a cyclic plat is claimed here.

## 1. The source already available on a general matching graph

Put \(d=N-1\), \(q=e^{\pi i/N}\), and \(Q=q^2\). The actual complete-circle identity in `notes/general_matching_graph_full_normal_source.md`, equations (1), (7)--(10), gives

\[
 A_{D,N}=\frac1{\nu_N}\sum_{\boldsymbol a}
  \left(\prod_e h_{0,a_e}\omega_{a_e}^{\epsilon_e}\right)
  \left.\frac{d}{d\varepsilon}F_{\Delta}(\boldsymbol a;\varepsilon)
  \right|_{\varepsilon=0},\qquad
 \nu_N=\frac{2N(-1)^N}{q-q^{-1}}.                         \tag{1}
\]

Here \(0\le a_e\le\lfloor d/2\rfloor\). The generic network uses the original ordered physical objects \(V_d\), the ordinary matching objects of highest weight \(2a_e\), their actual cups and caps, and regular maps \(W_{a_e}(\varepsilon)\), \(\pi_{a_e}(\varepsilon)\). At the root, a paired channel satisfies \(\pi_aW_a=0\), not \(I\). The exterior framing character, if used to convert \(A_{D,N}\) to another convention, is outside (1).

This formula is for the complete auxiliary-circle colors. A chosen regular lift of its fixed-root coupons computes the indicated normal; it is not the whole moving-\(q\) germ of the original coupon. The source note proves the resulting first normal is independent of that choice.

Several stronger results must be kept distinct. `general_signed_augmented_source_volume.md` proves the full signed complete-source asymptotic under the original labeled positive geometric certificate. `general_full_spectral_numerator_geometric_packet.md` proves a relative full-numerator packet on a fixed small spectral neighborhood. `general_all_cross_long_filling_volume.md` proves the whole Fourier/Hermite filling period of the all-CROSS sector. The last theorem expressly leaves the moving LEFT and RIGHT sectors of the full filling numerator outside its conclusion.

## 2. A physical obstruction to independent scalar boundary pairs

Let \(V\) be the original \(N\)-dimensional module, and let its Cartan operator be

\[
 Kv_a=xQ^{-a}v_a,\qquad 0\le a<N,\qquad x=q^d.
                                                               \tag{2}
\]

For two strands the full Hopf commutant is \(\mathbb C[\Omega]\), with the repeated Casimir nodes and their first derivatives retained. On four strands consider the proposed independent-pair algebra

\[
 \mathcal B_N=\mathbb C[\Omega_{12}]\otimes
               \mathbb C[\Omega_{34}]
          \subset\operatorname{End}(V^{\otimes4}).             \tag{3}
\]

Every element of (3) commutes with \(K_{12}=K_1K_2\). This follows directly from the pair coproduct: \(\Omega_{12}\) commutes with \(K_1K_2\), and \(\Omega_{34}\) acts on the other two factors. It remains true for any linear combination, including one with arbitrary coefficients in additional spectral variables.

The literal positive checked crossing \(\check R_{23}\) does not commute with \(K_{12}\). Indeed the nilpotent part of the physical braid is a sum of \(E^r\otimes F^r\). On \(v_0\otimes v_1\), only \(r=0\) contributes. The retained Cartan factor and swap therefore give

\[
 \check R_{23}(v_0\otimes v_0\otimes v_1\otimes v_0)
 =q^{d(d-2)/2}
   v_0\otimes v_1\otimes v_0\otimes v_0.                      \tag{4}
\]

Consequently

\[
 [K_{12},\check R_{23}](v_0\otimes v_0\otimes v_1\otimes v_0)
 =x^2(Q^{-1}-1)q^{d(d-2)/2}
   v_0\otimes v_1\otimes v_0\otimes v_0\ne0                 \tag{5}
\]

for every \(N\ge2\), at both parities. The fractional Cartan exponent is the actual fixed highest-weight exponent; no principal matrix logarithm is substituted.

Thus a region containing this actual crossing cannot have an exterior-independent expression in (3). In particular, replacing a four-head separator by two independent scalar Newton variables is not a universal physical source identity. This is an operator obstruction before attaching an exterior, not evidence from numerical asymptotics. It does not say that a particular final scalar contraction cannot simplify after its genuine exterior has acted.

There is also a useful stability statement. If \(A,B\in\mathcal B_N\) are invertible, then

\[
 [K_{12},A\check R_{23}B]=A[K_{12},\check R_{23}]B\ne0.
                                                               \tag{6}
\]

Hence invertible pair-local decorations do not erase the coupled channel exactly. This assertion applies when the literal decoration is such an invertible operator. It is not asserted for arbitrary turned terminal tangles, which may be singular at particular levels. An asymptotic damping result would require a separate estimate even when (6) applies.

## 3. An exact polynomial message which does retain the channels

There is nevertheless a general boundary-message construction without any semisimple reduction. Fix the matching labels in (1). Work in the dual-number ring

\[
 \mathbb D=\mathbb C[\varepsilon]/(\varepsilon^2),\qquad
 T=T^{(0)}+\varepsilon T^{(1)}                              \tag{7}
\]

for every original regular local tensor. For a region \(B\), keep all its uncontracted physical and ordinary-channel half-edges. If their dimensions are \(m_1,\ldots,m_b\), define

\[
 \mathcal M_B(z_1,\ldots,z_b)
 =\sum_{0\le i_j<m_j}
     T_B(i_1,\ldots,i_b)\prod_{j=1}^b z_j^{i_j}
       \quad\in\mathbb D[z_1,\ldots,z_b].                    \tag{8}
\]

Here \(T_B\) is the contraction of the original tensors inside \(B\). It is a definition by finite tensor contraction, rather than an assumed invariant of a surface. Each variable has degree at most \(m_j-1<N\), because the matching objects also have dimension \(2a+1\le N\).

For a straight physical wire, gluing two exposed variables with coefficient arrays \(f_i,g_j\) is the exact pairing

\[
 \sum_{i=0}^{m-1} f_i g_i
   =[z^{m-1}]f(z)z^{m-1}g(z^{-1}).                          \tag{9}
\]

For a cup or cap with entries \(p_{ij}\) or \(\ell_{ij}\), use instead \(\sum_{ij}p_{ij}f_i g_j\) or \(\sum_{ij}\ell_{ij}f_i g_j\), with its specified port order. The physical cups have complementary support \(i+j=d\); their actual nonconstant coefficients remain in this pairing. Reversing a port changes the typed pairing, not merely the name of its variable. Multiple boundary wires are glued by the corresponding multiple finite contraction. A closure within one region is the same operation on two variables of its single message, so cycles are allowed.

Multiplication in \(\mathbb D\) gives exactly

\[
 (AB)^{(0)}=A^{(0)}B^{(0)},\qquad
 (AB)^{(1)}=A^{(1)}B^{(0)}+A^{(0)}B^{(1)}.                 \tag{10}
\]

Induction over any elimination order proves that the final coefficient of \(\varepsilon\) is the derivative of the full original ordinary closure. Inserting it into (1) therefore recovers the marked source, including its one physical normal. There is no division by \(\pi_aW_a\) and no separate normal assigned to each separator. If a meromorphic recoupling basis is introduced instead, first jets of those new coordinates need not suffice; this statement uses the regular physical presentation throughout.

The boundary arrays have at most \(N^b\) entries. Thus a fixed decomposition of bounded separator size gives an exact finite algorithm with a fixed polynomial cost in \(N\), including a separate finite sum over matching labels. This is a statement about storage and finite arithmetic, not about the magnitude or condition number of its entries. For a fixed diagram, the number of matching labels and the separator size are fixed. No estimate uniform in a growing family is asserted.

The same regular physical compiler applies directly to a filled plat at complete main color: replace its boxes by their literal fixed integer powers of the generic highest-weight crossing, retain the original cups and caps, and use the one exposed physical cut. Negative powers are allowed because that crossing is invertible in the generic neighborhood. The generic \(N\)-dimensional highest-weight module then makes the open knot operator scalar, so its ordinary closure is its scalar times the generic quantum dimension. Differentiating once at the root extracts the original marked complete-color scalar with the same \(\nu_N\). This gives a source-exact algorithm for the full filled knot, without first projecting to CROSS. It supplies no asymptotic estimate. At a nonintegral moving main color one must instead use its actual fixed-root unrolled modules and their prescribed modified cut; a generic-\(q\), fixed-dimension highest-weight continuation is not asserted there.

Unlike (3), (8) records a general four-head coefficient array and therefore contains (4). It is a faithful candidate for a cyclic extension. A nonzero leading contraction and a relative bound for the boundary messages remain analytic questions.

## 4. The cycle variables which the exact complete source retains

The more economical root compiler in `actual_matching_graph_shared_cycle_fourier_compiler.md` makes part of the missing data explicit. Restore the ordinary cap to identify the physical cycles, collapse each such cycle to a vertex of \(\Gamma\), and direct matching edge \(e\) from its \(\pi\) cycle to its \(W\) cycle. Set

\[
 w_e=r_e-a_e,\qquad |w_e|\le a_e,\qquad
       \operatorname{div}_{\Gamma}w=0.                       \tag{11}
\]

The actual source is

\[
 A_{D,N}=q^{-d^2}N^{C-1}
 \sum_{\substack{\boldsymbol a,\boldsymbol w\text{ as in }(11)}}
  \left(\prod_e h_{0,a_e}\omega_{a_e}^{\epsilon_e}\right)
  [X_{c_*}^{1}]_N\mathcal L_{c_*}(X_{c_*})
  \prod_{c\ne c_*}[X_c^0]_N\mathcal L_c(X_c).                \tag{12}
\]

Here \(C\) is the number of physical cycles, the marked cycle is \(c_*\), and \([X^j]_N\) sums coefficients whose exponent is \(j\bmod N\). Each \(\mathcal L_c\) contains the original endpoint, cup, cap and Fourier phases. In particular its positive local coefficient factors are not permission to replace the whole Laurent polynomial by a positive polynomial. The mark selects charge one, not charge zero. The source proof also retains the physical affine index lifts before using their first-failure zero lemma; they are not freely wrapped modulo \(N\).

Choose a spanning tree of a connected \(\Gamma\). Its \(b_1=|E|-|V|+1\) chord variables determine every integral circulation uniquely. In the resulting integral fundamental-cycle basis \(C_{e\alpha}\),

\[
 w_e=\sum_{\alpha=1}^{b_1}C_{e\alpha}t_\alpha,
 \qquad t_\alpha\in\mathbb Z,\qquad
 \left|\sum_\alpha C_{e\alpha}t_\alpha\right|\le a_e.
                                                               \tag{13}
\]

To prove integrality and uniqueness, prescribe the flow on the chords and solve the vertex equations successively at leaves of the spanning tree. Each removed tree edge has a prescribed integral flow; the last equation follows because the total divergence is zero. This proof allows loops and parallel edges by treating loops as chords. It does not assert that every feasible circulation has a nonzero Fourier coefficient in (12).

**Bridge-attachment lemma.** If a tree is attached to \(\Gamma\) along a single vertex, every newly attached edge has zero flow, and restriction induces an isomorphism of integral circulation lattices. The proof is leaf removal in the attached tree. The capacities in (11) remain satisfied by its zero flow. Repeating the operation does not remove any original circulation variable.

This lemma is conditional only on identifying the actual induced operation on \(\Gamma\). A terminal tangle insertion in a plat must first be checked in the literal strand compiler; its physical-cycle graph is not determined by the visual operation-tree alone. Even when it is a bridge attachment, the new tensors can change the weights and Fourier constraints in (12). The lemma says that support counting alone cannot establish damping of the old circulation channels.

For the literal stellar terminal insertion, that operation is in fact a loop addition, not a bridge addition. In the matched white triangulation, write the old triangle as \((x,b,y)\), with matching side \(xy\). The new triangle pieces are

\[
 (x,b,w),\qquad (x,y,w),\qquad (y,b,w).
                                                               \tag{13a}
\]

The old matching side \(xy\) remains incident to the middle triangle; the new matching side is \(bw\), joining the two outer triangles. After deleting matching edges in the cubic dual, the old two-leg physical vertex is replaced by the path through these three triangles. Its physical cycle is unchanged up to subdivision. The endpoints of the new matching edge therefore belong to that same cycle. Upon collapsing the cycles, this is a new loop at the old vertex of \(\Gamma\).

Consequently, before capacities and the Fourier coefficients in (12) are imposed, its circulation lattice is

\[
 \ker\operatorname{div}_{\Gamma_{\mathrm{new}}}
   =\ker\operatorname{div}_{\Gamma_{\mathrm{old}}}\oplus\mathbb Z,
 \qquad -a_{\mathrm{new}}\le w_{\mathrm{new}}\le a_{\mathrm{new}}.
                                                               \tag{13b}
\]

The old cycle's Laurent coefficient also acquires the two actual new vertex factors. Thus the new loop flow is not an independent scalar multiplier after Fourier extraction. This explains why terminal fans can alter and potentially improve a geometric weight balance while enlarging, rather than eliminating, the source's magnetic circulation space. The triangle-to-cycle calculation uses the W/\(\pi\) source cycles; it must not be confused with the link components obtained from an untwisted pairing of strands.

## 5. A separate algebraic warning about closing scalar Frobenius diagrams

Let \(\mathcal A=\mathbb C[z]/P_0\), with

\[
 P_0(z)=\mathcal T_N(z)+2,\qquad
 \phi(f)=\kappa[z^{N-1}](f\bmod P_0),\qquad
 \kappa=(-1)^{N-1}N^2.
                                                               \tag{14}
\]

Its Newton basis is exactly anti-diagonally dual: \(\phi(e_i e_j)=\delta_{i+j,N-1}\). The contraction of a multiplication with its bilinear dual therefore produces the Euler element

\[
 \mathfrak e=\sum_{i=0}^{N-1}e_i e_{N-1-i}
              =\frac{P_0'(z)}{\kappa}\quad\bmod P_0.          \tag{15}
\]

Here is a proof retaining the repeated nodes. First use a monic polynomial \(P\) with distinct roots. The primitive idempotent at a root \(c\) has trace \(\kappa/P'(c)\); its dual is therefore \(P'(c)/\kappa\) times that idempotent. This gives (15) at every root. Both the bilinear inverse matrix and polynomial reduction are polynomial expressions in the coefficients of monic \(P\), apart from the fixed nonzero scalar \(\kappa\): the monomial trace matrix is anti-triangular with anti-diagonal \(\kappa\), so its determinant is a fixed nonzero constant. Polynomial continuation proves (15) at the repeated-root \(P_0\).

When \(N\) is even, every root of \(P_0\) is double. Then \((P'_0)^2\) is divisible by \(P_0\), while \(P'_0\) itself is a nonzero polynomial of degree \(N-1\). Hence

\[
 \mathfrak e\ne0,\qquad \mathfrak e^2=0,
 \qquad \phi(\mathfrak e)=N.                                \tag{16}
\]

For odd \(N\), the root \(-2\) is simple and the other roots are double; the same Euler element has both its simple-node part and its retained nilpotent data. A closed scalar Frobenius contraction can therefore depend strongly on its internal cycle topology. In particular one cannot replace its handles by an invertible constant or discard its normals. This algebraic observation is not an assertion that a physical cyclic plat equals this Frobenius diagram. Establishing that equality is precisely what is missing from a naive scalar-kernel extension.

## 6. Why neither bounded separators nor long local powers complete the estimate

Bounded separator size gives polynomially many coefficients in (8), but those coefficients can have different exponential rates and phases. Polynomial dimension does not bound the ratio of an absolute contraction to its signed value. The original matching graph has a concrete example: the full numerator contains LEFT and RIGHT path coefficients whose ratio to the complete positive endpoint can be exponentially large at a fixed real spectral point. At \(N\) divisible by \(24\), the literal LEFT coefficient recorded in `actual_cross_cofactor_factorization.md`, equation (32), has ratio at least

\[
 (3+2\sqrt3)^{N/12}.                                        \tag{17}
\]

That is a local coefficient obstruction, not a counterexample to the coupled invariant. It does rule out using the all-CROSS coefficientwise bound for the full cyclic message.

Likewise a signed crossing power on one fixed pair is not an absolute spectral filter: its complete Casimir eigenvalues have modulus one. Its effects include phase and normal data. An inserted *turned* terminal tangle is a different physical operator and can have a useful magnitude profile, but that profile must be established in the coupled boundary frame of (8) or (12). Equation (6) also shows why exact pair-local diagonalization cannot be assumed to erase a crossing between boundary pairs.

The first concrete analytic target for attached-tree filters is therefore a bound for the actual phase-bearing cyclic contraction after the literal local decorations have been inserted, with the shared flows (11), marked Fourier charge and LEFT/RIGHT coefficients retained. One can compute that object using (8), or, at complete circle colors, using (12). A projected scalar edge model or a count of added leaves is insufficient. The already proved signed complete-source asymptotic provides the complete anchor; extending its full moving numerator beyond the local packet remains the substantive missing estimate.

The conclusions established here are finite and unconditional: the counterexample (5), the faithful first-jet compiler (8)--(10), the circulation parameterization and bridge lemma, and the Euler-element calculation (15)--(16). They exclude several shortcuts while preserving a source-exact route for future coupled estimates. No conclusion about the hyperbolic volume of a cyclic comparison graph is substituted for the original complement.

## 7. The separate balanced-fan route

The subsequent files *md-cyclic-source-terminal-fan-morse-adapter* and *md-cyclic-source-general-morse-period-audit-and-theorem* provide a different route for suitably decorated certified cores. They retain the full shared face coefficient, including all magnetic loop channels, and use the actual complete-radius balance established by the two-sided geometric fan construction to control the full one-sided remainder. The resulting complete-main-color long-filling theorem does not require the false scalar-pair reduction excluded here. It does not prove the same global estimate for an undecorated arbitrary core.
