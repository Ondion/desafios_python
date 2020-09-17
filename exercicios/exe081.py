# Crie um programa que leia varios números e coloque-os numa lista, depois: Quantos números foram digitados?
# Ordem decrescente, o valor 5 foi ou não digitado?

print('===== DESAFIO 81 =====\n')

lista = list()

while True:
    local = int(input('Entre com o valor númerico, ou -1 para sair: '))

    if local == -1:
        break

    if local in lista:
        continue

    lista.append(local)

print(f'Foram digitados {len(lista)} números \n'
      f'Em ordem decrescente: {sorted(lista, reverse=True)}')
print(f'O valor 5 foi digitado na posição {lista.index(5)}' if 5 in lista else 'O valor 5 não foi digitado!')
