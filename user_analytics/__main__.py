import logging
from . import order_status
from .utils import notify, setup_logging  # pylint: disable=E0401, E0611

try:
    setup_logging()
    order_status.main()
    logging.info("Done order status")

except Exception as err:
    logging.error("Error: {}".format(err))
    notify(err)
    raise err
