# Crie um programa que tenha uma tupla única com nomes de produtos e seus resectivos preços na sequencia.
# No final mostre uma listagem de preços, organizando os dados em forma tabular

print('===== DESAFIO 76 =====\n')

tupla = ('Lapis', 'R$:00,30',
         'Borracha', 'R$:00,45',
         'Caneta', 'R$:00,99',
         'Bloco de Notas', 'R$:01,50',
         'Caderno', 'R$:02,50',
         'Fichário', 'R$:05,00',
         'Livro Algebra', 'R$:15,15')

for item in range(0, len(tupla), 2):
    print(f'{tupla[item] + ":":-<20}', end= '')
    print('> ',tupla[item + 1])
