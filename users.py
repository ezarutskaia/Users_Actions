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

print(df)