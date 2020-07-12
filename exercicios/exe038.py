# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior ou o segundo valor é maior ou não existe valor maior, od dois são iguais.


print('===== \033[35mDESAFIO 38\033[m =====\n')

valor_a = int(input('Digite o primeiro valor: '))
valor_b = int(input('Digite o segundo valor: '))

if valor_a > valor_b:
    print('O primeiro valor é maior que o segundo!')
elif valor_b > valor_a:
    print('O segundo valor é maior que o primeiro!')
else:
    print('Os valores são iguais!')
