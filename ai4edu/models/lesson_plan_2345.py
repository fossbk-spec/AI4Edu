from typing import List, Optional
from pydantic import BaseModel, Field

class Step2345(BaseModel):
    step_number: int = Field(description="Bước (1: Chuyển giao, 2: Thực hiện, 3: Báo cáo/Thảo luận, 4: Kết luận/Nhận định)")
    step_name: str = Field(description="Tên bước tổ chức thực hiện")
    teacher_action: str = Field(description="Hành động của giáo viên")
    student_action: str = Field(description="Hành động và nhiệm vụ của học sinh")

class Activity2345(BaseModel):
    activity_name: str = Field(description="Tên hoạt động (Khởi động, Khám phá, Luyện tập, Vận dụng)")
    objective: str = Field(description="Mục tiêu của hoạt động (Kiến thức, Năng lực, Phẩm chất)")
    content: str = Field(description="Nội dung hoạt động / Nhiệm vụ giao cho học sinh")
    product: str = Field(description="Sản phẩm học tập của học sinh (câu trả lời, vở ghi, phiếu học tập...)")
    implementation_steps: List[Step2345] = Field(description="4 bước tổ chức thực hiện theo CV 2345")
    advanced_extension: Optional[str] = Field(None, description="Nhiệm vụ mở rộng / thử thách nâng cao cho học sinh khá giỏi")

class LessonPlan2345(BaseModel):
    school_name: str = Field(default="Trường Tiểu học Hoàng Mai", description="Tên trường")
    grade: str = Field(description="Khối lớp (Lớp 1 - Lớp 5)")
    subject: str = Field(description="Môn học")
    lesson_title: str = Field(description="Tên bài học")
    duration_periods: int = Field(default=1, description="Số tiết học")
    required_competencies: List[str] = Field(description="Yêu cầu cần đạt (YCKĐN) về phẩm chất và năng lực")
    teaching_equipment: List[str] = Field(description="Đồ dùng dạy học, thiết bị số và học liệu AI")
    activities: List[Activity2345] = Field(description="Các hoạt động học theo cấu trúc 5 cột")
    differentiation_notes: str = Field(description="Ghi chú phân hóa đối tượng và hỗ trợ cá nhân hóa")
