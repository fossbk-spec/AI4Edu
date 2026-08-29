from typing import List, Optional
from pydantic import BaseModel, Field

class SubjectEvaluation(BaseModel):
    subject_name: str = Field(description="Tên môn học đánh giá")
    level: str = Field(description="Mức độ đạt được: Hoàn thành tốt (T), Hoàn thành (H), Chưa hoàn thành (C)")
    strengths: str = Field(description="Điểm nổi bật, tiến bộ rõ nét")
    improvements: str = Field(description="Điểm cần rèn luyện thêm và biện pháp hỗ trợ cụ thể")

class CoreCompetencyEvaluation(BaseModel):
    competency_name: str = Field(description="Tên năng lực (Tự chủ và tự học, Giao tiếp và hợp tác, Giải quyết vấn đề và sáng tạo)")
    level: str = Field(description="Mức độ: Tốt (T), Đạt (Đ), Cần cố gắng (C)")
    specific_evidence: str = Field(description="Biểu hiện hành vi cụ thể trong các hoạt động học tập")

class PrimaryQualityEvaluation(BaseModel):
    quality_name: str = Field(description="Tên phẩm chất (Yêu nước, Nhân ái, Chăm chỉ, Trung thực, Trách nhiệm)")
    level: str = Field(description="Mức độ: Tốt (T), Đạt (Đ), Cần cố gắng (C)")
    specific_evidence: str = Field(description="Biểu hiện hành vi trong lớp và sinh hoạt tập thể")

class PrimaryAssessmentTT27(BaseModel):
    student_alias: str = Field(description="Mã ẩn danh học sinh (vd: HS01, HS_A) để bảo mật dữ liệu")
    grade: str = Field(description="Khối lớp (Lớp 1 - 5)")
    school: str = Field(default="Trường Tiểu học Hoàng Mai", description="Tên trường")
    evaluation_period: str = Field(description="Giai đoạn đánh giá: Giữa kì I, Cuối kì I, Giữa kì II, Cuối năm")
    subject_evaluations: List[SubjectEvaluation] = Field(description="Đánh giá môn học theo Thông tư 27")
    competency_evaluations: List[CoreCompetencyEvaluation] = Field(description="Đánh giá năng lực cốt lõi")
    quality_evaluations: List[PrimaryQualityEvaluation] = Field(description="Đánh giá phẩm chất chủ yếu")
    general_comment_for_parents: str = Field(description="Lời nhận xét tổng hợp gửi phụ huynh (tích cực, cụ thể, có tính xây dựng)")
    suggested_personalized_tasks: List[str] = Field(description="Các nhiệm vụ ôn tập / mở rộng gợi ý cho học sinh")
