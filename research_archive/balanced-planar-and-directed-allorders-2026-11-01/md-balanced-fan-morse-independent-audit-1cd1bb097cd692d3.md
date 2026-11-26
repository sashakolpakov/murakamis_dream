# Independent mathematical audit of balanced terminal fans and the Morse period

This record concerns the three requested private drafts, together with the subsequent full-period assembly. It checks their literal finite inputs and the relevant inherited estimates. It does not treat a finite numerical test as a proof and does not claim to reprove every local cofactor theorem in the dependency chain.

## 1. Conclusion and exact scope

No fatal mathematical defect was found in the stated theorem with its supplied labeled positive complete certificate. The two-sided fan construction produces strict balance at the one actual refined complete packing. The orientation-correct Morse coefficient identity then supplies the same full numerator, primitive measure and full-Hermite filling functional to which the existing weighted one-sided and whole-period estimates apply. The conclusion is for sufficiently long fixed fillings of **all ports of the decorated diagram**, including the original core ports. It is not a result about short fillings of those ports or the undecorated knot.

The additional assertion that every actual simple white sphere automatically supplies the required certificate is not part of the four texts audited here. Root and geometry are developing that statement separately; this audit does not remove the certificate premise by inference.

The files read in full were:

* md-cyclic-geometry-balanced-terminal-fans.md;
* md-cyclic-geometry-cut-and-morse-packet-interface.md;
* md-cyclic-source-terminal-fan-morse-adapter.md;
* md-cyclic-source-general-morse-period-audit-and-theorem.md.

Their hashes and the exact inherited files consulted are in the accompanying JSON manifest.

## 2. The entropy and fan inequalities

The absolute normalization in the fan proof is the actual triangle entropy, not the full Fejer entropy or a rescaled capacity. At positive middle curvature b, stationary allocation satisfies

\[
 \tan(\pi\alpha_j)=w_j/z,
 \qquad z^2=xb+xy+by=Ab+P,
 \quad A=x+y,\quad P=xy.
\]

Thus \(\partial_{\log b}F=\pi^{-1}\arctan(b/\sqrt{Ab+P})\). This matches the marked cofactor/triangle theorem, including a single outer zero. The supported simplex is essential: zero weights receive zero load, rather than a regularized positive load.

The limit \(F(x,b,y)-\frac12\log b\to0\) at fixed outer curvatures follows directly from that entropy maximization. A maximizing sequence whose outer allocation failed to tend to zero would incur an unbounded negative log-weight cost after division by b. Once both allocations tend to zero, continuity of the bounded entropy gives the upper limit zero; the middle vertex supplies the lower bound. Integration from infinity therefore fixes exactly

\[
 F(x,b,y)=\tfrac12\log b+
 \frac1\pi\int_b^\infty
       \arctan\!\left(\frac{\sqrt{At+P}}t\right)\frac{dt}{t}.
\]

There is no missing additive constant. The integral converges, and the lower bound in fan (11) follows from monotonicity in P and \(\arctan z\ge z-z^3/3\), valid for every \(z\ge0\). Its two integrals give coefficients \(2/\pi\) and \(2/(9\pi)\), respectively.

The positive Descartes update gives

\[
 b_{j+1}=A+b_j+2\sqrt{Ab_j+P},\qquad
 \sqrt{Ab_{j+1}+P}=\sqrt{Ab_j+P}+A.
\]

This proves the quadratic formula for b_j, with the positive square-root branch. The same update on the other retained side gives independent even counts j,k. Rounding the initial difference in units of two makes \(|U-V|\le1\); adding a common even amount makes both U,V at least four. No density or arithmetic approximation beyond this elementary rounding is required.

The rational constants in the retained-port comparison check directly. For \(U\ge V\ge4\), \(U\le V+1\le5V/4\). The positive part is at least \(18/(5\pi V)\), and the cubic correction is at most \(1/(36\pi V)\), giving \(643/(180\pi V)\). The log-ratio is at most \(64/(63V)\). Their difference exceeds \(3347/(27720V)\) using \(\pi<22/7\). Consequently the exact full port action strictly exceeds both middle logarithms. The strictness can become small for large fan counts, but each final diagram is fixed, so this creates no uniformity problem.

