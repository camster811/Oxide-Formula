import uvicorn 
import configparser
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import sys

config = configparser.ConfigParser()
config.read("config.ini")

host = config.get("General", "host")
clientport = config.getint("General", "clientport")
hostport = config.getint("General", "hostport")
oxide_path = config.get("Oxide", "path")
clientip = config.get("General", "clientip")

sys.path.append(oxide_path)

from routes import collections_router, modules_router, retrieve_router, oxide_router
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[f"http://{host}:{clientport}", f"http://{clientip}:{clientport}"],  # Adjust to your SvelteKit dev server URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],    
)
app.include_router(collections_router, prefix="/api")
app.include_router(modules_router, prefix="/api")
app.include_router(retrieve_router, prefix="/api")
app.include_router(oxide_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, port=hostport, host=host)
    