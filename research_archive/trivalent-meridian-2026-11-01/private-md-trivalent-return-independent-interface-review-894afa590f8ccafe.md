# Independent check of the trivalent return comparison

1 November 2026. This report checks the proof in
`/private/tmp/md-trivalent-bare-component-simultaneous-clamp.md`,
SHA256 `a83465c18882ad82cb6dcac35e91018153a9e775f99ba906e52087e9d036d066`,
against the exact fixed-Newton source and the earlier positive probe theorem.
No repository source is changed.

## 1. Exact source and endpoint domains

In fully covariant coordinates a physical turn identifies equal incident indices. The fixed metric alone would identify complementary indices. Thus the argument applies to a trivalent component of the original reduced tree, with a physical turn on every internal edge, and not to a binary resolution of a higher-valence product.

The exact old support is
\[
 i+j,\ i+k,\ j+k\le d,\qquad i+j+k\ge d,\qquad d=N-1.
\]
The exact return support is
\[
 i+j,\ i+k,\ j+k\ge N,\qquad i+j+k\ge2N-1.
\]
The return coefficient, including its sign and common factor, is
\[
 -\Delta_s(-1)^{i+j+k-d}
 \frac{N^2}{S_iS_jS_kS_tS_{i-t}S_{j-t}S_{k-t}},
 \qquad t=i+j+k-(2N-1).
\]
This is the symmetric form of the coefficient extracted by the unchanged anti-diagonal Frobenius pairing. It retains all repeated-root information.

For a finite-to-continuous comparison, the corrected proof uses \(x=i/d,y=j/d,z=k/d\). The old support is then exactly the old continuous domain. The return complements are nonnegative and have total at most \(1-1/d\). This avoids substituting a finite tuple with total \(1+1/N\) into the real-domain integral \(J\). The exact factorial arguments divided by \(N\) differ by \(O(1/N)\), so the endpoint modulus of continuity of \(J\) costs only \(O(\log N)\) in the logarithm. The finite offset has therefore been accounted for, including zero complement endpoints.

The six-type turn table also gives the needed separation of return vertices. An equal-color endomorphism turns into a constant-relation mixed morphism; a constant mixed morphism can turn into an equal-color endomorphism. No physical turn joins two moving-relation product vertices. Since a return requires a moving relation, return vertices form an independent set. This is a statement about the original ordered types, not a property inferred from the absolute entropy.

## 2. The hard-half region lemma

For an old region with at most one marked incidence at each vertex, set each marked label to one half and every other wire or ordinary terminal to \(3/8\). Every cubic inequality is strict. This gives a full open box of feasible marked boundary values.

The boundary-barrier proof remains valid with the marked half terminals. Root at one of them. Endpoint descent along a product/turn tree cannot terminate at another marked terminal, because its fixed value is one half. It must reach an ordinary leaf at an endpoint or a nonvertex-flat gate. The directional derivative toward the strict state is then positive infinity, while the other volume atoms contribute finite derivatives or positive infinity, never negative infinity. With all variable wires interior, every saturated gate face similarly supplies a nonvertex-flat atom. Thus the constrained maximizer is strict.

Each strict cubic has negative definite Hessian in its three labels. Every free wire occurs in a gate. The constrained Hessian is therefore negative definite, proving uniqueness and an analytic maximizing branch near the all-half boundary.

The response argument does not assign an artificial physical geometry to a fixed terminal. Its incident gate supplies a positive response \(\kappa\), and its cotangent \(B=0\) gives \(-Y<B<X\) for every such response. Ordinary terminals are \(L\)-type, with \(B=X>0,Y=1\). Every internal turn acts on a proper product output, not on an ordinary \(L\) terminal. The corrected structural wording is essential here.

The product formulas preserve properness. For \(X\ge1\), proper inputs have positive \(B_i\), and
\[
 B-X=\frac{(X-B_1)(X-B_2)-1}{B_1+B_2}<0.
\]
For \(X<1\), write \(B_i=h\cot\alpha_i\), \(Y_i=h\csc\alpha_i\), \(h=\sqrt{1-X^2}\). The positive denominator implies \(\alpha_1+\alpha_2<\pi\), and \(B_i\le X\) gives the strict output inequality. Turns preserve the proper inequalities.

