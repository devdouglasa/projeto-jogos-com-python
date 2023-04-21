import adivinhacao
import forca

print("Bem vindo !")
print("")
print("(1) Adivinhação (2) Forca")
selecao = int(input("Selecione um jogo para continuar: "))

if selecao == 1:
    adivinhacao.jogar()
elif selecao == 2:
    forca.jogar()