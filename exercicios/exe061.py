# Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da PA usando a estrutura while.


print('===== DESAFIO 61 =====\n')

p_termo = int(input('primeiro termo: '))
razao = int(input('razão: '))
contador = 0

while contador < 10:
    print(f'{p_termo}',  end=', ')
    p_termo += razao
    contador += 1
