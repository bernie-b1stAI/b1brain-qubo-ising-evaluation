# Public Per-Run Schema

- `public_row_id`: stable public identifier for the redacted row.
- `evidence_lane`: claim lane; do not merge lanes into one leaderboard.
- `source_file_public_id`: filename stem only; no filesystem paths.
- `suite_id`, `instance_id`: public benchmark identifiers.
- `tier_label`, `hardware_class`: coarse hardware label.
- `seed`: run seed where present.
- `status`: only `completed` rows are included in public per-run claim CSVs.
- `claim_pin_status`, `capability_boundary_status`: integrity gates carried from the raw row.
- `best_known_source_id`, `baseline_value_type`, `best_known_value`: source-locked comparison reference.
- `objective_value`, `quality_metric`, `gap_to_best_known`, `gap_fraction`, `gap_percent`: quality evidence. In the released public per-run extracts, `quality_metric` is the numeric gap fraction used for sorting and comparison; it duplicates `gap_fraction` for schema compatibility with internal claim ledgers.
- `timing_claim_allowed`: always `false` in this public supplement.
- `timing_disclosure_status`: explains why timing fields are absent.
- `source_row_sha256`: digest of the raw row before redaction, for internal reproducibility linkage.
- `public_row_sha256`: digest of the public row after redaction.
