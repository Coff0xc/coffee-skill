# coffee-skill Türkçe referans

## Nedir

`coffee-skill`, Codex için bir skill paketidir. Yazılım mühendisliği, AI Agent/RAG, API ve veri, UI ve dokümanlar, savunma odaklı güvenlik, tespit, olay müdahalesi ve zafiyet yönetimini kapsar.

## Neden var

- Çok fazla küçük skill otomatik tetiklemeyi güvenilmez hale getirir.
- Birçok istemci skill seçimini ağırlıkla `SKILL.md` içindeki frontmatter `name` ve `description` alanlarından yapar.
- Güvenlik iş akışları açık yetki ve savunma amaçlı kullanım sınırları ister.
- Gerçek işlerde genel tavsiyeden çok doğrulanabilir adımlar gerekir.

## Neden kullanılır

- 91 kaynak skill/workflow'u 17 kapsamlı yetenek skill'ine ve bir router'a indirger.
- Belirli bir skill tetiklenmezse `coff0xc-skill-router` fallback olarak çalışır.
- Her skill kapsam, hariçler, yetenek matrisi, iş akışı aşamaları, kanıt seviyeleri, sert kapılar, doğrulama ve anti-pattern içerir.
- Güvenlik içeriği yetkili savunma, tespit, sıkılaştırma, doğrulama ve raporlamaya odaklanır.

## Nasıl kullanılır

```text
Use coff0xc-ai-agent-rag to design a RAG Agent.
Use coff0xc-secure-code-appsec to review this project.
Use coff0xc-cloud-devsecops to review Kubernetes and CI/CD risk.
```

Otomatik tetikleme kaçırırsa:

```text
Use coff0xc-skill-router to choose the right skill.
```

## Nerede kullanılır

- Yerel Codex skill dizinleri.
- `SKILL.md` klasörlerini yükleyen uyumlu istemciler.
- Engineering, AI sistemleri, dokümantasyon, savunma güvenliği, tespit ve zafiyet yönetimi.

## Tetikleme başarısız olursa

1. Klasör adının frontmatter `name` ile aynı olduğunu kontrol edin.
2. Kopyaladıktan sonra Codex'i yeniden başlatın veya yenileyin.
3. Yinelenen skill adlarını kaldırın.
4. `coff0xc-skill-router`'ı açıkça çağırın.

## Güvenlik sınırı

Yalnızca sahip olduğunuz veya açıkça değerlendirme yetkiniz olan varlıklar, kod, log, örnek, lab ve eğitim ortamlarında kullanın. Yetkisiz erişim, kimlik bilgisi hırsızlığı, kalıcılık, kaçınma, C2, phishing toplama, veri sızdırma veya yıkıcı işlemler için kullanmayın.
