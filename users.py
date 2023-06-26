import pandas as pd
from urllib.parse import parse_qsl
from mysql.connector import connect, Error

dictionary = []

file1 = open("C:/dev/python/source/bigfiles/users.txt", "r")

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
                query = "INSERT INTO Users (uuid, ip, page, user_agent, hash, code, lot, lng, city) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (df['uuid'][ind], df['ip'][ind], df['page'][ind], df['user_agent'][ind], df['hash'][ind], df['code'][ind], df['lot'][ind], df['lng'][ind], df['city'][ind] ))
                connection.commit()

except Error as e:
    print('Error:',e)

#print(df.info())