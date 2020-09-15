# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# e as suas respectivas posições na lista.


print('===== DESAFIO 78 =====\n')

lista = list()

for x in range(0, 5):
    lista.append(int(input('Entre com um valor inteiro: ')))

print(f'O maior valor é {max(lista)}, que está na posição {lista.index(max(lista))}')
print(f'O menor valor é {min(lista)}, que está na posição {lista.index(min(lista))}')
