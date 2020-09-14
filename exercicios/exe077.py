# Crie um programa que tenha uma tupla com varias palavras. Depois disso, você deve mostrar, para cada palavra
# quais são as suas vogais.


print('===== DESAFIO 77 =====\n')

palavras = ('Notebook', 'Caneta', 'Lapis', 'Caderno', 'Caneca', 'Telefone', 'Escola')

for palavra in palavras:
    print('Na palavra:', palavra, 'temos as vogais: ', end='')
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            print(letra, end=' ')
    print('\n')
