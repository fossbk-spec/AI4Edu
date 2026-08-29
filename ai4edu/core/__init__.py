"""
Core modules cho AI4Edu Hub
"""
from ai4edu.core.client import get_genai_client, DEFAULT_MODEL
from ai4edu.core.prompt_engine import PromptEngine

__all__ = ["get_genai_client", "DEFAULT_MODEL", "PromptEngine"]
