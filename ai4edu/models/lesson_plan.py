from typing import List, Optional
from pydantic import BaseModel, Field

class Phase5E(BaseModel):
    name: str = Field(description="Tên giai đoạn 5E: Engage, Explore, Explain, Elaborate, Evaluate")
    duration_minutes: int = Field(description="Thời lượng ước tính (phút)")
    teacher_activities: List[str] = Field(description="Hoạt động của giáo viên")
    student_activities: List[str] = Field(description="Hoạt động của học sinh")
    ai_integration_tip: Optional[str] = Field(None, description="Gợi ý tích hợp công cụ AI hỗ trợ trong giai đoạn này")

class LessonPlan5E(BaseModel):
    title: str = Field(description="Tên bài học hoặc chủ đề giáo án")
    grade: str = Field(description="Khối lớp áp dụng, ví dụ: Lớp 6")
    subject: str = Field(description="Môn học, ví dụ: Khoa học Tự nhiên")
    objectives: List[str] = Field(description="Mục tiêu bài học theo phẩm chất và năng lực (YCKĐN)")
    prerequisites: List[str] = Field(default_factory=list, description="Kiến thức tiền đề học sinh cần có")
    materials_needed: List[str] = Field(default_factory=list, description="Thiết bị, đồ dùng dạy học hoặc tài liệu số")
    phases: List[Phase5E] = Field(description="Chi tiết 5 pha giảng dạy theo mô hình 5E")
    differentiation_notes: Optional[str] = Field(None, description="Ghi chú phân hóa dạy học cho học sinh yếu/khá giỏi")
