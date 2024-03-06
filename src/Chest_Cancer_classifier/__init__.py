import os
import sys # The sys module provides information about constants, functions and methods of the Python interpreter.
import logging 
# import the logging module, which is part of the Python standard library
#It is used to log messages to a file or any other output streams like the console or any other output streams.

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("Chest_Cancer_classifierLogger")