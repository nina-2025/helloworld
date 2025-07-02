# logger.py
import logging
import os

# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure the root logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
    handlers=[
        logging.FileHandler("logs/project.log", mode='a'),
        logging.StreamHandler()  # also logs to console
    ]
)

# Shortcut to get the logger
logger = logging.getLogger(__name__)
