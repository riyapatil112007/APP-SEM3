import logging
from logging.handlers import RotatingFileHandler

# Create logger
logger = logging.getLogger("MyLogger")
logger.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Console handler
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

# File handler with rotation
file = RotatingFileHandler(
    "app.log", maxBytes=1000, backupCount=3
)
file.setLevel(logging.DEBUG)
file.setFormatter(formatter)

# Add handlers
logger.addHandler(console)
logger.addHandler(file)

# Logging messages
logger.debug("Debug message")
logger.info("Program started")
logger.warning("This is a warning")
logger.error("An error occurred")
logger.critical("Critical error")

# Exception logging
try:
    a = 10 / 0
except Exception:
    logger.exception("Exception occurred")