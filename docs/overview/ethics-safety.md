# Đạo đức & An toàn AI trong Giáo dục (AI Ethics & Safety)

Khi ứng dụng AI trong môi trường sư phạm, yếu tố đạo đức và bảo mật dữ liệu phải được đặt lên hàng đầu.

## 1. Các Nguyên tắc Đạo đức Cốt lõi

> [!IMPORTANT]
> **Con người là trung tâm (Human-in-the-loop)**: AI chỉ đóng vai trò trợ lý hỗ trợ. Quyết định chuyên môn, chấm điểm chung cuộc và đánh giá học sinh luôn thuộc về Giáo viên.

1. **Bảo mật Thông tin Học sinh (Data Privacy)**:
   - Không nhập tên đầy đủ, mã số định danh, địa chỉ hoặc dữ liệu nhạy cảm của học sinh vào các mô hình AI công cộng.
   - Sử dụng các kỹ thuật ẩn danh (Anonymization) trước khi xử lý dữ liệu qua API.

2. **Chống Sai lệch & Định kiến (Bias & Fairness)**:
   - Các mô hình AI có thể mang định kiến văn hóa hoặc giới tính từ dữ liệu huấn luyện.
   - Giáo viên cần thẩm định lại câu trả lời của AI trước khi phổ biến tới học sinh.

3. **Tính Minh bạch (Transparency)**:
   - Học sinh và giáo viên cần biết rõ khi nào một tài liệu hoặc phản hồi được tạo ra bởi AI.
   - Khuyến khích học sinh ghi rõ nguồn và cách thức sử dụng AI trong bài làm.

## 2. Phòng chống Ảo giác AI (Hallucination Management)

Nhiều mô hình AI có thể đưa ra thông tin trông rất thuyết phục nhưng thực chất là sai sự thật (hallucination).

### Biện pháp xử lý:
- Sử dụng phương pháp **RAG (Retrieval-Augmented Generation)**: Cung cấp tài liệu giáo trình chuẩn làm ngữ cảnh (Context) để AI chỉ trả lời dựa trên tài liệu đó.
- Cấu hình tham số `temperature` thấp (ví dụ: `temperature = 0.2`) khi yêu cầu AI tạo thông tin thực tế hoặc bài tập toán học.
