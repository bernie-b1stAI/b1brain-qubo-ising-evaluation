# Zenodo Form Values

Copy these values into the Zenodo upload form.

## Files

Upload these files from `zenodo/2026-06-12/upload/`:

- `b1brain_source_locked_evaluation_2026-06-12.pdf`
- `b1brain_public_source_package_2026-06-12.zip`
- `b1brain_public_supplement_2026-05-31.zip`
- `UPLOAD_FILE_MANIFEST.sha256`

## Basic Information

**DOI**

No existing DOI. Let Zenodo mint the DOI on publication. Reserve a DOI only if you plan to edit files before publishing to include the DOI.

**Resource Type**

Publication > Preprint

If the UI does not expose a preprint subtype, use:

Publication > Report

**Title**

Source-Locked Evaluation of Black-Box QUBO and Ising Heuristics: Public Evidence from Gset Max-Cut and BiqMac Certified-Value Checks

**Publication Date**

2026-06-12

**Creators**

Bernardo De Araujo Coutinho Mendonca

Affiliation: Independent Researcher, United States

ORCID: leave blank unless you have one to add.

**Publisher**

Zenodo

**Version**

2026.06.12

**Language**

English

**License**

Creative Commons Attribution 4.0 International (CC-BY-4.0)

Do not publish until you are comfortable granting this reuse license. Zenodo requires a license and defaults to CC-BY-4.0.

## Description

This record archives the public-safe evidence package for "Source-Locked Evaluation of Black-Box QUBO and Ising Heuristics: Public Evidence from Gset Max-Cut and BiqMac Certified-Value Checks."

The paper presents a source-locked, append-only evaluation protocol for proprietary black-box QUBO and Ising solvers and applies it to B1Brain across locally controlled compute tiers. The public evidence snapshot includes completed solver rows across public-safe evidence lanes, a redacted Gset Max-Cut frontier extract, BiqMac certified-value parity checks, checksum manifests, public validation tables, and verifier/reproducer scripts.

The archive is intentionally conservative. It supports claims about source-locked row accounting, public-safe evidence integrity, redacted per-run frontier objectives, checksum verification, and distributional reporting. It does not support claims of Max-Cut leadership, proven optimality for G72/G77/G81, timing superiority, throughput, energy efficiency, public rerunability of controlled baselines, or release of proprietary solver internals.

The public GitHub evidence repository is:

https://github.com/bernie-b1stAI/b1brain-qubo-ising-evaluation

## Additional Notes

Optimization Online status: submitted on 2026-06-04 and rejected as out of scope on 2026-06-11. This Zenodo record is the DOI-backed public archive replacing Optimization Online as the public anchor.

The archive excludes unredacted append-only JSONL rows, solution bitstrings, exact solver-interface details, timing/resource traces, private run orchestration files, and controlled-baseline command pins. Those omissions are release boundaries, not hidden support for stronger claims.

## Keywords

QUBO

Ising

Max-Cut

Gset

BiqMac

black-box solver evaluation

source-locked evaluation

reproducibility

optimization benchmarking

checksum manifest

public evidence package

## Related URL To Include In Description

https://github.com/bernie-b1stAI/b1brain-qubo-ising-evaluation

No related DOI exists yet.
