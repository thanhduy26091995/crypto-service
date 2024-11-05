import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("sqlalchemy.engine")


def log_info(message):
    logger.info(message)
