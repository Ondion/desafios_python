# Escreve um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$: 7,00 por cada Km acima do limite.


print('===== DESAFIO 29 =====\n')

velocidade = float(input('Qual a velocidade atual do veiculo?: '))
if velocidade > 80:
    print(f'Você foi multado em R$:{(velocidade - 80) * 7:.2f} por está {velocidade - 80:.2f}Km/h acima do limite de 80Km/h')
else:
    print(f'Sua velocidade está dentro do esperado: {velocidade:.2f}Km/h')
