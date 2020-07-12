# Escreva um programa para aprovar empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
# casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não
# pode exceder 30% do salário ou então o empréstimo será negado.


print('===== \033[34mDESAFIO 36\033[m =====\n')

casa = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual a sua renda mensal? '))
anos = int(input('Em quantos anos você quer parcelar? '))

if casa / (anos * 12) <= salario * 0.3:
    print(f'Seu empréstimo foi \033[1;32mAprovado!!!\n\033[mAnálise:\nPrestação R$:{casa / (anos * 12):.2f}\n30% do salário R$:{salario * .3:.2f} ')
else:
    print(f'Seu empréstimo foi \033[1;31mNegado!!!\n\033[mAnálise:\nPrestação R$:{casa / (anos * 12):.2f}\n30% do salário R$:{salario * .3:.2f} ')
