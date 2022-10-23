# run.py

import logging

import config
from app import app

if __name__ == "__main__":
    if config.DEBUG:
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

    app.run(threaded=True)
