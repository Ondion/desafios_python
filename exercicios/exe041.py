# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# até 9 anos - Mirim, até 14 anos - Infantil, até 19 anos - Junior, até 25 anos - Senior, acima de 25 - Master.


print('\033[1;33m===== DESAFIO 41 =====\033[m\n')
from datetime import date

idade = date.today().year - int(input('Qual o ano de nascimento do atleta? '))

if idade <= 9:
    print(idade, 'anos Categoria: Mirin')
elif idade <= 14:
    print(idade, 'anos Categoria: Infantil')
elif idade <= 19:
    print(idade, 'anos Categoria: Junior')
elif idade <= 25:
    print(idade, 'anos Categoria: Senior')
else:
    print(idade, 'anos Categoria: Master')
