# Notes: zhizhi Learning Data Migration

## Source

- Source path: `/Users/linqihai/Work/zhizhi`
- Source is not a Git repository.
- Source size: about 294 MB, mostly textbook PDFs under `textbooks/`.

## Source Top-Level Contents

- Learning data to migrate: `memory/`, `mistakes/`, `records/`, `weak-points/`, `worksheets/`.
- Local tooling or reusable artifacts to exclude: `skills/`, `scripts/`, `templates/`.
- IDE/system files to exclude: `.idea/`, `.DS_Store`.
- Large/copyright-sensitive files to exclude from Git: `textbooks/**/*.pdf`, OCR raw outputs, `zhizhi.zip`.

## Target

- Target path: `/Users/linqihai/Work/zhizhi-math-learning-data`
- Remote: `git@github.com:linzi007/zhizhi-math-learning-data.git`
- Remote cloned successfully; repository was empty.

## Migration Result

- Initialized standard personal learning repository structure.
- Copied old learning directories into the target repository.
- Generated child-facing `site/` pages from existing worksheet HTML.
- Migrated/created 57 files under learning-data directories: `memory/`, `mistakes/`, `records/`, `weak-points/`, `worksheets/`, `curriculum/`, `knowledge-points/`, and `site/`.
- Updated curriculum files to reflect 芝芝, 一年级下学期, 人教版一年级下册, and current weak-point-driven scope.
- Created `curriculum/textbook-sources.md` from old textbook metadata without copying PDF files.

## Verification Notes

- No files larger than 1 MB are present in the target working tree.
- No PDF, zip, image, `.DS_Store`, `ocr-output/`, or old `skills/` files are present in the target working tree.
- `site/` scan found no answer-key markers, answer details, or grading-standard markers.
- HTTPS check for `https://github.com/linzi007/zhizhi-math-learning-data` returned `200`, so the remote appears publicly accessible. User explicitly confirmed direct push is acceptable.
