from fastapi import APIRouter
from oxide.core import oxide as oxide

collections_router = APIRouter(prefix="/collections")

@collections_router.get("/get")
async def get_collections():
   collection_names = oxide.collection_names()
   return collection_names
      