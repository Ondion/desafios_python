# Desenvolva um programa que leia as duas noteas de um aluno, calcule e mostre a sua média.


print('===== DESAFIO 07 =====\n')

nota_1 = int(input('Digite a nota do aluno: '))     # recebendo os valores para calculo
nota_2 = int(input('Digite a outra nota: '))
nota_3 = int(input('Digite a outra nota: '))

if min(nota_1, nota_2, nota_3) == nota_1:       # condicional para verificação da menor nota para descarte
    print(f'A média, ignorando a menor nota, é {(nota_2 + nota_3) / 2}')
elif min(nota_1, nota_2, nota_3) == nota_2:
    print(f'A média, ignorando a menor nota, é {(nota_1 + nota_3) / 2}')
else:
    print(f'A média, ignorando a menor nota, é {(nota_1 + nota_2) / 2}')
