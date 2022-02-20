import logging
from datetime import datetime
from time import time
import uuid


def setup_logging():
    logging.getLogger("boto3").setLevel(logging.WARNING)
    logging.basicConfig(format='%(asctime)s : Line-%(lineno)s : %(message)s', level=logging.INFO)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return True


def notify(message):
    logging.error(message)
    return True


def get_uuid():
    uuid_gen = datetime.now().strftime('%Y%m%d') + "_" + (str(time()).replace(".", "-")) + "_" + uuid.uuid4().hex[:10]
    return str(uuid_gen)


def str_to_bool(value):
    """
    convert string to boolean
    """
    return str(value).lower() not in ("", "f", "false", "n", "no", "0")
