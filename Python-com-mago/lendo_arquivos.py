
## Para abrir arquivo

## Reescrever o arquivo 
arquivo = open("arquivo.txt", 'w')

# Para adicionar info 

arquivo = open("arquivo.txt", 'a+')

## Para escrever 

arquivo.write("fodase")

# Para fechar o arquivo 

arquivo.close()


## Para ler o arquivo 

arquivo = open("arquivo.txt", 'r')
conteudo = arquivo.read()
arquivo.close()

print(conteudo)
print(type(conteudo))

## Outra forma de leitura do arquivo 

arquivo = open("arquivo.txt", 'r')
linhas = arquivo.readlines()
arquivo.close()

print(linhas)
print(type(linhas))


## Trabalhando com with

with open("arquivo.txt", "r") as file:
    conteudo = file.read()

print(conteudo)