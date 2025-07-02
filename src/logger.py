# logger.py
import logging
import os

class ProjectLogger:
    """Custom logger class that is used across the project."""
    def __init__(self):
        # Get the directory of this script
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir, "logs")
        os.makedirs(log_dir, exist_ok=True)

        log_file = os.path.join(log_dir, "project.log")

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
            handlers=[
                logging.FileHandler(log_file, mode='a'),
                logging.StreamHandler()
            ]        )

        self.logger = logging.getLogger("ProjectLogger")

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)
    
    def debug(self, message):
        self.logger.debug(message)
