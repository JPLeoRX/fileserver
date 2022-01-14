from injectable import load_injection_container
load_injection_container()

from fastapi import FastAPI
from resources.resource_ping import router_ping
from resources.resource_upload import router_upload

app = FastAPI()
app.include_router(router_ping)
app.include_router(router_upload)
