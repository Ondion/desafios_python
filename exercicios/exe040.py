# Crie um prgrama que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
# média atingida. Média abaixo de 5: Reprovado. Média entre 5 e 6.9: Recuperação. Média 7 ou superior: Aprovado.


print('\033[1;36m===== DESAFIO 40 =====\033[m\n')

nota_a = float(input('Digite o valor da primeira nota: '))
nota_b = float(input('Digite o valor da segunda nota: '))

if (nota_a + nota_b) / 2  < 5:
    print((nota_a + nota_b) / 2, 'de média você foi \033[1;31mReprovado!\033[m')
elif (nota_a + nota_b) / 2 >=5 and (nota_a + nota_b) / 2 < 7:
    print((nota_a + nota_b) / 2, 'de média você está de \033[1;33mRecuperação!\033[m')
else:
    print((nota_a + nota_b) / 2, 'de média você foi \033[1;32mAprovado!\033[m')
