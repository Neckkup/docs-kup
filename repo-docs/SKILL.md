---
name: repo-docs
description: จัดโครงและเขียนเอกสารของ repo จากโค้ดจริง (docs/architecture, คู่มือ backend/frontend, ci-cd, ops, reference) หรืออัปเดตเอกสารชุดนั้นหลัง merge ฟีเจอร์ ใช้เมื่อผู้ใช้ขอให้ทำเอกสารระบบ, จัด docs ใหม่, เขียน architecture, ทำเอกสาร onboarding, เทียบเอกสารกับโค้ด หรือย้ายไฟล์เอกสารโดยไม่ให้ลิงก์เสีย
---

# repo-docs

สร้างหรือจัดเอกสารของ repo ให้บอกว่าระบบ **ตอนนี้** ทำงานอย่างไร เขียนจากโค้ด ลิงก์กลับไปที่ไฟล์ต้นทาง และไม่คัดลอกรายการยาวที่จะล้าหลังโค้ด

## โครงเป้าหมาย

```
docs/
├── README.md               ← สารบัญ + วิธีดูแลเอกสาร
├── architecture/
│   ├── README.md           ← ภาพรวมระบบ (container diagram + หลักใหญ่ + ตารางหน้า 01–0N)
│   ├── 01-modules.md       ← โมดูล/แพ็กเกจหลัก ขอบเขต การพึ่งพา
│   ├── 02-api.md           ← เส้นทาง request, middleware, handler, error, pagination
│   ├── 03-auth.md          ← login, session, role, permission
│   ├── 04-database.md      ← schema, migration, convention, การแยก tenant
│   ├── 05-events-jobs.md   ← คิว, worker, งานตามเวลา, การแจ้งเตือน
│   └── 06-frontend.md      ← route, การเรียก api, state, i18n, offline
├── backend/README.md       ← คู่มือพัฒนา: เริ่มรัน, คำสั่ง, งานที่ทำบ่อย
├── frontend/README.md      ← คู่มือพัฒนา (+ DESIGN.md ถ้ามี)
├── ci-cd.md                ← pipeline, stack ที่ deploy, CI variables, rollback
├── ops/                    ← deploy/ดูแลระบบ, บัญชีเครื่องพัฒนา (ถ้ามีเนื้อหา)
└── reference/              ← ความรู้ภายนอกที่ใช้อ้างอิง ไม่ใช่ของระบบนี้
```

หน้า 01–06 เป็นค่าเริ่มต้น ตัดหน้าที่ระบบไม่มี (เช่น ไม่มีคิวงาน → ไม่มี 05) และเพิ่มหน้าที่ระบบมีจริง (เช่น 07-search) โดยเรียงเลขต่อ
ถ้า repo ไม่ได้แยก backend/frontend ให้ใช้ชื่อโฟลเดอร์ตามส่วนที่มีจริง

## ขั้นตอน

### 1. สำรวจ (อ่านอย่างเดียว)

- `git status` และ `git log -5` ก่อนเสมอ บอกผู้ใช้ถ้ามีงานค้างที่ยังไม่ commit เพราะเอกสารจะถูกเขียนตาม working tree
- โครงโฟลเดอร์, README ทุกตัว, `docs/`, ไฟล์ .md ทั้งหมด (`find . -name '*.md'` ข้าม node_modules, .git, vendor)
- ตัวจริงของแต่ละเรื่อง: compose/Dockerfile, CI config, Makefile/package.json scripts, OpenAPI/route, migration/schema, entrypoint ของแต่ละ process
- เอกสารเดิมที่จะย้ายหรือทับ: ใครลิงก์มาหาบ้าง (`grep -rn` ทั้ง repo รวมคอมเมนต์ในโค้ดและ script) และไฟล์ไหนอยู่ใน `.gitignore`

### 2. เสนอโครงและถามก่อนแก้

แสดง tree ของ `docs/` ที่จะได้ ตารางว่าหน้าไหนมาจากไฟล์ไหน และรายการไฟล์ที่จะย้าย แล้วถามผู้ใช้ด้วย AskUserQuestion ถ้ามีทางเลือกจริง (เช่น เลขนำหน้าชื่อไฟล์, จะย้ายเอกสารอ้างอิงไหม) ห้ามย้ายหรือเขียนก่อนผู้ใช้ตกลง

