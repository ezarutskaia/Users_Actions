import pandas as pd
from urllib.parse import parse_qsl
import datetime
import numpy as np

dictionary = []

file1 = open("C:/dev/python/source/bigfiles/new/a1.txt", "r")

while True:
    line = file1.readline()
    if not line:
        break
    line = line.replace('\n','')
    dictionary.append(dict(parse_qsl(line)))

file1.close

df = pd.DataFrame(dictionary)

df['time'] = pd.to_datetime(df['time'])

new = df.groupby(['user']).agg({'time': ['min', 'max']}). reset_index()
new.columns = ['user', 't_min', 't_max']
new['t_diff'] = new['t_max'] - new['t_min']
new['diff_sec'] = new['t_diff'].dt.total_seconds()

p026 = np.percentile(new['diff_sec'], 0.26)

print()