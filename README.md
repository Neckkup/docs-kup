# claude-skills

สกิลของ Claude Code ที่ใช้เอง

| สกิล | ทำอะไร |
|---|---|
| [neck-dog](neck-dog/SKILL.md) | จัดโครงและเขียนเอกสารของ repo จากโค้ดจริง (architecture, คู่มือ backend/frontend, ci-cd) และอัปเดตหลัง merge |

## ติดตั้ง

ใช้กับทุกโปรเจกต์บนเครื่อง:

```
git clone <url ของ repo นี้> ~/claude-skills
ln -s ~/claude-skills/neck-dog ~/.claude/skills/neck-dog
```

หรือใช้เฉพาะโปรเจกต์เดียว: คัดลอกโฟลเดอร์ `neck-dog/` ไปไว้ที่ `<project>/.claude/skills/neck-dog/`

เรียกใช้ใน Claude Code ด้วย `/neck-dog` หรือขอแบบปกติ เช่น "ทำเอกสาร architecture ของ repo นี้ให้หน่อย"
