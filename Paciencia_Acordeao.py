import random

#Função para criar baralho
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
#Função para extrair o naipe da carta
def extrai_naipe(carta):
    if len(carta)==2: #Para todas as cartas com exceção das cartas com o número 10
        return carta[1]
    if len(carta) == 3: #Para todas as cartas com o número 10
        return carta[2]

#Função para extrair o valor da carta
def extrai_valor(carta):
    if len(carta)==2: #Para todas as cartas com exceção das cartas com o número 10
        return carta[0]
    if len(carta) == 3: #Para todas as cartas com o número 10
        return carta[0]+carta[1]
    
#Função para saber a lista de movimentos possíveis no Paciência Acordeão
def lista_movimentos_possiveis(cartas,indice):
    movimentos_possiveis=[]
    if indice == 0: #Caso a posição do índice seja 0
        return movimentos_possiveis
    if indice>=1: #Caso a posição do índice seja 1
        if extrai_naipe(cartas[indice])==extrai_naipe(cartas[indice-1]):
            movimentos_possiveis.append(1)
        elif extrai_valor(cartas[indice])==extrai_valor(cartas[indice-1]):
            movimentos_possiveis.append(1)
    if indice>=3: #Caso a posição do índice seja maior ou igual a 3
        if extrai_naipe(cartas[indice])==extrai_naipe(cartas[indice-3]):
            movimentos_possiveis.append(3)
        elif extrai_valor(cartas[indice])==extrai_valor(cartas[indice-3]):
            movimentos_possiveis.append(3)
    return movimentos_possiveis

#Função para empilhar as cartas no Paciência Acordeão
def empilha(cartas, origem, destino):
    if lista_movimentos_possiveis(cartas,origem) == [1]: #Empilhar as cartas caso a lista da função lista_movimentos_possiveis seja [1]
        del cartas[destino]
    elif lista_movimentos_possiveis(cartas,origem) == [3]: #Empilhar as cartas caso a lista da função lista_movimentos_possiveis seja [3]
        cartas.insert(destino, cartas[origem])
        del cartas[destino + 1]
        del cartas[origem]
    elif lista_movimentos_possiveis(cartas,origem) == [1,3]: #Empilhar as cartas caso a lista da função lista_movimentos_possiveis seja [1,3]
        cartas.insert(destino, cartas[origem])
        del cartas[destino + 1]
        del cartas[origem]
    return cartas

#Função para saber se há movimentos possiveis no Paciência Acordeão
def possui_movimentos_possiveis(baralho):
    lista_movimento = [[1], [3], [1,3]]
    i = 0
    while i < len(baralho):
        if lista_movimentos_possiveis(baralho,i) in lista_movimento:
            return True
        i += 1
    return False

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
    random.shuffle(baralho)
    i1 = 1
    for carta in baralho:
        print("{}. {}".format(i1, carta))
        i1 += 1
        

#Quantidade de cartas
qntd_cartas = 52
continuar = True
while continuar:
    escolha_carta = int(input("Escolha uma carta do baralho acima(1 a {})".format(qntd_cartas)))
    carta = baralho[escolha_carta - 1]
    indice_carta = escolha_carta
    if possui_movimentos_possiveis(baralho) == True :
        lista_de_2_cartas = [baralho[escolha_carta], carta]
        lista_de_4_cartas = [ baralho[escolha_carta - 4],baralho[escolha_carta - 3],baralho[escolha_carta - 2], carta]
        if lista_movimentos_possiveis(lista_de_2_cartas,1) == [1]:

            empilha(carta,indice_carta,indice_carta - 1)
        elif lista_movimentos_possiveis(lista_de_4_cartas,3) == [3]:
            empilha(carta,indice_carta,indice_carta-3)
        elif lista_movimentos_possiveis(lista_de_4_cartas,3) == [1,3]:
            input("Você pode movimentar essa carta de duas formas! Como quer movimentar? ")



        qntd_cartas -= 1
        a = input("Não há movimentos disponíveis para essa carta! Escolha uma outra carta do baralho acima(1 a {}).".format*qntd_cartas)
    elif possui_movimentos_possiveis(baralho) == False:
        print("Você perdeu! Para jogar, novamente, reinicie o jogo!")
        continuar = False


