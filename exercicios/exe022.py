 # Crie um programa que leia o nome completo de uma pessoa e mostre:
 # O nome com todas as letras maiúsculas.
 # O nome com todas as letras minúsculas.
 # Quantas letras ao todo (sem considerar espaços).
 # Quantas letras tem o primeiro nome.

print('===== DESAFIO 22 =====\n')

nome = str(input('Qual o seu nome? ')).strip()      # entrada do nome em formato string

print(f'O nome com todas as letras maiúsculas é {nome.upper()}')
print(f'O nome com todas as letras minúsculas é {nome.lower()}')
print(f'Quantas letras ao todo sem considerar espaços é {len("".join(nome.split()))}')      # retirando os espaços
# entre as palavras para depois unir novamamente sem eles, gerando o len total sem espaços
print(f'Quanta letras tem o primeiro nome é: {len(nome.split()[0])}') # usando o len após quebrar a string para
# localizar a primeira palavra
