 # Faça um programa que leia uma frase pelo teclado e mostre:
 # Quantas vezes aparece a letra 'A'.
 # Em que posição ela aparece a primeira vez.
 # Em que posição ela aparece a última vez.

print('===== DESAFIO 26 =====\n')

frase = str(input('Digite uma frase qualquer: ')).lower().strip()

print(f'Quantas vezes aparece a letra "A": {frase.count("a")}')
print(f'Em que posição ela aparece a primera vez: {frase.find("a")}')
print(f'Em que posição ela aparece a última vez: {frase.rfind("a")}')
