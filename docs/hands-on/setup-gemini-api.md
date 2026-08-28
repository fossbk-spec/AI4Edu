# Hướng dẫn Cài đặt & Cấu hình Gemini API Key từ Google AI Studio

Để sử dụng các mô hình AI mới nhất của Google (như Gemini 2.5 Flash / Gemini 1.5 Pro) trong các công cụ AI4Edu, bạn cần lấy **API Key miễn phí** từ Google AI Studio và cấu hình vào dự án.

---

## 🔑 1. Các bước lấy Gemini API Key Miễn phí

Follow các bước đơn giản sau:

### Bước 1: Truy cập Google AI Studio
- Mở trình duyệt và truy cập: **[https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)**
- Đăng nhập bằng tài khoản **Google / Gmail** cá nhân hoặc tổ chức của bạn.

```
┌────────────────────────────────────────────────────────┐
│               Google AI Studio Dashboard               │
├────────────────────────────────────────────────────────┤
│  [ Create API key ]  <-- Nhấp vào nút này               │
│                                                        │
│  Project: Create API key in new project                │
└────────────────────────────────────────────────────────┘
```

### Bước 2: Tạo API Key mới
- Nhấp vào nút **"Get API key"** hoặc **"Create API key"**.
- Chọn **"Create API key in new project"** (Tạo API key trong dự án mới).
- Hệ thống sẽ tạo một chuỗi khóa bí mật bắt đầu bằng `AIzaSy...`.
- Nhấp nút **Copy** để sao chép API Key.

---

## ⚙️ 2. Cách thêm API Key vào Dự án AI4Edu

### Cách 1: Thêm vào file `.env` của dự án (Khuyên dùng)

1. Mở file `.env` tại thư mục gốc của dự án [`/Users/Admin/Desktop/Antigravity/AI4Edu`](file:///Users/Admin/Desktop/Antigravity/AI4Edu).  
   *(Nếu chưa có file `.env`, nhân bản từ `.env.example` bằng cách chạy `cp .env.example .env`)*.
2. Dán API Key của bạn vào dòng `GEMINI_API_KEY`:

```txt
# File: .env tại thư mục gốc /Users/Admin/Desktop/Antigravity/AI4Edu/.env
GEMINI_API_KEY=AIzaSyBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Cách 2: Thiết lập biến môi trường hệ thống (macOS / Linux Terminal)

Nếu muốn dùng API Key cho toàn bộ các script Python trong cửa sổ Terminal hiện tại:

```bash
export GEMINI_API_KEY="AIzaSyBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

---

## 🧪 3. Kiểm tra API Key đã hoạt động chưa

Chạy thử script kiểm tra kết nối AI Tutor trong thư mục `scripts/`:

```bash
python scripts/gemini_client.py
```


## 3. Kiểm tra Kết nối API bằng Python

Tạo file `test_connection.py`:

```python
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Xin chào! Hãy giới thiệu ngắn gọn về vai trò của Gemini trong giáo dục.',
)

print(response.text)
```

Chạy file:
```bash
python test_connection.py
```
