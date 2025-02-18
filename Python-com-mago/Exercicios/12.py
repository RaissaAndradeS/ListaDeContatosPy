total = 0 

entrada = "x"

while True:

    entrada = input("Digite um valor de saldo: ")
    if entrada == "":
        break

    total += float(entrada)

print(total)