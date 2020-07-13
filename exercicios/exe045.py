# Faça um programa que faça o computador jogar jokenpô com você.


print('===== DESAFIO 45 =====\n')
from random import randint

while True: # Treinamento de condiçoes alinhadas.
    sorteio = randint(1, 3)
    jogador = int(input('Escolha:\n[1]\033[1;31mPEDRA\033[m\n[2]\033[1;32mPAPEL\033[m\n'
                        '[3]\033[1;34mTESOURA\033[m\n[0]\033[1;33mSAIR\033[m\n'))
    if jogador == 1:
        if sorteio == 1:
            print('\nEMPATE! JOGADOR > \033[1;31mPEDRA\033[m VS \033[1;31mPEDRA\033[m < PC\n')
        elif sorteio == 2:
            print('\nDERROTA! JOGADOR > \033[1;31mPEDRA\033[m VS \033[1;32mPAPEL\033[m < PC\n')
        else:
            print('\nVITÓRIA! JOGADOR > \033[1;31mPEDRA\033[m VS \033[1;34mTESOURA\033[m < PC\n')

    elif jogador == 2:
        if sorteio == 1:
            print('\nVITÓRIA! JOGADOR > \033[1;32mPAPEL\033[m VS \033[1;31mPEDRA\033[m < PC\n')
        elif sorteio == 2:
            print('\nEMPATE! JOGADOR > \033[1;32mPAPEL\033[m VS \033[1;32mPAPEL\033[m < PC\n')
        else:
            print('\nDERROTA! JOGADOR > \033[1;32mPAPEL\033[m VS \033[1;34mTESOURA\033[m < PC\n')

    elif jogador == 3:
        if sorteio == 1:
            print('\nDERROTA! JOGADOR > \033[1;34mTESOURA\033[m VS \033[1;31mPEDRA\033[m < PC\n')
        elif sorteio == 2:
            print('\nVITÓRIA! JOGADOR > \033[1;34mTESOURA\033[m VS \033[1;32mPAPEL\033[m < PC\n')
        else:
            print('\nEMPATE! JOGADOR > \033[1;34mTESOURA\033[m VS \033[1;34mTESOURA\033[m < PC\n')

    elif jogador == 0:
        print('\nFINALIZANDO O PROGRAMA...\n')
        break
    else:
        print('\nOpção invalida... Tente novamente.\n')
