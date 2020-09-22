# Faça um programa que leia o nome e pesso de varias pessoas, usando lista. depois: Quantas pessoas? pessoas mais
# pesadas? pessoas mais leves?

print('===== DESAFIO 84 =====\n')

lista = []
contador = 0

for x in range (0, 5):
    lista.append([input(f'{x+1}-Nome: '), int(input(f'{x+1}-Peso: '))])




print(f'Foram cadastradas {len(lista)} pessoas!')

print(max(lista))