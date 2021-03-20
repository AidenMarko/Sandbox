import os

print("The files are folders in {} are:".format(os.getcwd()))
items = os.listdir('.')
for item in items:
    print(item)
