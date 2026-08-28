"""
Gemini API Client Helper for AI4Edu Labs
Uses official google-genai SDK
"""
import os
import sys
from dotenv import load_dotenv

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

from google import genai
from google.genai import types

load_dotenv()

def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("⚠️ CẢNH BÁO: Chưa tìm thấy GEMINI_API_KEY trong file .env")
        print("Vui lòng sao chép .env.example thành .env và điền API key của bạn.")
    return genai.Client()

def interactive_tutor():
    client = get_gemini_client()
    system_prompt = (
        "Bạn là một gia sư AI thân thiện, kiên nhẫn chuyên về các môn KHTN. "
        "Áp dụng phương pháp Socratic: Đặt câu hỏi gợi mở thay vì cho đáp án trực tiếp."
    )
    
    chat = client.chats.create(
        model="gemini-3.7-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.4
        )
    )
    
    print("==================================================")
    print("🎓 AI4Edu Demo - AI Tutor (Phương pháp Socratic)")
    print("Gõ 'exit' hoặc 'quit' để kết thúc hội thoại.")
    print("==================================================\n")
    
    while True:
        try:
            user_msg = input("Học sinh 👤: ")
            if user_msg.strip().lower() in ["exit", "quit"]:
                print("Cảm ơn em! Chúc em học tốt!")
                break
            if not user_msg.strip():
                continue
                
            response = chat.send_message(user_msg)
            print(f"\nAI Tutor 🤖: {response.text}\n")
        except Exception as e:
            print(f"\n❌ Lỗi: {e}\n")
            break

if __name__ == "__main__":
    interactive_tutor()