For a newly added port the outer sum is \(A'=b+b_1\ge A=x+y\); its middle pair is x,y. The algebraic test \((A'+x)(A'+y)\ge\max(x^2,y^2)\) follows. At every surviving positive middle the entropy bound \(F\ge\frac12\log(\text{sum of weights})\) is strict because at least two weights are positive. This gives genuine strict balance even when the algebraic inequality is an equality. Previously added ports are not changed: the next insertion subdivides only the triangle belonging to the retained old port, not either triangle of an earlier new matching pair.

## 3. Protected zeros and the geometric insertion

The two protected vertices are joined by the marked MAIN edge. A matching edge cannot have that same pair of endpoints in a simple white sphere. Thus every port has \(A=x+y>0\). The four vertices of a matched quadrilateral are distinct, so there cannot be a hidden third zero from identifying a middle with an outer vertex.

The possible degeneracies are harmless for the formulas actually used:

* If one outer curvature is zero, the fan and triangle derivative use \(P=0\) and remain valid.
* If a current middle is zero, the positive Descartes update still creates a positive new curvature because A is positive.
* With two protected lines in one triangle, the positive disk is the interstice disk between those lines and the remaining circle. In the normalized zero-curvature formula the new disk can have the same curvature as the existing finite circle; this is a genuine strip configuration, not a forbidden three-zero triangle.
* If an overloaded middle is zero, the corresponding finite LEFT or RIGHT polynomial is exactly zero. No logarithm of zero is taken and no lower bound is requested from that missing sector.

The local topological change has been specified by actual strip joins. In particular it uses \(P_v=T^{-1}h_v\), not a scalar convention \(T^2=1\). Replacing one matched triangle by three and matching the two side triangles gives exactly the retained old port and new port stated in fan (3). All external ends may lie in a larger cyclic diagram; the operation is supported inside its disk collar.

The geometry is likewise local. The positive interstice circle lies in the chosen complementary triangular region of the existing labeled packing. The usual attachment is one ideal right-angled octahedron across that shaded triangle in each projection copy. Its neighboring white planes coincide with the old ones, and its new shaded disks lie inside the old outward shaded disk. This containment is the supporting-halfspace argument in actual_smoothing_fixed_radius_gap §3. It prevents intersections with unrelated old facets; it is stronger than observing the local dihedral angles or matching a volume. The construction is invariant under the normalization of any tangent triple, including a line limit. It therefore preserves the supplied global certificate and adds exactly \(2v_{\mathrm{oct}}\) per insertion.

The marked MAIN edge remains as a boundary edge of any subdivided triangle containing it. A point of its physical strip can be kept outside the insertion collars, so the original mark and its two adjacent faces persist. There is no replacement by a new mark with independent target normalization.

Even numbers of turned odd terminal braids give the identity four-endpoint pairing. Composing these through-braids creates no internal closed component. This proves preservation of the core's knot **pairing**, and only that. None of these steps proves isotopy of the filled knots before and after decoration.

## 4. Actual source, ordering, measure and full normals

The first-side new quartet in the source adapter is orientation preserving: outer pair b,w, input middle y and output middle x. Therefore its polynomial is

\[
                         H_g(b,y,x,w),
\]

while the old retained polynomial becomes \(H_f(x,w,c,y)\). Replacing this factor by an entropy-symmetric permutation would not be justified at finite level. The displayed factor is the correct one obtained from the actual three triangle sectors and strip joins.

The original local matrix formula is

\[
 f(\Omega)_{r,s;u,v}
  =N^{-1}q^{-d(r-u)}c^{-d}H_f(x,b,c,y)
  =N^{-1}H_f(x,b,c,y)/(bc)^{d/2}.
\]

The second equality uses coherent integrated face-log lifts, not arbitrary reductions of individual heads modulo N. The Casimir endpoint zeros exclude a modular transition with an illegal unwrapped total before it can contribute. These are precisely the hypotheses of actual_homogeneous_casimir_face_source (6)–(7a), and they survive the inserted collar.

The changes of middle counts are \(\delta M_b=-1\), \(\delta M_x=\delta M_y=1\), \(M_w=1\). The actual face winding relation \(M_f-T_f=2\), with exterior value -2, gives the displayed changes of turn counts and \(T_w=-1\). Hence the new face exponent is \(-d\), all old demands are unchanged, and the new ordinary target is exactly d. The argument includes a possible exterior old face because its winding is unchanged; w is a new bounded face.

At even N, the parity cochain has zero jump on matching sides and unit jump on MAIN sides. The extension \(t_w=t_b\) is forced and gives the new matching side bw and both new MAIN sides the correct clocks. This is not a new choice of parity frame.

The mark is unrestricted until whole-network conservation forces its two remaining heads to sum to d. Only then is its ratio to the original ordinary cap \(N^{-1}(L_{b_*}/L_a)^d\). Literal cup/cap formulas show that an inserted cancelling pair contributes no residual N power or fixed q scalar. A new coupon supplies \(N^{-1}\) and the new primitive face grid supplies N. Thus the refined marked summand has exactly \(N^{-R'-1}\) and its coefficient average exactly cancels this factor.

The number of faces is R'+2, leaving R'+1 grids after the common potential is fixed. Homogeneous degree dR' and nonnegative exponents force every ordinary exponent to equal d, and both protected exponents to equal zero; no additional N-shift alias can survive. The even coset character is then one. This checks the full coefficient (15), rather than only its exponential rate.

The arbitrary full coupon hypothesis includes the cleared resolvent polynomial. Consequently repeated Casimir-node derivatives are retained by the same source identity. CROSS is selected only afterward by the disjoint finite polynomial path partition. It need not, and is not asserted to, be a separate physical Hopf-algebra coupon.

## 5. The one-sided estimate is the actual weighted estimate

The key inherited input is actual_global_left_weighted_spectral_envelope, not a false coefficientwise domination. It retains both unused cofactor products and the original start/end indices, proves the signed tail bound, and obtains a value bound for arbitrary phases at the fixed positive moduli. Its endpoint argument extends through the small excluded real spectral cap, including both parity conventions.

At one port the resulting rates are exactly

\[
 L=\max\{\log c,F(x,b,y)+\tfrac12\log c\},\qquad
 R=\max\{\log b,F(x,c,y)+\tfrac12\log b\}.
\]

If c=0, LEFT vanishes; if b=0, RIGHT vanishes. Otherwise strict balance beats the first term, and \(F(x,c,y)>\frac12\log c\), or its b analogue, beats the second term. The latter inequality remains strict for a single outer zero because A is positive. Thus every surviving one-sided factor loses a positive amount against its complete port action.

The SAME face radii are used in every factor and in the one shared coefficient target. The calibrated subtraction of ordinary log radii is exactly \(\operatorname{Vol}(Y)/(2\pi)\). There is no independent radius optimization, capacity minimax or interchange of maxima. A fixed diagram has finitely many sectors; the minimum of its surviving gaps is positive. If none survives, the full-minus-CROSS remainder is zero.

This explicitly avoids the known counterexample to a universal individual-coefficient LEFT/CROSS comparison. It also explains why a one-sided fan is insufficient: sending only one middle to infinity can violate the true balance condition, even though it improves some simpler local quantities. The two-sided construction controls the logarithmic imbalance by the positive integral remainder.

## 6. CROSS packet and geometric intersections

Deleting two vertices from a simple triangulated sphere leaves the ordinary graph connected. Each surviving ordinary edge is contained in an actual triangle with two positive weights. Its local angular gap detects the corresponding phase difference; one-variable boundary triangles remain monomials and impose no false phase equation. Primitive difference rows imply that common phase is the only surviving phase, with no new angular alias. The Cauchy quotient dimension is R'-1 and its measure is the original coefficient measure.

The complete face action is the sum of the local source-normalized triangle actions minus the ordinary targets. Its Hessian has only common scaling in its kernel; after fixing scale it is positive. The original finite cofactor interpolation, including beta factors, midpoint offsets and parity, therefore produces the same relative finite-N CROSS packet. This uses only the all-CROSS packet theorem and its explicit general Morse extension. It does not use the older full-numerator Fejer/flat-forest restoration.

At a matching port there is at least one nonmonomial triangle. If both outers are positive this is immediate; if one outer is protected zero, at most one of its two distinct middle vertices can be the remaining zero. Hence a separated real spectral coordinate has a strict local loss. The shared angular complement handles arbitrary spectator phases, giving the required whole-coefficient global spectral bound.

The geometric deformation is also one global pattern, not independent reflected circles chosen at ports. The marked line-circle system fixes the two protected lines and all signed matching inversive distances on the original simplicial sphere. Its rank proof propagates rigid infinitesimal motions across the triangulated disk left by the two protected-edge triangles. At line limits the side equations fix the strip consistently. Thus the nearby complex pattern exists on one common chart and has the stationary radii. Nonincident geometric inequalities are strict at the fixed complete certificate; the sufficiently small real geometric neighborhood retains them. The complex neighborhood is used holomorphically, not asserted to be a real circle packing.

From that same pattern, the products of white reflections telescope along every Morse slice. A cup or cap contributes inverse heads because its outside faces coincide. Each physical port uses its full primitive collar, including its parabolic divided-difference value, and the original signed Hurwitz factor. Cycles introduce no independently selected frame because all reflections already belong to the common pattern. This is the substantive representation-level reason that the Morse extension has the original geometric target. Matching eigenratios alone would not suffice.

## 7. Whole period, charges and noncancellation

The literal period retains its Cartan scalar, charge product, parity and every sine endpoint. The all-CROSS finite phase remains in the exponential; replacing it by its limit could alter a prefactor and is not done. It is separately even and has the nondegenerate limiting diagonal angular Hessian. The local fixed-charge equations in the period audit preserve the exact multiplicative denominator in each slope, so independent signs and very unequal fixed slopes do not produce an uncontrolled additive error.

The local Gaussian leading coefficient is nonzero. Reflecting one charge reverses both its sine factor and its charge multiplier, so the sign-unit terms are exactly equal before approximation. The parity product cancels the original (-1)^{dR'} in the packet. This is a genuine noncancellation argument at both parities.

Whole-interval integration by parts is the correct operation for the infinite charge sum. The sine factor is zero at both endpoints, the first derivatives agree, and the second-derivative endpoint current remains after three integrations. Multiplication by the original charge weight leaves an absolutely summable inverse-square spectator bound. Far-charge vertical currents are paired before estimating; their double zero at the lower endpoint gives the stated cubic denominator. The new half-angle endpoints and frame characters in the Morse source are unchanged, so that proof has exactly its original hypotheses. No infinite sharply cutoff charge series or complex deformation of unnecessary real spectators is introduced.

The noncross gap extends to a fixed thin strip by finite spectral degree. Applying the same whole-period estimate preserves an exponential loss below the complete augmented action. The nonzero first-charge action approaches that complete action as the minimum fixed filling magnitude tends to infinity. A threshold depending on the final decorated diagram therefore places it above the remainder and all retained nonminimal charges. This is not uniform in a growing diagram or in N-dependent filling powers.

Finally the original primitive equations are U+pV=-2pi i with n=epsilon-2p, retaining the half twist once. The marked regulator cancels the filling Gaussian and linear boundary terms; the target is the actual smooth filled decorated exterior. For the retained knot parity it is that knot complement. The final zero-framing/component conversion is its own original unit character, and a full one-cut modified convention retains its polynomial factor. None of these operations restores the undecorated knot or removes the cyclic magnetic coordinates.

## 8. Qualifications that should remain visible

The source identity alone needs no positive certificate or balance. The volume theorem does. All new fan sizes and all final filling powers are fixed before the level tends to infinity. The old core powers are also sufficiently long in this theorem. The source still has its cyclic magnetic lattice; it has not become an operation-tree kernel product. No moving-main profile or filtered operator consequence is obtained for this new Morse family by this argument.

The supplied-certificate version contains no remaining analytic/source omission identified in this read. A future removal of that premise must cite the separate simple-block geometric proof, and is not justified merely by the entropy or scalar source calculations audited here.
