import boto3
import pandas as pd

client = boto3.client('ce', region_name='ap-south-1')

response = client.get_cost_and_usage(
    TimePeriod={
        'Start': '2022-06-01',
        'End': '2022-07-01'
    },
    Granularity='MONTHLY',
    Metrics=[
        'AmortizedCost',
    ]
)


a = response["ResultsByTime"]

final = a[0]['Total'] 

df = pd.DataFrame(final).T
df.to_csv('file.csv')