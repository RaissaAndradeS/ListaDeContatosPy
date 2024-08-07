tipo_sorvete = input("Qual é o tipo de sorvete? [casquinha/cascão/cestinha]")

sabor = input("Qual é o sabor de sorvete: [morango/creme/chocolate]")

cobertura = input("Qual cobertura deseja? [caramelo/morango/chocolate]")

valor = 0

if tipo_sorvete == 'casquinha':
    valor = valor + 1.00

elif tipo_sorvete == 'cascão':
    valor += 2.50

elif tipo_sorvete == 'cestinha':
    valor += 4.00

else: 
    print("Escolha corretamente.")

if cobertura == 'caramelo':
    valor += 1.50

elif cobertura == 'morango':
    valor += 1.50

elif cobertura == 'chocolate':
    valor += 1.50

elif cobertura == '':
    pass

else:
    print("Escolha algo válido.")

print("Seu sorvete", tipo_sorvete, "de", sabor, "cobertura", cobertura, "é de R$:", valor)