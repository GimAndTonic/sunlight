# Use with from python_helper.logging_setup import logger

import logging
from pathlib import Path

# Ensure logs directory exists
Path("logs").mkdir(exist_ok=True)

# Set up root logger once
logging.basicConfig(
    level=logging.INFO,
    filemode='a',                           # Append mode
    filename='logs/sunlight_lib.log',                # Output file
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger("sunlight")  # Optional custom name

