numero_sorte = 8

for i in range(3):

    while True:
        try:
            numero = int(input("Entre com um número entre 1 e 15: "))
            break

        except ValueError:
            print("Digita um NÚMERO!")

    if numero == numero_sorte:
        print("Você acertou!")
        break

    elif numero > numero_sorte:
        print("Você errou! Tente um número menor!")
    else:
        print("Você errou! Tente um número maior")


## ---------------------------- ##

## Try e except 

try:
    numero = int(input("Digita ai um número: "))

except ValueError as err:
    print("My consagrete, pedi um NÚMERO!")
 