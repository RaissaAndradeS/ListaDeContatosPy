qtde = int(input(" Quantos fodases você quer? "))

count = 1 
while count <= qtde:
    print("Fodase!")
    count += 1 # count = count + 1


## Break

while True:
    
    senha = input("Entre com a senha: ")
    if senha == "fodase":
        break
    else:
        print("fodase")

print("Saí, porra")


## continue

while True:
    
    senha = input("Entre com a senha: ")
    if senha == "fodase":
        break
    elif senha == 'raissinha':
        print("quase")
        continue
    
    print("fodase")

print("Saí, porra")



## De 2 em 2

contador = 1
while contador <= 15:

    if contador % 2 == 0:
        print(contador)

    contador += 1