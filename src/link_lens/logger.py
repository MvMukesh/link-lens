import os
import sys
import logging



logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "./logs" # ./ project root
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(level=logging.INFO,format=logging_str,
                    handlers=[logging.FileHandler(log_filepath),
                              logging.StreamHandler(sys.stdout)])
logger = logging.getLogger("link_lens")


### More production centric

# # Configuration options (customize as needed)
# LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")  # Logs directory relative to script
# LOG_FILEPATH = os.path.join(LOG_DIR, "running_logs.log")
# LOG_LEVEL = logging.INFO  # Adjust logging level (e.g., DEBUG, WARNING, ERROR)
# LOG_FORMAT = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"


# def setup_logger():
#     """
#     Creates the log directory if it doesn't exist, sets the desired log level,
#     format, and handlers for file and stdout output.

#     Returns:
#         logging.Logger: The configured logger instance.
#     """

#     # Create log directory if it doesn't exist
#     os.makedirs(LOG_DIR, exist_ok=True)

#     # Configure logging
#     logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT,
#                         handlers=[logging.FileHandler(LOG_FILEPATH),
#                                   logging.StreamHandler(sys.stdout)])

#     # Get a logger instance
#     logger = logging.getLogger("link_lens")
#     return logger


# # Create a single instance of the logger
# logger = setup_logger()
