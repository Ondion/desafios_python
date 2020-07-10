# Faça um programa que leia o comprimento do cateto oposto e do adjacente de um triângulo retângulo, calcule e mostre
# o comprimento da hipotenusa.

print('===== DESAFIO 17 =====\n')
from math import hypot      # Importando a bibliotéca de funções matematicas

cateto_o = float(input('Digite o cateto oposto: '))     # Lendo as variaveis
cateto_a = float(input('Digite o cateto adjacente: '))

print('A Hipotenusa dos catetos é: {:.2f}'.format(hypot(cateto_a, cateto_o)))       # Realizando o calculo proposto
