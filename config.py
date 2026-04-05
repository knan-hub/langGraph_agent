import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        # LLM
        self.llm_model = os.getenv("OPENAI_MODEL")
        self.llm_api_key = os.getenv("OPENAI_API_KEY")
        self.llm_base_url = os.getenv("OPENAI_ENDPOINT")
        self.llm_tiktoken_model = os.getenv("OPENAI_TIKTOKEN_MODEL")
        self.llm_timeout = int(os.getenv("OPENAI_TIMEOUT"))
        self.llm_max_tokens = int(os.getenv("OPENAI_MAX_TOKENS"))