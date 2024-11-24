import logging
import os

class Logger:
    def __init__(self, log_file='project.log'):
        # 确保日志目录存在
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger()

    def log_interaction(self, message):
        self.logger.info(f"INTERACTION: {message}")

    def log_execution(self, message):
        self.logger.info(f"EXECUTION: {message}")

    def log_error(self, message):
        self.logger.error(f"ERROR: {message}")
