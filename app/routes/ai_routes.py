# app/routes/ai_routes.py
from fastapi import APIRouter
from app.agents.query_agent import ai_query_agent
from app.crud.person_crud import get_all_persons

router = APIRouter(prefix="/AI")

@router.post("/query_person", tags=["AI"])
async def ai_query(user_query: str):
    mongo_filter = await ai_query_agent(user_query)
    data = await get_all_persons(mongo_filter)
    return {
        "user_query": user_query,
        "mongo_filter": mongo_filter,
        "result": data
    }
