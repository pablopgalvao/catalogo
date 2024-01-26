import os

def listar_arquivos(caminho):
    for raiz, pastas, arquivos in os.walk(caminho):
        for arquivo in arquivos:
            caminho_completo = os.path.join(raiz, arquivo)
            print(caminho_completo)

if __name__ == "__main__":
    caminho = input('Digite o caminho: ')

    try:
        os.chdir(caminho)
        print(os.getcwd())
        listar_arquivos(caminho)
    except FileNotFoundError:
        print("Caminho não encontrado.")
    except PermissionError:
        print("Permissão negada para acessar o caminho.")
