# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
#  sobre ele.


print('===== DESAFIO 04 =====\n')

while True:  # loop infinito para os testes

    b = str(input('\nValor: '))

    print(f'tipo: {type(b)}')
    print(f'alnum: {b.isalnum()}')
    print(f'alpha: {b.isalpha()}')
    print(f'ascii: {b.isascii()}')
    print(f'decimal: {b.isdecimal()}')
    print(f'digit: {b.isdigit()}')
    print(f'identifier: {b.isidentifier()}')
    print(f'lower: {b.islower()}')
    print(f'numeric: {b.isnumeric()}')
    print(f'printable: {b.isprintable()}')
    print(f'space: {b.isspace()}')
    print(f'title: {b.istitle()}')
    print(f'supper: {b.isupper()}')
