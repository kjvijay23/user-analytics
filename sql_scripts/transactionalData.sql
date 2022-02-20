CREATE EXTERNAL TABLE `dhh-analytics.BackendDataSample.transactionalData`
OPTIONS(
  format="PARQUET",
  uris=["gs://product-analytics-hiring-tests-public/BackendDataSample/transactionalData/*"]
);