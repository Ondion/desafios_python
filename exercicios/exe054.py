# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantos já são maiores.


print('===== DESAFIO 54 =====\n')

from datetime import date

maior = menor = 0
for i in range(0, 7):
    nascimento = date.today().year - int(input('Idade de nascimento? '))
    if nascimento >= 18:
        maior += 1
    else:
        menor += 1
print(f'\nMaiores de idade são {maior}, menores são {menor}.')
