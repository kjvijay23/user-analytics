import logging
from . import app
from .utils import notify, setup_logging  # pylint: disable=E0401, E0611

try:
    setup_logging()
    app.run(host='0.0.0.0', port=5000)  # Runs the flask app on port 5000
    logging.info("Started user-analytics API")

except Exception as err:
    logging.error("Error: {}".format(err))
    notify(err)
    raise err
