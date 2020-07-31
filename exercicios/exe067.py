# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário o
# programa será interrompido quando o número solicitado for negativo.

print('===== DESAFIO 67 =====\n')

while True:
    tabuada = int(input('Qual tabuada você gostaria de ver? <número negativo para sair> '))
    if tabuada < 0:
        break
    interacoes = int(input('Quantas interações por tabuada? '))
    for i in range(1, interacoes + 1):
        print(f'{tabuada} X {i} = {tabuada * i}')

    print('\n')
