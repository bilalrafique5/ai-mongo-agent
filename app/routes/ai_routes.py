# app/routes/ai_routes.py
from fastapi import APIRouter, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from app.agents.query_agent import ai_query_agent
from app.config import MONGO_URI, DATABASE_NAME

router = APIRouter(prefix="/AI", tags=["AI"])

# MongoDB client
client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]

@router.post("/query_person")
async def ai_query(user_query: str):
    
    # Step 1: Ask AI for structured JSON instruction
    try:
        instr = await ai_query_agent(user_query)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Step 2: If user wants collection list
    if instr.get("list_collections_request"):
        collections = await db.list_collection_names()
        return {"available_collections": collections}

    # Step 3: Ensure collection is specified
    collection_name = instr.get("collection")
    if not collection_name:
        raise HTTPException(status_code=400, detail="Could not detect collection from query")

    # Check if collection exists
    if collection_name not in await db.list_collection_names():
        raise HTTPException(status_code=404, detail=f"Collection '{collection_name}' not found")

    # Step 4: If schema requested
    if instr.get("schema_request"):
        sample = await db[collection_name].find_one()
        if not sample:
            return {"collection": collection_name, "schema": "Empty collection"}
        schema = {k: type(v).__name__ for k, v in sample.items()}
        return {"collection": collection_name, "schema": schema}

    # Step 5: Otherwise fetch data using AI-generated filter
    mongo_filter = instr.get("filter", {})
    raw_data = await db[collection_name].find(mongo_filter).to_list(100)

    # Convert ObjectId to string
    data = []
    for doc in raw_data:
        doc["_id"] = str(doc["_id"])
        data.append(doc)

    return {
        "collection": collection_name,
        "user_query": user_query,
        "mongo_filter": mongo_filter,
        "result": data
    }

