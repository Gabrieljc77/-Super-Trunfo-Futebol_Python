# Integrantes: Gabriel Jardim, Gabriel Alonso e Nicolas Gabriel

import random

def criar_gabarito():
    return ["Nome", "Ataque", "Meio-campo", "Defesa"]

def criar_baralho():
    return [
        ["Flamengo", 80, 77, 77],
        ["Palmeiras", 79, 77, 78],
        ["Corinthians", 76, 75, 74],
        ["São Paulo", 76, 75, 74],
        ["Atlético Mineiro", 77, 76, 76],
        ["Botafogo", 76, 76, 75],
        ["Fluminense", 75, 76, 74],
        ["Grêmio", 75, 74, 74]
    ]

def exibir_topo(baralho, gabarito):
    carta = baralho[0]

    for i in range(len(gabarito)):
        print(f"{gabarito[i]} : {str(carta[i])}")

def valida_escolha():
    escolha = int(input())

    while escolha < 1 or escolha > 3:
        escolha = int(input())

    return escolha

def distribuir_cartas(baralho):
    random.shuffle(baralho)

    mao1 = []
    mao2 = []

    for i in range(len(baralho)):
        if i % 2 == 0:
            mao1.append(baralho[i])
        else:
            mao2.append(baralho[i])

    return mao1, mao2

def escolher_atributo(gabarito):
    print("Escolha um atributo:")

    for i in range(1, len(gabarito)):
        print(str(i) + " - " + gabarito[i])

    return valida_escolha()

def comparar_cartas(mao1, mao2, atributo):
    if mao1[0][atributo] > mao2[0][atributo]:
        return 1
    elif mao2[0][atributo] > mao1[0][atributo]:
        return 2
    else:
        return 0

def atualizar_maos(mao1, mao2, vencedor):
    if vencedor == 1:
        mao1.append(mao2[0])
        mao2.pop(0)
    elif vencedor == 2:
        mao2.append(mao1[0])
        mao1.pop(0)

def guardar_empate(mao1, mao2, monte_espera):
    monte_espera.append(mao1[0])
    monte_espera.append(mao2[0])
    mao1.pop(0)
    mao2.pop(0)

def entregar_monte(mao, monte_espera):
    for i in range(len(monte_espera)):
        mao.append(monte_espera[i])

    monte_espera.clear()

def mostrar_placar(mao1, mao2):
    print(f"Cartas do Jogador 1: {(len(mao1))}")
    print(f"Cartas do Jogador 2: {(len(mao2))}")

def jogar(modo):
    gabarito = criar_gabarito()
    baralho = criar_baralho()
    mao1, mao2 = distribuir_cartas(baralho)
    monte_espera = []
    jogador_da_vez = 1

    while len(mao1) > 0 and len(mao2) > 0:
        print()
        mostrar_placar(mao1, mao2)
        print(f"Jogador da vez: {str(jogador_da_vez)}")

        if modo == 1 and jogador_da_vez == 2:
            atributo = random.randint(1, 3)
            print(f"Computador escolheu: {gabarito[atributo]}")
        else:
            if jogador_da_vez == 1:
                exibir_topo(mao1, gabarito)
            else:
                exibir_topo(mao2, gabarito)

            atributo = escolher_atributo(gabarito)

        print(f"Jogador 1 - {gabarito[atributo]}: {str(mao1[0][atributo])}")
        print(f"Jogador 2 - {gabarito[atributo]}: {str(mao2[0][atributo])}")

        vencedor = comparar_cartas(mao1, mao2, atributo)

        if vencedor == 1:
            print("Jogador 1 venceu a rodada.")
            atualizar_maos(mao1, mao2, 1)
            entregar_monte(mao1, monte_espera)
            jogador_da_vez = 1
        elif vencedor == 2:
            print("Jogador 2 venceu a rodada.")
            atualizar_maos(mao1, mao2, 2)
            entregar_monte(mao2, monte_espera)
            jogador_da_vez = 2
        else:
            print("Empate. As cartas foram para o monte de espera.")
            guardar_empate(mao1, mao2, monte_espera)

    print()
    if len(mao1) > len(mao2):
        print("Jogador 1 venceu o jogo.")
    elif len(mao2) > len(mao1):
        print("Jogador 2 venceu o jogo.")
    else:
        print("O jogo terminou empatado.")

def menu():
    opcao = 0

    while opcao != 3:
        print()
        print("1 - Single Player")
        print("2 - Multiplayer")
        print("3 - Sair")

        opcao = valida_escolha()

        if opcao == 1:
            jogar(1)
        elif opcao == 2:
            jogar(2)
        elif opcao == 3:
            print("Programa finalizado.")

menu()
