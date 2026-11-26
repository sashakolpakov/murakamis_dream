#!/usr/bin/env python3
"""Validate a saved exact partition for resumption, without replaying its inequalities."""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from replay_pair_height_sector import verify_cover


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkpoint", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    digest = hashlib.sha256()
    decoder = json.JSONDecoder()
    rows = []
    with args.checkpoint.open("rb") as source:
        def chunk():
            data = source.read(65536)
            digest.update(data)
            return data.decode("utf-8")

        buffer = chunk()
        marker = ',"certificate":['
        while marker not in buffer:
            part = chunk()
            assert part, "Missing certificate array"
            buffer += part
        prefix, buffer = buffer.split(marker, 1)
        header = json.loads(prefix + "}")
        assert header["status"] == "incomplete"
        assert header["mode"] in ("scaled", "affine")
        assert header["precision_bits"] == 100
        for filename, expected in header["sha256"].items():
            assert hashlib.sha256((root / filename).read_bytes()).hexdigest() == expected
        while True:
            buffer = buffer.lstrip()
            if not buffer:
                buffer = chunk()
                assert buffer, "Truncated certificate array"
            if buffer.startswith("]"):
                buffer = buffer[1:]
                break
            while True:
                try:
                    row, end = decoder.raw_decode(buffer)
                    break
                except json.JSONDecodeError:
                    part = chunk()
                    assert part, "Truncated certificate item"
                    buffer += part
            rows.append({"box": row["box"]})
            buffer = buffer[end:].lstrip()
            while not buffer:
                buffer = chunk()
                assert buffer, "Truncated certificate separator"
            if buffer.startswith(","):
                buffer = buffer[1:].lstrip()
                while not buffer:
                    buffer = chunk()
                    assert buffer, "Truncated certificate item"
                    buffer = buffer.lstrip()
                assert not buffer.startswith("]"), "Trailing comma in certificate array"
            else:
                assert buffer.startswith("]"), "Invalid certificate separator"
        while part := chunk():
            buffer += part
        assert buffer.strip() == "}", "Trailing or truncated JSON"
    assert len(rows) == header["accepted_boxes"]
    assert header["pending"], "A completed certificate requires analytic replay"
    all_rows = rows + [{"box": box} for box in header["pending"]]
    low = Fraction(3, 100) if header["mode"] == "scaled" else Fraction(37, 40)
    high = Fraction(23, 20)
    assert header["domain"] == {"sector_coordinate": ["0", "1"],
                                "height": [str(low), str(high)]}
    cover = verify_cover(all_rows, low, high)
    result = {
        "status": "valid_for_resume",
        "scope": "Frozen hashes, complete JSON, accepted count and exact accepted-plus-pending partition; not an analytic replay.",
        "checkpoint_sha256": digest.hexdigest(),
        "accepted_boxes": header["accepted_boxes"],
        "visited_boxes": header["visited_boxes"],
        "pending_boxes": len(header["pending"]),
        "prior_elapsed_seconds": header["elapsed_seconds"],
        "coverage": cover,
        "frozen_input_sha256": header["sha256"],
        "validator_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "cover_checker_sha256": hashlib.sha256((root / "experiments/replay_pair_height_sector.py").read_bytes()).hexdigest(),
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
