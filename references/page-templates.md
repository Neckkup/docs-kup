# แม่แบบของแต่ละหน้า

หัวข้อในแต่ละแม่แบบเป็นจุดเริ่ม ตัดหัวข้อที่ระบบไม่มีออก ห้ามเขียน "ไม่มี" หรือ "n/a" ทิ้งไว้

## README.md (root ของ repo)

หน้าแรกที่คนเปิด repo เห็น ใช้โครงนี้ตามลำดับ และไม่มีลิงก์ย้อนกลับ

````markdown
# <ชื่อโปรเจกต์>

<ระบบทำอะไร ใครใช้ ขอบเขตตอนนี้ 1–2 ประโยค>

## Tech Stack

| ส่วน | เทคโนโลยี |
|------|-----------|
| Frontend | <framework + major version>, <library หลัก 2–4 ตัว> |
| Backend | <ภาษา/framework + major version>, <DB access, migration, คิว> |
| Database / Storage | ... |
| Infrastructure | <compose/orchestrator, reverse proxy, ที่ deploy> |
| CI/CD | ... |
| Testing | ... |

## Overview

เริ่มรันบนเครื่องใหม่:

```bash
<คำสั่งเรียงตามลำดับที่รันได้จริง>
```

| Service | URL |
|---------|-----|
| ... | http://localhost:... |

<บัญชี login ของเครื่องพัฒนา (ถ้ามี) + bullet ข้อควรรู้ 3–7 ข้อ: อัปเดต/ปิด stack, hot reload, พอร์ตที่ต้องว่าง, สเปกเครื่อง, ข้อจำกัดของ platform>

### คำสั่งพัฒนาแยกส่วน

**Backend** (`/backend`):
```bash
<คำสั่ง>   # <ทำอะไร>
```

**Frontend** (`/frontend`):
```bash
<คำสั่ง>   # <ทำอะไร>
```

**Database**:
```bash
<migrate / generate / seed>   # <ทำอะไร>
```

### โครงสร้างโปรเจค

```
├── backend/                  # <อะไร> (port ...)
│   ├── <โฟลเดอร์>/           # <หน้าที่>
│   ...
├── frontend/                 # <อะไร> (port ...)
│   ...
├── docs/                     # เอกสารของโปรเจค
├── docker-compose*.yml       # <ใช้ที่ไหน>
└── <CI config>               # <ทำอะไร>
```

## เอกสารประกอบ

| เอกสาร | คำอธิบาย |
|--------|---------|
| [Architecture](docs/architecture/README.md) | ภาพรวมระบบ (เริ่มอ่านที่นี่) + หน้า 01–0N |
| [Backend Docs](docs/backend/README.md) | คู่มือพัฒนา backend |
| [Frontend Docs](docs/frontend/README.md) | คู่มือพัฒนา frontend |
| [CI/CD Pipeline](docs/ci-cd.md) | pipeline และการ deploy |
| ... | ops, direction, constitution, reference ตามที่มีจริง |

ดูเอกสารทั้งหมดได้ที่ [`docs/`](docs/README.md)
````

- Tech Stack ในหน้านี้ใส่แค่ major version ต่อแถวเดียว รายละเอียด minor และ "กำหนดที่" อยู่ใน `architecture/README.md`
- คำสั่งและ URL อ่านจาก Makefile, package.json, compose จริง ตัดส่วนที่ repo ไม่มี (เช่น ไม่มี frontend → ไม่มีบล็อก Frontend)
- โครงสร้างโปรเจคลงลึก 2–3 ชั้น เฉพาะโฟลเดอร์ที่คนต้องรู้ ไม่ลิสต์ทุกไฟล์
- เอกสารที่ยังไม่เสร็จต่อท้ายคำอธิบายว่า *(อยู่ระหว่างจัดทำ)*

## docs/README.md

