# Migration Summary

## Source And Target

- Source: `/Users/linqihai/Work/zhizhi`
- Target: `/Users/linqihai/Work/zhizhi-math-learning-data`
- Remote: `git@github.com:linzi007/zhizhi-math-learning-data.git`
- Migration date: 2026-05-18

## Migrated

- `memory/`
- `mistakes/`
- `records/`
- `weak-points/`
- `worksheets/`
- initialized `curriculum/`, `knowledge-points/`, and `site/`
- generated child-facing GitHub Pages HTML under `site/`

## Excluded From Git

- `.idea/`
- `.DS_Store`
- old installed `skills/`
- old local `scripts/`
- old local `templates/`
- `zhizhi.zip`
- `ocr-output/`
- textbook PDF files under `textbooks/`

## Notes

Textbook source metadata was preserved in `curriculum/textbook-sources.md`. Textbook PDFs and OCR outputs were not copied into this Git repository.

The `site/` directory contains child-facing worksheet pages only. Answer keys, diagnosis records, memory, weak-point history, and worksheet source specs stay outside `site/`.

The remote repository appeared publicly accessible during migration. The user explicitly confirmed direct push is acceptable.
