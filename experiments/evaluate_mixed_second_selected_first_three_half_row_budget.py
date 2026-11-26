"""Alpha-zero metadata adapter for the unchanged original half-row arithmetic.

There is no numerical work on import or initialization.  The caller
supplies one certified original alpha-zero reference and its evaluator.
"""
from fractions import Fraction as F
import hashlib
import importlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FROZEN = "experiments/evaluate_mixed_second_selected_half_row_budget.py"
SPEC = "notes/research_mixed_second_selected_first_three_half_row_evaluation.md"
PINNED = {
    FROZEN: "ad5130b15bd3b403d4fdcc59ab97a73e536bdbff8e8e44be67d742cbe403f639",
    "notes/research_mixed_second_selected_half_row_evaluation.md":
        "4ed8584c2ee32c2f31d24a3e8b1dca73fc6edaff0fa2e078bfda9af6f6ca134f",
    "notes/research_mixed_second_selected_half_row_budget.md":
        "784c71292d450c201c1b591f977eec424f4ec92ee90d2bee4465ec47c2685788",
    "notes/research_mixed_second_selected_first_three_extension.md":
        "d488ff98e01cfd5cd077de664c7e3bee3bfeeb735009f8c78f7c0ac60c7ad0e2",
    SPEC: "8de75d8e7628977c48e2eab9a76b0a02bb3502b9b12247f64a0b683f6f801e75",
}
ALPHA = 0
_STATE = None


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(bindings):
    for name, expected in bindings.items():
        if sha(ROOT/name) != expected:
            raise ValueError("first-type-three half-row binding mismatch: "+name)


def initialize():
    """Verify metadata only; the preserved alpha-one label is reported explicitly."""
    global _STATE
    bindings = dict(PINNED)
    verify(bindings)
    frozen = importlib.import_module(Path(FROZEN).stem)
    if Path(frozen.__file__).resolve() != (ROOT/FROZEN).resolve():
        raise ValueError("unexpected frozen half-row module")
    metadata = frozen.initialize()
    if metadata.get("alpha") != 1 or metadata.get("beta_cases") != [0, 1]:
        raise ValueError("unexpected preserved half-row metadata")
    for name, expected in metadata["bindings"].items():
        if name in bindings and bindings[name] != expected:
            raise ValueError("conflicting half-row binding: "+name)
        bindings[name] = expected
    bindings[str(Path(__file__).resolve().relative_to(ROOT))] = sha(Path(__file__))
    verify(bindings)
    _STATE = {"bindings": bindings, "frozen": frozen}
    return {**metadata, "alpha": ALPHA, "bindings": dict(bindings),
            "frozen_calculation_label": {
                "provider": FROZEN, "provider_sha256": PINNED[FROZEN],
                "reported_alpha": metadata["alpha"],
                "meaning": "legacy arithmetic-helper label, not the supplied reference family"},
            "additional_reference_calls": 0, "additional_source_calls": 0}


def evaluate_reference(e, shapes, coordinates, beta, gap=F(1, 2000)):
    """Call the unchanged helper once on the caller's alpha-zero reference."""
    if _STATE is None:
        initialize()
    bindings, frozen = _STATE["bindings"], _STATE["frozen"]
    verify(bindings)
    try:
        original = frozen.evaluate_reference(e, shapes, coordinates, beta, gap)
    finally:
        verify(bindings)
    if original.get("alpha") != 1 or original.get("beta") != beta:
        raise ValueError("unexpected frozen half-row result labels")
    digest = hashlib.sha256(json.dumps(
        original, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    restore = {name: original[name] for name in ("alpha", "scope")}
    output = dict(original)
    output.update({
        "alpha": ALPHA,
        "scope": "upper bounds for the supplied original first-type-three stationary reference",
        "alpha_adapter": {
            "provider": FROZEN, "provider_sha256": PINNED[FROZEN],
            "frozen_reported_alpha": 1,
            "frozen_label_meaning": "legacy helper metadata, not the supplied reference family",
            "restore_original_metadata": restore,
            "remove_for_original_result": ["alpha_adapter"],
            "frozen_result_canonical_sha256": digest,
            "arithmetic_details_and_status_unchanged": True,
            "frozen_helper_calls": 1,
            "input_sha256": dict(bindings),
            "reference_existence_and_stationarity_are_caller_premises": True,
            "additional_primitive_calls": 0, "additional_conjugate_calls": 0,
            "additional_reference_calls": 0, "additional_response_calls": 0,
        },
    })
    return output
