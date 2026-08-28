# Ứng dụng AI trong Khối Y - Dược & Khoa học Sức khỏe

Đào tạo Y khoa, Dược học và Khoa học Sức khỏe là lĩnh vực đặc biệt có tính rủi ro cao nhất, liên quan trực tiếp đến tính mạng con người. Việc ứng dụng AI phải tuân thủ nghiêm ngặt nguyên tắc **Y học dựa trên Bằng chứng (Evidence-Based Medicine - EBM)** và **Đạo đức Y sinh học**.

---

## 🩺 1. Các Kịch bản Ứng dụng trong Đào tạo Y - Dược

### 1.1. Mô phỏng Ca bệnh Lâm sàng (Virtual Patient Simulation)
- AI đóng vai bệnh nhân ảo (Virtual Standardized Patient) với đầy đủ bệnh sử, triệu chứng cơ năng, tâm lý lo âu.
- Sinh viên Y khoa thực hành kỹ năng hỏi bệnh sử (Anamnesis), đề xuất xét nghiệm cận lâm sàng (Lab tests, X-quang, CT/MRI) và lập luận chẩn đoán phân biệt (Differential Diagnosis).

**Ví dụ Prompt mô phỏng ca bệnh:**
```text
Hãy đóng vai một bệnh nhân nam 55 tuổi, tiền sử hút thuốc lá 20 năm, đến khám vì đau ngực trái âm ỉ lan ra vai.
- Hãy chỉ trả lời khi bác sĩ (người dùng) hỏi. Trả lời với giọng mệt mỏi, lo lắng.
- KHÔNG nói ra tên bệnh (như Nhồi máu cơ tim hay Trào ngược dạ dày), chỉ mô tả đúng cảm giác và hoàn cảnh xuất hiện cơn đau.
```

### 1.2. Tổng hợp Y văn & Phân tích Đánh giá Tổng quan (Systematic Review)
- Hỗ trợ sàng lọc tiêu đề và tóm tắt bài báo (Abstract screening) theo tiêu chuẩn PICO (Population, Intervention, Comparison, Outcome).
- Trích xuất dữ liệu thử nghiệm lâm sàng ngẫu nhiên có đối chứng (RCT) từ PubMed / Cochrane Library.

### 1.3. Dược lý học & Tương tác Thuốc (Pharmacology & Drug Interactions)
- Hỗ trợ tra cứu cơ chế tác dụng dược lý, chống chỉ định, liều dùng theo độ tuổi và các tương tác thuốc nguy hiểm (Drug-Drug Interactions).

---

## ⚠️ 2. Ranh giới Đạo đức & An toàn Y sinh Bắt buộc

> [!CAUTION]
> **AI chỉ là công cụ hỗ trợ học tập và mô phỏng, KHÔNG BAO GIỜ được thay thế chẩn đoán của Bác sĩ được cấp chứng chỉ hành nghề.**

```
┌─────────────────────────────────────────────────────────────┐
│                 NGUYÊN TẮC AN TOÀN Y TẾ & AI                 │
├─────────────────────────┬───────────────────────────────────┤
│ 1. Không dùng dữ liệu thật│ Xóa sạch thông tin định danh (HIPAA)│
│ 2. Giám sát chuyên môn   │ Luôn có Bác sĩ giảng viên thẩm định│
│ 3. Tránh tự chẩn đoán   │ Ghi chú cảnh báo pháp lý y khoa   │
└─────────────────────────┴───────────────────────────────────┘
```

1. **Bảo mật Dữ liệu Bệnh nhân Tuyệt đối (De-identification)**: Nghiêm cấm tải lên AI bất kỳ thông tin bệnh án thực tế nào có chứa tên tuổi, mã số bệnh nhân, hình ảnh khuôn mặt hoặc số CCCD.
2. **Cảnh báo Trách nhiệm Pháp lý**: Mọi nội dung thảo luận y khoa trên môi trường học tập phải đính kèm thông báo: *"Dành riêng cho mục đích đào tạo y khoa, không dùng làm phác đồ điều trị trực tiếp trên người bệnh."*
