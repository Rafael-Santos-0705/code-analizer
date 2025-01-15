from crewai import LLM
from utils import Environment

class LLMProvider:
    def __init__(self):
        llm_model = Environment.get("LLM_MODEL", "gpt-4")
        self.model = LLM(
            model=llm_model,
            temperature=0.8,
            max_tokens=150,
            top_p=0.9,
            frequency_penalty=0.1,
            presence_penalty=0.1,
            stop=["END"],
            seed=42
        )
