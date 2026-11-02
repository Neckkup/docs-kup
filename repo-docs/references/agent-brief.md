# brief สำหรับ agent ที่เขียนหน้า architecture

คัดลอกแม่แบบนี้แล้วเติมส่วนใน `<...>` ให้ agent แต่ละตัว ตัวละ 1–2 หน้า

```
You are writing architecture documentation for the repo at <absolute repo path>.
Write <N> file(s):

1. <docs/architecture/0X-name.md> — <what the page covers, in one paragraph>.
   Primary sources: <files/folders that are the source of truth>.
   Rationale docs to link for "why": <spec/ADR/plan paths, if any>.

Writing rules (must follow):
- Language: <language of existing docs>. Read <one existing doc in the repo> first to match tone and density
  (short sentences, tables where useful, technical terms stay English).
- Current state only, verified by reading code. Tag claims [โค้ด] (read from source) or [อนุมาน] (inferred,
  unverified). Never invent.
- Cite sources as markdown links relative to docs/architecture/ (e.g. [server.go](../../backend/internal/httpserver/server.go)).
  Folders with parentheses must be percent-encoded in links: (app) → %28app%29.
- No exhaustive lists that drift (every endpoint/permission/event/column). Explain the pattern, give 2–5
  examples, link the source file.
- Don't repeat deploy/env content; link <ops or ci-cd doc> instead.
- At most 1–2 small mermaid diagrams.
- Start with `# <title>`, then `[← architecture](README.md)`, then a 1–2 sentence intro.
  Target <80–200> lines.
- Do not edit any other file. Do not commit.

Report at the end: files written, line counts, and a list of inconsistencies you found between code and
specs/existing docs (one line each).
```

## การจับคู่หัวข้อ

| agent | หน้า | เหตุผล |
|---|---|---|
| 1 | 01-modules + 05-events-jobs | ใช้ entrypoint, การ wire และ event ของโมดูลชุดเดียวกัน |
| 2 | 02-api + 03-auth | ใช้ middleware และ session ชุดเดียวกัน |
| 3 | 04-database | อ่าน migration ทั้งหมด งานหนักพอตัวเดียว |
| 4 | 06-frontend | แยก codebase |

ถ้า repo เล็ก (ไม่เกิน ~50 ไฟล์โค้ด) เขียนเองโดยไม่ใช้ agent
