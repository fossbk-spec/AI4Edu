import os
import json
import re
from typing import Type, TypeVar, Optional, List, Dict, Any
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

T = TypeVar("T", bound=BaseModel)

# Danh sách các Model được hỗ trợ
SUPPORTED_PROVIDERS = {
    "Google Gemini": [
        {"id": "gemini-3.5-flash", "name": "Gemini 3.5 Flash (Khuyên dùng - Rất nhanh & Ổn định)"},
        {"id": "gemini-3.6-flash", "name": "Gemini 3.6 Flash (Tối ưu phản hồi)"},
        {"id": "gemini-3.5-flash-lite", "name": "Gemini 3.5 Flash Lite (Siêu nhẹ)"},
        {"id": "gemini-3.7-flash", "name": "Gemini 3.7 Flash (Mô hình mới nhất)"},
    ],
    "Anthropic Claude": [
        {"id": "claude-3-7-sonnet-20250219", "name": "Claude 3.7 Sonnet (Tư duy & Văn phong sư phạm đỉnh cao)"},
        {"id": "claude-3-5-sonnet-20241022", "name": "Claude 3.5 Sonnet (Chuẩn mực sâu sắc)"},
        {"id": "claude-3-5-haiku-20241022", "name": "Claude 3.5 Haiku (Siêu tốc độ)"},
    ],
    "OpenAI": [
        {"id": "gpt-4o", "name": "GPT-4o (Đa năng mạnh mẽ)"},
        {"id": "gpt-4o-mini", "name": "GPT-4o Mini (Tiết kiệm & Nhanh)"},
    ]
}

def clean_json_string(raw: str) -> str:
    """Loại bỏ markdown block ```json ... ``` nếu model trả về bọc text"""
    text = raw.strip()
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()

