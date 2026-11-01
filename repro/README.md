# Reproducing the calculations

The manuscript proves inequalities on continuous regions of state variables. Some of those inequalities are reduced, by concavity and supporting tangent planes, to a finite set of rational comparisons. This directory provides the scripts and reference records for those comparisons. The quantitative circle-tree theorem also has a group of symbolic, geometric and finite numerical checks, described below.

## Run the checks

The exact verifiers require Python 3.10 or later and only its standard library. From the repository root, run:

```sh
python3 repro/verify.py --list
python3 repro/verify.py --plan
python3 repro/verify.py --output repro/results
```

The first command lists the checks. The second prints the execution plan without running them. The third executes the checks serially, writes fresh result records to `repro/results`, and compares them with the committed exact reference records. It does not overwrite those references. Without `--output`, the runner uses temporary results and removes them when it finishes.

Each verifier runs in Python's isolated mode. This prevents environment options from silently disabling the assertions on which the check depends. A successful run means that every required comparison and reference-record comparison passed; a failure should be investigated rather than accepted as a new reference result.

## What is being verified

A *leaf* is one basic two-strand twist piece in the manuscript's tangle construction. A *block* joins such pieces. The finite invariant has signed terms outside its selected central contribution; the proof calls those terms *aliases*. The certificates show that their upper bounds are strictly smaller than the relevant central value, throughout the specified parameter regions.

| Check | Mathematical role and finite work |
| --- | --- |
| Two-leaf block | Controls the two possible alias types in a two-piece block, using 16 slope intervals and 288 exact corner/vertex comparisons. |
| Single-leaf attachment | Controls an additional piece attached to a constructed box, using 55 dyadic rectangles and 880 exact comparisons over the full two-parameter slope square. |
| Single-leaf endpoint | Checks four exact vertex comparisons used with the monotone-response argument at the endpoint. |
| Elementary endpoints | Checks rational lower bounds used for the large-cotangent leaf estimate and the isolated three-piece closure. |

Here a *slope* is a derivative of an entropy function used in the source estimate. It is not a Dehn-filling slope. The interval engine bounds sine, logarithm, pi and the integrated log-sine function by rational series with explicit remainder estimates. It does not infer a continuum inequality from samples or call a numerical optimizer to certify a maximum.

The written proof explains why concavity and affine parameter dependence reduce the continuum statement to these finite comparisons. The [proof-input map](PROOF_INPUTS.md) identifies those arguments and the exact records used by the runner.

## The quantitative circle-tree theorem

Run its three programs with one command:

```sh
python3 repro/run_research_checks.py curvature-fillings
```

This group requires Python, SymPy and mpmath. It checks four edge-action
identities and 990 finite complex Gaussian samples; 46 rational
octahedral identities and seven bounds; and 128 ordered trees with
448 local attachments and 28 additional algebraic identities. The
programs retain both half-twist signs and the original peripheral
curves. Results record the exact source hashes.

The [proof-input map](PROOF_INPUTS.md#the-quantitative-circle-tree-theorem)
locates the uniform estimates, arbitrary-tree induction and geometric
completion. The finite tree examples check the attachment code against
the original strand compiler; the induction proves the general case.
The numerical Gaussian samples check formulas, while the written
bounds control the whole complex domain.

## What a passing run does not replace

The suite verifies the finite arithmetic in the source bounds. It does not mechanically verify the whole manuscript. In particular, the invariant normalization, the ordered tangle identities, the geometric gluing, the complex interpolation estimates and the filling-period argument require their written proofs. A passing result should not be reported as a computer proof of the volume conjecture for arbitrary knots.

## Build the paper and documentation

The [manuscript source guide](../manuscript/README.md) gives the paper and figure build commands. Documentation builds are separate from the proof checks and do not launch this suite.

The paper and figure builds require TeX Live or MacTeX with `latexmk`, `pdflatex`, TikZ and `standalone`, plus Ghostscript (`gs`) for PNG previews. The guide requires Pandoc. Its builder uses Python's standard library and produces native MathML, with no separate documentation framework.

Then, from the repository root:

```sh
python3 tools/build_manuscript.py
python3 tools/build_book.py
python3 tools/check_book.py
```

The certificate runner itself still requires only Python's standard library. Keeping rendering and verification separate makes a failed build distinguishable from a failed mathematical certificate.
