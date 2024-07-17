from random import choice

# Jogo de pedra, papel e tesoura 

vitorias_jogador = 0
vitorias_maquina = 0

def opcao_jogador():
    jogador = input("Escolha Pedra, Papel ou Tesoura: ").strip()
    jogador.lower()
    if jogador == "pedra":
        return jogador
    elif jogador == "papel":
        return jogador
    elif jogador == "tesoura":
        return jogador
    else:
        print("Opção inexistente! Tente novamente")
        opcao_jogador()

def opcao_maquina():
    maquina = choice(["pedra", "papel", "tesoura"])
    return maquina


while True:
    print("*"*25)
    jogador = opcao_jogador()
    maquina = opcao_maquina()
    print("*"*25)


    if (jogador == "pedra") and (maquina == "tesoura")\
        or (jogador == "papel") and (maquina == "pedra")\
            or (jogador == "tesoura") and (maquina == "papel"):
        print(f"A maquina colocou {maquina}, jogador venceu!! ")
        vitorias_jogador += 1 
    elif jogador == maquina:
        print(f"A maquina colocou {maquina}, empatou!")
    else:
        print(f"A maquina colocou {maquina}, maquina venceu!! ")
        vitorias_maquina += 1
    
    print("*"*25)
    print(f"Placar do Jogador: {vitorias_jogador}")
    print(f"Placar da Maquina: {vitorias_maquina}")
    print("*"*25)

    jogador = input("Deseja jogar novamente? ")
    if jogador in ["SIM", "Sim", "sim", "S", "s"]:
        pass
    elif jogador in ["NAO", "Nao", "nao", "N", "n"]:
        break
    else:
        break