class UnifiedLLMClient:
    """
    Client hợp nhất hỗ trợ đa nhà cung cấp: Google Gemini, Anthropic Claude, OpenAI.
    Tự động xử lý fallback khi Gemini bị lỗi 503 Quá tải.
    """
    
    def __init__(self, provider: str = "Google Gemini", model_id: str = "gemini-3.5-flash", api_key: Optional[str] = None):
        self.provider = provider
        self.model_id = model_id
        self.api_key = api_key

    def generate_structured(self, prompt: str, schema_cls: Type[T], system_instruction: Optional[str] = None) -> T:
        """
        Sinh dữ liệu có cấu trúc tuân theo Pydantic schema_cls.
        """
        if "Gemini" in self.provider:
            return self._generate_gemini_structured(prompt, schema_cls, system_instruction)
        elif "Claude" in self.provider or "Anthropic" in self.provider:
            return self._generate_claude_structured(prompt, schema_cls, system_instruction)
        elif "OpenAI" in self.provider:
            return self._generate_openai_structured(prompt, schema_cls, system_instruction)
        else:
            return self._generate_gemini_structured(prompt, schema_cls, system_instruction)

    def generate_text(self, prompt: str, system_instruction: Optional[str] = None, conversation_history: Optional[List[Dict[str, str]]] = None) -> str:
        """
        Sinh văn bản tự do / Chat text.
        """
        if "Gemini" in self.provider:
            return self._generate_gemini_text(prompt, system_instruction, conversation_history)
        elif "Claude" in self.provider or "Anthropic" in self.provider:
            return self._generate_claude_text(prompt, system_instruction, conversation_history)
        elif "OpenAI" in self.provider:
            return self._generate_openai_text(prompt, system_instruction, conversation_history)
        else:
            return self._generate_gemini_text(prompt, system_instruction, conversation_history)

    # -------------------------------------------------------------
    # GOOGLE GEMINI BACKEND
    # -------------------------------------------------------------
    def _generate_gemini_structured(self, prompt: str, schema_cls: Type[T], system_instruction: Optional[str]) -> T:
        from google import genai
        from google.genai import types
        
        api_key = self.api_key or os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Chưa cấu hình GEMINI_API_KEY. Vui lòng nhập API Key trên thanh Sidebar hoặc file .env")
            
        client = genai.Client(api_key=api_key)
        
        models_to_try = [self.model_id]
        if "gemini-3.5-flash" not in models_to_try:
            models_to_try.append("gemini-3.5-flash")
        if "gemini-3.6-flash" not in models_to_try:
            models_to_try.append("gemini-3.6-flash")
        if "gemini-3.5-flash-lite" not in models_to_try:
            models_to_try.append("gemini-3.5-flash-lite")
            
        last_error = None
        for m in models_to_try:
            try:
                config = types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=schema_cls,
                    temperature=0.3,
                )
                if system_instruction:
                    config.system_instruction = system_instruction

                resp = client.models.generate_content(
                    model=m,
                    contents=prompt,
                    config=config
                )
                return schema_cls.model_validate_json(clean_json_string(resp.text))
            except Exception as e:
                last_error = e
                continue
                
        raise last_error

    def _generate_gemini_text(self, prompt: str, system_instruction: Optional[str], conversation_history: Optional[List[Dict[str, str]]]) -> str:
        from google import genai
        from google.genai import types
        
        api_key = self.api_key or os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Chưa cấu hình GEMINI_API_KEY.")
            
        client = genai.Client(api_key=api_key)
        models_to_try = [self.model_id, "gemini-3.5-flash", "gemini-3.6-flash", "gemini-3.5-flash-lite"]
        
        contents = []
        if conversation_history:
            for msg in conversation_history:
                contents.append(f"{'Học sinh' if msg.get('role') == 'user' else 'Trợ giảng'}: {msg.get('content')}")
        contents.append(f"Học sinh: {prompt}")
        full_content = "\n".join(contents)
        
        for m in models_to_try:
            try:
                config = types.GenerateContentConfig(temperature=0.7)
                if system_instruction:
                    config.system_instruction = system_instruction
                resp = client.models.generate_content(model=m, contents=full_content, config=config)
                return resp.text
            except Exception:
                continue
        return "Xin lỗi bạn nhỏ, hệ thống AI đang bận một chút. Bạn hãy thử lại câu hỏi nhé!"

    # -------------------------------------------------------------
    # ANTHROPIC CLAUDE BACKEND
    # -------------------------------------------------------------
    def _generate_claude_structured(self, prompt: str, schema_cls: Type[T], system_instruction: Optional[str]) -> T:
        import anthropic
        api_key = self.api_key or os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("Chưa cấu hình ANTHROPIC_API_KEY. Vui lòng nhập API Key của Anthropic Claude trên thanh Sidebar.")

        client = anthropic.Anthropic(api_key=api_key)
        json_schema = json.dumps(schema_cls.model_json_schema(), ensure_ascii=False)
        
        system = (system_instruction or "") + f"\n\nBẮT BUỘC: Bạn phải xuất kết quả dưới dạng JSON hợp lệ theo đúng JSON Schema sau, không thêm lời chào hay markdown thừa bên ngoài JSON:\n{json_schema}"
        
        message = client.messages.create(
            model=self.model_id,
            max_tokens=4096,
            temperature=0.3,
            system=system,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        raw_text = message.content[0].text
        cleaned = clean_json_string(raw_text)
        return schema_cls.model_validate_json(cleaned)

    def _generate_claude_text(self, prompt: str, system_instruction: Optional[str], conversation_history: Optional[List[Dict[str, str]]]) -> str:
        import anthropic
        api_key = self.api_key or os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("Chưa cấu hình ANTHROPIC_API_KEY. Vui lòng nhập API Key của Anthropic Claude trên thanh Sidebar.")

        client = anthropic.Anthropic(api_key=api_key)
        messages = []
        if conversation_history:
            for msg in conversation_history:
                role = "assistant" if msg.get("role") == "assistant" else "user"
                messages.append({"role": role, "content": msg.get("content", "")})
        messages.append({"role": "user", "content": prompt})

        message = client.messages.create(
            model=self.model_id,
            max_tokens=2048,
            temperature=0.7,
            system=system_instruction or "Bạn là Trợ giảng Sư phạm Tiểu học Hoàng Mai thân thiện và kiên nhẫn.",
            messages=messages
        )
        return message.content[0].text

    # -------------------------------------------------------------
    # OPENAI BACKEND
    # -------------------------------------------------------------
    def _generate_openai_structured(self, prompt: str, schema_cls: Type[T], system_instruction: Optional[str]) -> T:
        import openai
        api_key = self.api_key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("Chưa cấu hình OPENAI_API_KEY. Vui lòng nhập OpenAI API Key trên thanh Sidebar.")

        client = openai.OpenAI(api_key=api_key)
        messages = []
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})
        messages.append({"role": "user", "content": prompt})

        response = client.beta.chat.completions.parse(
            model=self.model_id,
            messages=messages,
            response_format=schema_cls,
            temperature=0.3
        )
        return response.choices[0].message.parsed

    def _generate_openai_text(self, prompt: str, system_instruction: Optional[str], conversation_history: Optional[List[Dict[str, str]]]) -> str:
        import openai
        api_key = self.api_key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("Chưa cấu hình OPENAI_API_KEY.")

        client = openai.OpenAI(api_key=api_key)
        messages = []
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})
        if conversation_history:
            for msg in conversation_history:
                messages.append({"role": msg.get("role", "user"), "content": msg.get("content", "")})
        messages.append({"role": "user", "content": prompt})

        response = client.chat.completions.create(
            model=self.model_id,
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content
