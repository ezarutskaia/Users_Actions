import os

dir_list = os.listdir("C:/dev/python/source/bigfiles/new")

for item in dir_list:
    os.system("py actions.py new/" + str(item))
    #print('py actions.py ' + (item))
