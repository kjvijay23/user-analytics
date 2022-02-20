import logging
from flask import Flask, abort, jsonify
from .connectivity import connections
from .utils import setup_logging
from .dao import get_order_status


db_client = None
app = Flask(__name__)
setup_logging()


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    return jsonify(error=str(e)), code


@app.before_request
def establish_db_conn():
    global db_client
    if db_client is None:
        logging.info("Establishing database connection")
        db_client = connections.connect_bq()


@app.route('/heartbeat/')
def heart_beat():
    return jsonify({"status_code": "200",
                    "status_message": "OK"})


@app.route('/orderStatus/<string:fullvisitorid>')
def get_order_details(fullvisitorid):
    if fullvisitorid is None:
        abort(404)
    return jsonify(get_order_status(db_client, fullvisitorid))


@app.errorhandler(404)
def error_msg(e):
    return jsonify(error='Bad request - Required fullvisitorid')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
