# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade, Qual é o nome do homem mais velho, Quantas mulheres tem menos de 20 anos.


print('===== \033[1;33mDESAFIO 56\033[m =====\n')

media = homem = i_homem = mulheres = 0
for range in range(0, 4):
    nome = str(input('\nNome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M] - [F] ')).lower()

    media += idade
    if sexo == 'm' and idade > i_homem:
        homem = nome
        i_homem = idade
    if sexo == 'f' and idade < 20:
        mulheres += 1

print(f'\nMédia de idade: {media / 4}'
      f'\nHomem mais velho: {homem} e tem {i_homem} anos'
      f'\nMulheres menos de 20: {mulheres}')
