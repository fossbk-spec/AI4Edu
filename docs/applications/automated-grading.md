# Chấm điểm & Nhận xét Tự động (Automated Assessment)

AI có thể hỗ trợ giáo viên chấm bài tự luận, bài tập lập trình hoặc bài luận văn học bằng cách so sánh bài làm của học sinh với **Rubric chấm điểm** được định sẵn.

## 1. Quy trình Chấm bài & Phản hồi bằng AI

```
[Bài làm của Học sinh] + [Đáp án / Rubrics Chấm]
                        │
                        ▼
            [Mô hình Gemini Flash/Pro]
                        │
                        ▼
      ┌─────────────────────────────────┐
      │  • Điểm số dự kiến theo Rubric │
      │  • Ưu điểm bài làm              │
      │  • Nhược điểm & Lỗi sai         │
      │  • Gợi ý cải thiện cụ thể       │
      └─────────────────────────────────┘
```

## 2. Định dạng Đăng ký Structured Output (JSON)

Để hệ thống chấm bài hoạt động ổn định và tích hợp vào cơ sở dữ liệu, ta yêu cầu AI trả về kết quả dưới dạng JSON có cấu trúc (Structured Outputs):

```json
{
  "score": 8.5,
  "strengths": [
    "Lập luận logic, bố cục rõ ràng 3 phần",
    "Dẫn chứng thực tế phong phú"
  ],
  "weaknesses": [
    "Còn 2 lỗi chính tả ở đoạn 2",
    "Kết luận chưa mở rộng được vấn đề"
  ],
  "recommendations": "Nên bổ sung thêm liên hệ bản thân ở phần kết bài để đạt điểm tối đa."
}
```

Xem bài lab thực hành Python chi tiết tại [Lab 2: Hệ thống Chấm bài](/hands-on/python-lab-grading).
