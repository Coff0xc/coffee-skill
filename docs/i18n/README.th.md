# coffee-skill เอกสารอ้างอิงภาษาไทย

## คืออะไร

`coffee-skill` คือชุด skill สำหรับ Codex ครอบคลุม software engineering, AI Agent/RAG, API และ data, UI/report output, Office/PDF file delivery, defensive security, detection, incident response และ vulnerability management

## ทำไมต้องมี

- Skill ขนาดเล็กจำนวนมากทำให้การ trigger อัตโนมัติไม่น่าเชื่อถือ
- Client หลายตัวเลือก skill จาก frontmatter `name` และ `description` ใน `SKILL.md`
- งาน security ต้องมีขอบเขต authorization และ defensive-use ที่ชัดเจน
- งานจริงต้องมีขั้นตอนที่ตรวจสอบได้ ไม่ใช่คำแนะนำทั่วไปเท่านั้น

## ดีอย่างไร

- รวม 91 source skills/workflows เป็น 17 capability skills และ router 1 ตัว
- `coff0xc-skill-router` เป็น fallback เมื่อ skill เฉพาะไม่ถูก trigger
- แต่ละ skill มี scope, exclusions, capability matrix, workflow phases, evidence levels, hard gates, validation checks และ anti-patterns
- เนื้อหา security เน้น authorized defense, detection, hardening, verification และ reporting

## วิธีใช้

```text
Use coff0xc-ai-agent-rag to design a RAG Agent.
Use coff0xc-secure-code-appsec to review this project.
Use coff0xc-detection-response to write detection rules.
```

ถ้า automatic trigger ไม่ทำงาน:

```text
Use coff0xc-skill-router to choose the right skill.
```

## ใช้ที่ไหน

- Local Codex skill directories
- Client ที่รองรับโฟลเดอร์ `SKILL.md`
- Engineering, AI systems, Office/document artifacts, defensive security, detection และ vulnerability management

## เมื่อ trigger ล้มเหลว

1. ตรวจว่า folder name ตรงกับ frontmatter `name`
2. Restart หรือ refresh Codex หลัง copy
3. ลบ skill names ที่ซ้ำกัน
4. เรียก `coff0xc-skill-router` โดยตรง

## ขอบเขตความปลอดภัย

ใช้เฉพาะกับ assets, code, logs, samples, labs และ training environments ที่คุณเป็นเจ้าของหรือได้รับอนุญาตชัดเจน ห้ามใช้เพื่อ unauthorized access, credential theft, persistence, evasion, C2, phishing collection, data exfiltration หรือ destructive actions
