# Faça um programa que jogue par ou impar com o computador. O jogo só sera interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

print('===== DESAFIO 68 =====\n')
from random import randint

soma = 0
while True:
    pc = randint(0, 6)
    humano = int(input('Entre com o número que você irar jogar: '))
    parimpar = input('Você quer Par ou Impar? <P> <I>').lower()
    if parimpar != 'p' and parimpar != 'i':
        print('Você entou com valor errado para Par ou Impar, programa reiniciando...')
        continue
    if parimpar == 'p' and (pc + humano) % 2 == 0:
        print(f'Você ganhou! Escolheu par e o número somado do jogo foi {pc + humano}')
        soma += 1
    elif parimpar == 'p' and (pc + humano) % 2 == 1:
        print(f'Você perdeu! Escolheu par e o número somado do jogo foi {pc + humano}, total de ganhos: {soma}')
        break
    elif parimpar == 'i' and (pc + humano) % 2 == 1:
        print(f'Você ganhou! Escolheu impar e o número somado do jogo foi {pc + humano}')
        soma += 1
    else:
        print(f'Você perdeu! Escolheu impar e o número somado do jogo foi {pc + humano}, total de ganhos: {soma}')
        break
