import os

MONGO_URI=os.getenv("MONGO_URI","mongodb://localhost:27017")
DATABASE_NAME="ai_agent_db"
COLLECTION_NAME="persons"
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY","AIzaSyDcB6H6GyTYttQsl0VELYOak8Rz4EhqDA4")