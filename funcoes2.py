def soma(*args):
    total = 0

    for i in args:
        total += i

    return total

soma(10, 20, 100)


## ----------------------- ##

dados = ['teozin', 'calvin', 31, ['pqp', 'chata', 'calva']]

nome, sobrenome, *lixo = dados

print(nome)
print(sobrenome)

## *_ o resto vai pro lixo, fica so os dois primeiros nesse caso 

## ----------------------------- ##

# Reatribuindo valores 

a = 10
b = 20
print(a, b)

a,b = b,a

## Mesma coisa que tupla 

## ----------------------------- ##


## Docstring 

"""Documentar a função :))"""