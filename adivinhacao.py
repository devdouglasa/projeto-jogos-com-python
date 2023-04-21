from random import randint
import os

def jogar():
    print("=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-")
    print("Bem vindo ao jogo de adivinhação!")
    print("=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-")

    chute_maquina = randint(1, 101)
    total_tentativas = 3
    rodada = 1
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil ")

    nivel = int(input("Digite o nível: "))

    if nivel == 1:
        total_tentativas = 15
    elif nivel == 2:
        total_tentativas = 10
    elif nivel == 3:
        total_tentativas = 5
    else:
        while nivel < 1 or nivel > 3:
            os.system('clear')
            print("Digite um número válido!")
            print("(1) Fácil (2) Médio (3) Difícil ")
            nivel = int(input("Digite o nível: "))
            if nivel == 1:
                total_tentativas = 15
            elif nivel == 2:
                total_tentativas = 10
            elif nivel == 3:
                total_tentativas = 5

    while rodada <= total_tentativas:

        print(f'Tentativa {rodada:02d} de {total_tentativas:02d}')
        chute_usuario = int(input("Digite um número [1 à 100]: "))

        if (chute_usuario < 1 or chute_usuario > 100):
            print("Você deve digitar um número de 1 à 100!")
            continue

        acertou = (chute_usuario == chute_maquina)
        maior = (chute_usuario > chute_maquina)
        menor = (chute_usuario < chute_maquina)

        if acertou:
            print(f"Parabéns! Você Acertou e fez {pontos} Pontos !")
            break
        else:
            if maior:
                print("Você Errou! Chute um número MENOR!")
            elif menor:
                print("Você Errou! Chute um número MAIOR!")
            pontos_perdidos = abs(chute_maquina - chute_usuario)
            pontos -= pontos_perdidos

        rodada += 1

    print("-=-=-=-=-=-=-=- Fim de Jogo! -=-=-=-=-=-=-=-")
    if not acertou:
        print("Que pena, Você Perdeu !")

if __name__ == "__main__":
    jogar()