# 📔 Nhật ký Phát triển & Bối cảnh Phiên làm việc (Dev Journal)

Tài liệu này ghi lại toàn bộ tiến độ, các quyết định kiến trúc, các tính năng đã hoàn thành và danh sách công việc tiếp theo để **đồng bộ bối cảnh giữa các máy tính và các phiên làm việc với AI**.

---

## 📅 Phiên làm việc: 29/08/2026 - Mở rộng Chuyên Trang Tiểu Học Hoàng Mai & Hệ Sinh Thái K-12

### 1. Trạng thái & Kiến trúc Mới
- **Chuyên Trang Cấp Tiểu Học - Trường Tiểu Học Hoàng Mai (`docs/hoang-mai-primary/`):** Xây dựng bộ cẩm nang 7 trụ cột năng lực AI chuyên biệt cho mô hình trường chất lượng cao & đổi mới sáng tạo, bám sát Công văn 2345/BGDĐT-GDTH và Thông tư 27/2020/TT-BGDĐT.
- **Quản lý phân cấp K-12 (CTGDPT 2018):** Triển khai đầy đủ 12 khối lớp (từ Lớp 1 đến Lớp 12), phân định rõ 3 cấp học (Tiểu học, THCS, THPT).
- **Core AI Engine (`ai4edu` Package):** Chuyển đổi toàn bộ mã nguồn script rời rạc thành Python Package module hóa hoàn chỉnh, cấu hình động qua `ai4edu/config/curriculum_matrix.yaml`.
- **Hỗ trợ Structured Outputs:** Tích hợp Pydantic v2 cho mô hình `LessonPlan2345`, `PrimaryAssessmentTT27`, `DifferentiatedTaskSet`, `LessonPlan5E`, `AssessmentResult`.
- **Giao diện dòng lệnh (`ai4edu.cli`):** Cung cấp các sub-commands chuyên biệt: `list-grades`, `plan`, `plan-2345`, `differentiate`, `review-tt27`, `tutor`, `grade`.

---

### 2. Các Hạng mục Đã Hoàn thành trong Phiên này

#### A. Chuyên Trang Tiểu Học Hoàng Mai (`docs/hoang-mai-primary/`)
- [x] [`index.md`](file:///c:/Antigravity/AI4Edu/docs/hoang-mai-primary/index.md): Cẩm nang tổng quan 7 trụ cột năng lực AI trường Hoàng Mai.
- [x] [`lesson-planning-2345.md`](file:///c:/Antigravity/AI4Edu/docs/hoang-mai-primary/lesson-planning-2345.md): Hướng dẫn & Prompt Soạn KHBD 5 cột (CV 2345) và Chatbot đóng vai nhân vật ảo.
- [x] [`differentiation-advanced.md`](file:///c:/Antigravity/AI4Edu/docs/hoang-mai-primary/differentiation-advanced.md): Phân hóa 4 tầng nhiệm vụ (Hỗ trợ - Chuẩn - Khá - Giỏi) và bài toán nhiều cách giải cho trường CLC.
- [x] [`assessment-tt27.md`](file:///c:/Antigravity/AI4Edu/docs/hoang-mai-primary/assessment-tt27.md): Đánh giá & Nhận xét học sinh chuẩn Thông tư 27/2020 + Quy tắc ẩn danh dữ liệu Excel (De-identification).
- [x] [`digital-toolchain.md`](file:///c:/Antigravity/AI4Edu/docs/hoang-mai-primary/digital-toolchain.md): Quy trình phối hợp công cụ số: `AI` $\rightarrow$ `Canva/Gamma` $\rightarrow$ `Quizizz/Wordwall` $\rightarrow$ `Excel` $\rightarrow$ `AI`.
- [x] [`stem-ai-literacy.md`](file:///c:/Antigravity/AI4Edu/docs/hoang-mai-primary/stem-ai-literacy.md): Dự án STEM/STEAM phân bổ 5 khối lớp & Giáo dục năng lực số (AI Literacy) cho trẻ em.
- [x] [`prompt-engineering.md`](file:///c:/Antigravity/AI4Edu/docs/hoang-mai-primary/prompt-engineering.md): Kỹ thuật Prompt Chaining & Tạo Trợ lý AI riêng cho từng Tổ chuyên môn (Khối 1 $\rightarrow$ Khối 5).

#### B. Khối Tài liệu K-12 (`docs/curriculum/`)
- [x] Ma trận 12 khối lớp K-12 (`curriculum/index.md`).
- [x] Cấp Tiểu học Lớp 1 - 5 (`curriculum/primary/`).
- [x] Cấp THCS Lớp 6 - 9 (`curriculum/lower-secondary/`).
- [x] Cấp THPT Lớp 10 - 12 (`curriculum/upper-secondary/`).

#### C. Xây dựng Package Python `ai4edu` & CLI
- [x] `ai4edu/models/`: `lesson_plan_2345.py`, `primary_assessment.py`, `differentiated_task.py`, `curriculum.py`, `lesson_plan.py`, `assessment.py`.
- [x] `ai4edu/services/`: `hoang_mai_service.py`, `lesson_planner.py`, `ai_tutor.py`, `auto_grader.py`.
- [x] `ai4edu/cli.py`: Hỗ trợ đầy đủ lệnh dòng lệnh cho giáo viên tiểu học.

---

## 🎯 Kế hoạch Các bước Tiếp theo (Next Steps / Backlog)

1. [ ] **Xây dựng Giao diện Web App (Streamlit / Next.js)**: Cho phép giáo viên trường Hoàng Mai chọn Khối lớp từ dropdown menu và trực tiếp sử dụng AI Tutor / Soạn bài giảng 2345 trực quan.
2. [ ] **Tích hợp RAG (Retrieval-Augmented Generation)**: Nạp tài liệu Sách giáo khoa (Kết nối tri thức, Chân trời sáng tạo, Cánh diều) vào Vector Store.
3. [ ] **Xuất bản Tài liệu Trực tuyến (GitHub Pages / Vercel)**.
