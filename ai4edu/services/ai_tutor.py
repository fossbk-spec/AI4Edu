from typing import List, Optional, Dict, Any
from google.genai import types
from ai4edu.core.client import get_genai_client, DEFAULT_MODEL
from ai4edu.core.prompt_engine import PromptEngine

def tutor_chat(
    grade: int,
    subject: Optional[str],
    user_message: str,
    conversation_history: Optional[List[Dict[str, str]]] = None,
    model_name: str = DEFAULT_MODEL
) -> str:
    """
    Tạo phản hồi Trợ giảng AI Socratic phù hợp với lứa tuổi và khối lớp
    """
    engine = PromptEngine()
    grade_info = engine.get_grade(grade)
    if not grade_info:
        raise ValueError(f"Khối lớp không hợp lệ: {grade}. Hỗ trợ lớp 1 đến 12.")

    subject_info = engine.get_subject(grade_info, subject) if subject else None
    system_instruction = engine.build_system_prompt_for_tutor(grade_info, subject_info)

    client = get_genai_client()

    # Xây dựng contents từ conversation_history nếu có
    contents = []
    if conversation_history:
        for turn in conversation_history:
            role = turn.get("role", "user")
            content = turn.get("content", "")
            contents.append(f"{role.upper()}: {content}")
    contents.append(f"USER: {user_message}")

    full_prompt = f"System Instruction:\n{system_instruction}\n\n" + "\n".join(contents)

    response = client.models.generate_content(
        model=model_name,
        contents=full_prompt,
        config=types.GenerateContentConfig(
            temperature=0.6,
        ),
    )
    return response.text
