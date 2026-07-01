import os
# select the directory path you want to list
path = "/"
# use the os module to list the conntents of the directory
contents = os.listdir(path)
# print the contents of the directory
for item in contents:
    print(item)