```markdown
# เอกสารของ <project>

ถ้าเพิ่งเข้ามาในโปรเจกต์ ให้เริ่มอ่านที่ [architecture/](architecture/README.md)

## สารบัญ

| เอกสาร | เนื้อหา |
|---|---|
| [architecture/](architecture/README.md) | ภาพรวมระบบ และการทำงานภายในทีละเรื่อง |
| [backend/](backend/README.md) | คู่มือพัฒนา backend |
| [frontend/](frontend/README.md) | คู่มือพัฒนา frontend |
| [ci-cd.md](ci-cd.md) | pipeline และการ deploy |
| [ops/](ops/...) | ... |
| [reference/](reference/README.md) | ความรู้ภายนอกที่ใช้อ้างอิง |

## วิธีดูแล architecture/, backend/ และ frontend/

- **อัปเดตใน MR เดียวกับฟีเจอร์:** ...
- **ไม่คัดลอกรายการยาวจากโค้ด:** ...
- **ป้ายความมั่นใจ:** [โค้ด] / [อนุมาน]
```

## architecture/README.md

1. ประโยคนำ: หน้านี้เป็นภาพรวมว่าระบบตอนนี้ประกอบขึ้นอย่างไร ใช้อะไรสร้าง ข้อมูลวิ่งอย่างไร เหตุผลอยู่ที่ไหน การ deploy อยู่ที่ไหน
2. `## ภาพรวมระบบ`
   - ระบบทำอะไร ใครใช้ ขอบเขตตอนนี้ (เช่น มีกี่โมดูล) 2–3 ประโยค
   - mermaid `graph LR` ของ container: ผู้ใช้ → ingress → frontend/api → DB/storage/คิว/อีเมล ใส่เฉพาะสิ่งที่ compose หรือ deploy จริงมี
   - ตาราง process `| process | รันด้วย | ทำอะไร |` รวมคำสั่ง admin/CLI ที่รันเอง
   - ตารางที่รัน `| ที่ | ไฟล์ | ต่างกันอย่างไร |` (dev แต่ละแบบ, staging, production)
   - bullet หลักใหญ่ 3–5 ข้อ แต่ละข้อลิงก์ไปหน้า 01–0N ที่ลงรายละเอียด
3. `## Tech Stack`: ตาราง `| ชั้น | เทคโนโลยี | เวอร์ชัน | กำหนดที่ |`
   - อ่านเวอร์ชันจาก manifest จริง (go.mod, package.json, Dockerfile, compose, CI) ห้ามเขียนจากความจำ ใส่แค่ major.minor
   - ครอบคลุม frontend, runtime, backend, HTTP, ฐานข้อมูล, migration, คิว, ไฟล์, อีเมล, login ภายนอก, metrics, proxy, test, CI/CD เฉพาะที่มีจริง
   - คอลัมน์ "กำหนดที่" ลิงก์ไปไฟล์ ให้คนตรวจและอัปเดตได้
4. `## Data Flow`: `sequenceDiagram` 3–4 รูปของ flow หลัก แต่ละรูปมีประโยคนำ 1–2 ประโยคและลิงก์ไปหน้ารายละเอียด เลือกจากที่ระบบมีจริง เช่น
   - อ่าน/เขียนข้อมูล: browser → proxy → frontend → api → DB
   - login และ session
   - ไฟล์ (อัปโหลด/ดาวน์โหลด)
   - event หรือ job เบื้องหลัง → การแจ้งเตือน

   รูปในหน้านี้ใส่ participant 4–5 ตัว ขั้นละเอียดไว้ในหน้า 01–0N
5. `## หน้าในโฟลเดอร์นี้`: ตาราง `| หน้า | เนื้อหา | ตัวจริงอยู่ที่ |` ของหน้า 01–0N คอลัมน์สุดท้ายใช้ตอนอัปเดตเอกสารหลัง merge
6. บรรทัดท้าย: คู่มือพัฒนาอยู่ใน backend/ และ frontend/

## 01-modules.md

- ตารางโมดูลหรือแพ็กเกจหลัก: หน้าที่ 1 บรรทัด, เปิด-ปิดได้ไหม, ขึ้นกับอะไร
- กฎขอบเขต: อะไร import อะไรได้ และอะไรบังคับกฎนั้น (compiler, linter, script)
- mermaid กราฟการพึ่งพา
- process แต่ละตัวประกอบจากโมดูลอย่างไร (entrypoint, การ wire)
- แพ็กเกจกลางหรือ shared/lib

