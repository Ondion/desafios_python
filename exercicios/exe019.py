# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome do escolhido.

print('===== DESAFIO 19 =====\n')
from random import choice      # impotando a bibliotéca para gerar inteiros aleatórios

aluno01 = str(input('Digite o nome do primeiro aluno: '))       #Lendo os nomes dos alunos
aluno02 = str(input('Digite o nome do segundo aluno: '))
aluno03 = str(input('Digite o nome do terceiro aluno: '))
aluno04 = str(input('Digite o nome do quarto aluno: '))

print(f'O aluno escolhido: {choice([aluno01, aluno02, aluno03, aluno04])}')     # Realizando o sorteio por string
