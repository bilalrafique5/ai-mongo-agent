# app/agents/query_agent.py
import os
import json
import re
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

async def ai_query_agent(user_query: str, schemas: dict) -> dict:
    schema_text = json.dumps(schemas, indent=2)

    prompt = f"""
You are an intelligent MongoDB AI agent.

Available collections and their schemas:
{schema_text}

Rules:
- Automatically select the most relevant collection
- If user asks for schema, set schema_request = true
- If user asks for available collections, set list_collections_request = true
- If no collection matches, return collection = null
- Return ONLY valid JSON

JSON format:
{{
  "collection": string | null,
  "filter": object | null,
  "schema_request": boolean,
  "list_collections_request": boolean
}}

User query:
{user_query}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[types.Part.from_text(text=prompt)]
    )

    text = response.text.strip()
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text)

    return json.loads(text)
