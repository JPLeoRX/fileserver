from injectable import injectable, autowired, Autowired
from message_objects.ping_output import PingOutput
from utils.utils_id import UtilsId
from utils.utils_time import UtilsTime


@injectable
class UtilsPing:
    @autowired
    def __init__(self, utils_id: Autowired(UtilsId), utils_time: Autowired(UtilsTime)):
        self.utils_id = utils_id
        self.utils_time = utils_time

    def build(self) -> PingOutput:
        id = self.utils_id.generate_uuid()
        success = True
        timestamp = self.utils_time.get_current_timestamp_ms()
        return PingOutput(id, success, timestamp)
