import logging
import os


def get_logger(name):
    log_dir = os.path.join(os.getcwd(), "../log")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    return Logger(name, log_file=os.path.abspath(os.path.join(os.path.dirname(__file__), '../../log', 'output.log')))


class Logger:
    def __init__(self, name, log_file):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)
