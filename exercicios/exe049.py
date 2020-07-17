# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher,só que agora ultilizando um laço for.


print('===== DESAFIO 49 =====\n')

tabuada = int(input('Digite o valor da tabuada a ser gerada: '))

print()
for i in range(0, 11):
    print(f'{tabuada} X {i} = {tabuada * i}')
