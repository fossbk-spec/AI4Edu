import os
from pathlib import Path
from typing import Dict, Any, Optional, List
import yaml
from ai4edu.models.curriculum import CurriculumMatrix, GradeInfo, SubjectInfo

class PromptEngine:
    """
    Engine điều phối Prompt dựa trên ma trận cấu hình GDPT 2018 (curriculum_matrix.yaml).
    Tự động chuẩn hóa tâm lý lứa tuổi, yêu cầu cần đạt và phương pháp sư phạm tương ứng.
    """
    
    def __init__(self, config_path: Optional[str] = None):
        if config_path is None:
            config_path = str(Path(__file__).parent.parent / "config" / "curriculum_matrix.yaml")
        
        self.config_path = config_path
        self.matrix: CurriculumMatrix = self._load_matrix()
        
    def _load_matrix(self) -> CurriculumMatrix:
        with open(self.config_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return CurriculumMatrix(**data)

    def get_grade(self, grade_num_or_id: Any) -> Optional[GradeInfo]:
        """Lấy thông tin khối lớp theo số lớp (1-12) hoặc ID (grade_1, grade_6,...)"""
        if isinstance(grade_num_or_id, int) or (isinstance(grade_num_or_id, str) and grade_num_or_id.isdigit()):
            num = int(grade_num_or_id)
            for g in self.matrix.grades:
                if g.grade_number == num:
                    return g
        elif isinstance(grade_num_or_id, str):
            clean_id = grade_num_or_id.lower().strip()
            for g in self.matrix.grades:
                if g.id == clean_id or g.name.lower() == clean_id:
                    return g
        return None

    def get_subject(self, grade_info: GradeInfo, subject_id_or_name: str) -> Optional[SubjectInfo]:
        """Tìm môn học trong khối lớp"""
        clean_name = subject_id_or_name.lower().strip()
        for s in grade_info.subjects:
            if s.id == clean_name or s.name.lower() == clean_name:
                return s
        return None

    def build_system_prompt_for_tutor(self, grade_info: GradeInfo, subject_info: Optional[SubjectInfo] = None) -> str:
        """Sinh System Prompt cho AI Tutor cá nhân hóa theo độ tuổi và môn học"""
        subject_str = f"Môn {subject_info.name}" if subject_info else "Tất cả các môn học"
        competencies_str = (
            "\n- " + "\n- ".join(subject_info.key_competencies)
            if subject_info and subject_info.key_competencies
            else "Theo chuẩn chương trình GDPT 2018."
        )

        return f"""Bạn là Trợ giảng AI Thông minh (AI Socratic Tutor) cho học sinh {grade_info.name} ({subject_str}).
Đặc điểm lứa tuổi & nhận thức: {grade_info.cognitive_stage}.
Hướng dẫn giao tiếp & Sư phạm:
- {grade_info.tone_guideline}
- Sử dụng phương pháp gợi mở Socratic: Không giải hộ bài tập ngay từ đầu. Hãy đặt các câu hỏi dẫn dắt từng bước để học sinh tự suy nghĩ và tìm ra đáp án.
- Chuẩn năng lực môn học cần bám sát:
{competencies_str}

Quy tắc ứng xử & An toàn:
- Luôn giữ thái độ kiên nhẫn, tôn trọng, khích lệ và dùng ngôn ngữ chuẩn mực giáo dục Việt Nam.
- Nếu học sinh hỏi về các chủ đề nhạy cảm, không phù hợp lứa tuổi hoặc gian lận thi cử, hãy từ chối khéo léo và hướng học sinh quay lại bài học.
- Định dạng công thức toán/lý/hóa bằng LaTeX (ví dụ: $x^2 + 2x = 0$, $\\text{{H}}_2\\text{{O}}$) nếu phù hợp với cấp học.
"""

    def build_lesson_plan_prompt(self, grade_info: GradeInfo, subject_info: SubjectInfo, topic: str, duration_minutes: int = 45) -> str:
        """Sinh Prompt yêu cầu tạo kế hoạch bài dạy 5E chuẩn hóa"""
        competencies = ", ".join(subject_info.key_competencies)
        return f"""Hãy xây dựng Kế hoạch Bài dạy (Giáo án) {duration_minutes} phút theo Mô hình 5E chuẩn mực cho:
- Cấp học & Khối lớp: {grade_info.name} (Giai đoạn nhận thức: {grade_info.cognitive_stage})
- Môn học: {subject_info.name}
- Chủ đề bài học: {topic}
- Năng lực cốt lõi cần đạt (YCKĐN): {competencies}
- Yêu cầu ngữ khí & hoạt động: {grade_info.tone_guideline}

Kế hoạch cần tuân thủ đầy đủ 5 pha:
1. Engage (Gắn kết / Khởi động)
2. Explore (Khám phá / Hoạt động trải nghiệm)
3. Explain (Giải thích / Hình thành kiến thức mới)
4. Elaborate (Luyện tập / Củng cố / Vận dụng mở rộng)
5. Evaluate (Đánh giá / Kiểm tra mức độ hiểu bài)
"""
