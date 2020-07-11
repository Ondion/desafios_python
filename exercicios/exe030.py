# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.


print('===== DESAFIO 30 =====\n')

numero = int(input('Digite um número: '))       # usando conceiro matemático da sobra de divisão para achar par/impar
print(f'O número {numero} é par' if numero % 2 == 0 else f'O número {numero} é impar')
