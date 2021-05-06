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

#Função para extrair o naipe da carta
def extrai_naipe(carta):
    if len(carta)==2: #Para todas as cartas com exceção das cartas com o número 10
        return carta[1]
    else: #Para todas as cartas com o número 10
        return carta[2]

#Função para extrair o valor da carta
def extrai_valor(carta):
    if len(carta)==2: #Para todas as cartas com exceção das cartas com o número 10
        return carta[0]
    else: #Para todas as cartas com o número 10
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
def possui_movimentos_possiveis(cartas):
    lista_movimento = [[1], [3], [1,3]]
    i = 0
    while i < len(cartas):
        if lista_movimentos_possiveis(cartas,i) in lista_movimento:
            return True
        i += 1
    return False