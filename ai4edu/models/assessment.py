from typing import List, Optional
from pydantic import BaseModel, Field

class RubricCriterion(BaseModel):
    criterion_name: str = Field(description="Tên tiêu chí đánh giá")
    weight_percentage: float = Field(description="Trọng số phần trăm của tiêu chí (ví dụ: 30%)")
    score_achieved: float = Field(description="Điểm số đạt được")
    max_score: float = Field(description="Điểm tối đa của tiêu chí")
    feedback: str = Field(description="Nhận xét chi tiết theo tiêu chí này")

class AssessmentResult(BaseModel):
    submission_id: Optional[str] = Field(None, description="Mã bài nộp nếu có")
    student_grade: str = Field(description="Khối lớp của học sinh")
    subject: str = Field(description="Môn học")
    overall_score: float = Field(description="Tổng điểm bài làm trên thang 10")
    general_comment: str = Field(description="Lời nhận xét tổng quát mang tính khích lệ và định hình")
    strengths: List[str] = Field(description="Những điểm làm tốt của học sinh")
    areas_for_improvement: List[str] = Field(description="Những điểm cần khắc phục và cải thiện")
    criteria_breakdown: List[RubricCriterion] = Field(default_factory=list, description="Bảng điểm chi tiết theo rubric")
    suggested_next_steps: List[str] = Field(description="Các bài tập hoặc tài liệu gợi ý học thêm")
