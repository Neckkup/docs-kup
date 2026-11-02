# claude-skills

สกิลของ Claude Code ที่ใช้เอง

| สกิล | ทำอะไร |
|---|---|
| [repo-docs](repo-docs/SKILL.md) | จัดโครงและเขียนเอกสารของ repo จากโค้ดจริง (architecture, คู่มือ backend/frontend, ci-cd) และอัปเดตหลัง merge |

## ติดตั้ง

ใช้กับทุกโปรเจกต์บนเครื่อง:

```
git clone <url ของ repo นี้> ~/claude-skills
ln -s ~/claude-skills/repo-docs ~/.claude/skills/repo-docs
```

หรือใช้เฉพาะโปรเจกต์เดียว: คัดลอกโฟลเดอร์ `repo-docs/` ไปไว้ที่ `<project>/.claude/skills/repo-docs/`

เรียกใช้ใน Claude Code ด้วย `/repo-docs` หรือขอแบบปกติ เช่น "ทำเอกสาร architecture ของ repo นี้ให้หน่อย"
