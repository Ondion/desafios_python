# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram
# no intervalo de 1 até 500.


print('===== DESAFIO 48 =====\n')

soma = 0
for i in range(1, 500):
    if i % 2 == 1:
        if i % 3 == 0:
            soma += i

print(soma)
