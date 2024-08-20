numero = int(input("Fala um número de 1 a 15 "))

numero_sorte = 8

if numero == numero_sorte:
    print("você acertou!")
elif numero> numero_sorte:
    print("Você errou! Tente um numero menor.")
else:
    print("Você errou! Tente um numero maior")