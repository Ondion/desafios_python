# Refaça o desaafio 35 dos triângulos, acrescentando o recurso de mostrar que tipp de triângulo será formado:
# Equilátero: Todos os lados iguais, Isúsceles: Dois lados iguais, Escaleno: Todos os lados diferentes.

print('\033[1;33;44m===== DESAFIO 42 =====\033[m\n')

reta_a = float(input('Digite o tamanho da reta 1: '))
reta_b = float(input('Digite o tamanho da reta 2: '))
reta_c = float(input('Digite o tamanho da reta 3: '))

if reta_a + reta_b > reta_c and reta_a + reta_c > reta_b and reta_c + reta_b > reta_a:
    if reta_a == reta_b == reta_c:
        print('Triângulo Equilátero, todos os lados iguais!')
    elif reta_a == reta_b or reta_a == reta_c or reta_b == reta_c:
        print('Triângulo Isúsceles, dois lados iguais')
    else:
        print('Triângulo Escoleno, Nenhum lado igual')

else:
    print('As medidas NÃO podem formar um triângulo')
