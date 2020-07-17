# Faça um programa que mostre na tela umacontagem regressiva para o estouro de fogos de artificio, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.

print('===== DESAFIO 46 =====\n')
from time import sleep as timer

for i in range(10, 0, -1):
    print(f'\033[1;3{i % 7}m{i} \033[1;3{i+1 % 7}m...') # comandos de cores do terminal
    timer(1)
print("BUM!!!")
