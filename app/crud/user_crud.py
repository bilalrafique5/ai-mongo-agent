# app/crud/user_crud.py
from app.database import db
from passlib.context import CryptContext

collection = db["users"]
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# Create user
async def create_user(user_data: dict):
    user_data["password"] = pwd_context.hash(user_data["password"])
    result = await collection.insert_one(user_data)
    return str(result.inserted_id)

# Get user by username
async def get_user_by_username(username: str):
    return await collection.find_one({"username": username})

# Verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
