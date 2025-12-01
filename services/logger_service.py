import logging
import os
from config import Config

class LoggerService:
    def __init__(self):
        self.log_path = Config.LOG_PATH

        
        log_dir = os.path.dirname(self.log_path)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        logging.basicConfig(
            filename=self.log_path,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def log(self, message):
        logging.info(message)
