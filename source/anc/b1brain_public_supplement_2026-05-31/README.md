# B1Brain Public Raw-Results Supplement

This is a redacted public supplement for the B1Brain black-box optimization manuscript. It is intentionally organized by evidence lane rather than by a single global leaderboard claim.

## Evidence lanes

- `frontier_quality`: G72/G77/G81 are the narrow frontier Max-Cut claim lane. They support robustness and reproducibility against current best-known heuristic values. The frontier per-run public extract is complete for the final 15,807-row G72/G77/G81 claim set.
- `gset_breadth`: broader Gset breadth rows demonstrate source-identified execution breadth with released row checksums. They are not used to claim frontier leadership.
- `biqmac_parity`: source-repaired BiqMac rows demonstrate parity against proven-optimum baseline rows in a bounded subset. They are not used to claim broad BiqMac dominance.
- `controlled_baselines`: context-only summary values. Do not treat this lane as independently rerunnable or as a solver-superiority claim until raw baseline rows, command pins, seed lists, versions, stopping rules, and distributional traces are released or provided under controlled review.
- `tier1_entry` and `tier5_structure`: summary-only hardware evidence lanes. They are not performance-superiority lanes.
- `bitstring_release_status`: explicit marker that solution bitstrings are not public and require IP/disclosure review before any release.
- `deferred_release_gates`: concrete artifacts required before stronger bitstring, baseline-rerun, Tabu, timing, or related-work claims. No public target dates are stated for controlled artifacts.

## Redaction policy

Public per-run rows omit absolute paths, internal execution identifiers, machine fingerprints, timing fields, and implementation-level failure explanations. Timing, throughput, and perf-per-watt claims are not made in this package.

## Why G72/G77/G81 receive special focus

G72/G77/G81 are not the only tested instances. They are emphasized because they are the cleanest public frontier subset: large Gset instances, source-locked current best-known heuristic values, and a complete public per-run extract. Broader Gset and BiqMac evidence is included in separate lanes so it supports credibility without turning into an unsupported global-best claim.

G63, G64, and other active frontier instances are not included in the public frontier claim lane unless their source locks, comparison rows, and baseline release artifacts are completed. This is a claim-boundary decision, not a statement that they were never tested.

## Known limitations

- Controlled baseline raw rows, exact command pins, versions, seed lists, stopping rules, and distributional baseline traces are not included in this public supplement.
- Separate public Gset instance-file digest manifests are not included in this public supplement; Gset instance identity is recorded by public source, instance name, objective convention, and cited best-known value.
- Solution bitstrings are not public and require IP/disclosure review before any release; no public release timeline is guaranteed.
- Tabu Search/MaxCut-Bench-style lanes are deferred until a reproducible public wrapper, objective convention, restart policy, stopping rule, and command record are source-locked.
- Timing, throughput, time-to-target, GPU-hours, and energy-efficiency claims are out of scope for this supplement.

## Verifier dependencies

The verifier and summary reproducer use only the Python standard library. No third-party packages are required.

## Reproduce public summaries

Run:

```bash
python reproduce_public_summaries.py
```

This recomputes `frontier_large_seed_summary.csv` from the released `frontier_per_run_public_extract.csv` and prints the generated summary table. It does not rerun B1Brain or external baselines.
