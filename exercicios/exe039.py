# Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com sua idade, se ele ainda vai se
# alistar ao serviço militar, se [e a hora de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostar o tempo que falta ou que passou do prazo.


print('===== \033[47;30mDESAFIO 39\033[m =====\n')
from datetime import date

ano = int(input('Qual o ano do seu nascimento? '))

if  date.today().year - ano < 18:
    print(f'Ainda é cedo para o alistamento, volte em {18 - (date.today().year - ano)} ano\s')
elif date.today().year - ano == 18:
    print('Você deve se alistar esse ano! CORRE!!!')
else:
    print(f'Você passou do prazo de alistamento em {(date.today().year - ano) - 18} ano\s')
