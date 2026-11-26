# Review before the fixed Wall degree-separation test

7 November 2026. This record is written before the single execution.

The fixed protocol is
`notes/research_mixed_fourier_wall_degree_separation_protocol.md`,
SHA256 `e962441bf71b0d0d92cb24862280ee80823af8a1e87ed2d3ba3c4ce91ce99ac4`.
The complete checker is
`experiments/check_mixed_fourier_wall_degree_separation.py`, SHA256
`142d1f2911ba727d1a1ea230a2a9cdeb189ec827a2b6398c337cf648474627db`.

Root and the terminal reviewer have read the complete proof and code.
They checked the original degree polynomial, the identity for its
unit-circle exclusion, both rational charts, the degree-eight
Bernstein transformation, exact interval operations, all 128 cells
and 1152 coefficients, and the full saved parameter provenance.
The input root square and its parameter image are retained in full.
All source bindings are checked again at completion. The initialized
finite-solution proof was also fully read; its extension remains
conditional until the certificate succeeds.

The output path
`repro/results/research-mixed-fourier-wall-degree-separation.json`
was checked absent. It will be created exclusively. No preceding
execution, arithmetic trial, source replay, root solve or parameter
probe has been performed for this test. Only source reading, AST
inspection, metadata inspection and hash checks preceded this record.

The sole command is

```sh
python3 experiments/check_mixed_fourier_wall_degree_separation.py --script-sha 142d1f2911ba727d1a1ea230a2a9cdeb189ec827a2b6398c337cf648474627db
```

An inconclusive or failed result is retained without refinement,
changed criteria or retry. Success will certify root separation;
the finite asymptotic and the comparison with the knot volume remain
written mathematical deductions with their own stated scope.
