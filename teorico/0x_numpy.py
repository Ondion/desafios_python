import numpy as np
from random import random

# Uma das mais importantes bibliotécas para computação cientifica.
# O core do numpy é escrito em C e Fortran, por esse motivo ela é muito rapida.
# Muito usado para vetores e matrizes em forma de arrays.
# Considerando um plano cartesiano: axis 0 = Y, axis 1 = X e axis 2 = Z
# Logo: shape(0, 1, 2) linha, coluna e profundidade

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Modo basico para a criação de arrays do numpy

array_0s = np.zeros([3, 3, 3])
# Cria matrizes apenas com valores 0, no exemplo o shape foi definido como 3x3x3

array_1s = np.ones([3, 3, 3])
# Cria matrizes apenas com valores 1, no exemplo o shape foi definido como 3x3x3

print(np.shape(array))
# Detanha o formado do array chamado

print(f'Array 2 dimensões:\n{array}\n')
print(f'Array 3 dimensões de 0s:\n{array_0s}\n')
print(f'Array 3 dimensões de 1s:\n{array_1s}\n')

print(f' Valores igualmente espaçados:\n', np.linspace(array_0s, array_1s, 3), '\n')
# retorna valores igualmente espaçados linearmente. parametros= inicio, fim, total de valores divididos

print(f'Matriz identidade:\n{np.eye(5)}\n')
# Retorna uma matriz identidade, duas dimensões, quadrada, completa por 0s menos na diagonal principal que recebe 1s

print('\n', np.random.random(size=(3, 3, 3)), '\n')
# retorna valores aleatórios, pode ser usado para construir uma matriz de valores aleatórios

x2 = np.linspace(10, 120, 12)

print(f'primeiro elemento de x2:\n{x2[0]}\n') # Fatiamento de vetores
print(f'segundo elemento de x2:\n{x2[1]}\n')
print(f'ultimo elemento de x2:\n{x2[11]}\n')
print(f'-1 ultimo elemento de x2:\n{x2[-1]}\n')
print(f'dois primeiros elementos de x2:\n{x2[0:2]}\n')
print(f'dois primeiros elementos de x2:\n{x2[:2]}\n')
print(f'dois ultimos elementos de x2:\n{x2[-2:]}\n')
print(f'inversão de x2:\n{x2[::-1]}\n')

x2 = x2.reshape(2, 6)
print(f'\nX2 = \n{x2}\n')

print(f'Valor maximo de uma matriz: \n{x2.max()}\n')
print(f'Valor minimo de uma matriz: \n{x2.min()}\n')
print((f'Soma de todos os valores de uma matriz: \n{x2.sum()}\n'))
print(f'Média dos valores de uma matriz: \n{x2.mean()}\n')
print(f'Desvio padrão de uma matriz: \n{x2.std()}\n')
print(f'Mediana de uma matriz: \n{np.median(x2)}\n')


print(f'primeira linha, segunda coluna:\n{x2[0, 1]}\n') # Fatiamento de matrizes
print(f'segunda linha, penúltima colina:\n{x2[1, -2]}\n')
print(f'última linha, última coluna:\n{x2[1, 5]}\n')
print(f'última linha, última coluna:\n{x2[-1, -1]}\n')

print(f'primeira linha inteira: \n{x2[0, :]}\n')
print(f'primeira linha, segunda a quarta coluna: \n{x2[0, 1:4]}\n')
print(f'última coluna inteira: \n{x2[:, [-1]]}\n')

x3 = np.array([1, 2, 3]) # laços de arrays por objeto de memoria
print(f'X3 antes  sem o copy():', x3)
y3 = x3
x4 = x3.copy()
y3[0] = y3[2] = 5
print(f'X3 depois sem o copy():', x3)
print(f'X3 depois com o copy():', x4, '\n')

# Operaçoes aritméticas no numpy, sobrecarga de operador, elemento a elemento

x5 = np.ones([2, 2])
x6 = np.eye(2)

print('X5: \n', x5, '\n')
print('X6: \n', x6, '\n')

print(f'soma de dois arrays: \n{x5 + x6}\n') # ou np.add()
print(f'soma de arrays com broadcasting: \n{x5 + 6}\n')
print(f'subtração de dois arrays: \n{x5 - x6}\n') # ou np.subtract()
print(f'subtração de arrays com broadcasting: \n{x5 - 6}\n')
print(f'multiplicação de dois arrays: \n{x5 * x6}\n') # ou np.multiply()
print(f'multiplicação de arrays com broadcasting: \n{x5 * 6}\n')
print(f'divisão de dois arrays: \n{x5 / x5}\n') # ou np.divide()
print(f'divisão de arrays com broadcasting: \n{x5 / 6}\n')


x_random = 100 * np.random.random([10, 10])
# Matriz 10 x 10 aleatória com valores entre 0 e 100
print(x_random, '\n')

print(np.linalg.inv(x_random), '\n') # Retorna a matriz inversa.

print(x5 == x6, '\n') # ComparaçÕes entre arrays
print(x5 >= x6, '\n')
print(x5 < x6, '\n')

x_cond = x5 == x6 # Indexação de array para filtrar valores True.
x_impar: bool = x5 % 2 == 1
print(x5[x_cond], '\n')
print(x5[x_impar], '\n') # Retorna nomente os valores impares da matriz

print(x_random.reshape(4, 5, 5), '\n') # Exemplo de reshape para modificar formato de arrays
print(x_random.reshape(4, 5, 5).T, '\n') # Transposição de matriz, Troca linhas por colunas e vice versa

print(np.sum(x5, 0,), '\n') # soma da valores de uma matriz pelo numpy e capturando apelas a primeira linha

print(x_random, '\n') # where() retorna os indices da matriz onde a condição foi satisfeita
where_exe = x_random >= 90
where_return_1, where_return_2 = np.where(where_exe)
print(where_return_1,'\n', where_return_2, '\n')


