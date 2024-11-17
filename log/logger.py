'''
@copyright ziqi-jin
'''

import logging

class Logger:
    def __init__(self, log_file='project.log'):
        logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

    def log_interaction(self, message):
        logging.info(f"INTERACTION: {message}")

    def log_execution(self, message):
        logging.info(f"EXECUTION: {message}")
