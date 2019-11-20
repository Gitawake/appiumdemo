# -*- coding: utf-8 -*-
import logging
import os.path
import time


class Logger:
    def __init__(self):
        # Create a logger
        self.logger = logging.getLogger('App')
        self.logger.setLevel(logging.DEBUG)

        # Create a handler to write to the log file
        log_dir = os.path.dirname(os.path.abspath('.')) + '/output/logs/'
        # Determine whether the required folder exists, otherwise create a
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_dir = log_dir + time.strftime('%Y-%m-%d-%H-%M-%S') + '.log'

        fh = logging.FileHandler(log_dir, encoding='utf-8')
        fh.setLevel(logging.INFO)

        # Create another handler to output to the console
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # Define the output format of handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # Add handler to logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
