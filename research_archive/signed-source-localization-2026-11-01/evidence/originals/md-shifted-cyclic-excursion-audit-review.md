# Read of the finite cyclic-excursion runner

1 November 2026.

I read the entire runner against the frozen proof and then ran it once:

- Script: md-shifted-cyclic-excursion-audit.py, SHA256 d213d2d73aadaeeb550ff1a3ed5208e53f99065c2404417a0483eef3c9d52331.
- Proof: md-shifted-cyclic-excursion-and-clock-reduction.md, SHA256 353c2939a06731c88da1843b7946f2640755e8eba822cf05892232bf1978a55d.
- Independent run: python /private/tmp/md-shifted-cyclic-excursion-audit.py --output /private/tmp/md-shifted-cyclic-excursion-independent-results.json.

The run completed successfully: 16 finite-field source cases, 96 local clock comparisons, 10 support graphs, two shifted-target cases, and the two exact integer counterexamples. Neither the runner nor the proof was edited.

## What is computed independently

The local numerator comes from powers of the literal two-variable upper-band Casimir, using the polynomial divided difference of \(\chi_N\). It does not import the continuant, Green expansion, transfer formula, or Schur identity. The additional check \((\sigma-C)V=\chi_N(\sigma)I\) is an exact polynomial-matrix check, including repeated spectral roots. The formulas for the off-diagonal entries agree with \(s_j^2=2-q^{2j}-q^{-2j}\) and \(s_js_{j-1}=c_0-c_{j-1}\).

The direct source calculation multiplies homogeneous monomial dictionaries in the south variable and ordinary rim variables, discards positive powers on the protected rim face, and extracts the prescribed target. Truncation above a target is legitimate because all exponents are nonnegative. It retains the reversed south middle order.

The transfer instead enumerates partial-load states and multiplies sparse matrices. Its local CROSS filter is compared with direct monomial CROSS extraction. Separately, the position-clock projection uses the incoming-state mask; the trace of its good block is compared with the same direct CROSS coefficient. Thus the projection identity is not tested merely by reusing the locally masked transfer.

The Schur computation constructs all four position-clock blocks and forms the coefficient of
\[
 (I-zA)^{-1}z^2B(I-zD)^{-1}C
\]
by sparse matrix convolution. It then sums the traces of its powers with the factors \(1/\ell\). It never substitutes the precomputed full-minus-CROSS value. The fields have characteristic larger than \(m=6\), so all divisions used in these finite trace coefficients are legitimate.

The support check is independent of all evaluated spectral coefficients. It builds the larger support containing every homogeneous north triple and every allowed homogeneous south triple, constructs the bad-state directed graph, topologically sorts it, and checks that its longest path has fewer than \(3m\) edges. This checks bounded instances of the support proof without obtaining acyclicity from signed cancellations or from a numerically small matrix power.

The clock calculation compares direct monomial phases with the proposed incoming/outgoing diagonal exponents. These are different calculations of equations (22)–(23). The reported 96 checks are local checks; they are not advertised as a separate test of every global Ward identity.

The shifted-target tests compare direct extraction with an enlarged transfer having \(u\le2d\). The selected shifts increase one ordinary rim target and decrease another, so their sum is unchanged. Consequently homogeneity still forces the south degree to be \(d\), and evaluating the completed transfer at \(S=1\) is correct in these tests. They do not test arbitrary south-target changes or replace the proof's instruction to retain the requested \(S\)-coefficient for general shifted targets.

## False-positive limits and one small hardening opportunity

All source calculations share the literal local-coefficient builder and its north/south interpretation. An identical error in that builder could survive the transfer comparisons. I therefore checked those formulas directly against the proof; the runner is not an independent reconstruction of the topological compiler. The independent integer \(N=3\) counterexamples provide additional fixed normalizations but do not remove that common dependency.

The finite-field checks establish the stated finite residues, not characteristic-zero polynomial identities at all levels or spectra. The support DAG checks concern only their listed \(N,m\). The written all-level support proof remains necessary.

The shifted-target code asserts that the enlarged transfer equals direct extraction, but only records, rather than asserts, inequality with the old state box. The current independent run has:

- \(N=3\): direct/enlarged \(625\), old box \(485\), modulo \(1009\);
- \(N=4\): direct/enlarged \(707\), old box \(588\), modulo \(1009\).

Thus the present statement that these two examples require enlargement is supported. An explicit old-box-inequality assertion would protect that negative check against a future change of cases or field. Its absence does not invalidate the current results.

I found no mismatch between the reported finite checks and their computations. They establish no spectral norm, exponential remainder bound, or volume theorem. This review includes one actual execution, not only a source read.
