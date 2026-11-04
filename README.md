# docs-kup

สกิลของ Claude Code สำหรับจัดโครงและเขียนเอกสารของ repo จากโค้ดจริง ได้แก่ `docs/architecture`, คู่มือ backend/frontend, ci-cd, ops และ reference รวมถึงอัปเดตเอกสารชุดนั้นหลัง merge ฟีเจอร์

ขั้นตอนอยู่ใน [SKILL.md](SKILL.md) แม่แบบและกฎการเขียนอยู่ใน [references/](references/) สคริปต์ย้ายไฟล์และตรวจลิงก์อยู่ใน [scripts/](scripts/)

## ติดตั้ง

ใช้กับทุกโปรเจกต์บนเครื่อง:

```
git clone https://github.com/Neckkup/docs-kup.git ~/.claude/skills/docs-kup
```

ใช้เฉพาะโปรเจกต์เดียว:

```
git clone https://github.com/Neckkup/docs-kup.git <project>/.claude/skills/docs-kup
```

## ใช้งาน

ใน Claude Code พิมพ์ `/docs-kup` หรือขอแบบปกติ เช่น "ทำเอกสาร architecture ของ repo นี้ให้หน่อย" หรือ "อัปเดต docs หลัง merge ฟีเจอร์ล่าสุด"

สคริปต์ใช้แยกได้:

```
python3 -I scripts/relink.py <repo> old/path.md=new/path.md   # ย้ายไฟล์ + แก้ลิงก์ relative
python3 -I scripts/checklinks.py <repo>                       # ตรวจลิงก์เสียทั้ง repo
```
