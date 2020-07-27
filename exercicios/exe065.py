# Crie um programa que leia vários números inteiros pelo teclado. No final da execução. Mostre a média entre todos os
# valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a
# digitar valores.

print('===== DESAFIO 65 =====\n')

maior = menor = somatoria = contador = media = 0

while True:
    base = input('Digite quantos valores quiser, digite "sair" para sair: ').lower()
    if contador == 0 and base.isnumeric():
        maior = menor = int(base)
    if not base.isnumeric() and base != 'sair':
        continue
    if base == 'sair':
        print(f'A média dos valores é {media}, o maior é: {maior} e o menor é: {menor}.')
        break
    base = int(base)
    if base > maior:
        maior = base
    if base < menor:
        menor = base
    somatoria += base
    contador += 1
    media = somatoria / contador
