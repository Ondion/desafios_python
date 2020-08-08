# Crie um programa que tenha uma tupla com varias palavras. Depois disso, você deve mostrar, para cada palavra
# quais são as suas vogais.


print('===== DESAFIO 77 =====\n')

palavras = ('Notebook', 'Caneta', 'Lapis', 'Caderno', 'Caneca', 'Telefone')

for x in palavras:
    print('Na palavra:', x, 'temos as vogais: ', end='')
    for y in x:
        if y in 'aeiou':
            print(y, end=' ')
    print('\n')
