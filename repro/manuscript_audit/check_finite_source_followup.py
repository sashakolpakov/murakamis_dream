#!/usr/bin/env python3
"""Replay hashes and links for a bounded audit record, not its mathematics."""

import hashlib
import json
from pathlib import Path
import re
import subprocess


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    if not __debug__:
        raise RuntimeError("Run with assertions enabled.")
    here = Path(__file__).resolve().parent
    root = here.parent.parent
    snapshot = json.loads(
        (here / "finite-source-and-filling-followup-snapshot.json").read_text()
    )
    report = here / "finite-source-and-filling-followup.md"
    assert digest(report.read_bytes()) == snapshot["curated_report"]["sha256"]
    assert digest(Path(__file__).read_bytes()) == snapshot["replay_script_sha256"]
    for item in snapshot["historical_records"]:
        assert digest(item["content"].encode()) == item["sha256"], item["name"]
    for item in snapshot["audited_source_versions"]:
        if item["storage"] == "git":
            data = subprocess.check_output(
                ["git", "show", snapshot["baseline_commit"] + ":" + item["path"]],
                cwd=root,
            )
        else:
            assert item["storage"] == "embedded"
            data = item["content"].encode()
        assert digest(data) == item["sha256"], item["path"]
    for item in snapshot["integration_sources"]:
        data = subprocess.check_output(
            ["git", "show", snapshot["integration_commit"] + ":" + item["path"]],
            cwd=root,
        )
        assert digest(data) == item["sha256"], item["path"]
    links = re.findall(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", report.read_text())
    checked = 0
    for link in links:
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", link):
            continue
        target = link.split("#", 1)[0]
        if not target:
            continue
        assert (here / target).resolve().is_file(), link
        checked += 1
    print(json.dumps({
        "baseline_commit": snapshot["baseline_commit"],
        "integration_commit": snapshot["integration_commit"],
        "historical_records": len(snapshot["historical_records"]),
        "audited_source_versions": len(snapshot["audited_source_versions"]),
        "integration_sources": len(snapshot["integration_sources"]),
        "relative_links": checked,
        "scope": "Hash and link consistency only; no mathematical proof replay.",
    }, indent=2))


if __name__ == "__main__":
    main()
