# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('===== DESAFIO 12 =====\n')

desconto = float(input('Valor para desconto R$: '))
print(f'Você digitou R$:{desconto:.2f} e aplicando 5% de desconto temos: R$:{desconto * 0.95:.2f} ')
