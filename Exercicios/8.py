escolha = input("Você quer qual água, mineral ou com gás? [mineral/gas]: ")

quantidade = int(input("Quantas águas você deseja? "))

total = 0

if escolha == "mineral":
    total = 1.5 * quantidade

elif escolha == "gas":
    total = 2.5 * quantidade

else:
    print("Faça uma escolha válida")

print("Fica R$:", total)
