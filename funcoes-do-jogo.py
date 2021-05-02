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
    if len(string)==2: #Para todas as cartas com exceção das cartas com o número 10
        return string[1]
    else: #Para todas as cartas com o número 10
        return string[2]

#Extrai valor da carta
def extrai_valor(string):
    if len(string)==2: #Para todas as cartas com exceção das cartas com o número 10
        return string[0]
    else: #Para todas as cartas com o número 10
        return string[0]+string[1]
    
#Lista movimentos possíveis no Paciência Acordeão
def lista_movimentos_possiveis(baralho,indice):
    movimentos_possiveis=[]
    if indice == 0: #Caso a posição do índice seja 0
        return movimentos_possiveis
    if indice>=1: #Para qualquer posição maior ou acima de 1
        if extrai_naipe(baralho[indice])==extrai_naipe(baralho[indice-1]):
            movimentos_possiveis.append(1)
        elif extrai_valor(baralho[indice])==extrai_valor(baralho[indice-1]):
            movimentos_possiveis.append(1)
    if indice>=3: #Caso a posição do índice for maior ou igual a 3
        if extrai_naipe(baralho[indice])==extrai_naipe(baralho[indice-3]):
            movimentos_possiveis.append(3)
        elif extrai_valor(baralho[indice])==extrai_valor(baralho[indice-3]):
            movimentos_possiveis.append(3)
    return movimentos_possiveis

#Empilhar as cartas no Paciência Acordeão
def empilha(baralho, origem, destino):
    if lista_movimentos_possiveis(baralho,origem) == [1]: #Empilhar as cartas caso a lista da função lista_movimentos_possiveis seja [1]
        del baralho[destino]
    elif lista_movimentos_possiveis(baralho,origem) == [3]: #Empilhar as cartas caso a lista da função lista_movimentos_possiveis seja [3]
        baralho.insert(destino, baralho[origem])
        del baralho[destino + 1]
        del baralho[origem]
    elif lista_movimentos_possiveis(baralho,origem) == [1,3]: #Empilhar as cartas caso a lista da função lista_movimentos_possiveis seja [1,3]
        baralho.insert(destino, baralho[origem])
        del baralho[destino + 1]
        del baralho[origem]
    return baralho

#Há movimentos possiveis no Paciência Acordeão?
def possui_movimentos_possiveis(baralho):
    lista_movimento = [[1], [3], [1,3]]
    i = 0
    while i < len(baralho):
        if lista_movimentos_possiveis(baralho,i) in lista_movimento:
            return True
        else:
            i += 1
    return False