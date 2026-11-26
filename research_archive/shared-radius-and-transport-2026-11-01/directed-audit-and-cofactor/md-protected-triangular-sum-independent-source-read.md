# Independent source read of the protected triangular-sum closure

This is a bounded mathematical review of `md-protected-triangular-sum-full-volume-closure.md` at SHA256 `d522b708d44f9dcd87f644402caabc306aeb850805870847b3d715205a039a6d`. All seven sections were read. No mathematical correction was found in the new closure argument. The scope is the stated unabridged shared-radius hypothesis; it is not a transfer theorem for arbitrary signed source bounds or for arbitrary inserted blocks.

No numerical experiment, compiler, or global manuscript build was run for this review. The existing local spectral estimates and geometric completion remain written proof inputs. This review checks their literal interface with the new construction; it does not count an earlier review verdict as a proof of those inputs.

## 1. Oriented construction and target count

The first removed triangle is \((u,v,B)\), and its matching partner is \((u,B,c)\). The first old quartet is therefore \((u,v,c,B)\). The second removed triangle is \((u,B,v)\), with partner \((u,a,B)\), giving the old quartet \((u,a,v,B)\). The two removed faces have opposite orientations. The two surviving partners meet along the same edge \(uB\) and give exactly \((u,a,c,B)\).

This uses the recorded ordered quartets. No symmetry of a scalar entropy is being substituted for a physical frame. The allowed reflection of an entire input transports its cyclic orders, label meanings and crossing signs; it is not a relabeling of one matrix inside a fixed source.

The two closed triangular disks being glued have disjoint interiors and only their three named boundary vertices in common. Simplicity is preserved: no interior edge acquires coincident endpoints, and the three common edges are identified once. The only changed matching pairs are the two selected pairs; their surviving triangles are paired across \(uB\). The original nonmatching edge \(uv\) stays nonmatching. In particular
\[
 V=V_1+V_2-3,\qquad
 R=R_1+R_2-1,
\]
and the ordinary target list is the union of the old ordinary lists with the two copies of \(B\) identified. No other ordinary target is lost or duplicated.

The inverse-cut source theorem applies to this new simple matched sphere. Its original terminal-pairing test must still be made for the chosen parity pattern. The note retains that test and makes no claim that the old knots or their old twist words survive unchanged. A spanning-tree choice can produce a one-component pairing, but the volume conclusion is restricted to a chosen parity that passes the actual new test.

## 2. Shared pressure identity

The singleton triangle has \(Q(0,0,B)=\frac12\log B\), because the only allowed load is \(1/2\) at \(B\) and the endpoint entropy is zero. Let
\[
 Q_a=Q(0,a,B),\quad Q_c=Q(0,c,B),\quad q_B=\log B.
\]
The two old central bridge rates are
\[
 C_1=\tfrac12q_B+Q_c,\qquad C_2=Q_a+\tfrac12q_B,
\]
whereas the new one is \(X=Q_a+Q_c=C_1+C_2-q_B\). The sum of old target terms subtracts \(q_B\) twice, while the new target subtracts it once. Hence the full shared action, rather than merely its local terms, satisfies
\[
 P_{\rm new}=P_1+P_2
\]
when the two coordinate vectors agree at \(B\).

All local rates have homogeneous degree one and the number of ordinary targets is the number of crossing regions. Rescaling a whole input witness therefore does not change its action. Both complete minimizers may be normalized to \(B=1\), giving the exact equality of complete pressures. Conversely every glued vector restricts to two input vectors, so its pressure is at least the sum of the two minima. This proves the claimed equality in both directions. It also identifies the glued complete curvature vector, without assuming that filled manifolds are sums of their filled inputs.

## 3. The genuine one-sided inequalities

The simplex vertex at \(B\) gives \(Q_a,Q_c\ge q_B/2\). This remains true when \(q_B<0\); it does not use \(B\ge1\). The old first crossing has protected input middle \(v\), so its right piece is absent. The old second has protected output middle \(v\), so its left piece is absent. Their surviving one-sided rates are
\[
 L_1=\max(q_c,(q_B+q_c)/2),\qquad
 R_2=\max(q_a,(q_B+q_a)/2).
\]
At the merged crossing,
\[
 L=\max(q_c,Q_a+q_c/2),\qquad
 R=\max(q_a,Q_c+q_a/2).
\]
Direct subtraction gives
\[
 L\le L_1+C_2-q_B,\qquad
 R\le C_1+R_2-q_B.
\]
Both branches of each maximum are retained. A pure overloaded-middle bound would not suffice for these inequalities.

The whole output label string maps to input labels by
\(C\mapsto(C,C)\), \(L\mapsto(L,C)\), \(R\mapsto(C,R)\); every other local label stays on its input. The induced labels are locally allowed. A noncentral output necessarily has a noncentral induced input, either at the merged crossing or elsewhere.

