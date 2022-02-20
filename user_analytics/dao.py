import logging


def get_order_status(bq_client, fullvisitorid):
    """Get the order status from bigquery based on the visior_id

    :param: bq_client: bigquery client
    :param: string: fullvisitorid - visitor_id to lookup
    :returns: dict: result - dictionary contains the response required
    """

    result = "No data found for the visitor_id {}".format(fullvisitorid)
    query_string = """
    SELECT * FROM
    (SELECT orderDate, common_name, deliveryType, backendOrderId, frontendOrderId, status_id, declinereason_code,
    declinereason_type, CAST(ST_X(ST_GEOGFROMTEXT(geopointCustomer)) AS STRING) as lat_customer,CAST(ST_Y(ST_GEOGFROMTEXT(geopointCustomer)) AS STRING) as long_customer, geopointDropoff
    FROM  `dhh-analytics-hiring-22.BackendDataSample.transactionalData`) td
    JOIN `dhh-analytics-hiring-22.GoogleAnalyticsSample.vw_location_change_old` vw ON vw.order_date = td.orderDate
    AND vw.latitude_end = td.lat_customer
    AND vw.longitude_end = td.long_customer
    WHERE fullvisitorid = '{}';""".format(fullvisitorid)

    dataframe = bq_client.query(query_string).result().to_dataframe()

    if not dataframe.empty:  # if visitor is present
        logging.info("Retrieved status from bigquery for visitor {}".format(fullvisitorid))
        result_set = dataframe.to_dict(orient='records')[0]  # take only the first record
        order_placed = True if result_set.get("backendOrderId") else False
        order_delivered = True if result_set.get("status_id") == 24 else False
        result = {"full_visitor_id": result_set.get("fullvisitorid"),
                  "address_changed": result_set.get("address_changed"),
                  "is_order_placed": order_placed,
                  "Is_order_delivered": order_delivered,
                  "application_type": result_set.get("operatingSystem")}
    return result
