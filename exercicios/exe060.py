# Faça um programa que leia um númeor qualquer e mostre seu fatorial.

print('===== DESAFIO 60 =====\n')


resul = fatorial = int(input('Digite um número para calculo fatorial: '))


while fatorial > 1:
    print(f'{fatorial} x ', end = '')
    fatorial -= 1
    resul = resul * (fatorial)
print(f'1 = {resul}\n')
