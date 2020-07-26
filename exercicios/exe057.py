# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'. Caso esteja errado, peça a
# digitação até ter um valor correto.


print('===== DESAFIO 57 =====\n')

entrada = str(input('Sexo? [M] ou [F]: ')).strip().upper()
while entrada != 'M' and entrada != 'F':

        print(f'Entrada Incorreta! {entrada} não é um M ou F \n')
        entrada = str(input('Sexo? [M] ou [F]: ')).strip().upper()

print(f'Entrada correta, digitado {entrada}')
