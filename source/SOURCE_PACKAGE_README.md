# arXiv Black-Box Source Package

Status: public-safe source package prepared for public evidence release and Optimization Online PDF support.
Date: 2026-06-02.

Public evidence repository:

`https://github.com/bernie-b1stAI/b1brain-qubo-ising-evaluation`

## Contents

- `main.tex` - canonical LaTeX manuscript.
- `references.bib` - public bibliography entries.
- `main.bbl` - generated bibliography file, retained for arXiv portability.
- `figures/` - public-safe PNG figures used by `main.tex`, including evidence volume, row-admissibility flow, frontier box plot, ECDF, and seed-plateau figures generated from public-safe data.
- `data/` - public-safe validation CSVs and data notes supporting the manuscript tables, figures, row accounting, and cross-tier diagnostics.
- `anc/b1brain_public_supplement_2026-05-31/` - redacted ancillary supplement with evidence-lane inventory, complete public frontier per-run extract, public per-run extracts for Gset breadth and BiqMac parity, checksums, deferred-release gates, a local verifier, and a one-command summary reproducer.
- `requirements.txt` - verifier dependency note; the public supplement verifier uses only the Python standard library.

This source package is a public-safe black-box candidate. It includes summary figures, validation tables, and redacted public per-run CSV extracts. It intentionally excludes unredacted append-only JSONL rows, solution bitstrings, implementation details, execution setup files, and internal review documents.

The public-safe evidence snapshot contains `20,223` completed solver rows across non-overlapping evidence lanes. A separate `3`-row controlled-baseline summary is retained only as context and is not counted inside that completed-row evidence total.

## Reviewer Note

Public files support source-locked row accounting, redacted per-run frontier objectives, Gset breadth rows, BiqMac parity rows, checksum verification for released artifacts, and a context-only controlled-baseline summary. Controlled-review artifacts that are intentionally not public are unredacted JSONL traces, solution bitstrings, exact solver interface details, timing/resource traces, raw controlled-baseline rows or command transcripts, and separate public Gset instance-file digest manifests. Those omissions are release gates, not hidden evidence for stronger claims.

## Evidence-Lane Boundary

G72/G77/G81 are the frontier Max-Cut lane because they have clean source-locked current best-known heuristic values and a complete public per-run frontier extract. They are not the whole campaign. Broader Gset and source-repaired BiqMac rows are included in the ancillary supplement as separate breadth/parity lanes, not as global leadership claims. Breadth and parity lanes use bounded seed counts for coverage and integrity checks; the frontier lane is deep-sampled because it is the main distributional stability target. For BiqMac, source-repaired means the public instance/reference-value mapping, objective convention, and certified-value association are corrected and verified against the cited source before rows are admitted; solver outputs are not changed by the repair step.

G63, G64, Tabu Search/MaxCut-Bench-style baselines, exact controlled-baseline commands, and bitstring validation are explicit follow-up lanes. They should not be implied by the current arXiv candidate.

## Known Limitations

- Controlled baseline source-locking is asymmetric in the public package: B1Brain public extracts and released CSV/script checksums are more completely exposed than baseline command pins, raw controlled rows, and separate public Gset instance-file digests.
- Solution bitstrings are not included. They remain controlled-review artifacts pending IP, patent, export-control, and disclosure clearance.
- Table/figure claims about the controlled baseline lane are summary-level only until exact command pins, versions, seed lists, stopping rules, and raw controlled rows are released or made available under controlled review.
- G63, G64, Tabu Search/MaxCut-Bench-style baselines, broader Gset lanes, and vertical examples are deferred until source-lock artifacts are complete.
- Timing, throughput, time-to-target, GPU-hours, and perf-per-watt are not claimed.

## Final Submission Checklist

1. Final author, affiliation, contact, and public URL metadata were added on 2026-06-02.
2. The author confirmed public-disclosure clearance for this redacted package on 2026-06-02.
3. Source-lock baseline commands, versions, seeds, build flags, stopping rules, and raw controlled rows remain required before claiming independent rerunability of the controlled-baseline context table.
4. Solution bitstrings remain controlled-review artifacts pending separate IP, patent, export-control, and disclosure clearance.
5. Re-run the related-work freshness check if submission moves materially beyond the current submission window.
6. Re-run compile immediately before upload if author metadata changes.
7. Run the public-source hygiene scan before upload.
8. Run `python anc/b1brain_public_supplement_2026-05-31/verify_public_supplement.py`.
9. Run `python anc/b1brain_public_supplement_2026-05-31/reproduce_public_summaries.py`.
10. Check `pdffonts main.pdf` for Type 3 fonts after final compile.
11. Visually inspect the final compiled PDF after metadata is filled.
12. Build the upload ZIP from source files only; do not include `main.pdf`, generated logs, editor backups, or QA artifacts.

## Compile / Visual QA

Local build check passed on 2026-06-01 using MiKTeX `pdflatex` against the included bibliography output. Re-run after final metadata edits:

`pdflatex -interaction=nonstopmode -halt-on-error main.tex`

The generated PDF, compile log, and rendered PNG pages should remain QA artifacts. The arXiv upload ZIP should contain source files, bibliography output, referenced figures, data tables, and the ancillary supplement, but not the compiled PDF.

Public supplement verifier passed on 2026-06-01:

- frontier public extract rows: `15807`
- Gset breadth public rows: `330`
- BiqMac parity public rows: `90`
- inventory lanes: `6`
- redaction rules: `5`
- checksum manifest entries: `16`
- supplement sha256: `736dd22ee2411eb52df1ca7e74d9e79b9810ee7fef3a77ae9e579c7f7a650b41`

Public summary reproduction also passed on 2026-06-01:

- `frontier_large_seed_summary.csv`: `PASS`
- controlled baseline summary rows: `3`

Font QA passed on 2026-06-01 using MiKTeX `pdffonts`: all listed fonts are embedded Type 1 fonts; no Type 3 fonts were reported.

## Public Wording Boundary

Describe the controlled-baseline table as context-only unless raw rows, commands, seeds, versions, stopping rules, and distributional baseline traces are released or provided under controlled review. Avoid promotional comparison verbs, quality-leadership language, and proven-optimum language for G72/G77/G81.
