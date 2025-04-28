import logging
from loguru import logger

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# format='%(asctime)s | %(levelname)s | %(message)s | %(filename)s | %(funcName)s \
#         | %(lineno)d | %(module)s | %(name)s | %(pathname)s | %(process)d | %(processName)s \
#         | %(thread)d | %(threadName)s'

# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning")
logger.error("This is an error")
logger.critical("This is critical")
