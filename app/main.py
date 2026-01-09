from fastapi import FastAPI
from app.routes import person_routes, ai_routes
from dotenv import load_dotenv

load_dotenv()


app=FastAPI(title="AI MongoDB Agent")

app.include_router(person_routes.router)
app.include_router(ai_routes.router)