## 02-api.md

- mermaid `sequenceDiagram` จาก browser ถึง DB
- ชั้นที่ request ผ่าน: frontend → proxy (ลิงก์ ops/ci-cd ไม่เขียนซ้ำ) → server → middleware ตามลำดับจริง (ตาราง) → handler → service → data access
- ตัวจริงของ endpoint (OpenAPI, router) และอะไรตรวจว่าโค้ดตรงกับมัน
- รูปแบบ error, pagination, validation
- การแยก tenant หรือการกรองข้อมูลต่อผู้ใช้ (ถ้ามี)

## 03-auth.md

- วิธี login ที่มีจริง (ตาราง)
- session หรือ token: เก็บที่ไหน อายุ การหมุน การเพิกถอน
- role และ permission: รูปแบบชื่อ ที่ลงทะเบียน (ยกตัวอย่าง ไม่ลิสต์ทั้งหมด)
- จุดที่ตรวจสิทธิ์ และ mermaid flowchart ของการตรวจ
- consent, PDPA, audit log (ถ้ามี)

## 04-database.md

- convention ก่อน: schema, รูปแบบ id, เวลา, soft delete, การแยก tenant (RLS หรือ filter), FK ข้ามโมดูล
- migration: เครื่องมือ, ที่อยู่ไฟล์, ลำดับ, วิธีเพิ่มไฟล์ใหม่
- เครื่องมือ generate โค้ดจาก SQL หรือ ORM
- ต่อโมดูล: `erDiagram` เล็ก ๆ + bullet 2–4 ข้อ + ลิงก์ไปโฟลเดอร์ migration
- ผู้ใช้ฐานข้อมูล: ลิงก์ไป ops ไม่เขียนซ้ำ

## 05-events-jobs.md

- กลไกคิว: ตัวไหน, insert ใน transaction ไหม, retry
- ตารางตัวอย่างว่าใครส่ง event อะไร ใครรับ
- worker: คิวที่รับ, concurrency, ตัววัด
- งานตามเวลา: ตารางตัวอย่าง, การกันรันซ้ำหลายเครื่อง
- การแจ้งเตือน: ช่องทาง, template, ตัวตรวจ

## 06-frontend.md

- stack และหลักการ (เช่น แสดงผลอย่างเดียว)
- route/layout/guard (ตาราง) และ mermaid route → layout → api
- การเรียก api: client ที่ generate, server vs client, cookie, error
- i18n, offline, อุปกรณ์พิเศษ (ถ้ามี)
- design system: ลิงก์ DESIGN.md
- การทดสอบ

## backend/README.md และ frontend/README.md (คู่มือพัฒนา)

1. ประโยคนำ + ลิงก์ไป architecture
2. **เริ่มพัฒนา:** บล็อกคำสั่งเรียงตามลำดับที่รันได้จริงบนเครื่องใหม่ + URL ที่เปิดดู
3. **คำสั่ง:** ตาราง `| คำสั่ง | ทำอะไร |` จาก Makefile หรือ package.json
4. **งานที่ทำบ่อย:** เพิ่ม endpoint, migration, permission, หน้า, ข้อความแปล เป็นขั้นที่มีลำดับ
5. **อ่านต่อ:** ตาราง `| หัวข้อ | หน้า |`

## ci-cd.md

- stack หรือ service ที่ deploy (ตาราง: อะไร, deploy โดยอะไร, ต้องมีอะไรให้ก่อน)
- เส้นทางของ domain/path
- pipeline: job ทีละตัว, เงื่อนไข trigger, อัตโนมัติหรือกดเอง
- CI/CD variables (ตาราง ชื่อ, ชนิด, ใช้ทำอะไร) ห้ามใส่ค่าจริง
- สิ่งที่ต้องเตรียมครั้งเดียว
- redeploy และ rollback