At a chosen marked root, its outgoing product has \(B=0\). Both input labels are below one half, hence \(B_1,B_2>0\), and
\[
 Y^2=1-X^2=B_1B_2\le X^2.
\]
Thus the outgoing derivative is nonnegative and the derivative in the marked covariant boundary coordinate is nonpositive. Joint concavity supplies one supporting plane at the all-half point. It proves the simultaneous clamp for all marked coordinates at once; it does not assert the false coordinatewise monotonicity with the other boundaries fixed above one half.

## 3. Low return arms and reassembly

Record the exact finite high/low pattern before passing to a limit. An old vertex has at most one recorded high incidence; a return has at least two. The pattern survives exact-half limiting labels.

After deleting all returns, every low return arm ends in exactly one old region or one original boundary leaf, because returns are nonadjacent. Assign the profile \(g(x)\) to its old-region endpoint. This increases the starting comparison because the discarded return entropy is nonpositive and \(g(x)\ge0\). It does not replace a signed source by a new physical leaf; it is an intermediate action comparison.

Each region can now be optimized jointly, with all its high boundaries clamped to one half. The added low-arm profiles are genuine \(g\)-profiles for purposes of the hard-half lemma. Their labels are free during this optimization. Different regions have disjoint free labels.

Reinsert each return as an old vertex. Two high arms and a low arm become \((1/2,1/2,x)\), whose old action is exactly \(g(x)\). Three high arms become \((1/2,1/2,1/2)\), with action zero. The \(g(x)\) assigned during the region optimization is consumed here exactly once. A low arm ending directly in an original leaf contributes \(2g(x)+c\), at least its original \(g(x)+c\); a high original leaf becomes half and keeps its constant because \(g(1/2)=0\).

These statements include \(x=0\), \(x=1/2\), and cases in which there are no old regions at all. No division by an endpoint sine is used. No low arm is held at its former value while an incompatible high interface is changed.

The reassembled state is feasible in the original all-old coupled source. At least one replaced vertex has a pair sum equal to one. Its action is bounded by the maximum on that fixed old boundary stratum. The original unique optimizer is strict, so compactness gives a positive gap. This proves a strict absolute gap for every nonempty return sector, including returns with zero local entropy.

## 4. Relation to the existing source bounds

The old sector with a high original input or high output probe is already covered by the arbitrary-array result in
`notes/actual_conway_unflagged_core_probe_bound.md`,
Sections 1–4. Its recursive grammar permits turns and products inside a general unflagged region; its input hypothesis is the full low \(g+c\)/high \(c\) coefficient cone. This is the required interface, not a physical core/alias equality. The same proof supplies original-coordinate localization and local boundary-coefficient loss transfer in its Section 5.

The paired edge weights are uniformly bounded on every fixed \(|s|\le R<1\). There are finitely many sector patterns and polynomially many states for a fixed tree. The uniform closed factorial rates therefore convert the action gap into a strict finite-source exponential deficit. Additive boundary constants remain affine, so inherited full-cone deficits propagate with the same constant shift.

The leading clean comparison must keep the full range of internal bare–bare labels. An internal complete maximizer can be exactly at one half; the earlier global all-retained-low assertion cannot be reused. Boundary labels at circle interfaces remain in compact low intervals. Near a strict old cubic, pair sums are below one and total degree is below \(3N/2+O(1)\), so its moving trace equals the complete trace exactly once the raw degree is below \(2N-1\). The fixed Gamma-product interpolation and \(H_N/W_k\) insertion are regular for all internal labels in compact subsets of \((0,1)\), including one half.

Accordingly the local packet has the same strict primitive Hessian, while its admissible window must allow these full internal labels. The auxiliary-color and filling conclusions require this corrected clean-window invariant to be inserted throughout the global argument. They do not follow from an unchanged claim that every high retained edge has a gap.

## 5. Conclusion and limits

The corrected proof establishes the whole-component source bound and strict nonempty-return/high-boundary deficits for arbitrary finite trivalent bare components with actual physical turns. No many-boundary count is required for such a component. It is compatible with previously controlled components elsewhere in the reduced tree.

