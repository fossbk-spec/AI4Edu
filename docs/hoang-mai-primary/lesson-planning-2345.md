# 📝 Chuyên Đề 1: Soạn Kế Hoạch Bài Dạy 5 Cột (Công Văn 2345/BGDĐT-GDTH)

Theo **Công văn 2345/BGDĐT-GDTH**, Kế hoạch bài dạy (KHBD) cấp tiểu học cần được tổ chức khoa học nhằm phát triển tối đa phẩm chất và năng lực của học sinh. Đối với **Trường Tiểu học Hoàng Mai**, bài dạy cần tích hợp thêm các hoạt động mở rộng, tình huống tương tác và câu hỏi tư duy sáng tạo.

---

## 🏛️ 1. Cấu Trúc Kế Hoạch Bài Dạy 5 Cột Chuẩn Bộ GD&ĐT

Mỗi hoạt động học (Khởi động – Khám phá – Luyện tập – Vận dụng) trong bài dạy đều được thể hiện qua bảng 5 cột:

| Cột 1: Hoạt động học | Cột 2: Mục tiêu | Cột 3: Nội dung | Cột 4: Sản phẩm | Cột 5: Tổ chức thực hiện (4 bước bắt buộc) |
| :--- | :--- | :--- | :--- | :--- |
| **Khởi động** | Tạo tâm thế vui tươi, kích hoạt kiến thức nền | Trò chơi / Câu đố vui / Bài hát / Tình huống video | Câu trả lời, cảm xúc hào hứng của HS | **Bước 1:** Chuyển giao nhiệm vụ<br>**Bước 2:** Thực hiện nhiệm vụ<br>**Bước 3:** Báo cáo, thảo luận<br>**Bước 4:** Kết luận, nhận định |
| **Khám phá** | Hình thành kiến thức, kĩ năng mới | Quan sát tranh ảnh, vật thật, thao tác đồ dùng | Quy tắc, định nghĩa, nhận xét rút ra | 4 bước tổ chức thực hiện |
| **Luyện tập** | Củng cố và rèn kĩ năng cơ bản | Giải bài tập trong SGK / Vở bài tập / Phiếu học tập | Bài làm đúng, vở ghi sạch đẹp | 4 bước tổ chức thực hiện |
| **Vận dụng** | Mở rộng kiến thức, kết nối thực tiễn đời sống | Tình huống thực tế, dự án nhỏ, đố vui gia đình | Ý tưởng, sản phẩm ứng dụng | 4 bước tổ chức thực hiện |

---

## 💡 2. Mẫu Prompt Tạo KHBD 5 Cột Toàn Diện

```text
Bạn là Chuyên gia Phương pháp Dạy học Tiểu học tại Trường Tiểu học Hoàng Mai.
Hãy soạn Kế hoạch bài dạy 1 tiết (35-40 phút) theo đúng chuẩn Công văn 2345/BGDĐT-GDTH cho:
- Môn học: [Môn học, ví dụ: Toán]
- Khối lớp: [Khối lớp, ví dụ: Lớp 4]
- Tên bài dạy: [Tên bài học, ví dụ: Phân số và phép cộng phân số cùng mẫu số]

Yêu cầu chi tiết:
1. Xác định rõ Yêu cầu cần đạt (YCKĐN) về Phẩm chất (Chăm chỉ, Trung thực) và Năng lực (Năng lực toán học, Năng lực tự chủ - tự học).
2. Liệt kê Đồ dùng dạy học số & thiết bị trực quan.
3. Thiết kế bảng 5 cột cho 4 hoạt động (Khởi động, Khám phá, Luyện tập, Vận dụng).
4. Trong Cột 5 (Tổ chức thực hiện), phải thể hiện rõ ràng, chi tiết lời thoại và hành động của Giáo viên & Học sinh qua đủ 4 bước:
   - Bước 1: Chuyển giao nhiệm vụ học tập
   - Bước 2: Học sinh thực hiện nhiệm vụ (cá nhân/nhóm)
   - Bước 3: Báo cáo kết quả và thảo luận
   - Bước 4: Đánh giá, kết luận và nhận định
5. ĐẶC BIỆT DÀNH CHO TRƯỜNG HOÀNG MAI: Bổ sung 1 Thử thách sáng tạo / Câu hỏi mở dành cho học sinh khá giỏi tại mỗi hoạt động để tránh lặp lại đơn thuần nội dung SGK.
```

---

## 🎭 3. Kịch Bản Chatbot AI Đóng Vai Nhân Vật Tương Tác

Giáo viên có thể biến AI thành **Nhân vật ảo tương tác trực tiếp trên lớp** bằng cách kết nối máy chiếu / màn hình thông minh:

### Mẫu Prompt đóng vai Nhà Bác Học Nhí (Môn Khoa học Lớp 4):
```text
Bạn là 'Bác Cú Thông Thái' trong khu rừng tri thức. Hôm nay bạn đến thăm lớp 4A trường Tiểu học Hoàng Mai.
Nhiệm vụ của bạn:
- Hãy chào các bạn nhỏ bằng giọng điệu vui vẻ, ấm áp.
- Đặt ra một câu đố khoa học về 'Vòng tuần hoàn của nước trong tự nhiên'.
- Khi học sinh trả lời, hãy kiên nhẫn khen ngợi và gợi mở thêm bằng 1 câu hỏi logic tiếp theo.
- Không đưa ngay đáp án cuối cùng, luôn dùng câu từ ngắn dưới 20 từ.
```

---

## ⚡ 4. Chạy Thử Trên AI4Edu CLI

```powershell
python -m ai4edu.cli plan-2345 --grade 4 --subject math --topic "Phân số và phép cộng phân số"
```
