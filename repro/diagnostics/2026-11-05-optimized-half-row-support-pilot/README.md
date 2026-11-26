# Bounded optimized-envelope half-row pilot

This is an incomplete diagnostic, not a uniform half-row theorem.
Exactly one run used own flag 0, external flags (1,1), first input
on its circle and second input in its disk. It tested both original
conditional orientations and all real targets using the new
optimized-envelope rule. No full run, restart or numerical replay
followed.

Command:

    python3 experiments/certify_mixed_optimized_half_row_support.py --precision 256 --pilot --max-nodes 511 --max-seconds 60 --output repro/diagnostics/2026-11-05-optimized-half-row-support-pilot/result.json

The process ended with exit code 2 at the node cap. The
[saved partial record](result-partial.json) reports:

- 511 visited nodes and 249 accepted leaves; no completed face.
- 14 pending boxes, with exact volume 261609/262144.
- Accepted volume 535/262144; maximum accepted and visited depth 18.
- 68 root-enclosure subdivisions and 194 source-bound subdivisions.
- 11.0203 seconds, including setup and loading the pinned old record.
- 29 current dependency bindings.

No outward point obstruction was reported. The whole optimizer box
was clipped with outward interval arithmetic; only midpoint target
gains were added. Every accepted cell retained the original phase,
chirp, own flag, both outer halfweights and coupled root response.

## Comparison with the original pilot

The [original fixed-trial pilot](../2026-11-05-half-row-support-pilot/result-partial.json)
also used 256 bits and the same 511-node weak-face limit. Exact
tree reconstruction gives the **same resolved volume and the same
14-box pending frontier**, not merely the same leaf count.

| Accepted depth | Original rule | Optimized rule |
|---|---:|---:|
| 15 | 4 | 4 |
| 16 | 67 | 66 |
| 17 | 57 | 60 |
| 18 | 121 | 119 |

There are 243 identical accepted boxes and six different boxes on
each side. Two local refinements are balanced by two local
coarsenings. Thus this bounded prefix shows no net coverage
improvement. It does not establish how either rule performs on
the remaining domain. The elapsed times are not directly comparable:
the new run includes reading and validating the structure of the
large pinned partial record during setup.

## Provenance and validation

Record SHA256:
16e0ffe2e8b2ad6d33ecefbf34f1c6f01523d49102072d06ecf145ac20cec145

Proof:
[research_mixed_optimized_half_row_support.md](../../../notes/research_mixed_optimized_half_row_support.md),
SHA256 db82d176c074e92162ee59dca00605b03291c95600d70ee7da063baf7e8a0140.

Checker:
[certify_mixed_optimized_half_row_support.py](../../../experiments/certify_mixed_optimized_half_row_support.py),
SHA256 47c1b9e2cb546c0adf9e066dff112c54bdda68aa4c4473c6373986a2969cf9df.

The final audit reconstructed every accepted and pending dyadic
box, checked their total volume equals one, compared the two exact
frontiers and depth histograms, and verified all current hashes.
It did not rerun any numerical root or source certificate.
The old partial proof, checker and result remain unchanged.
