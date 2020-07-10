# Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira.

print('===== DESAFIO 16 =====\n')
from math import floor      # Importando a bibliotéca de funções matematicas

numero = float(input('Digite um numero real (float): '))        # Lendo o numero ponto flutuante
print(f'O mesmo numero na porção inteira é: {floor(numero)}')       # convertendo para inteiro via arredondamento
