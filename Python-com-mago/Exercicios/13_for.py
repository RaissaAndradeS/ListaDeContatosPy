## Exercicio 8

alturas = []

for i in range(4):

    a = int(input(f"Entre com as alturas em cm {i+1}: "))
    alturas.append(a)

soma = sum(alturas)
print(soma)

