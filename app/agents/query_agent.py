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
You are an assistant that converts natural language queries into JSON instructions for MongoDB.
Always return a valid JSON object with the following keys:
- "collection": string name of the collection (or null if user asks only for collection list)
- "filter": MongoDB filter object (or null if not needed)
- "schema_request": true if the user wants schema, else false
- "list_collections_request": true if user asks for available collections, else false

Examples:
1. "give me all users with age > 20" ->
{
  "collection": "users",
  "filter": {"age": {"$gt": 20}},
  "schema_request": false,
  "list_collections_request": false
}

2. "show schema of persons collection" ->
{
  "collection": "persons",
  "filter": null,
  "schema_request": true,
  "list_collections_request": false
}

3. "kon kon si collections hain" ->
{
  "collection": null,
  "filter": null,
  "schema_request": false,
  "list_collections_request": true
}
"""

async def ai_query_agent(user_query: str) -> dict:
    prompt = f"""
{SYSTEM_PROMPT}

User query: {user_query}
Return ONLY JSON object.
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[types.Part.from_text(text=prompt)]
    )

    # Clean AI response
    text = response.text.strip()
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.IGNORECASE)

    # Debug print for development
    print("AI raw response:", text)

    # Try to parse JSON
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Fallback: return default empty structure
        return {
            "collection": None,
            "filter": None,
            "schema_request": False,
            "list_collections_request": False
        }
