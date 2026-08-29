from typing import List, Optional
from pydantic import BaseModel, Field

class SubjectInfo(BaseModel):
    id: str = Field(description="Mã định danh môn học, ví dụ: math, natural_sciences, literature")
    name: str = Field(description="Tên môn học tiếng Việt, ví dụ: Toán học, Khoa học Tự nhiên")
    key_competencies: List[str] = Field(default_factory=list, description="Các chuẩn năng lực cốt lõi theo CTGDPT 2018")

class GradeInfo(BaseModel):
    id: str = Field(description="Mã định danh khối lớp, ví dụ: grade_1, grade_6")
    grade_number: int = Field(description="Số khối lớp (1-12)")
    level: str = Field(description="Cấp học: primary, lower_secondary, upper_secondary")
    name: str = Field(description="Tên khối lớp tiếng Việt, ví dụ: Khối Lớp 6")
    cognitive_stage: str = Field(description="Giai đoạn phát triển nhận thức theo tâm lý học lứa tuổi")
    tone_guideline: str = Field(description="Hướng dẫn ngữ khí và phương pháp tiếp cận AI phù hợp")
    subjects: List[SubjectInfo] = Field(default_factory=list, description="Danh sách môn học của khối lớp")

class EducationLevelInfo(BaseModel):
    id: str
    name: str
    grades: List[int]
    age_range: str
    pedagogical_focus: str

class CurriculumMatrix(BaseModel):
    levels: List[EducationLevelInfo]
    grades: List[GradeInfo]
