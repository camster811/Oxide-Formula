import uvicorn 

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import collections_router, modules_router
from routes import retrieve_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust to your SvelteKit dev server URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],    
)
app.include_router(collections_router, prefix="/api")
app.include_router(modules_router, prefix="/api")
if __name__ == "__main__":
    uvicorn.run(app)
