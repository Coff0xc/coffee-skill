# coffee-skill referensi Bahasa Indonesia

## Apa ini

`coffee-skill` adalah paket skill untuk Codex. Paket ini mencakup software engineering, AI Agent/RAG, API dan data, UI dan dokumen, keamanan defensif, deteksi, respons insiden, dan manajemen kerentanan.

## Mengapa dibuat

- Terlalu banyak skill kecil membuat pemicu otomatis kurang andal.
- Banyak client memilih skill terutama dari frontmatter `name` dan `description` di `SKILL.md`.
- Workflow keamanan membutuhkan batas otorisasi dan penggunaan defensif yang jelas.
- Pekerjaan nyata membutuhkan langkah yang bisa diverifikasi, bukan hanya saran umum.

## Mengapa berguna

- Menggabungkan 91 skill/workflow sumber menjadi 17 skill kemampuan luas plus satu router.
- `coff0xc-skill-router` menjadi fallback saat skill tertentu tidak terpicu otomatis.
- Setiap skill berisi cakupan, pengecualian, matriks kemampuan, tahap kerja, level bukti, hard gate, validasi, dan anti-pattern.
- Konten keamanan tetap fokus pada defense, detection, hardening, verification, dan reporting yang terotorisasi.

## Cara menggunakan

```text
Use coff0xc-ai-agent-rag to design a RAG Agent.
Use coff0xc-secure-code-appsec to review this project.
Use coff0xc-detection-response to write detection rules.
```

Jika pemicu otomatis gagal:

```text
Use coff0xc-skill-router to choose the right skill.
```

## Di mana digunakan

- Direktori skill Codex lokal.
- Client kompatibel yang memuat folder `SKILL.md`.
- Engineering, sistem AI, dokumentasi, keamanan defensif, deteksi, dan manajemen kerentanan.

## Jika triggering gagal

1. Pastikan nama folder sama dengan frontmatter `name`.
2. Restart atau refresh Codex setelah menyalin.
3. Hapus nama skill duplikat.
4. Panggil `coff0xc-skill-router` secara eksplisit.

## Batas keamanan

Gunakan hanya pada aset, kode, log, sampel, lab, dan lingkungan pelatihan yang Anda miliki atau secara eksplisit diizinkan untuk dinilai. Jangan gunakan untuk akses tidak sah, pencurian kredensial, persistence, evasion, C2, pengumpulan phishing, eksfiltrasi data, atau tindakan destruktif.
