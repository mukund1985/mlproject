import logging
import os
from datetime import datetime

# Generating a unique log file name
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Creating a directory path for logs
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)  # Ensure the directory exists

# Defining the full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Creating and exporting the logger object
logger = logging.getLogger(__name__)

if __name__=="__main__":
    logging.info("Logging has started")
