# Ứng dụng AI trong Khối Kỹ thuật & Công nghệ

Khối Kỹ thuật & Công nghệ (CNTT, Cơ kỹ thuật, Điện - Điện tử, Xây dựng, Khoa học Máy tính) là nơi sinh viên và giảng viên vừa là **người sử dụng AI**, vừa là **người phát triển các ứng dụng AI**.

---

## ⚙️ 1. Các Kịch bản Ứng dụng Trọng tâm

### 1.1. Trợ lý Lập trình & Kỹ thuật Phần mềm (Software Engineering)
- **Hỗ trợ Thiết kế Kiến trúc Hệ thống**: Tạo sơ đồ cơ sở dữ liệu (ERD), sơ đồ luồng dữ liệu (Dataflow Diagram) và định nghĩa API Endpoints (Swagger / OpenAPI).
- **Tự động sinh Unit Test & Kiểm thử Tự động**: Viết các bộ test case bao phủ các trường hợp biên (Edge cases) bằng pytest, Jest, JUnit.
- **Tối ưu Hiệu năng & Rà soát Lỗ hổng Bảo mật (Code Review)**: Phát hiện lỗi SQL Injection, tràn bộ nhớ (Buffer Overflow), rò rỉ bộ nhớ (Memory Leaks).

**Ví dụ Prompt sinh Unit Test bằng Python:**
```text
Hãy viết bộ Unit Test toàn diện bằng pytest cho hàm sau:
Hàm xử lý việc tính điểm trung bình và phân loại học lực học sinh, có kiểm tra dữ liệu đầu vào hợp lệ (điểm từ 0 đến 10, không nhận chuỗi rỗng).
Bao gồm: Test trường hợp hợp lệ, test giá trị biên (0.0, 10.0), test ngoại lệ TypeError và ValueError.
```

### 1.2. Tính toán Khoa học, Mô phỏng & Tối ưu hóa (Scientific Computing)
- Sinh mã nguồn xử lý tín hiệu số, ma trận và đạo hàm riêng trong MATLAB / Python NumPy.
- Hỗ trợ viết script tự động hóa thiết kế trong AutoCAD / FreeCAD / SolidWorks qua Python API.

### 1.3. Khoa học Dữ liệu & Học máy (Data Science & Machine Learning)
- Làm sạch và tiền xử lý dữ liệu lớn (Pandas / PySpark).
- Giải thích kết quả phân tích thống kê và huấn luyện mô hình dự báo.

---

## 🛡️ 2. Đổi mới Đánh giá trong Đào tạo Kỹ thuật

> [!IMPORTANT]
> Khi sinh viên có thể dùng AI để sinh code trong vài giây, **cách đánh giá lập trình truyền thống (chấm điểm code nộp) đã lỗi thời**.

1. **Chuyển sang Đánh giá Vấn đáp & Debug Trực tiếp**: Yêu cầu sinh viên giải thích luồng thực thi, tại sao chọn cấu trúc dữ liệu đó và yêu cầu sửa trực tiếp một bug phát sinh tại phòng thi.
2. **Đánh giá Khả năng Thiết kế & Tích hợp**: Tập trung vào tư duy kiến trúc hệ thống lớn, khả năng kết nối nhiều module phức tạp thay vì viết từng hàm nhỏ lẻ.
