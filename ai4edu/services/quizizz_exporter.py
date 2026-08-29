import io
from typing import List, Optional
import pandas as pd
from pydantic import BaseModel, Field
from ai4edu.core.prompt_engine import PromptEngine
from ai4edu.core.llm_provider import UnifiedLLMClient

class QuizQuestion(BaseModel):
    question: str = Field(description="Nội dung câu hỏi đố vui")
    option1: str = Field(description="Phương án A")
    option2: str = Field(description="Phương án B")
    option3: str = Field(description="Phương án C")
    option4: str = Field(description="Phương án D")
    correct_option_number: int = Field(description="Số thứ tự đáp án đúng (1, 2, 3 hoặc 4)")
    time_in_seconds: int = Field(default=30, description="Thời gian làm bài tính bằng giây (30 hoặc 45)")
    explanation: str = Field(description="Giải thích ngắn gọn, vui vẻ vì sao đáp án đó đúng")

class QuizSet(BaseModel):
    title: str = Field(description="Tên bộ câu hỏi")
    grade: str = Field(description="Khối lớp")
    subject: str = Field(description="Môn học")
    questions: List[QuizQuestion] = Field(description="Danh sách các câu hỏi trắc nghiệm")

def generate_quizizz_questions(
    grade: int,
    subject: str,
    topic: str,
    num_questions: int = 5,
    llm_client: Optional[UnifiedLLMClient] = None
) -> QuizSet:
    """
    Sinh bộ câu hỏi trắc nghiệm đố vui và chuẩn hóa dữ liệu cho Quizizz/Wordwall.
    """
    engine = PromptEngine()
    grade_info = engine.get_grade(grade)
    grade_name = grade_info.name if grade_info else f"Khối Lớp {grade}"
    subject_info = engine.get_subject(grade_info, subject) if grade_info else None
    subject_name = subject_info.name if subject_info else subject

    prompt = f"""
Bạn là Chuyên gia Thiết kế Trò chơi Học tập Số (Gamification) cho Trường Tiểu học Hoàng Mai.
Hãy tạo {num_questions} câu hỏi trắc nghiệm đố vui hấp dẫn, có yếu tố gây tò mò cho:
- Khối lớp: {grade_name}
- Môn học: {subject_name}
- Chủ đề: {topic}

Yêu cầu:
1. Câu hỏi gần gũi với đời sống, ngôn ngữ vui nhộn phù hợp lứa tuổi học sinh tiểu học.
2. 4 phương án lựa chọn rõ ràng, các phương án sai có tính phân tích sư phạm nhẹ nhàng.
3. Chỉ rõ số thứ tự đáp án đúng (1, 2, 3 hoặc 4).
4. Kèm lời giải thích ngắn gọn, tích cực.

Xuất kết quả định dạng JSON theo đúng schema QuizSet.
"""

    client = llm_client or UnifiedLLMClient()
    return client.generate_structured(prompt=prompt, schema_cls=QuizSet)

def export_quiz_to_excel(quiz_set: QuizSet) -> io.BytesIO:
    """
    Xuất bộ câu hỏi thành file Excel định dạng chuẩn để tải lên Quizizz / Kahoot / Wordwall.
    """
    data = []
    for q in quiz_set.questions:
        data.append({
            "Question Text": q.question,
            "Question Type": "Multiple Choice",
            "Option 1": q.option1,
            "Option 2": q.option2,
            "Option 3": q.option3,
            "Option 4": q.option4,
            "Correct Answer": q.correct_option_number,
            "Time in seconds": q.time_in_seconds,
            "Explanation": q.explanation
        })
    df = pd.DataFrame(data)
    
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Quizizz_Template')
    output.seek(0)
    return output
