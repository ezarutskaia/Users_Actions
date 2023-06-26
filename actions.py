import pandas as pd
from urllib.parse import parse_qsl
from mysql.connector import connect, Error

dictionary = []

file1 = open("C:/dev/python/source/bigfiles/actions1.txt", "r")

while True:
    line = file1.readline()
    if not line:
        break
    line = line.replace('\n','')
    dictionary.append(dict(parse_qsl(line)))

file1.close

df = pd.DataFrame(dictionary)
df['date'] = pd.to_datetime(df.date, dayfirst=True)

try:
    with connect(
        host="localhost",
        user="root",
        password="secret",
        database="Users_Actions",
        port="4306",
    ) as connection:

        with connection.cursor(buffered=True) as cursor:
            for ind in df.index:
                query = "INSERT INTO Actions (user, time, date, uuid) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (df['user'][ind], df['time'][ind], df['date'][ind], df['uuid'][ind]))
                connection.commit()

except Error as e:
    print('Error:',e)

print(df.head(5))