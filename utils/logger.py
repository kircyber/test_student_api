import logging
from io import StringIO

def create_logger():
    logger = logging.getLogger('api')
    logger.setLevel(logging.INFO)

    logger.handlers.clear()

    log_stream = StringIO()

    handler = logging.StreamHandler(log_stream)
    handler.setFormatter(
        logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    )

    logger.addHandler(handler)

    return logger, log_stream