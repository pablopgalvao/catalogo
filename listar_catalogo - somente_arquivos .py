#Se sua pretensão for listar apenas os arquivos de um determinado diretório você pode:

#Informar o caminho do diretório;
#Solicitar a exibição dos arquivos deste diretório.


from os import chdir, getcwd, listdir
from os.path import isfile

cam = input('Digite o caminho: ')

chdir(cam)
print(getcwd())

for c in listdir():
    if isfile(c):
        print(c)
