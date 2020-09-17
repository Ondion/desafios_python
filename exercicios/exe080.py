# Crie um programa onde um usúario possa digitar 5 valores numéricos e os cadastre já em ordem crescente em uma lista
# No final mostre a lista ordenada.

print('===== DESAFIO 80 =====\n')

lista = []

for x in range(0, 5):
    local = int(input('Digite um valor inteiro: '))
    if x == 0 or local > lista[-1]:
        lista.append(local)
    else:
        y = 0
        while y < len(lista):
            if local <= lista[y]:
                lista.insert(y, local)
                break
            y += 1

print(f'Valores: {lista}\n'
      f'')