from typing import Optional, List, Dict, Any
from ai4edu.core.prompt_engine import PromptEngine
from ai4edu.core.llm_provider import UnifiedLLMClient
from ai4edu.data.math_curriculum import get_math_lessons
from ai4edu.data.vietnamese_curriculum import get_vietnamese_lessons
from ai4edu.data.math_grade3_textbook_content import get_textbook_lesson_detail
from ai4edu.models.lesson_plan_2345 import LessonPlan2345
from ai4edu.models.differentiated_task import DifferentiatedTaskSet
from ai4edu.models.primary_assessment import PrimaryAssessmentTT27

import re

def _find_curriculum_lesson(grade: int, subject: str, topic: str) -> Optional[Dict[str, Any]]:
    """Tìm thông tin bài học trong dữ liệu chuẩn SGK (Toán & Tiếng Việt Lớp 1-5) để cấp bối cảnh chính xác cho AI."""
    if not topic:
        return None
        
    subject_norm = subject.lower()
    if any(k in subject_norm for k in ["toán", "math"]):
        lessons = get_math_lessons(grade)
    elif any(k in subject_norm for k in ["tiếng việt", "vietnamese", "văn"]):
        lessons = get_vietnamese_lessons(grade)
    else:
        lessons = []

    if not lessons:
        return None

    topic_clean = topic.strip().lower()
    
    # 1. Match theo tiêu đề đầy đủ
    for l in lessons:
        title_clean = l["title"].strip().lower()
        if topic_clean in title_clean or title_clean in topic_clean:
            return l
            
    # 2. Match theo số thứ tự bài học với word boundary (ví dụ "Bài 20" không bao giờ nhầm với "Bài 2")
    sorted_lessons = sorted(lessons, key=lambda x: len(x["title"].split(":")[0]), reverse=True)
    for l in sorted_lessons:
        lesson_prefix = l["title"].split(":")[0].strip().lower() # "bài 20", "bài 2"
        pattern = r'\b' + re.escape(lesson_prefix) + r'\b'
        if re.search(pattern, topic_clean):
            return l
    return None

def generate_lesson_plan_2345(
    grade: int,
    subject: str,
    topic: str,
    advanced_focus: bool = True,
    llm_client: Optional[UnifiedLLMClient] = None
) -> LessonPlan2345:
    """
    Sinh Kế hoạch Bài dạy (KHBD) 5 cột chuẩn Công văn 2345/BGDĐT-GDTH cho Trường Tiểu học Hoàng Mai.
    Căn cứ chặt chẽ 100% vào Sách Giáo Khoa (Kết nối tri thức với cuộc sống).
    """
    engine = PromptEngine()
    grade_info = engine.get_grade(grade)
    if not grade_info or grade_info.level != "primary":
        raise ValueError(f"Khối lớp {grade} không thuộc Cấp Tiểu học (Hỗ trợ lớp 1 đến 5).")

    subject_info = engine.get_subject(grade_info, subject)
    subject_name = subject_info.name if subject_info else subject

    # Tìm thông tin SGK chính xác
    matched_lesson = _find_curriculum_lesson(grade, subject, topic)
    lesson_grounding = ""
    target_topic_title = topic
    if matched_lesson:
        target_topic_title = matched_lesson["title"]
        page_info = f" (Trang {matched_lesson.get('page')})" if 'page' in matched_lesson else ""
        lesson_grounding = f"""
CĂN CỨ BẮT BUỘC TỪ SÁCH GIÁO KHOA CHUẨN (KẾT NỐI TRI THỨC VỚI CUỘC SỐNG - NXB GIÁO DỤC VIỆT NAM):
- Khối lớp: Lớp {matched_lesson['grade']}
- Vị trí bài học: {matched_lesson['topic_group']}, Tập {matched_lesson['volume']}{page_info}
- TÊN BÀI HỌC CHÍNH XÁC: "{matched_lesson['title']}"
"""
        # Đính kèm nội dung trích xuất nguyên bản từ file SGK
        tb_detail = get_textbook_lesson_detail(grade, target_topic_title)
        if tb_detail:
            concepts_str = "\n".join([f"  + {c}" for c in tb_detail.get("original_concepts", [])])
            exercises_str = "\n".join([f"  + {e}" for e in tb_detail.get("original_exercises", [])])
            lesson_grounding += f"""
NỘI DUNG NGUYÊN VĂN TRÍCH TỪ SÁCH GIÁO KHOA ({tb_detail['page']}):
* Khái niệm, quy tắc và định nghĩa gốc:
{concepts_str}

* Hoạt động khám phá, ví dụ & bài tập gốc:
{exercises_str}
"""

        lesson_grounding += f"""
NGUYÊN TẮC CỐT LÕI (TUYỆT ĐỐI TUÂN THỦ):
1. Trường 'lesson_title' trong JSON kết quả BẮT BUỘC PHẢI LÀ: "{matched_lesson['title']}".
2. Nội dung các Hoạt động 1 (Khởi động), Hoạt động 2 (Khám phá), Hoạt động 3 (Luyện tập), Hoạt động 4 (Vận dụng) PHẢI CĂN CỨ VÀO ĐÚNG ĐƠN VỊ KIẾN THỨC VÀ BÀI TẬP TRÍCH DẪN TỪ SGK Ở TRÊN. 
   TUYỆT ĐỐI KHÔNG BỊA ĐẶT NỘI DUNG HOẶC NHẦM SANG BÀI HỌC KHÁC!
"""

    advanced_prompt = (
        "- ĐẶC BIỆT DÀNH CHO MÔ HÌNH TRƯỜNG CHẤT LƯỢNG CAO HOÀNG MAI: Thiết kế các câu hỏi mở, nhiệm vụ mở rộng/thử thách sáng tạo "
        "dành cho học sinh khá giỏi, tích hợp gợi ý học liệu số (Canva, Wordwall, Audio AI), giàn giáo tư duy phân hóa.\n"
        if advanced_focus else ""
    )

    prompt = f"""
Bạn là Chuyên gia Phương pháp Dạy học Tiểu học tại Trường Tiểu học Hoàng Mai (Mô hình Trường Chất lượng cao & Đổi mới sáng tạo).
Hãy xây dựng Kế hoạch bài dạy chuẩn theo đúng hướng dẫn của Công văn 2345/BGDĐT-GDTH cho:
- Trường: Trường Tiểu học Hoàng Mai
- Khối lớp: {grade_info.name} (Đặc điểm tâm lý: {grade_info.cognitive_stage})
- Môn học: {subject_name}
- Tên bài học / Chủ đề: {target_topic_title}
- Ngữ khí & Phương pháp: {grade_info.tone_guideline}

{lesson_grounding}
{advanced_prompt}

Yêu cầu cấu trúc Kế hoạch bài dạy 5 cột:
1. 'school_name': "Trường Tiểu học Hoàng Mai"
2. 'grade': "Khối Lớp {grade}"
3. 'subject': "{subject_name}"
4. 'lesson_title': "{target_topic_title}"
5. Yêu cầu cần đạt (YCKĐN) về Phẩm chất và Năng lực bám sát nội dung bài học.
6. Đồ dùng dạy học và thiết bị số.
7. 4 Hoạt động học (Khởi động, Khám phá, Luyện tập, Vận dụng). Mỗi hoạt động phải có:
   - Mục tiêu
   - Nội dung
   - Sản phẩm
   - Tổ chức thực hiện (Gồm đủ 4 bước: 1. Chuyển giao nhiệm vụ -> 2. Thực hiện nhiệm vụ -> 3. Báo cáo, thảo luận -> 4. Kết luận, nhận định)
   - Nhiệm vụ mở rộng cho học sinh khá giỏi.
8. Ghi chú phân hóa đối tượng.

Xuất kết quả định dạng JSON theo đúng schema LessonPlan2345.
"""

    client = llm_client or UnifiedLLMClient()
    return client.generate_structured(prompt=prompt, schema_cls=LessonPlan2345)


