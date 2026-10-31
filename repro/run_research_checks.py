#!/usr/bin/env python3
"""Run explicitly selected research-check groups, serially, with saved logs.

This is an orchestration tool. A successful process exit does not establish
any mathematical statement beyond the scope of the individual check.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import shlex
import subprocess
import sys
import tempfile
import time


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = Path(__file__).with_name("research_check_groups.json")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_groups(path: Path) -> dict[str, dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != 1 or not isinstance(data.get("groups"), list):
        raise ValueError("expected schema_version 1 and a groups list")
    groups = {}
    for item in data["groups"]:
        if not isinstance(item, dict):
            raise ValueError("each group must be a JSON object")
        name = item.get("name", "")
        commands = item.get("commands")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            raise ValueError(f"invalid group name: {name!r}")
        if name in groups or not isinstance(commands, list) or not commands:
            raise ValueError(f"duplicate or empty group: {name}")
        for command in commands:
            if (
                not isinstance(command, list)
                or len(command) < 2
                or command[0] != "python3"
                or not all(isinstance(arg, str) for arg in command)
            ):
                raise ValueError(f"{name}: expected ['python3', 'path.py', ...]")
            script = (ROOT / command[1]).resolve()
            if not script.is_relative_to(ROOT) or script.suffix != ".py":
                raise ValueError(f"{name}: script must be a Python file in the repository")
            if not script.is_file():
                raise ValueError(f"{name}: script not found: {command[1]}")
        groups[name] = item
    return groups


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("groups", nargs="*", help="explicit group names, in run order")
    parser.add_argument("--list", action="store_true", help="list groups without running them")
    parser.add_argument("--dry-run", action="store_true", help="print selected commands only")
    parser.add_argument("--python", default=sys.executable, help="Python interpreter for checks")
    parser.add_argument("--log-dir", type=Path, help="new or empty directory for logs")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST, help="group manifest")
    args = parser.parse_args(argv)
    try:
        groups = read_groups(args.manifest)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        parser.error(f"cannot read group manifest: {exc}")

    if args.list:
        for name, item in groups.items():
            print(f"{name} ({len(item['commands'])} checks)")
            print(f"  {item.get('description', '')}")
        return 0
    if not args.groups:
        parser.error("select at least one group, or use --list")
    selected = list(dict.fromkeys(args.groups))
    unknown = [name for name in selected if name not in groups]
    if unknown:
        parser.error("unknown group(s): " + ", ".join(unknown))

    jobs = []
    for name in selected:
        for original in groups[name]["commands"]:
            command = [args.python, str((ROOT / original[1]).resolve()), *original[2:]]
            jobs.append((name, original, command))
    if args.dry_run:
        print(f"Repository: {ROOT}")
        for number, (name, original, _) in enumerate(jobs, 1):
            display = [args.python, *original[1:]]
            print(f"{number:03d} [{name}] {shlex.join(display)}")
        print(f"{len(jobs)} checks selected; no commands executed and no logs created.")
        return 0

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    log_dir = args.log_dir or Path(tempfile.gettempdir()) / "murakamis-research-checks" / stamp
    log_dir = log_dir.resolve()
    try:
        if log_dir.exists() and (not log_dir.is_dir() or any(log_dir.iterdir())):
            parser.error(f"log directory must be new or empty: {log_dir}")
        log_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        parser.error(f"cannot create log directory: {exc}")

    summary = {
        "schema_version": 1,
        "manifest": str(args.manifest.resolve()),
        "repository": str(ROOT),
        "selected_groups": selected,
        "started_utc": utc_now(),
        "planned_checks": len(jobs),
        "results": [],
    }
    summary_path = log_dir / "summary.json"

    def save_summary() -> None:
        summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    save_summary()
    interrupted = False
    for number, (name, original, command) in enumerate(jobs, 1):
        log_path = log_dir / f"{number:03d}-{name}-{Path(original[1]).stem}.log"
        print(f"[{number}/{len(jobs)}] {name}: {original[1]}", flush=True)
        start = time.monotonic()
        started = utc_now()
        with log_path.open("w", encoding="utf-8") as output:
            output.write(f"Started: {started}\nDirectory: {ROOT}\n")
            output.write("Command: " + shlex.join(command) + "\n\n")
            output.flush()
            try:
                completed = subprocess.run(
                    command, cwd=ROOT, stdout=output, stderr=subprocess.STDOUT, check=False
                )
                returncode = completed.returncode
            except OSError as exc:
                output.write(f"\nCould not start command: {exc}\n")
                returncode = 127
            except KeyboardInterrupt:
                output.write("\nInterrupted by user.\n")
                returncode = 130
                interrupted = True
        record = {
            "group": name,
            "original_command": original,
            "command": command,
            "started_utc": started,
            "finished_utc": utc_now(),
            "duration_seconds": round(time.monotonic() - start, 6),
            "returncode": returncode,
            "log": str(log_path),
        }
        summary["results"].append(record)
        save_summary()
        print(f"  exit {returncode}; log: {log_path}", flush=True)
        if interrupted:
            break

    failed = [item for item in summary["results"] if item["returncode"] != 0]
    summary["finished_utc"] = utc_now()
    summary["completed_checks"] = len(summary["results"])
    summary["failed_checks"] = len(failed)
    summary["interrupted"] = interrupted
    summary["status"] = "interrupted" if interrupted else ("failed" if failed else "passed")
    save_summary()
    print(
        f"\nCompleted {len(summary['results'])}/{len(jobs)} checks; "
        f"{len(failed)} nonzero exit code(s)."
    )
    for item in failed:
        print(f"  FAILED [{item['group']}] {item['original_command'][1]}: exit {item['returncode']}")
    print(f"Summary: {summary_path}")
    return 130 if interrupted else (1 if failed else 0)


if __name__ == "__main__":
    raise SystemExit(main())
