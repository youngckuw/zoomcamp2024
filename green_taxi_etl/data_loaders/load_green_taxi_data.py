import ssl

import io
import pandas as pd
import requests
from pandas import DataFrame

# for local development purpose
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(**kwargs) -> DataFrame:    
    taxi_dtypes = {
        'VendorID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'RatecodeID':pd.Int64Dtype(),
        'store_and_fwd_flag':str,
        'PULocationID':pd.Int64Dtype(),
        'DOLocationID':pd.Int64Dtype(),
        'payment_type': pd.Int64Dtype(),
        'fare_amount': float,
        'extra':float,
        'mta_tax':float,
        'tip_amount':float,
        'tolls_amount':float,
        'improvement_surcharge':float,
        'total_amount':float,
        'congestion_surcharge':float
    }

    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    green_tripdata_2020_10_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz'
    green_tripdata_2020_11_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz'
    green_tripdata_2020_12_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz'

    df_green_tripdata_2020_10 = pd.read_csv(green_tripdata_2020_10_url, sep=",", compression="gzip", dtype=taxi_dtypes, parse_dates=parse_dates)
    df_green_tripdata_2020_11 = pd.read_csv(green_tripdata_2020_11_url, sep=",", compression="gzip", dtype=taxi_dtypes, parse_dates=parse_dates)
    df_green_tripdata_2020_12 = pd.read_csv(green_tripdata_2020_12_url, sep=",", compression="gzip", dtype=taxi_dtypes, parse_dates=parse_dates)

    final_pd = pd.concat([df_green_tripdata_2020_10, df_green_tripdata_2020_11, df_green_tripdata_2020_12], ignore_index=True)

    return final_pd
    

# @test
# def test_output(df) -> None:
#     """
#     Template code for testing the output of the block.
#     """
#     assert df is not None, 'The output is undefined'
