# Task Plan: zhizhi Learning Data Migration

## Goal
Migrate existing local learning data from `/Users/linqihai/Work/zhizhi` into this personal learning repository and push it to GitHub.

## Phases
- [x] Phase 1: Inspect source and target directories
- [x] Phase 2: Initialize target learning repository structure
- [x] Phase 3: Copy learning data and exclude reusable skill/source artifacts
- [x] Phase 4: Review Git contents and privacy-sensitive exclusions
- [x] Phase 5: Commit and push to GitHub after explicit public-sync confirmation

## Key Questions
1. Which old directories are learning data and should be committed?
2. Which old directories are tools, installed skills, IDE files, large copyrighted sources, or generated artifacts that should be excluded?

## Decisions Made
- Copy learning data directories: `memory/`, `mistakes/`, `records/`, `weak-points/`, `worksheets/`.
- Initialize missing current-layout directories such as `curriculum/`, `knowledge-points/`, and `site/`.
- Keep textbook metadata as curriculum references, but do not commit textbook PDF files.
- Exclude `.idea/`, `.DS_Store`, `skills/`, `scripts/`, `templates/`, `zhizhi.zip`, OCR raw output, and textbook PDF files from Git commit.
- Preserve source directory and copy data into the target repository; do not move or delete source files.

## Errors Encountered
- Target directory did not exist locally; resolved by cloning `git@github.com:linzi007/zhizhi-math-learning-data.git`.
- Remote repository appears publicly accessible over HTTPS. User explicitly confirmed direct push is acceptable.

## Status
**Ready to push** - User confirmed public sync is acceptable.
