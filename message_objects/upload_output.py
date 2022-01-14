from pydantic import BaseModel
from simplestr import gen_str_repr


@gen_str_repr
class UploadOutput(BaseModel):
    id: str
    path: str
    upload_started_timestamp: int
    upload_ended_timestamp: int

    def __init__(self, id: str, path: str, upload_started_timestamp: int, upload_ended_timestamp: int) -> None:
        super().__init__(id=id, path=path, upload_started_timestamp=upload_started_timestamp, upload_ended_timestamp=upload_ended_timestamp)
