CREATE OR REPLACE VIEW `dhh-analytics.GoogleAnalyticsSample.vw_location_change`
AS SELECT a.fullvisitorid, PARSE_DATE('%Y%m%d',  a.date) AS order_date, a.operatingSystem,a.latitude_start, b.latitude_end,a.longitude_start, b.longitude_end, ST_DISTANCE(ST_GEOGPOINT(CAST(a.latitude_start as FLOAT64),CAST(a.longitude_start as FLOAT64)),
ST_GEOGPOINT(CAST(b.latitude_end as FLOAT64),CAST(b.longitude_end as FLOAT64))) as coordinate_difference,
NOT ST_EQUALS(ST_GEOGPOINT(CAST(a.latitude_start as FLOAT64),CAST(a.longitude_start as FLOAT64)),
ST_GEOGPOINT(CAST(b.latitude_end as FLOAT64),CAST(b.longitude_end as FLOAT64))) AS address_changed
FROM 
(SELECT fullvisitorid, date, operatingSystem,
CASE
    WHEN latitude_begin ='NA' THEN '0'
    WHEN latitude_begin ='N/A' THEN '0'
    WHEN latitude_begin ='null' THEN '0'
    ELSE IFNULL(latitude_begin, '0')
  END
  AS latitude_start,
  CASE
    WHEN longitude_begin ='NA' THEN '0'
    WHEN longitude_begin ='N/A' THEN '0'
    WHEN longitude_begin ='null' THEN '0'
    ELSE IFNULL(longitude_begin, '0')
  END
  AS longitude_start,
start_screen
FROM (SELECT 
  fullvisitorid, date, operatingSystem,
  MAX(IF(index = 18, value, NULL)) AS latitude_begin,
  MAX(IF(index = 19, value, NULL)) AS longitude_begin,
  MAX(IF(index = 11, value, NULL)) AS start_screen
FROM 
(SELECT
  fullvisitorid, visitNumber, visitStartTime, date, visits, hits, timeOnSite, transactions, transactionRevenue,
  newVisits, screenviews, uniqueScreenviews, timeOnScreen, totalTransactionRevenue, source, medium, browser, operatingSystem, isMobile, deviceCategory, country,
  lists.element.hitNumber, lists.element.time, lists.element.hour, lists.element.isInteraction, lists.element.isEntrance, lists.element.isExit, lists.element.type, lists.element.name, lists.element.landingScreenName, lists.element.screenName, lists.element.eventCategory, lists.element.eventAction, lists.element.eventLabel, lists.element.transactionId, cd.element.INDEX, cd.element.value
FROM
  `dhh-analytics.GoogleAnalyticsSample.ga_sessions_export`,
  UNNEST(hit.list) lists,
  UNNEST(element.customDimensions.list) cd)
    GROUP BY fullvisitorid, date, operatingSystem)
      WHERE (start_screen = 'home' or start_screen = 'shop_list')) a
    INNER JOIN
(SELECT fullvisitorid, date, operatingSystem,
CASE
    WHEN latitude_end ='NA' THEN '0'
    WHEN latitude_end ='N/A' THEN '0'
    WHEN latitude_end ='null' THEN '0'
    ELSE IFNULL(latitude_end, '0')
  END
  AS latitude_end,
  CASE
    WHEN longitude_end ='NA' THEN '0'
    WHEN longitude_end ='N/A' THEN '0'
    WHEN longitude_end ='null' THEN '0'
    ELSE IFNULL(longitude_end, '0')
  END
  AS longitude_end
FROM
    (SELECT 
  fullvisitorid, date, operatingSystem,
  MAX(IF(index = 18, value, NULL)) AS latitude_end,
  MAX(IF(index = 19, value, NULL)) AS longitude_end
FROM 
(SELECT
  fullvisitorid, visitNumber, visitId, visitStartTime, date, visits, hits, timeOnSite, transactions, transactionRevenue,
  newVisits, screenviews, uniqueScreenviews, timeOnScreen, totalTransactionRevenue, source, medium, browser, operatingSystem, isMobile, deviceCategory, country,
  lists.element.hitNumber, lists.element.time, lists.element.hour, lists.element.isInteraction, lists.element.isEntrance, lists.element.isExit, lists.element.type, lists.element.name, lists.element.landingScreenName, lists.element.screenName, lists.element.eventCategory, lists.element.eventAction, lists.element.eventLabel, lists.element.transactionId, cd.element.INDEX, cd.element.value
FROM
  `dhh-analytics.GoogleAnalyticsSample.ga_sessions_export`,
  UNNEST(hit.list) lists,
  UNNEST(element.customDimensions.list) cd)
  WHERE (eventAction = 'checkout.clicked' or eventAction = 'checkout.clicked')
GROUP BY fullvisitorid, date, operatingSystem)) b
on a.fullvisitorid = b.fullvisitorid AND
a.date = b.date;