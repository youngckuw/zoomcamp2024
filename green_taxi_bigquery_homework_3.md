```sql
  -- total row count
SELECT
  COUNT(*)
FROM
  `datacamp2004.ny_taxi.green_taxi_2022_homework_3`

  -- count distinct number of column value count
SELECT
  COUNT(DISTINCT PULocationID) AS distinct_count
FROM
  `datacamp2004.ny_taxi.green_taxi_2022_homework_3`
  
  -- count fare_amount = 0
SELECT
  COUNT(*)
FROM
  `datacamp2004.ny_taxi.green_taxi_2022_homework_3`
WHERE
  fare_amount = 0
  
  -- Partition by lpep_pickup_datetime Cluster on PUlocationID
-- used create table menu from the bigquery.
  
  -- Write a query to retrieve the distinct PULocationID between lpep_pickup_datetime 06/01/2022 and 06/30/2022 (inclusive)
SELECT
  DISTINCT PULocationID
FROM
  `datacamp2004.ny_taxi.green_taxi_2022_homework_3_partitioned_clustered`
WHERE
  lpep_pickup_datetime BETWEEN TIMESTAMP('2022-06-01')
  AND TIMESTAMP('2022-06-30');
```