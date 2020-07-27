# Escreva um programa que leia um número inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência
# Fibonacci.

print('===== DESAFIO 63 =====\n')

inteiro = int(input('Quantas interações interações Fibonacci vamos realizar?'))
x = 1
y = 0
r = 1

while inteiro != 0:
    r = x + y
    print(x, '+', y, f'= {r}')
    y = x
    x = r

    inteiro -= 1
