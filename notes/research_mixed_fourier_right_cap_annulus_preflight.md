# Preflight record for the correlated endpoint annulus test

7 November 2026. This record precedes the sole prescribed execution.
The result is not known at the time of this record.

The fixed proof and protocol are
[research_mixed_fourier_right_cap_annulus_protocol.md](research_mixed_fourier_right_cap_annulus_protocol.md),
SHA-256 `3069c8412a7a9b58e0c55597462d437394be15030ebf239f77e81f198b8d2e90`.
The final checker is
[check_mixed_fourier_right_cap_annulus.py](../experiments/check_mixed_fourier_right_cap_annulus.py),
SHA-256 `39337ada17af9122286050c4bcc9b04edc4707983072ce8ee56d1bbda01f316d`.

The root and terminal reviewer completed full proof, source and code
reads before execution. These reads cover the connected actual-family
argument, all nineteen necessary filters, cleared rational equations,
denominator exclusions, degree-fourteen Bernstein conversion, full
closed-circle coverage, and the inherited full-square parameter bound.
They also cover the exclusive output, preserved failure operands,
partial-record handling, and unchanged-input checks. The author
completed the same preflight. The final changes to the checker only
preserve failure evidence; no arithmetic or inventory was changed.

The initial root static inspection verified all twenty-six inherited
and direct input bindings, in-memory syntax, and absence of the output.
The final script hash above replaces the earlier evidence-handling
revision. No checker has been run during these reviews. One preliminary
root attempt to parse the static pin dictionary with `ast.literal_eval`
failed on its named constant keys; a corrected static reader resolved
those keys. This did not import the checker, construct a bound, or
create an output.

The prescribed output is exclusively created at
`repro/results/research-mixed-fourier-right-cap-annulus.json.gz`.
The complete inventory is eight charts, 512 cells, 9,728 polynomial
upper bounds and 145,920 Bernstein coefficient intervals. It uses
only rational interval arithmetic on the saved parameter enclosure.
No analytic function, root, source gain or proposal is evaluated.

Only the root executes the checker. There is no subdivision, changed
filter, alternate input, refinement, or retry after seeing its result.
Every nonexcluded cell makes this sufficient test inconclusive. Even a
successful result establishes only the actual auxiliary-domain
containment; the finite right-cap allocation and remainder bounds stay
separate.
