import os

filesize = 120 * 5
fileNumber = 1

fileSource = open("C:/dev/python/source/bigfiles/actions1.txt", "r")

while True:
    line = fileSource.readline()
    if not line:
        break

    fileNew = open("C:/dev/python/source/bigfiles/new/a" + str(fileNumber) + ".txt", "a+")
    fileNew.write(line)
    fileNew.close()
    if os.path.getsize("C:/dev/python/source/bigfiles/new/a" + str(fileNumber) + ".txt") > filesize:
        fileNumber += 1

    

