# Lista vazia

minha_lista = []

# Lista

minha_lista = ['raissa', 'andrade', 25]
print(minha_lista)

# Acessando os elementos da lista 

minha_lista[0]

minha_lista[1]

minha_lista[2]

# Tamanho da lista

indice = len(minha_lista)-1
minha_lista[indice]

## Ou 

minha_lista[len(minha_lista)-1]

minha_lista[-1]


## Fatiamento de lista

minha_lista[0:2]

# Ultimo elemento 

minha_lista[0:-1]


## de dois em dois 

minha_lista[::2] #start:stop:step

# Ao contrario 

minha_lista[::-1]


### Aula 4 

minha_lista = ['raissa', 'andrade', 25, 2.88]

# primeiro elemento

minha_lista[0]

# segundo elemento

minha_lista[1]

# ultimo elemento

minha_lista[-1]

# slice (fatiamento)

minha_lista[:2]

# dois ultimos 

minha_lista[-2:]

# copia

nova_lista = minha_lista[:]
print(nova_lista)

# step - fim para inicio 

minha_lista[::-1]

# step de 2 em 2 

minha_lista[::2]

## Exemplo para add nota 

notas = []

nota = 7.75

notas.append(nota)

print(notas)

notas.append(10)
print(notas)


# append só permite um único elemento 

notas.append()

## add dois 

notas.extend([5.75, 6.24])
print(notas)

## ou 

notas = notas + [10, 9.25]
print(notas)


# Uma variavel nova que é a antiga em caixa alta, 
# com lista funciona diferente, ela altera a própria lista 

nome = 'raissa'
nome_alto = nome.upper()
print(nome_alto)


## Listas com for 

nomes = ['raissa', 'raicca', 'jose']
for i in nomes:
    print( i.title() )

