from typing import List, Optional
from pydantic import BaseModel, Field

class TaskTier(BaseModel):
    tier_name: str = Field(description="Tầng phân hóa: Cần hỗ trợ, Đạt chuẩn, Khá, Giỏi/Nâng cao")
    target_student_group: str = Field(description="Đối tượng học sinh hướng tới")
    pedagogical_scaffolding: str = Field(description="Mức độ trợ giúp / Giàn giáo học tập (Gợi ý, hình ảnh trực quan, câu hỏi mồi...)")
    task_prompt: str = Field(description="Đề bài / Nhiệm vụ học tập cụ thể")
    expected_output: str = Field(description="Sản phẩm kỳ vọng học sinh hoàn thành")
    bloom_level: str = Field(description="Cấp độ tư duy Bloom (Nhận biết, Thông hiểu, Vận dụng, Vận dụng cao/Sáng tạo)")

class DifferentiatedTaskSet(BaseModel):
    grade: str = Field(description="Khối lớp (Lớp 1 - 5)")
    subject: str = Field(description="Môn học")
    topic: str = Field(description="Chủ đề / Đơn vị kiến thức")
    core_competency: str = Field(description="Yêu cầu cần đạt cốt lõi theo CTGDPT 2018")
    tiers: List[TaskTier] = Field(description="4 tầng nhiệm vụ phân hóa")
    creative_challenge: Optional[str] = Field(None, description="Thử thách sáng tạo liên môn / STEM mở rộng")
