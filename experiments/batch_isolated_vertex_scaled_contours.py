#!/usr/bin/env python3
"""Run the unchanged isolated-vertex certificate on finite degree ranges.

Each pair receives its own deterministic gzip certificate. The manifest
lists the exact tested parameter set; it never substitutes sampling for
the missing pairs. Existing certificates are reused only if every proof
engine hash and the fixed wire interval agree.
"""

import argparse
import contextlib
import gzip
import hashlib
import io
import json
import multiprocessing
import time
import traceback
from concurrent.futures import ProcessPoolExecutor, as_completed
from fractions import Fraction
from pathlib import Path

import certify_isolated_vertex_scaled_contours as verifier


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def atomic_bytes(path, data):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_bytes(data)
    temporary.replace(path)


def certify_one(request):
    degree, power, precision, directory, metadata = request
    directory = Path(directory)
    path = directory / f"d{degree:03d}-n{power:02d}.json.gz"
    captured = io.StringIO()
    pair_started = time.perf_counter()
    try:
        reused = False
        report = None
        if path.exists():
            existing = json.loads(gzip.decompress(path.read_bytes()))
            if (existing.get("status") != "certified"
                    or any(existing.get(k) != v for k, v in metadata.items())
                    or existing["result"]["degree"] != degree
                    or existing["result"]["power"] != power):
                raise RuntimeError(f"Existing certificate has incompatible metadata: {path}")
            if existing["requested_precision_bits"] >= precision:
                report = existing
                reused = True
        if report is None:
            with contextlib.redirect_stdout(captured):
                result = verifier.certify_pair(degree, power, precision,
                                               Fraction(1, 128))
            report = {
                "status": "certified", **metadata,
                "requested_precision_bits": precision,
                "elapsed_seconds": time.perf_counter() - pair_started,
                "result": result,
            }
            encoded = json.dumps(report, separators=(",", ":")).encode()
            atomic_bytes(path, gzip.compress(encoded, compresslevel=9, mtime=0))
        result = report["result"]
        assert len(result["surfaces"]) == 19
        return {
            "status": "certified",
            "degree": degree, "power": power,
            "certificate": str(path),
            "certificate_sha256": digest(path),
            "reused": reused,
            "actual_requested_precision_bits": report["requested_precision_bits"],
            "surface_count": len(result["surfaces"]),
            "visited_boxes": sum(s["counts"]["visited"] for s in result["surfaces"]),
            "selected_rate": result["selected_rate"],
            "wire_tail_gap": result["wire_tail_gap"],
            "elapsed_seconds": report["elapsed_seconds"],
        }
    except Exception:
        failure = {
            "status": "failed", **metadata,
            "degree": degree, "power": power,
            "requested_precision_bits": precision,
            "elapsed_seconds": time.perf_counter() - pair_started,
            "traceback": traceback.format_exc(),
            "completed_surface_log": captured.getvalue(),
        }
        failure_path = directory / f"d{degree:03d}-n{power:02d}.failure.json"
        atomic_bytes(failure_path, (json.dumps(failure, indent=2) + "\n").encode())
        return {
            "status": "failed", "degree": degree, "power": power,
            "failure_report": str(failure_path),
            "elapsed_seconds": failure["elapsed_seconds"],
        }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--degrees", type=int, nargs=2, required=True,
                        metavar=("FIRST", "LAST"))
    parser.add_argument("--precision", type=int, default=180)
    parser.add_argument("--workers", type=int, choices=(1, 2, 3), default=2)
    parser.add_argument("--report-directory", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()
    first, last = args.degrees
    if not 3 <= first <= last <= 127 or args.precision < 140:
        parser.error("Require 3<=FIRST<=LAST<=127 and precision>=140.")
    # d>=128 satisfies the criterion using d alone. For n>=64,
    # d*d+n*n>=4096>=1024 and d*d+n*n-128*d
    # >=(d-64)**2>=0. Thus this independently enumerated rectangle
    # contains every uncovered pair in the infinite positive lattice.
    all_pairs = [(d, n) for d in range(3, 128)
                 for n in range(1, 128)
                 if d*d + n*n < max(1024, 128*d)]
    assert len(all_pairs) == len(set(all_pairs)) == 6369
    assert max(n for d, n in all_pairs) == 63
    pairs = [(d, n) for d, n in all_pairs if first <= d <= last]
    assert len(pairs) == len(set(pairs))
    metadata = {
        "verifier_sha256": digest(verifier.__file__),
        "degree_two_engine_sha256": digest(verifier.c.__file__),
        "primitive_engine_sha256": digest(verifier.e.__file__),
        "wire_interval": ["1/128", "63/128"],
    }
    args.report_directory.mkdir(parents=True, exist_ok=True)
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest = {
        "scope": "Complete outward certificates for the listed finite parameter set only.",
        "status": "running",
        "batch_script_sha256": digest(__file__),
        **metadata,
        "degree_range": [first, last],
        "parameter_rule": "d>=3,n>=1,d*d+n*n<max(1024,128*d)",
        "expected_pair_count": len(pairs),
        "full_uncovered_pair_count": len(all_pairs),
        "requested_precision_bits": args.precision,
        "workers": args.workers,
        "pairs": [],
        "failures": [],
    }
    started = time.perf_counter()

    def save():
        manifest["elapsed_seconds"] = time.perf_counter() - started
        atomic_bytes(args.manifest,
                     (json.dumps(manifest, indent=2) + "\n").encode())

    save()
    requests = [(d, n, args.precision, str(args.report_directory), metadata)
                for d, n in pairs]
    try:
        with ProcessPoolExecutor(
                max_workers=args.workers,
                mp_context=multiprocessing.get_context("spawn")) as executor:
            futures = [executor.submit(certify_one, request) for request in requests]
            for index, future in enumerate(as_completed(futures), 1):
                item = future.result()
                manifest["pairs" if item["status"] == "certified"
                         else "failures"].append(item)
                if index % 25 == 0 or item["status"] == "failed" or index == len(pairs):
                    print(f"Completed {index}/{len(pairs)}; "
                          f"certified={len(manifest['pairs'])}, "
                          f"failed={len(manifest['failures'])}; "
                          f"last=({item['degree']},{item['power']}); "
                          f"elapsed={time.perf_counter()-started:.1f}s",
                          flush=True)
                    save()
    except BaseException:
        manifest["status"] = "interrupted"
        manifest["orchestration_error"] = traceback.format_exc()
        save()
        raise
    manifest["pairs"].sort(key=lambda item: (item["degree"], item["power"]))
    manifest["failures"].sort(key=lambda item: (item["degree"], item["power"]))
    manifest["status"] = "certified" if not manifest["failures"] else "incomplete"
    observed = [(item["degree"], item["power"])
                for key in ("pairs", "failures") for item in manifest[key]]
    assert len(observed) == len(set(observed))
    assert set(observed) == set(pairs)
    save()
    print(f"Final status: {manifest['status']}; "
          f"{len(manifest['pairs'])}/{len(pairs)} pairs certified.", flush=True)


if __name__ == "__main__":
    main()
