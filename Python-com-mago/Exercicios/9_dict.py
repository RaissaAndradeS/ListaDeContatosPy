tipo_sorvete = input("Qual é o tipo de sorvete? [casquinha/cascão/cestinha]")

sabor = input("Qual é o sabor de sorvete: [morango/creme/chocolate]")

cobertura = input("Qual cobertura deseja? [caramelo/morango/chocolate]")

valor = 0

sorvetes = {
    "casquinha": 1.00,
    "cascão": 2.50,
    "cestinha": 4.00 
}

valor = 0
if tipo_sorvete in sorvetes:
    valor += sorvetes[tipo_sorvete]
else:
    print("Pede direito!")


coberturas = {
    "caramelo":1.5,
    "morango": 1.5, 
    "chocolate": 1.5,
    "":0
}

if cobertura in coberturas:
    valor += coberturas[cobertura]
else: 
    print("Escolhe um válido")

print("Seu sorvete", tipo_sorvete, "de", sabor, "cobertura", cobertura, "custará: R$", valor)