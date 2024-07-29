import uvicorn 
import configparser
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import sys

config = configparser.ConfigParser()
config.read("config.ini")

host = config.get("General", "host")
port = config.getint("General", "port")
oxide_path = config.get("Oxide", "path")


sys.path.append(oxide_path)


from routes import collections_router, modules_router, retrieve_router
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
app.include_router(retrieve_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app)
    