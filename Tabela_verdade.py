## Numeros 
# 1
# 10.0
# -5

#soma = 2 + 2 = 4

## Booleanos 
# True
# False 

# if idade >= 18

condicao = 12 > 18 # True ou False

if condicao:
    print("Isso é verdade")
else:
    print("Isso nunca vai acontecer")


## Exercicio 

idade = int(input("Entre com a sua idade: "))
cnh = input("Você tem CNH? ")

if idade >= 18 and cnh == 'sim':
    print("Siga em frente")

else:
    print("Preso em nome da lei!")

condicao = idade >= 18 and cnh == 'sim'
print(condicao)


## Mais facil, True é 1 e False é 0 

print(True * 100)

print(False * 100)


# So é verdade quando as 2 são verdadeiras no caso de E, AND, multiplicação

print(True * True)
print(False * True)
print(True * False)
print(False * False)

print(1 * 1)
print(0 * 1)
print(1 * 0)
print(0 * 0)

print("True e True =", 1 * 1)
print("False e True =", 0 * 1)
print("True e False =", 1 * 0)
print("False e False =", 0 * 0)

print("True e True =", bool(1 * 1))
print("False e True =", bool(0 * 1))
print("True e False =", bool(1 * 0))
print("False e False =", bool(0 * 0))


# OU soma

print("True ou True =", bool(1 + 1))
print("False ou True =", bool(0 + 1))
print("True ou False =", bool(1 + 0))
print("False ou False =", bool(0 + 0))