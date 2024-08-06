## if 

idade = int(input("Entre com sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")


## else 

idade = int(input("Entre com a sua idade: "))

if idade >= 18:
    print("Você é maior de idade")

else: 
    print("Você é muito jovem.")


## elif 

idade = int(input("Entre com a sua idade: "))

if idade < 18:
    print("Você é menor de idade")

elif idade > 90:
    print("Cuidado, você ta velhinho.")

else:
    print("Beba a vontade")

##  Outra forma 

if 18 <= idade <= 89:
    print("Você é maior de idade")

elif idade >= 90:
    print("você precisa se cuidar")

else: 
    print("Você é neném ainda.")

