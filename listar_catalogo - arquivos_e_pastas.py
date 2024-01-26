#Agora, se você pretende exibir todo o conteúdo de um determinado diretório - pastas e arquivos - você pode:

#Informar o caminho do diretório;
#Solicitar a exibição de todo o conteúdo do respectivo diretório.

from os import chdir, getcwd, listdir

cam = input('Digite o caminho: ')

chdir(cam)
print(getcwd())

for c in listdir():
    print(c)
