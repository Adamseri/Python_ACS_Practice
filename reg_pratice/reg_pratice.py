import urllib3
import pandas as pd

http = urllib3.PoolManager()
resp = http.request('GET', 'https://amazon-bodym.s3.us-west-2.amazonaws.com/testA/measurements.csv', preload_content = False)

with open('measurements.csv', 'wb') as f:
    for chunk in resp.stream(1024):
        f.write(chunk)
resp.release_conn()
data = pd.read_csv('measurements.csv')
# run regression
print(data.head())