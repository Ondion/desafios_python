# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for impar, desconsidere-o.

print('===== DESAFIO 50 =====\n')

soma = 0
for i in range(0, 6):
    numero = int(input(f'\033[1;3{i}mDigite um número inteiro: '))
    if numero % 2 == 0:
        soma += numero

print('A soma dos números pares digitados é:', soma)
