# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome Santo.


print('===== DESAFIO 24 =====\n')

cidade = str(input('Digite o nome de uma cidade: ')).lower().strip()

if cidade.split()[0] == 'santo':        # realizando teste if para saber se a primeira palavra é "santo"
    print('Tem Santo ai')
else:
    print('Não tem Santo (no começo do nome) ai')
