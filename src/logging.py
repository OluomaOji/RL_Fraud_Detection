import logging
import os

# set the directory
LOG_DIR = "LOGS"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# set the log path
logging.basicConfig(
    level = logging.INFO,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    handlers=[
        logging.FileHandler(os.path.join(LOG_DIR,"rl_fraud_detection.logs")),
        logging.StreamHandler()
    ]
)

def logging(name):
    return logging.getLogger(name)