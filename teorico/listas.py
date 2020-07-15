lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10.5]
lista_animais = ['rato', 'gato', 'cachorro', 'leão', 'elefante']
lista_mistura = [1, 1.35, 'mistura', True]

print(lista_animais[2]) # buscando valor de uma lista pelo indice.

print(sum(lista_numeros)) # sum() realiza a somatória de componentes de uma lista, desde que numéricos

for valor in lista_mistura:
    print(valor) # percorrendo todos os valores de uma lista pelo laço for

print(max(lista_numeros), min(lista_numeros)) # max() e min() retorna o maior e o menos valor numérico
print(max(lista_animais), min(lista_animais)) # no caso de strings, retorna ordem alfabética

print('gato' in lista_animais) # possivel usar condicional com o IN

nova_lista = lista_mistura * 2 # multiplicando listas
print(nova_lista)

lista_animais.append('girafa') # Incluindo um valor para a lista com append
print(lista_animais)
