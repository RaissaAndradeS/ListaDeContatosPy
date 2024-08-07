for i in "Raissa":

    if i == "R":
        continue 

    elif i == " ":
        continue

    print(i)


## Range

seq = range(0, 10) #start, stop = qtde = stop - start 

for i in seq:
    print(i)


## Fodase

qtde = int(input("Quantos fodases você quer? "))

for i in range(qtde):
    print("fodase")