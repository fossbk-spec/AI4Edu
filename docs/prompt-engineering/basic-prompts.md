# Kỹ thuật Prompt Engineering Cơ bản cho Sư phạm

Prompt Engineering là nghệ thuật đặt câu hỏi và giao nhiệm vụ cho AI để nhận được kết quả chính xác, chất lượng cao nhất.

## 1. Công thức Prompt 5 Thành phần (CLEAR)

Để có câu trả lời tốt từ AI, hãy áp dụng khung **C-L-E-A-R**:

1. **C - Context (Ngữ cảnh)**: Đối tượng học sinh là ai? Lớp mấy? Trình độ nào?
2. **L - Logic (Vai trò)**: Đóng vai ai? (Ví dụ: "Bạn là giáo viên chuyên Sinh học THPT").
3. **E - Explicit Task (Nhiệm vụ rõ ràng)**: Yêu cầu AI làm gì cụ thể?
4. **A - Action Rules (Quy tắc hành động)**: Giới hạn từ ngữ, giọng văn, định dạng đầu ra.
5. **R - Result Format (Định dạng kết quả)**: Trả về Bảng, Markdown, JSON hay Bài văn?

---

## 2. Ví dụ So sánh Prompt Dở vs. Prompt Chuẩn

❌ **Prompt Dở**:
> "Hãy soạn cho tôi bài giảng về Hệ mặt trời."

✅ **Prompt Chuẩn (Theo chuẩn CLEAR)**:
> **Ngữ cảnh**: Tôi là giáo viên Khoa học tự nhiên lớp 6. Học sinh rất thích hình ảnh và hoạt động trải nghiệm.  
> **Vai trò**: Hãy đóng vai một chuyên gia giáo dục STEM xuất sắc.  
> **Nhiệm vụ**: Soạn kế hoạch bài dạy 45 phút chủ đề "Hệ Mặt Trời và các Hành tinh".  
> **Quy tắc**: Giọng văn hào hứng, bao gồm 1 trò chơi đóng vai 10 phút, không dùng thuật ngữ quá phức tạp.  
> **Định dạng**: Trình bày dưới dạng bảng Markdown gồm 4 cột: Thời gian, Hoạt động Giáo viên, Hoạt động Học sinh, Thiết bị cần thiết.
