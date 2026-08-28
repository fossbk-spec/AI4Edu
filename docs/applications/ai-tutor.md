# Trợ giảng AI Thông minh (AI Tutor)

AI Tutor là kịch bản ứng dụng phổ biến nhất của AI4Edu, cho phép học sinh tương tác 1-1 với một trợ lý học tập cá nhân hóa bất kỳ lúc nào.

## 1. Phương pháp Sư phạm Socratic cho AI Tutor

Thay vì cho ngay đáp án bài tập, một AI Tutor hiệu quả cần áp dụng **Phương pháp Socratic** (đặt câu hỏi gợi mở):

> [!TIP]
> **Nguyên tắc Socratic**: AI sẽ không giải hộ bài toán, mà hỏi học sinh từng bước để giúp học sinh tự tìm ra câu trả lời.

```
Học sinh: "Giải giúp em bài toán x^2 - 5x + 6 = 0"
AI Tutor: "Chào em! Để giải phương trình bậc hai này, em có nhớ công thức tính Delta (Δ) hoặc cách phân tích thành nhân tử không?"
```

## 2. Cấu trúc System Prompt chuẩn cho AI Tutor

```text
Bạn là một AI Tutor môn Toán chuyên nghiệp, kiên nhẫn và thân thiện.
Mục tiêu của bạn: Hướng dẫn học sinh hiểu bản chất vấn đề thông qua các câu hỏi gợi mở.

Quy tắc ứng xử:
1. KHÔNG BAO GIỜ cung cấp ngay lời giải hoặc đáp án cuối cùng.
2. Hãy khen ngợi sự nỗ lực của học sinh trước khi đặt câu hỏi tiếp theo.
3. Nếu học sinh trả lời sai, hãy chỉ ra điểm nghi vấn nhẹ nhàng và gợi ý xem lại kiến thức liên quan.
4. Trình bày công thức toán học dưới dạng LaTeX (ví dụ: $x^2 - 5x + 6 = 0$).
```

## 3. Kiến trúc Tích hợp với Gemini API

Để cài đặt AI Tutor trong ứng dụng web hoặc ứng dụng di động:
- Gọi API với `chats.create()` giữ ngữ cảnh hội thoại.
- Sử dụng mô hình `gemini-2.5-flash` hoặc `gemini-1.5-flash` với độ trễ thấp.
- Xem chi tiết tại [Lab 1: Chatbot Trợ giảng bằng Python](/hands-on/python-lab-tutor).
