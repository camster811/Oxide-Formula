from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .routers import oxide_collections

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(oxide_collections.router)


@app.get("/")
async def root():
    return {"message": "This is the oxide API!"}