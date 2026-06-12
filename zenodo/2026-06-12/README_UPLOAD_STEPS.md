# Zenodo Upload Handoff

Date: 2026-06-12

This folder is the DOI handoff package for the public B1Brain QUBO/Ising evaluation evidence repository.

## Upload These Files

Upload only the files inside `upload/`:

1. `b1brain_source_locked_evaluation_2026-06-12.pdf`
2. `b1brain_public_source_package_2026-06-12.zip`
3. `b1brain_public_supplement_2026-05-31.zip`
4. `UPLOAD_FILE_MANIFEST.sha256`

Do not upload `.git`, private workspace files, internal review notes, raw JSONL traces, solution bitstrings, timing logs, solver internals, or controlled-baseline command pins.

## Zenodo Steps

1. Open `https://zenodo.org/uploads/new`.
2. Upload the four files listed above.
3. In the DOI field, choose `No` for "Do you already have a DOI for this upload?"
4. Optional: click `Get a DOI now!` only if you want to reserve a DOI before publishing and then edit files to include that DOI.
5. Copy the fields from `ZENODO_FORM_VALUES.md`.
6. Preview the record.
7. Publish only after confirming the license choice.

## Source For These Instructions

Zenodo documentation used for this handoff:

- Records include metadata, files, and a DOI; Zenodo registers a DOI when a record is published.
- After publication, files and the persistent identifier are not generally mutable; use versions for substantive updates.
- New uploads require basic metadata including resource type, title, publication date, creators, and publisher.
- Zenodo supports up to 100 files / 50GB; it recommends ZIP archives when there are 20+ files.
- The license field is required and Zenodo defaults to CC-BY-4.0.

Official docs:

- https://help.zenodo.org/docs/deposit/about-records/
- https://help.zenodo.org/docs/deposit/create-new-upload/
- https://help.zenodo.org/docs/deposit/manage-files/
- https://help.zenodo.org/docs/deposit/describe-records/reserve-doi/
- https://help.zenodo.org/docs/deposit/describe-records/resource-type/
- https://help.zenodo.org/docs/deposit/describe-records/licenses/
