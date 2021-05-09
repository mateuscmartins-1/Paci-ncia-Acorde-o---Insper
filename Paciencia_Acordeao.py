import random
from colorama import Fore, Back, Style
  
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


#Junção das funções para jogar o Paciência Acordeão

print("======== Paciência Acordeão ========")
print("")
print("Bem vindo(a) ao Paciência Acordeão. Para ganhar é preciso empilhar todas as cartas em uma mesma pilha!")
print("")
print("Existem duas maneiras para empilhar as cartas:")
print("")
print("1. Empilhar uma carta sobre a carta anterior;")
print("2. Empilhar uma carta sobre a terceira carta anterior.")
print("")
print("Para poder realizar um movimento é necessário que pelo menos uma das condições abaixo seja válida:")
print("")
print("1. As duas cartas possuem o mesmo naipe;")
print("2. As duas cartas possuem o mesmo valor.")
print("")

naipes_vermelho = ["♥", "♦"]
naipes_preto = ["♠", "♣"]

jogar=99>1
while jogar:
    iniciar=True
    while iniciar:
        inicio = input("Para iniciar o jogo digite INICIAR: ")
        if (inicio == "INICIAR" or inicio == "Iniciar" or inicio == "iniciar"):
            random.shuffle(baralho)
            i1 = 0
            while i1<len(baralho):
                while i1<=8:
                    carta=baralho[i1]
                    if ("♥" in carta or "♦" in carta):
                        print(Fore.BLACK + "{}.   {}".format(i1+1, carta))
                    elif ("♠" in carta or "♣" in carta):
                        print(Fore.RED + "{}.   {}".format(i1+1, carta))
                    i1 += 1
                carta=baralho[i1]
                if ("♥" in carta or "♦" in carta):
                    print(Fore.RED + "{}.  {}".format(i1+1, carta))
                elif ("♠" in carta or "♣" in carta):
                    print(Fore.BLACK + "{}.  {}".format(i1+1, carta))
                i1 += 1
            iniciar=False
        else:
            print("Digite iniciar para começar o jogo!")

    quantidade_cartas = 52
    continuar = True
    while continuar:
        print("")

        if quantidade_cartas == 1:
            print("O jogo acabou e você venceu! Parabéns!!! :)")
        
        escolha_carta = int((input(Fore.WHITE + "Escolha uma carta do baralho acima(2 a {}): ".format(quantidade_cartas))))
        if escolha_carta> quantidade_cartas or escolha_carta< 2:
            print("Essa posição é inválida! ")
            continue

        carta = baralho[escolha_carta - 1]

        indice_carta = escolha_carta - 1

        if possui_movimentos_possiveis(baralho) == True and (indice_carta == 1 or indice_carta == 2):
            if indice_carta == 1:
                if lista_movimentos_possiveis(baralho,indice_carta) == [1]:
                    empilha(baralho, indice_carta, indice_carta-1)
                    i2 = 0
                    while i2<len(baralho):
                        while i2<=8:
                            carta=baralho[i2]
                            if ("♥" in carta or "♦" in carta):
                                print(Fore.RED + "{}.   {}".format(i2+1, carta))
                            elif ("♠" in carta or "♣" in carta):
                                print(Fore.BLACK + "{}.   {}".format(i2+1, carta)) 
                            i2 += 1
                        if len(baralho)<=9:
                            break
                        carta=baralho[i2]
                        if ("♥" in carta or "♦" in carta):
                            print(Fore.RED + "{}.  {}".format(i2+1, carta))
                        elif ("♠" in carta or "♣" in carta):
                            print(Fore.BLACK + "{}.  {}".format(i2+1, carta))
                        i2 += 1
                    quantidade_cartas -= 1
                else:
                    print("Essa carta não possui movimento. Tente outra carta ")

            if indice_carta == 2:
                if lista_movimentos_possiveis(baralho,indice_carta) == [1]:
                    empilha(baralho, indice_carta, indice_carta-1)
                    i3 = 0
                    while i3<len(baralho):
                        while i3<=8:
                            carta=baralho[i3]
                            if ("♥" in carta or "♦" in carta):
                                print(Fore.RED + "{}.   {}".format(i3+1, carta))
                            elif ("♠" in carta or "♣" in carta):
                                print(Fore.BLACK + "{}.   {}".format(i3+1, carta)) 
                            i3 += 1
                        if len(baralho)<=9:
                            break
                        carta=baralho[i3]
                        if ("♥" in carta or "♦" in carta):
                            print(Fore.RED + "{}.  {}".format(i3+1, carta))
                        elif ("♠" in carta or "♣" in carta):
                            print(Fore.BLACK + "{}.  {}".format(i3+1, carta)) 
                        i3 += 1
                    quantidade_cartas -= 1
                else:
                    print("Essa carta não possui movimento. Tente outra carta ")

        elif possui_movimentos_possiveis(baralho) == True and indice_carta >=3:  
            if lista_movimentos_possiveis(baralho,indice_carta) == [1]:
                empilha(baralho, indice_carta, indice_carta-1)
                i4 = 0
                while i4<len(baralho):
                    while i4<=8:
                        carta=baralho[i4]
                        if ("♥" in carta or "♦" in carta):
                            print(Fore.RED + "{}.   {}".format(i4+1, carta))
                        elif ("♠" in carta or "♣" in carta):
                            print(Fore.BLACK + "{}.   {}".format(i4+1, carta)) 
                        i4 += 1
                    if len(baralho)<=9:
                        break
                    carta=baralho[i4]
                    if ("♥" in carta or "♦" in carta):
                        print(Fore.RED + "{}.  {}".format(i4+1, carta))
                    elif ("♠" in carta or "♣" in carta):
                        print(Fore.BLACK + "{}.  {}".format(i4+1, carta)) 
                    i4 += 1
                quantidade_cartas -= 1

            elif lista_movimentos_possiveis(baralho,indice_carta) == [3]:
                empilha(baralho, indice_carta, indice_carta-3)
                i5 = 0
                while i5<len(baralho):
                    while i5<=8:
                        carta=baralho[i5]
                        if ("♥" in carta or "♦" in carta):
                            print(Fore.RED + "{}.   {}".format(i5+1, carta))
                        elif ("♠" in carta or "♣" in carta):
                            print(Fore.BLACK + "{}.   {}".format(i5+1, carta)) 
                        i5 += 1
                    if len(baralho)<=9:
                        break
                    carta=baralho[i5]
                    if ("♥" in carta or "♦" in carta):
                        print(Fore.RED + "{}.  {}".format(i5+1, carta))
                    elif ("♠" in carta or "♣" in carta):
                        print(Fore.BLACK + "{}.  {}".format(i5+1, carta)) 
                    i5 += 1
                quantidade_cartas -= 1

            elif lista_movimentos_possiveis(baralho,indice_carta) == [1,3]:
                print("1. Empilhar a carta {} em cima a carta {} (Mover uma posição)".format(carta, baralho[escolha_carta - 2]))
                print("2. Empilhar a carta {} em cima a carta {} (Mover 3 posições)".format(carta, baralho[escolha_carta - 4]))
                avancar=True
                while avancar:
                    movimenta_carta = int(input("Você pode movimentar essa carta de duas formas! Como quer movimentar? (1 ou 2): "))
                    if movimenta_carta == 1:
                        empilha(baralho, indice_carta, indice_carta-1)
                        avancar=False
                        i6 = 0
                        while i6<len(baralho):
                            while i6<=9:
                                carta=baralho[i6]
                                if ("♥" in carta or "♦" in carta):
                                    print(Fore.RED + "{}.   {}".format(i6+1, carta))
                                elif ("♠" in carta or "♣" in carta):
                                    print(Fore.BLACK + "{}.   {}".format(i6+1, carta)) 
                                i6 += 1
                            if len(baralho)==9:
                                break
                            carta=baralho[i6]
                            if ("♥" in carta or "♦" in carta):
                                print(Fore.RED + "{}.  {}".format(i6+1, carta))
                            elif ("♠" in carta or "♣" in carta):
                                print(Fore.BLACK + "{}.  {}".format(i6+1, carta)) 
                            i6 += 1
                    if movimenta_carta == 2:
                        empilha(baralho, indice_carta, indice_carta-3)
                        avancar=False
                        i7 = 0
                        while i7<len(baralho):
                            while i7<=9:
                                carta=baralho[i7]
                                if ("♥" in carta or "♦" in carta):
                                    print(Fore.RED + "{}.   {}".format(i7+1, carta))
                                elif ("♠" in carta or "♣" in carta):
                                    print(Fore.BLACK + "{}.   {}".format(i7+1, carta))                                
                                i7 += 1
                            if len(baralho)<=9:
                                break
                            carta=baralho[i7]
                            if ("♥" in carta or "♦" in carta):
                                print(Fore.RED + "{}.  {}".format(i7+1, carta))
                            elif ("♠" in carta or "♣" in carta):
                                print(Fore.BLACK + "{}.  {}".format(i7+1, carta))                             
                            i7 += 1
                    else:
                        print("Digite 1 ou 2")
                quantidade_cartas -= 1

            else:
                print("Essa carta não possui movimento. Tente outra carta ")
        
        elif possui_movimentos_possiveis(baralho) == False:
            print("Fim de jogo! Você perdeu!")
            continuar = False
    print("")

    novamente=77<89
    while novamente==True:
        jogar_novamente=input("Você deseja jogar novamente? Responda ===> sim, para iniciar um novo jogo. OU . Responda ===> não, para parar de jogar!")
        if jogar_novamente=='sim':
            break
        if jogar_novamente=='não':
            jogar=False
            break