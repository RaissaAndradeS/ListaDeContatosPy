segundos = int(input("Entre com um némoro em segundos: "))

horas = segundos // (60*60) # horas 

segundos = segundos % (60*60) # resto de segundos da divisão por hora

minutos = segundos // 60  # minutos inteiros

segundos = segundos % 60 # resto de segundos da divisão de minutos 

print(horas, ":", minutos, ":", segundos, sep="")

