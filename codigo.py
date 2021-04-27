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

#Extrai naipe da carta
def extrai_naipe(string):
    if len(string)==2:
        return string[1]
    else:
        return string[2]

#Extrai valor da carta
def extrai_valor(string):
    if len(string)==2:
        return string[0]
    else:
        return string[0]+string[1]
#Lista movimentos possíveis no Paciência Acordeão
def extrai_naipe(string):
    if len(string)==2:
        return string[1]
    else:
        return string[2]
def extrai_valor(string):
    if len(string)==2:
        return string[0]
    else:
        return string[0]+string[1]
def lista_movimentos_possiveis(baralho,indice):
    movimentos_possiveis=[]
    if indice>=1:
        if extrai_naipe(baralho[indice])==extrai_naipe(baralho[indice-1]):
            movimentos_possiveis.append(1)
        elif extrai_valor(baralho[indice])==extrai_valor(baralho[indice-1]):
            movimentos_possiveis.append(1)
    if indice>=3:
        if extrai_naipe(baralho[indice])==extrai_naipe(baralho[indice-3]):
            movimentos_possiveis.append(3)
        elif extrai_valor(baralho[indice])==extrai_valor(baralho[indice-3]):
            movimentos_possiveis.append(3)
    return movimentos_possiveis