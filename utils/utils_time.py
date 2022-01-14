import time
from datetime import datetime
from injectable import injectable


@injectable
class UtilsTime:
    def get_current_timestamp_ms(self) -> int:
        return int(time.time() * 1000)

    def format_timestamp_ms(self, timestamp_ms: int) -> str:
        return datetime.fromtimestamp(timestamp_ms / 1000).strftime('%d.%m.%Y %H:%M:%S')
