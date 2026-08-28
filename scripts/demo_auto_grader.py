"""
Script tự động chấm điểm & nhận xét bài luận với Structured Outputs (Pydantic)
"""
import os
import sys
import json
from dotenv import load_dotenv

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

from pydantic import BaseModel, Field
from google import genai
from google.genai import types

load_dotenv()

class AssessmentResult(BaseModel):
    score: float = Field(description="Điểm số bài làm trên thang điểm 10 (ví dụ: 8.5)")
    strengths: list[str] = Field(description="Danh sách các điểm mạnh nổi bật trong bài làm")
    weaknesses: list[str] = Field(description="Danh sách các điểm còn hạn chế hoặc lỗi sai")
    detailed_feedback: str = Field(description="Lời nhận xét chi tiết, mang tính động viên và hướng dẫn khắc phục")

def grade_submission(essay_text: str, topic: str):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ Lỗi: Chưa cấu hình GEMINI_API_KEY trong file .env")
        sys.exit(1)

    client = genai.Client()
    
    prompt = f"""
    Hãy đánh giá bài làm tự luận của học sinh dựa trên tiêu chí: Lập luận, Bố cục, và Sáng tạo.
    
    Chủ đề: {topic}
    Bài làm:
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
    sample_essay = (
        "Bảo vệ môi trường là trách nhiệm của toàn xã hội. Hiện nay ô nhiễm rác thải nhựa "
        "đang ở mức báo động. Chúng ta cần tăng cường tái chế, hạn chế sử dụng túi nilon "
        "và trồng thêm nhiều cây xanh để giữ cho không khí trong lành."
    )
    
    print("🔄 Đang chấm bài tự luận...\n")
    try:
        result: AssessmentResult = grade_submission(
            essay_text=sample_essay,
            topic="Ý thức bảo vệ môi trường của thế hệ trẻ"
        )
        print(f"📊 Điểm số: {result.score} / 10")
        print("\n✅ Ưu điểm:")
        for s in result.strengths:
            print(f"  - {s}")
        print("\n⚠️ Cần cải thiện:")
        for w in result.weaknesses:
            print(f"  - {w}")
        print(f"\n💬 Nhận xét chi tiết:\n{result.detailed_feedback}")
    except Exception as e:
        print(f"❌ Có lỗi xảy ra: {e}")
