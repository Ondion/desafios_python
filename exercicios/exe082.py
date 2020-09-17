# Crie um programa que leia varios números e os coloque em uma lista. Depois crie duas listas extras que vão conter
# apenas os vaores pares e outra os impares, ao final mostre as três listas.

print('===== DESAFIO 82 =====\n')

lista_a = list()
lista_b = lista_a.copy()
var = 0

while True:
    if input('Deseja adicionar números? [s/n]') in 'Ss':
        var = int(input('Valor: '))
        if var % 2 == 0:
            lista_a.append(var)
        else:
            lista_b.append(var)
    else:
        break
print(f'PARES: {lista_a}, IMPARES: {lista_b}, COMPLETA: {sorted(lista_a + lista_b)}')
