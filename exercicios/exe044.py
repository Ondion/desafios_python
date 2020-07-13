# Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de
# pagamento: A vista dinheiro / cheque, 10% de desconto. A vista no cartão: 5% de desconto.
# em até 2x no cartão: preço normal. 3x ou mais no cartão: 20% de juros.


print('===== \033[1;40mDESAFIO 44\033[m =====\n')

valor = float(input('Qual o valor do produto? '))
opcao = int(input('[1] - DINHEIRO A VISTA\n[2] - CHEQUE A VISTA\n[3] - CARTÃO A VISTA\n[4] - 2X NO CARTÃO\n'
'[5] - 3X OU MAIS NO CARTÃO\n'))

if opcao == 1:
    print(f'Para pagamento a vista em dinheiro, o valor, com 10% de desconto será R$:{valor * 0.9:.2f}')
elif opcao == 2:
    print(f'Para o pagamento a vista em cheque, o valor, com 10% de desconto será R$:{valor * 0.9:.2f}')
elif opcao == 3:
    print(f'Para o pagamento a vista em cartão, o valor, com 5% de desconto será R$:{valor * 0.95:.2f}')
elif opcao == 4:
    print(f'Para o pagamento em 2X no cartão, o valor, sem descontos, será R$:{valor:.2f}')
elif opcao == 5:
    parc = int(input('Em quantas vezes deseja parcelar? '))
    print(f'Para o pagamento parcelado no cartão, o valor total, com juros de 20%, será R$:{valor * 1.2:.2f} - '
          f'O parcelamento será {parc}X de R$:{(valor * 1.2) / parc:.2f}')
else:
    print('Opção invalida! Tente novamente.')
