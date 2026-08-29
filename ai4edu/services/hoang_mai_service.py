from typing import Optional, List, Dict, Any
from google.genai import types
from ai4edu.core.client import get_genai_client, DEFAULT_MODEL
from ai4edu.core.prompt_engine import PromptEngine
from ai4edu.models.lesson_plan_2345 import LessonPlan2345
from ai4edu.models.differentiated_task import DifferentiatedTaskSet
from ai4edu.models.primary_assessment import PrimaryAssessmentTT27

def generate_lesson_plan_2345(
    grade: int,
    subject: str,
    topic: str,
    advanced_focus: bool = True,
    model_name: str = DEFAULT_MODEL
) -> LessonPlan2345:
    """
    Sinh Kế hoạch Bài dạy (KHBD) 5 cột chuẩn Công văn 2345/BGDĐT-GDTH cho Trường Tiểu học Hoàng Mai.
    Bao gồm 4 hoạt động (Khởi động, Khám phá, Luyện tập, Vận dụng) với 4 bước tổ chức thực hiện và nhiệm vụ mở rộng.
    """
    engine = PromptEngine()
    grade_info = engine.get_grade(grade)
    if not grade_info or grade_info.level != "primary":
        raise ValueError(f"Khối lớp {grade} không thuộc Cấp Tiểu học (Hỗ trợ lớp 1 đến 5).")

    subject_info = engine.get_subject(grade_info, subject)
    subject_name = subject_info.name if subject_info else subject

    advanced_prompt = (
        "- ĐẶC BIỆT DÀNH CHO MÔ HÒ TRƯỜNG CHẤT LƯỢNG CAO HOÀNG MAI: Thiết kế các câu hỏi mở, nhiệm vụ mở rộng/thử thách sáng tạo "
        "dành cho học sinh khá giỏi, tránh lặp lại nguyên bản nội dung SGK, tích hợp gợi ý học liệu số (Canva, Wordwall, Audio AI).\n"
        if advanced_focus else ""
    )

    prompt = f"""
Bạn là Chuyên gia Phương pháp Dạy học Tiểu học tại Trường Tiểu học Hoàng Mai (Mô hình Trường Chất lượng cao & Đổi mới sáng tạo).
Hãy xây dựng Kế hoạch bài dạy chuẩn theo đúng hướng dẫn của Công văn 2345/BGDĐT-GDTH cho:
- Trường: Trường Tiểu học Hoàng Mai
- Khối lớp: {grade_info.name} (Đặc điểm tâm lý: {grade_info.cognitive_stage})
- Môn học: {subject_name}
- Tên bài học / Chủ đề: {topic}
- Ngữ khí & Phương pháp: {grade_info.tone_guideline}
{advanced_prompt}

Yêu cầu cấu trúc Kế hoạch bài dạy 5 cột:
1. Yêu cầu cần đạt (YCKĐN) về Phẩm chất và Năng lực.
2. Đồ dùng dạy học và thiết bị số.
3. 4 Hoạt động học (Khởi động, Khám phá, Luyện tập, Vận dụng). Mỗi hoạt động phải có:
   - Mục tiêu
   - Nội dung
   - Sản phẩm
   - Tổ chức thực hiện (Gồm đủ 4 bước: 1. Chuyển giao nhiệm vụ -> 2. Thực hiện nhiệm vụ -> 3. Báo cáo, thảo luận -> 4. Kết luận, nhận định)
   - Nhiệm vụ mở rộng cho học sinh khá giỏi.
4. Ghi chú phân hóa đối tượng.

Xuất kết quả định dạng JSON theo đúng schema LessonPlan2345.
"""

    client = get_genai_client()
    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=LessonPlan2345,
            temperature=0.3,
        ),
    )

    return LessonPlan2345.model_validate_json(response.text)


