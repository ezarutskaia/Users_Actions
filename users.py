import pandas as pd
from urllib.parse import parse_qsl

dictionary = []

file1 = open("C:/dev/python/source/bigfiles/users1.txt", "r")

while True:
    line = file1.readline()
    if not line:
        break
    line = line.replace('\n','')
    dictionary.append(dict(parse_qsl(line)))

file1.close

df = pd.DataFrame(dictionary)

expanded = df['location'].str.split(pat="', '", expand=True)
df['lot'] = expanded[0]
df['lng'] = expanded[1]
df['city'] = expanded[2]

search = lambda s: s.lstrip("['")
df['lot'] = df['lot'].map(search)

df = df.drop(columns='location')

print(df.info())