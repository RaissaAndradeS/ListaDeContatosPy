## Código espaguete 

def valida_entrada():
    while True:
        try:
            numero = int(input("Entre com um número entre 1 e 15: "))
            return numero

        except ValueError:
            print("Digita um NÚMERO!")
            continue

        if 1 <= numero <=15:
            return numero
        else:
            print("Fale um número válido")


numero_sorte = 8

for i in range(3):

    numero = valida_entrada()

    if numero == numero_sorte:
        print("Você acertou!")
        break

    elif numero > numero_sorte:
        print("Você errou! Tente um número menor!")
    else:
        print("Você errou! Tente um número maior")



## or 

def check_input():
    try:
        return int(input("Entre com um número entre 1 e 15: "))

    except ValueError:
        return "Escreva um número!"

def check_interval(numero):
    return 1 <= numero <= 15


def valida_entrada():
    while True:

        numero = check_input()

        if type(numero) != int:
            print(numero)
            continue

        if check_interval(numero):
            return numero


numero_sorte = 8

for i in range(3):

    numero = valida_entrada()

    if numero == numero_sorte:
        print("Você acertou!")
        break

    elif numero > numero_sorte:
        print("Você errou! Tente um número menor!")
    else:
        print("Você errou! Tente um número maior")