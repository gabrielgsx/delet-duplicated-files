import os
from os import listdir
from os.path import isfile, join
lista = []

filesnames = [f for f in listdir('E:/2019-03') if isfile(join('E:/2019-03', f))]


for x in range(len(filesnames)):
    if filesnames[x].count('('):
        lista.append(filesnames[x])



for x in range(len(lista)):
    file_path = f'E:/2019-03/{lista[x]}'
    try:
        os.remove(file_path)
    except OSError as e:
        print("Error: %s : %s" % (file_path, e.strerror))
