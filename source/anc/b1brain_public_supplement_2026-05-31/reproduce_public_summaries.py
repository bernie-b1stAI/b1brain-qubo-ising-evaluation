#!/usr/bin/env python3
"""Recompute the public frontier summary table from released CSV rows."""

from __future__ import annotations

import csv
import math
import statistics
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent

SUMMARY_COLUMNS = [
    "tier",
    "accelerator",
    "instance",
    "n_completed",
    "best_objective",
    "best_gap_percent",
    "mean_gap_percent",
    "std_gap_percent",
    "p50_gap_percent",
    "p90_gap_percent",
    "p95_gap_percent",
    "claim_use",
]

TIER_METADATA = {
    "T2_RTX4070": ("T2", "RTX4070", "large_seed_robustness_quality_only"),
    "T3_RTX4060_TI": ("T3", "RTX4060_Ti", "cross_tier_reproducibility"),
    "T4_RTX5090": ("T4", "RTX5090", "primary_dedicated_gpu_frontier_evidence"),
}


def read_csv(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def percentile(values: list[float], q: float) -> float:
    ordered = sorted(values)
    if not ordered:
        raise ValueError("percentile requires at least one value")
    pos = (len(ordered) - 1) * q
    lo = math.floor(pos)
    hi = math.ceil(pos)
    if lo == hi:
        return ordered[lo]
    return ordered[lo] * (hi - pos) + ordered[hi] * (pos - lo)


def fmt3(value: float) -> str:
    return f"{value:.3f}"


def frontier_summary() -> list[dict[str, str]]:
    rows = read_csv("frontier_per_run_public_extract.csv")
    groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)

    for row in rows:
        if row["status"] != "completed":
            continue
        groups[(row["tier_label"], row["instance_id"])].append(row)

    summary: list[dict[str, str]] = []
    for tier_label in ["T2_RTX4070", "T3_RTX4060_TI", "T4_RTX5090"]:
        for instance in ["G72", "G77", "G81"]:
            grouped = groups[(tier_label, instance)]
            if not grouped:
                raise ValueError(f"missing public rows for {tier_label} {instance}")

            tier, accelerator, claim_use = TIER_METADATA[tier_label]
            gaps = [float(row["gap_percent"]) for row in grouped]
            objectives = [float(row["objective_value"]) for row in grouped]

            summary.append(
                {
                    "tier": tier,
                    "accelerator": accelerator,
                    "instance": instance,
                    "n_completed": str(len(grouped)),
                    "best_objective": str(int(max(objectives))),
                    "best_gap_percent": fmt3(min(gaps)),
                    "mean_gap_percent": fmt3(statistics.mean(gaps)),
                    "std_gap_percent": fmt3(statistics.pstdev(gaps)),
                    "p50_gap_percent": fmt3(percentile(gaps, 0.50)),
                    "p90_gap_percent": fmt3(percentile(gaps, 0.90)),
                    "p95_gap_percent": fmt3(percentile(gaps, 0.95)),
                    "claim_use": claim_use,
                }
            )
    return summary


def compare_expected(generated: list[dict[str, str]]) -> list[str]:
    expected = read_csv("frontier_large_seed_summary.csv")
    failures: list[str] = []
    if len(expected) != len(generated):
        failures.append(
            f"frontier_large_seed_summary.csv row count mismatch: "
            f"expected {len(expected)}, generated {len(generated)}"
        )
        return failures

    for idx, (left, right) in enumerate(zip(expected, generated), start=1):
        for column in SUMMARY_COLUMNS:
            if left[column] != right[column]:
                failures.append(
                    f"summary row {idx} column {column}: "
                    f"expected {left[column]!r}, generated {right[column]!r}"
                )
    return failures


def print_csv(rows: list[dict[str, str]]) -> None:
    writer = csv.DictWriter(sys.stdout, fieldnames=SUMMARY_COLUMNS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)


def main() -> int:
    frontier = read_csv("frontier_per_run_public_extract.csv")
    gset = read_csv("gset_breadth_per_run_public.csv")
    biqmac = read_csv("biqmac_parity_per_run_public.csv")
    controlled = read_csv("controlled_maxcut_comparison.csv")
    generated = frontier_summary()
    failures = compare_expected(generated)

    print("Public summary reproduction")
    print(f"  frontier public extract rows: {len(frontier)}")
    print(f"  Gset breadth public rows: {len(gset)}")
    print(f"  BiqMac parity public rows: {len(biqmac)}")
    print(f"  controlled baseline summary rows: {len(controlled)}")
    print(
        "  frontier_large_seed_summary.csv: "
        + ("PASS" if not failures else "FAIL")
    )
    print()
    print_csv(generated)

    if failures:
        print("\nFailures:")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
