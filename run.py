# run.py

import logging

from app import app

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    app.run(threaded=True)
