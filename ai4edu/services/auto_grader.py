from typing import Optional, List
from google.genai import types
from ai4edu.core.client import get_genai_client, DEFAULT_MODEL
from ai4edu.core.prompt_engine import PromptEngine
from ai4edu.models.assessment import AssessmentResult

def grade_student_submission(
    grade: int,
    subject: str,
    assignment_prompt: str,
    student_work: str,
    rubric_guidelines: Optional[str] = None,
    model_name: str = DEFAULT_MODEL
) -> AssessmentResult:
    """
    Chấm bài và sinh phản hồi định hình (Formative Feedback) theo chuẩn Rubric và Pydantic Schema.
    """
    engine = PromptEngine()
    grade_info = engine.get_grade(grade)
    if not grade_info:
        raise ValueError(f"Khối lớp không hợp lệ: {grade}. Hỗ trợ lớp 1 đến 12.")

    subject_info = engine.get_subject(grade_info, subject)
    subject_name = subject_info.name if subject_info else subject

    rubric_text = rubric_guidelines or "Đánh giá theo 4 tiêu chuẩn: Độ chính xác kiến thức (40%), Tư duy lập luận (30%), Cách trình bày diễn đạt (20%), Tính sáng tạo/mở rộng (10%)."

    prompt = f"""
Bạn là Chuyên gia Khảo thí và Đánh giá Giáo dục cho cấp {grade_info.name} (Môn: {subject_name}).
Đặc điểm nhận thức lứa tuổi: {grade_info.cognitive_stage}
Ngữ khí đánh giá: {grade_info.tone_guideline}

ĐỀ BÀI:
{assignment_prompt}

HƯỚNG DẪN CHẤM / RUBRIC:
{rubric_text}

BÀI LÀM CỦA HỌC SINH:
{student_work}

Hãy đánh giá khách quan, chỉ rõ điểm mạnh, điểm cần cải thiện, điểm số chi tiết từng tiêu chí và đề xuất bước học tiếp theo.
Xuất kết quả định dạng JSON theo đúng schema quy định.
"""

    client = get_genai_client()
    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=AssessmentResult,
            temperature=0.2,
        ),
    )

    return AssessmentResult.model_validate_json(response.text)
