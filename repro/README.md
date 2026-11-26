# Reproducing the retained results

The papers contain the proofs. This directory provides the finite
certificates, consistency checks and Lean compilation used alongside
them. Each check has a limited purpose: a rational certificate proves its
specified inequality, a compiler checks a formal implication, and a
sampled calculation tests a formula at its sampled inputs.

The [current audit](MANUSCRIPT_AND_LOGIC_AUDIT_2026-11-25.md) records the
manuscript corrections. The [formal coverage report](PAPER_FORMAL_COVERAGE.md)
explains exactly which statements Lean proves. The seven-paper Conway
edition has its own [exposition report](CONWAY_SERIES_AUDIT_2026-11-25.md).
Superseded reviews and failed diagnostic runs have been removed from the
working collection; their sources are preserved in Git history.

## Checking the papers

Run these commands from the repository root.

| Purpose | Command |
| --- | --- |
| Build the 21 current papers | `python3 tools/build_papers.py` |
| Build the reference manuscript | `python3 tools/build_manuscript.py` |
| Rebuild the statement dependency graph | `python3 tools/build_dependency_graph.py` |
| Check sources, compiled statement exports and published PDFs | `python3 tools/check_paper_collection.py` |
| Run all 20 registered finite algebra and certificate groups | `python3 repro/check_paper_algebra.py --output repro/results/paper-collection/finite` |
| Replay the three elementary Conway certificates | `python3 repro/verify.py --output repro/results` |
| Check the declared logical dependency map | `python3 repro/check_manuscript_logic.py --output repro/results/manuscript-and-lean/manuscript-logic` |
| Compile the retained Lean proofs and statement contracts | `python3 repro/check_lean.py --output repro/results/manuscript-and-lean/lean` |

The document builds require a TeX installation. The paper algebra suite
uses SymPy, python-flint, NumPy and mpmath; see
[requirements-core.txt](../requirements-core.txt). The three-certificate
replay and dependency-map checker need only Python's standard library.
The [Std](../formal/README.md) and [Mathlib](../formal-real/README.md)
instructions describe the pinned Lean environment.

The finite suite saves each program's output and stops on failure. Its
record identifies the scripts, certificates and manuscript sources by
hash. The checks include parity endpoints, repeated-root derivatives,
peripheral conventions and the rational constants used by the retained
families. A finite sample does not establish a uniform contour estimate
or a complete hyperbolic metric.

The dependency checker validates 49 declared proof steps and rejects
23 deliberately invalid substitutions. It checks the recorded uses of
written proofs; it does not prove their mathematical assertions. For
reading order, use the [statement graph](../docs/papers/dependencies.html).

The Lean runner compiles 28 modules from empty local build directories,
checks all public declarations for additional axioms or admitted proofs,
and compiles 76 independently stated expected-type contracts. Their
symbol dictionaries distinguish exact matches, specializations,
components of written proofs and conditional applications. Three compiler
controls test incorrect changes to Fourier normalization, the
holomorphic transpose and the strict remainder gap. Contour estimates,
physical knot-source identifications and geometric completion retain
written proofs.

## Research calculations

The remaining exploratory calculations support the
[finite-exception research](../notes/research_finite_exceptions_progress.md)
and the conceptual approaches explained in the illustrated guide. They
are separate from the frozen paper checks. A successful exploratory run
is not a new volume theorem.

The research runner lists its retained groups without executing them:

```sh
python3 repro/run_research_checks.py --list
```

Choose a group by its stated scope. Do not treat an old output file as
current evidence without checking its inputs and the associated written
argument. Useful counterexamples are retained because they rule out
incorrect proof steps; obsolete parameter pilots and superseded outputs
are not maintained.

## The illustrated guide

After changing guide sources or the retained note collection, rebuild
and check the site:

```sh
python3 tools/build_book.py
python3 tools/check_book.py
```

The builder removes generated note pages whose source has been deleted.
The checker examines local links, section anchors, image descriptions,
rendered formulas and agreement between the note collection and search
index. These checks concern the exposition, not its mathematical truth.

Current compilation and check records are linked from the
[combined verification record](results/manuscript-and-lean/verification-summary.json).
The [publication plan](HEXAGON_PUBLICATION_PLAN_2026-11-25.md) concerns
submission preparation; it is separate from mathematical verification.
