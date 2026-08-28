"""
Script tự động tạo Kế hoạch Bài dạy (Giáo án 5E) bằng Gemini API
"""
import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

def generate_lesson_plan(subject: str, grade: str, topic: str):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ Lỗi: Chưa cấu hình GEMINI_API_KEY trong file .env")
        sys.exit(1)
        
    client = genai.Client()
    
    prompt = f"""
    Hãy đóng vai một Chuyên gia Giáo dục STEM. Hãy xây dựng Kế hoạch bài dạy 45 phút theo mô hình 5E cho:
    - Môn học: {subject}
    - Khối lớp: {grade}
    - Chủ đề: {topic}

    Định dạng đầu ra: Markdown chi tiết với 5 phần:
    1. Engage (Gắn kết)
    2. Explore (Khám phá)
    3. Explain (Giải thích)
    4. Elaborate (Củng cố)
    5. Evaluate (Đánh giá)
    """
    
    print(f"🔄 Đang tạo giáo án cho chủ đề '{topic}' ({subject} {grade})...\n")
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.3,
        )
    )
    
    return response.text

if __name__ == "__main__":
    plan = generate_lesson_plan(
        subject="Khoa học Tự nhiên",
        grade="Lớp 6",
        topic="Sự nở vì nhiệt của chất rắn"
    )
    print(plan)
