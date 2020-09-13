# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.


print('===== DESAFIO 55 =====\n')

maior = menor = peso = float(input('Entre com o peso: '))
for range in range(0 , 4):
    peso = float(input('Entre com o peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'Maior: {maior} e Menor: {menor}')
