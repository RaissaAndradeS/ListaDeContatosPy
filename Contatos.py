agenda = {}

# Pedir o nome e telefone do contato 
# Associar as variáveis 
# Print resultados

def adicionar():
    nome = input("Qual é o nome do contato? ").strip().title()
    telefone = input("Qual é o telefone para contato? ").strip()
    agenda[nome] = telefone
    print("Contato adicionado com sucesso!")

# Exibe uma lista de contatos 

def exibir():
    if agenda:
        print("Lista de Contatos:")
    for nome, telefone in agenda.items():
        print(f"Nome: {nome}")
        print(f"Telefone: {telefone}")
        print("-"*30)
    else:
        print("Contato não encotrado")

# Pergunta o nome do contato e verifica se ele existe
# Retorna o resultado 

def buscar():
    nome = input("Qual é o nome do contato que deseja buscar? ")
    if nome in agenda: 
        print("-"*30)
        print(f"Nome: {nome}")
        print(f"Telefone: {agenda[nome]}")
        print("-"*30)
    else:
        print("Contato não encontrado")
    print("-"*30)

# Pedir o contato para deletar, verifica se o contato existe e retorna o resultado 

def deletar():
    nome = input("Qual é o contato que deseja deletar? ")
    if nome in agenda:
        del agenda[nome]
        print("-"*30)
        print("Contato deletado com sucesso!")
        print("-"*30)
    else:
        print("-"*30)
        print("Contato não encontrado")
        print("-"*30)

def menu():
    print("1. Para adicionar um contato")
    print("2. Para exibir a lista de contatos")
    print("3. Para buscar um contato")
    print("4. Para deletar um contato")
    print("5. Para sair da lista")

def finalizar():
    print("1. Sim")
    print("2. Não")

def loop():
    while True:
        menu()
        x = input("Escolha uma opção: ")

        if x == "1":
            adicionar()
            finalizar()
            y = input("Deseja algo mais? ")
            if y == "1":
                loop()
            elif y == "2":
                print("Até a próxima")
                break

        if x == "2":
            exibir()
            finalizar()
            y = input("Deseja algo mais? ")
            if y == "1":
                loop()
            elif y == "2":
                print("Até a próxima")
                break

        if x == "3":
            buscar()
            finalizar()
            y = input("Deseja algo mais? ")
            if y == "1":
                loop()
            elif y == "2":
                print("Até a próxima")
                break

        if x == "4":
            deletar()
            finalizar()
            y = input("Deseja algo mais? ")
            if y == "1":
                loop()
            elif y == "2":
                print("Até a próxima")
                break

        if x == "5":
            print("Até a próxima")
            break


loop()