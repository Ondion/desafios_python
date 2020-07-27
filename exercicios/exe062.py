# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
# ele disser que quer mostrar 0 termos.

print('===== DESAFIO 62 =====\n')

p_termo = int(input('primeiro termo: '))
razao = int(input('razão: '))
contador = 0

while True:
    print(f'{p_termo}',  end=', ') # formatação das saidas de dados
    p_termo += razao
    contador +=1
    if contador == 10:
        parada = int(input('\nQuantas PA mais você quer ver? Digite 0 para sair!'))
        if parada == 0:
            break
        else:
            contador = contador - parada # usando o fator de parada para realizar o calculo dos novos loops
