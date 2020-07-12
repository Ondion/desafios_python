# Escreva um programa que leia um número inteiro qualquer e peça para o asuário escolher qual será a base de conversão.
# 1 para binário, 2 para octal e 3 para hexadecimal.


print('===== \033[1;33;40mDESAFIO 37\033[m =====\n')

numero = int(input('Digite o numero que você quer converter: '))
escolha = int(input('Agora escolha qual a conversão:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n:'))
if escolha == 1:
    print('O valor Binário é:', bin(numero)[2:])        # Relizando a conversão direta de bases númericas
elif escolha == 2:
    print('O valor em Octal é:', oct(numero)[2:])
elif escolha == 3:
    print('O valor em hexadecimal é:', hex(numero)[2:])
else:
    print('Opção invalida, execute novamente o programa.')
