# Desenvolva um programa que leia 4 valores pelo teclado, guarde-os em uma tupla. No final, mostre quantoas vezes
# apareceu o valor 9, Em que posição foi digitado o primeiro valor 3 e quais foram os números pares.

print('===== DESAFIO 75 =====\n')

tupla = (int(input('1 número: ')), int(input('2 número: ')), int(input('3 número: ')), int(input('4 número: ')))
tag = False

print(f'O valor 9 foi digitado: {tupla.count(9)} vez/vezes' if 9 in tupla else 'O valor 9 não foi digitado!')
print(f'O valor 3 aparece na posição: {tupla.index(3) + 1} primeiramente' if 3 in tupla else 'O valor 3 não foi digitado!')
for n in tupla:
    if n % 2 == 0:
        print(n, end=', ')
        tag = True
print('Não foram digitados valores pares!' if tag == False else 'são os números pares digitados!')