def generate_differentiated_taskset(
    grade: int,
    subject: str,
    topic: str,
    llm_client: Optional[UnifiedLLMClient] = None
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

    matched_lesson = _find_curriculum_lesson(grade, subject, topic)
    target_topic_title = matched_lesson["title"] if matched_lesson else topic

    prompt = f"""
Bạn là Chuyên gia Thiết kế Nhiệm vụ Học tập Phân hóa cho Trường Tiểu học Hoàng Mai.
Từ một chủ đề / đơn vị kiến thức, hãy xây dựng 4 tầng nhiệm vụ học tập phân hóa theo năng lực:
- Khối lớp: {grade_info.name}
- Môn học: {subject_name}
- Chủ đề / Bài học: {target_topic_title}

4 Tầng phân hóa bắt buộc:
1. Tầng 1 (Học sinh cần hỗ trợ): Nhiệm vụ có giàn giáo hỗ trợ tối đa (hình ảnh trực quan, mẫu câu, gợi ý từng bước).
2. Tầng 2 (Học sinh đạt chuẩn): Nhiệm vụ bám sát yêu cầu cần đạt cơ bản trong SGK của bài học này.
3. Tầng 3 (Học sinh khá): Nhiệm vụ yêu cầu vận dụng, kết hợp 2 bước suy luận hoặc tự liên hệ thực tế.
4. Tầng 4 (Học sinh giỏi / Nâng cao): Nhiệm vụ phát triển tư duy bậc cao (phản biện, giải quyết vấn đề, bài toán nhiều cách giải, sáng tạo).

Kèm theo 1 Thử thách sáng tạo liên môn / STEM mini.
Xuất kết quả định dạng JSON theo đúng schema DifferentiatedTaskSet.
"""

    client = llm_client or UnifiedLLMClient()
    return client.generate_structured(prompt=prompt, schema_cls=DifferentiatedTaskSet)


def generate_tt27_assessment(
    grade: int,
    subject: str,
    student_alias: str,
    evaluation_notes: str,
    period: str = "Cuối học kì I",
    llm_client: Optional[UnifiedLLMClient] = None
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
- Ghi chú thực tế của giáo viên: {evaluation_notes}

Yêu cầu xuất kết quả định dạng JSON theo đúng schema PrimaryAssessmentTT27 gồm:
1. Đánh giá Môn học & Hoạt động giáo dục (Mức Hoàn thành Tốt 'T' / Hoàn thành 'H' / Chưa hoàn thành 'C', nêu rõ điểm nổi bật và biện pháp hỗ trợ).
2. Đánh giá Năng lực chung & Năng lực đặc thù.
3. Đánh giá Phẩm chất chủ yếu (Yêu nước, Nhân ái, Chăm chỉ, Trung thực, Trách nhiệm).
4. Lời nhận xét tổng hợp gửi phụ huynh (tôn trọng, khích lệ, cụ thể).
5. Gợi ý 2-3 nhiệm vụ tự học cá nhân hóa.
"""

    client = llm_client or UnifiedLLMClient()
    return client.generate_structured(prompt=prompt, schema_cls=PrimaryAssessmentTT27)
