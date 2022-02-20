CREATE EXTERNAL TABLE `dhh-analytics.GoogleAnalyticsSample.ga_sessions_export`
OPTIONS(
  format="PARQUET",
  uris=["gs://product-analytics-hiring-tests-public/GoogleAnalyticsSample/ga_sessions_export/*"]
);