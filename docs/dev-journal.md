# 📔 Nhật ký Phát triển & Bối cảnh Phiên làm việc (Dev Journal)

Tài liệu này ghi lại toàn bộ tiến độ, các quyết định kiến trúc, các tính năng đã hoàn thành và danh sách công việc tiếp theo để **đồng bộ bối cảnh giữa các máy tính và các phiên làm việc với AI**.

---

## 📅 Phiên làm việc: 28/08/2026

### 1. Trạng thái Hiện tại của Dự án
- **Repository**: [`fossbk-spec/AI4Edu`](https://github.com/fossbk-spec/AI4Edu.git) (Nhánh `main`)
- **Môi trường chạy**: Python 3.11+ / 3.13+, `google-genai` SDK v1+, VitePress 1.6+
- **Mô hình AI chuẩn**: **`gemini-3.7-flash`** (thay thế cho `gemini-2.5-flash` đã deprecated)

---

### 2. Các Hạng mục Đã Hoàn thành trong Phiên này

#### A. Hạ tầng & Môi trường Lập trình
- [x] Tạo và cấu hình môi trường ảo Python [`.venv`](file:///d:/Antigravity/AI4Edu/.venv) trên Windows.
- [x] Khắc phục lỗi `404 NOT_FOUND` bằng cách nâng cấp model sang `gemini-3.7-flash` cho:
  - [`scripts/gemini_client.py`](file:///d:/Antigravity/AI4Edu/scripts/gemini_client.py) (AI Tutor Socratic)
  - [`scripts/demo_lesson_plan.py`](file:///d:/Antigravity/AI4Edu/scripts/demo_lesson_plan.py) (Tạo giáo án 5E)
  - [`scripts/demo_auto_grader.py`](file:///d:/Antigravity/AI4Edu/scripts/demo_auto_grader.py) (Chấm bài Pydantic Structured Outputs)
- [x] Bổ sung cấu hình UTF-8 stream output tương thích với Windows PowerShell / Terminal.
- [x] Cấu hình phím tắt đồng bộ Git nhanh: **`gsave`** (`git add` + `git commit` kèm timestamp + `git push`) và **`gload`** (`git pull`).

#### B. Khối Tài liệu Phân cấp theo 5 Cấp học K-16 (`docs/education-levels/`)
- [x] [`index.md`](file:///d:/Antigravity/AI4Edu/docs/education-levels/index.md): Ma trận phân cấp ứng dụng AI (Mầm non $\rightarrow$ Đại học).
- [x] [`preschool.md`](file:///d:/Antigravity/AI4Edu/docs/education-levels/preschool.md): Giáo dục Mầm non (Kể chuyện tương tác, đa phương thức giọng nói/hình ảnh).
- [x] [`primary.md`](file:///d:/Antigravity/AI4Edu/docs/education-levels/primary.md): Cấp Tiểu học (Gamification, trợ lý đọc/toán, bài tập phân hóa 3 mức).
- [x] [`secondary.md`](file:///d:/Antigravity/AI4Edu/docs/education-levels/secondary.md): Cấp THCS (Tư duy Socratic môn KHTN, dự án STEM, chống chép bài giải).
- [x] [`high-school.md`](file:///d:/Antigravity/AI4Edu/docs/education-levels/high-school.md): Cấp THPT (Cá nhân hóa luyện thi tốt nghiệp, Debate AI phản biện, hướng nghiệp).
- [x] [`higher-education.md`](file:///d:/Antigravity/AI4Edu/docs/education-levels/higher-education.md): Đại học & Sau Đại học (Literature Review, RAG, thang đo 4 mức độ sử dụng AI).

#### C. Khối Tài liệu Phân loại theo Môn học & Ngành học
- [x] **4 Cụm Môn học Phổ thông K-12 (`docs/subjects-k12/`)**:
  - `math-computing.md`: Cụm Toán học & Tin học (Socratic giải toán, LaTeX, vẽ đồ thị, học code).
  - `natural-sciences.md`: Cụm Khoa học Tự nhiên (Mô phỏng thí nghiệm, cơ chế phản ứng, di truyền).
  - `social-humanities.md`: Cụm KH Xã hội & Nhân văn (Dàn ý Ngữ văn, đóng vai Lịch sử, số liệu Địa lý).
  - `languages.md`: Cụm Ngoại ngữ (Luyện nói 1-1, chấm Writing theo rubric IELTS/VSTEP).
- [x] **4 Khối Ngành Đại học (`docs/higher-ed-disciplines/`)**:
  - `engineering-tech.md`: Kỹ thuật & Công nghệ (Sinh Unit Test, Code Review, MATLAB/CAD).
  - `business-economics.md`: Kinh tế & Quản trị (Phân tích Báo cáo tài chính, Case studies, IMC).
  - `law-social-sciences.md`: Luật & Xã hội (Tra cứu án lệ, RAG học thuật, chống bịa đặt trích dẫn).
  - `medical-health.md`: Y - Dược & Sức khỏe (Bệnh nhân ảo, EBM/PICO, bảo mật bệnh án).

#### D. Tích hợp Thẩm định Khoa học & Đồng bộ Claude.ai
- [x] Bổ sung Mục 5 vào [`CLAUDE.md`](file:///d:/Antigravity/AI4Edu/CLAUDE.md): Tiêu chuẩn thẩm định sư phạm (5E, Bloom, Socratic, CTGDPT 2018).
- [x] Tạo script [`scripts/export_docs_for_claude.py`](file:///d:/Antigravity/AI4Edu/scripts/export_docs_for_claude.py): Gom toàn bộ tài liệu thành 1 file ngữ cảnh duy nhất tải lên Claude.

---

## 🎯 Kế hoạch Các bước Tiếp theo (Next Steps / Backlog)

1. [ ] **Thêm các mã nguồn thực hành Lab chuyên biệt**:
   - Lab chấm bài Writing tiếng Anh tự động theo rubric CEFR.
   - Lab sinh dữ liệu trắc nghiệm có giải thích phương án gây nhiễu.
2. [ ] **Xây dựng Giao diện Demo trực quan (Web UI / Streamlit / Next.js)** cho giáo viên trải nghiệm nhanh các tính năng AI Tutor và Soạn giáo án.
3. [ ] **Thẩm định & Kiểm thử Thực tế**: Sử dụng Claude.ai để rà soát tính chuẩn xác của các câu prompt chuyên ngành.
4. [ ] **Xuất bản Tài liệu Trực tuyến (CI/CD Deploy)** lên GitHub Pages / Vercel.

---

> 💡 **Hướng dẫn cho AI ở Phiên làm việc / Máy tính tiếp theo:**
> Hãy đọc file này cùng [`CLAUDE.md`](file:///d:/Antigravity/AI4Edu/CLAUDE.md) để nắm toàn bộ tiến độ, sau đó hỏi người dùng xem muốn tiếp tục triển khai hạng mục nào trong mục **Kế hoạch Tiếp theo**.
