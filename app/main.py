from fastapi import FastAPI
from app.routes import person_routes, ai_routes, auth_routes
from dotenv import load_dotenv

load_dotenv()


app=FastAPI(title="AI MongoDB Agent")

# AUTH ROUTES
app.include_router(auth_routes.router)
# PERSON ROUTES
app.include_router(person_routes.router)
# AI ROUTES
app.include_router(ai_routes.router)

