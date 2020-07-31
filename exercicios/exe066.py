# Crie um programa que leia varios números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
# (desconsiderando o flag)

print('===== DESAFIO 66 =====\n')

soma = contador = 0
while True:
    interio = int(input('Digite o número a ser somado, <999> para sair: '))
    if interio == 999:
        print(f'Foram digitados {contador} valores e a soma total é: {soma}')
        break
    contador += 1
    soma += interio
