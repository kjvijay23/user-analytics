"""
Purpose:    Package Parameters
Import:     import params as env
Use:        env.VAR_NAME
"""
from os import getenv as envs

# GCP creds
GCP_CONFIG_JSON = envs("GOOGLE_APPLICATION_CREDENTIALS", None)
GCP_TYPE = envs("TYPE")
GCP_PROJECT_ID = envs("PROJECT_ID")
GCP_PRIVATE_KEY_ID = envs("PRIVATE_KEY_ID")
GCP_PRIVATE_KEY = envs("PRIVATE_KEY")
GCP_CLIENT_EMAIL = envs("CLIENT_EMAIL")
GCP_CLIENT_ID = envs("CLIENT_ID")
GCP_AUTH_URI = envs("AUTH_URI")
GCP_TOKEN_URI = envs("TOKEN_URI")
GCP_AUTH_PROVIDER_X509_CERT_URL = envs("AUTH_PROVIDER_X509_CERT_URL")
GCP_CLIENT_X509_CERT_URL = envs("CLIENT_X509_CERT_URL")

# Aurora config
DB_HOST = envs("DB_HOSTNAME")
DB_USERNAME = envs("DB_USERNAME")
DB_NAME = envs("DB_NAME")
DB_PASSWORD = envs("DB_PASSWORD")

# Others
LOG_LEVEL = envs("LOG_LEVEL", "INFO")
NOTIFICATION_CHANNEL = envs("NOTIFICATION_CHANNEL", "email")
NOTIFY_USER = envs("NOTIFY_USER", "recipe_analysis@dh.com")
NOTIFY_TO = envs("NOTIFY_TO", "data-engineers@dh.com")
