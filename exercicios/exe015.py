# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$: 60,00 por dia e R$: 0,15
# por km rodado.

print('===== DESAFIO 15 =====\n')

kms = float(input('Quantos Kms foram rodados: '))
dias = int(input('Quantos dias o veiculo foi usado: '))
print(f'Valores faturados; R$:{dias * 60},00 pelos dias (R$60,00 p/dia), R$:{kms * 0.15:.2f} pelos Kms (R$:0.15 p/Km),'
      f' totalizando R$:{(kms * 0.15) + (dias * 60):.2f}')
