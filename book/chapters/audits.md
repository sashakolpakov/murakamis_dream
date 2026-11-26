# Reproducing the arguments and calculations

The papers contain written proofs, exact finite certificates and a
partial Lean formalization. Each has a different role. A rational
certificate can establish the inequality it encodes. A Lean proof
establishes its stated proposition. A numerical sample can expose an
incorrect formula, but cannot establish a uniform asymptotic estimate.
Building a PDF checks its presentation and references.

Start with the [collection-wide audit](../../repro/MANUSCRIPT_AND_LOGIC_AUDIT_2026-11-25.md)
and the [reproduction instructions](../../repro/README.md). The
[seven-paper Conway audit](../../repro/CONWAY_SERIES_AUDIT_2026-11-25.md)
records the earlier revision of the Conway theorem and its prerequisites.
The current subject papers give the detailed statements and proofs;
the reference supplies a unified account of overlapping material.

## Following the proof's dependencies

The [dependency graph](../../docs/papers/dependencies.html) records
named mathematical results and the places where later proofs use them.
An arrow runs from a prerequisite to its consumer. The detailed view
shows the source statement, its direct prerequisites and the reason for
each use. Selecting a result gives a reading route in which shared
prerequisites occur once.

The current inventory has 154 statement entries and 348 recorded uses,
organized into 16 components and 21 subject papers. The statement,
component and article graphs are acyclic. These are checks on the
recorded dependencies. An omitted premise would still be a mathematical
error even if the resulting graph were acyclic.

A separate proof-logic record distinguishes the original diagram class,
its knot-component test, its filling hypothesis and the conclusion to
which each argument applies. For example, evaluating a nonzero central
contribution is a different statement from bounding the rest of the
invariant. The latter premise cannot be removed from the final volume
argument. Replay that structural check with:

~~~sh
python3 repro/check_manuscript_logic.py --output repro/results/manuscript-and-lean/manuscript-logic
~~~

The current record checks 49 declared steps and rejects 23 deliberately
invalid substitutions. It detects errors in those recorded implications;
it does not turn their written analytic or geometric inputs into formal
proofs.

## Separating the strict Conway proof

