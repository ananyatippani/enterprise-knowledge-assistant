import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-2.5-flash"

TEMPERATURE = 0.2
MAX_OUTPUT_TOKENS = 1024
TOP_K = 5
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150