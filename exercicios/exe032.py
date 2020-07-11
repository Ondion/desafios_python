# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.


print('===== DESAFIO 32 =====\n')

ano = int(input('Digite um ano qualquer para calculo: '))
if ano % 4 == 0 and ano % 100 != 0:     # laços Ifs seguindo lógica matematica sobre anos bissextos.
    print(f'o ano de {ano} é bissexto')
elif ano % 4 == 0 and ano % 400 == 0:
    print(f'o ano de {ano} é bissexto')
else:
    print(f'o ano de {ano} não é bissexto')
