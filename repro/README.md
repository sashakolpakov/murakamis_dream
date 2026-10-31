# Reproducing the Conway composition manuscript

The exact certificate suite requires Python 3.10 or newer and only its
standard library. Run these commands from the repository root:

```sh
python3 repro/verify.py --list
python3 repro/verify.py --plan
python3 repro/verify.py --output repro/results
```

The first two commands describe the work without running it. The last
command executes the checks serially, writes fresh records, and compares
them with the committed exact records. It does not overwrite those
reference records. Without `--output`, temporary results are removed when
the run finishes. Each verifier runs with Python's isolated mode, so
environment options cannot disable its assertions.

| Check | What is checked |
| --- | --- |
| Two-leaf block | 16 slope intervals and 288 exact corner/vertex comparisons for the two possible alias types |
| Single-leaf attachment | 55 dyadic rectangles and 880 exact corner/vertex comparisons over the entire slope square |
| Single-leaf endpoint | Four exact vertex comparisons used with the monotone-response argument |
| Elementary endpoints | The rational lower bounds for the large-cotangent leaf estimate and the isolated three-leaf case |

The interval engine bounds sine, logarithm, pi and the integrated
log-sine function using explicit rational remainder estimates. It does
not invoke a numerical optimizer or infer a continuum inequality from
sampling. The manuscript explains why concavity and affine dependence
reduce the required inequalities to these finite certificates.

The suite verifies the finite arithmetic in those arguments. Its output
does not mechanically verify the entire paper. In particular, the
original-invariant normalization, ordered geometric gluing, complex
interpolation estimates and filling-period argument require the written
proofs. The [proof-input map](PROOF_INPUTS.md) identifies their sources.

The manuscript and documentation build instructions are supplied with
the [manuscript sources](../manuscript/README.md). Documentation builds
do not launch the certificate suite. Python dependencies for Sphinx are
kept separate from the standard-library proof checks.

For a clean illustrated documentation build, install TeX Live or MacTeX
with `latexmk`, `pdflatex`, and the `standalone`/TikZ packages; Ghostscript
(`gs`) for the PNG figure previews; Pandoc for the Markdown book; and
the Sphinx version in `requirements-docs.txt`. The certificate runner
itself requires only Python 3.10 or later.
