#!/usr/bin/python
import logging
import logging.handlers

def setup(log_file, level=logging.INFO):
    log_handler = logging.handlers.RotatingFileHandler(log_file, mode='a', maxBytes=1024*500, backupCount=5)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')
    log_handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(log_handler)
    logger.setLevel(level)
