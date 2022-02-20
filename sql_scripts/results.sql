-- 1. How many sessions are there?

	SELECT count(*) as total_sessions,  (
	SELECT sum(visits) as total_sessions FROM `dhh-analytics.GoogleAnalyticsSample.ga_sessions_export`) session_with_events 
	FROM  `dhh-analytics.GoogleAnalyticsSample.ga_sessions_export`;
	
-- 2. How many sessions does each visitor create?

	SELECT
	  count(DISTINCT concat(fullvisitorid, visitStartTime)) / count(distinct fullvisitorid) as sessions_per_visitor
	FROM  `dhh-analytics.GoogleAnalyticsSample.ga_sessions_export`;
 	
-- 3. How much time does it take on average to reach the order_confirmation screen per session (in minutes)?
   
   SELECT
	  AVG(TIMESTAMP_DIFF(TIMESTAMP_MICROS(visitStartTime*1000000 + lists.element.time*1000),
    TIMESTAMP_MICROS(visitStartTime*1000000), MINUTE)) as avg_order_time_in_minutes
	FROM `dhh-analytics.GoogleAnalyticsSample.ga_sessions_export`,
	UNNEST(hit.list) lists,
	UNNEST(element.customDimensions.list) cd
    WHERE cd.element.value = 'order_confirmation';
