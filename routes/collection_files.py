from fastapi import APIRouter, HTTPException
from oxide.core import oxide as oxide

files_router = APIRouter(prefix="/collection-files")

@files_router.get("/get")
async def get_collection_files(selected_collection: str):
    names = []
    try:
        cid = oxide.get_cid_from_name(selected_collection)
        files = oxide.expand_oids(cid)
        for cid in files:
            names += oxide.get_names_from_oid(cid)
        return names
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))