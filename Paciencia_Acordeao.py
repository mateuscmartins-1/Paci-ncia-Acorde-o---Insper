from random import *
def cria_baralho():
    naipes = ["♠", "♥", "♦", "♣"]
    valor_carta = ["2","3","4","5","6","7","8","9","10","J","Q", "K", "A"]
    baralho = []
    i = 0
    j = 0
    while i < len(valor_carta) and j < len(naipes):
        carta = "{}{}".format(valor_carta[i],naipes[j])
        baralho.append(carta)
        i+= 1
        if i == 13:
            j += 1
            i = 0
    return baralho
baralho = cria_baralho()

print("======== Paciência Acordeão ========")
print("")
print("Bem vindo(a) ao Paciência Acordeão. Para ganhar é preciso empilhar todas as cartas em uma mesma pilha!")
print("")
print("Para empilhar as cartas existem duas maneiras:")
print("")
print("1. Empilhar uma carta sobre a carta imediatamente anterior;")
print("2. Empilhar uma carta sobre a terceira carta anterior.")
print("")

print("Para poder empilhar as cartas é necessário que elas satisfazem uma das duas condições abaixo:")
print("")
print("1. Elas possuem o mesmo naipe;")
print("2. Ela possuem o mesmo valor.")
print("")

inicio = input("Para iniciar o jogo digite INICIAR: ")
if (inicio == "INICIAR" or inicio == "Iniciar" or inicio == "iniciar"):
    shuffle(baralho)
    print(baralho)