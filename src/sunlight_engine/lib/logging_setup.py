import os
import logging

class Logger:
    def __new__(cls, name="sunlight"):
        logger = logging.getLogger(name)

        if not logger.hasHandlers():
            logger.setLevel(logging.INFO)

            # Get base directory from environment or default to current dir
            base_dir = os.getenv("SUNLIGHT_HOME", os.getcwd())
            log_dir = os.path.join(base_dir, "logs")
            os.makedirs(log_dir, exist_ok=True)

            log_file = os.path.join(log_dir, "sunlight_lib.log")
            file_handler = logging.FileHandler(log_file, mode='a')

            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.propagate = False  # Avoid double logging to console

        return logger