The [Conway application](../../docs/papers/conway-asymptotics.pdf)
uses five companion papers directly and one further geometric
prerequisite. The [paper guide](../../papers/README.md#the-conway-paper-and-its-supporting-proofs)
lists that route. Its seven papers form a fixed, dated edition so that
their cited theorem numbers can be used together.

The standalone article and reference include the same Conway proof
files. The proof keeps the original coherent color contraction, uses the
pure auxiliary source, and restores each full signed crossing power by
its exact finite coefficients. The whole Fourier remainder estimate and
the nonzero leading coefficient are both needed. A local critical-point
calculation alone would supply neither conclusion.

After building the papers, check their actual inputs, compiled statement
labels, published PDFs and companion references with:

~~~sh
python3 tools/build_papers.py
python3 tools/build_dependency_graph.py
python3 tools/check_paper_collection.py
~~~

The [collection record](../../repro/results/paper-collection/summary.json)
covers all 21 current papers. Its source and PDF hashes describe the
edition checked. They identify files; they do not verify their proofs.

## Checking the implications in Lean

The [formal coverage guide](../../repro/PAPER_FORMAL_COVERAGE.md)
explains the relationship between the written arguments and the retained
Lean code. There are 76 selected manuscript statements in 28 modules.
For each one, a correspondence record states the symbol dictionary,
hypotheses, conclusion and any step that remains written.

The records distinguish four relationships. Fifteen are exact matches
with the cited abstract statement. Ten specialize a more general
formal theorem. Forty-one verify a specified component of a longer
proof. Ten prove a conditional implication whose application hypotheses
must be supplied by the written arguments. An exact scalar lemma still
needs a written application identifying its sequence with the knot
invariant.

Each selected statement has an independent expected-type contract: an
anonymous Lean example first spells out the proposition and then proves
it using the selected theorem. This catches a mismatch in hypotheses or
conclusions that checking only a theorem name would miss. The mathematical
interpretation of the symbols is also read against the manuscript;
Lean does not translate the prose automatically.

The formalization retains the full coefficient pairing, including its
Gram matrix and null directions. It checks the normalized shifted Fourier
transform, derivative data at repeated roots, and the finite crossing
coefficient bound. The stationary calculation uses an ordinary transpose
for a holomorphic Hessian. The scalar asymptotic argument keeps a strict
exponential gap for the entire remainder and permits the finite-level
action to vary with the level.

The final Conway implication assumes the written physical source
identity, contour estimates, nonzero limiting amplitude and marked
geometric action-volume comparison. Those are visible hypotheses. The
fixed-boundary variational modules likewise require the diagram's
written support and cut calculations before their generic balance
results apply.

Run the complete formal replay with:

~~~sh
python3 repro/check_lean.py --output repro/results/manuscript-and-lean/lean
~~~

The runner uses the pinned Lean and Mathlib versions, clears only local
generated build directories, and compiles the active modules and all 76
contracts. It also inventories all 534 public declarations and checks
their axiom dependencies. Admitted proofs and extra axioms are rejected.
The [formal setup](../../formal-real/README.md) gives the dependency
installation instructions for a fresh checkout.

Three compiler controls test substantive distinctions. Removing the
factor \(1/N\) from Parseval gives the wrong norm already for a constant
array at level two. Replacing the holomorphic mixed-block identity by a
conjugate-transpose identity fails over \(\mathbb C\). Replacing a strict
remainder gap by a nonstrict one permits complete cancellation of the
leading term. The valid control sources compile; the altered types are
rejected. These controls check the intended interfaces, rather than a
numerical volume limit.

## Exact certificates and finite checks

The [registered finite suite](../../repro/check_paper_algebra.py)
collects the checks needed by the current papers. It runs each program
in a separate process with assertions enabled and stops on a failure:

~~~sh
python3 repro/check_paper_algebra.py --output repro/results/paper-collection/finite
~~~

Its 20 groups include finite spectral and Newton identities, both parity
conventions, primitive peripheral coordinates and the rational constants
used by the stated volume families. Some groups invoke retained component
checks. The saved record identifies the scripts, data and manuscript
sources by their hashes.

The planar certificate verifiers use outward bounds and explicit series
remainders on a finite domain cover. The written argument explains why
those cells cover the required continuous region. In particular, a list
of sampled radii would not replace that cover. The Conway attachment
certificates are exact rational checks for their stated domains; their
analytic interpretation is proved in the source-bound paper.

The small certificate suite can also be run without the optional
scientific Python packages:

~~~sh
python3 repro/verify.py --output repro/results
~~~

Numerical matrix comparisons, Gaussian samples and selected-level tests
have a narrower purpose. They check formulas and conventions. They do not
prove analytic continuation, uniform error estimates, survival of a
geometric contribution or completion of a hyperbolic metric.

## Running a named group

The [research runner](../../repro/run_research_checks.py) is separate
from the publication suite. It groups the retained exploratory checks so
that one need not copy a long sequence of individual commands. Use its
help and group listing to select the desired calculation. A research
record describes its own scope; it is not another prerequisite for the
Conway theorem merely because it has been computed successfully.

## Rebuilding this guide and its figures

The guide is built from the retained chapter, figure and note sources:

~~~sh
python3 tools/build_book.py
python3 tools/check_book.py
~~~

The second command checks local links, fragments, image descriptions,
search coverage and rendered formulas. A typesetting or link check has no
mathematical proof content. After editing a native TikZ drawing, regenerate
its exports with `python3 tools/render_figures.py` before rebuilding the
guide. See the [guide source instructions](../../book/README.md) for the
required software.

Obsolete working notes, duplicated reports and failed diagnostic outputs
are absent from the maintained collection. Their source snapshot remains
in Git history. The current library contains the retained arguments and
research questions; it is not a second archive of every intermediate
calculation.
