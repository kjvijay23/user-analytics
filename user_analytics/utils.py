import logging
from datetime import datetime
from time import time
import uuid


def setup_logging():
    """
    Configures custom log format handler
    """
    logging.getLogger("werkzeug").setLevel(logging.ERROR)  # supress flask warnings
    logging.basicConfig(format='%(asctime)s : Line-%(lineno)s : %(message)s', level=logging.INFO)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return True


def notify(message):
    """
    Function to notify status through slack/ email
    """
    logging.error(message)
    return True


def get_uuid():
    """
    Generated UUID based on the date and time
    """
    uuid_gen = datetime.now().strftime('%Y%m%d') + "_" + (str(time()).replace(".", "-")) + "_" + uuid.uuid4().hex[:10]
    return str(uuid_gen)


def str_to_bool(value):
    """
    convert string to boolean
    """
    return str(value).lower() not in ("", "f", "false", "n", "no", "0")
