nome = input("Entre com seu nome completo: ")

nome = nome.lower()

if "andrade" in nome:
    print("Pertence a familia andade")

else:
    print("Não pertence a familia andrade")


## Outro 

nome = input("Entre com seu nome : ")

nome = nome.lower()

if "andrade" in nome or "silva" in nome:
    print("Pertence a familia andrade ou silva")

else:
    print("Num te conheço")


## Outro 

lista = "laranja, cerveja, miojo, carvão, picanha"

item = input("O que vocÊ quer comprar?  [laranja, cerveja, miojo, carvão, picanha] ")

if item in lista:
    print("Pode passar!")

else: 
    print("Num tem esse item!")