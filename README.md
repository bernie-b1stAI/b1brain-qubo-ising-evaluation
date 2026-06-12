# B1Brain QUBO/Ising Evaluation Evidence Package

This repository contains the public-safe evidence package for:

**Source-Locked Evaluation of Black-Box QUBO and Ising Heuristics: Public Evidence from Gset Max-Cut and BiqMac Certified-Value Checks**

The package supports a conservative Optimization Online submission about black-box solver evaluation methodology. It is not a release of the B1Brain solver implementation.

## Public Anchor Status

- Submitted to Optimization Online: 2026-06-04.
- Optimization Online decision: rejected as out of scope on 2026-06-11.
- Current public anchor: this GitHub evidence repository.
- DOI path: use the Zenodo upload folder in `zenodo/2026-06-12/` to publish a DOI-backed archive of the public paper, source package, and supplement.

## What Is Included

- `paper/b1brain_source_locked_evaluation.pdf` - rendered manuscript PDF.
- `source/main.tex` - LaTeX manuscript source.
- `source/main.bbl` and `source/references.bib` - bibliography artifacts.
- `source/figures/` - public-safe paper figures.
- `source/data/` - public validation CSVs used by the paper tables and figures.
- `source/anc/b1brain_public_supplement_2026-05-31/` - redacted public supplement, including the 15,807-row G72/G77/G81 frontier extract, verifier, reproducer, checksums, and release-boundary files.

## Claim Boundary

The public evidence supports source-locked row accounting, redacted per-run frontier objectives, Gset breadth rows, BiqMac certified-value parity checks, checksum verification, and distributional robustness reporting.

The public evidence does **not** support claims of Max-Cut leadership, proven optimality for G72/G77/G81, timing superiority, throughput, energy efficiency, public rerunability of controlled baselines, or full reproduction of proprietary solver internals.

The controlled-baseline table is context-only. Raw baseline rows, command pins, seed lists, versions, stopping rules, and distributional traces are not public in this release.

## Reproduce Public Summaries

From `source/anc/b1brain_public_supplement_2026-05-31/`:

```bash
python verify_public_supplement.py
python reproduce_public_summaries.py
```

Expected result: both scripts report `PASS`.

## Disclosure Boundary

This repository intentionally excludes unredacted append-only JSONL rows, solution bitstrings, exact solver-interface details, timing logs, private run orchestration files, and implementation-level solver mechanics.

## DOI Status

No DOI has been minted yet. The Zenodo record should be published from the release-ready files and metadata in `zenodo/2026-06-12/`; after Zenodo publication, update this README and `CITATION.cff` with the minted DOI.
