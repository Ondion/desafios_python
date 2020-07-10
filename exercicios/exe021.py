# Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.

print('===== DESAFIO 21 =====\n')
from pygame import mixer        # Importanto um módulo de criação multimídia para uso de saida de áudio

mixer.init()        # Realizando a leitura e execução do arquivo mp3
mixer.music.load('exe021.mp3')
mixer.music.play()

input('Aperte qualquer tecla para parar.')      # Gatilho para encerrar o programa
