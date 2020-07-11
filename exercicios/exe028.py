# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5, e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário vendeu ou perdeu.


print('===== DESAFIO 28 =====\n')

from random import randint      # módulo de geração de números aleatorios

sorteio = randint(1, 5)     # gerando um número aleatório entre 1 e 5
chute = int(input('Tente advinhar qual número estou pensando de 1 até 5: '))
print(f'Pensei no número {sorteio}, você acertou!' if chute == sorteio else f'Pensei no número {sorteio}, você errou!')
# teste condicional para analisar se as variaveis são iguais
