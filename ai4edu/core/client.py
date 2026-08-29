import os
import sys
from dotenv import load_dotenv
from google import genai

# Cấu hình UTF-8 cho Windows console nếu cần
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

load_dotenv()

DEFAULT_MODEL = "gemini-3.7-flash"

def get_genai_client() -> genai.Client:
    """
    Khởi tạo Gemini Client từ google-genai SDK chính thức.
    Yêu cầu GEMINI_API_KEY trong biến môi trường hoặc file .env.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(
            "❌ Lỗi: Chưa cấu hình GEMINI_API_KEY. "
            "Vui lòng tạo file .env tại thư mục gốc dự án và khai báo: GEMINI_API_KEY=your_key_here"
        )
    return genai.Client(api_key=api_key)
