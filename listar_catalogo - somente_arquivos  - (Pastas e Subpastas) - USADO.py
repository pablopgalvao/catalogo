import os

def gerar_html(caminho):
    with open("lista_arquivos.html", "w", encoding="utf-8") as arquivo_html:
        arquivo_html.write("<html>\n")
        arquivo_html.write("<head><title>Lista de Músicas</title></head>\n")
        arquivo_html.write("<body>\n")
        arquivo_html.write("<h1>Lista de Músicas</h1>\n")
        arquivo_html.write("<table border='1'>\n")
        arquivo_html.write("<tr><th>Caminho do Arquivo</th></tr>\n")

        for raiz, pastas, arquivos in os.walk(caminho):
            for arquivo in arquivos:
                caminho_completo = os.path.join(raiz, arquivo)
                arquivo_html.write(f"<tr><td>{caminho_completo}</td></tr>\n")

        arquivo_html.write("</table>\n")
        arquivo_html.write("</body>\n")
        arquivo_html.write("</html>\n")

if __name__ == "__main__":
    caminho = input('Digite o caminho: ')

    try:
        os.chdir(caminho)
        print(os.getcwd())
        gerar_html(caminho)
        print("Página HTML gerada com sucesso: lista_arquivos.html")
    except FileNotFoundError:
        print("Caminho não encontrado.")
    except PermissionError:
        print("Permissão negada para acessar o caminho.")
