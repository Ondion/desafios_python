# Desenvolda um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.


print('===== DESAFIO 51 =====\n')

p_termo = int(input('primeiro termo: '))
razao = int(input('razão: '))
interacoes = int(input('Quantas interações? '))

for i in range (0, interacoes):
    print(f'{p_termo}', end=' - ')
    p_termo += razao
