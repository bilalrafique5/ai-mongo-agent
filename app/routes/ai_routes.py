# app/routes/ai_routes.py
from fastapi import APIRouter, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from app.agents.query_agent import ai_query_agent
from app.utils.schema_utils import get_all_collection_schemas
from app.config import MONGO_URI, DATABASE_NAME
from google.genai.errors import ClientError

router = APIRouter(prefix="/AI", tags=["AI"])

client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]

@router.post("/query")
async def ai_query(user_query: str):

    schemas = await get_all_collection_schemas(db)

    try:
        instr = await ai_query_agent(user_query, schemas)
    except ClientError:
        raise HTTPException(500, "AI service failed")

    # 1️⃣ List collections
    if instr.get("list_collections_request"):
        return {"available_collections": list(schemas.keys())}

    collection = instr.get("collection")
    if not collection:
        raise HTTPException(400, "AI could not determine collection")

    if collection not in schemas:
        raise HTTPException(404, f"Collection '{collection}' not found")

    # 2️⃣ Schema request
    if instr.get("schema_request"):
        return {
            "collection": collection,
            "schema": schemas[collection]
        }

    # 3️⃣ Query data
    mongo_filter = instr.get("filter") or {}
    docs = await db[collection].find(mongo_filter).to_list(100)

    return {
        "collection": collection,
        "filter": mongo_filter,
        "result": [{**d, "_id": str(d["_id"])} for d in docs]
    }
