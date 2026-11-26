# Independent source-bound reproduction check

1 November 2026. Private report; no script or publication file is changed by this check.

I read `experiments/audit_main_meridian_source_bounds.py` in full. Its cyclotomic calculation builds low Newton factors directly from the node factors and then uses ordinary polynomial division by the monic moving relation. Independently, it expands that polynomial at `z=-(u+u^-1)` and evaluates the stated Fourier formula as a polynomial in the deformation parameter. The normalization `(-1)^(N-1)N^2`, the Fourier sign `(-1)^((N-1)(ell+1))`, and `cos(2 pi s)=1+delta/2` agree with the source conventions. The use of any primitive cyclotomic embedding is legitimate for these algebraic identities; it is not used for a positivity test.

The integer interval checks convolve interval indicators directly. The path checks locate the first strict slack in an original odd-level positive closing path, add one to that and every subsequent running index, and verify each original even-level support inequality. Existence of such a slack follows from the separately imposed total degree at least `N-1` and odd final index `N-2`. The program also checks the stated multiplicity bound. The factorial ratio section is explicitly an 80-digit numerical check rather than an exact proof.

I replayed the unchanged script with `/Users/sasha/.venvs/global/bin/python3`, writing only `/private/tmp/md-source-bounds-independent-reproduction.json`. It completed with 131 exact trace identities, 911 integer tail comparisons and 148 mapped paths. The complete result is byte-identical to `/private/tmp/md-source-bounds-root-reproduction.json`, including versions and the script hash.

Private reproduction SHA256:
`9ef9949b00a8fd1f43d20a7fb7acc3773bf67bdc241afb7f92cc562ad045f5a9`.

These computations check the finite examples recorded by the script. The arbitrary-level Fourier identity, all-index path bounds, geometric pressure and source theorem depend on the written proofs, not on extrapolation from this finite reproduction.
