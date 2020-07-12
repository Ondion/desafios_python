# Escreva um programa que pergunte o salário de um funcionario e calcule o seu aumento. Para salários superiores a
# R$: 1250,00 calcule um aumento de 10%. Para os inferiores ou iguais o aumento é de 15%.


print('===== DESAFIO 34 =====\n')

salario = float(input('Qual o salário a calcular?: '))
print(f'Seu salário reajustado é R$:{salario * 1.1:.2f}' if salario > 1250.00 else f'Seu salário reajustado é R$:{salario * 1.15:.2f}')
