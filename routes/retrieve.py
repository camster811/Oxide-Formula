from fastapi import APIRouter
from oxide.core import oxide as oxide
from pydantic import BaseModel
 
     
retrieve_router = APIRouter()

@retrieve_router.get("/retrieve")
async def retrieve_module(selected_module: str, selected_collection: str):
    try:
        cid = oxide.get_cid_from_name(selected_collection)
        files = oxide.expand_oids(cid)
        results = oxide.retrieve(selected_module, files)
        return results
    except Exception as e:
        return {"error": str(e)}