The proof does not cover arbitrary higher-valence adjacent bare junctions by resolving them into cubics. Such resolution changes the internal edge pairing and can create adjacent returns or returns with all original exterior indices low. The old open-profile and coordinatewise-clamp counterexamples remain valid outside the precise simultaneous comparison established here.

## 6. Direct check of the grouped-packet hypotheses

I reread `notes/actual_main_meridian_grouped_wire_packet.md`, Sections 3–8, with the full internal-label invariant. Its present Section 3 states that every retained edge is regular low, and Section 4 removes a summed high-edge part. Those statements belong to its currently stated separated/path-budget class. For the new trivalent class they must be replaced, rather than quoted unchanged: remove nonempty return sectors and high effective input/probe sectors, keep all complete-supported internal bare labels, and restrict only circle-incident labels to a compact subset of \((0,1/2)\).

After this replacement, no additional low-index hypothesis is needed in the packet argument. The bare factorials are in compact bulk intervals by the strict old cubic inequalities. The edge insertion in its equations (25)–(26) is regular on every compact subset of \((0,1)\), including half; its expansion remains valid there. The special basis evaluation in (23)–(24), which does require a low label, occurs only at a circle incidence. The angular localization of Section 7 likewise uses these circle factors, multiplied by nonnegative complete bare coefficients. It never uses a low bare–bare label.

The primitive lattice, integer complements and power count do not change. The strict Hessian covers a circle-incident variable by its leaf action and every remaining variable by a retained gate. The exact finite cotangent contour only needs a strict bulk box, a nondegenerate saddle and a strict boundary loss. Thus its residue representation, endpoint currents, even angular Hessian and insertion expansion survive the corrected window. For a trivalent bare vertex the complete replacement is exact, so the higher-valence regular-alias estimate is unnecessary there. It remains available for other components already within its stated low-input hypotheses.

This is a dependency check of the packet construction. The final enlarged global statement should still assemble the corrected component invariant, arbitrary-color rerooting and joint filling transform explicitly; it should not replace the hypotheses of the currently published packet theorem without that assembly.

## 7. The written global extension

The subsequent full derivation `/private/tmp/md-trivalent-bare-components-global-meridian-extension.md`, SHA256 `f5d4481010a50697884071fa5496851a18f315723db6ac4b56e0d6b7e4a2c012`, supplies that assembly. Its exact component decomposition retains the full old internal support, removes returns and high effective boundaries by the respective strict losses, and propagates inherited losses by a shift of the boundary constants. Reconstructing only around the maximizing low output probe gives the fresh angular Gaussian; the remaining canonical polynomial is controlled by full Hermite interpolation with its already proved strict deficit.

Its three rerooting cases retain the original typed adjunction scalar. An ordinary leaf attached to a bare junction now exposes the whole maximal component, whose probe closure is precisely the original closure with that existing leaf. No new geometric cap is charged. The auxiliary-color contour therefore receives the same original exponent and a fresh Gaussian on its stated smaller main-parameter disk.

The global packet proof explicitly distinguishes low circle incidences from full-bulk internal edges. The regular bare equality for a trivalent vertex follows directly by division of a polynomial of degree less than \(2N-1\): changing the quotient relation changes only a remainder of degree at most \(N-2\), which its top-coefficient trace does not see. Every strict primitive factorial and edge insertion is then holomorphic in the same kind of fixed tube. The nonzero wire Gaussian, the real-spectator angular estimate and the finite-grid currents therefore supply the unchanged joint-charge hypotheses.

The final threshold argument correctly keeps the structural error at the augmented action until the joint first-charge saddle is chosen. All tubes, geometric losses and curvatures are independent of the fixed disk radius. The Fourier multipliers have a bound with \(R'<1\) replaced by one; constants may worsen as the disk approaches its boundary, while the slope threshold stays fixed. Independent slope sizes cause no new comparison of separate local errors.

The author applied the following wording refinement in Sections 2 and 4: the statement that return-free bare tensors are literally complete and positive concerns the new trivalent clean sector. When a tree also contains previously allowed higher-valence components, their existing whole-hub positive majorant controls the global low sector before their regular trace replacement. Their low-input return terms are not discarded by that sentence. This does not alter the derived estimate or scope.
