from fastapi import APIRouter
from oxide.core import oxide as oxide
from pydantic import BaseModel
 
     
retrieve_router = APIRouter()

@retrieve_router.get("/retrieve")
async def retrieve_module(selected_module: str, selected_collection: str):
    try:
        oids = oxide.get_oids_with_name(selected_collection)
        results = oxide.retrieve(selected_module, oids)
        return results
    except Exception as e:
        return {"error": str(e)}
