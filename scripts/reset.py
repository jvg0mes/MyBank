import shelve
import os
from services.schema import schemas

dbpath = './mocks'

os.chdir(dbpath)

del_list = []

for e in list(schemas.keys()):

    files = os.listdir()
    
    for x in files:
        if x.__contains__(e):
            del_list.append(x)
    
for x in del_list:
    os.remove(x)

dbase = shelve.open('dbase')

for k,v in dbase.items():
    dbase.update({k:0})
