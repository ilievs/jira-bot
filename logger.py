import logging
import sys

LOGGER_NAME = 'jira-bot'

_logger = logging.getLogger(LOGGER_NAME)
_logger.setLevel(logging.INFO)

# create logger formatter
_formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")

# log to stdout
_stdout_handler = logging.StreamHandler(sys.stdout)
_stdout_handler.setFormatter(_formatter)
_logger.addHandler(_stdout_handler)

# log the same to a file
_file_handler = logging.FileHandler('log.txt')
_file_handler.setFormatter(_formatter)
_logger.addHandler(_file_handler)


def info(message, *args, **kwargs):
    _logger.info(message, *args, **kwargs)


def warning(message, *args, **kwargs):
    _logger.warning(message, *args, **kwargs)
