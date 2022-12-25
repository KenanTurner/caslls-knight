# Enable file logging
import logging
def setup_logger(name, file, level=logging.INFO, format='%(message)s'):
    formatter = logging.Formatter(format)
    handler = logging.FileHandler(file, encoding="utf-8")
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger
logger = setup_logger("default", "debug.log", logging.DEBUG, '%(asctime)s %(levelname)s %(name)s %(message)s')
