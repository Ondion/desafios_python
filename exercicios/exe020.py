# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada.

print('===== DESAFIO 20 =====\n')
from random import shuffle      # Importanto a bibliotéca de aleatoriedade

aluno01 = str(input('Digite o nome do primeiro aluno: '))       # Lendo os nomes dos alunos
aluno02 = str(input('Digite o nome do segundo aluno: '))
aluno03 = str(input('Digite o nome do terceiro aluno: '))
aluno04 = str(input('Digite o nome do quarto aluno: '))
lista = [aluno01, aluno02, aluno03, aluno04]        # Gerando uma lista para usar o shuffle
shuffle(lista)      # Realizando o sorteio pela lista

print('Segue a ordem de apresentação: ', lista)
