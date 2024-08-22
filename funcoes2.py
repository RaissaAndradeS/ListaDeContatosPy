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


a = 10
b = 20

c = a 
a = b
b = c

print(a, b)