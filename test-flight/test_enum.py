import log
from enum import Enum


class LogFormat(str, Enum):
    CONSOLE = "CONSOLE"
    JSON = "JSON"


log.get_logger().info(LogFormat.CONSOLE)
print(LogFormat.CONSOLE)
print(isinstance(LogFormat.CONSOLE, str))
log.get_logger().info(LogFormat.CONSOLE.value)
log.get_logger().info("User logged in", extra={"user_id": 123, "analytics": True})
