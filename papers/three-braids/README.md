# Volume limits for long alternating-generator three-braids

[Read the PDF](../../docs/papers/three-braids.pdf) · [TeX source](main.tex)

The 14-page draft fixes an even number of alternating braid generators,
at least six. Independently sufficiently long signed powers give the
all-level Kashaev volume limit when the strand permutation gives a knot.
The generators alternate; their crossing signs need not alternate.

The paper proves its diagram identification, marked packing formula,
three choices of coefficient weights and the estimates for every allowed
number of factors. Theorem 1 states the conclusion. Three numbered
companion statements retain the exact diagram evaluation, uniform local
coefficient estimates and nonzero geometric filling contribution. Their
proofs are explicitly located in the reference account. The finite
filling norm is cited as Theorem 1.1 of the separate Hermite-functional
paper. The draft does not present those substantial imported proofs as
if they were contained in its 14 pages.

From the repository root, build with
`python3 tools/build_papers.py three-braids`. Reproduce the rational
constant bounds with `python3 repro/check_cyclic_source_constants.py`.
The argument for every fixed even number of factors is written in the
paper; the script does not infer it from a finite sample of lengths.
