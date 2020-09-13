from random import randint

parada = 0
while True:
    if randint(1, 10) % 2 == 0:
        parada += randint(1, 4)
        print(f'parada atual {parada} \n')
    else:
        parada -= randint(1,4)
        print(f'parada atual {parada} \n')
    if parada == 1000:
        break