def generate_differentiated_taskset(
    grade: int,
    subject: str,
    topic: str,
    model_name: str = DEFAULT_MODEL
) -> DifferentiatedTaskSet:
    """
    Sinh 4 mức độ nhiệm vụ phân hóa (Cần hỗ trợ, Đạt chuẩn, Khá, Giỏi/Nâng cao) từ 1 đơn vị kiến thức.
    """
    engine = PromptEngine()
    grade_info = engine.get_grade(grade)
    if not grade_info or grade_info.level != "primary":
        raise ValueError(f"Khối lớp {grade} không thuộc Cấp Tiểu học (Lớp 1-5).")

    subject_info = engine.get_subject(grade_info, subject)
    subject_name = subject_info.name if subject_info else subject

    prompt = f"""
Bạn là Chuyên gia Thiết kế Nhiệm vụ Học tập Phân hóa cho Trường Tiểu học Hoàng Mai.
Từ một chủ đề / đơn vị kiến thức, hãy xây dựng 4 tầng nhiệm vụ học tập phân hóa theo năng lực:
- Khối lớp: {grade_info.name}
- Môn học: {subject_name}
- Chủ đề: {topic}

4 Tầng phân hóa bắt buộc:
1. Tầng 1 (Học sinh cần hỗ trợ): Nhiệm vụ có giàn giáo hỗ trợ tối đa (hình ảnh trực quan, mẫu câu, gợi ý từng bước).
2. Tầng 2 (Học sinh đạt chuẩn): Nhiệm vụ bám sát yêu cầu cần đạt cơ bản trong SGK.
3. Tầng 3 (Học sinh khá): Nhiệm vụ yêu cầu vận dụng, kết hợp 2 bước suy luận hoặc tự liên hệ thực tế.
4. Tầng 4 (Học sinh giỏi / Nâng cao): Nhiệm vụ phát triển tư duy bậc cao (phản biện, giải quyết vấn đề, bài toán nhiều cách giải, sáng tạo).

Kèm theo 1 Thử thách sáng tạo liên môn / STEM mini.
Xuất kết quả định dạng JSON theo đúng schema DifferentiatedTaskSet.
"""

    client = get_genai_client()
    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=DifferentiatedTaskSet,
            temperature=0.3,
        ),
    )

    return DifferentiatedTaskSet.model_validate_json(response.text)


def generate_tt27_assessment(
    grade: int,
    subject: str,
    student_alias: str,
    evaluation_notes: str,
    period: str = "Cuối học kì I",
    model_name: str = DEFAULT_MODEL
) -> PrimaryAssessmentTT27:
    """
    Sinh nhận xét học sinh tiểu học chuẩn Thông tư 27/2020/TT-BGDĐT.
    """
    engine = PromptEngine()
    grade_info = engine.get_grade(grade)
    grade_name = grade_info.name if grade_info else f"Khối Lớp {grade}"

    prompt = f"""
Bạn là Giáo viên Chủ nhiệm & Giáo viên Bộ môn tại Trường Tiểu học Hoàng Mai.
Hãy hỗ trợ viết nhận xét đánh giá học sinh chuẩn mực theo đúng Thông tư 27/2020/TT-BGDĐT:
- Học sinh: {student_alias} (Đã ẩn danh)
- Khối lớp: {grade_name}
- Môn học: {subject}
- Đợt đánh giá: {period}
- Ghi chú quá trình học tập thực tế của giáo viên:
{evaluation_notes}

Yêu cầu theo Thông tư 27/2020:
1. Đánh giá Môn học: Chỉ rõ mức đạt (T/H/C), điểm nổi bật và biện pháp hỗ trợ/rèn luyện cụ thể, tránh nhận xét chung chung.
2. Đánh giá Năng lực cốt lõi: Tự chủ - tự học, Giao tiếp - hợp tác, Giải quyết vấn đề & sáng tạo kèm biểu hiện cụ thể.
3. Đánh giá Phẩm chất chủ yếu: Yêu nước, Nhân ái, Chăm chỉ, Trung thực, Trách nhiệm.
4. Lời nhận xét gửi phụ huynh: Thân thiện, tôn trọng, mang tính khích lệ và định hướng hành động rõ ràng.
5. Gợi ý 2-3 nhiệm vụ tự học cá nhân hóa.

Xuất kết quả định dạng JSON theo đúng schema PrimaryAssessmentTT27.
"""

    client = get_genai_client()
    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=PrimaryAssessmentTT27,
            temperature=0.3,
        ),
    )

    return PrimaryAssessmentTT27.model_validate_json(response.text)
