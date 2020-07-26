# Crie um programa que leia dois valores e mostre um menu com as operações fundamentais.
# Seu programa deverá realizar a operação solicitada em cada caso.

print('===== DESAFIO 59 =====\n')

sda = 'sda'

while sda != 's' and sda != 'S':
    operador_a = float(input('\nPrimeiro Digito: '))      # Recebendo o primeiro valor da calculadora

    fator = str(input('Qual a operação a ser realizada? [+] [-] [*] [/]'))      # Recebendo a operação a ser realizada, com tratamento de erro

    while fator != '+' and fator != '-' and fator != '*' and fator != '/':
        print('Entrada incorreta, tente novamente!')
        fator = str(input('Qual a operação a ser realizada? [+] [-] [*] [/]: '))

    operador_b = float(input('Segundo Digito: '))       # Recebendo o segundo operador, evitando possivel divisão por zero
    while operador_b == 0 and fator == '/':
        print('Não podemos dividir por zero! Tente outro número!')
        operador_b = float(input('Segundo Digito: '))

    if fator == '+':
        print(f'{operador_a} {fator} {operador_b} = {operador_a + operador_b}')

    elif fator == '-':
        print(f'{operador_a} {fator} {operador_b} = {operador_a - operador_b}')

    elif fator == '*':
        print(f'{operador_a} {fator} {operador_b} = {operador_a * operador_b}')

    else:
        print(f'{operador_a} {fator} {operador_b} = {operador_a / operador_b}')

    sda = str(input('Quer sair do programa? [S] ou [N]: '))
