# Crie um programa que leia o nome de uma pessoa ediga se ela tem Silva no nome.


print('===== DESAFIO 25 =====\n')

nome = str(input('Digite o seu nome completo: ')).lower()

if 'silva' in nome:        # realizando teste if para saber se existe a palavra 'silva'
    print('Você tem Silva no seu nome!')
else:
    print('Você não tem Silva no seu nome!')
