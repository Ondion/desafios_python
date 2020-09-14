# Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será
# o valor a ser sacado, (inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$:50, R$:20, R$:10 e R$:1

print('===== DESAFIO 71 =====\n')

from random import choice

saque = int(input('Qual o valor do saque: '))

list = [50, 20, 10, 1]
n_50 = n_20 = n_10 = n_1 = 0


while True:
    aleatorio = choice(list)
    if aleatorio == 50 or aleatorio == 20 or aleatorio == 10 or aleatorio == 1:
        if saque >= aleatorio:
            if aleatorio == 50:
                n_50 += 1
            elif aleatorio == 20:
                n_20 += 1
            elif aleatorio == 10:
                n_10 += 1
            else:
                n_1 += 1
            saque -= aleatorio
        if saque == 0:
            if n_50 != 0:
                print(f'Você receberá {n_50} nota/s de R$:50,00')
            if n_20 != 0:
                print(f'Você receberá {n_20} nota/s de R$:20,00')
            if n_10 != 0:
                print(f'Você receberá {n_10} nota/s de R$:10,00')
            if n_1 != 0:
                print(f'Você receberá {n_1} nota/s de R$:1,00')
            break
