# Crie um programa onde o úsuario possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
# exista, ele não será adicionado. No final, serão exibidos todos os valores númericos em ordem crescente.

print('===== DESAFIO 79 =====\n')

lista = list()

while True:
    local = input('Entre com um valor ou (S) p/ sair: ')

    if local == '' or local == ' ':
        continue
    elif local in 'Ss':
        break
    elif int(local) in lista:
        print(f'{local} já existe na lista e será ignorado!')
        continue
    else:
        lista.append(int(local))

lista.sort()
print(f'Os valores digitados em ordem crescente são: {lista}')
