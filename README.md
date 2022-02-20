# Bigquery - User Analytics
[![Python UnitTests](https://github.com/kjvijay23/user-analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/kjvijay23/user-analytics/actions/workflows/ci.yml)
#### Containerized Flask Application to get the user metrics from Bigquery

## Results
> SQL queries are in the `sql_scripts` folder
1. How many sessions are there?

    | total_sessions | session_with_events |
    | -------------- | ------------------- |
    | 216672 | 215925|

2. How many sessions does each visitor create?

    | sessions_per_visitor |
    | -------------------- |
    | 2.17509411233248     |
    
3. How much time does it take on average to reach the order_confirmation screen per
session (in minutes)? 

    | avg_order_time_in_minutes |
    | ------------------------- |
    | 34.01767111955396         |

4. By using the GoogleAnalyticsSample data and BackendDataSample tables, analyse
how often users tend to change their location in the beginning of their journey (screens
like home and listing) versus in checkout and on order placement and demonstrate the
the deviation between earlier and later inputs (if any) in terms of coordinates change.
Then, using the BackendDataSample table, see if those customers who changed their
address ended placing orders and if those orders were delivered successfully, if so, did
they match their destination.

### Installation
Create the docker image
```sh
docker build -t user_analytics .
```

Run the docker image
```sh
docker run -d -p 5000:5000 -e GOOGLE_APPLICATION_CREDENTIALS=/app/config.json --name user-analytics user_analytics
```
BigQuery table details
> All the SQL DDLs are provided in the `sql_scripts` folder
 - `ga_sessions_export` - GA raw hit data
 - `transactionalData`  - Backend order transactions data
 - `vw_location_change` - A unified view built on joining the GA dataset and BackendDataSample 
 
### Usage example
> Required `GOOGLE_APPLICATION_CREDENTIALS`  to run

### Examples
#### Healthcheck
- GET /heartbeat
```sh
curl -X GET "http://localhost:5000/heartbeat/"
```
#### Retrieve the order status
 - GET /orderStatus/{id}
> Gets the orderStatus of the given visitor_id

```sh
curl -X GET "http://localhost:5000/orderStatus/123456789"
```

### Tech Stack
  - GCP: BigQuery
  - Python
  - Flask
  - Docker
  
### Requirements
| Tool | Version |
| ------ | ------ |
| Python | 3.8 |
| Flask | 2.0.3 |
| Docker | Stable |
| GOOGLE_APPLICATION_CREDENTIALS | config.json |

Run command `pip install -r requirements.txt`. This file contains all the necessary libraries  to run the app.

### Execution
1. Execute `./build.sh` to build the docker image
2. Execute `./test.sh` to run the unittest cases and coverage report
3. Execute `./run.sh` to runs the flask application @ `http://localhost:5000/`
 
### Snapshots
    1. Test Coverage
![Coverage](https://user-images.githubusercontent.com/91729608/154835806-e67dc4e8-05a2-40f8-bb44-ad25f91d0ee6.png)

    2. API - Healthcheck 
![Healthcheck](https://user-images.githubusercontent.com/91729608/154835966-dd1c12cd-e1dd-466a-90b9-4d1971a8bcfb.png)

    3. API - OrderStatus 
![orderStatus](https://user-images.githubusercontent.com/91729608/154835992-4d475126-7ee1-426e-98ef-1995a6d63057.png)

    4. API - OrderException 
![OrderException](https://user-images.githubusercontent.com/91729608/154836019-e8456443-4f03-42b9-a0f9-9af164b41f41.png)
