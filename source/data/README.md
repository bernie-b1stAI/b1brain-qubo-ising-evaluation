# Public Validation Tables

This directory contains public-safe validation tables for the B1Brain arXiv draft.

These files are intended to make the paper more auditable without exposing protected implementation details:

- `frontier_large_seed_summary.csv`
- `controlled_maxcut_comparison.csv`
- `hardware_evidence_matrix.csv`
- `exclusion_registry.csv`
- `validation_manifest.csv`
- `tier_invariance_diagnostics.csv`
- `seed_plateau_summary.csv`

The companion ancillary supplement under `../anc/b1brain_public_supplement_2026-05-31/` adds the complete 15,807-row redacted public frontier extract for G72/G77/G81, plus redacted public per-run CSV extracts for broader Gset breadth and source-repaired BiqMac parity rows. G72/G77/G81 remain the frontier Max-Cut claim lane; broader rows support breadth and parity, not global leadership.

Unredacted append-only JSONL rows, solution bitstrings, raw controlled-baseline rows, and separate public Gset instance-file digest manifests are not included in this public source package. They remain controlled-review artifacts or deferred release gates until public release is separately cleared. The manuscript therefore claims distributional robustness, source-identified benchmark identity, released-artifact checksum verification, and context-only controlled-baseline accounting, not best-known leadership, full baseline rerunability, baseline superiority, or independent cut-certificate release.
