# Desenvolva um programa que leia o comprimento de três retas e diga ao usúario se elas podem ou não formar um triângulo.


print('===== DESAFIO 35 =====\n')

reta_a = float(input('Digite o tamanho da reta 1: '))
reta_b = float(input('Digite o tamanho da reta 2: '))
reta_c = float(input('Digite o tamanho da reta 3: '))

if reta_a + reta_b > reta_c and reta_a + reta_c > reta_b and reta_c + reta_b > reta_a:
    print('As medidas podem formar um triângulo')
else:
    print('As medidas NÃO podem formar um triângulo')
