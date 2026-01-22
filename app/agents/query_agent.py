import os
import json
import re
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

SYSTEM_PROMPT = """
Convert user query into MongoDB filter JSON.
Return ONLY valid JSON.

Examples:
find person with name bilal -> {"name": "bilal"}
age greater than 20 -> {"age": {"$gt": 20}}
age less than 15 -> {"age": {"$lt": 15}}
"""

async def ai_query_agent(user_query: str) -> dict:
    prompt = f"""
{SYSTEM_PROMPT}

User query: {user_query}
MongoDB filter:
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[types.Part.from_text(text=prompt)]
    )


    # Clean the AI response to remove ```json or ``` markers
    text = response.text.strip()
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.IGNORECASE)

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON from AI: {text}")
