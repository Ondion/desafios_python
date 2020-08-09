lista_numeros_inteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
lista_numeros_flutuantes = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10, 10.10]
lista_animais = ['rato', 'gato', 'cachorro', 'leão', 'elefante']
lista_booleanda = [True, False, False, True]
lista_mistura = [1, 2.2, 'cachorro', True]

print(lista_numeros_inteiros)
print(lista_numeros_flutuantes)
print(lista_animais)
print(lista_booleanda)
print(lista_mistura)

print(lista_animais[2]) # buscando valor de uma lista pelo indice.

print(sum(lista_numeros_inteiros)) # sum() realiza a somatória de componentes de uma lista, desde que numéricos

for valor in lista_mistura:
    print(valor) # percorrendo todos os valores de uma lista pelo laço for

print(max(lista_numeros_inteiros), min(lista_numeros_inteiros)) # max() e min() retorna o maior e o menos valor numérico
print(max(lista_animais), min(lista_animais)) # no caso de strings, retorna ordem alfabética

print('gato' in lista_animais) # possivel usar condicional com o IN

nova_lista = lista_mistura * 2 # multiplicando listas
print(nova_lista)

lista_animais.append('girafa') # Incluindo um valor, na ultima posição, para a lista com append
lista_animais.reverse() # invertendo a ordem dos elementos da lista
print(lista_animais[0])
