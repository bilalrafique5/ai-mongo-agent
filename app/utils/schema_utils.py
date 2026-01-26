# app/utils/schema_utils.py
async def get_all_collection_schemas(db):
    schemas = {}

    collections = await db.list_collection_names()
    for col in collections:
        sample = await db[col].find_one()
        if sample:
            schemas[col] = {k: type(v).__name__ for k, v in sample.items()}
        else:
            schemas[col] = {}

    return schemas
