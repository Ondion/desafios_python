# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


print('===== DESAFIO 52 =====\n')


primo = 1
local = 1
while True:     # programa que gera números primos infinitamente.
    if primo % 2 == 1:
        for local in range(2, primo):
            if primo % local == 0:
                break
        if primo == local + 1:
            print(primo)


    primo += 1
