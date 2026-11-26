#!/usr/bin/env python3
"""Bounded normalization diagnostics; no imported main or public output writes."""
import argparse
import json
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("finite-replay.json"))
    args = parser.parse_args()
    if not __debug__:
        raise RuntimeError("Assertions must be enabled")
    sys.path.insert(0, str(args.repo.resolve() / "experiments"))
    from audit_kashaev_crossing import audit, characteristic_zero_phase_check
    from audit_actual_complete_augmented_source_normalization import link_cases, peripheral_germ
    result = {
        "scope": "Bounded replay of independently constructed original weights and quantum matrices; not a proof of uniform identities. Imported mains not called, no public outputs written.",
        "crossing": [audit(n) for n in (2, 3, 4, 6, 9)],
        "characteristic_zero_inverse": characteristic_zero_phase_check(),
        "link_cuts": [row for n in (2, 3, 4, 6) for row in link_cases(n)],
        "whole_dimension_germs": [peripheral_germ(n) for n in (2, 3, 4, 6, 9, 12)],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print("5 crossing levels; 31 knot/link cuts; 6 meridian-germ levels; all checks completed")


if __name__ == "__main__":
    main()
