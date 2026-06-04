#!/usr/bin/env python3
"""Verify the public B1Brain supplement has the expected redaction shape."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parent
FORBIDDEN_SUBSTRINGS = [
    "/mnt/",
    "/home/",
    "C:\\",
    "raw_log_path",
    "host_fingerprint",
    "solver_config_hash",
    "solver_entrypoint",
    "PROFVAL_FINAL_ASSEMBLY_PLAN",
    "NotebookLM",
    "Claude",
    "Gemini",
    "beats" + " open SB",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def csv_row_count(path: Path) -> str:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        try:
            next(reader)
        except StopIteration:
            return "0"
        return str(sum(1 for _ in reader))


def check_manifest() -> list[str]:
    manifest = read_csv(ROOT / "checksum_manifest.csv")
    by_name = {row["file"]: row for row in manifest}
    expected = sorted(
        path
        for path in ROOT.iterdir()
        if path.is_file() and path.name != "checksum_manifest.csv"
    )

    failures: list[str] = []
    expected_names = {path.name for path in expected}
    manifest_names = set(by_name)

    for name in sorted(expected_names - manifest_names):
        failures.append(f"checksum_manifest.csv: missing {name}")
    for name in sorted(manifest_names - expected_names):
        failures.append(f"checksum_manifest.csv: stale entry {name}")

    for path in expected:
        row = by_name.get(path.name)
        if not row:
            continue
        if row.get("sha256") != sha256_file(path):
            failures.append(f"checksum_manifest.csv: sha256 mismatch for {path.name}")
        if row.get("bytes") != str(path.stat().st_size):
            failures.append(f"checksum_manifest.csv: byte count mismatch for {path.name}")
        expected_rows = csv_row_count(path) if path.suffix.lower() == ".csv" else ""
        if row.get("csv_rows", "") != expected_rows:
            failures.append(f"checksum_manifest.csv: csv row count mismatch for {path.name}")

    return failures


def scan_forbidden() -> list[str]:
    hits: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.name == "verify_public_supplement.py":
            continue
        if path.suffix.lower() not in {".csv", ".md", ".py", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for term in FORBIDDEN_SUBSTRINGS:
            if term in text:
                hits.append(f"{path.name}: {term}")
    return hits


def main() -> int:
    inventory = read_csv(ROOT / "evidence_lane_inventory.csv")
    redactions = read_csv(ROOT / "redaction_manifest.csv")
    frontier = read_csv(ROOT / "frontier_per_run_public_extract.csv")
    gset = read_csv(ROOT / "gset_breadth_per_run_public.csv")
    biqmac = read_csv(ROOT / "biqmac_parity_per_run_public.csv")

    failures: list[str] = []
    for name, rows in {
        "frontier_per_run_public_extract.csv": frontier,
        "gset_breadth_per_run_public.csv": gset,
        "biqmac_parity_per_run_public.csv": biqmac,
    }.items():
        bad = [r for r in rows if r.get("status") != "completed"]
        if bad:
            failures.append(f"{name}: contains {len(bad)} non-completed rows")
        timed = [r for r in rows if r.get("timing_claim_allowed") != "false"]
        if timed:
            failures.append(f"{name}: timing claim flag not false on {len(timed)} rows")

    if not inventory:
        failures.append("evidence_lane_inventory.csv is empty")
    if not redactions:
        failures.append("redaction_manifest.csv is empty")

    forbidden = scan_forbidden()
    failures.extend(f"forbidden text hit: {hit}" for hit in forbidden)
    failures.extend(check_manifest())

    print("Public supplement verification")
    print(f"  frontier public extract rows: {len(frontier)}")
    print(f"  Gset breadth public rows: {len(gset)}")
    print(f"  BiqMac parity public rows: {len(biqmac)}")
    print(f"  inventory lanes: {len(inventory)}")
    print(f"  redaction rules: {len(redactions)}")
    print(f"  checksum manifest entries: {len(read_csv(ROOT / 'checksum_manifest.csv'))}")
    print(f"  supplement sha256: {sha256_file(ROOT / 'checksum_manifest.csv')}")

    if failures:
        print("FAIL")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
