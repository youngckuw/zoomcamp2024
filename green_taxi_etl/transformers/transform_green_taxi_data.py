import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    print(data.shape[0])
    print(data.shape[1])

    data.columns = (data.columns
                    .str.replace(' ', '_')
                    .str.lower()
    )

    data.rename(columns={'vendorid': 'vendor_id'}, inplace=True)
    data.rename(columns={'ratecodeid': 'rate_code_id'}, inplace=True)
    data.rename(columns={'pulocationid': 'pu_location_id'}, inplace=True)
    data.rename(columns={'dolocationid': 'do_location_id'}, inplace=True)    
    
    data = data[(data['passenger_count'] != 0) & (data['trip_distance'] != 0)]
    
    data['lpep_pickup_datetime'] = pd.to_datetime(data['lpep_pickup_datetime'], unit='ms')
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    data['lpep_dropoff_datetime'] = pd.to_datetime(data['lpep_dropoff_datetime'], unit='ms')
    data['lpep_dropoff_date'] = data['lpep_dropoff_datetime'].dt.date

    print(data.shape[0])
    print(data.shape[1])

    print(data['vendor_id'].unique())
 
    return data


@test
def test_output(output, *args) -> None:
    assert 'vendor_id' in output.columns, 'column vendor_id should exist'
    assert (output['passenger_count'] > 0).all(), 'passenger_count should not be less than 0'
    assert (output['trip_distance'] > 0).all(), 'trip_distance should not be less than 0'
    assert output is not None, 'The output is undefined'
