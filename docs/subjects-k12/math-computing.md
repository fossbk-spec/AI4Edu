# Ứng dụng AI trong Cụm môn Toán học & Tin học

Cụm môn Toán học & Tin học đòi hỏi tính chính xác tuyệt đối, tư duy logic chặt chẽ và khả năng giải quyết vấn đề theo thuật toán.

---

## 📐 1. Ứng dụng trong Môn Toán học

### 1.1. Trợ giảng Socratic Giải Toán Từng bước
- AI đóng vai người gợi mở: Phát hiện học sinh vướng ở bước nào (ví dụ: biến đổi đại số sai, quên điều kiện xác định, áp dụng nhầm công thức) và đưa ra câu hỏi định hướng.

**Mẫu Prompt System cho AI Tutor Toán:**
```text
Bạn là gia sư môn Toán THPT. Khi học sinh gửi một bài toán:
1. KHÔNG BAO GIỜ giải bài toán từ đầu đến cuối ngay lập tức.
2. Hãy yêu cầu học sinh nêu ý tưởng hoặc bước biến đổi đầu tiên của mình.
3. Nếu học sinh biến đổi sai, hãy chỉ ra điểm nghi vấn và hỏi học sinh xem lại định lý/công thức liên quan.
4. Xuất công thức toán học dưới dạng chuẩn LaTeX (ví dụ: $f'(x) = 3x^2 - 6x$).
```

### 1.2. Sinh Đề thi có Tham số Biến thiên (Parametric Variations)
- Giáo viên có thể yêu cầu AI giữ nguyên bản chất tư duy của một câu hỏi khó nhưng thay đổi số liệu, hàm số hoặc bối cảnh hình học để tạo ra nhiều mã đề chống gian lận.

### 1.3. Sinh Mã nguồn Vẽ Hình học & Đồ thị
- Yêu cầu AI sinh mã nguồn TikZ / GeoGebra / Python Matplotlib để vẽ hình minh họa cho đề thi:
```text
Hãy viết mã Python dùng Matplotlib để vẽ đồ thị hàm số y = x^3 - 3x + 1 và tiếp tuyến của nó tại điểm có hoành độ x = 2. Có chú thích rõ các điểm cực trị và trục tọa độ.
```

---

## 💻 2. Ứng dụng trong Môn Tin học & Lập trình

### 2.1. Trợ lý Giải thích Lỗi Code (Debugging Assistant)
- Thay vì sửa lỗi hộ học sinh, AI hướng dẫn học sinh đọc thông báo lỗi (Traceback / Compilation Error) và đặt câu hỏi gợi ý cách khắc phục.

### 2.2. Học Lập trình Khối (Scratch) đến Lập trình Hướng đối tượng (Python/C++)
- Chuyển đổi ý tưởng thuật toán bằng lời nói tự nhiên thành sơ đồ khối hoặc mã giả (Pseudocode).
- Tạo các bài tập lập trình game mini vui nhộn phù hợp với lứa tuổi học sinh (Ví dụ: Game đoán số, Flappy Bird bằng Pygame).

### 2.3. Luyện thi Học sinh giỏi Tin học & Thuật toán
- Phân tích độ phức tạp thời gian $O(N)$ và không gian bộ nhớ của thuật toán.
- Gợi ý các trường hợp biên (Edge cases, Corner cases) để kiểm thử bộ test.