### 3. ย้ายไฟล์เดิม (ถ้ามี)

ใช้ `scripts/relink.py` ย้ายทุกไฟล์ในครั้งเดียว สคริปต์ใช้ `git mv` กับไฟล์ที่ track อยู่ และคำนวณลิงก์ relative ใหม่ทั้งในไฟล์ที่ย้ายและไฟล์ที่ชี้เข้ามา:

```
python3 -I <skill>/scripts/relink.py <repo> old/path.md=new/path.md [...]
```

จากนั้นค้น path ที่เขียนเป็นข้อความ (ไม่ใช่ลิงก์) เช่น ในแผนผังโฟลเดอร์ของ README, คอมเมนต์ในโค้ด, script แล้วแก้เอง
ไม่ต้องแก้บันทึกประวัติ (tasks ที่ติ๊กแล้ว, changelog, sync report) เพราะเป็นข้อเท็จจริง ณ เวลานั้น
ไฟล์ที่อยู่ใน `.gitignore` ต้องแก้ ignore ตามที่อยู่ใหม่ ไม่งั้นจะหลุดเข้า git

### 4. เขียนหน้า

- หน้าภาพรวม (`architecture/README.md`), `docs/README.md` และคู่มือ backend/frontend เขียนเอง
- หน้า 01–0N ที่ต้องอ่านโค้ดมาก แบ่งให้ agent เขียนพร้อมกัน 3–4 ตัว (จับคู่หัวข้อที่ใช้ไฟล์ต้นทางชุดเดียวกัน เช่น api+auth, modules+events) และให้ทุกตัวได้ brief จาก [references/agent-brief.md](references/agent-brief.md)
- แม่แบบของแต่ละหน้าอยู่ใน [references/page-templates.md](references/page-templates.md)
- กฎการเขียนทุกหน้าอยู่ใน [references/writing-rules.md](references/writing-rules.md)

### 5. ตรวจ

1. `python3 -I <skill>/scripts/checklinks.py <repo>` ต้องได้ `broken 0` (ข้าม worktree และ node_modules ให้แล้ว)
2. สุ่มเช็คข้อเท็จจริง 3–5 ข้อจากแต่ละหน้าเทียบกับโค้ด (ชื่อ cookie, ค่าคงที่, ลำดับ middleware, ชื่อ job)
3. ทำคำสั่งในคู่มือให้ถูกลำดับบนเครื่องใหม่ (เช่น ต้องเปิด DB ก่อน migrate) ถ้าไม่ได้ลองรันจริงให้บอกผู้ใช้
4. ก่อน commit รัน `git status` อีกครั้ง ถ้ามีไฟล์ที่เปลี่ยนจากที่อื่นระหว่างทำ (ไฟล์หาย, CI ถูกแก้) หยุดแล้วถามผู้ใช้ และแก้เอกสารให้ตรงกับสภาพล่าสุดก่อน

### 6. รายงาน

บอกผู้ใช้สั้น ๆ:
- tree ของ docs ที่ได้
- สิ่งที่ย้าย/แก้ลิงก์
- **จุดที่โค้ดไม่ตรงกับ spec หรือเอกสารเดิม** แยกเป็น "ควรแก้" กับ "spec ล้าหลัง" (agent ทุกตัวต้องรายงานส่วนนี้)
- สิ่งที่ยังไม่ได้ตรวจ

commit เฉพาะเมื่อผู้ใช้สั่ง ถ้าอยู่บน branch หลักให้แตก branch ก่อน และแยก commit ของเอกสารออกจากงานอื่นที่ค้างอยู่

## อัปเดตเอกสารชุดเดิมหลัง merge

1. หา commit ล่าสุดที่แก้ `docs/architecture` (`git log -1 --format=%H -- docs/architecture`) แล้วดู `git diff --stat <commit>..HEAD`
2. จับคู่ไฟล์ที่เปลี่ยนกับหน้า (ใช้คอลัมน์ "ตัวจริงอยู่ที่" ในตารางของ `architecture/README.md`)
3. แก้เฉพาะหน้าที่ได้รับผลกระทบ แล้วตรวจตามขั้น 5
