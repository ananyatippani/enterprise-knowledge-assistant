import os

import google.generativeai as genai
from dotenv import load_dotenv

from app.utils.logger import logger

# Load environment variables
load_dotenv()

# Read Gemini API Key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Please check your .env file.")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Initialize Gemini model
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash"
)


def generate_answer(question: str, context: str) -> str:
    """
    Generate an answer using the retrieved document context.
    """

    logger.info("Preparing prompt for Gemini...")

    prompt = f"""
You are an Enterprise Knowledge Assistant.

Your job is to answer questions ONLY using the provided document context.

Instructions:

- Only use information found in the context.
- If multiple sections contain useful information, combine them into one clear answer.
- Do not invent facts.
- Do not use outside knowledge.
- If the answer is not available in the context, reply exactly:

"I couldn't find that information in the uploaded documents."

----------------------------
DOCUMENT CONTEXT
----------------------------

{context}

----------------------------
USER QUESTION
----------------------------

{question}

----------------------------
ANSWER
----------------------------
"""

    try:

        logger.info("Sending request to Gemini...")

        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                temperature=0.2,
                max_output_tokens=1024,
            )
        )

        logger.info("Gemini response received.")

        if response.text:
            return response.text.strip()

        return "No response generated."

    except Exception as e:

        logger.exception("Gemini generation failed.")

        return f"Error generating response: {str(e)}"