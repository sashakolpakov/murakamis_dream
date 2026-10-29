# Murakami’s Dream

Research notes, exact finite-matrix experiments, and audit results concerning Kashaev invariants, quantum A-polynomials, and hyperbolic volume.

**The general volume conjecture is not claimed solved.** The current notes contain a claimed full-sequence volume-equality proof for a specified long-pretzel family: every fixed odd width **s ≥ 9**, with independently sufficiently large **fixed signed** twist integers p_i and the recorded source convention R^(-(2p_i+1)). The corresponding specified single-cut reduced **two-component link** statement holds at fixed even widths **s ≥ 10**. Width and slopes remain fixed before N → ∞; both level parities and composite levels are included. These are research proofs and internal analytical audits, requiring external mathematical review.

The unfilled complete augmented volume V_s and the filled source volume V_src,s(p) are different. The broader task—original-source control and volume equality for arbitrary hyperbolic knots or arbitrary augmented graphs—remains open. Exploratory calculations, counterexamples to intermediate proposals, and historical checkpoints are retained with their own scope.

## Start here

- [Current general frontier](notes/general_equality_frontier.md)
- [Whole original-source survival](notes/actual_long_pretzel_full_source_survival.md)
- [Width and even-link extension](notes/actual_pretzel_all_width_extension.md)
- [Source-to-hyperbolic-volume certificate](notes/source_volume_casson_rivin_certificate.md)
- [Adversarial dependency audit](notes/actual_source_casson_rivin_dependency_audit.md)
- [General geometric completion and regulator theorem](notes/general_source_regulator_hyperbolic_equality.md)
- [Positive Newton metric for genuine turns](notes/actual_newton_turn_positive_gram.md)
- [Actual six-port divided-power source kernel](notes/actual_six_port_divided_power_source_kernel.md)
- [Historical research log](RESEARCH_LOG.md)

The proofs are in `notes/`. Scripts and recorded results are in `experiments/`. A finite audit checks stated identities or examples; it is not by itself a proof of an all-level asymptotic theorem. Some scripts are diagnostics or work in progress, rather than a single application test suite.

## Reproducing focused checks

Use Python 3. Research scripts use NumPy, SymPy, mpmath, and other packages as indicated by their imports. Exact interval, topology, and hyperbolic diagnostics may additionally require python-flint, Regina, SnapPy, Spherogram, or Sage. This snapshot does not bundle an environment or downloaded papers.

```sh
python3 -m pip install -r requirements-core.txt
python3 experiments/audit_actual_newton_turn_positive_gram.py
python3 experiments/audit_actual_six_port_divided_power_source_kernel.py
python3 experiments/audit_general_augmented_graph_source_extension.py
```

For each substantive result, read the note’s exact hypotheses and its linked audit before interpreting an output marked `PASS`.

## Publication snapshot

This is an isolated snapshot of the `volume-conjecture` research workspace, prepared on 29 October 2026. [PUBLICATION_MANIFEST.json](PUBLICATION_MANIFEST.json) records source-relative paths, hashes, transformations, and exclusions. Local absolute paths are made relative, one private-input context note is replaced by a stub, and the unpublished source manuscript is omitted.

Credentials, `.env` files, agent/session metadata, virtual environments, Python caches, downloaded/source PDFs, and private manuscript inputs are excluded. Publication does not change the mathematical working directory.
