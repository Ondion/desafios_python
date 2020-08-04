# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá
# perguntar se o usuário quer ou não continuar. no final mostre:
# Quantas pessoas tem mais de 18 anos. Quantos homens foram cadastrados. Quantas mulheres tem menos de 20 anos.

print('===== DESAFIO 69 =====\n')

soma_pessoas = soma_idade = soma_f_idade = soma_sexo = 0

while True:
    sexo = input('Qual o sexo? <M> ou <F> ').lower()
    if sexo != 'm' and sexo != 'f':
        print('Entrada incorreta! <M> ou <F>! Reiniciando....')
        continue
    idade = input('Qual à idade? ')
    if not idade.isnumeric():
        print('Entrada incorreta! Apenas números positivos! Reiniciando....')
        continue
    elif int(idade) <= 0:
        print('Entrada incorreta! Apenas números positivos! Reiniciando....')
        continue
    if int(idade) >= 18:
        soma_idade += 1
    if sexo == 'm':
        soma_sexo += 1
    if sexo == 'f' and int(idade) < 20:
        soma_f_idade += 1
    soma_pessoas += 1
    if input('Você deseja continuar? <S> ou <N> ').lower() == 'n':
        print(f'Pessoas passadas: {soma_pessoas}, mais de 18: {soma_idade}, homens: {soma_sexo}, mulheres: {soma_f_idade} ')
        break
