# coffee-skill tham khảo tiếng Việt

## Đây là gì

`coffee-skill` là một gói skill cho Codex. Nó bao phủ software engineering, AI Agent/RAG, API và dữ liệu, UI và tài liệu, an ninh phòng thủ, phát hiện, ứng phó sự cố và quản lý lỗ hổng.

## Vì sao có gói này

- Quá nhiều skill nhỏ làm việc tự động kích hoạt kém tin cậy.
- Nhiều client chọn skill chủ yếu từ frontmatter `name` và `description` trong `SKILL.md`.
- Workflow bảo mật cần ranh giới rõ ràng về ủy quyền và mục đích phòng thủ.
- Công việc thực tế cần các bước có thể xác minh, không chỉ lời khuyên chung chung.

## Vì sao nên dùng

- Hợp nhất 87 skill nguồn thành 15 skill năng lực toàn diện.
- `coff0xc-skill-router` là fallback khi một skill cụ thể không tự kích hoạt.
- Mỗi skill có phạm vi, loại trừ, ma trận năng lực, giai đoạn công việc, mức bằng chứng, hard gate, kiểm chứng và anti-pattern.
- Nội dung bảo mật tập trung vào phòng thủ được ủy quyền, phát hiện, hardening, xác minh và báo cáo.

## Cách dùng

```text
Use coff0xc-ai-agent-rag to design a RAG Agent.
Use coff0xc-secure-code-appsec to review this project.
Use coff0xc-cloud-devsecops to review Kubernetes and CI/CD risk.
```

Nếu tự động kích hoạt bị bỏ lỡ:

```text
Use coff0xc-skill-router to choose the right skill.
```

## Dùng ở đâu

- Thư mục skill Codex cục bộ.
- Client tương thích có thể tải thư mục `SKILL.md`.
- Engineering, hệ thống AI, tài liệu, an ninh phòng thủ, phát hiện và quản lý lỗ hổng.

## Khi trigger thất bại

1. Kiểm tra tên thư mục khớp với frontmatter `name`.
2. Khởi động lại hoặc refresh Codex sau khi copy.
3. Xóa tên skill trùng lặp.
4. Gọi rõ `coff0xc-skill-router`.

## Ranh giới an toàn

Chỉ dùng trên tài sản, code, log, mẫu, lab và môi trường đào tạo mà bạn sở hữu hoặc được ủy quyền rõ ràng để đánh giá. Không dùng cho truy cập trái phép, đánh cắp credential, persistence, evasion, C2, thu thập phishing, rò rỉ dữ liệu hoặc hành động phá hoại.
