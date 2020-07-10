# Faça um programa que leia um número entre 0 e 9999 e mostre na tela cada um dos digitos separados.


print('===== DESAFIO 23 =====\n')

numero = str(input('Digite um valor de 0 até 9999: '))

print(f'Unidade: {numero[-1]}')     # realizando a formatação de texto para imprimir sempre indices separados
print(f'Dezena: {numero[-2:-1]}')       # imprimindo do ultimo para o primeiro
print(f'Centena: {numero[-3:-2]}')
print(f'Milhar: {numero[-4:-3]}')
