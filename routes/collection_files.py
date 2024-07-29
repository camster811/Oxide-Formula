from fastapi import APIRouter, HTTPException
from oxide.core import oxide as oxide

files_router = APIRouter(prefix="/collection-files")

@files_router.get("/get")
async def get_collection_files(selected_collection: str):
    names = {}
    try:
        cid = oxide.get_cid_from_name(selected_collection)
        file_oids = oxide.expand_oids(cid)
        for oid in file_oids:
            names.update({'%s' % oxide.get_names_from_oid(oid) : '%s' % {oid}})
        return names
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))