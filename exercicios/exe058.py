# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar advinhar até acertar, mostrando no fina quantos palpites foram necessários para vencer.

print('===== DESAFIO 58 =====\n')
from random import randint as rint

contador = 0
palpite_pc = rint (0, 10)
jogador = int(input('Qual o seu palpite no jogo da advinhação? (de 0 até 10): '))

while palpite_pc != jogador:
    if jogador > palpite_pc:
        contador += 1
        print(f'Você errou, o número que pensei é menor! Tente novamente! Você já tentou {contador}x\n')
        jogador = int(input('Qual o seu palpite no jogo da advinhação? (de 0 até 10): '))
    else:
        contador += 1
        print(f'Você errou, o número que pensei é maior! Tente novamente! Você já tentou {contador}x\n')
        jogador = int(input('Qual o seu palpite no jogo da advinhação? (de 0 até 10): '))

print(f'Você acertou!!! Tentativas = {contador}')
