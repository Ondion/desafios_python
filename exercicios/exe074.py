# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a
# listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

print('===== DESAFIO 74 =====\n')

from random import randint

tupla = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print(f'Tupla: {tupla}\nMinimo: {min(tupla)}\nMaximo: {max(tupla)}')
