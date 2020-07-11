# Desenvolva um programa que pergunte a distância de uma viagem em Kms. Calcule o preço da passagem, cobrando R$ 0,50
# por Km para viagens de até 200Kms e R$: 0,45 para viagens mais longas.

print('===== DESAFIO 31 =====\n')

distancia = float(input('Qual a distância da viagem em Kms?: '))
print(f'Valor da passagem R$:{0.50 * distancia}' if distancia <= 200 else f'Valor da passagem R$:{0.45 * distancia}')