The unabridged hypothesis is essential and is stated explicitly. It covers induced input strings even if an independent global support argument made their old shared coefficient zero. Such a zero is not silently inherited by the new coefficient. Only local protected-overloaded vanishing is omitted automatically.

Choose a strict witness for each noncentral induced input, and the complete minimizer for a central one. Normalize each entire vector at \(B\). The shared coordinates then agree: \(u,v\) are exactly zero and \(B=1\). The duplicate-target calculation gives one legal shared Cauchy vector with loss at least \(\min(\gamma_1,\gamma_2)\). No face is weighted separately at different incidences.

## 4. From that inequality to the original full invariant

The local bound used here is phase-uniform on the entire real spectral interval. The left-envelope proof retains both unused spectral products and all original start/end rows; its continuous-real tail positivity supplies the passage to arbitrary face phases. The reflected physical order supplies the right bound. The central bound is the original two-triangle bound and includes the odd central row. These local statements apply at both parities.

After multiplying the actual local polynomials and taking the original one shared coefficient, the source has degree at most \(d=N-1\) in each spectral variable. Local projection to a specified path piece does not increase that degree. For each of finitely many output strings, the preceding witness gives the rate \(\Phi-\gamma\). Replacing target \(d\) by \(N\) in the normalized rate costs only \(\sum\log L_f/N\), with one fixed witness per string. Fixed polynomial prefactors, fixed source size and finitely many label strings therefore contribute only \(o(N)\). This proves a supremum bound for the whole complementary polynomial on \([-2,2]^R\), not merely for one endpoint.

The exact source identity is the general Morse identity in `research_matched_sphere_morse_source.md`, Sections 5--6. Its supported head sums and primitive grids cancel the original marked/grid factor; its total homogeneous degree forces the two protected targets to be zero and the other targets to be \(d\). The even-level coset character is one on that supported alias. Thus no new factor of \(N\), mark, or independent face sum is added by the triangular join.

The finite functional of `actual_uniform_filling_supremum_bound.md`, equations (1), (6)--(15), acts on this full polynomial after the shared coefficient is taken. Its norm is at most
\[
 \prod_e(1+|n_e|/2)
\]
for fixed signed powers. This includes the actual crossing scalar and the first derivatives at double nodes. Its odd simple node is counted once. The stronger node-vanishing bound is unnecessary. Consequently the filled complementary term has the same exponential upper rate; there is no new Fourier-tail argument to assume.

The all-central Morse period theorem supplies a separate nonzero asymptotic for the actual new sphere. Its source hypotheses are a simple white sphere, the recorded matching and cyclic orders, the marked edge, and the positive geometric certificate. The constructive complete packing exists before any terminal decorations and allows separating triangles. The new sphere satisfies these hypotheses. No middle-face forest or flat-plat presentation is invoked.

The all-central theorem retains the parity-dependent raw factors, the primitive face quotient lattice, the first-charge coefficient and the spectral determinant branch. Its geometric companion identifies the same first-charge action with the new filled complement using the original disk slopes and same-chain volume calibration. The note does not deduce this filled volume from additivity of the complete pressure.

For independently sufficiently long fixed signed fillings, the central real action is above \(\Phi-\gamma/2\), while the complementary rate is at most \(\Phi-\gamma\). The strict separation and nonzero central asymptotic yield the full-invariant equality by the reverse triangle inequality. The original framing/component character has unit modulus at complete color; the optional one-cut modified factor has only polynomial size. The diagram and all powers are fixed before \(N\), exactly as stated.

## 5. Iteration and weak balance

The retained marked edge again has two incident triangles with a single ordinary third vertex. At a later attachment, rescale the whole previous witness, not its already identified faces separately. The same target and sector calculation then applies. Thus arbitrary finite iteration preserves a positive loss equal to at least the minimum of the fixed input losses. It does not give a size-independent threshold for a growing sequence of diagrams.

For weak-balanced inputs, \(X\ge C_1\ge\log c\) and \(X\ge C_2\ge\log a\). Every other complete comparison is unchanged after the common rescaling. This is a valid closure corollary of the existing weak-balance theorem. More general unabridged finite-cover inputs are also permitted, but arbitrary signed cancellations or fixed-cap estimates do not imply that hypothesis.

## Review limit

The new oriented sum, the pressure identity, all three merged-label cases, the unabridged-cover issue, the exact degree/mark/coset interface, and the comparison of filled rates were checked directly. The published local cofactor estimates and complete geometric metric construction remain external mathematical dependencies; their full proofs were not all repeated in this bounded review. No private cap-neighborhood or adjugate conjecture is used in the closure theorem.
