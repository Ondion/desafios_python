# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.

print('===== DESAFIO 53 =====\n')

frase = str(input('Digite uma frase: ')).upper().strip().split()
frase = ''.join(frase)
inverso = frase[::-1]

if frase == inverso:
    print(f'Sim são palindromos - normal: {frase} inverso: {inverso}')
else:
    print(f'Não são palindromos - normal: {frase} inverso: {inverso}')
