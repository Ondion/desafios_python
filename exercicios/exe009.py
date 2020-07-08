# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

print('===== DESAFIO 09 =====\n')

inteiro = int(input('Valor: '))
print('='*16)

for i in range(0, 11):      # laço for para repetição e criação da tabuada
    print(f'| {inteiro:^2} X {i:^2} = {inteiro * i:^2} |')
print('='*16)
