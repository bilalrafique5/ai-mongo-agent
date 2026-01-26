from fastapi import APIRouter, Depends
from app.schemas.person_schema import PersonSchema
from app.crud.person_crud import (
    create_person, get_all_persons, get_person_by_id,
    update_person, delete_person,
    get_person_by_name, get_persons_by_start_letter,
    delete_person_by_name
)
from app.routes.auth_routes import get_current_user

router = APIRouter(prefix="/persons")

@router.post("/create", tags=["CREATE"])
async def add_person(person: PersonSchema, user: dict = Depends(get_current_user)):
    return {"user created with id": await create_person(person.dict())}

@router.get("/", tags=["READ"])
async def all_persons(user: dict = Depends(get_current_user)):
    return await get_all_persons()

@router.get("/{person_id}", tags=["READ"])
async def get_person(person_id: str, user: dict = Depends(get_current_user)):
    return await get_person_by_id(person_id)

@router.put("/{person_id}", tags=["UPDATE"])
async def update(person_id: str, person: PersonSchema, user: dict = Depends(get_current_user)):
    return await update_person(person_id, person.dict())

@router.delete("/{person_id}", tags=["DELETE"])
async def delete(person_id: str, user: dict = Depends(get_current_user)):
    return {"deleted": await delete_person(person_id)}

@router.get("/name/{name}", tags=["READ"])
async def by_name(name: str, user: dict = Depends(get_current_user)):
    return await get_person_by_name(name)

@router.get("/start/{letter}", tags=["READ"])
async def by_letter(letter: str, user: dict = Depends(get_current_user)):
    return await get_persons_by_start_letter(letter)

@router.delete("/name/{name}", tags=["DELETE"])
async def delete_name(name: str, user: dict = Depends(get_current_user)):
    return {"deleted": await delete_person_by_name(name)}
