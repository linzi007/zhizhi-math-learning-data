# zhizhi-math-learning-data

This is a personal learning repository for `zhizhi-math-coach`.

Open this repository as the OpenClaw workspace for daily grading, diagnosis, worksheet generation, and learning-record updates.

## Directory Roles

- `memory/`: long-term and short-term learning memory.
- `curriculum/`: grade, semester, textbook, calendar, and progress scope.
- `knowledge-points/`: reusable explanation cards and mastery rules.
- `weak-points/`: durable weak-point history.
- `mistakes/`: school and system-generated mistake books.
- `records/`: dated diagnosis and progress records.
- `worksheets/`: generated worksheet specs, printable HTML, and answer keys.
- `site/`: optional child-facing public pages only.

## Daily Use

Run OpenClaw in this repository and invoke:

```text
$zhizhi-math-coach 批改这张练习卷，记录薄弱项。
$zhizhi-math-coach 根据最近错题生成变式练习。
```

Sync to GitHub explicitly:

```bash
git add curriculum knowledge-points memory mistakes records weak-points worksheets site
git commit -m "Update learning records"
git push
```

If this repository is public, commit only files that are safe to expose.
