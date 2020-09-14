# Crie um programa que leia o nome e o preço de varios produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre qual é o total gasto na compra. Quantos produtos cistam mais de R$: 1000 e qual o nome do produto
# mais barato.


print('===== DESAFIO 70 =====\n')

barato = nome_barato = total = mais_de_1k = 0

while True:
    nome = str(input('Nome no produto: '))
    valor = float(input('Preço do produto: '))

    if barato == 0:
        barato = valor

    if valor < barato:
        barato = valor
        nome_barato = nome

    if valor >= 1000:
        mais_de_1k += 1

    total += valor

    if input('Você deseja continuar? <S> ou <N> ').lower() == 'n':
        print(f'Total R$:{total:.2f}, Custam mais de 1k: {mais_de_1k}, O mais barato: {nome_barato}')
        break
