# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
# tabela abaixo:
# Abaixo de 18,5 - Abaixo do peso
# Entre 18,5 e 24,99 - Peso ideal
# Entre 25 e 29,99 - Sobrepeso
# Entre 30 e 40 - Obesidade
# Acima de 40 - Obesidade mórbida


print('===== DES\033[1;33;40mA\033[mFIO 43 =====\n')

altura = float(input('Qual sua altura em Metros? '))
peso = float(input('Qual seu peso em Kgs? '))
imc = peso / altura**2

if imc < 18.5:
    print(f'{imc:.2f} de IMC, Abaixo de 18,5 - Abaixo do peso')
elif 18.5 <= imc <= 24.99:
    print(f'{imc:.2f} de IMC, Entre 18,5 e 24,99 - Peso ideal')
elif 25 <= imc <= 29.99:
    print(f'{imc:.2f} de IMC, Entre 25 e 29,99 - Sobrepeso')
elif 30 <= imc <= 40:
    print(f'{imc:.2f} de IMC, Entre 30 e 40 - Obesidade')
else:
    print(f'{imc:.2f} de IMC, Acima de 40 - Obesidade mórbida')
