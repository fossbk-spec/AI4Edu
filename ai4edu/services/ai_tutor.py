from typing import List, Optional, Dict, Any
from ai4edu.core.prompt_engine import PromptEngine
from ai4edu.core.llm_provider import UnifiedLLMClient

def tutor_chat(
    grade: int,
    subject: Optional[str],
    user_message: str,
    conversation_history: Optional[List[Dict[str, str]]] = None,
    llm_client: Optional[UnifiedLLMClient] = None
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

    client = llm_client or UnifiedLLMClient()
    return client.generate_text(
        prompt=user_message,
        system_instruction=system_instruction,
        conversation_history=conversation_history
    )
