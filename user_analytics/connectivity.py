"""
Purpose:    Connectivity class
Import:     from connectivity import connections
Use:        connections.method
"""
import sys
import logging
from google.cloud import bigquery
from . import params as env


class Connectivity():
    """
    A class for connecting to external services and databases.
    utilizes params to read credentials from the environment variables
    """

    def __init__(self):
        super(Connectivity, self).__init__()
        self.env = env

    def connect_bq(self):
        if env.GCP_CONFIG_JSON:
            logging.info("Connected to Big Query using config JSON")
            bq_client = bigquery.Client().from_service_account_json(self.env.GCP_CONFIG_JSON)
            return bq_client

        credentials = {
                    "type": self.env.TYPE,
                    "project_id": self.env.PROJECT_ID,
                    "private_key_id": self.env.PRIVATE_KEY_ID,
                    "private_key": self.env.PRIVATE_KEY,
                    "client_email": self.env.CLIENT_EMAIL,
                    "client_id": self.env.CLIENT_ID,
                    "auth_uri": self.env.AUTH_URI,
                    "token_uri": self.env.TOKEN_URI,
                    "auth_provider_x509_cert_url": self.env.AUTH_PROVIDER_X509_CERT_URL,
                    "client_x509_cert_url": self.env.CLIENT_X509_CERT_URL}
        bq_client = bigquery.Client().from_service_account_info(credentials)
        logging.info("Connected to Big Query using credentials")
        return bq_client


this = sys.modules[__name__]
this.connections = Connectivity()
