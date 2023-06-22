import pandas as pd

dictionary = []

file1 = open("C:/dev/python/source/bigfiles/users1.txt", "r")

while True:
    line = file1.readline()
    if not line:
        break
    dictionary.append(dict(subString.split("=") for subString in line.split("&")))

file1.close

df = pd.DataFrame(dictionary)

print(df)