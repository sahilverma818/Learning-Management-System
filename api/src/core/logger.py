import os
import datetime
import logging
from colorlog import ColoredFormatter
from logging.handlers import RotatingFileHandler


# Creating a directory for log files if it doesn't exist
log_dir = 'log_files'
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Define a handler to output logs to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Define formatter
formatter = ColoredFormatter(
    "%(log_color)s%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG': 'green',
        'INFO': 'blue',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red',
    }
)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Define a handler to output logs to a file inside the application_logs directory
log_filename = os.path.join(log_dir, datetime.datetime.now().strftime("%Y-%m-%d") + '_app.log')
file_handler = RotatingFileHandler(log_filename, maxBytes=10485760, backupCount=10)
file_handler.setLevel(logging.DEBUG)

# Define a formatter for file logs
file_formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)