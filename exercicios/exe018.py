# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.



print('===== DESAFIO 18 =====\n')
from math import radians, sin, cos, tan     # Importando a bibliotéca de funções matematicas

angulo = float(input('Digite o valor de um angulo: '))
print(f'Seno: {sin(radians(angulo)):.2f}, cosseno: {cos(radians(angulo)):.2f}, tangente: {tan(radians(angulo)):.2f}')
