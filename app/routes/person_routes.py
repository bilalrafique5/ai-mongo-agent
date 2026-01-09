from fastapi import APIRouter
from app.crud.person_crud import create_person,get_all_persons,get_person_by_id,update_person,delete_person
from app.schemas.person_schema import PersonSchema


router=APIRouter(prefix="/Persons")


@router.post("/create", tags=["CREATE"])
async def add_person(person: PersonSchema):
    person_dict = person.dict()
    person_id = await create_person(person_dict)
    return {"id": person_id}



@router.get("/students",tags=["READ"])
async def all_persons():
    return await get_all_persons()

@router.get("/{person_id}",tags=["READ"])
async def get_person(person_id:str):
    return await get_person_by_id(person_id)


@router.put("/update/{person_id}",tags=["UPDATE"])
async def modify_person(person_id:str, person:dict):
    return await update_person(person_id, person)


@router.delete("/delete/{person_id}",tags=["DELETE"])
async def delete_person_data(person_id:str):
    deleted=await delete_person(person_id)
    return {"deleted":deleted}
