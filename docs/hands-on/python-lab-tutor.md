# Lab 1: Chatbot Trợ giảng bằng Python

Trong bài lab này, chúng ta sẽ xây dựng một chatbot gia sư toán học tương tác trên giao diện dòng lệnh (CLI) bằng cách sử dụng `google-genai` SDK.

## Mã nguồn bài Lab (`scripts/demo_tutor.py`)

Xem file thực tế tại [scripts/gemini_client.py](file:///Users/Admin/Desktop/Antigravity/AI4Edu/scripts/gemini_client.py).

```python
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

SYSTEM_INSTRUCTION = """
Bạn là một AI Tutor môn Vật lý và Toán học chuyên nghiệp. 
Hãy áp dụng phương pháp Socratic:
1. Đặt câu hỏi gợi mở thay vì cho ngay đáp án.
2. Hướng dẫn từng bước một.
3. Luôn giữ thái độ khích lệ, thân thiện.
"""

def run_tutor():
    client = genai.Client()
    chat = client.chats.create(
        model="gemini-3.7-flash",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.4,
        )
    )
    
    print("🤖 AI Tutor đã sẵn sàng! Gõ 'exit' để thoát.\n")
    while True:
        user_input = input("Học sinh: ")
        if user_input.lower() in ["exit", "quit"]:
            break
            
        response = chat.send_message(user_input)
        print(f"\nAI Tutor: {response.text}\n")

if __name__ == "__main__":
    run_tutor()
```
