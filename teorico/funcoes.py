def func_1(): # função sem argumentos ou parametros
    print('Exemplo de função!')

print(func_1()) # retorna 'None', pois a função não tem retorno (dentro do print)

def func_2(x, y): # recebendo dois argumentos
    return x * y # essa função retorna a multiplicação dos argumentos

def func_3(x, y): # essa função retorna a pontecia do primeiro parametro pelo segundo
    return x**y

func_2(y = 4, x = 8) # é possivel especificar as variaveis no momento de chamar a função

def func_4 (*z): # o * nos deixa especificar um número ilimitado de argumentos, porém apelas um campo pode fazer usso desse método
    for i in z:
        print(i, end=' ')
    return '=', z

print(func_4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
