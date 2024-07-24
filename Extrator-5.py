import re 
import requests # Instalar biblioteca 

def extrair_links_pagina(url):
    try:
        resposta = requests.get(url)
        conteudo = resposta.text
        links = re.findall(r'href=[\'](https?://.*)(?=["\'])', conteudo)
        return links
    except Exception as e:
        print(f"Erro ao extrair links: {str(e)}")
        return []

if __name__ == "__main__":
    url = input("Digite a url desejada para extrair links: ")
    links = extrair_links_pagina(url)

    if links:
        print("Links encontrados: ")
        for link in links:
            print(link)
    else:
        print(f"Nenhum link foi encontrado!")
