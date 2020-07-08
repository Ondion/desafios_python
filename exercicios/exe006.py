# Crie um algoritmo que leia um némero e mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt       # importando função raiz quadrada

print('===== DESAFIO 06 =====\n')

numero = int(input('Digite um valor: '))        # recebendo o valor a ser calculado

print(f'Você digitou: {numero}, o dobro é {numero * 2}, o triplo é {numero * 3}'
      f' e a raiz quadrada é {sqrt(numero):.2f}')       # realizando todos os calculos local
