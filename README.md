# Murakami’s Dream

Research notes, exact finite-matrix experiments, and audit results concerning Kashaev invariants, quantum A-polynomials, and hyperbolic volume.

**The general volume conjecture is not claimed solved.** The current notes contain a claimed full-sequence volume-equality proof for a specified long-pretzel family: every fixed odd width **s ≥ 9**, with independently sufficiently large **fixed signed** twist integers p_i and the recorded source convention R^(-(2p_i+1)). The corresponding specified single-cut reduced **two-component link** statement holds at fixed even widths **s ≥ 10**. Width and slopes remain fixed before N → ∞; both level parities and composite levels are included. These are research proofs and internal analytical audits, requiring external mathematical review.

A second verified research result concerns **complete augmented links**: every fixed balanced word of **2k octahedral belt pieces**, k ≥ 1, gives a **2k+3-component** link with original all-level volume limit **4k v₈**, equal to its explicitly constructed complete hyperbolic volume. The proof retains one physical belt and uses exact cyclotomic Chebyshev sampling. Possible coverage by the earlier Whitehead-chain literature is recorded; no novelty of this topological family is claimed. Fixed fillings of these new bases are not established here.

The unfilled complete augmented volume V_s and the filled source volume V_src,s(p) are different. The broader task—original-source control and volume equality for arbitrary hyperbolic knots or arbitrary augmented graphs—remains open. Exploratory calculations, counterexamples to intermediate proposals, and historical checkpoints are retained with their own scope.

## Start here

- [Current general frontier](notes/general_equality_frontier.md)
- [Whole original-source survival](notes/actual_long_pretzel_full_source_survival.md)
- [Width and even-link extension](notes/actual_pretzel_all_width_extension.md)
- [Source-to-hyperbolic-volume certificate](notes/source_volume_casson_rivin_certificate.md)
- [Adversarial dependency audit](notes/actual_source_casson_rivin_dependency_audit.md)
- [General geometric completion and regulator theorem](notes/general_source_regulator_hyperbolic_equality.md)
- [Positive Newton metric for genuine turns](notes/actual_newton_turn_positive_gram.md)
- [Literal reflected two-circle base and its two-octahedron geometry](notes/actual_reflected_two_circle_octahedral_base.md)
- [Bandlimited cyclotomic sampling and complete-belt energy](notes/actual_complete_circle_nodal_energy_and_belt_sewing.md)
- [Balanced octahedral belt stacks: source and volume](notes/actual_balanced_octahedral_belt_stack_volume.md)
- [Finite real-algebraic geometric certificate](notes/finite_real_algebraic_geometric_certificate.md)
- [Coherent turn reductions](notes/actual_newton_coherent_turn_reduction.md)
- [Two-twist interaction packet](notes/actual_newton_two_twist_interaction_packet.md)
- [Run endpoint vectors and universal fixed-run mode test](notes/actual_newton_run_endpoint_vectors.md)
- [Actual Gaussian twist endpoints](notes/actual_twist_endpoint_gaussian_certificate.md)
- [Rank-three coherent folded packet](notes/actual_newton_rank_three_folded_packet.md)
- [Backward dominant-source certificate](notes/actual_backward_cubic_dominant_source_certificate.md)
- [Exact Newton kernel and canonical graph](notes/actual_newton_twist_canonical_graph.md)
- [What algebraic source/geometry criteria certify](notes/algebraic_source_geometry_criteria_audit.md)
- [Actual six-port divided-power source kernel](notes/actual_six_port_divided_power_source_kernel.md)
- [Historical research log](RESEARCH_LOG.md)

Root-level Casimir Hermite data are distinguished from actual generic-q normal deformations. A formal generic-Q continuation of a root scalar recurrence is not automatically the original generic-q source germ; the linked notes retain the required Cartan factors, turn families, and normal currents.

The proofs are in `notes/`. Scripts and recorded results are in `experiments/`. A finite audit checks stated identities or examples; it is not by itself a proof of an all-level asymptotic theorem. Some scripts are diagnostics or work in progress, rather than a single application test suite.

## Reproducing focused checks

Use Python 3. Research scripts use NumPy, SymPy, mpmath, and other packages as indicated by their imports. Exact interval, topology, and hyperbolic diagnostics may additionally require python-flint, Regina, SnapPy, Spherogram, or Sage. This snapshot does not bundle an environment or downloaded papers.

```sh
python3 -m pip install -r requirements-core.txt
python3 experiments/audit_actual_newton_turn_positive_gram.py
python3 experiments/audit_actual_six_port_divided_power_source_kernel.py
python3 experiments/audit_general_augmented_graph_source_extension.py
python3 experiments/audit_actual_complete_circle_nodal_energy_and_belt_sewing.py
python3 experiments/audit_actual_balanced_octahedral_belt_stack_volume.py
```

With the optional geometry packages installed, the belt-stack script also supports `--software-only` for its separately labeled literal-diagram diagnostics. The exact geometric proof is the reversible disk/face/cusp certificate in the notes, rather than software recognition.

For each substantive result, read the note’s exact hypotheses and its linked audit before interpreting an output marked `PASS`.

## Publication snapshot

This is an isolated snapshot of the `volume-conjecture` research workspace, prepared on 29 October 2026. [PUBLICATION_MANIFEST.json](PUBLICATION_MANIFEST.json) records source-relative paths, hashes, transformations, and exclusions. Local absolute paths are made relative, one private-input context note is replaced by a stub, and the unpublished source manuscript is omitted.

Credentials, `.env` files, agent/session metadata, virtual environments, Python caches, downloaded/source PDFs, and private manuscript inputs are excluded. Publication does not change the mathematical working directory.
