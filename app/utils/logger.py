import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("crypto_service")


def log_info(message):
    logger.info(message)
