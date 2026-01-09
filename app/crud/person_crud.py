from app.database import db
from app.config import COLLECTION_NAME
from bson import ObjectId


collection=db[COLLECTION_NAME]

async def create_person(data):
    result=await collection.insert_one(data)
    return str(result.inserted_id)

async def get_all_persons(filter_query={}):
    persons=[]
    async for p in collection.find(filter_query):
        p["_id"]=str(p["_id"])
        persons.append(p)
    return persons


async def get_person_by_id(person_id):
    person=await collection.find_one({"_id":ObjectId(person_id)})
    if person:
        person["_id"]=str(person["_id"])
    return person

async def update_person(person_id,data):
    await collection.update_one({"_id":ObjectId(person_id)},{"$set":data})
    return await get_person_by_id(person_id)

async def delete_person(person_id):
    result=await collection.delete_one({"_id":ObjectId(person_id)})
    return result.deleted_count   


