# Circle-tree degree corollary and primitive normalized lengths

This is a read-only check of the quantitative master theorem, its analytic companion, and the original marked peripheral formulas. The input-file hashes are recorded separately in `md-all-circle-padding-and-normalized-length-inputs.json`. No numerical calculation is used below.

## Adding terminal circles

Let the starting ordered tree have \(m\ge1\) vertices, with original degrees \(\delta_v\ge0\) and arbitrary fixed integer powers \(n_v\). Attach the positive integer number \(B\) of new terminal vertices at each original vertex, retaining a specified cyclic insertion order and all physical frames. The new degree of an original vertex is
\[
 D_v=\delta_v+B\ge B.
\]
Each added vertex has degree one. This remains a finite tree, with \(mB\) new leaves and \(m-1+mB\) edges. Every vertex has its own crossing-circle location. A new terminal vertex may be chosen as the root, retaining the literal framed collar moves and the left/right child order of the resulting diagram.

The original vertices contribute at most
\[
 \sum_{v=1}^m\frac{D_v}{D_v^2+n_v^2}
 \le \sum_{v=1}^m\frac1{D_v}\le\frac mB.
\]
If every added power has magnitude at least \(B\), the new leaves contribute at most
\[
 \frac{mB}{1+B^2}<\frac mB.
\]
Consequently the enlarged tree has \(\mathfrak S<2m/B\). The integer condition \(B\ge2^{26}m\) implies \(\mathfrak S<2^{-25}\). This includes arbitrary zero or nonzero powers at the original vertices and also the case \(m=1\), whose original degree is zero.

The combinatorial estimate is independent of parity, but the knot conclusion is not. One must still trace all main strands in the enlarged literal diagram and exclude every extra closed component, including an internal one. The master explicitly retains this knot/parity test; neither the bound on \(B\) nor the magnitudes of the new powers prove it. The terminal additions produce a new filled diagram in general. The corollary does not assert an isotopy to the starting knot, or preservation of its invariant or volume.

## Inserting the identity at an existing product junction

This is different from adding the terminal branches above. At an existing ordered product junction, inserting the braid \(R^0\) between the prescribed factors does not change their two actual connecting strips or their order. Add an auxiliary crossing circle around that identity box and use the pure retained crossing \(\epsilon=0\). Its original disk-framed filling with \(p=0\) restores
\[
 R^{\epsilon-2p}=R^0.
\]
Thus the filled diagram is the same original ordered diagram. The augmented link is different: it now contains this extra auxiliary component. At a junction of degree \(d\), its contribution to the criterion is exactly
\[
 \frac{d}{d^2+0^2}=\frac1d.
\]
This applies inside the stated literal ordered tree class, with physical turns, the original closing convention and the knot test retained. It gives no free removal of a low-degree contribution and no assertion about arbitrary unrelated tangle graphs. The master states these qualifications.

For comparison, its other numerical consequence is exact: if every power satisfies \(|n_v|\ge8192\sqrt E\), then
\[
 \mathfrak S\le\frac{\sum_v d_v}{8192^2E}
 =\frac{2E}{2^{26}E}=2^{-25}.
\]

## Primitive cusp calculation

The original marked auxiliary curves in `actual_conway_general_mask_marked_filling.md`, Section 6, equation (18), have logarithms
\[
 U=\epsilon v-2\pi i t,\qquad V=-2v,
 \qquad v=\log\frac{\sin\pi(x-t)}{\sin\pi(x+t)}.
\]
At completeness put \(c=\cot(\pi x)>0\). Then
\[
 v_t=-2\pi c,\quad U_t=-2\pi(i+\epsilon c),
 \quad V_t=4\pi c,
 \quad \tau_{\mathrm{aux}}=\frac{dV}{dU}
       =\frac{2ic}{1-i\epsilon c}.
\]
Both \(U,V\) use the same squared-eigenvalue convention, so their ratio introduces no extra factor. In particular the Gaussian parameter denoted \(\tau_i\) in equation (21) of that older note is half this primitive translation ratio and must not be substituted for it.

The fully circled complete geometry gives \(c_v=1/d_v\). To read the degree convention directly from `actual_conway_rigid_spine_and_flagged_tree_geometry.md`, Section 5, equation (13), its Frobenius hub valence includes the distinguished circle leaf and is \(d_v+1\). Thus its formula \(1/(\text{hub valence}-1)\) is \(1/d_v\) here. Terminal circle vertices have \(d_v=1\) and the original quarter-index leaf has \(c_v=1\), consistently.

For a Euclidean torus whose primitive meridian is scaled to length one and whose primitive longitude vector is \(\tau_{\mathrm{aux}}\), its area is \(\Im\tau_{\mathrm{aux}}\). Hence the normalized squared length of the actual slope \(\mu+p\lambda\) is
\[
 \mathcal L^2=\frac{|1+p\tau_{\mathrm{aux}}|^2}
                         {\Im\tau_{\mathrm{aux}}}.
\]
Using the original physical identity \(n=\epsilon-2p\),
\[
 1+p\tau_{\mathrm{aux}}
   =\frac{1-inc}{1-i\epsilon c},\qquad
 \Im\tau_{\mathrm{aux}}=\frac{2c}{1+\epsilon^2c^2}.
\]
The common shear denominator cancels exactly, giving
\[
 \mathcal L^2=\frac{1+n^2c^2}{2c}
             =\frac{d^2+n^2}{2d},\qquad
 \mathfrak S=\frac12\sum_v\mathcal L_v^{-2}.
\]
Therefore \(\mathfrak S\le2^{-25}\) is exactly equivalent to
\(\sum_v\mathcal L_v^{-2}\le2^{-24}\). This is the normalized length in the original complete augmented metric and original primitive peripheral basis. It is not a statement about the length of a slope on the filled metric or an imported surgery criterion. The calculation is valid for both choices of odd retained crossing and for the pure crossing, including zero power.

The quantified corollary, the identity-braid qualification and all displayed normalized-length constants are correct as written. No editorial correction is needed.
