## Instalar o Pillow e Rembg

from PIL import Image
import Rembg

def remover(caminho_entrada, caminho_saida):
    with open(caminho_entrada, "rb") as arquivo_entrada, open(caminho_saida "wb") as arquivo_saida

        imagem_entrada Image.open(arquivo_entrada)

        imagem_saida = rembg.remove(imagem_entrada)

        imagem_saida.save(arquivo_saida, "PNG")

Caminho_entrada = "colocar o caminho de entrada"
caminho_saida =  "colocar o caminho de saida/Nova.png"
remover(caminho_entrada, caminho_saida)

