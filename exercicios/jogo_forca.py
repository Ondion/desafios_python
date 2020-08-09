import random
from jogo_forca_lista_palavras import lista_palavras_forca # importando o banco de palavras

def escolhe_palavra(): # função para escolher uma palavra aleatóriamente da lista de palavras
    palavra = random.choice(lista_palavras_forca)
    return palavra.upper()

def jogar(palavra):
    espacos = '-' + len(palavra)
    acertou = False
    guessed_letters = []
    guessed_words = []
    tentativas = 6
    print('Vamos começar')
    print(desenha_forca(tentativas))
    print(espacos, '\n')

    while not acertou and tentativas > 0:
        chute = input('Entre com a letra ou palavra').upper()
        if len(chute) == 1 and chute.isalpha():
            print('essa letra já apareceu aqui: ', chute)
        elif chute not in palavra:
            print(chute, ' não está na palavra.')
            tentativas -= 1
            guessed_letters.append(chute)
        else:
            print(f'Isso ai, {chute} pertence à palavra!')
            guessed_letters.append(chute)
            word_as_list = list(espacos)
            indices = [i for i, ]




