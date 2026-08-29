from typing import Optional
from google.genai import types
from ai4edu.core.client import get_genai_client, DEFAULT_MODEL
from ai4edu.core.prompt_engine import PromptEngine
from ai4edu.models.lesson_plan import LessonPlan5E

def generate_structured_lesson_plan(
    grade: int,
    subject: str,
    topic: str,
    duration_minutes: int = 45,
    model_name: str = DEFAULT_MODEL
) -> LessonPlan5E:
    """
    Sinh Kế hoạch bài dạy 5E dưới dạng Structured Output (Pydantic model)
    """
    engine = PromptEngine()
    grade_info = engine.get_grade(grade)
    if not grade_info:
        raise ValueError(f"Khối lớp không hợp lệ: {grade}. Hỗ trợ lớp 1 đến 12.")

    subject_info = engine.get_subject(grade_info, subject)
    if not subject_info:
        available = ", ".join([s.id for s in grade_info.subjects])
        raise ValueError(f"Môn học '{subject}' không tìm thấy ở {grade_info.name}. Các môn có sẵn: {available}")

    prompt = engine.build_lesson_plan_prompt(grade_info, subject_info, topic, duration_minutes)
    client = get_genai_client()

    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=LessonPlan5E,
            temperature=0.3,
        ),
    )

    return LessonPlan5E.model_validate_json(response.text)

def generate_markdown_lesson_plan(
    grade: int,
    subject: str,
    topic: str,
    duration_minutes: int = 45,
    model_name: str = DEFAULT_MODEL
) -> str:
    """
    Sinh Kế hoạch bài dạy 5E dưới dạng văn bản Markdown chuẩn
    """
    engine = PromptEngine()
    grade_info = engine.get_grade(grade)
    if not grade_info:
        raise ValueError(f"Khối lớp không hợp lệ: {grade}. Hỗ trợ lớp 1 đến 12.")

    subject_info = engine.get_subject(grade_info, subject)
    if not subject_info:
        available = ", ".join([s.id for s in grade_info.subjects])
        raise ValueError(f"Môn học '{subject}' không tìm thấy ở {grade_info.name}. Các môn có sẵn: {available}")

    prompt = engine.build_lesson_plan_prompt(grade_info, subject_info, topic, duration_minutes)
    prompt += "\n\nHãy xuất định dạng Markdown chi tiết, rõ ràng, có bảng biểu phân chia hoạt động GV - HS."
    
    client = get_genai_client()
    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.4,
        ),
    )
    return response.text
