# 🎓 AI4Edu Hub - Bộ Tài Liệu & Mã Nguồn Ứng Dụng AI Trong Giáo Dục

Dự án này là bộ tài nguyên mở giúp các nhà giáo dục, nghiên cứu sinh và lập trình viên thiết lập môi trường, nghiên cứu kịch bản và phát triển ứng dụng **Trí tuệ Nhân tạo (AI) trong Giáo dục**.

---

## 📁 Cấu trúc Dự án

```
AI4Edu/
├── docs/                        # Trang tin & Bộ tài liệu VitePress
│   ├── index.md                 # Trang chủ Hub
│   ├── overview/                # Tổng quan, Tầm nhìn, Đạo đức AI & Roadmap
│   ├── applications/            # Kịch bản ứng dụng (AI Tutor, Soạn giáo án, Chấm bài)
│   ├── prompt-engineering/      # Thư viện Prompt mẫu chuẩn Sư phạm
│   └── hands-on/                # Bài lab hướng dẫn lập trình với SDK
├── scripts/                     # Mã nguồn Python & AI Tools
│   ├── requirements.txt         # Danh sách thư viện Python
│   ├── gemini_client.py         # Demo AI Tutor tương tác CLI (Socratic method)
│   ├── demo_lesson_plan.py      # Tự động sinh giáo án 5E
│   └── demo_auto_grader.py      # Chấm bài tự luận (Structured Outputs JSON)
├── package.json                 # Cấu hình VitePress Documentation Engine
├── .env.example                 # Mẫu cấu hình API Key
└── README.md
```

---

## 🚀 1. Hướng dẫn Thiết lập Môi trường

### Bước 1: Khởi động Trang Web Tài liệu (VitePress Hub)
```bash
# 1. Cài đặt các gói phụ thuộc Node.js
npm install

# 2. Chạy môi trường xem trước tài liệu (Dev Server)
npm run docs:dev
```
Sau đó truy cập địa chỉ `http://localhost:5173` trên trình duyệt để xem trang tài liệu.

### Bước 2: Thiết lập Môi trường Lập trình Python & Gemini API
```bash
# 1. Cài đặt các thư viện Python cần thiết
pip install -r scripts/requirements.txt

# 2. Tạo file cấu hình môi trường .env
cp .env.example .env

# 3. Mở file .env và điền Gemini API Key lấy từ Google AI Studio:
# GEMINI_API_KEY=AIzaSy...
```

---

## 💻 2. Chạy thử các Bài Lab AI Giáo dục

### Lab 1: Thử nghiệm Chatbot AI Tutor (Phương pháp Socratic)
```bash
python scripts/gemini_client.py
```

### Lab 2: Tự động Sinh Giáo án chuẩn STEM 5E
```bash
python scripts/demo_lesson_plan.py
```

### Lab 3: Hệ thống Chấm bài Tự luận & Nhận xét Tự động (JSON Structured Output)
```bash
python scripts/demo_auto_grader.py
```

---

## 🛡️ Đạo đức & An toàn Dữ liệu
- **Không gửi thông tin cá nhân của học sinh** (tên thật, địa chỉ, ID) lên API public.
- **Human-in-the-loop**: Giáo viên luôn là người thẩm định và đưa ra quyết định cuối cùng.
