# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


print('===== DESAFIO 33 =====\n')

numero_1 = int(input('Digire 0 número 1: '))
numero_2 = int(input('Digire o número 2: '))
numero_3 = int(input('Digire o número 3: '))

print(f'O maior número é {max(numero_1, numero_2, numero_3)}')        # funçao que retorna o maior número entre os argumentos
print(f'O menor número é {min(numero_1, numero_2, numero_3)}')        # funçao que retorna o menor número entre os argumentos
