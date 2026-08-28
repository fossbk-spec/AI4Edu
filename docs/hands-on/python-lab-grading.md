# Lab 2: Hệ thống Chấm bài & Nhận xét Tự động

Bài lab này hướng dẫn cách ép mô hình AI trả về kết quả định dạng JSON chuẩn (Structured Output) với Pydantic để chấm điểm bài làm của học sinh.

## Mã nguồn bài Lab (`scripts/demo_auto_grader.py`)

Xem file thực tế tại [scripts/demo_auto_grader.py](file:///Users/Admin/Desktop/Antigravity/AI4Edu/scripts/demo_auto_grader.py).

```python
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

load_dotenv()

# 1. Định nghĩa cấu trúc kết quả mong muốn
class AssessmentResult(BaseModel):
    score: float = Field(description="Điểm số trên thang điểm 10")
    strengths: list[str] = Field(description="Các ưu điểm chính trong bài làm")
    weaknesses: list[str] = Field(description="Các điểm còn hạn chế hoặc lỗi sai")
    detailed_feedback: str = Field(description="Nhận xét chi tiết và hướng dẫn cải thiện")

def grade_submission(essay_text: str, topic: str):
    client = genai.Client()
    
    prompt = f"""
    Hãy chấm điểm bài viết dưới đây theo tiêu chí: Bố cục, Lập luận, Từ vựng và Đáo đức văn học.
    - Chủ đề: {topic}
    - Bài làm của học sinh:
    ---
    {essay_text}
    ---
    """
    
    response = client.models.generate_content(
        model='gemini-3.7-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=AssessmentResult,
            temperature=0.2,
        ),
    )
    
    return response.parsed

if __name__ == "__main__":
    sample_essay = "Tình hữu nghị giữa các dân tộc là yếu tố cốt lõi để giữ gìn hòa bình thế giới..."
    result = grade_submission(sample_essay, "Nghị luận xã hội về Hòa bình")
    print(result)
```
