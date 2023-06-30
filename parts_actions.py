import os

filesize = 1024 * 1024 * 50
fileNumber = 1

fileSource = open("C:/dev/python/source/bigfiles/actions.txt", "r")

while True:
    line = fileSource.readline()
    if not line:
        break

    fileNew = open("C:/dev/python/source/bigfiles/new/a" + str(fileNumber) + ".txt", "a+")
    fileNew.write(line)
    fileNew.close()
    if os.path.getsize("C:/dev/python/source/bigfiles/new/a" + str(fileNumber) + ".txt") > filesize:
        fileNumber += 1

    

