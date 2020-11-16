import os
from os import listdir
from os.path import isfile, join
lista = []

filesnames = [f for f in listdir('mypath') if isfile(join('mypath', f))]


for x in range(len(filesnames)):
    if filesnames[x].count('('):
        lista.append(filesnames[x])



for x in range(len(lista)):
    file_path = f'mypath/{lista[x]}'
    try:
        os.remove(file_path)
    except OSError as e:
        print("Error: %s : %s" % (file_path, e.strerror))
