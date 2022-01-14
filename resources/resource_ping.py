from message_objects.ping_output import PingOutput
from fastapi import APIRouter
from utils.utils_ping import UtilsPing

router_ping = APIRouter()
utils_ping = UtilsPing()

@router_ping.get("/ping", response_model=PingOutput)
def ping() -> PingOutput:
    return utils_ping.build()
