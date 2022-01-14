from a360_message_protocol import PingOutput
from fastapi import APIRouter
from a360_utils import UtilsPing

router_ping = APIRouter()
utils_ping = UtilsPing()

@router_ping.get("/ping", response_model=PingOutput)
def ping() -> PingOutput:
    return utils_ping.build()
