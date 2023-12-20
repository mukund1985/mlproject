import logging
import os
from datetime import datetime

# Generating a unique log file name using the current date and time.
# This ensures that each log file is distinct and easily identifiable.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Creating a directory path for storing log files.
# The logs directory is set to be inside the current working directory.
logs_dir = os.path.join(os.getcwd(), "logs")

# Ensuring that the logs directory exists. If it doesn't, it's created.
# 'exist_ok=True' prevents an error if the directory already exists.
os.makedirs(logs_dir, exist_ok=True)

# Defining the full path for the log file.
# This combines the logs directory path with the generated log file name.
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Setting up the basic configuration for the logging system.
# 'filename' specifies the file where logs will be stored.
# 'format' defines the structure of the log messages, including timestamp, line number, logger name, log level, and the message.
# 'level' sets the threshold for logging. Messages that are less severe than this level will be ignored.
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# The following commented-out code is for creating a logger object and testing the logging setup.
# Uncomment to use in an application where you need logging.

# # Creating and exporting the logger object for use in other modules.
# # '__name__' gives the logger the name of the current module.
# logger = logging.getLogger(__name__)

# # Example use of the logger in the main part of the application.
# # This is a conditional that checks if the script is run as the main program.
# if __name__ == "__main__":
#     # Writing an info-level log message indicating that logging has started.
#     logging.info("Logging has started")
